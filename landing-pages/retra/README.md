# Retra Screen-Free Camera: product landing page template

`index.html` is a self-contained product page (images in `images/`).

**Structure and branding: Retro-pia's product page, section for section.** Studied from
retro-pia.com/products/retropia-disposable-camera-lens:
- **Colours:** one paper ground (#FCFBF9) on every section, navy #022B49, blue-grey body text #416077.
- **Type:** small handwritten taupe kickers (#A39680); 48px Times headlines in two lines, one line navy and the other at 50% navy; Inter body text at 16–18px.
- **Buttons and photos:** slate-blue gradient pill buttons; photos as tilted white-bordered prints.
- **Section order:**
  1. Buy box: vertical thumbnails, rating, title and subtitle, navy checks, price with the Buy 1, Get 1 Free pill, a "Choose your color" step, Add to Cart, the payment banner, a returns note, accordions
  2. Four film looks: Klik's row of four filters, same scene
  3. How it works: Klik's four illustrated steps
  4. Three-column comparison (Retra / Disposable / Phone camera)
  5. Tilted review card carousel
  6. Made for real moments: Klik's photo grid
  7. Navy guarantee panel
  8. FAQ framed by photo collages
  9. Navy footer

Removed for now: the bundle selector, the Black Friday extras card, the explainer section, the bundle builder and the Instagram section.

The content (product facts, offer, product gallery images) follows KlikCamera.

## Copy

- **Announcement bar and marquee:** the user's line, "BLACK FRIDAY SALE - BUY 1, GET 1 FREE".
- **Page copy:** written by StefanBrain (chat `chat_50348e588b9d4d9595a63eb210f50971`). Sources: `copy/14-stefanbrain-v4-sections.md` for the filters, How it works and moments headlines, `copy/12-stefanbrain-v3-retropia-structure.md` for the section headlines and new slots, `copy/13-stefanbrain-v3-fixes.md` for replacement headlines (originals were too close to Retro-pia's own lines) and accessory bullets, and `copy/11` for the accordions and reviews.
- **Text on the product-gallery graphics:** Klik's own image text with the brand swapped to Retra, as the user asked. Edit it in `gallery-src/gallery.html` and run `node gallery-src/render.js` (needs Playwright) to regenerate `images/g1`–`g8`.
- **Earlier long-form drafts:** `copy/01`–`10` (superseded).

## Offer

The announcement bar and the price pill say "Buy 1, Get 1 Free". The bundle tiers were removed for now (the copy for them is still in `copy/12`).


## Images

All images were generated with **Nano Banana 2.1 (2K)** in Atria (project "Retra product page images").

- **Camera:** matches Klik's camera body detail for detail. Klik's own product photos were used only as design references; the photos themselves are new. The logo reads "Retra" in a gold classic serif, like Retro-pia's wordmark.
- **Lifestyle photos:** a consistent 35mm point-and-shoot film look. Natural muted colour, fine grain and candid people not facing the camera, which is what makes Klik's and Retro-pia's photos read as real.

**Files:**
- `g0-<colour>`: hero shot in 7 colourways; swaps with the colour picker.
- `g1`–`g8`: the gallery graphics (Klik's slots and text), set in Retro-pia's fonts. The source is in `gallery-src/`; re-render with `node gallery-src/render.js`.
- `fs-*`: one Cinque Terre scene in the 4 filters (made with `filters.py`).
- `how-1`–`how-4`: hand-drawn How it works illustrations.
- `m-*`: the Made for real moments grid.
- `rv-*`: review card photos.
- `payments.png`: the payment banner you supplied.

## Before this goes live

- **Placeholders (yellow on the page):** price, bundle totals, strap value, add-on prices, rating, review count, delivery times, support email. `g5` also has "[4.8]" in the image; set the real rating in `gallery.html` and re-render.
- **Reviews:** the 12 photo reviews, the buy-box quote and the `g5` quotes are SAMPLES written in Klik's style. They are not Klik's customers' reviews and not real Retra reviews. Replace them with real reviews (e.g. a Loox import) before running traffic.
- **Photos:** replace the generated product photos with real supplier photos of the unit.
- **Supplier check:** confirm the optical viewfinder, the filter control and the seven colours.
- **Wiring:** the buttons and forms are template-only.
