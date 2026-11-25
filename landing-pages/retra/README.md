# Retra Screen-Free Camera: product landing page template

`index.html` is a self-contained product page (images in `images/`).

**Structure and branding: Retro-pia's product page, section for section.** Studied from
retro-pia.com/products/retropia-disposable-camera-lens:
- **Colours:** one paper ground (#FCFBF9) on every section, navy #022B49, blue-grey body text #416077.
- **Type:** small handwritten taupe kickers (#A39680); 48px Times headlines in two lines, one line navy and the other at 50% navy; Inter body text at 16–18px.
- **Buttons and photos:** slate-blue gradient pill buttons; photos as tilted white-bordered prints.
- **Section order:**
  1. Buy box: vertical thumbnails, rating, title and subtitle, navy checks, price and pill, a numbered "Choose your color" step, a numbered "Choose your bundle" step, Add to Cart, a Black Friday extras card with a countdown, payment badges, a returns note, accordions with icons
  2. Explainer: kicker, two-line headline, paragraph with "Read more", a big photo, two tilted prints, features 01–03
  3. Before/after filter slider with tabs for each filter
  4. Three-column comparison (Retra / Disposable / Phone camera) with a price-dots row
  5. Tilted review card carousel
  6. Bundle builder (camera plus case, strap and card reader)
  7. Navy guarantee panel
  8. FAQ framed by photo collages
  9. Instagram grid
  10. Navy footer

The content (product facts, offer, product gallery images) follows KlikCamera.

## Copy

- **Announcement bar and marquee:** the user's line, "BLACK FRIDAY SALE - BUY 1, GET 1 FREE".
- **Page copy:** written by StefanBrain (chat `chat_50348e588b9d4d9595a63eb210f50971`). Sources: `copy/12-stefanbrain-v3-retropia-structure.md` for the section headlines and new slots, `copy/13-stefanbrain-v3-fixes.md` for replacement headlines (originals were too close to Retro-pia's own lines) and accessory bullets, and `copy/11` for the accordions and reviews.
- **Text on the product-gallery graphics:** Klik's own image text with the brand swapped to Retra, as the user asked. Edit it in `gallery-src/gallery.html` and run `node gallery-src/render.js` (needs Playwright) to regenerate `images/g1`–`g8`.
- **Earlier long-form drafts:** `copy/01`–`10` (superseded).

## Offer as built (confirm)

- **2x cameras:** Buy 1, Get 1 Free (most popular).
- **4x cameras:** Buy 2, Get 2 Free (best value).
- **6x cameras:** Buy 3, Get 3 Free.

All three tiers include free shipping, a free wrist strap per camera, and a free Christmas gift ribbon with every camera.

## Images (all AI-generated mockups of the Klik-style body: black top, coloured leatherette, gold "RETRA." logo)

- **Gallery (same nine slots as Klik):**
  - `g0-<colour>`: hero; swaps with the colour picker (Brown, Green, Blue, Yellow, Pink, Black, White).
  - `g1`: 4 pre-installed filters.
  - `g2`: Screen-free. on purpose.
  - `g3`: Easy USB-C transfer.
  - `g4`: How to use Retra.
  - `g5`: rating + review quotes.
  - `g6`: in hand.
  - `g7`: what's in the box.
  - `g8`: Gift-ready.
- **Filters section:** `f-*`, four different scenes, one per filter, as Klik does.
- **Comparison chart:** `cmp-retra.png`, `cmp-disposable.png` (unbranded disposable).
- **Reviews:** `rev*`, plus the Europe / theme-park / beach lifestyle shots.

## Before this goes live

- **Placeholders (yellow on the page):** price, bundle totals, strap value, add-on prices, rating, review count, delivery times, support email. `g5` also has "[4.8]" in the image; set the real rating in `gallery.html` and re-render.
- **Reviews:** the 12 photo reviews, the buy-box quote and the `g5` quotes are SAMPLES written in Klik's style. They are not Klik's customers' reviews and not real Retra reviews. Replace them with real reviews (e.g. a Loox import) before running traffic.
- **Photos:** replace the generated product photos with real supplier photos of the unit.
- **Supplier check:** confirm the optical viewfinder, the filter control and the seven colours.
- **Wiring:** the buttons and forms are template-only.
