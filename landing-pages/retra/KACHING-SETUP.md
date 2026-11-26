# Retra-Shots bundle offer in Kaching Bundles: setup steps

Store: Reclaim Nutra. Live theme: "Retra-Shots (bar update)". The product page already has a slot, brand styling and cart
handling for the Kaching picker (see "On/off" below). Copy: StefanBrain (copy/16-stefanbrain-shopify-slots.md).

## 1. Create the deal
Kaching Bundles → Create deal → Bundle / quantity breaks.
- Deal name (internal): Retra-Shots Black Friday bundles
- Products: Retra-Shots Screen-Free Camera
- Block title: Black Friday Bundles

Bars:
| Bar | Quantity | Price | Title | Subtitle | Badge | Free gift |
|---|---|---|---|---|---|---|
| 1 | 1 | Default ($99) | 1x Retra-Shots Camera | $99 each (Regular price $200) | none | none |
| 2 | 3 | Fixed total $198 (or 33.33% off) | Buy 2, Get 1 Free (3x) | $66/ea ($198 total) + Free $29 Strap | MOST POPULAR (pre-select this bar) | Retra-Shots Woven Camera Strap Leash ×1, label "+ Free Strap Leash ($29 value)" |
| 3 | 5 | Fixed total $297 (or 40% off) | Buy 3, Get 2 Free (5x) | $59.40/ea ($297 total) + Free Gifts ($79) | BEST VALUE | Strap Leash ×1 + Retra-Shots Leather Camera Bag ×1, labels "+ Free Strap Leash ($29 value)" / "+ Free Leather Bag ($50 value)" |

- Footer / note text (if offered): Mix and match any of the 7 colors. 30-day returns apply.
- Variant selectors: on (one colour picker per camera).

## 2. Design (the theme CSS refines this; these values keep the admin preview on-brand)
Corner radius 14 · Border #D9DFE4 · Selected border #022B49 · Background #FFFFFF · Title #022B49 · Subtitle #416077
Price #022B49 · Compare price #416077 · Badge background #0E1C27, text #FCFBF9 · Gift background #F9F7F2, selected #F1EBE0, text #022B49.
Font: inherit from theme.

## 3. Placement and cart
- Leave placement on automatic: Kaching inserts the picker in the product form, above Add to Cart.
  If it lands elsewhere: Online Store → Customize → product template → Retra-Shots buy box → Add block → Apps → Kaching.
- After add to cart: "stay on page" / no redirect. The theme opens its own slide-out cart after any add.
- Save and activate the deal.

## On/off
- Pause or activate the deal in Kaching (Deals list toggle).
- Or Customize → Retra-Shots buy box → "Show the bundle offer" checkbox (off = plain Add to Cart, picker hidden).

## Gift products (created)
- Retra-Shots Woven Camera Strap Leash: $29, handle retra-woven-camera-strap-leash, SKU RETRA-STRAP
- Retra-Shots Leather Camera Bag: $50, handle retra-leather-camera-bag, SKU RETRA-BAG
Both active on the Online Store channel, tagged retra-gift, inventory not tracked, generated photos (swap for supplier photos).
