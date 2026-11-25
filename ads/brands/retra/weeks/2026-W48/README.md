# Retra W48 statics (7 TOF + 3 BOF)

Brief: `ads/brands/retra/brief.md`. Masters (1080x1350), contact sheet and CSV are in `output/`.

## What's where
- `copy.json`: StefanBrain's final copy (project "Retra Launch", chat `chat_e2881d64bb4e43c687b42831eb31dff3`), v3 after claim fixes and with no currency code on the image.
- `picks.json`: the render each ad uses, plus its version and per-ad layout data (05 card box, 03 sign blur boxes).
- `qa.json`: section 8 QA result and re-render reasons per ad (also in the CSV `notes` column).
- `renders/`: raw Kie scenes (`{id}_t{try}`), committed as JPEG archives; the 2K PNGs stay local. `_usage.jsonl` logs every billed Kie task and its prompt.
- Product references: `assets/retra/product/` (Sam's 5 shots, upscaled 2x on Kie with recraft/crisp-upscale; originals in `original/`; cutouts from `make_cutouts.py`).

## Rebuild
```bash
python3 render.py 03            # new Kie try for one ad (or --fix 03 "correction")
python3 lineup.py               # 09/10 lineup bases from the real cutouts
python3 compose.py              # composite copy -> output/ (LANG_AD=fr for FR headlines)
python3 finalize.py             # contact sheet + CSV
```

## Type and layout
Landing-page type system (`landing-pages/retra/index.html`): Tinos display at -0.04em in navy #022B49 for headlines, prices and filter labels; Inter for subheads and CTAs; Shantell Sans italic for the 09 pill and the 05 place card. CTAs use the landing page's slate-blue gradient pill. Headlines are balance-wrapped. Text covers 9–17% of each image.

## Open items
- 08 filter tiles are ILLUSTRATIVE (the landing page's filter looks applied to one Kie scene). Replace them with real Retra sample photos before launch.
- 10 has no "Sold out" stamps: stock is low on all colours and none is sold out, so every colour gets a "Low Stock" tag.
- 08 primary text names "Lightroom" (a third-party trademark), and several primary texts say "optical viewfinder": confirm both.
