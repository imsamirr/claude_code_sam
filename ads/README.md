# Static ad pipeline (Comfort Wear)

Research → concepts → images, generated with OpenAI's image model (ChatGPT image generation).

```
ads/
  analysis.md          findings: winners vs losers, scripts, Trustpilot, inspiration
  concepts.json        19 ad concepts with full image prompts
  generate.py          renders concepts with the OpenAI image API
  review.py            preview sheets + approve/reject log (feeds back into prompts)
  feedback.json        your verdicts and notes (created on first review)
  atria_pull.py        refreshes winners / losers / inspiration from Atria
  reference/           product photos sent with every prompt (keeps the shoe accurate)
  data/                pulled CSVs and video transcripts
  output/              generated images
```

## Setup

Add the keys to `.env` at the repo root (already gitignored), or as environment secrets in Claude Code cloud environments:

```
OPENAI_API_KEY=sk-...
ATRIA_API_KEY=atria-sk_...
```

## Generate

```bash
python ads/generate.py                   # every concept, 1 image each
python ads/generate.py C01 C04 -n 3      # 3 variants of two concepts
python ads/generate.py C05 --size 1024x1536 --extra "use a white background"
```

Each image costs roughly $0.17–0.25 at `--quality high` (gpt-image-1, 1024px). Use `--quality medium` to explore cheaply.

## Review loop

1. Claude generates a batch, builds a preview sheet (`python ads/review.py sheet`) and shows it in chat.
2. You reply with verdicts, e.g. "approve C01_v1, C07_v2 · reject C05_v1: too much text".
3. Claude logs them (`python ads/review.py log C05_..._v1 reject "too much text"`).
4. Every later `generate.py` run adds the approved/rejected notes to its prompts, and rejected concepts get regenerated with the fix.

## Refresh research

```bash
python ads/atria_pull.py winners   # statics >= $5k spend since 2024
python ads/atria_pull.py losers    # statics < $200, paused, last 12 months
python ads/atria_pull.py inspo     # image ads, rising impressions, launched last 30 days
```

## Improving accuracy

The files in `reference/` are crops from past ads. For the most faithful shoe renders, replace them with clean studio PNGs (white background, side profile) of each colorway, keeping the same filenames.
