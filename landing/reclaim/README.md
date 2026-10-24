# RECLAIM product page (draft)

`index.html` follows the section order of Blume's SuperBelly product page: lime bar, header, breadcrumb,
gallery + buy box (subscription box with perk tiles, accordions, shaker promo), plum ticker, "Midlife has been hard on our cortisol"
split with cited stats, ingredient carousel, "Benefits you can feel" split, orange band, plum comparison table,
three cards, FAQ with references, blush footer.

Images in `img/` were generated with `generate_images.py` (OpenAI gpt-image-2, using `reclaim-pouch.webp` as the product
reference). Re-run one with `python landing/reclaim/generate_images.py pdp-1-hero` after deleting or to overwrite it.
`sec-meet.webp` is a spare wide shot not used on the page yet.

Yellow dashed chips are unconfirmed facts (price, doses, terms, NPN). "Draft note" boxes are internal guidance.
The **Hide draft notes** button shows the customer view and hides the reviews placeholder.
The page is a body fragment (published as a claude.ai Artifact, which adds `<html>`/`<head>`).
