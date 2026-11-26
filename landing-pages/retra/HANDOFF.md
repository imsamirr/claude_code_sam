# Retra landing page: handoff for a new session

Read this first, then `README.md` in this folder.

## Where things are

- **Branch:** `claude/inspiring-rubin-dx7oyi` in `imsamirr/claude_code_sam`. Everything below lives in `landing-pages/retra/` on that branch.
- **`index.html`:** the latest page (version 6). It's one self-contained HTML file (CSS and JS inline) that loads images from `images/`, so it's the source of truth. Edit it directly; nothing needs rebuilding.
- **Live preview:** the user's private artifact https://claude.ai/artifact/81Z9vQw1xrM8zWSk7GJodg. Republish to the same URL by passing it as `url` to the Artifact tool after a `read`.
- **`copy/`:** every line of page copy, written by StefanBrain (chat `chat_50348e588b9d4d9595a63eb210f50971`). The current page uses `11` (accordions, reviews), `12`/`13` (section headlines), `14` (filters, How it works, moments) and `15` (Four classic looks; Why Retra works). `01`–`10` are superseded drafts.
- **`gallery-src/`:** the source for the gallery graphics `g1`–`g8` (Klik's image text with the brand swapped, set in Retro-pia's fonts). Edit `gallery.html`, then run `node render.js` (needs Playwright).
- **`tools/kie.py`:** batch image generation on Kie.ai with Nano Banana Pro. Run it as `python3 tools/kie.py jobs.json OUTDIR`. The key is in env var `KIE_AI` on the "Sam's Default C-environment" cloud environment, so it needs no approvals. Kie sometimes returns "Internal Error"; rerunning skips finished images.
- **`tools/filters2.py`:** the Natural/Vintage/B&W/Film looks used on the filter photos.

## What the user asked for (the brief, as it evolved)

- **Product:** "Retra Screen-Free Camera". Same product, facts and claims as KlikCamera (klikcamera.com/products/klik-camera), but never Klik's wording.
- **Structure:** Klik's content and image slots, laid out on Retro-pia's section structure and branding (retro-pia.com/products/retropia-disposable-camera-lens).
- **Retro-pia branding:**
  - **Colours:** background #FCFBF9 on every section, navy #022B49, body text #416077.
  - **Type:** taupe handwritten kickers (#A39680) in Shantell Sans; two-line Times headlines at 48px with line 2 at 50% navy; Inter body text.
  - **Buttons and photos:** slate-blue gradient buttons (#2C4D63 → #8EA6B4); tilted white-bordered prints.
  - **Panels:** navy panels for the guarantee and the footer.
  - **Theme:** light only (no dark mode).
- **Camera:** must look EXACTLY like Klik's body: black top band, square viewfinder plus ribbed flash, pebbled leatherette, ribbed lens ring with a small lens, pill button. The logo reads "Retra" in a gold classic serif (Retro-pia style). There are 7 colours, Dune/Pine/Aegean/Sol/Blossom/Obsidian/Chalk, matching Klik's Brown/Green/Blue/Yellow/Pink/Black/White.
- **Offer:** announcement bar "BLACK FRIDAY SALE - BUY 1, GET 1 FREE" (the user's exact text). The bundle tiers and Black Friday extras card are removed for now.
- **Image quality:** must look like Klik's. Candid, real snapshots: ordinary people, subjects small or turned away, disposable-film colour, imperfect framing. Avoid glossy, posed "AI" images.
- **Mobile first:** the user said "the most important thing in ecommerce is mobile optimization".

### Page sections, in order

1. **Buy box:**
   - Vertical thumbnails and a 9-image gallery (Klik's slots).
   - Rating, then the name "Retra Screen-Free Camera" (no ™).
   - Klik-style icon badges, then the price with the BOGO pill.
   - "Almost sold out" with a pulsing green dot.
   - Colour swatches, Add to Cart, then the payment banner `payments.png` (supplied by the user).
   - The 30-day returns note.
   - Accordions: Product Details, Specs, Shipping & Returns, FAQ's.
2. Why Retra works: 6 hand-drawn icons.
3. Four classic looks: a different photo per filter, like Klik.
4. How it works: Klik-style, 4 illustrated steps.
5. Comparison: Retra / Disposable / Phone camera.
6. Review carousel: full photo, text below. These are 12 SAMPLE reviews.
7. Made for real moments: Klik grid (Europe, Theme parks, Beach, Road trips, Celebrations, Everyday).
8. Navy guarantee panel.
9. FAQ (also inside the buy-box accordion).
10. Navy footer.

**Mobile:** hamburger menu, sticky Add to Cart bar, 2×2 How it works, 3×2 icons, a comparison that fits the screen, one-row swatches, a two-column footer.

## Rules that still apply

- `CLAUDE.md`: StefanBrain writes every word of copy. Send it facts, not wording; send failing lines back with the reason.
- **Don't copy Klik's or Retro-pia's lines.** Four early headlines were near-copies of Retro-pia's and were rewritten.
- **No fake reviews.** The reviews are labelled samples and are not Klik's real reviews. Keep [RATING] and [REVIEW COUNT] as placeholders until real data exists.
- **No Disney names, rides or castle look-alikes.** Theme parks stay generic.
- **Placeholders (shown in yellow) still to fill:** price, compare price, rating, review count, delivery times, support email, brand entity.

## Likely next step: put it on the new Shopify store

The user connected a second Shopify store (not ComfortWear) for this. Approach:

1. Confirm the store with `get-shop-info`.
2. Create the product "Retra Screen-Free Camera" with 7 colour variants, using `images/g0-*.jpg` plus the gallery images.
3. Build a product template or sections that reproduce `index.html`. Shopify's theme tools and skills cover this; load the relevant skill first.
4. Wire Add to Cart and the forms to the real cart and email platform.
5. Ask the user for the price, offer mechanics and real reviews before going live.

## Shopify build (2026-11-25)

Live on **RECLAIM NUTRA** (reclaimnutra.com, ff0c5a-21.myshopify.com) as an **unpublished theme named "Retra"**
(`gid://shopify/OnlineStoreTheme/188991406298`, a copy of Dawn). The live K-Tube theme was not touched.
Preview: https://reclaimnutra.com/?preview_theme_id=188991406298

- **Product:** "Retra Screen-Free Camera", handle `retra-screen-free-camera`, Active, Online Store channel only.
  7 colour variants (Dune, Pine, Aegean, Sol, Blossom, Obsidian, Chalk), $99 / compare-at $200, SKUs `RETRA-<COLOUR>`,
  inventory not tracked. Each variant has its `g0-*` photo; `g1`–`g8` are the gallery. Template suffix `retra`.
- **Images:** all page images are in Shopify Files as `retra-*.{jpg,png}` (sections point at them with `shopify://shop_images/...`).
- **Theme source:** `shopify-theme/` in this folder. `layout/retra.liquid` (own header/footer, no Dawn chrome),
  `sections/retra-*.liquid` (one per page section, all copy editable in the theme editor), `assets/retra.css|js`,
  `templates/index.json` (home = the same page, product picked in the buy box) and `templates/product.retra.json`.
  `tools/build_templates.py` regenerates both templates from the copy. Upload changed files with `themeFilesUpsert`
  (body type URL, a raw.githubusercontent link pinned to the commit SHA). Note: the `theme_bash` sandbox keeps its
  first snapshot and does not see upserted files, so check the real preview link (Playwright) rather than `theme_screenshot`.
- **Behaviour:** colour swatches swap the photo, the variant and `?variant=`; Add to Cart posts to `/cart/add.js` and opens
  a slide-out cart (qty +/-, remove, Check Out); the sticky bar shows once the main button scrolls away on every screen size,
  and its "Claim BOGO Offer" button scrolls back to `#retra-cta` (the price row). Bundles go there later.
  The newsletter is a Shopify customer form tagged `newsletter,retra`.
- **Copy:** `copy/16-stefanbrain-shopify-slots.md` (StefanBrain) filled the last placeholders: shipping, contact page,
  newsletter without a discount, sticky and cart labels. Rating 4.8 / 1,753 is real (wholesale channel).
- **Still to do before ads:**
  - Buy 1, Get 1 Free is only text. No discount exists, so checkout charges full price for 2. Set up a BXGY automatic discount
    or the bundle selector.
  - The 12 review cards and the `g5` quotes are still SAMPLE reviews (labelled). Swap in the real wholesale reviews.
  - Publishing: the "Retra" theme replaces K-Tube for the whole store; the other products would use Dawn's default
    product template. Exit popup ("Mystery Discount") was dropped because no discount exists.

## Live theme and bundles (2026-11-26)
- Live theme: "Retra (bar update)" `gid://shopify/OnlineStoreTheme/189021028570`. The user renamed the logo to "Retra-Shots" and
  edited home-page offer text in the editor; keep editor settings when deploying (edit templates with sed, not full rewrites).
- Deploying to the live theme: `themeFilesUpsert` is blocked on live themes. Use `theme_bash` (this theme's sandbox is in sync)
  → `theme_commit` → `theme_publish` after the user says yes. The old "Retra" theme's sandbox is stale; don't use it.
- Announcement bar: countdown removed; offer tag setting is `offer_tag` (BUY 2, GET 1 FREE); bar styles live in the header section.
- Bundles: Kaching Bundles. Setup steps in KACHING-SETUP.md. Theme side: buy box has an `@app` block slot, `show_bundles` toggle,
  Kaching skin CSS, and a fetch hook that opens the slide-out cart after Kaching adds. Gift products: strap leash $29, leather bag $50.
- Still to verify once the deal exists: Add to Cart with each bar (bundle + gifts land in the cart, price $198 / $297).

## Brand rename to Retra-Shots (2026-11-26)
Brand is now **Retra-Shots** everywhere visitors see it (theme text, section defaults, footer, og:site_name, product titles,
vendor, descriptions, alt text). Handles and file names keep `retra-` so URLs and image references still work.
Favicon: images/retra-shots-favicon.png (Files: retra-shots-favicon.png), source brand/favicon.html.
The camera photos still show the old "Retra" logo printed on the body. The Shopify store name ("RECLAIM NUTRA") is changed by
the owner in Settings → Store details; there is no API for it.
