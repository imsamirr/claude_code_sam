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

    const mockup = initMockup(root, gallery);

    // style cards -> hidden property + optional gallery jump
    $$('[data-sg-style]', root).forEach((card) => {
      const input = $('input', card);
      input.addEventListener('change', () => {
        $$('[data-sg-style]', root).forEach((c) => c.classList.toggle('is-selected', c === card));
        const slideIndex = parseInt(card.dataset.slide, 10);
        if (gallery && gallery.sgGo && !isNaN(slideIndex)) gallery.sgGo(slideIndex);
        if (mockup) mockup.styleChanged();
      });
    });

    // upload
    const drop = $('[data-sg-dropzone]', root);
    const buy = $('[data-sg-buy]', root);
    const preview = $('[data-sg-preview]', root);
    if (preview && drop) initPreview(root, preview, drop, buy);
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
        if (preview) {
          preview.hidden = false;
          setTimeout(() => preview.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 60);
        } else if (buy) {
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
    const frameIndex = product.options.findIndex((o) => /frame/i.test(o));
    const sizeIndex = product.options.findIndex((o, i) => i !== frameIndex && /size/i.test(o));
    const update = (initial) => {
      const selected = product.options.map((_, i) => {
        const checked = $(`input[data-option-index="${i}"]:checked`, form);
        return checked ? checked.value : null;
      });
      $$('.sg-option-group', form).forEach((group) => {
        const out = $('[data-sg-option-value]', group);
        const checked = $('input[data-option-index]:checked', group);
        if (out && checked) out.textContent = group.classList.contains('sg-option-group--size') ? checked.value.replace(/x/i, ' × ') : checked.value;
      });
      // size prices follow the selected frame
      if (frameIndex > -1 && sizeIndex > -1) {
        $$(`input[data-option-index="${sizeIndex}"]`, form).forEach((r) => {
          const v = product.variants.find((x) => x.options[sizeIndex] === r.value && x.options[frameIndex] === selected[frameIndex]);
          const out = $('[data-sg-size-price]', r.closest('label'));
          if (out) out.textContent = v ? formatMoney(v.price, moneyFormat).replace(/\.00(?!\d)/, '') : '';
        });
      }
      if (mockup && frameIndex > -1) {
        const frameInput = $(`input[data-option-index="${frameIndex}"]:checked`, form);
        mockup.setFrame(frameInput ? frameInput.dataset.frame : 'wrap', selected[frameIndex] || '', sizeIndex > -1 ? selected[sizeIndex] : '');
      }
      document.dispatchEvent(new CustomEvent('sg:variant', {
        detail: { frame: frameIndex > -1 ? selected[frameIndex] : null, size: sizeIndex > -1 ? selected[sizeIndex] : null }
      }));
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
      if (initial) return;
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
    $$('input[data-option-index]', form).forEach((r) => r.addEventListener('change', () => update()));
    update(true);

    form.addEventListener('submit', (e) => {
      const err = $('[data-sg-error]', root);
      const fileInput = drop ? $('input[type="file"]', drop) : null;
      if (fileInput && fileInput.required && !(fileInput.files && fileInput.files.length)) {
        e.preventDefault();
        if (err) { err.hidden = false; err.textContent = err.dataset.msg; }
        drop.scrollIntoView({ behavior: 'smooth', block: 'center' });
        return;
      }
      const previewId = $('[data-sg-preview-id]', root);
      if (preview && previewId && (previewId.disabled || (buy && buy.hidden))) {
        e.preventDefault();
        preview.scrollIntoView({ behavior: 'smooth', block: 'center' });
        return;
      }
      if (submit) { submit.disabled = true; submit.setAttribute('aria-busy', 'true'); }
    });
  }

  /* ---------- framed mockup (follows the Frame and Size options) ---------- */
  function parseSize(value) {
    const m = /(\d+(?:\.\d+)?)\s*[x×]\s*(\d+(?:\.\d+)?)/i.exec(value || '');
    return m ? { w: parseFloat(m[1]), h: parseFloat(m[2]) } : null;
  }

  function initMockup(root, gallery) {
    const el = $('[data-sg-mockup]', root);
    if (!el) return null;
    const img = $('[data-sg-mockup-img]', el);
    const blank = $('.sg-mockup__blank', el);
    const caption = $('[data-sg-mockup-caption]', el);
    const tag = $('[data-sg-mockup-tag]', el);
    const showBtn = $('[data-sg-mockup-show]', root);
    const previews = {};
    const currentStyle = () => {
      const c = $('[data-sg-style] input:checked', root);
      return c ? c.value : '';
    };
    const setArt = (src, isPreview) => {
      if (!src) return;
      img.src = src;
      img.hidden = false;
      if (blank) blank.hidden = true;
      tag.hidden = !isPreview;
    };
    const visible = (on) => {
      el.hidden = !on;
      if (showBtn) showBtn.hidden = on;
    };
    const styleChanged = () => {
      const style = currentStyle();
      if (previews[style]) { setArt(previews[style], true); visible(true); return; }
      const card = $('[data-sg-style] input:checked', root);
      const sample = card ? $('.sg-style__media img', card.closest('[data-sg-style]')) : null;
      if (sample) setArt(sample.currentSrc || sample.src, false);
      else tag.hidden = true;
    };
    // the largest size fills most of the wall; smaller ones shrink in proportion
    const setFrame = (key, frameName, sizeValue) => {
      el.dataset.frame = key || 'wrap';
      const size = parseSize(sizeValue);
      const sizes = $$('.sg-option-group--size input', root).map((r) => parseSize(r.value)).filter(Boolean);
      if (size) {
        const maxH = Math.max(...sizes.map((s) => s.h), size.h);
        el.style.setProperty('--ar', `${size.w} / ${size.h}`);
        el.style.setProperty('--scale', (0.56 + 0.3 * (size.h / maxH)).toFixed(3));
      }
      caption.textContent = [frameName, size ? `${size.w} × ${size.h} in` : sizeValue].filter(Boolean).join(' · ');
    };

    root.addEventListener('sg:preview', (e) => {
      const { url, style } = e.detail;
      if (!url) {
        Object.keys(previews).forEach((k) => delete previews[k]);
        styleChanged();
        return;
      }
      previews[style] = url;
      setArt(url, true);
      visible(true);
    });
    if (gallery) {
      $$('[data-sg-thumb], [data-sg-prev], [data-sg-next]', gallery).forEach((b) => b.addEventListener('click', () => visible(false)));
    }
    if (showBtn) showBtn.addEventListener('click', () => visible(true));
    styleChanged();
    return { setFrame, styleChanged };
  }

  /* ---------- AI preview (talks to the preview server) ---------- */
  // Downscale big phone photos before upload; falls back to the original file.
  async function shrinkPhoto(file, max = 2048) {
    try {
      if (!('createImageBitmap' in window)) return file;
      const bmp = await createImageBitmap(file, { imageOrientation: 'from-image' });
      const scale = Math.min(1, max / Math.max(bmp.width, bmp.height));
      if (scale === 1 && file.type === 'image/jpeg' && file.size < 4e6) return file;
      const canvas = document.createElement('canvas');
      canvas.width = Math.round(bmp.width * scale);
      canvas.height = Math.round(bmp.height * scale);
      canvas.getContext('2d').drawImage(bmp, 0, 0, canvas.width, canvas.height);
      const blob = await new Promise((ok) => canvas.toBlob(ok, 'image/jpeg', 0.9));
      return blob ? new File([blob], 'photo.jpg', { type: 'image/jpeg' }) : file;
    } catch (e) {
      return file;
    }
  }

  function initPreview(root, pv, drop, buy) {
    const btn = $('[data-sg-preview-btn]', pv);
    const label = $('[data-sg-preview-btn-label]', pv);
    const loading = $('[data-sg-preview-loading]', pv);
    const note = $('[data-sg-preview-note]', pv);
    const error = $('[data-sg-preview-error]', pv);
    const idInput = $('[data-sg-preview-id]', root);
    const urlInput = $('[data-sg-preview-url]', root);
    const result = $('[data-sg-result]', root);
    // with a framed mockup the preview is shown inside the frame instead
    const resultImg = $('[data-sg-result-img]', root) || new Image();
    const file = $('input[type="file"]', drop);
    let lastStyle = null;

    const currentStyle = () => {
      const c = $('[data-sg-style] input:checked', root);
      return c ? c.value : '';
    };
    const setLabel = () => {
      label.textContent = lastStyle === null ? pv.dataset.labelFirst : pv.dataset.labelAgain;
      const matches = lastStyle !== null && currentStyle() === lastStyle;
      btn.disabled = matches;
      // Only allow ordering the style that was actually previewed
      if (buy && lastStyle !== null) buy.hidden = !matches;
    };
    const reset = () => {
      lastStyle = null;
      idInput.value = ''; idInput.disabled = true;
      urlInput.value = ''; urlInput.disabled = true;
      if (result) result.hidden = true;
      root.dispatchEvent(new CustomEvent('sg:preview', { detail: { url: null } }));
      note.hidden = true; error.hidden = true;
      if (buy) buy.hidden = true;
      setLabel();
    };

    root.addEventListener('change', (e) => { if (e.target.closest('[data-sg-style]')) setLabel(); });
    file.addEventListener('change', reset);

    btn.addEventListener('click', async () => {
      const f = file.files && file.files[0];
      if (!f) { drop.scrollIntoView({ behavior: 'smooth', block: 'center' }); return; }
      btn.hidden = true; loading.hidden = false; error.hidden = true;
      const ctrl = new AbortController();
      const timer = setTimeout(() => ctrl.abort(), 150000);
      try {
        const fd = new FormData();
        fd.append('photo', await shrinkPhoto(f));
        fd.append('style', currentStyle());
        fd.append('category', pv.dataset.category || 'classic');
        const res = await fetch(pv.dataset.endpoint, { method: 'POST', body: fd, signal: ctrl.signal });
        const data = await res.json().catch(() => ({}));
        if (!res.ok || !data.previewUrl) throw new Error(data.message || 'Something went wrong. Please try again.');
        await new Promise((ok, bad) => { resultImg.onload = ok; resultImg.onerror = bad; resultImg.src = data.previewUrl; });
        if (result) result.hidden = false;
        idInput.value = data.id; idInput.disabled = false;
        urlInput.value = data.previewUrl; urlInput.disabled = false;
        lastStyle = currentStyle();
        root.dispatchEvent(new CustomEvent('sg:preview', { detail: { url: data.previewUrl, style: lastStyle } }));
        let msg = (pv.dataset.labelRemaining || '').replace('[count]', data.remaining);
        if (data.remaining === 1) msg = msg.replace('previews', 'preview');
        note.textContent = msg;
        note.hidden = !note.textContent;
        if (buy) buy.hidden = false;
        const shown = result || $('[data-sg-mockup]', root);
        const target = window.innerWidth < 990 && shown ? shown : buy || pv;
        setTimeout(() => target.scrollIntoView({ behavior: 'smooth', block: 'center' }), 80);
      } catch (e) {
        error.textContent = e.name === 'AbortError'
          ? 'This is taking longer than usual. Please try again.'
          : e instanceof TypeError
            ? "We couldn't reach our studio. Please check your connection and try again."
            : (e.message || 'Something went wrong. Please try again.');
        error.hidden = false;
      } finally {
        clearTimeout(timer);
        loading.hidden = true; btn.hidden = false;
        setLabel();
      }
    });
    setLabel();
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
