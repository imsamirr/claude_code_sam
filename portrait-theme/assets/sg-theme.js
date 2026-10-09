/* Portrait theme interactions. No dependencies. */
(function () {
  'use strict';

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  /* ---------- menu drawer ---------- */
  function initDrawer() {
    const drawer = $('[data-sg-drawer]');
    if (!drawer) return;
    let lastFocus = null;
    const open = () => {
      lastFocus = document.activeElement;
      drawer.classList.add('is-open');
      drawer.setAttribute('aria-hidden', 'false');
      document.body.classList.add('sg-lock');
      $$('[data-sg-drawer-open]').forEach((b) => b.setAttribute('aria-expanded', 'true'));
      const first = $('[data-sg-drawer-close]', drawer);
      if (first) first.focus();
    };
    const close = () => {
      drawer.classList.remove('is-open');
      drawer.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('sg-lock');
      $$('[data-sg-drawer-open]').forEach((b) => b.setAttribute('aria-expanded', 'false'));
      if (lastFocus) lastFocus.focus();
    };
    $$('[data-sg-drawer-open]').forEach((b) => b.addEventListener('click', open));
    $$('[data-sg-drawer-close]', drawer).forEach((b) => b.addEventListener('click', close));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) close();
    });
  }

  /* ---------- product gallery ---------- */
  function initGallery(root) {
    const track = $('[data-sg-track]', root);
    if (!track) return;
    const slides = $$('[data-sg-slide]', root);
    const thumbs = $$('[data-sg-thumb]', root);
    const thumbTrack = $('[data-sg-thumb-track]', root);
    let index = 0;
    const go = (i) => {
      if (!slides.length) return;
      index = (i + slides.length) % slides.length;
      track.style.transform = `translateX(-${index * 100}%)`;
      thumbs.forEach((t, n) => t.setAttribute('aria-current', n === index ? 'true' : 'false'));
      const active = thumbs[index];
      if (active && thumbTrack) {
        const left = active.offsetLeft - thumbTrack.clientWidth / 2 + active.clientWidth / 2;
        thumbTrack.scrollTo({ left, behavior: 'smooth' });
      }
    };
    $$('[data-sg-prev]', root).forEach((b) => b.addEventListener('click', () => go(index - 1)));
    $$('[data-sg-next]', root).forEach((b) => b.addEventListener('click', () => go(index + 1)));
    thumbs.forEach((t, n) => t.addEventListener('click', () => go(n)));

    // swipe
    const vp = $('[data-sg-viewport]', root);
    if (vp) {
      let x0 = null;
      vp.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
      vp.addEventListener('touchend', (e) => {
        if (x0 === null) return;
        const dx = e.changedTouches[0].clientX - x0;
        if (Math.abs(dx) > 40) go(dx < 0 ? index + 1 : index - 1);
        x0 = null;
      });
    }
    root.sgGo = go;
    root.sgSlides = slides;
  }

  /* ---------- product builder (styles, upload, variants) ---------- */
  function formatMoney(cents, format) {
    const value = (cents / 100).toFixed(2);
    const noDec = Math.round(cents / 100).toString();
    const withComma = value.replace('.', ',');
    const thousands = (n) => n.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return (format || '${{amount}}').replace(/\{\{\s*(\w+)\s*\}\}/, (_, k) => {
      switch (k) {
        case 'amount_no_decimals': return thousands(noDec);
        case 'amount_with_comma_separator': return withComma;
        case 'amount_no_decimals_with_comma_separator': return noDec;
        default: return thousands(value.split('.')[0]) + '.' + value.split('.')[1];
      }
    });
  }

  function initBuilder(root) {
    const dataEl = $('[data-sg-product-json]', root);
    const product = dataEl ? JSON.parse(dataEl.textContent) : null;
    const form = $('form[data-sg-form]', root);
    const moneyFormat = root.dataset.moneyFormat;
    const gallery = $('[data-sg-gallery]', root);

    // style cards -> hidden property + optional gallery jump
    $$('[data-sg-style]', root).forEach((card) => {
      const input = $('input', card);
      input.addEventListener('change', () => {
        $$('[data-sg-style]', root).forEach((c) => c.classList.toggle('is-selected', c === card));
        const slideIndex = parseInt(card.dataset.slide, 10);
        if (gallery && gallery.sgGo && !isNaN(slideIndex)) gallery.sgGo(slideIndex);
      });
    });

    // upload
    const drop = $('[data-sg-dropzone]', root);
    const buy = $('[data-sg-buy]', root);
    if (drop) {
      const file = $('input[type="file"]', drop);
      const img = $('[data-sg-preview-img]', drop);
      const name = $('[data-sg-preview-name]', drop);
      const show = () => {
        const f = file.files && file.files[0];
        if (!f) { drop.classList.remove('has-file'); return; }
        drop.classList.add('has-file');
        if (name) name.textContent = f.name;
        if (img && f.type.indexOf('image') === 0) {
          const reader = new FileReader();
          reader.onload = (e) => { img.src = e.target.result; };
          reader.readAsDataURL(f);
        }
        if (buy) {
          buy.hidden = false;
          setTimeout(() => buy.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 60);
        }
      };
      file.addEventListener('change', show);
      ['dragenter', 'dragover'].forEach((ev) => drop.addEventListener(ev, () => drop.classList.add('is-dragover')));
      ['dragleave', 'drop'].forEach((ev) => drop.addEventListener(ev, () => drop.classList.remove('is-dragover')));
    }

    // scroll-to-upload buttons
    $$('[data-sg-scroll-upload]').forEach((b) => b.addEventListener('click', (e) => {
      const target = drop || $('[data-sg-buy]', root);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'center' });
      if (drop) setTimeout(() => $('input[type="file"]', drop).focus({ preventScroll: true }), 500);
    }));

    if (!product || !form) return;

    // variant resolution from option radios
    const idInput = $('input[name="id"]', form);
    const priceEl = $('[data-sg-price]', root);
    const submit = $('[data-sg-submit]', root);
    const submitLabel = submit ? $('[data-sg-submit-label]', submit) : null;
    const update = () => {
      const selected = product.options.map((_, i) => {
        const checked = $(`input[data-option-index="${i}"]:checked`, form);
        return checked ? checked.value : null;
      });
      const variant = product.variants.find((v) => v.options.every((o, i) => o === selected[i]));
      if (!variant) {
        if (submit) submit.disabled = true;
        if (submitLabel) submitLabel.textContent = submit.dataset.unavailable;
        return;
      }
      idInput.value = variant.id;
      if (priceEl) {
        const cmp = variant.compare_at_price && variant.compare_at_price > variant.price
          ? `<s>${formatMoney(variant.compare_at_price, moneyFormat)}</s>` : '';
        priceEl.innerHTML = cmp + formatMoney(variant.price, moneyFormat);
      }
      if (submit) {
        submit.disabled = !variant.available;
        if (submitLabel) submitLabel.textContent = variant.available ? submit.dataset.add : submit.dataset.soldOut;
      }
      if (variant.featured_media && gallery && gallery.sgGo) {
        const i = gallery.sgSlides.findIndex((s) => s.dataset.mediaId === String(variant.featured_media.id));
        if (i > -1) gallery.sgGo(i);
      }
      const url = new URL(window.location.href);
      if (document.body.dataset.template && document.body.dataset.template.indexOf('product') === 0) {
        url.searchParams.set('variant', variant.id);
        window.history.replaceState({}, '', url.toString());
      }
    };
    $$('input[data-option-index]', form).forEach((r) => r.addEventListener('change', update));

    form.addEventListener('submit', (e) => {
      const err = $('[data-sg-error]', root);
      const fileInput = drop ? $('input[type="file"]', drop) : null;
      if (fileInput && fileInput.required && !(fileInput.files && fileInput.files.length)) {
        e.preventDefault();
        if (err) { err.hidden = false; err.textContent = err.dataset.msg; }
        drop.scrollIntoView({ behavior: 'smooth', block: 'center' });
        return;
      }
      if (submit) { submit.disabled = true; submit.setAttribute('aria-busy', 'true'); }
    });
  }

  /* ---------- sticky mobile CTA ---------- */
  function initStickyCta() {
    const bar = $('[data-sg-sticky-cta]');
    const intro = $('[data-sg-hero-intro]');
    const upload = $('[data-sg-dropzone]') || $('[data-sg-buy]');
    if (!bar || !intro || !('IntersectionObserver' in window)) return;
    let introVisible = true;
    let uploadVisible = false;
    const sync = () => bar.classList.toggle('is-visible', !introVisible && !uploadVisible);
    new IntersectionObserver(([e]) => { introVisible = e.isIntersecting; sync(); }).observe(intro);
    if (upload) new IntersectionObserver(([e]) => { uploadVisible = e.isIntersecting || e.boundingClientRect.top < 0; sync(); }).observe(upload);
  }

  /* ---------- before / after sliders ---------- */
  function initCompare() {
    $$('[data-sg-compare]').forEach((el) => {
      if (el.dataset.sgInit) return;
      el.dataset.sgInit = '1';
      const range = $('input[type="range"]', el);
      const set = (v) => el.style.setProperty('--pos', v + '%');
      range.addEventListener('input', () => set(range.value));
      set(range.value);
    });
  }

  /* ---------- review read-more ---------- */
  function initReviews() {
    $$('[data-sg-review-text]').forEach((p) => {
      if (p.dataset.sgInit) return;
      p.dataset.sgInit = '1';
      const btn = p.parentElement.querySelector('[data-sg-review-more]');
      if (!btn) return;
      requestAnimationFrame(() => {
        if (p.scrollHeight - 2 <= p.clientHeight) { btn.hidden = true; return; }
        btn.hidden = false;
      });
      btn.addEventListener('click', () => {
        const clamped = p.classList.toggle('is-clamped');
        btn.textContent = clamped ? btn.dataset.more : btn.dataset.less;
      });
    });
  }

  /* ---------- reveal ---------- */
  function initReveal() {
    const els = $$('.sg-reveal');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) { els.forEach((e) => e.classList.add('is-in')); return; }
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -40px 0px' });
    els.forEach((e) => io.observe(e));
  }

  /* ---------- localization select ---------- */
  function initLocale() {
    $$('[data-sg-locale]').forEach((sel) => sel.addEventListener('change', () => sel.form.submit()));
  }

  function init(scope) {
    $$('[data-sg-gallery]', scope).forEach(initGallery);
    $$('[data-sg-builder]', scope).forEach(initBuilder);
  }

  document.addEventListener('DOMContentLoaded', () => {
    initDrawer();
    init(document);
    initStickyCta();
    initCompare();
    initReviews();
    initReveal();
    initLocale();
  });

  // theme editor support
  document.addEventListener('shopify:section:load', (e) => {
    init(e.target);
    initCompare();
    initReviews();
    if (e.target.querySelector('[data-sg-drawer]')) initDrawer();
    $$('.sg-reveal', e.target).forEach((el) => el.classList.add('is-in'));
  });
})();
