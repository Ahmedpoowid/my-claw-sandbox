# QuantumBeat project video: narration script

There are two versions of the video, both 2:24 long:

- `QuantumBeat-Demo-voiceover.mp4` has an AI voiceover (Piper text-to-speech, "Joe" voice) reading lines almost identical to these. Use it as it is, or as a timing guide.
- `QuantumBeat-Demo.mp4` has captions but no voice. Use it if your team records its own voices with the script below.

Each block below starts at the time shown. The speaker split is only a suggestion, so swap it however your team likes.
Read at a calm pace, about the speed you'd use to explain something to a friend.

| Time | On screen | Speaker | What to say |
|---|---|---|---|
| 0:00 | Title | Saif | Hi, we're the QuantumBeat team from Applied Technology School, Al Ain. This is QuantumBeat, a contactless quantum heart monitor. |
| 0:08 | The problem | Saif | Heart disease is the world's leading cause of death: 17.9 million deaths in 2019. Rhythm problems come and go, so a short check-up can miss them. ECG needs electrodes on the skin, and SQUID scanners need extreme cooling. |
| 0:23 | The quantum science | Ahmed | Every heartbeat makes a tiny magnetic field. Our sensor reads it with quantum physics. Laser light lines up the spins of atoms in a vapour cell. Each heartbeat tilts the spins, the light shows how much, and our software checks the gap between beats. All at room temperature. |
| 0:43 | App demo | Mubarak | Here's our QuantumBeat app. It's a concept demo that uses synthetic heartbeat data, not a real patient. |
| 0:50 | Clicking *Run sample scan* | Mubarak | When we click Run sample scan, the app builds a thirty-second heartbeat signal and analyses it. |
| 0:56 | Zoom on the graph | Mubarak | In the graph, each sharp spike is one heartbeat, and the small wiggles in between are noise. |
| 1:03 | Zoom on the numbers | Mubarak | It calculates the average heart rate, 72 beats per minute, and measures 34 beat gaps between the beats. |
| 1:10 | Zoom on the result | Shaab | Then come the statistics: any gap with a z-score above 1.5 is flagged. In this sample, 3 gaps were flagged. |
| 1:19 | Result card | Shaab | A flag means a doctor should take a look. It's not a diagnosis. |
| 1:25 | The 5 steps | Shaab | Below the demo, the app explains our five steps: input, quantum sensor, process, statistics and output. |
| 1:30 | Development status | Shaab | And it shows where we are today: Technology Readiness Level 2. |
| 1:35 | Python simulation | Shaab | Behind the app is our Python simulation. Filtering cleans the noisy signal, then 30 beat gaps are measured. Three were flagged, and one was a false alarm, so we still need to tune it. |
| 1:48 | Three key features | Mohammed | QuantumBeat has three key features: contactless sensing, with no electrodes; smart noise filtering, for fewer false alarms; and a statistical early alert that flags unusual beats for a doctor. |
| 2:00 | Readiness (TRL 2) | Mohammed | We're at Technology Readiness Level 2: the sensor science is proven, but our tool is still a concept. Next: public ECG data, a lab partner, then medical testing. |
| 2:11 | Key message and credits | Mohammed | Our message: quantum sensing could make heart screening contactless, so problems are found earlier. Thank you for watching! |

## Adding your voices

1. Each speaker records their lines with a phone's voice recorder, in a quiet room.
2. Open `QuantumBeat-Demo.mp4` in a video editor that can add audio, for example Clipchamp on Windows, iMovie on a Mac or CapCut on a phone.
3. Drop each recording in at its start time from the table above, then export the video.

## Putting it on slide 16

Slide 16 asks for a video link and a QR code:

1. Upload the finished video somewhere the judges can open it, for example YouTube (set to *Unlisted*) or Google Drive / OneDrive with link sharing on.
2. Paste the link where it says *[Insert Project Video Link Here]*.
3. Make a QR code from the same link with any QR code generator, and put the image in the *Replace with video QR code* box.
