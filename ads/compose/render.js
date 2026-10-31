// Render an HTML ad layout to PNG at exact feed size (default 1080x1350, 4:5) and print a design lint report.
// usage: node ads/compose/render.js <in.html> <out.png> [width] [height]
// Lint (from brand.json production_method / SKILL.md "Design rules"): words on the ad, smallest text size,
// number of separate text blocks, text inside the 7% safe margin, and image coverage of the product.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out, w = 1080, h = 1350] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(inp), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: out, clip: { x: 0, y: 0, width: +w, height: +h } });
  const r = await page.evaluate(([W, H]) => {
    const mx = W * 0.07, my = H * 0.07, blocks = [], out = [];
    let words = 0, minFont = 999;
    for (const el of document.body.querySelectorAll('*')) {
      const own = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim());
      if (!own.length) continue;
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      const txt = own.map(n => n.textContent.trim()).join(' ');
      words += txt.split(/\s+/).filter(t => /[A-Za-z0-9$%]/.test(t)).length;
      minFont = Math.min(minFont, parseFloat(cs.fontSize));
      const rg = document.createRange(); rg.selectNodeContents(el); const b = rg.getBoundingClientRect();
      blocks.push(txt.slice(0, 30));
      if (b.left < mx - 1 || b.top < my - 1 || b.right > W - mx + 1 || b.bottom > H - my + 1) out.push(txt.slice(0, 40));
    }
    let img = 0;
    for (const i of document.images) { const b = i.getBoundingClientRect(); img = Math.max(img, b.width * b.height / (W * H)); }
    return { words, minFont, blocks: blocks.length, outside: out, productArea: Math.round(img * 100) };
  }, [+w, +h]);
  const warn = [];
  if (r.words > 30) warn.push(`too many words (${r.words} > 30)`);
  if (r.minFont < 26) warn.push(`text too small for 60+ readers (${r.minFont}px < 26px)`);
  if (r.blocks > 6) warn.push(`too many text blocks (${r.blocks} > 6)`);
  if (r.outside.length) warn.push(`text inside the 7% margin: ${r.outside.join(' | ')}`);
  console.log(`${path.basename(out)}: ${r.words} words, min text ${r.minFont}px, ${r.blocks} text blocks, largest image ${r.productArea}% of canvas` + (warn.length ? `\n  WARN ${warn.join('\n  WARN ')}` : '  OK'));
  await browser.close();
})();
