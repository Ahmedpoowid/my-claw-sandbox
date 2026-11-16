"""Build a narration track with Piper TTS and mux it into a video.

usage: python3 voiceover.py <lines.json> <voice.onnx> <video_in.mp4> <video_out.mp4>

lines.json: {"end": <seconds>, "lines": [[start_seconds, "text"], ...]}
Each line is synthesized, sped up a little (never below 0.88x length) if it would run
into the next line, placed at its start time, then the track is loudness-normalised
(-16 LUFS) and muxed as stereo AAC.
"""
import json
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np

GAP = 0.25          # minimum silence before the next line starts
MIN_SCALE = 0.88    # fastest allowed speaking rate (Piper length_scale)


def synth(text, model, out, length_scale):
    subprocess.run([sys.executable, "-m", "piper", "-m", str(model), "-f", str(out),
                    "--length-scale", f"{length_scale:.3f}", "--sentence-silence", "0.25"],
                   input=text.encode(), check=True, capture_output=True)
    with wave.open(str(out)) as w:
        sr = w.getframerate()
        data = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    # trim leading/trailing near-silence so placement is exact
    idx = np.where(np.abs(data) > 0.01)[0]
    if len(idx):
        data = data[max(0, idx[0] - int(.02 * sr)): idx[-1] + int(.08 * sr)]
    return data, sr


def main(lines_json, model, vin, vout):
    spec = json.loads(Path(lines_json).read_text())
    lines, end = spec["lines"], spec["end"]
    tmp = Path(tempfile.mkdtemp())
    track, sr = None, None
    report = []
    for i, (start, text) in enumerate(lines):
        nxt = lines[i + 1][0] if i + 1 < len(lines) else end
        avail = nxt - start - GAP
        scale = 1.0
        data, sr = synth(text, model, tmp / f"l{i}.wav", scale)
        dur = len(data) / sr
        for _ in range(4):  # speed fitting is not linear, so iterate
            if dur <= avail or scale <= MIN_SCALE:
                break
            scale = max(MIN_SCALE, scale * avail / dur * 0.985)
            data, sr = synth(text, model, tmp / f"l{i}.wav", scale)
            dur = len(data) / sr
        if track is None:
            track = np.zeros(int(end * sr) + sr, dtype=np.float32)
        s = int(start * sr)
        track[s:s + len(data)] += data[: len(track) - s]
        report.append((start, round(dur, 2), round(avail, 2), round(scale, 2), "OVERLAP" if dur > avail + .01 else "ok"))
    for r in report:
        print("%7.2fs  dur %5.2f  avail %5.2f  scale %.2f  %s" % r)
    raw = tmp / "voice.wav"
    with wave.open(str(raw), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(track, -1, 1) * 32767).astype(np.int16).tobytes())
    # gentle clean-up: high-pass, light compression, loudness normalisation, 48 kHz stereo
    af = "highpass=f=70,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=120,loudnorm=I=-16:TP=-1.5:LRA=7,aresample=48000"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(vin), "-i", str(raw),
                    "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-af", af, "-ac", "2",
                    "-c:a", "aac", "-b:a", "160k", "-t", str(end), "-movflags", "+faststart", str(vout)], check=True)
    print("wrote", vout)


if __name__ == "__main__":
    main(*sys.argv[1:5])
