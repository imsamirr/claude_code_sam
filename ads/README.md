# Static ad pipeline

Research → personas → weekly concepts → 9:16 statics (+ GIFs) → review loop, rendered with
OpenAI's image model (`gpt-image-2`). Works for any brand. The full process is in the
`static-ads` skill (`.claude/skills/static-ads/SKILL.md`).

```
ads/
  generate.py            renders concepts (statics + GIFs)
  review.py              preview sheets + approve/reject log (feeds back into prompts)
  atria_pull.py          pulls winners / losers / inspiration from Atria
  brands/
    _template/           copy this to start a new brand
    comfortwear/
      brand.json         product, palette, colorways, personas (+ allowed colors), language rules
      reference/         studio product photo per colorway (sent with every prompt)
      research/          analysis.md + pulled data
      concepts.json      concept library / backlog (C01–C23)
      output/            renders from the library
      weeks/2026-W42/    weekly batch: concepts.json + output/
      feedback.json      verdicts and notes (created on first review)
```

## Setup

Keys go in `.env` at the repo root (gitignored) or as environment secrets:

```
OPENAI_API_KEY=sk-...
ATRIA_API_KEY=atria-sk_...
```

## Generate

```bash
python ads/generate.py --brand comfortwear --week 2026-W42           # the whole weekly batch
python ads/generate.py --brand comfortwear --week 2026-W42 W42_05    # one concept
python ads/generate.py --brand comfortwear --week 2026-W42 --gif-only   # GIFs for concepts that define one
python ads/generate.py --brand comfortwear C17                       # a library concept
python ads/generate.py ... --extra "make the headline bigger" --quality medium
```

**Format:** every ad is rendered at 4:5 (1088×1360). Its background is then extended to 9:16
(1088×1920) and the original 4:5 pixels are pasted back on top, so text and product always
sit inside the 4:5 safe area. Each concept writes `<id>_v1.png` (9:16, Stories/Reels) and
`<id>_v1_4x5.png` (feed). There's one static per concept; a rerun after a rejection makes `_v2`.

**GIFs:** a concept with a `gif` block gets `<id>_v1.gif` (544×960). With `"build": true`, each
edit removes one element from the finished static and the GIF plays in reverse, so it builds up
and ends on the full ad. All frames share the static's extended edges.

**Personas and colors:** each concept names a `persona` and a `colorway`. The colorway picks the
reference photo, and `generate.py` warns if it's outside the persona's palette in `brand.json`.

**Spanish:** `"lang": "es"` adds the brand's Spanish rules (US Latino voice, accents kept, US
number format). Write Spanish concepts natively; don't translate English ones.

**Cost:** about 2 image calls per static (render + background extension) plus 1 per GIF frame,
roughly $0.40–0.60 per static at `--quality high`.

## Review loop

```bash
python ads/review.py sheet --week 2026-W42                 # 9:16 contact sheets, 4:5 area dashed in red
python ads/review.py log W42_05_teacher_cute_and_comfy_v1 approve "warm classroom, shoe reads as stylish"
python ads/review.py log W42_11_step_counter_weightloss_v1 reject "progress ring doesn't match 10,000"
python ads/review.py summary
```

Notes from every verdict are added to later prompts for that brand.

## Research

```bash
python ads/atria_pull.py winners --brand comfortwear --account WearOrtho   # statics >= $5k spend since 2024
python ads/atria_pull.py losers  --brand comfortwear --account WearOrtho   # < $200, paused, last 12 months
python ads/atria_pull.py inspo   --brand comfortwear --account WearOrtho   # rising image ads, last 30 days
```

## Comfort Wear references

`brands/comfortwear/reference/` holds side-profile studio shots from the brand Drive
(Studio → Catalog 1x1, `..._CATALOG_Side N.jpg`), resized to 1536px: navy blue (Side 1, the
team's "WhiteBlue"), red burgundy (3), all black (6), black/purple (7), purple (9), light grey (11),
black/mint (15), black/white (21, "BlackWhite"), grey/pink (26).

On-image text is rendered by the image model, so check spelling on every ad before approving.
