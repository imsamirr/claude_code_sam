// Renders each 1080x1080 slide in gallery.html to ../images/<id>.jpg
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1100, height: 1100 } });
  await p.goto('file://' + path.join(__dirname, 'gallery.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(1500);
  for (const el of await p.$$('.s')) {
    const id = await el.getAttribute('id');
    await el.screenshot({ path: path.join(__dirname, '..', 'images', id + '.jpg'), type: 'jpeg', quality: 86 });
    console.log('rendered', id);
  }
  await b.close();
})();
