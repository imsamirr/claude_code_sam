---
name: static-ads
description: Research, write and render a weekly batch of Meta static ads (and build-up GIFs) for any brand in ads/brands/, with persona-matched product colorways, English and US-Spanish copy, 9:16 output with all content in the 4:5 safe area, and an approve/reject loop. Use for "make this week's statics", "new static concepts for <brand>", "set up static ads for my other brand", "Spanish statics", "turn these concepts into GIFs", or a weekly static-ads trigger.
---

# Static ads

The engine lives in `ads/` (`generate.py`, `review.py`, `atria_pull.py`); each brand lives in
`ads/brands/<brand>/`. Read `ads/README.md` for commands. This skill is the process around them.

Two batches a week, 1 static per concept (no variations), each saved as a 9:16 PNG
(Stories/Reels) plus its 4:5 crop (feed), about **30% Spanish**. GIFs are rendered only for statics
the user approves.

| Batch | When | Folder | Ids | Content |
|---|---|---|---|---|
| **Iterations** | Tuesday | `weeks/<YYYY>-W<ww>-tue` (current week) | `T<ww>_nn_slug` | 20 big-swing iterations of what's winning now and what won this time last year. **No net-new ideas.** |
| **Net-new** | Friday | `weeks/<YYYY>-W<ww>-fri` (next week) | `W<ww>_nn_slug` | 40 concepts: ~32 net-new, ~8 in proven winning-persona formats. |

## 0. New brand? Onboard it first

1. `cp -r ads/brands/_template ads/brands/<brand>` and fill in `brand.json`:
   - `product`, `price`, `palette`, `font_style`, `website`.
   - `prompt_rules[0]`: a precise physical description of the product, so the model keeps it exact.
   - `claims_to_avoid`: anything legal, ops or reviews say the brand can't promise.
   - `audience`: who the product is for (e.g. Comfort Wear is women only). If the product is
     gendered, add a `prompt_rules` line saying who may wear it, and frame personas and gifting to
     match (gift for mom/grandma/wife, not dad).
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

## Schedule

One routine ("Comfort Wear weekly statics") fires **Tuesday and Friday at 5:50am ET**, done by 9am:
- **Tuesday** → iteration batch for the current ISO week (`2026-W44-tue` on Tue Oct 27, 2026).
- **Friday** → net-new batch for the coming ISO week (Fri Oct 16, 2026 builds `2026-W43-fri`; Fri Oct 23 builds `2026-W44-fri`, which already holds 7 seasonal travel concepts to top up to 40).
(The first two batches, `2026-W42` and `2026-W43`, predate this naming.)
If the target `concepts.json` already exists, keep its concepts and add until the batch is full.

## 1. Research refresh (each run, short)

- Read `research/analysis.md` and `feedback.json` (what was approved/rejected and why).
- **Same window last year**: `python ads/atria_pull.py seasonal --week <target week>` lists the top
  spenders (videos and statics) from the matching dates last year (±7 days). Make at least 5
  concepts from them, tagged `"group": "seasonal"` (they count toward the winning half): turn each
  top video's script (hook, test/ranking, proof lines) into static formats. Example: the travel
  "we tested 5 shoes" video (Kyro 293, 2.15 ROAS) won late Oct–early Nov 2025, so `2026-W44` leads with travel rankings.
  Atria's API returns no transcripts for these, so match ad names (e.g. "Kyro_293") against
  `research/data/video_transcripts.md` for script lines, and use the ad name/headline/primary text
  otherwise. Rank by spend: ROAS from Feb 2025 on is unreliable (tracking break, see analysis.md).
- **Current winners (Tuesday)**: `python ads/atria_pull.py current` lists every ad in the last 30 days
  with **spend >= $300 and ROAS >= 1.8**, any format (`audience` marks retargeting vs prospecting);
  `python ads/atria_pull.py rising` is the same filter limited to ads launched in that window.
  Spend remains the reference for older ads (`seasonal`, `winners`), whose ROAS is unreliable.
- **Atria inspiration**: `python ads/atria_pull.py inspo` (rising image ads, last 30 days) every
  week. Skim `inspiration_raw.csv` for new formats and try at least 3 of them in the net-new half.
  Re-read `brand_inspiration_longrunning.csv` (ads running for months) when stuck.
- If an Atria call fails with 401, the key isn't set as `ATRIA_API_KEY`. Say so and continue with the
  existing data; don't look for the key elsewhere.
- Optional pulls: Atria `inspo` for rising formats; the brand's customer survey sheet (Drive) for new
  language; Trustpilot. Reddit is usually unreachable from the cloud container (WebFetch is
  blocked and search rarely returns threads), so use forum mirrors, Mayo Clinic Connect-type
  communities, and your own category knowledge, and say so in the write-up.
- Never copy raw customer rows (emails, order numbers) into the repo; keep aggregates and short
  anonymous quotes only.

## 2. Write the weekly batch

Create `ads/brands/<brand>/weeks/<folder>/concepts.json` (folder per the schedule table above).
Ids are `W<ww>_<nn>_<slug>` (Friday) or `T<ww>_<nn>_<slug>` (Tuesday), unique forever. Schema per concept:

```json
{"id": "W42_07_grandkids_cant_keep_up", "persona": "active_retiree", "lang": "en",
 "colorway": "grey_pink", "angle": "...", "based_on": "the data this comes from",
 "headline": "...", "prompt": "full image prompt with every on-image word in double quotes",
 "gif": {"build": true, "first_ms": 2400,
         "frames": [{"edit": "Remove the headline ...", "ms": 900}, {"edit": "...", "ms": 900}]}}
```

### Tuesday: iteration batch (20, iterations only)

Sources, in this order: (1) `current_winners.csv` (rising winners first), (2) `seasonal_<week>.csv`
(top spenders this time last year, by spend). Every concept must name its source ad in `based_on`
(name, spend, ROAS or "spend-ranked, last year") and keep that ad's **concept and angle**: same
audience, problem, promise and core hook idea. **No net-new ideas.**

Make them **big swings**, not tweaks: put the angle into a static format the source never used,
taken from Atria inspiration (`inspiration_raw.csv` rising formats, `brand_inspiration_longrunning.csv`)
or formats that are already working in the account. Examples: a video's "we tested 5 shoes" becomes a
ranked list, a scorecard, a receipt or postcards; a testimonial becomes a chat screenshot, a sticky note
or a quote card. Name the new format in `angle`. Spread the 20 across the winners (2–4 per strong ad;
the top spender/ROAS gets the most), at least 8 different formats, and **~6 Spanish** (Spanish winners
get Spanish iterations; also put proven English angles into Spanish). Retargeting winners can get
objection-handling or proof formats; prospecting winners get hook-led formats. Tag `"group": "iteration"`.

### Friday: net-new batch (40, mostly net new)

Rules for the 40 (tag each concept `"group": "net_new"` or `"winning"`):
- **Split**: ~32 `net_new` concepts (new angles, personas and formats; weight the personas the user
  wants to grow: currently housekeeping, gifting for her and weight-loss walkers) and ~8 `winning`
  concepts in proven winning-persona formats (Comfort Wear: nurses, CNAs). Don't repeat angles from
  this week's Tuesday iterations.
- **Unique**: 40 different angles, none repeating a previous week's angle. No two concepts share persona + angle; mix formats (lifestyle photo,
  product + callouts, split/comparison, quote/testimonial, native chat/comment screenshot,
  checklist/steps, bold type-only). Try at least 3 formats from the latest Atria `inspo` pull.

### Both batches

- **Personas**: cover at least 8 personas across the week.
- **Colorway**: pick from the persona's `colorways` (or `test_colorways`, at most 2 per week) and
  rotate so no colorway appears more than 8 times. `generate.py` warns when a colorway is
  outside the persona's palette.
- **Spanish**: when the brand has Spanish history (Comfort Wear: Spanish nurse statics at 1.79–2.14
  ROAS, Spanish video $48k), about 30% of each batch is written natively in Spanish, not translated.
  Write as a Spanish speaker living in the US talks: `tú`, everyday Mexican-leaning US Latino
  phrasing ("los pies me mataban", "parado todo el día", "comadre", "porfa", "doble turno"),
  family and coworker framing, US number format. Avoid Spain-isms and stiff translated copy
  ("Consigue el tuyo", "120.000").
- **Copy**: audience or situation in the headline; one problem and one payoff; 15 words or fewer
  on the image when possible; no claim from `claims_to_avoid`. Respect `audience`: only the right people wear
  the product (Comfort Wear: women only; no men or kids wearing it).
- **Native formats (user rule)**: every testimonial/review ad uses `"format": "fb_comment"` (Facebook
  comment thread) or `"format": "trustpilot"` (Trustpilot review cards), and every tweet-style ad uses
  `"format": "x_post"` (real X post). `generate.py` appends the matching guide from `brand.json` →
  `format_guides`; see `ads/brands/comfortwear/format_examples/` for approved-looking examples. In the
  prompt give the exact names, handle, text, date and counts. Use real customer language (Trustpilot
  5★ reviews, survey) for review text; names are first name + last initial only, handles generic. No
  ages, job titles or photos implying a specific verified person, no TrustScore/overall rating, no
  "Verified" badges, no platform logos.
- **GIFs**: add a `gif` block to 5–8 candidates, only where motion adds meaning (a counter ticking up, chat bubbles
  appearing, steps or callouts revealed, a clock moving through a shift). Use `"build": true`:
  each edit removes one element from the finished ad and the GIF plays in reverse, so it builds
  up and holds on the full static. Keep it to 2–3 edits.

## 3. Render

```bash
python ads/generate.py --brand <brand> --week <YYYY-Www>                  # statics (run ids in parallel with xargs -P 8)
python ads/generate.py --brand <brand> --week <YYYY-Www> --gif-only <ids> # GIFs, only for approved statics
python ads/review.py cost --brand <brand> --week <YYYY-Www>              # what the week actually cost
```

Measured gpt-image-2 costs (every call is logged to `output/_usage.jsonl`):

| Step | Default quality | Cost | All-high cost |
|---|---|---|---|
| 4:5 render | medium | ~$0.06 | ~$0.21 |
| 9:16 background extension | low | ~$0.02 | ~$0.17 |
| GIF (2 edit frames) | medium | ~$0.14 | ~$0.43 |
| **40 statics + 8 GIFs per week** | | **~$4.30** | ~$18.60 |

Use `--quality high` only for product close-ups where shoe detail matters. Keep the extension at
`low`, since it only fills background outside the safe area.

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
future prompts for the brand. Rejected concepts get one regeneration with the fix. Then render GIFs for approved concepts
that have a `gif` block (`--gif-only <ids>`) and send them.

## 6. Save and deliver

Commit the week folder, `feedback.json` and any brand/research changes on the working branch, then push.

Drive (Comfort Wear): the folder **"Comfort Wear – Weekly Static Ads"** (id in `brand.json` →
`drive_folder_id`) gets one subfolder per week (`2026-W44`). In it, create the concept sheet from
`python ads/review.py csv --week <week>` (create_file with `textContent`, `contentMimeType: text/csv`,
converted to a Google Sheet, title `<week> concepts`). Image files are too large to upload through the
Drive connector, so the sheet links to each 9:16, 4:5 and GIF file on GitHub. The user fills in the
Verdict and Notes columns, and the next run logs those with `review.py log`.

Slack (last step, once the sheet exists; no Asana task): DM `brand.json` → `slack.notify_channel_id`
with slack_send_message: a bold title "Comfort Wear <Tuesday iterations|Friday net-new> ready: <folder>
(<n> concepts)", then links to the review sheet, the Drive folder and the GitHub output folder, then one
line with the group split, source ads iterated on (Tuesday), Spanish count, GIF candidates and image cost.
