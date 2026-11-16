// Screenshots of the real QuantumBeat app in three states, for the in-deck interactive version.
// usage: node shots.js <QuantumBeat_App.html> <outDir>
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const INIT = `(function(){
  var s=1; window.__seed=function(v){s=v>>>0;};
  Math.random=function(){s|=0;s=s+0x6D2B79F5|0;var t=Math.imul(s^s>>>15,1|s);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};
  var timers=[],now=0,idc=1;
  window.setInterval=function(fn,ms){var id=idc++;timers.push({id:id,fn:fn,ms:ms,next:now+ms,rep:true});return id;};
  window.clearInterval=function(id){for(var i=0;i<timers.length;i++)if(timers[i].id===id){timers.splice(i,1);return;}};
  window.__advanceTo=function(target){for(;;){var nx=null;for(var i=0;i<timers.length;i++){var x=timers[i];if(x.next<=target&&(!nx||x.next<nx.next))nx=x;}if(!nx)break;now=nx.next;if(nx.rep)nx.next+=nx.ms;else timers.splice(timers.indexOf(nx),1);nx.fn();}if(target>now)now=target;};
})();`;

(async () => {
  const [app, out] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  // 1440x810 CSS px (16:9) at 8/3 scale -> 3840x2160 images
  const page = await browser.newPage({ viewport: { width: 1440, height: 810 }, deviceScaleFactor: 8 / 3 });
  await page.addInitScript(INIT);
  await page.goto('file://' + path.resolve(app));
  await page.addStyleTag({ content: '*{transition:none!important}' });
  await page.evaluate(() => document.fonts.ready);
  const btn = await page.locator('#scanBtn').boundingBox();
  await page.screenshot({ path: path.join(out, 'app-1-ready.jpg'), type: 'jpeg', quality: 90 });
  await page.evaluate(() => { window.__seed(6); document.getElementById('scanBtn').click(); window.__advanceTo(4 * 45 + 1); });
  await page.screenshot({ path: path.join(out, 'app-2-processing.jpg'), type: 'jpeg', quality: 90 });
  await page.evaluate(() => window.__advanceTo(2000));
  await page.screenshot({ path: path.join(out, 'app-3-result.jpg'), type: 'jpeg', quality: 90 });
  const result = await page.evaluate(() => ({ bpm: document.getElementById('bpm').textContent, gaps: document.getElementById('gaps').textContent, flagged: document.getElementById('flagged').textContent }));
  fs.writeFileSync(path.join(out, 'hotspot.json'), JSON.stringify({ viewport: [1440, 810], button: btn, result }, null, 1));
  console.log(JSON.stringify({ button: btn, result }));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
