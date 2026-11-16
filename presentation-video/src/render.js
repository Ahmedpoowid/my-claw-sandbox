// Renders scene.html frame-by-frame with Playwright and encodes an MP4 with ffmpeg.
// Usage:
//   node render.js snap <outDir> <t1> <t2> ...     -> PNG stills at those times (seconds)
//   node render.js video <out.mp4> [workers=4] [fps=30]
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const HTML = 'file://' + path.join(__dirname, 'scene.html');

async function openPage(browser) {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  await page.goto(HTML);
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => window.init());
  if (errors.length) throw new Error('Page errors:\n' + errors.join('\n'));
  return { page, errors };
}

async function snap(outDir, times) {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const { page, errors } = await openPage(browser);
  for (const t of times) {
    await page.evaluate(t => window.renderAt(t), t);
    const f = path.join(outDir, `t${String(t).replace('.', '_')}.png`);
    await page.screenshot({ path: f });
    console.log(f);
  }
  if (errors.length) console.error('Errors:\n' + errors.join('\n'));
  await browser.close();
}

async function renderChunk(idx, f0, f1, fps, segPath) {
  const browser = await chromium.launch();
  const { page, errors } = await openPage(browser);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', String(fps), segPath], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise(r => ff.on('close', r));
  for (let f = f0; f < f1; f++) {
    await page.evaluate(t => window.renderAt(t), f / fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 94 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if ((f - f0) % 60 === 0) console.log(`[w${idx}] frame ${f - f0}/${f1 - f0}`);
  }
  ff.stdin.end();
  await done;
  await browser.close();
  if (errors.length) throw new Error(`worker ${idx} page errors:\n` + errors.join('\n'));
}

async function video(out, workers = 4, fps = 30) {
  const dur = 128;
  const total = Math.round(dur * fps);
  const tmp = fs.mkdtempSync(path.join(path.dirname(out), '.segs-'));
  const per = Math.ceil(total / workers);
  const jobs = [];
  for (let w = 0; w < workers; w++) {
    const f0 = w * per, f1 = Math.min(total, f0 + per);
    if (f0 >= f1) break;
    jobs.push(renderChunk(w, f0, f1, fps, path.join(tmp, `seg${w}.mp4`)));
  }
  await Promise.all(jobs);
  const list = path.join(tmp, 'list.txt');
  fs.writeFileSync(list, jobs.map((_, w) => `file 'seg${w}.mp4'`).join('\n'));
  const joined = path.join(tmp, 'joined.mp4');
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list, '-c', 'copy', joined]);
  // add a silent stereo track so every player/editor treats it as a normal video
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', joined, '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo',
    '-shortest', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', out]);
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('wrote', out);
}

const [mode, a, ...rest] = process.argv.slice(2);
(async () => {
  if (mode === 'snap') await snap(a, rest.map(Number));
  else if (mode === 'video') await video(path.resolve(a), Number(rest[0] || 4), Number(rest[1] || 30));
  else { console.error('usage: node render.js snap <dir> <t...> | video <out.mp4> [workers] [fps]'); process.exit(1); }
})().catch(e => { console.error(e); process.exit(1); });
