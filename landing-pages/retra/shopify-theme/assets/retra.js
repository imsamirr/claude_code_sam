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

  /* ---------- cart ---------- */
  var drawer = $('#cart-drawer');
  var countEls = $$('[data-cart-count]');
  var lastFocus = null;
  function money(cents) {
    var fmt = (window.RetraCart && RetraCart.moneyFormat) || '${{amount}}';
    var v = (cents / 100);
    var noDec = (cents % 100 === 0);
    return fmt.replace(/\{\{\s*(\w+)\s*\}\}/, function (m, k) {
      if (k === 'amount_no_decimals') return Math.round(v).toLocaleString('en-US');
      if (k === 'amount_with_comma_separator') return v.toFixed(2).replace('.', ',');
      return noDec ? v.toLocaleString('en-US') : v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    });
  }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function setCount(n) { countEls.forEach(function (el) { el.textContent = n; el.setAttribute('data-count', n); }); }
  function render(cart) {
    setCount(cart.item_count);
    if (!drawer) return;
    var list = $('.c-items', drawer), empty = $('.c-empty', drawer), foot = $('.c-foot', drawer);
    var L = drawer.dataset;
    if (!cart.items.length) { list.innerHTML = ''; empty.hidden = false; foot.hidden = true; return; }
    empty.hidden = true; foot.hidden = false;
    list.innerHTML = cart.items.map(function (it) {
      var img = it.image ? it.image + (it.image.indexOf('?') > -1 ? '&' : '?') + 'width=160' : '';
      var variant = it.variant_title && it.variant_title !== 'Default Title' ? '<div class="v">' + esc(it.variant_title) + '</div>' : '';
      var was = it.original_line_price > it.final_line_price ? '<s>' + money(it.original_line_price) + '</s>' : '';
      return '<li class="c-line" data-key="' + esc(it.key) + '">' +
        (img ? '<img src="' + esc(img) + '" alt="" width="72" height="72" loading="lazy">' : '<span></span>') +
        '<div><div class="t">' + esc(it.product_title) + '</div>' + variant +
        '<div class="c-qty"><button type="button" data-q="' + (it.quantity - 1) + '" aria-label="' + esc(L.dec) + '">−</button><span aria-live="polite">' + it.quantity + '</span><button type="button" data-q="' + (it.quantity + 1) + '" aria-label="' + esc(L.inc) + '">+</button></div>' +
        '<button type="button" class="c-rm" data-q="0">' + esc(L.remove) + '</button></div>' +
        '<div class="pr">' + money(it.final_line_price) + was + '</div></li>';
    }).join('');
    $('[data-subtotal]', drawer).textContent = money(cart.total_price);
  }
  function getCart() { return fetch('/cart.js', { headers: { Accept: 'application/json' } }).then(function (r) { return r.json(); }); }
  function openCart() {
    if (!drawer) { location.href = '/cart'; return; }
    lastFocus = document.activeElement;
    drawer.hidden = false; document.body.classList.add('cart-open');
    var x = $('.c-x', drawer); if (x) x.focus();
  }
  function closeCart() {
    if (!drawer) return;
    drawer.hidden = true; document.body.classList.remove('cart-open');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  if (drawer) {
    $$('[data-close-cart]', drawer).forEach(function (b) { b.addEventListener('click', closeCart); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !drawer.hidden) closeCart(); });
    $('.c-items', drawer).addEventListener('click', function (e) {
      var b = e.target.closest('button[data-q]'); if (!b) return;
      var li = b.closest('.c-line');
      li.classList.add('busy');
      fetch('/cart/change.js', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify({ id: li.dataset.key, quantity: Number(b.dataset.q) }) })
        .then(function (r) { return r.json(); }).then(render).catch(function () { li.classList.remove('busy'); });
    });
  }
  /* Open the slide-out cart after any add to cart on the page, including Kaching's bundle adds. */
  if (window.fetch && drawer) {
    var nativeFetch = window.fetch;
    window.fetch = function (input, init) {
      var url = typeof input === 'string' ? input : (input && input.url) || '';
      var req = nativeFetch.apply(this, arguments);
      if (/\/cart\/add(\.js)?(\?|$)/.test(url) && !(init && init.retraOwn)) {
        req.then(function (r) { if (r.ok) setTimeout(function () { getCart().then(render).then(openCart); }, 150); }).catch(function () {});
      }
      return req;
    };
  }
  $$('[data-open-cart]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); getCart().then(render).then(openCart).catch(openCart); }); });

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
        .then(function () { return getCart(); })
        .then(function (cart) {
          render(cart);
          if (status) status.textContent = form.dataset.added;
          if (btn) { var lab = $('[data-label]', btn); if (lab) { var orig = lab.textContent; lab.textContent = form.dataset.added; setTimeout(function () { lab.textContent = orig; }, 2400); } }
          openCart();
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
