---
name: static-ads
description: Run a brand's Meta static ad program from ads/brands/<brand>/: onboard a new brand (product references, personas, colorways, Atria research, Drive folder, Slack, twice-weekly routine), then each run research → write → render (9:16 with content in the 4:5 safe area, plus 4:5 crop) → QA → Drive sheet → Slack DM. Two batch types: iteration batches (big-swing iterations of current and seasonal winners only) and net-new batches. English and native US-Spanish copy, native Facebook/Trustpilot/X formats, build-up GIFs after approval. Use for "set up static ads for my other brand", "make this week's statics", "iteration batch", "net-new concepts", "Spanish statics", "turn these into GIFs", or a scheduled static-ads routine.
---

# Static ads

Engine: `ads/generate.py` (render), `ads/review.py` (sheets, verdicts, cost, CSV), `ads/atria_pull.py`
(research). Each brand lives in `ads/brands/<brand>/`; **everything brand-specific is in its `brand.json`**
(product, colorways, personas, claims to avoid, languages, native-format guides, `atria_account`,
`program`, `drive_folder_id`, `slack`). Read it first on every run. `ads/README.md` has the commands.
Comfort Wear (`ads/brands/comfortwear/`) is the fully worked example: copy its depth and structure.

Every deliverable is 1 static per concept (no variations): a 9:16 PNG (Stories/Reels) with all content
inside the centered 4:5 area, plus the 4:5 crop (feed). GIFs only for statics the user approves.

## Batch types (sizes and days from `brand.json` → `program`)

| Batch | Default day | Folder | Ids | Content |
|---|---|---|---|---|
| **Iteration** | Tuesday | `weeks/<YYYY>-W<ww>-tue` (current ISO week) | `T<ww>_nn_slug` | `iteration_batch.size` big-swing iterations of what's winning now and what won this time last year. **No net-new ideas.** |
| **Net-new** | Friday | `weeks/<YYYY>-W<ww>-fri` (coming ISO week) | `W<ww>_nn_slug` | `netnew_batch.size` concepts: mostly net-new, a few in proven winning-persona formats. |

If the target `concepts.json` already exists (seasonal or hand-made concepts), keep them and add until
the batch is full. Ids are unique forever. (Comfort Wear's `weeks/2026-W42` and `2026-W43` predate the
`-tue`/`-fri` naming.)

## 0. Onboarding a new brand

Ask the user for anything below you can't find. Do the steps in order; each ends with something saved.

1. **Scaffold**: `cp -r ads/brands/_template ads/brands/<brand>` (lowercase slug, no spaces).
2. **Product references**: find clean studio shots in the brand's Drive (search the shared assets folder
   for Studio/Catalog/Product folders; prefer one side-profile or hero shot per colorway/variant, plain
   light background). Download, resize to ~1536px PNG into `reference/`, and list each in
   `colorways` with a plain-language `label`, and set `colorway_template` (the sentence the prompt
   uses to name the variant, e.g. "The product is the {label} shown in the reference photo."). Never use crops of old ads; they make the product drift.
   Check with a contact sheet that each file is a different variant.
3. **brand.json basics**: `name`, `product`, `price`, `website`, `palette` (with hex), `font_style`,
   `audience` (who uses it; if gendered, add a `prompt_rules` line on who may be shown using it),
   `prompt_rules[0]` (a precise physical description of the product: every distinctive detail), and
   `claims_to_avoid` (guarantees, shipping speed, medical/endorsement claims, anything reviews or
   ops say the brand can't promise). Ask the user to confirm colorway names and any color rules per
   audience.
4. **Research** (write `research/analysis.md`, model it on Comfort Wear's):
   - Set `atria_account` (list accounts if unsure; the API returns names) and `inspo_queries`
     (10–15 category/problem keywords for the ad-library search; without them inspo searches shoe terms). Pull
     `atria_pull.py winners`, `losers`, `inspo`, `current`, `rising`, and `seasonal --week <next week>`.
   - Set `competitor_brands` (direct competitors plus 8–12 adjacent DTC brands in the category) and run
     `atria_pull.py competitors`; review contact sheets of the longest-running ads per brand and write a
     "formats to borrow" playbook into analysis.md. Refresh it on Friday runs.
     Check whether recent ROAS is readable; note unreliable periods in `program.roas_note`.
   - Winners vs losers patterns, top video scripts (transcripts if available), reviews (Trustpilot,
     survey sheets in Drive: aggregates and short anonymous quotes only, never raw customer rows),
     competitor/long-running inspiration, forums (Reddit is usually unreachable from the cloud; say so).
5. **Personas**: 8–13 personas, each with `name`, `source` (the data behind it) and `colorways`
   (`"any"` allowed; `test_colorways` for colors to try). Set `program.winning_personas` (proven
   spend) and `program.grow_personas` (the user's priorities).
6. **Languages**: keep `language_rules.es` only if the brand has Spanish ads or a Spanish audience
   (check account history for Spanish ad names/copy); set the Spanish counts in `program`.
7. **Native formats**: the template's `format_guides` (Facebook comment, Trustpilot, X post) apply to
   every brand; adjust the persona wording if needed. Render one test of each into `format_examples/`
   and show the user.
8. **Delivery**: create a Drive folder "<Brand> – Weekly Static Ads" and save its id as
   `drive_folder_id`; find the user's Slack id (or a channel) and save `slack.notify_channel_id`.
9. **First batch by hand**: run a net-new batch now (sections 1–6), show it, log verdicts.
10. **Routine**: create one routine per brand (create_trigger, `create_new_session_on_fire: true`,
    cron e.g. `CRON_TZ=America/New_York 50 5 * * 2,5`) using the prompt template at the end of this
    file. Routines created from a session get no connectors, so tell the user to open the routine in
    claude.ai → Routines → Edit and add **Google Drive** and **Slack**. Then fire it once with
    `TEST RUN:` instructions (list the Drive folder, run an Atria pull, send a Slack test DM) and read
    its transcript to confirm. Record the schedule and trigger id in `program.schedule`.
11. Commit and push; tell the user what's automated, what each run costs, and what's left for them.

## 1. Research refresh (each run, short)

- Read `brand.json`, `research/analysis.md` and `feedback.json` (approved/rejected and why).
- **Iteration runs**: `atria_pull.py current` (any ad in the last `iterate_when.days` days with spend
  ≥ `min_spend` and ROAS ≥ `min_roas`, any format; `audience` marks retargeting vs prospecting),
  `atria_pull.py rising` (same filter, only ads launched in the window), and
  `atria_pull.py seasonal --week <current week>` (top spenders by **spend** in the same window last
  year, ±7 days). Atria returns no transcripts; match ad names against `research/data/` scripts.
- **Both runs**: `atria_pull.py inspo` (rising image ads, last 30 days) for new formats; re-read
  `brand_inspiration_longrunning.csv` when stuck.
- If Atria returns 401, `ATRIA_API_KEY` isn't set: say so and use existing data. Never look for keys.

## 2. Write the batch

`ads/brands/<brand>/weeks/<folder>/concepts.json`, schema per concept:

```json
{"id": "W43_07_grandkids_cant_keep_up", "group": "net_new", "persona": "active_retiree", "lang": "en",
 "colorway": "grey_pink", "format": "x_post", "angle": "...", "based_on": "the data or source ad",
 "headline": "...", "prompt": "full image prompt, every on-image word in double quotes",
 "gif": {"build": true, "first_ms": 2400,
         "frames": [{"edit": "Remove the headline ...", "ms": 900}, {"edit": "...", "ms": 900}]}}
```
(`format` and `gif` are optional.)

### Iteration batch: iterations only

Sources in order: `current_winners.csv` (rising winners first), then `seasonal_<week>.csv`. Each concept
names its source ad in `based_on` (name, spend, ROAS, or "spend-ranked, last year") and keeps that ad's
**concept and angle**: same audience, problem, promise and core hook. **No net-new ideas.**
Make **big swings**: move the angle into a static format the source never used, taken from Atria
inspiration or formats already working in the account (a "we tested 5" video → ranked list, scorecard,
receipt, postcards; a testimonial → Facebook comment thread, Trustpilot cards, X post, sticky note).
Name the new format in `angle`. 2–4 per strong ad (best performers get the most), at least 8 formats,
Spanish count from `program`. Spanish winners get Spanish iterations; proven English angles can be
rewritten natively in Spanish. Retargeting winners suit proof/objection formats; prospecting winners
suit hook-led formats. `"group": "iteration"`.

### Net-new batch: mostly net new

- `program.netnew_batch.net_new` concepts `"group": "net_new"`: new angles, personas and formats,
  weighted to `grow_personas`; at least 3 formats from the latest `inspo` pull.
- `program.netnew_batch.winning` concepts `"group": "winning"` in proven formats for `winning_personas`.
- No angle repeats from this week's iteration batch or any earlier folder.

### Rules for every batch

- **Unique**: no two concepts share persona + angle; mix formats (lifestyle photo, product + callouts,
  split/comparison, ranked list, scorecard, native comment/review/post, checklist/steps, bold type-only).
- **Personas**: at least 8 per net-new batch. **Colorways**: from the persona's list (≤2
  `test_colorways` per batch), no colorway more than ~20% of the batch.
- **Audience**: only the right people are shown using the product (Comfort Wear: women only, no men or kids).
- **Copy**: audience or situation in the headline; one problem, one payoff; ≤15 words on the image
  when possible; nothing from `claims_to_avoid`, even if a source ad used it.
- **Spanish** (if enabled): written natively as a Spanish speaker in the US talks (`tú`, everyday
  Mexican-leaning US Latino phrasing, family/coworker framing, US number format), never translated or
  Spain-style ("Consigue el tuyo", "120.000").
- **Native formats (user rule)**: testimonials/reviews use `"format": "fb_comment"` or `"trustpilot"`;
  tweet-style ads use `"format": "x_post"`. `generate.py` appends the guide from `format_guides`. Give
  exact names, handle, text, date and counts in the prompt. Review text comes from real customer
  language; names are first name + last initial, handles generic; no ages/job titles implying a real
  verified person, no overall rating/TrustScore, no "Verified" badges, no platform logos.
- **GIF candidates**: 3–8 `gif` blocks where motion adds meaning (counter ticking, bubbles appearing,
  steps revealed). `"build": true`: each edit removes one element; the GIF plays in reverse and holds on
  the full static. 2–3 edits.

## 3. Render

```bash
python ads/generate.py --brand <brand> --week <folder> <ids>              # run ids in parallel: xargs -P 8
python ads/generate.py --brand <brand> --week <folder> --gif-only <ids>   # GIFs for approved statics
python ads/review.py cost --brand <brand> --week <folder>                 # actual spend
```

Measured gpt-image-2 cost per static ≈ $0.08 (medium 4:5 render ~$0.06 + low 9:16 extension ~$0.02);
GIF ≈ $0.14. Use `--quality high` only for product close-ups.

## 4. QA (always, before anything is shown or posted)

`python ads/review.py sheet --brand <brand> --week <folder>`, then Read every page (zoom into text-heavy
ads). Re-render anything with: a misspelling (incl. accents, ¿ ¡), extra text or panels nobody asked for,
competitor logos/products, the wrong people using the product, a product that doesn't match its
reference, or a native format that doesn't look like the real platform. Use `--extra "<fix>"`, then
delete the bad `_v1` files so each concept has exactly one static.

## 5. Verdicts

Show preview sheets (SendUserFile, `display: render`) when working live. Log verdicts with
`python ads/review.py log <stem> approve|reject "<reason>"`; notes feed every future prompt for the brand.
Rejected concepts get one regeneration with the fix; approved GIF candidates get `--gif-only`.

## 6. Save and deliver

1. Commit the batch folder, `feedback.json` and any brand/research changes; push to the working branch.
2. Drive: subfolder "<folder>" under `drive_folder_id` (reuse if present), then a Google Sheet
   "<folder> concepts" from `python ads/review.py csv --brand <brand> --week <folder>` (create_file,
   `textContent`, `contentMimeType: text/csv`; trash an older sheet for the same folder first). Images
   are too large for the Drive connector, so the sheet links to each 9:16/4:5/GIF on GitHub. The user
   fills in Verdict and Notes; the next run logs them first.
3. Slack: DM `slack.notify_channel_id`: "**<Brand> <iterations|net-new> ready: <folder> (<n> concepts)**",
   links to the sheet, Drive folder and GitHub output folder, then one line: group split · source ads
   (iteration runs) · Spanish count · GIF candidates · image cost. Mention anything skipped.

## Routine prompt template (one routine per brand)

```
Build this run's <Brand> static ads batch so it is complete by 9am Eastern today.
Repo: <owner>/<repo>. If it isn't in the working directory, clone it. Then
`git fetch origin <branch> && git checkout <branch>`; push to that branch (no PR).
Install deps if missing: `python3 -m pip install -q requests python-dotenv pillow pandas`.
Follow .claude/skills/static-ads/SKILL.md for brand `<slug>`. Check the weekday in America/New_York:
<iteration weekday> → iteration batch (section 2) for the current ISO week, folder `<week>-tue`;
<net-new weekday> → net-new batch for the coming ISO week, folder `<week>-fri`; other days: stop.
Steps: log Drive sheet verdicts → research (section 1) → write → render → QA (section 4) →
commit/push → Drive sheet → Slack DM (section 6) → short summary with links and cost.
If Atria returns 401, continue with existing data; never search for keys.
If this run's extra instructions say TEST RUN, do only what they say.
```
