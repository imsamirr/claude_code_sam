# Portrait print-on-demand theme

Custom Shopify theme files that recreate the layout and structure of a
personalised art-portrait storefront (announcement bar, Prints/Suncatcher
tabs, product-builder hero with style picker and photo upload, before/after
sliders, how-it-works, reviews wall, FAQ, footer, and content pages).

These files are layered on top of a copy of **Dawn** in the Shopify store
(unpublished theme "Art Portrait Theme (Saviors Gift layout)"). Dawn still
renders the cart, customer accounts, search, collections and 404 pages; this
theme re-skins them to the same palette.

## Files

| Area | Files |
| --- | --- |
| Layout | `layout/theme.liquid` |
| Styles / scripts | `assets/sg-theme.css`, `assets/sg-theme.js` |
| Header group | `sections/sg-announcement.liquid`, `sections/sg-topbar.liquid`, `sections/sg-header.liquid`, `sections/header-group.json` |
| Footer group | `sections/sg-footer.liquid`, `sections/footer-group.json` |
| Homepage | `sections/home-group.json` (rendered from the layout, see note) and `templates/index.liquid` |
| Content sections | `sg-hero-product`, `sg-before-after`, `sg-how-it-works`, `sg-video-showcase`, `sg-reviews`, `sg-faq`, `sg-doc`, `sg-track` |
| Templates | `product.json` (+ `.kids`, `.pets`, `.wedding`, `.suncatcher`, `.pet-suncatcher`), `page.json` (+ `.contact`, `.how-it-works`, `.track`, `.reviews`) |
| Snippets | `sg-icon`, `sg-stars`, `sg-logo`, `sg-dawn-head` |

## Notes

- **Homepage:** the store's homepage template was a Replo `index.liquid`,
  which can't be deleted through the API, so the homepage content lives in the
  "Home page" section group (`sections/home-group.json`) and `index.liquid`
  is intentionally empty. To switch to a normal `index.json` template, delete
  `templates/index.liquid` in the Shopify code editor, then move the sections.
- **Photo upload:** the hero adds the photo as a `Photo` line-item property
  (uploaded to Shopify's CDN) and the chosen style as a `Style` property, so
  both show on the order.
- **Images and copy** are placeholders. Replace them in the theme editor:
  product media, style-card images, before/after pairs, review photos, the
  logo (Theme settings > Logo or the Header section), and all text.
- The JSON templates in this folder mirror what is live in the theme. Edits
  made in the theme editor change Shopify's copy, not this folder.
