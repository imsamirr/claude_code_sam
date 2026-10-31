# Static ad pipeline

Research → personas → weekly concepts → 4:5 statics (+ GIFs) → review loop, rendered through the
Kie.ai API (GPT Image 2 image-to-image). Works for any brand. The full process is in the
`static-ads` skill (`.claude/skills/static-ads/SKILL.md`).

```
ads/
  generate.py            renders concepts (statics + GIFs)
  review.py              preview sheets + approve/reject log (feeds back into prompts)
  atria_pull.py          pulls winners / losers / current / seasonal / inspiration / competitor ads from Atria
  contact_sheet.py       thumbnail grids of any Atria CSV (competitors, winners, inspo)
  brands/
    _template/           copy this to start a new brand (every brand.json field, with placeholders)
    dentalpulse/         second worked brand: product scope, approved claims, mix, competitor playbook
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
KIE_AI=...                     # Kie.ai API key (KIE_API_KEY also works)
ATRIA_API_KEY=atria-sk_...
```

## Generate

```bash
python ads/generate.py --brand comfortwear --week 2026-W42           # the whole weekly batch
python ads/generate.py --brand comfortwear --week 2026-W42 W42_05    # one concept
python ads/generate.py --brand comfortwear --week 2026-W42 --gif-only   # GIFs for concepts that define one
python ads/generate.py --brand comfortwear C17                       # a library concept
python ads/generate.py ... --extra "make the headline bigger" --resolution 4K
```

**Format:** every ad is one 4:5 image (1088×1360, feed). No 9:16 versions. Each concept writes
`<id>_v1.png`; a rerun after a rejection makes `_v2`. (Batches before 2026-10-31 have a 9:16
`<id>_v1.png` plus `<id>_v1_4x5.png`.) The reference photo is uploaded to Kie, a
`gpt-image-2-image-to-image` task runs with `aspect_ratio: 4:5`, and the result is polled and saved.

**GIFs:** a concept with a `gif` block gets `<id>_v1.gif` (544×960). With `"build": true`, each
edit removes one element from the finished static and the GIF plays in reverse, so it builds up
and ends on the full ad. GIFs are 544×680.

**Personas and colors:** each concept names a `persona` and a `colorway`. The colorway picks the
reference photo, and `generate.py` warns if it's outside the persona's palette in `brand.json`.

**Spanish:** `"lang": "es"` adds the brand's Spanish rules (US Latino voice, accents kept, US
number format). Write Spanish concepts natively; don't translate English ones.

**Cost:** about 6 Kie credits per static at 1K (~$0.03 at $0.005/credit; set `KIE_USD_PER_CREDIT` if
your rate differs) and about a minute per task; GIF frames cost the same. Every task is logged to
`output/_usage.jsonl` with its credits; see `python ads/review.py cost --week <week>`. Flags:
`--resolution 1K|4K` (2K doesn't support 4:5).

## Review loop

```bash
python ads/review.py sheet --week 2026-W42                 # contact sheets of unreviewed ads
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
python ads/atria_pull.py current --brand dentalpulse      # last 30 days, spend >= $300, ROAS >= 1.8
python ads/atria_pull.py seasonal --brand dentalpulse --week 2026-W43   # top spenders this time last year
python ads/atria_pull.py competitors --brand dentalpulse  # brand.json -> competitor_brands, longest-running first
python ads/contact_sheet.py --brand dentalpulse competitor_ads.csv --by brand --per 6   # -> research/sheets/
```

`--account` defaults to brand.json → `atria_account`; inspo search terms come from `inspo_queries`.

## Comfort Wear references

`brands/comfortwear/reference/` holds side-profile studio shots from the brand Drive
(Studio → Catalog 1x1, `..._CATALOG_Side N.jpg`), resized to 1536px: navy blue (Side 1, the
team's "WhiteBlue"), red burgundy (3), all black (6), black/purple (7), purple (9), light grey (11),
black/mint (15), black/white (21, "BlackWhite"), grey/pink (26).

On-image text is rendered by the image model, so check spelling on every ad before approving.
