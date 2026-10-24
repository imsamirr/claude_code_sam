# Static ad pipeline

Research → personas → weekly concepts → 4:5 statics (+ GIFs) → review loop, rendered with
OpenAI's image model (`gpt-image-2`). Works for any brand. The full process is in the
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

**Format (since 2026-10-18):** one size, 4:5 (1088×1360), rendered once at high quality (`--layout feed`, the default; ≈ $0.22/ad). Each concept writes `<id>_v1.png`; a rerun after a rejection makes `_v2`. Older flags: `--layout native` (9:16 + 4:5) and `--layout extend`.

**GIFs:** a concept with a `gif` block gets `<id>_v1.gif` (544×960). With `"build": true`, each
edit removes one element from the finished static and the GIF plays in reverse, so it builds up
and ends on the full ad. All frames share the static's extended edges.

**Personas and colors:** each concept names a `persona` and a `colorway`. The colorway picks the
reference photo, and `generate.py` warns if it's outside the persona's palette in `brand.json`.

**Spanish:** `"lang": "es"` adds the brand's Spanish rules (US Latino voice, accents kept, US
number format). Write Spanish concepts natively; don't translate English ones.

**Cost:** a static is 2 calls: a medium 4:5 render (~$0.06) and a low-quality extension (~$0.02).
A GIF adds about $0.14. A week of 40 statics plus 8 GIFs comes to about $4.30, vs about $18.60
with everything at high. Every call is logged to `output/_usage.jsonl`; see
`python ads/review.py cost --week <week>`. Flags: `--quality`, `--extend-quality`, `--gif-quality`.
Render GIFs only for approved statics (`--gif-only <ids>`).

## Review loop

```bash
python ads/review.py sheet --week 2026-W42                 # contact sheets
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
