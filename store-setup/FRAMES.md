# Frames and sizes

Portrait products are sold as **Frame × Size** (5 × 6 = 30 variants), the same
structure as the reference store:

| Frame | 12x16 | 18x24 | 24x32 | 30x40 | 36x48 | 40x60 | SKU code |
|---|---|---|---|---|---|---|---|
| Gallery-Wrap (1.5" canvas) | $80 | $120 | $165 | $230 | $340 | $550 | UNF |
| Natural Floating Frame | $130 | $190 | $265 | $365 | $520 | $790 | FNA |
| Black Floating Frame | $130 | $190 | $265 | $365 | $520 | $790 | FBK |
| White Floating Frame | $130 | $190 | $265 | $365 | $520 | $790 | FWH |
| Gold Ornate Frame | $150 | $220 | $300 | $400 | $580 | $840 | GOR |

SKU = `<product prefix>-<frame code>-<size>`, e.g. `PP-GOR-24x32` (Jesus with
Pets, Gold Ornate, 24×32). Prefixes: CP classic, PP pets, RP riders, KP kids,
GP grandparents, WP wedding. Suncatchers keep their own options.

Machine-readable spec: `frame-variants.json`.

## How the theme uses it

`sections/sg-hero-product.liquid` looks for an option whose name contains
"Frame" (and one containing "Size"). When found:

- the gallery shows a live wall mockup; the frame and proportions change with
  the selected Frame/Size, and the customer's AI preview is shown inside it;
- Frame is shown as swatch cards ("from $X"), Size as a 3-column grid with the
  price for the selected frame;
- `sections/sg-frame-guide.liquid` (Frame guide + to-scale size chart) reads the
  Size values and highlights the selected size.

Frame values are matched by keyword (gold/ornate, black, white,
natural/wood/oak, poster/paper, otherwise gallery-wrap), so renaming a value
keeps working as long as it contains one of those words.
Products without a Frame option render exactly as before.

## Applying the variants (needs the Shopify connector)

For each product in `frame-variants.json`, run `productSet` with the product
`id`, `productOptions` (Frame, Size) and the 30 `variants`
(`optionValues`, `price`, `inventoryItem: { sku, tracked: false, requiresShipping: true }`,
`inventoryPolicy: CONTINUE`). `productSet` replaces the variant list, so the old
Format variants (Digital Download, posters, canvases) are removed; nothing else
on the product changes. Check one product on the storefront before the rest.

AI previews are 2:3 (1024×1536). Five of the six sizes are 3:4, so the print
file is cropped slightly top/bottom; the mockup already shows that crop.
