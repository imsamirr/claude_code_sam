# Preview server — handoff

Status as of 2026-10-14: **built and tested locally in mock mode; not yet deployed.**
The next session needs the environment variables below, which only reach
sessions started after they were saved.

## What exists

- `preview-server/` — Cloudflare Worker (`src/index.js`), prompt catalogue
  (`src/prompts.js`), watermark tile (`src/assets/watermark.png`),
  `wrangler.toml`, `deploy.sh`.
- Theme changes in `portrait-theme/` (**not yet uploaded to Shopify**):
  - `sections/sg-hero-product.liquid` — "Create my free preview" button,
    loading state, result overlay in the gallery, hidden `_preview_id` and
    `Preview` order properties, new "AI preview" settings (preview is off
    while `preview_endpoint` is empty).
  - `assets/sg-theme.js` — preview request, client-side photo downscale,
    buy panel only shows for the style that was actually previewed.
  - `assets/sg-theme.css` — preview styles.
  - `snippets/sg-dawn-head.liquid` — loads Dawn's `search-form.js` (fixes
    "SearchForm is not defined" on cart/search pages).

Local mock test passed: upload → preview → style check → add to cart; the
cart line carried `Style`, `Photo`, `_preview_id` and `Preview`.

## Remaining steps

1. **Check the environment** — these must be set (values never printed):
   `DIVINE_GIFTS_OPENAI_API_KEY`, `CLOUDFLARE_API_TOKEN`,
   `CLOUDFLARE_ACCOUNT_ID`, `DIVINE_GIFTS_ADMIN_TOKEN`.
   Do **not** use `OPENAI_API_KEY` — it belongs to another project.
2. **Cloudflare plan** — image processing needs the Workers Paid plan
   ($5/month). If deploy fails on `cpu_ms`, that's why.
3. **Deploy** — `cd preview-server && ./deploy.sh`, then commit the KV id it
   writes into `wrangler.toml`. Note the `*.workers.dev` URL.
4. **Smoke test** — `GET /health`, then one real `POST /api/preview` (with
   `Origin: https://reclaimnutra.com`) using a photo the owner provides.
   Check identity is preserved and the watermark looks right.
   If the model name is rejected, update `OPENAI_IMAGE_MODEL` in
   `wrangler.toml` (and drop `OPENAI_INPUT_FIDELITY` if unsupported).
5. **Theme** — reconnect the Shopify connector. Upload the four files above
   **only to the unpublished theme "Copy of Art Portrait Theme (Saviors Gift
   layout)"** (`gid://shopify/OnlineStoreTheme/187124285658`); the live theme
   (`187106885850`) is write-protected. Compare checksums first in case the
   owner edited the copy in the editor. Set the `preview_endpoint` setting's
   schema default to `https://<worker>/api/preview` so every template picks
   it up, then test on
   `https://reclaimnutra.com/products/jesus-with-pets?preview_theme_id=187124285658`.
6. **Owner publishes** the copy when happy.

## Later phases (not built)

- **Print-resolution upscale** of `final/<id>.png` (OpenAI output is
  1024×1536; a 24×36″ print at 300 DPI needs ~7200×10800).
- **Order webhook** (`orders/paid`) → read `_preview_id` → upscale → send
  file + SKU + address to the 3PL (owner still to name the 3PL).
- Admin downloads today: `GET /admin/final/<id>` with
  `Authorization: Bearer <DIVINE_GIFTS_ADMIN_TOKEN>`.
- Optional: Cloudflare Turnstile on the preview button to stop bots burning
  OpenAI credit (the daily per-IP limit is the only guard right now).
