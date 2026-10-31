// Render an HTML ad layout to PNG at exact feed size (default 1080x1350, 4:5).
// usage: node ads/compose/render.js <in.html> <out.png> [width] [height]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out, w = 1080, h = 1350] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(inp), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: out, clip: { x: 0, y: 0, width: +w, height: +h } });
  await browser.close();
})();
