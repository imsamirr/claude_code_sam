---
name: dr-concepts
description: Generate new, testable ad concepts for a brand by stacking personas, occasions, conditions and seasons ("big swings"), grounded in the brand's own Atria ad-account evidence and scored with Stefan Georgi's RMBC direct-response method (Research, Mechanism, Brief, Copy). Each concept card carries the stack, awareness level, angle type, a named mechanism, hooks across trigger types, proof, the objection it answers, a format built from the account's winning skeleton, and claims compliance. Also critiques concepts the user is already testing. Use for "what new concepts should I test", "give me angles for <brand>", "big swing ideas", "combine personas", "RMBC concepts", or "StefanBrain"-style concepting.
---

# DR concepts (big swings + RMBC)

Per-brand rules live in `ads/brands/<brand>/brand.json` → `concept_rules`, and the brand's research
in `ads/brands/<brand>/research/`. Read both first. If `concept_rules` is missing, build it from
§1 and confirm the stacking rule with the user.

Methodology adapted from Stefan Georgi's RMBC skills (MIT): github.com/coleschaffer/dtc-copywriting-skills
(`rmbc-context`, `mechanism-ideation`, `ad-angle-generator`, `hook-battery`, `ad-creative-audit`).
Use the method only. Don't install that repo or run its preambles: they phone home for update
checks, log analytics and try to open videos.

## 1. Research (R): what the account already proves

Use as few Atria calls as possible. Calls beyond the plan's allowance cost 1 workspace credit each,
so say so when it happens. Use existing research files before new calls.

1. `list_ad_account_ads`, last_30d by spend, limit 50: winners, losers, fatigue.
2. `list_ad_account_creative_tags` with `category=persona`, last_30d. Spend and ROAS by persona.
   Buckets overlap: compare them with each other, never sum them.
3. `research/analysis.md` and `research/data/*`: customer language, the survey, the angle databank,
   and what killed past concepts.
4. **Voice of customer (seasonal or new angles):**
   - **Reddit:** reddit.com blocks cloud fetches. Use `scripts/reddit_pull.py <out.json> <queries.txt>`,
     which goes through the public Pullpush archive. Wait between runs: it rate-limits (429) after
     about 40 searches. Filter to the months you care about, and to posts that mention feet or shoes
     together with pain.
   - **YouTube:** use `scripts/yt.py <out.json> <queries.txt>` for titles and view counts. View counts
     show demand.
   - **Amazon:** blocks automated access. Say so; don't guess at its reviews.
   - Quote real posts with links. Never present them as the brand's reviews.
5. Build a **stack table** with columns *ad (full name) | dimensions stacked | spend | ROAS*. Use it to
   confirm or update the stacking rule. Keep the exceptions: stacks that lost, and why.
6. Note concepts already in test so you don't duplicate them. Critique them in the same RMBC terms.

## 2. Stack (the big-swing rule)

A concept is a **stack of 2–3 dimensions** with one ad-ready reason they collide:

| Dimension | Examples (ComfortWear) |
|---|---|
| Persona / job | nurse, travel nurse, CNA, retail, teacher, stylist, server, housekeeping |
| Body / life stage | plus-size (200+ lb), 60+, pregnant, menopause, GLP-1 / new walker |
| Condition | plantar fasciitis, bunions, swelling, arthritis hands, balance |
| Occasion / season | Disney, cruise, NYC at Christmas, Christmas markets, holiday shifts, Black Friday retail, New Year walking, church Sunday |
| Language / culture | US Spanish, faith community |

Rules:
- Never ship a single-dimension concept ("shoes for travel", "nurse shoes").
- The collision must create a **specific, dated, physical problem**. "Plus-size at Disney" works
  because it means 20,000 steps × more load × swelling × lines. Avoid stacks that are only
  demographic overlap.
- Prefer stacks where a **real product feature** solves the collision better than the obvious
  alternative. ComfortWear examples: the stretch knit for swelling, the no-tie bungee laces for anyone
  who struggles to bend, the built-in arch vs foam that flattens.
- Check the calendar: produce for what's 2–6 weeks out.

## 3. Mechanism (M): "only we", built from real features

For each concept, name one mechanism and give the causal chain: feature → physical process →
outcome in the stack's situation.
- Name it in plain, ownable words (e.g. "the breakfast-to-fireworks fit"). Never invent materials,
  tests, patents or stats.
- It must answer: why did the thing they already tried fail? Run the competitor teardown with prices
  if the account's winners use it.
- Score novelty and specificity 1–5 each, and believability high/medium/low. Flag low believability.

**Hero mechanism.** Prefer one named hero mechanism per brand. Every concept's angle traces back to
it, and the other features act as supporting proof. Several angles can stack in one ad if each ties
back to the hero. ComfortWear's proposed hero: "The Hour-4 Foam Collapse" → "Built-In Arch". See
`research/formats_from_jamil_2026-11-23.md`.

**Formats.** Keep a working-formats table per brand (format | account evidence | status). Bring in
formats that are hot in other niches but untested in this one, and give each a stack. Concepts
should pass the "squint test": if two ads look the same when you squint, they aren't different tests.

## 4. Brief (B)

Each concept card holds:
- **Stack**, and the **collision** in one line.
- **Awareness level** (Schwartz): problem-aware or solution-aware for cold traffic.
- **Angle type** from the RMBC taxonomy: problem-aware, mechanism-led, proof-stacked, enemy,
  contrarian, identity, comparison. A batch spans at least 4 types, and no two concepts share a lever.
- **Hooks**: 3 hooks, each a different trigger (curiosity, fear, desire, social proof, contrarian).
  Gates for every hook:
  - it includes a number, name or timeframe
  - it says where the reader IS ("you've tried…")
  - at least one hook per concept has sensory language
- **Format**: the brand's winning skeleton (for ComfortWear: expert composited over real occasion
  footage in the first 3s, competitor teardown with prices, mechanism, hour-by-hour pain, payoff shot,
  product shown by about 0:40, proof block, offer). Name the b-roll the stack needs.
- **Proof**: at least 2 types (demonstration, customer quote, authority explanation, real stat).
- **Objection** handled, and how.
- **Message match**: the landing page, headline and ad text this concept needs.
- **Compliance**: check the claim against `claims_to_avoid` in `brand.json` and drop anything that
  breaks it.
- **Evidence**: which account ads or tags support this stack, with numbers. Say "untested" if none.
- **Kill signal**: what result after about $500–1,000 spend means stop.

## 5. Score, rank, deliver

- Score each concept on the RMBC dimensions, 0–25 each: result specificity, mechanism novelty,
  proof believability, CTA clarity. Cut anything under 60.
- Rank by evidence × timing × production ease.
- Save the full cards to `ads/brands/<brand>/research/concepts_<YYYY-MM-DD>.md`, then commit and push.
- In chat, give a compact ranked table plus the top 3–5 in detail. Use full Atria ad names when citing
  evidence.
- Hand-offs:
  - briefs and scripts: the `ugc-brief-writer` skill, or the RMBC `ugc-brief` / `vsl-script` method
  - statics: the `static-ads` skill (iteration or net-new batch)
