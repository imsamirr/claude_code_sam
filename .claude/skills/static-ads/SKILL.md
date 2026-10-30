---
name: static-ads
description: Run a brand's Meta static ad program from ads/brands/<brand>/: onboard a new brand (intake questions, product references, claims, personas, Atria + competitor research, Drive folder, Slack, twice-weekly routine), then each run research → write → render (single size, 4:5, high quality) → QA → Drive sheet → Slack DM. Two batch types: iteration batches (big-swing iterations of current and seasonal winners only) and net-new batches. Native Facebook/Trustpilot/X formats, cartoon/animation formats, competitor-inspired formats, English and native US-Spanish copy, build-up GIFs after approval. Use for "set up static ads for my other brand", "onboard <brand>", "make this week's statics", "iteration batch", "net-new concepts", "competitor research", "Spanish statics", "cartoon ads", "turn these into GIFs", or a scheduled static-ads routine.
---

# Static ads

Engine: `ads/generate.py` (render), `ads/review.py` (sheets, verdicts, cost, CSV), `ads/atria_pull.py`
(research), `ads/contact_sheet.py` (thumbnail grids of any Atria CSV). Each brand lives in
`ads/brands/<brand>/`; **everything brand-specific is in its `brand.json`**: read it first on every run.
`ads/README.md` has the commands. Two fully worked brands to copy from:
- `comfortwear/`: women's orthopedic shoes. Colorways per persona, wellness-wide inspiration pull, format ledger,
  customer-voice mining (English only since 2026-10-28; see its standing rules below).
- `dentalpulse/`: ultrasonic appliance cleaner. Product-scope limits, approved aggressive claims,
  appliance mix, old-method "enemy", competitor playbook (research/analysis.md §6), cartoon formats.

Every deliverable is 1 static per concept (no variations) in ONE size, 4:5 (1088x1360, feed), rendered once
with `--layout feed` (the default; user rule 2026-10-18: no 9:16) via `--provider auto` (Kie.ai ~$0.05/ad, else OpenAI high ~$0.22/ad; see §1). The file is
`<id>_vN.png`. GIFs only for statics the user approves.

## DentalPULSE quality rules (user, Oct 28: supersede every older DentalPULSE rule below)

These are encoded in `ads/brands/dentalpulse/brand.json` (`program`, `copy_rules`, `quality_bar`, `font_style`, `typography`, `banned_formats`, `inspiration_rule`) and `ads/atria_pull.py inspiration`; follow them on every run.

1. **Inspiration = curated Atria pull only.** `python ads/atria_pull.py inspiration --brand dentalpulse` returns STATIC images that are currently ACTIVE, launched in the last 45 days, have run at least 7 days (everything launched in the last 7 days is excluded) and whose impressions are GROWING week over week (impression_trend rising and reach/rank improving over 7 days). It searches oral-care AND health & wellness brands (`inspiration_queries`). Contact-sheet it (`contact_sheet.py inspiration_curated.csv --by query --per 3`), read every page, and log "formats growing now" in `research/analysis.md` (section 13 has the Oct 28 read). Borrow formats and hooks from this list, not from old competitor pulls.
2. **Iterations** come from what performed well for us in the past as statics: `winners` (lifetime top-spend statics), `current`, `seasonal`. Rebuild the proven static formats (comparison table / ranking, warm lifestyle hero, giant "40% OFF" type, quote + badge, native advertorial paper photo) as real photographs, not as new gimmicks.
3. **No cartoon, animation, illustration, comic, meme or funny ads.** `generate.py` refuses `banned_formats`. Allowed: real photos, real-looking screenshots/native UI (X post, text messages, FB comment, Trustpilot card), documents/lab reports, imaging/macro photos, clean typographic layouts. Tone is serious and credible.
4. **Direct-response copy** (brand.json `copy_rules`): customer pain in their words, agitate, mechanism, proof, one clear CTA. Specific promises, numbers, imperatives. No jokes or puns.
5. **Mix: 50% dentures / 25% night guards / 25% aligners + retainers.** Tuesday 20 = 10/5/5; Friday 40 = 20/10/10. **Funnel: 70% top-of-funnel (no price) / 30% offer-driven.**
6. **Current offer (use only in the 30%):** 40% OFF sitewide, FREE shipping, FREE dental case, FREE travel bag with every order, 120-day money-back guarantee, Pod $99.95. Show the case and bag as small items next to the Pod (`denture_gift_bundle` reference).
7. **Customer language first.** Re-read `research/feedback_deep_dive.md` (Oct 28 refresh: 180 responses) before writing; bacteria (64%) and yellow stains (39%; 68% of night guard buyers) must be explicit; never promise set-in yellow vanishes in one cycle; answer the price objection with the offer and the skepticism objection with the 6-of-7 lab test + guarantee.
8. **Photoreal, not AI-looking.** Real camera light and texture, natural skin and hands, believable appliances, no glossy 3D look (brand.json `quality_bar`). Use `"style": "ugc"` for lo-fi/native photos. In QA, reject anything that looks rendered, plastic, over-saturated or symmetrical-perfect.
9. **Website typography:** Inter for headlines (SemiBold/Bold, sentence case) and body, Barlow Bold for big numbers and prices; navy #0E283C or white text; blue #1188FF as the only accent; palette from dentalpulsepro.com. Reject any ad with serif, script, rounded-cartoon or decorative lettering (except genuine handwritten-note or native-UI formats).

10. **Appliance accuracy (user feedback Oct 28).** Every concept sets `"appliance"` (`denture_full`, `denture_partial`, `night_guard`, `retainer_hawley`, `retainer_clear`, `aligner`); `generate.py` appends the correct shape description from brand.json `appliance_shapes`. If the headline says dentures the picture shows real dentures (pink acrylic gums + full tooth row); a night guard is a thick rigid horseshoe tray; a Hawley retainer has the acrylic palate plate + wire; a clear retainer/aligner is a thin tray. Never mix appliances.
11. **Real-world size (user, Oct 30; replaces the Oct 28 scale rule):** the Pod is a SMALL bathroom-counter gadget (~12 cm wide, 10 cm tall, about a large coffee mug). Held in one palm, fingers reach past its sides; on a counter it's smaller than a tissue box. A denture/night guard/retainer is about HALF the Pod's width and fits in its basin. Reject any ad where the Pod looks like a big machine or dwarfs a hand/head. Free gifts in offer shots stay clearly visible (travel bag about the Pod's size, case about half).
11b. **Different-looking ads (user, Oct 30):** each concept recreates ONE specific ad from this run's Atria research (rival or curated inspiration) as a layout reference: save it to `reference/benchmarks/rv_ref_<slug>.jpg`, register it in brand.json `benchmarks`, and set `"benchmark"` + `"format_ref": true`. Copy that ad's structure, type treatment, background and copy PATTERN (adapted to our angle, mostly dentures), never its words. When the reference's text is not a top headline (signs, split labels, bars, quotes), render the text in the image instead of using `overlay`. No two ads in a batch share a reference or a background/composition; QA the contact sheet for sameness.
12. **One fixed headline size.** Designed ads use `"overlay": {"headline", "sub"?, "pos": "top|bottom", "tone": "dark|light"}`: `generate.py` sets the text itself in real Inter Bold at 72 px (sub line Inter Medium 38 px), max 3 lines (about 60-70 characters), same size on every ad (fonts in `ads/fonts/`). The prompt must not contain the headline; the model leaves a calm 34% band for it. Native screenshots (X post, FB comment, Trustpilot, iOS) keep their own UI text and have no overlay. `headline` in concepts.json equals the overlay headline.
13. **Bacteria and yellow stains on EVERY ad.** The picture must show it (yellow/stained/filmy appliance macro, brown debris water, petri/UV biofilm, yellow vs clean pair; offer ads too) and the headline names bacteria, yellow/stain/film or what is left on the appliance. Use the feedback sheet's words (`research/feedback_deep_dive.md`).
14. **No gimmicks that need explaining** (pharmacy-bottle parodies, joke labels, puzzles). Two-second rule: one idea, instantly clear.

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
- **Angles** (audience × pain × format): Nurse / 12-hour shifts ~35%, Travel incl. Disney + Europe ~25%, Plus-size women ~20% (mostly mash-ups: plus-size nurse, plus-size at Disney), test slot ~20% for new pain points. Pains (from 18,452 feedback answers, `research/feedback_pain_points_2026-10-28.md`): plantar fasciitis first (27%), bunions second (9%), then "no pain, just comfort" (22%, fastest-growing), arthritis, tired feet from standing, neuropathy, back/knee after shifts; test slot: wide feet (rising), Morton's neuroma / burning ball of foot, flat feet, swelling. Name what she already tried (insoles first, then pills, stretching, ice, running shoes/Hokas) and use her phrases. Guardrails: never promise fit or "extra wide", say "built for 12-hour shifts" not "no pain for 12 hours", set expectations for the rocker sole. ≥60% lead with a named pain in the customer's words. **Teacher is paused**: write none unless `atria_pull.py current` shows a teacher ad at ≥$300 spend and ≥1.8 ROAS (then say so in Slack). Reweight each run from Atria `current`, verdicts and the seasonal pull.
- **Research every run, in this order:** (1) our statics with **≥$10k spend** (`winning_statics.csv`, refresh with `atria_pull.py winners`) and `current` + `seasonal` winners: write down their patterns; (2) the customer voice in `research/feedback_pain_points_*.md` (re-mine the Drive feedback sheet monthly; aggregates and short anonymous quotes only) and our **winning video scripts** (`research/data/video_transcripts.md`) for hooks, objections, story beats, customer phrases; (3) **`atria_pull.py wellness`**: direct-response ads from ANY health & wellness brand, chosen OBJECTIVELY from data (user rule 2026-10-28): search only health & wellness category keywords (`wellness.queries`; never our angle words like nurse/travel/Disney, which belong in our copy, not the search); filters image, active, launched ≤45 days, running 10+ days, impressions rising, direct-response copy (offer/CTA/guarantee/number/problem hook), off-niche dropped, max 2 per brand; ranked by 7-day impression growth (`growth_rank`). Take formats from the TOP of that ranked list in order; skip a row only if its format is already in the ledger, it relies on another brand's licensed IP, or it needs a claim we can't make, and log the skip reason. No hand-picking by taste. Contact-sheet it (`contact_sheet.py inspiration_wellness_45d.csv --per 40`) and **Read every page**; (4) write a dated "formats found this run" table in `research/analysis.md` (format, brand, category, days running, why it works, our version) and the shared patterns of our winners vs the inspiration.
- **New formats every run.** Formats come from THIS run's Atria research, not from a fixed list. Each concept sets `format_name` (slug) and `format_source` (inspiration brand, category, days running). A format already in `research/format_ledger.json` may not be reused; only our own proven layouts (`wellness.proven_layouts`, named `proven:<slug>`) may repeat, max ~30% of a batch. Run `python ads/format_ledger.py --brand <b> check --week <folder>` before rendering (must print OK) and `add --week <folder>` after shipping. `based_on` names the inspiration ad with its growth rank and numbers (growth_7d, days running) AND the winner/script it is paired with, plus why.
- **Copy: direct response.** Pain in her words → agitate (what she tried, what it cost) → mechanism (arch, heel cushion, wide toe box, grip) → proof (peer, number, story) → one offer line. Headline ≤ ~8 plain words, specific (a number, a place, a shift length). No puns.
- **Look: realistic, NOT AI.** Real phone-photo scenes (uneven light, skin/fabric texture, grain, imperfect framing) or clean graphic layouts copied from the inspiration ad, never glossy composites. Full-bleed: the headline sits ON the image (sky, wall, floor), never in a separate band stacked above a photo. Natural walking stance (mid-stride, not two shoes planted side by side). **Poppins** for every typeset word (ExtraBold headlines, SemiBold labels); never condensed (Impact/Bebas/Anton) or script fonts; handwriting only on a real object (sticky note, cardboard sign). Legibility for women 60+ still applies. In QA, re-render anything with the wrong font, an invented slogan, or a headline that doesn't flow into the image.
- **Offer** (~30% of a batch): "40% OFF" + "FREE SHIPPING" + "30-DAY MONEY-BACK GUARANTEE"; "HSA/FSA ELIGIBLE" + "UP TO 30% SAVINGS" may replace or join it. A line, pill or seal, never the whole ad. Black Friday week uses its own offers (`program.black_friday_week_2026_11_09`).
- **Readable, uniform text (user 2026-10-28).** All text black, deep navy or white; never purple or other colored words (an accent color may only fill a pill/bar/block behind white text). Every line of one headline is the same size, weight and color: no oversized first word, no smaller second line, no regular/bold mixing. Supporting text is one uniform, large size. QA: re-render any ad with colored words, a headline with mixed sizes, or small text.
- **Cartoon/animation statics: no quota.** Only when this run's inspiration research (same criteria: image, active, launched ≤45 days, 10+ days running, health & wellness) surfaces an illustrated/animated static worth borrowing; it then counts as a new format in the ledger (`program.cartoon_rule`).
- Render one 4:5 per concept with the default `--provider auto` (Kie.ai gpt-image-2 at 2K, ~$0.05/ad; OpenAI at high quality, ~$0.22/ad, only when `KIE_API_KEY` is missing). Older rules below still apply where they don't conflict.

### 1a. Atria research: exact criteria per pull (user, 2026-10-30)

Every pull writes a CSV to `research/data/`; contact-sheet it and **Read every page** before writing.

| Pull | What it answers | Filters (exact) | Ranking | Output |
|---|---|---|---|---|
| `winners` | What has worked for us, ever | our ad account; statics only (IMAGE); lifetime spend ≥ $5k (`--min-spend`); since 2024 | spend, high → low | `winning_statics_raw.csv` (+ headline and primary text) |
| `current` | What works for us right now | our account; any format; last 30 days; spend ≥ $300; ROAS ≥ 1.8 | spend | `current_winners.csv` |
| `rising` | Our new ads taking off | as `current`, but only ads launched in the window | spend | `rising_winners.csv` |
| `seasonal --week W` | What won this time last year | our account; same ISO week last year ±7 days | spend, top 15 | `seasonal_<week>.csv` |
| `losers` | What to avoid | our statics; spend < $200; paused at ad level; last 12 months | spend, low → high | `losing_statics.csv` |
| `wellness` | New formats to borrow (objective) | Atria ad library; **health & wellness category keywords only** (`wellness.queries`, never our angle words); image; **active**; launched ≤ 45 days ago; running ≥ 10 days; impression trend **rising**; title/body has a direct-response signal (%, $, free, guarantee, money-back, buy N, today, sale, pain, question…); off-niche words dropped (`wellness.exclude`); max 2 ads per brand | **7-day impression growth** (places climbed), then impression share → `growth_rank` | `inspiration_wellness_45d.csv` |
| `rivals` | What Hike + Stepprs are doing | `core_competitors`; image **and** video; active and inactive; both Atria orders (most impressions, best match); brand-matched; full copy kept | competitor → active first → days running (longest first) | `core_competitors_<date>.csv` |
| `competitors` | Wider category | `competitor_brands` + `inspo_queries`; image and video | impression percentile | `competitor_ads.csv` |

How to use the wellness list: take formats **from the top of `growth_rank` in order**. Skip a row only if
its format is already in `research/format_ledger.json`, it depends on another brand's licensed IP, or it
needs a claim we can't make; write the skip reason in `analysis.md`. No picking by taste. A long-running
ad (60+ days, still active) is a stronger signal than a new one; an ad whose impressions are falling is a
weak one even if it is old. Note for each borrowed format: brand, category, days running, growth, and why it works.

**Inspiration priority (user, 2026-10-30, after a batch looked too plain).** The wellness growth list alone surfaced
off-target ads (dog pads, lenders) and our concepts drifted to plain white "product + labels" layouts. Order now:
(1) Hike + Stepprs highest-impression and longest-running ACTIVE statics (`rivals` + contact sheet), (2)
`competitors` top-impression statics, (3) the wellness list, using only rows that are visibly direct-response and
eye-catching on the contact sheet: bold color fields, huge type, real feet/people, text written on a body part or
object, sticky notes, warning tape, strike-through self-talk, split before/after, huge price/offer. Plain white
product-and-callouts layouts only when they are our own proven winners. Every batch: at least half the concepts
use one of these high-energy devices.
**Nurse colors (user, 2026-10-30):** nurse/healthcare concepts use ONLY Black/Purple, Black/White, All Black,
White Blue. **Text spacing:** every text element ≥7% of the width from every edge, with clear space around it;
QA rejects text that touches or crowds an edge. **Shoe contrast:** never a dark shoe on a dark background; light or mid-tone backgrounds so the shoe is clearly visible.

### 1b. Our own copy that works (read EVERY run, before writing a single headline)

1. **Winning statics' copy**: `winning_statics.csv` (headline + primary text of every ≥$5k static) and
   `current_winners.csv`. Write down the 3–5 copy patterns that repeat (e.g. "12-hour shift" in the
   headline, named audience, testimonial-first primary text, checklist ✅ rows, $ strike-through).
2. **Winning briefs and scripts**: the Notion "Scripts 2026" winning briefs, the angle databank
   (`research/data/notion_angles.md`) and our winning video scripts (`research/data/video_transcripts.md`):
   hooks, objections, story beats and the exact customer phrases. Keep a dated digest in
   `research/winning_briefs.md` (refresh from Notion each Friday run).
3. **Customer voice**: `research/feedback_pain_points_*.md`, Trustpilot 5★ language, the copy playbook
   (`research/copy_playbook_nurse_travel.md`).
4. Every concept's `based_on` names the winning static, brief or script line its copy comes from, and
   `headline` must trace back to a real pattern or phrase from 1–3. Reference images give the LAYOUT;
   the WORDS come from here.

### 1c. Core competitors (EVERY run, user rule 2026-10-30): Comfort Wear → Hike Footwear and Stepprs; DentalPULSE → Zima Dental and Sonic Dental (brand.json `core_competitors`; DentalPULSE notes in `research/core_competitors.md`)

They are our biggest competitors and write very direct-response copy. Each run:
1. `python ads/atria_pull.py rivals`, then contact-sheet their statics and Read every page.
2. Read the full copy of every **active** ad; transcribe (Atria `transcribe_library_ad`) their 2–3
   longest-running active videos if not already done.
3. Update `research/core_competitors.md` with a dated section: hooks, offers and guarantees, proof devices
   (numbers, testimonials, doctors, studies), claims, formats, CTA style, and **what changed since the last
   run** (new ads, ads they stopped).
4. Write at least ~20% of each batch as direct answers or upgrades to their strongest current angles,
   matching their DR intensity (specific numbers, named pain, agitation, risk reversal) with OUR approved
   claims only: never their claims we can't back, their brand names in a negative way, or their logos.

### Image provider and quality (user, 2026-10-30)

`generate.py --provider auto` (default): Kie.ai (`KIE_API_KEY` or `KIE_AI`), same gpt-image-2 model, 2K, ~$0.05/ad;
falls back to OpenAI at high quality (~$0.22/ad) when the key is missing, and says which it used. Kie has
no 4:5, so it renders 3:4 and crops to 4:5 (the prompt keeps text and product off the top/bottom 5%).
Quality is checked exactly as before (QA list in §4). Tested 2026-10-30 (HD_02 text-heavy x-ray, HD_04 product hero): text sharpness and shoe fidelity matched OpenAI
high, so Kie is the default. If one Kie render fails QA, re-render that one with `--provider openai`. Never drop to medium quality to save money: use Kie instead.

- Read `brand.json`, `research/analysis.md` and `feedback.json` (approved/rejected and why).
- **Iteration runs**: `atria_pull.py current` (last `iterate_when.days` days, spend ≥ `min_spend`,
  ROAS ≥ `min_roas`, any format), `rising` (same filter, only ads launched in the window), and
  `seasonal --week <current week>` (top spenders by spend in the same window last year, ±7 days).
- **Net-new runs**: DentalPULSE: `atria_pull.py inspiration` (curated criteria above) is the inspiration source; other brands: `atria_pull.py wellness` (brands with a `wellness` block; else `inspo`), and refresh `competitors` + the playbook when the brand has
  one (new long-running formats only). Iteration runs also pull `wellness` for their big-swing formats (not DentalPULSE: it uses `inspiration`).
- **Every run (DentalPULSE; the Oct 28 criteria above replace the competitor/ultrasonic pulls as the inspiration source, keep this for our own winners)**: analyze our own top-spend statics (`winners` + `current`, with the
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
used (a NEW format from this run's inspiration research, see the format ledger), and re-aim winners at the other
products/use cases in `program.mix`. Name the new format in `angle`. 2–4 per strong ad, at least 8
formats. `"group": "iteration"`.

### Net-new batch: mostly net new

- `netnew_batch.net_new` concepts `"group": "net_new"`: new angles, personas and formats weighted to
  `grow_personas`; every format new to the format ledger and discovered in this run's research (`wellness` pull, else `inspo`; plus, if present, the competitor
  playbook.
- `netnew_batch.winning` concepts `"group": "winning"` in proven formats for `winning_personas`.
- No angle repeats from this week's iteration batch or any earlier folder.

### Rules for every batch

- **Quality benchmark (user rule, Oct 13)**: every concept sets `"benchmark"` to the closest key in
  `brand.json` → `benchmarks` (the brand's own top statics in `reference/benchmarks/`); `generate.py`
  attaches it as a style/quality reference and adds `quality_bar`. Write prompts the way the winners look:
  shoe as the hero (35–60% of the frame, often a pair), tight legs/feet crops, one huge heavy headline,
  ≤3 solid pills/blocks/arrows. Default render: `--provider auto` (Kie.ai 2K, else OpenAI high). In QA, put each render next to its
  benchmark and re-render anything that looks like generic AI stock, has a small shoe or a weak headline.

- **Mix**: follow `program.mix` exactly (count it before rendering), plus the funnel split
  (`program.funnel_mix`; default ~65% top-of-funnel with no price, ~35% offer-based; DentalPULSE 70/30) and `copy_rules` / `naming_rule`.
  Also apply `program.angle_rules` (winning angles, mix-and-match, foot-pain share), `program.offer`
  (offer-stack share and exact wording) and `colorway_priority` (best sellers vs test colors) when the
  brand has them; count each before rendering.
- **Variety (user rule)**: every concept in a batch uses a different format, and (Comfort Wear) every format is new
  to the ledger and comes from this run's research. The list below is history/examples, not a menu: the
  top-impression category formats (analysis.md) and the briefs' formats: insult/shock headline + sticky-note
  offer, lo-fi real photo with minimal text, imaging/petri/microscope proof, price-anchor replacement,
  value-stack bundle flat-lay, big quote over product, real-world sign, advertorial article card, native UI
  (iOS reminder, cart, texts), founder letter, stat pictogram, news split-face, hand + arrows offer,
  ranking grid / report card, post-it confession, timeline, gift static (cartoon formats only for brands without `banned_formats`; DentalPULSE: never).
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
- **Spanish** (if enabled; Comfort Wear: disabled since 2026-10-28): written natively as US Latinos talk (`tú`, Mexican-leaning everyday
  phrasing, family/coworker framing, US number format), never translated or Spain-style.
- **Native formats (user rule)**: testimonials/reviews use `"format": "fb_comment"` or `"trustpilot"`;
  tweet-style ads use `"format": "x_post"`. Give exact names, handle, text, date and counts. Review text
  comes from real customer language (survey/reviews); names first name + last initial; no TrustScore,
  overall rating, "Verified" badges or platform logos.
- **Cartoon/animation formats: never for DentalPULSE (banned Oct 28, brand.json `banned_formats`).** For other brands: Use one ONLY when this run's
  inspiration research (same criteria: image, active, launched ≤45 days, 10+ days running, health & wellness)
  surfaces an illustrated/animated static worth borrowing; it then counts as a new format (`format_name`,
  `format_source`). Brands without that rule keep their own share. Styles available via `"format"`: `cartoon_3d`,
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

Default `--layout feed` (user rule, Oct 18): one native 4:5 render per ad via `--provider auto` (see §1 Image provider)
(headline upper third, product/scene large in the middle, copy or offer lower; edge-to-edge scene, at least
6% margin around text). No 9:16 is made. Older layouts (`native` 9:16 + 4:5 re-layout, `extend` outpaint)
remain available by flag but are not used. `generate.py` center-crops instead of stretching when the API
returns another aspect ratio, so the shoe is never squashed. If the image API rejects a prompt for safety
(e.g. chemicals + mouth = "self-harm"), reframe the visual and retry.

Cost: Kie.ai 2K ≈ $0.05 per ad; OpenAI high ≈ $0.22 (measured 2026-10-27/30); OpenAI medium ≈ $0.08 (not used: quality too low). Check `review.py cost` after every
batch and report cost per ad. GIF ≈ $0.14.
Shell gotcha: never `pkill -f`/`pgrep -f` a pattern that
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
- any purple or other colored text, or a headline whose lines differ in size or weight (Comfort Wear rule 2026-10-28);
- a native format that doesn't look like the real platform, or competitor logos;
- (DentalPULSE) wrong or mixed appliance shapes, an appliance as big as the Pod, tiny/unclear gifts, headline sizes that differ between ads, no visible bacteria/yellow, a blank or empty photo area, anything that looks AI-generated or rendered (plastic skin, glossy 3D, melted/duplicated letters, impossible hands or appliances, oversaturated glow), any cartoon/comic/joke tone, copy that isn't direct response, fonts other than Inter/Barlow (serif, script, rounded display), an offer that doesn't match the current offer exactly, or a concept whose appliance/funnel mix is off (50/25/25, 70/30).
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
   (iterations) · new formats and their inspiration ads · angle and pain split · offer count · Spanish count (if enabled) · GIF candidates · image cost.
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
- Formats: NEW every run, discovered in this run's inspiration pull (`atria_pull.py wellness` or `inspo`),
  checked with `format_ledger.py check`. Cartoon/animation only when the research surfaces one (no quota).

Check today's weekday in America/New_York:
- Tuesday → ITERATION batch: folder weeks/<current ISO week>-tue, ids T<ww>_nn_slug, <n> concepts
  (<mix counts>), ONLY iterations of `atria_pull.py current` + `seasonal --week <current week>`
  winners, big-swing NEW formats from this run's inspiration research; based_on names the source ad.
- Friday → NET-NEW batch: refresh `atria_pull.py competitors` (if the brand has competitor_brands);
  folder weeks/<coming ISO week>-fri, ids W<ww>_nn_slug, <n> concepts (<mix counts>): ~80% net_new
  (grow personas, all formats new to the ledger), ~20% winning personas. Don't repeat angles
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


## 7. Live requests from reference images (user, 2026-10-27 to 10-30)

Most live work is: the user pastes 1-5 ads from other brands ("make these for our shoes", "nurse version",
"60% off version", "make it in red and White Blue"). Workflow and lessons:

**Setting up**
- Save each reference to `reference/benchmarks/<prefix>_ref_<slug>.<ext>`, register it in `brand.json` →
  `benchmarks` with a `use_for` description, and set `"format_ref": true` on the concept. generate.py then
  attaches it as a LAYOUT reference and forbids copying any of its words or adding unrequested headlines.
- If an image only came through in chat (not saved as a file), describe the layout in the prompt instead.
- Words come from §1b (our winners, briefs, scripts, reviews) and §1c (Hike/Stepprs patterns), never from the
  reference. State what you changed from the reference and why (claims, prices, codes, counts, logos).
- One folder per request batch: `weeks/<YYYY>-W<ww>-<tag>` with a short id prefix (e.g. `O48_`, `TF_`, `HD_`).
- Black Friday letter/notice formats: `"style": "letter"` (plain typed note, big body text, bold key phrases).
- Brand logo on an object (travel bag, shoe box): `"logo": true` (attaches `reference/logo_comfortwear.png`).

**Variants of an approved render** ("same but red", "60% version", "nurse version", "pastel background")
- Register the approved PNG as `benchmarks.approved_<ID>` and create a new concept with
  `"benchmark": "approved_<ID>", "copy_of": "<ID>_vN"`; end the prompt with "Compared with the second attached
  image: identical …; only X changes." generate.py then copies that render exactly except the change.
- A fix of the same concept bumps the version (`_v2`, `_v3`); a new color/offer/persona is a new id.
- When the shoe color changes, adapt accent colors to match the shoe unless the user says otherwise; offer it.
- Drop the approved-render benchmark when it is the cause of the problem (it pulled bodies slim and shoes long).

**QA lessons from these rounds (check every image for these)**
- The model copies the reference's own words or repeats our headline (top + bottom, typed text over handwriting,
  a question both as headline and in the card). Re-render with "the ONLY text is …".
- Curved/ring text and long wobbly words garble (BLACCK, WALKINIG, BLACLE): use straight text in badges and add
  "spell X exactly".
- Top-down shoes come out elongated: use a three-quarter view.
- "Worn-out / before" shoes come out as OUR shoe or with brand-like stripes/swooshes: say "plain generic unbranded
  lace-up sneaker, NOT a sock-knit shoe, no stripes or logo shapes".
- Plus-size models come out slim unless the body is described explicitly (US size 22-24, full thighs/calves/hips,
  belly, crop that shows the figure).
- Pairs drift to the frame edge or overlap: give width % and margin ("each ~35% of width, 6% margin").
- Small inset photos often show a wrong shoe; the hero shoe must be checked separately from insets.
- Theme-park scenes may add a castle: say "no castles, characters or park logos" every time.

**Compliance defaults (flag, don't silently drop)**
- Competitors: names in text only, no logos; compare design features, never unverifiable claims ("collapses after
  2 months"); no made-up scores or customer counts.
- Prices/discounts must add up: flag "$120 → $59.95" next to "40% OFF" (that is ~50%), and stacked codes
  (60% + 10% = ~64%, not 70%). Strike-through price is $120 (user, 2026-10-29), never $90.
- Native FB/Reddit/X posts with invented names: flag that real quotes (with permission) are safest.
- Medical framing: no cure/relief/prevents-falls claims; condition words only in a customer quote; "sensitive feet"
  not "your neuropathy" (Meta personal-attributes policy).
- Source labels: "ComfortWear Comfort Guide", never a fake news or review site; HSA/FSA: "eligibility may vary".

**Delivering**
- Send every checked image with SendUserFile (`display: render`) as soon as it lands, with a table of what it says
  and what changed; hold back and re-render failures instead of sending them.
- When asked for "everything revised", copy the final version of each requested fix/variant into
  `revised_<date>/` (numbered, plain-English names + README index), zip it and send the zip (images stay
  gitignored there; the week folders keep the originals).
