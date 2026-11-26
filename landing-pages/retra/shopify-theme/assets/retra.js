/* Retra theme behaviour: gallery, colour swatches, AJAX cart + slide-out cart,
   sticky offer bar, review carousel, read-more toggles, mobile menu. */
(function () {
  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  /* ---------- mobile menu ---------- */
  var menuBtn = $('#menu-btn');
  if (menuBtn) menuBtn.addEventListener('click', function () {
    var o = document.body.classList.toggle('nav-open');
    menuBtn.setAttribute('aria-expanded', o);
  });
  $$('#main-nav a').forEach(function (a) { a.addEventListener('click', function () { document.body.classList.remove('nav-open'); if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false'); }); });

  /* ---------- read more (guarantee paragraph, review cards) ---------- */
  $$('.more[data-for]').forEach(function (b) {
    b.addEventListener('click', function () {
      var p = document.getElementById(b.dataset.for); if (!p) return;
      var open = p.classList.toggle('open');
      b.setAttribute('aria-expanded', open);
      b.firstChild.textContent = (open ? b.dataset.less : b.dataset.more) + ' ';
    });
  });
  $$('.rcard .rm').forEach(function (b) {
    b.addEventListener('click', function () {
      var q = b.previousElementSibling; var o = q.classList.toggle('open');
      b.textContent = o ? b.dataset.less : b.dataset.more;
      b.setAttribute('aria-expanded', o);
    });
  });

  /* ---------- review carousel ---------- */
  $$('[data-rv]').forEach(function (sec) {
    var tr = $('.track', sec), barEl = $('.progress i', sec);
    if (!tr) return;
    function bar() {
      if (!barEl) return;
      var max = tr.scrollWidth - tr.clientWidth; var w = tr.clientWidth / tr.scrollWidth * 100;
      barEl.style.width = w + '%'; barEl.style.left = (max > 0 ? tr.scrollLeft / max * (100 - w) : 0) + '%';
    }
    tr.addEventListener('scroll', bar, { passive: true }); window.addEventListener('resize', bar); bar();
    var p = $('.arrows .prev', sec), n = $('.arrows .next', sec);
    if (p) p.addEventListener('click', function () { tr.scrollBy({ left: -tr.clientWidth * .8, behavior: 'smooth' }); });
    if (n) n.addEventListener('click', function () { tr.scrollBy({ left: tr.clientWidth * .8, behavior: 'smooth' }); });
  });

  /* ---------- buy box: gallery + swatches ---------- */
  $$('[data-buybox]').forEach(function (box) {
    var stage = $('.stage img', box);
    var thumbs = $$('.thumbs button', box);
    var cur = 0;
    function show(i) {
      if (!thumbs.length) return;
      cur = (i + thumbs.length) % thumbs.length;
      var t = thumbs[cur];
      stage.src = t.dataset.full; stage.srcset = t.dataset.srcset || ''; stage.alt = t.dataset.alt || '';
      thumbs.forEach(function (x) { x.removeAttribute('aria-current'); });
      t.setAttribute('aria-current', 'true');
    }
    thumbs.forEach(function (b, i) { b.addEventListener('click', function () { show(i); }); });
    var prev = $('[data-prev]', box), next = $('[data-next]', box);
    if (prev) prev.addEventListener('click', function () { show(cur - 1); });
    if (next) next.addEventListener('click', function () { show(cur + 1); });

    var sw = $('.swatches', box);
    var idInput = $('input[name="id"]', box);
    var colorName = $('[data-color-name]', box);
    var stickyImg = $('#sticky-img');
    if (sw) sw.addEventListener('change', function (e) {
      var r = e.target; if (!r.dataset.variant) return;
      if (idInput) idInput.value = r.dataset.variant;
      if (colorName) colorName.textContent = r.value;
      var t0 = thumbs[0];
      if (t0 && r.dataset.full) {
        t0.dataset.full = r.dataset.full; t0.dataset.srcset = r.dataset.srcset; t0.dataset.alt = r.dataset.alt;
        var ti = $('img', t0); if (ti) { ti.src = r.dataset.thumb; ti.alt = r.dataset.alt; }
        show(0);
      }
      if (stickyImg && r.dataset.thumb) stickyImg.src = r.dataset.thumb;
      try { var u = new URL(location.href); u.searchParams.set('variant', r.dataset.variant); history.replaceState(null, '', u); } catch (err) {}
    });
  });

  /* ---------- cart: Retra-Shots drawer (Shopify-rendered section), rewards gifts, upsells ---------- */
  var drawer = $('#cart-drawer');
  var countEls = $$('[data-cart-count]');
  var lastFocus = null;
  var SECTION = 'retra-cart-drawer';
  var rewards = [];
  try { rewards = JSON.parse(drawer ? drawer.getAttribute('data-rewards') || '[]' : '[]'); } catch (e) { rewards = []; }
  var busy = false;

  function setCount(n) { countEls.forEach(function (el) { el.textContent = n; el.setAttribute('data-count', n); }); }
  function getCart() { return fetch('/cart.js', { headers: { Accept: 'application/json' } }).then(function (r) { return r.json(); }); }
  function post(url, body) { return fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(body), retraOwn: true }); }

  /* Add or remove the free reward gifts so the cart matches the spend thresholds. */
  function syncRewards(cart) {
    if (!rewards.length) return Promise.resolve(cart);
    var spent = 0;
    cart.items.forEach(function (it) { if (!(it.properties && it.properties._reward)) spent += it.final_line_price; });
    var jobs = [];
    rewards.forEach(function (r) {
      if (!r.variant) return;
      var mine = cart.items.filter(function (it) { return it.properties && it.properties._reward === r.key; });
      var keep = mine.filter(function (it) { return it.variant_id === r.variant; })[0];
      /* the same gift already added free by another app (e.g. a Kaching bundle gift) covers this reward */
      var other = cart.items.some(function (it) { var pr = it.properties || {}; return !pr._reward && it.final_line_price === 0 && (it.variant_id === r.variant || it.variant_id === r.alt); });
      var want = spent >= r.threshold && !other;
      if (want && !keep) jobs.push(function () { return post('/cart/add.js', { items: [{ id: r.variant, quantity: 1, properties: { _reward: r.key } }] }); });
      mine.forEach(function (it) {
        if (!want || it !== keep) jobs.push(function () { return post('/cart/change.js', { id: it.key, quantity: 0 }); });
        else if (it.quantity !== 1) jobs.push(function () { return post('/cart/change.js', { id: it.key, quantity: 1 }); });
      });
    });
    if (!jobs.length) return Promise.resolve(cart);
    return jobs.reduce(function (p, job) { return p.then(job); }, Promise.resolve()).then(getCart);
  }

  function renderDrawer(html) {
    if (!drawer || !html) return;
    var doc = new DOMParser().parseFromString(html, 'text/html');
    var inner = doc.querySelector('[data-cart-inner]');
    var cur = $('[data-cart-inner]', drawer);
    if (inner && cur) { cur.innerHTML = inner.innerHTML; cur.setAttribute('data-count', inner.getAttribute('data-count')); setCount(inner.getAttribute('data-count')); }
    initCarousel();
  }
  function loadDrawer() {
    return fetch('/?sections=' + SECTION, { headers: { Accept: 'application/json' } }).then(function (r) { return r.json(); }).then(function (j) { renderDrawer(j[SECTION]); });
  }
  /* After any cart change: fix up the reward gifts, then re-render the drawer from Shopify. */
  function refresh() {
    busy = true;
    return getCart().then(syncRewards).then(loadDrawer).catch(function () {}).then(function () { busy = false; });
  }
  function openCart() {
    if (!drawer) { location.href = '/cart'; return; }
    if (drawer.hidden) lastFocus = document.activeElement;
    drawer.hidden = false; document.body.classList.add('cart-open');
    var x = $('.c-x', drawer); if (x) x.focus({ preventScroll: true });
  }
  function closeCart() {
    if (!drawer) return;
    drawer.hidden = true; document.body.classList.remove('cart-open');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function initCarousel() {
    if (!drawer) return;
    var car = $('[data-carousel]', drawer); if (!car) return;
    var track = $('.c-ups__track', car), dots = $('.c-ups__dots', car);
    var cards = $$('.c-card', track);
    if (!cards.length) { car.hidden = true; return; }
    dots.innerHTML = cards.map(function () { return '<i></i>'; }).join('');
    function update() {
      var w = cards[0].getBoundingClientRect().width + 12;
      var i = Math.round(track.scrollLeft / w);
      $$('i', dots).forEach(function (d, k) { d.classList.toggle('on', k === i); });
      var prev = $('[data-car="-1"]', car), next = $('[data-car="1"]', car);
      if (prev) prev.disabled = track.scrollLeft < 4;
      if (next) next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
    }
    track.addEventListener('scroll', update, { passive: true });
    update();
  }

  if (drawer) {
    drawer.addEventListener('click', function (e) {
      if (e.target.closest('[data-close-cart]')) { closeCart(); return; }
      var nav = e.target.closest('[data-car]');
      if (nav) { var tr = $('.c-ups__track', drawer); var c = $('.c-card', tr); tr.scrollBy({ left: Number(nav.dataset.car) * ((c ? c.getBoundingClientRect().width : 300) + 12), behavior: 'smooth' }); return; }
      var q = e.target.closest('button[data-q]');
      if (q) {
        var li = q.closest('.c-line'); li.classList.add('busy');
        post('/cart/change.js', { id: li.dataset.key, quantity: Number(q.dataset.q) }).then(refresh);
        return;
      }
      var add = e.target.closest('[data-upsell-add]');
      if (add) {
        var card = add.closest('.c-card'), sel = $('.c-card__sel', card);
        var id = add.dataset.variant || (sel && sel.value);
        if (!id) { sel.classList.add('err'); sel.focus(); return; }
        add.disabled = true; card.classList.add('busy');
        post('/cart/add.js', { items: [{ id: Number(id), quantity: 1 }] }).then(refresh);
      }
    });
    drawer.addEventListener('change', function (e) { if (e.target.classList.contains('c-card__sel')) e.target.classList.remove('err'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !drawer.hidden) closeCart(); });
    initCarousel();
  }

  /* Open the slide-out cart after any add to cart on the page, including Kaching's bundle adds. */
  if (window.fetch && drawer) {
    var nativeFetch = window.fetch;
    window.fetch = function (input, init) {
      var url = typeof input === 'string' ? input : (input && input.url) || '';
      var req = nativeFetch.apply(this, arguments);
      if (/\/cart\/add(\.js)?(\?|$)/.test(url) && !(init && init.retraOwn)) {
        req.then(function (r) { if (r.ok) setTimeout(function () { refresh().then(openCart); }, 150); }).catch(function () {});
      }
      return req;
    };
  }
  $$('[data-open-cart]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); openCart(); refresh(); }); });

  $$('form[data-retra-atc]').forEach(function (form) {
    var btn = $('button[type="submit"]', form);
    var status = $('[data-atc-status]', form);
    form.addEventListener('submit', function (e) {
      /* When the Kaching bundle picker is showing, Kaching adds the chosen bundle and gifts itself. */
      var kbox = form.closest('[data-kaching-on]'); if (kbox && kbox.querySelector('.kaching-bundles')) return;
      e.preventDefault();
      if (btn) btn.disabled = true;
      if (status) { status.textContent = ''; status.classList.remove('err'); status.classList.add('vh'); }
      fetch('/cart/add.js', { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form), retraOwn: true })
        .then(function (r) { if (!r.ok) throw new Error('add'); return r.json(); })
        .then(function () {
          if (status) status.textContent = form.dataset.added;
          if (btn) { var lab = $('[data-label]', btn); if (lab) { var orig = lab.textContent; lab.textContent = form.dataset.added; setTimeout(function () { lab.textContent = orig; }, 2400); } }
          return refresh().then(openCart);
        })
        .catch(function () {
          if (status) { status.textContent = form.dataset.error; status.classList.add('err'); status.classList.remove('vh'); }
        })
        .then(function () { if (btn) btn.disabled = false; });
    });
  });

  /* ---------- sticky offer bar: shows once the main button scrolls away; its button scrolls back to the offer ---------- */
  var sticky = $('#sticky-atc'), anchor = $('[data-sticky-anchor]');
  if (sticky && anchor) {
    var ticking = false;
    var stickyBtn = $('.cta', sticky);
    function check() {
      ticking = false;
      var r = anchor.getBoundingClientRect();
      var on = r.bottom < 0;
      if (sticky.classList.contains('on') !== on) {
        sticky.classList.toggle('on', on); sticky.setAttribute('aria-hidden', !on);
        if (stickyBtn) stickyBtn.tabIndex = on ? 0 : -1;
      }
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(check); } }, { passive: true });
    window.addEventListener('resize', check);
    check();
    if (stickyBtn) stickyBtn.addEventListener('click', function () {
      var target = document.getElementById(stickyBtn.getAttribute('href').replace('#', ''));
      if (target) setTimeout(function () { var f = target.querySelector('input:checked, input, button'); if (f) f.focus({ preventScroll: true }); }, 600);
    });
  }
})();

/* Mobile gallery: swipe the big photo to change it; keep the selected thumbnail in view. */
(function () {
  document.querySelectorAll('[data-buybox]').forEach(function (box) {
    var stage = box.querySelector('.stage'), row = box.querySelector('.thumbs');
    if (!stage || !row) return;
    var x0 = null, y0 = 0;
    stage.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
    stage.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0; x0 = null;
      if (Math.abs(dx) < 40 || Math.abs(dx) < Math.abs(dy)) return;
      var btn = box.querySelector(dx < 0 ? '[data-next]' : '[data-prev]'); if (btn) btn.click();
    }, { passive: true });
    new MutationObserver(function () {
      var t = row.querySelector('button[aria-current="true"]');
      if (t && row.scrollWidth > row.clientWidth) row.scrollTo({ left: t.offsetLeft - row.offsetLeft - (row.clientWidth - t.clientWidth) / 2, behavior: 'smooth' });
    }).observe(row, { subtree: true, attributes: true, attributeFilter: ['aria-current'] });
  });
})();

/* Cart drawer upsell colour photo: picking a colour shows that camera. */
document.addEventListener('change', function (e) {
  var sel = e.target;
  if (!sel.classList || !sel.classList.contains('c-card__sel')) return;
  var opt = sel.options[sel.selectedIndex], card = sel.closest('.c-card'), img = card && card.querySelector('.c-card__img img');
  if (img && opt && opt.dataset.img) { img.src = opt.dataset.img; img.removeAttribute('srcset'); }
});

/* Bundle picker: choose 1 camera or the 3-camera Buy 2, Get 1 FREE bundle (one colour per camera). */
(function () {
  document.querySelectorAll('[data-bundles]').forEach(function (bp) {
    var box = bp.closest('[data-buybox]');
    function sync() { bp.querySelectorAll('.b-opt').forEach(function (o) { o.classList.toggle('is-on', o.querySelector('input[name="retra-bundle"]').checked); }); }
    bp.addEventListener('change', function (e) { if (e.target.name === 'retra-bundle') sync(); });
    bp.addEventListener('click', function (e) {
      var o = e.target.closest('.b-opt'); if (!o || e.target.closest('select, .b-col')) return;
      var r = o.querySelector('input[name="retra-bundle"]'); if (!r.checked) { r.checked = true; sync(); }
    });
    var sw = box && box.querySelector('.swatches');
    if (sw) sw.addEventListener('change', function (e) { var v = e.target.dataset && e.target.dataset.variant; if (v) bp.querySelectorAll('.b-sel').forEach(function (s) { s.value = v; }); });
    sync();
  });
  /* The bundle adds 3 cameras in one request; the cart drawer opens on its own after any add. */
  document.addEventListener('submit', function (e) {
    var form = e.target;
    if (!form.matches || !form.matches('form[data-retra-atc]')) return;
    var box = form.closest('[data-buybox]'), bp = box && box.querySelector('[data-bundles]');
    if (!bp) return;
    var r = bp.querySelector('input[name="retra-bundle"]:checked'), n = r ? Number(r.value) : 1;
    if (n <= 1) return;
    e.preventDefault(); e.stopImmediatePropagation();
    var counts = {};
    Array.prototype.slice.call(r.closest('.b-opt').querySelectorAll('.b-sel'), 0, n).forEach(function (s) { counts[s.value] = (counts[s.value] || 0) + 1; });
    var items = Object.keys(counts).map(function (id) { return { id: Number(id), quantity: counts[id] }; });
    var btn = form.querySelector('button[type="submit"]'); if (btn) btn.disabled = true;
    fetch('/cart/add.js', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify({ items: items }) })
      .catch(function () {}).then(function () { if (btn) btn.disabled = false; });
  }, true);
})();
