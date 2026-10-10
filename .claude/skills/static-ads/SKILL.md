---
name: static-ads
description: Research, write and render a weekly batch of Meta static ads (and build-up GIFs) for any brand in ads/brands/, with persona-matched product colorways, English and US-Spanish copy, 9:16 output with all content in the 4:5 safe area, and an approve/reject loop. Use for "make this week's statics", "new static concepts for <brand>", "set up static ads for my other brand", "Spanish statics", "turn these concepts into GIFs", or a weekly static-ads trigger.
---

# Static ads

The engine lives in `ads/` (`generate.py`, `review.py`, `atria_pull.py`); each brand lives in
`ads/brands/<brand>/`. Read `ads/README.md` for commands. This skill is the process around them.

Default deliverable per week: **20 unique concepts, 1 static each** (no variations), saved as a
9:16 PNG (Stories/Reels) plus its 4:5 crop (feed), with 3–5 concepts also rendered as GIFs.

## 0. New brand? Onboard it first

1. `cp -r ads/brands/_template ads/brands/<brand>` and fill in `brand.json`:
   - `product`, `price`, `palette`, `font_style`, `website`.
   - `prompt_rules[0]`: a precise physical description of the product, so the model keeps it exact.
   - `claims_to_avoid`: anything legal, ops or reviews say the brand can't promise.
   - `colorways`: one clean studio photo per colorway/variant in `reference/` (white or light-grey
     background, product only, ~1500px PNG). Find them in the brand's Drive (look for a studio
     or catalog folder; prefer side profile). Never use crops of old ads: they make the product drift.
   - `personas`: who buys and why, each with a `source` (data behind it) and the `colorways` that
     fit it (`"any"` allowed, `test_colorways` for colors you want to try). Ask the user for any
     color rules per audience.
   - `language_rules`: keep `es` if Spanish ads are wanted; add others the same way.
2. Ask for the Atria ad-account name and run `python ads/atria_pull.py winners|losers|inspo --brand <brand> --account "<name>"`.
3. Write `ads/brands/<brand>/research/analysis.md`: what $5k+ winners share, what losers share, video
   script lines worth stealing, review/survey language, competitor and long-running inspiration.
   Reuse the Comfort Wear analysis as the model for depth and structure.

## 1. Research refresh (each week, short)

- Read `research/analysis.md` and `feedback.json` (what was approved/rejected and why).
- Optional pulls: Atria `inspo` for rising formats; the brand's customer survey sheet (Drive) for new
  language; Trustpilot. Reddit is usually unreachable from the cloud container (WebFetch is
  blocked and search rarely returns threads), so use forum mirrors, Mayo Clinic Connect-type
  communities, and your own category knowledge, and say so in the write-up.
- Never copy raw customer rows (emails, order numbers) into the repo; keep aggregates and short
  anonymous quotes only.

## 2. Write the weekly batch

Create `ads/brands/<brand>/weeks/<YYYY>-W<ww>/concepts.json` (ISO week of the launch week).
Ids are `W<ww>_<nn>_<slug>`, unique forever. Schema per concept:

```json
{"id": "W42_07_grandkids_cant_keep_up", "persona": "active_retiree", "lang": "en",
 "colorway": "grey_pink", "angle": "...", "based_on": "the data this comes from",
 "headline": "...", "prompt": "full image prompt with every on-image word in double quotes",
 "gif": {"build": true, "first_ms": 2400,
         "frames": [{"edit": "Remove the headline ...", "ms": 900}, {"edit": "...", "ms": 900}]}}
```

Rules for the 20:
- **Unique**: 20 different angles. No two concepts share persona + angle; mix formats (lifestyle photo,
  product + callouts, split/comparison, quote/testimonial, native chat/comment screenshot,
  checklist/steps, bold type-only).
- **Personas**: cover at least 8 personas; weight toward proven winners (for Comfort Wear: nurses
  and shift workers), and give each new persona at most 1–2 slots until it proves itself.
- **Colorway**: pick from the persona's `colorways` (or `test_colorways`, at most 2 per week) and
  rotate so no colorway appears more than 4 times. `generate.py` warns when a colorway is
  outside the persona's palette.
- **Spanish**: when the brand has Spanish history (Comfort Wear: Spanish nurse statics at 1.79–2.14
  ROAS, Spanish video $48k), make ~6 of the 20 **net-new Spanish concepts**, not translations.
  Write as a Spanish speaker living in the US talks: `tú`, everyday Mexican-leaning US Latino
  phrasing ("los pies me mataban", "parado todo el día", "comadre", "porfa", "doble turno"),
  family and coworker framing, US number format. Avoid Spain-isms and stiff translated copy
  ("Consigue el tuyo", "120.000").
- **Copy**: audience or situation in the headline; one problem and one payoff; 15 words or fewer
  on the image when possible; no claim from `claims_to_avoid`.
- **GIFs**: 3–5 per week, only where motion adds meaning (a counter ticking up, chat bubbles
  appearing, steps or callouts revealed, a clock moving through a shift). Use `"build": true`:
  each edit removes one element from the finished ad and the GIF plays in reverse, so it builds
  up and holds on the full static. Keep it to 2–3 edits.

## 3. Render

```bash
python ads/generate.py --brand <brand> --week <YYYY-Www>          # statics (run ids in parallel with xargs -P 6 for speed)
python ads/generate.py --brand <brand> --week <YYYY-Www> --gif-only   # GIFs from the existing statics
```

Each static is 2 image calls (4:5 render + background extension), each GIF edit is 1 more.
Budget roughly $0.40–0.60 per static at `--quality high` with gpt-image-2. Use `--quality medium` to explore.

## 4. QA before showing anything

Build sheets with `python ads/review.py sheet --brand <brand> --week <YYYY-Www>` and Read every page.
For each ad check: every word spelled exactly (Spanish accents and ¿¡ included), the product matches
the reference (colors, laces, logo, sole), no invented logos or brands, nothing reads as a claim
to avoid, and people's hands and feet look right. Regenerate failures with
`--extra "<the fix>"` (this creates `_v2`; delete the bad `_v1` files so there's still one
static per concept). Look at at least one GIF frame sequence too.

## 5. Show the user and log verdicts

Send the preview sheets with SendUserFile (`display: render`) plus a table: concept, persona,
language, colorway, GIF yes/no, and anything you're unsure about. When they reply, log each verdict:
`python ads/review.py log <image_stem> approve|reject "<their reason>"`. Those notes feed into all
future prompts for the brand. Rejected concepts get one regeneration with the fix.

## 6. Save

Commit the week folder, `feedback.json` and any brand/research changes on the working branch, then push.
