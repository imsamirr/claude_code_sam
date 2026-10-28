---
name: static-ads
description: Run a brand's Meta static ad program from ads/brands/<brand>/: onboard a new brand (intake questions, product references, claims, personas, Atria + competitor research, Drive folder, Slack, twice-weekly routine), then each run research → write → render (single size, 4:5, high quality) → QA → Drive sheet → Slack DM. Two batch types: iteration batches (big-swing iterations of current and seasonal winners only) and net-new batches. Native Facebook/Trustpilot/X formats, cartoon/animation formats, competitor-inspired formats, English and native US-Spanish copy, build-up GIFs after approval. Use for "set up static ads for my other brand", "onboard <brand>", "make this week's statics", "iteration batch", "net-new concepts", "competitor research", "Spanish statics", "cartoon ads", "turn these into GIFs", or a scheduled static-ads routine.
---

# Static ads

Engine: `ads/generate.py` (render), `ads/review.py` (sheets, verdicts, cost, CSV), `ads/atria_pull.py`
(research), `ads/contact_sheet.py` (thumbnail grids of any Atria CSV). Each brand lives in
`ads/brands/<brand>/`; **everything brand-specific is in its `brand.json`**: read it first on every run.
`ads/README.md` has the commands. Two fully worked brands to copy from:
- `comfortwear/`: women's orthopedic shoes. Colorways per persona, Spanish, seasonal travel.
- `dentalpulse/`: ultrasonic appliance cleaner. Product-scope limits, approved aggressive claims,
  appliance mix, old-method "enemy", competitor playbook (research/analysis.md §6), cartoon formats.

Every deliverable is 1 static per concept (no variations) in ONE size, 4:5 (1088x1360, feed), rendered once
at high quality with `--layout feed` (the default; user rule 2026-10-18: no 9:16). The file is
`<id>_vN.png`. GIFs only for statics the user approves.

## Batch types (sizes and days from `brand.json` → `program`)

| Batch | Default day | Folder | Ids | Content |
|---|---|---|---|---|
| **Iteration** | Tuesday | `weeks/<YYYY>-W<ww>-tue` (current ISO week) | `T<ww>_nn_slug` | `iteration_batch.size` big-swing iterations of what's winning now and what won this time last year. **No net-new ideas.** |
| **Net-new** | Friday | `weeks/<YYYY>-W<ww>-fri` (coming ISO week) | `W<ww>_nn_slug` | `netnew_batch.size` concepts: mostly net-new, a few in proven winning-persona formats. |
| One-off (by hand) | any | `weeks/<YYYY>-W<ww>-<tag>` e.g. `-launch`, `-comp` | own letter, e.g. `L<ww>_`, `C<ww>_` | onboarding launch batch, competitor-inspired batch, seasonal pushes. List these folders in the routine prompt so runs don't repeat their angles. |

If the target `concepts.json` already exists, keep its concepts and add until the batch is full. Ids are
unique forever. (Comfort Wear's `weeks/2026-W42` and `2026-W43` predate the `-tue`/`-fri` naming.)

## 0. Onboarding a new brand

### 0a. Intake: ask the user up front (AskUserQuestion or one short message), then save the answers in brand.json

1. **Products in scope**: which products to advertise. Advertise **only** those. Other SKUs stay out of
   `reference/`, `colorways` and every prompt (DentalPULSE: Pod + Travel Pod only, no Pod Max or tablets).
2. **Product facts** the ads must get right: cycle time, sizes, who wears it, what it's for. Each becomes
   a `prompt_rules` line (DentalPULSE: "cycle is always 5 minutes, never 3"; Comfort Wear: "women only").
3. **Claims**: which of the account's live claims may be used (percentages, "clinical-grade", lab tests,
   star ratings), and how aggressive to be. Record them in `approved_claims` and `claims_note`. Keep
   unconfirmed ones (endorsements, guarantees, shipping, customer counts, awards, press) in
   `claims_to_avoid` until confirmed.
4. **Mix**: product/use-case split per batch (`program.mix`, e.g. 50% dentures / 25% night guards /
   25% aligners+retainers) and persona priorities.
5. **The enemy**: what customers used before (toothbrush, Polident, vinegar…) and whether those may be
   named or shown (`old_methods`). Competitors: who they are (`competitor_brands`) and whether naming
   is allowed (default: competitor pods/products unbranded).
6. **Data**: feedback/survey sheet link, Atria ad-account name, asset folder in Drive, and the team's
   **creative strategy briefs / research docs** (Notion, Google Docs): read them, don't guess the strategy.
   Also ask what the product should be called for cold audiences (e.g. "ultrasonic cleaner", not "Pod").
7. **Languages** (Spanish or not), **cadence** (default Tue iterations 20 + Fri net-new 40), **delivery**
   (Drive folder, Slack id or channel).

### 0b. Build

1. **Scaffold**: `cp -r ads/brands/_template ads/brands/<brand>` (lowercase slug, no spaces). The
   template has every field with placeholder text; replace them all.
2. **Product references**: clean studio/hero shots (brand Drive assets or the store's product images),
   one per variant, plain light background, ~1536px PNG in `reference/`. List each in `colorways` with a
   plain-language `label`; set `colorway_template` (the sentence naming the variant in prompts). Never use
   crops of old ads. Contact-sheet them to confirm each file is a different in-scope product. If the user
   sends product photos in chat, compare them with the references and fix `prompt_rules[0]`.
3. **brand.json basics**: `name`, `product` (only in-scope products), `price`, `website`, `palette`
   (hex), `font_style`, `audience`, `prompt_rules` (precise product description first, then who may use
   it, product facts, text/“nothing extra” rules), `approved_claims`, `claims_to_avoid`, `old_methods`.
4. **Research** → `research/analysis.md` (structure like DentalPULSE's: winners · survey · competitors ·
   personas · claims/mix · competitor playbook):
   - Set `atria_account` and `inspo_queries` (10–15 category/problem keywords; without them inspo
     falls back to shoe terms). Pull `atria_pull.py current`, `rising`, `winners`, `losers`, `inspo`,
     `seasonal --week <next week>` (all with `--brand`). Run the long pulls in the background.
   - Look at what wins: `contact_sheet.py current_winners.csv --per 20` and read the primary text of the
     top ads. Note formats (comparison, listicle, native advertorial, offer) and which product/persona
     carries spend; check whether ROAS is readable (`program.roas_note`).
   - **Competitors**: set `competitor_brands` (direct competitors + 8–12 adjacent DTC brands in the
     category) and `inspo_queries`, run `atria_pull.py competitors` (sorted by **most impressions**, so
     you see what gets delivery now), filter to the category, then `contact_sheet.py <csv> --per 40`.
     Read every page; write a "formats to borrow" playbook: per brand the longest-running formats and
     hooks, then a numbered "what to take" list (name the incumbent, before/after in hand, shock headline,
     native UI frames, premium offer tile, starter pack, big numbers, timely callouts…).
   - **Creative briefs (Notion etc.)**: delegate a read-only subagent to digest every monthly brief,
     research and competitor page into `research/notion_brief.md` (concepts to test, controversial lines,
     mechanism, proof, formats, offers, 20 sharpest hooks, citations). Briefs drive the net-new concepts.
   - **Survey/feedback sheet**: delegate a deep dive (counts per segment, purchase reasons, frustrations,
     objections, wins verbatim, 1–2★ themes, headline banks) into `research/feedback_deep_dive.md`;
     download via Drive (`download_file_content`, text/csv). Keep only
     aggregates and short anonymous quotes; never commit raw rows, emails or order numbers. Pull: appliance
     or use-case split, ages, previous method, frustrations, objections, wins in their words, who noticed,
     and the negatives to design around (claims that disappointed people).
   - Web search for competitor positioning and review complaints. Reddit is usually unreachable; say so.
5. **Personas**: 6–13, each with `name`, `source` (the data) and `colorways` (`"any"` allowed,
   `test_colorways` for colors to try). Include buyer personas (gift-giver, adult child, parent) and a
   "switcher" (burned by a cheaper competitor) when the data shows them. Set `program.winning_personas`
   and `program.grow_personas`.
6. **Languages**: keep `language_rules.es` only if the brand has Spanish ads or audience; set counts.
7. **Formats**: the template's `format_guides` hold the native formats (fb_comment, trustpilot,
   x_post) and the cartoon/animation formats (cartoon_3d, comic_strip, flat_illustration, claymation,
   retro_cartoon, anime_soft). Render 3–6 tests into `format_examples/` (`--week ../format_examples`)
   and show the user.
8. **Delivery**: Drive folder "<Brand> – Weekly Static Ads" → `drive_folder_id`; Slack id →
   `slack.notify_channel_id`.
9. **Launch batch by hand** (`weeks/<week>-launch`, ~20–24 concepts) following the mix: render, QA,
   Drive sheet, Slack DM, preview sheets in chat. Then usually a competitor-inspired batch
   (`-comp`) once the playbook exists.
10. **Routine**: one per brand (create_trigger, `create_new_session_on_fire: true`, cron like
    `CRON_TZ=America/New_York 5 6 * * 2,5`; stagger brands ~15 min). Use the prompt template below.
    **Routines created from a session get no connectors** (the connectors parameter isn't available for
    this org): tell the user to open claude.ai → Routines → <routine> and add **Google Drive** and
    **Slack**, as they did for Comfort Wear. Optionally fire once with `TEST RUN:` instructions and read the
    transcript. Record the schedule and trigger id in `program.schedule`.
11. Commit and push; tell the user what's automated, cost per run, and what's left for them (connectors,
    unconfirmed claims).

When the user adds a rule later ("only these products", "5-minute cycles", "50/25/25", "be aggressive",
"use cartoon formats"), apply it everywhere at once: brand.json (and the template if it's general),
analysis.md, any affected concepts (re-render), **every routine prompt** (update_trigger with the full
prompt), and this skill.

## 1. Research refresh (each run)

**Comfort Wear standing rules (user, 2026-10-28; override every older focus line, incl. the Oct 26 nurse+travel-only and Spanish-twin rules).** Full text in `brand.json` → `program.focus_2026_10_28`, `wellness`, `paused_personas`.
- **English only.** No Spanish concepts or twins until the user says otherwise.
- **Angles** (audience × pain × format): Nurse / 12-hour shifts ~35%, Travel incl. Disney + Europe ~25%, Plus-size women ~20% (mostly mash-ups: plus-size nurse, plus-size at Disney), test slot ~20% for new pain points. Pains: plantar fasciitis first, bunions second, then swollen feet, knee/back from standing, neuropathy, arthritis, "just want comfort", plus any new ones in the feedback sheet. ≥60% lead with a named pain in the customer's words. **Teacher is paused**: write none unless `atria_pull.py current` shows a teacher ad at ≥$300 spend and ≥1.8 ROAS (then say so in Slack). Reweight each run from Atria `current`, verdicts and the seasonal pull.
- **Research every run, in this order:** (1) our statics with **≥$10k spend** (`winning_statics.csv`, refresh with `atria_pull.py winners`) and `current` + `seasonal` winners: write down their patterns; (2) our **winning video scripts** (`research/data/video_transcripts.md`) for hooks, objections, story beats, customer phrases; (3) **`atria_pull.py wellness`**: OTHER health & wellness brands, not only footwear (socks, knee sleeves, supplements, grounding sheets, back-pain devices, heat/red light…): image, active, launched in the last 45 days, running 10+ days, max 2 per brand, off-niche dropped. Contact-sheet it (`contact_sheet.py inspiration_wellness_45d.csv --per 40`) and **Read every page**; (4) write a dated "formats found this run" table in `research/analysis.md` (format, brand, category, days running, why it works, our version) and the shared patterns of our winners vs the inspiration.
- **New formats every run.** Formats come from THIS run's Atria research, not from a fixed list. Each concept sets `format_name` (slug) and `format_source` (inspiration brand, category, days running). A format already in `research/format_ledger.json` may not be reused; only our own proven layouts (`wellness.proven_layouts`, named `proven:<slug>`) may repeat, max ~30% of a batch. Run `python ads/format_ledger.py --brand <b> check --week <folder>` before rendering (must print OK) and `add --week <folder>` after shipping. `based_on` names the inspiration ad AND the winner/script it is paired with, plus why.
- **Copy: direct response.** Pain in her words → agitate (what she tried, what it cost) → mechanism (arch, heel cushion, wide toe box, grip) → proof (peer, number, story) → one offer line. Headline ≤ ~8 plain words, specific (a number, a place, a shift length). No puns.
- **Look: realistic, NOT AI.** Real phone-photo scenes (uneven light, skin/fabric texture, grain, imperfect framing) or clean graphic layouts copied from the inspiration ad, never glossy composites. Full-bleed: the headline sits ON the image (sky, wall, floor), never in a separate band stacked above a photo. Natural walking stance (mid-stride, not two shoes planted side by side). **Poppins** for every typeset word (ExtraBold headlines, SemiBold labels); never condensed (Impact/Bebas/Anton) or script fonts; handwriting only on a real object (sticky note, cardboard sign). Legibility for women 60+ still applies. In QA, re-render anything with the wrong font, an invented slogan, or a headline that doesn't flow into the image.
- **Offer** (~30% of a batch): "40% OFF" + "FREE SHIPPING" + "30-DAY MONEY-BACK GUARANTEE"; "HSA/FSA ELIGIBLE" + "UP TO 30% SAVINGS" may replace or join it. A line, pill or seal, never the whole ad. Black Friday week uses its own offers (`program.black_friday_week_2026_11_09`).
- Render one 4:5 per concept with `--quality medium` (~$0.08/ad). Older rules below still apply where they don't conflict.

- Read `brand.json`, `research/analysis.md` and `feedback.json` (approved/rejected and why).
- **Iteration runs**: `atria_pull.py current` (last `iterate_when.days` days, spend ≥ `min_spend`,
  ROAS ≥ `min_roas`, any format), `rising` (same filter, only ads launched in the window), and
  `seasonal --week <current week>` (top spenders by spend in the same window last year, ±7 days).
- **Net-new runs**: `atria_pull.py wellness` (brands with a `wellness` block; else `inspo`), and refresh `competitors` + the playbook when the brand has
  one (new long-running formats only). Iteration runs also pull `wellness` for their big-swing formats.
- **Every run (user rule Oct 24, DentalPULSE)**: analyze our own top-spend statics (`winners` + `current`, with the
  thumbnails via `contact_sheet.py winning_statics_raw.csv`) AND other brands in the category: run
  `atria_pull.py ultrasonic --brand <brand>` (brand.json -> `ultrasonic_queries`, no brand filter, images and video),
  filter, `contact_sheet.py --by brand`, read every page, and update analysis.md. At least 40% of a batch must be
  product-forward iterations of the proven top-spend/top-impression formats (comparison tables, ranking charts,
  lifestyle hero, big-type offer, quote + badge); gimmick formats are the minority.
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
(`format` and `gif` are optional. Keep `headline` equal to the rendered headline; fix it after re-renders.)

### Iteration batch: iterations only

Sources: `current_winners.csv` (rising first), then `seasonal_<week>.csv`. Each concept names its source
ad in `based_on` (name, spend, ROAS) and keeps its **concept and angle** (audience, problem, promise, core
hook). **No net-new ideas.** Make **big swings**: move the angle into a static format the source never
used (from inspo, the competitor playbook, native and cartoon formats), and re-aim winners at the other
products/use cases in `program.mix`. Name the new format in `angle`. 2–4 per strong ad, at least 8
formats. `"group": "iteration"`.

### Net-new batch: mostly net new

- `netnew_batch.net_new` concepts `"group": "net_new"`: new angles, personas and formats weighted to
  `grow_personas`; at least 3 formats from the latest inspo pull and (if present) 5 from the competitor
  playbook.
- `netnew_batch.winning` concepts `"group": "winning"` in proven formats for `winning_personas`.
- No angle repeats from this week's iteration batch or any earlier folder.

### Rules for every batch

- **Quality benchmark (user rule, Oct 13)**: every concept sets `"benchmark"` to the closest key in
  `brand.json` → `benchmarks` (the brand's own top statics in `reference/benchmarks/`); `generate.py`
  attaches it as a style/quality reference and adds `quality_bar`. Write prompts the way the winners look:
  shoe as the hero (35–60% of the frame, often a pair), tight legs/feet crops, one huge heavy headline,
  ≤3 solid pills/blocks/arrows. Default render quality is medium (budget). In QA, put each render next to its
  benchmark and re-render anything that looks like generic AI stock, has a small shoe or a weak headline.

- **Mix**: follow `program.mix` exactly (count it before rendering), plus the funnel split
  (default ~65% top-of-funnel with no price, ~35% offer-based) and `copy_rules` / `naming_rule`.
  Also apply `program.angle_rules` (winning angles, mix-and-match, foot-pain share), `program.offer`
  (offer-stack share and exact wording) and `colorway_priority` (best sellers vs test colors) when the
  brand has them; count each before rendering.
- **Variety (user rule)**: every concept in a batch uses a different format. Rotate across the
  top-impression category formats (analysis.md) and the briefs' formats: insult/shock headline + sticky-note
  offer, lo-fi real photo with minimal text, imaging/petri/microscope proof, price-anchor replacement,
  value-stack bundle flat-lay, big quote over product, real-world sign, advertorial article card, native UI
  (iOS reminder, cart, texts), founder letter, stat pictogram, news split-face, hand + arrows offer,
  ranking grid / report card, post-it confession, timeline, gift static, cartoon formats.
- **Direct response**: pain in the customer's words → agitate → mechanism → proof/offer. Make the top
  purchase reasons explicit and visual (for DentalPULSE: bacteria and yellow stains). Controversial
  enemy framing is welcome when the brand asks for it.
- **No-product concepts**: lo-fi/native images that shouldn't show the product set `"no_product": true`
  (generate.py then drops the product-fidelity rule and tells the model not to show it).
- **Unique**: no two concepts share persona + angle. Mix formats: lifestyle photo, product + callouts,
  split/before-after, ranked list/scorecard, native comment/review/post, phone UI (texts, notes, cart,
  incoming call), big-number type, shock close-up, starter-pack flat-lay, premium offer tile, cartoon.
- **Personas/colorways**: ≥8 personas per net-new batch where the brand has them; colorways from the
  persona's list, ≤2 `test_colorways`, no colorway over ~20%.
- **Audience**: only the right people use the product (Comfort Wear: women only).
- **Product**: only in-scope products. Anything that isn't ours (the "before" cup, a cheap competitor
  pod) must look clearly different from our product, and the prompt must say so.
- **Copy**: audience or situation in the headline; one problem, one payoff; ≤15 words on the image when
  possible. Use `approved_claims` at the strength the user asked for; nothing from `claims_to_avoid`;
  product facts exactly (e.g. 5 minutes). Name the old method (`old_methods`) when allowed; competitor
  products stay unbranded unless the user allows names.
- **Spanish** (if enabled): written natively as US Latinos talk (`tú`, Mexican-leaning everyday
  phrasing, family/coworker framing, US number format), never translated or Spain-style.
- **Native formats (user rule)**: testimonials/reviews use `"format": "fb_comment"` or `"trustpilot"`;
  tweet-style ads use `"format": "x_post"`. Give exact names, handle, text, date and counts. Review text
  comes from real customer language (survey/reviews); names first name + last initial; no TrustScore,
  overall rating, "Verified" badges or platform logos.
- **Cartoon/animation formats (user rule)**: ~15–20% of every batch sets `"format"` to `cartoon_3d`,
  `comic_strip`, `flat_illustration`, `claymation`, `retro_cartoon` or `anime_soft`. `generate.py`
  swaps the photo-quality rule for an illustration rule that keeps the product recognizable. Mix styles.
  Proven ideas: product as hero while cute cartoon germs flee; 4-panel comic (problem → friend's
  advice → product → payoff line); 1930s "old way" with the product breaking out in modern color;
  claymation gift scenes.
- **GIF candidates**: 3–8 `gif` blocks where motion adds meaning. `"build": true`: each edit removes one
  element; the GIF plays in reverse and holds on the full static. 2–3 edits.

## 3. Render

```bash
python ads/generate.py --brand <brand> --week <folder> <ids>              # parallel: xargs -P 8
python ads/generate.py --brand <brand> --week <folder> --gif-only <ids>   # GIFs for approved statics
python ads/generate.py --brand <brand> --week ../format_examples <ids>    # format tests
python ads/review.py cost --brand <brand> --week <folder>                 # actual spend
python ads/format_ledger.py --brand <brand> check --week <folder>         # new formats only (before render)
python ads/format_ledger.py --brand <brand> add --week <folder>           # record them (after shipping)
```

Default `--layout feed` (user rule, Oct 18): one native 4:5 render per ad at the default `high` quality
(headline upper third, product/scene large in the middle, copy or offer lower; edge-to-edge scene, at least
6% margin around text). No 9:16 is made. Older layouts (`native` 9:16 + 4:5 re-layout, `extend` outpaint)
remain available by flag but are not used. `generate.py` center-crops instead of stretching when the API
returns another aspect ratio, so the shoe is never squashed. If the image API rejects a prompt for safety
(e.g. chemicals + mouth = "self-harm"), reframe the visual and retry.

Cost: one high-quality 4:5 render ≈ $0.22 per ad (measured Oct 18; the old medium 9:16 + 4:5 pair was
≈ $0.13). Check `review.py cost` after every batch and report cost per ad. GIF ≈ $0.14.
Use `--quality medium` only if the user asks to cut cost. Shell gotcha: never `pkill -f`/`pgrep -f` a pattern that
also appears in your own command line (it kills or matches the shell itself); wait on renders by
counting `*_4x5.png` files instead.

## 4. QA (always, before anything is shown or posted)

`python ads/review.py sheet --brand <brand> --week <folder> [ids]`, then Read every page. Re-render
(fix the prompt, delete the bad `_v1` files, render again) anything with:
- misspellings (incl. accents, ¿ ¡), extra text/panels nobody asked for, headline text crossing a dark
  or split background;
- the product not matching its reference, an out-of-scope product (e.g. a different model), or a
  non-brand object (case, cheap competitor, cup) that looks like our product;
- wrong product facts (e.g. a 3-minute timer), claims outside `approved_claims`;
- wrong people using the product, distorted hands/mouths/appliances;
- weak before/after (the "before" must look clearly worse);
- a product forced into a `no_product` concept, two copies of the product, bundle items at the wrong scale
  (accessories must look smaller than the hero product), non-physical items (warranties) shown as objects;
- a 4:5 with cut-off copy, less than ~6% margin around text, or blurred/empty/filler bands;
- a compressed, flattened, shortened or stretched shoe, or a shoe that's too small in the scene;
- supporting text (labels, pills, checklist, offer lines) too small to read for the audience (Comfort Wear:
  women 60+, see the legibility rule in `quality_bar`);
- purple headline/body text (purple is a small accent only);
- a native format that doesn't look like the real platform, or competitor logos.
`review.py sheet` with ids overwrites page 1: delete `_preview_*` and rebuild the full sheets at the end.

## 5. Verdicts

Show preview sheets (SendUserFile, `display: render`) when working live. Log verdicts with
`python ads/review.py log --brand <brand> <stem> approve|reject "<reason>"`; notes feed every future
prompt. Rejected concepts get one regeneration with the fix; approved GIF candidates get `--gif-only`.

## 6. Save and deliver (every batch, live or scheduled)

1. Commit the batch folder, `feedback.json`, brand/research changes; push to the working branch.
2. Drive: subfolder "<folder>" under `drive_folder_id` (reuse if present), then a Google Sheet
   "<folder> concepts" from `python ads/review.py csv --brand <brand> --week <folder>` (create_file,
   `textContent`, `contentMimeType: text/csv`; trash an older sheet for the same folder first). Images
   are too large for the Drive connector, so the sheet links to each 4:5/GIF on GitHub.
3. Slack: DM `slack.notify_channel_id`: "**<Brand> <batch type> ready: <folder> (<n> concepts)**", links
   to the sheet, Drive folder and GitHub output folder, then one line: mix split · source ads
   (iterations) · competitor formats · cartoon count · Spanish count · GIF candidates · image cost.
   Mention anything skipped. Also DM rule/format changes the user should know about.

## Routine prompt template (one routine per brand; fill every <…>; see the live DentalPULSE routine)

```
Build this run's <Brand> static ads batch so it is complete by 9am Eastern today.

Repo: <owner>/<repo>. If it is not already in the working directory, clone it first. Then
`git fetch origin <branch> && git checkout <branch>`; push to it when done (no PR). Install deps if
missing: `python3 -m pip install -q requests python-dotenv pillow pandas`.

Follow the `static-ads` skill for brand `<slug>` (always pass `--brand <slug>`). Read brand.json
(approved_claims, claims_to_avoid, old_methods, personas, program) and research/analysis.md first.
<Languages>. Products: ONLY <in-scope products>. <Product facts, e.g. cycle is always 5 minutes>.

User rules:
- Mix in every batch: <program.mix>.
- Claims: <how aggressive; approved_claims>; keep out claims_to_avoid.
- The enemy is <old methods, named/unnamed>; competitors <unbranded/named>.
- Borrow formats from research/analysis.md <playbook section>.
- Cartoon/animation formats: ~15–20% of every batch (3–4 Tue, 6–8 Fri): cartoon_3d, comic_strip,
  flat_illustration, claymation, retro_cartoon, anime_soft. Examples in format_examples/.

Check today's weekday in America/New_York:
- Tuesday → ITERATION batch: folder weeks/<current ISO week>-tue, ids T<ww>_nn_slug, <n> concepts
  (<mix counts>), ONLY iterations of `atria_pull.py current` + `seasonal --week <current week>`
  winners, big-swing formats from inspo/competitor playbook/cartoon; based_on names the source ad.
- Friday → NET-NEW batch: refresh `atria_pull.py competitors` (if the brand has competitor_brands);
  folder weeks/<coming ISO week>-fri, ids W<ww>_nn_slug, <n> concepts (<mix counts>): ~80% net_new
  (grow personas, ≥3 inspo formats, ≥5 playbook formats), ~20% winning personas. Don't repeat angles
  from earlier folders (<list one-off folders>).
- Any other day: say so and stop.

Native formats: reviews → fb_comment/trustpilot, tweets → x_post; real customer language; first name +
last initial; no platform logos/TrustScore/verified badges.

Steps: 1) log Drive sheet verdicts (review.py log), GIFs for approved candidates; 2) research (401 →
continue with existing data, never search for keys); 3) write concepts.json (keep existing, fill to
size; 3–8 GIF candidates); 4) render (xargs -P 8), sheets, read every page, re-render failures per the
skill's QA list; 5) commit/push, Drive subfolder + "<folder> concepts" sheet; 6) Slack DM
<notify_channel_id> with links + one summary line; if Slack/Drive tools are missing, say so at the top
of the summary; 7) short summary with counts, sources, re-renders, cost, Atria status, links.
If this run's extra instructions say TEST RUN, do only what they say and nothing else.
```
