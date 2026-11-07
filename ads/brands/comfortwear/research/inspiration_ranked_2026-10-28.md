# Objective inspiration pick, 2026-10-28 (for weeks/2026-W45-nurse-travel)

**Method (data only, user rule 2026-10-28).** `python ads/atria_pull.py wellness --brand comfortwear`:
34 health & wellness category keywords (no angle words like nurse/travel/Disney), image ads, active,
launched in the last 45 days, impressions rising (Atria `impression_trend=rising`), running 10+ days,
direct-response copy (offer, CTA, guarantee, number or problem hook), off-niche excluded, max 2 per brand,
ranked by 7-day impression growth (`growth_7d` = places climbed in Atria's impression rank). Result:
2,065 rising ads → 1,618 dropped (<10 days), 98 off-niche, 52 not direct-response → **191 ranked**
(`research/data/inspiration_wellness_45d.csv`).

**Selection.** Walk the list from #1 and take each ad's format unless: (a) the format is already in
`format_ledger.json`, (b) it repeats a format already taken in this batch, (c) the filter missed an
off-niche ad (pets, fashion, apps), (d) it needs an offer, claim or IP we can't use. First 20 that pass.

| Rank | Brand (category) | Growth 7d | Days | Format | Decision |
|---|---|---|---|---|---|
| 1 | Glov Beauty (lymphatic) | +348 | 11 | illustrated 2x2 progress panels + product | **TAKE** → NT45_01 |
| 2 | OrthoFlexx (insoles) | +294 | 11 | product on white + 4 arrow callouts | skip (a) proven callouts |
| 3 | FEM+ (lymphatic) | +188 | 16 | "Stop calling it X" reframe | skip (a) blame_shift |
| 4 | Cymbiotika (gut) | +161 | 37 | body close-up + one mechanism sentence | **TAKE** → NT45_02 |
| 5 | BRUNT Workwear (insoles/boots) | +158 | 21 | single-feature macro photo + hand arrow + label sticker | **TAKE** → NT45_03 |
| 6 | OrthoFlexx (insoles) | +145 | 11 | product + question headline | skip (a) question_headline |
| 7 | Inner Dose (nerve) | +137 | 11 | ingredient photo-circle grid + offer seal | **TAKE** → NT45_04 |
| 8 | PuppyPad | +132 | 19 | — | skip (c) pets |
| 9 | Wilson | +119 | 12 | — | skip (c) fashion |
| 10 | TheraPexa (massager) | +119 | 11 | Instagram "ask me anything" Q&A over product photo | **TAKE** → NT45_05 |
| 11 | Nutrition Geeks (supplements) | +112 | 10 | row of symptom sketches → arrows → solutions | **TAKE** → NT45_06 |
| 12 | Vivobarefoot (footwear) | +108 | 11 | contrarian "X is a myth" over gritty photo | **TAKE** → NT45_07 |
| 13 | NeuroMD (nerve) | +107 | 21 | illustrated morning before/after scene | **TAKE** → NT45_08 |
| 14 | Ancient Roots (lymphatic) | +106 | 34 | week panels | skip (b) = #1 |
| 15 | Dog is Human | +106 | 10 | — | skip (c) pets |
| 16 | Inno Supps | +100 | 10 | — | skip (c) sexual |
| 17 | Everstride (compression) | +92 | 10 | seasonal (Halloween) scene + offer circle | **TAKE** → NT45_09 |
| 18 | GroundingWell | +89 | 36 | email apology | skip (a) email/apology |
| 19 | NeuroMD | +83 | 21 | quote + benefit rows | skip (a) quote_plus_pills |
| 20 | Comrad Socks (compression) | +74 | 11 | legs on a bold solid color, condition named | **TAKE** → NT45_10 |
| 21 | Dr. Squatch | +73 | 10 | free bag | skip (d) gift offer |
| 22 | RenewaSkin | +71 | 12 | doctor + before/after | skip (d) endorsement |
| 23 | Senior Health Guide (circulation) | +70 | 43 | handwritten notebook log photo | **TAKE** → NT45_11 |
| 24-26 | Dr. Squatch, Sorviq, Viasox | +69/+59/+58 | | gifts, BOGO, back in stock | skip (d) |
| 27 | Stepprs (neuropathy insoles) | +58 | 12 | symptom metaphor illustration + guarantee headline | **TAKE** → NT45_12 |
| 28, 32 | Carol Bennett | +56/+53 | 20-21 | feet photo + red circle | skip (a) cause_split_red_circle |
| 29-31 | Clarifion, Nifora | +54/+53 | | last pallets, price letter, sticky offer | skip (a)/(d) |
| 33 | Rosabella | +51 | 42 | orbit callouts | skip (a) |
| 34 | Senior Health Guide (circulation) | +50 | 44 | real photo, no text at all (story in the post text) | **TAKE** → NT45_13 |
| 35-37 | Gripzilla, Speak, Inner Dose | | | progress / app / repeat | skip (b)(c) |
| 38 | Hyggear (hammer toes) | +45 | 12 | product worn on foot + dark offer panel | **TAKE** → NT45_14 |
| 39 | Viasox | +44 | 12 | BOGO | skip (d) |
| 40 | BioRoot Labs (inflammation) | +43 | 11 | photo of the enemy product + question | **TAKE** → NT45_15 |
| 41-46 | ATTAQUER, Zippra, Naked Harvest, Laundry Sauce, Pure Living, ComfoFeet | | | fashion, comparison table, certification, split, Halloween repeat | skip (a)(b)(c)(d) |
| 47 | Restelle (sleep patch) | +37 | 10 | two parallel lines over a real photo ("Nine hours she needed. Nine hours she got.") | **TAKE** → NT45_16 |
| 48-50 | Sorviq, TheraPexa, Almla | | | BOGO, notes app, pet | skip |
| 51 | The Modern (foot neuropathy) | +31 | 16 | "Sensitive content" blur overlay | **TAKE** → NT45_17 |
| 52-61 | Rosabella … Armadilo | | | mascot, claims, offers, pet, sticky, awards, strikethrough | skip (a)(c)(d) |
| 62 | Sarah Peekmill (circulation) | +21 | 11 | X-ray with red arrow | **TAKE** → NT45_18 |
| 63-64 | Shinzo, Rachel Whitfield | | | fashion, no-text repeat | skip (b)(c) |
| 65 | Protalus (insoles) | +19 | 23 | worn shoes from behind, "If your heels lean like this…" | **TAKE** → NT45_19 |
| 66-72 | Nuflos, Pferdegold, Holistic Healing, Flowell, The Modern, D&D, Pawira | | | offer, horse, no-text repeat, parallel-line repeat, sticky callouts, off-niche, copycat claim | skip |
| 73 | Seven Minerals (magnesium) | +17 | 21 | product big in foreground, person doing the activity behind | **TAKE** → NT45_20 |

**What the fastest-growing statics share:** (1) one problem named in plain words in the headline, often a
question or a reframe; (2) a real-looking photo or a simple illustration, rarely a studio composite;
(3) a visible mechanism (circles of ingredients, an X-ray arrow, a macro of the feature, ants for tingling);
(4) a progression or contrast (day 1 → week 4, before/after morning, today/tomorrow); (5) the offer as one
seal or panel, not the whole ad; (6) many run long body copy with an image that does only one job.
