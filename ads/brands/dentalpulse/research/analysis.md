# DentalPULSE: creative research (Oct 2026)

Sources: Atria (account "Dentalpulse": current winners, rising, inspo, seasonal, lifetime winners/losers in `data/`),
the post-purchase survey (about 165 responses, May 4 to Oct 11 2026; only aggregates and short anonymous quotes kept
here), the product pages, and competitor positioning (Zima Dental, Sonic Dental, oPro, GuruNanda, Novapod).

## 1. What's winning now (last 30 days, ≥$300 spend, ROAS ≥1.8): 15 ads

| Theme | Example (headline) | Spend | ROAS |
|---|---|---|---|
| Lab/comparison video ("we tested 7 pods") | "6 of 7 pods can't remove bacteria" / "6 of 7 pods leave live bacteria" | ~$17.5k across 7 ads | 1.8–3.7 |
| "You've been lied to" (brush + tablet is outdated) | VID_DEN24 | $4.5k | 1.97 |
| Native advertorial static (Ray, 71, retired machinist; "$2,400 dentures quote vs a drawer of receipts") | "read this before you consider ultrasonic cleaners" | $3.4k (2 ads) | 2.9–3.0 |
| Rankings bar chart static | "Top 7 Ultrasonic Cleaners for Dentures" | $0.7k | **3.28** |
| Anti-tablet ("evil Polident", nostalgia) | DEN226 | $1.0k | 1.91 |
| Offer static | "40% Off + Free Gifts" / "Half price today only" | $1.6k | 1.9–2.1 |

Takeaways:
- **Dentures carry the account.** Almost all spend sends traffic to the denture listicle. Night guards, retainers and aligners are under-tested, which is the room for big swings.
- **Comparison framing wins**: "we tested them so you don't have to", ranking charts, kept-vs-returned receipts, us-vs-them. Survey switchers (about 15% already owned another pod) confirm the pain.
- **Lo-fi native beats polished.** The advertorial static and the receipts photo outperform the designed offer tiles.
- Anti-tablet works as a second pillar: most buyers come from Polident or other tablets plus a brush.

## 2. Survey: who buys and why

- **Appliance**: dentures and partials about 55%, night guards about 22%, retainers about 13%, aligners/Invisalign about 6%, plus sleep-apnea, snore and tongue devices.
- **Age**: mostly 60+. Night guard owners skew 50–60. A few retainer and aligner owners are 20–30.
- **Before**: tablets (Polident, Efferdent, Steradent) plus a brush dominate. Others: hand soap, toothpaste, vinegar, peroxide, and another ultrasonic pod (Amazon, Zima, Novapod, "a cheaper version").
- **Reasons to buy**: bacteria (by far the top), yellow stains, food debris, smell, plaque/tartar, adhesive residue.
- **Frustrations, in their words**: "You could still see food on the denture"; "Half the time when I took them out in the morning they still hadn't cleaned them properly"; "Time consuming getting old adhesive off"; "My old night guard looked gross yellow and cloudy"; "Tablets made the retainer fragile"; "Always seeing something, like a film, left on my appliance even after brushing."
- **Objections**: price (most common, especially on a fixed income), skepticism ("too good to be true", "fake reviews", "every brand is the same"), "where is it made", and doubt after other pods failed.
- **Wins, in their words**: "Now it is as white as when I first got it! My husband noticed they were white again"; "My retainer is clear again!"; "Retainer clear not milky"; "No white film!"; "Much cleaner without scrubbing"; "Certainly cleans all the residue from denture paste"; "My night guard is noticeably cleaner and brighter"; "No more smell."
- **Who noticed**: mostly "no one" (it's private). When someone did, it's a husband, wife or grandchildren, so spouse proof is believable and rare.

### Negatives to design around (1–3 ratings)
- **Old yellow night-guard stains not removed** (several mentions). Don't promise to reverse set-in yellowing. Frame as preventing buildup and getting clearer over time.
- **"No difference from my $30 Amazon pod" / "every brand is the same."** The comparison angle has to show why this one is different (power, build, daily use), not just say it.
- **Noise** ("loud screeching"), **doesn't heat the water**, **upper denture or apnea device doesn't fit** (push Pod Max for big appliances), and units dead on arrival or not received.
- **Feeling misled by ads** ("does not come out as clean as in the advertisements"). Keep visuals believable: realistic appliances, no miracle before/afters.

## 3. Competitors (positioning only; never named or shown in ads)
- **Zima Dental (Dental Pod / Pod Pro)**: the category leader. "UK's first", 42–47 kHz plus UV, award badges, about $140–170. Weak spot per reviews: stains on older appliances.
- **GuruNanda**: cheap ($9–30) 45 kHz plus UV, three cycles, sold with foam. It appears in DentalPULSE's own competitor video.
- **oPro / Sonic Dental / Novapod**: sports-guard and aligner-focused pods. Novapod ("Ultra Duo") appears in the survey as a previous cleaner.
- **Gap DentalPULSE can own**: dentures plus every other appliance in one device; tap water only (no tablet subscription); "built to run every day" (durability is the category's top complaint).

### Ad library (Atria inspo, rising image ads in the last 30 days; `data/inspiration_raw.csv`, 288 ads)
- **Zima Dental** is running "The $30 version breaks in a month. The Dental Pod doesn't." (durability) and "Trusted by 20,000+ Dentists." Our durability and switcher angle has to be sharper and more visual: receipts, kept-vs-returned, real fails from the survey.
- Implant clinics ("Done with dentures?", "No more dentures") target the same 60+ feed. Counter with "keep the dentures you paid for looking new."
- Oral-care DTC brands (Hismile, Boka, LIVFRESH, The New Find) win with bundle offers ("Buy 3, get 5 free"), "the last breakthrough was in 1914" history hooks, and dentist-formulated framing. The history hook matches our own DEN226 nostalgia winner.

## 4. Personas (brand.json → personas)
- **Winning:** denture_wearer, switcher.
- **Grow (big swings):** night_guard, retainer, aligner, denture_caregiver.
- Every batch covers all four appliance types.

## 5. Claims and mix (user, Oct 11)
- **Approved; use aggressively:** "Eliminates 99.9% of bacteria", "clinical-grade", "42,000 Hz", "6 of 7 pods leave live bacteria (90-day lab test of 7 leading cleaners)", star ratings ("Rated 4.8/5", no counts), "tap water only, no tablets".
- **Approved later on Oct 11:** dentist endorsements (no counts), the Clinicians' Choice badge, the 120-day money-back guarantee, and the 40% OFF sale at $99.95 (current price).
- **Still unconfirmed, keep out:** shipping promises, customer/unit/dentist/review counts, a strike-through "was" price, other awards and press logos. The source list is brand.json → `approved_claims` and `claims_to_avoid`.
- **Appliance mix for every batch:** 50% dentures, 25% night guards, 25% aligners/retainers.
- **The enemy is the old routine, named directly:** toothbrush, Polident and Efferdent tablets, vinegar, bleach, soap, peroxide, denture cup. Competitor pods stay unbranded.

## 6. Competitor and dental-brand ads (Atria ad library, `data/competitor_ads.csv`, 870 ads)
Pulled with `atria_pull.py competitors` (brand.json → `competitor_brands`). Longest-running (= still paying) formats worth borrowing:

**Ultrasonic pods**
- **Zima Dental:**
  - "$60 value, on us" bundle tile (71 days).
  - "Ultimate Retainer Care" product-pattern bundle (48 days).
  - "Star of the clean girl starter pack": a numbered flat-lay of lifestyle items with the pod in the middle (18 days).
  - A woman holding up a yellow retainer vs a clear one, labeled "Before / After Zima" (11 days).
  - "Never Brush Your Retainer Again" with a feature icon list.
  - An incoming-call screen, "An exclusive offer is calling…", with decline "Stained retainers?" and accept "Clean + protected?".
  - "3x sold out / back in stock" scarcity.
  - Copy hooks: "Soaking your aligners in a cup isn't cutting it", "Does this look silly? So is brushing your retainers with a toothbrush", "This is why cleaning tablets won't finish the job".
- **Sonic Dental:**
  - Dark purple premium sale tiles with the device held on a palm under a glow ring, "Limited Time Sale" (115+ days).
  - "Der Unterschied?": hands bursting through paper holding a yellow vs a clear aligner, with a 03:00 timer.
  - "Brushing misses. Ultrasonic doesn't. Dentist-approved. Clinical-grade."
  - An "as seen in" press bar and big social-proof numbers.
  - Their best video has run 541 days: "New Year. Clean Start." (bundle).

**Other dental DTC brands**
- **Hismile:** "DO NOT F*CKING DO THIS" shock headline over a gross mouth close-up, a fake cart screenshot ("10 lip balms for $18??"), "Buy 3 get 2 free" bundles, and a price-challenge headline ("try find a better toothbrush for only $24.99").
- **LIVFRESH:** "Bad breath problem? Dentists say it's hiding below the gumline", a "LIVFRESH HELPS" icon diagram around the product, a review quote card over the product family, and "Buy 2 get 1 free".
- **Boka:**
  - A timely callout: "Using GLP-1s? Bad breath? We got you."
  - A stat claim: "Removes 7x more surface stains than an ordinary toothpaste."
  - Clean, minimal bathroom product photography.
- **Invisalign:** big split before/after faces with blue "before / after" bars, and an "FSA/HSA balance?" money angle.
- **GuruNanda:** "BETTER THAN A WISP." naming the incumbent, a giant number ("70"), and "Trusted by dentists. Loved by TikTok."
- **Cocofloss:** a wall of real Instagram comments begging for a restock (demand proof).
- **Smyle / usmile:** cart and checkout screenshots with the deal applied, seasonal scenes ("Pocket Clean for Fall"), and "Buy 1 get 1 free".

**What to take:**
1. Name the incumbent and beat it. "Better than Polident." "Brushing misses. Ultrasonic doesn't."
2. Before/after held up in hand: yellow vs clear, cloudy vs clear, stained denture vs white.
3. A shock or gross-out headline over a macro close-up ("Do NOT soak your dentures in this").
4. Native UI frames: incoming call, cart screenshot, comment wall, order confirmation.
5. A premium dark "hand + glow" product tile for offers.
6. A starter-pack flat-lay ("the denture wearer's starter pack").
7. Big-number typography (99.9%, 42,000, 6 of 7).
8. A timely callout (GLP-1 bad breath, holiday visits, New Year clean start).

## 7. Top-impression statics in the category (Atria, sorted by most impressions, Oct 13)
Pulled with `atria_pull.py competitors` (now `order=most_impressions`), filtered to oral-care/dental ads (`data/competitor_top_dental.csv`, sheets in `sheets/competitor_top_dental_*.jpg`). The formats that get the most delivery right now:
1. **Insult/shock product shot with sticky notes**: Asuno "DON'T BE SUCH AN IDIOT" with yellow post-its reading "70% OFF / TODAY ONLY" (top 0.1%).
2. **Lo-fi real photo, no designed text**: Denture Care Tips' grimy denture on a lace doily (top 0.4%, 129 days) and a retainer with red bumps. The copy lives in the primary text: "Read This If You Wear Dentures 👆", a first-person near-death story.
3. **Medical imaging / scan before-after**: "MRI Confirms…", a CBCT jaw scan with an arrow, X-ray grids with red highlighted areas, petri dish "99.9% mold-spore reduction" before/after (barnakl).
4. **Price-anchor replacement**: Remi "Lost your $600 night guard? Replace it for $99." with 4 icon benefits; Remi "$627 of dental care. Yours for $250." bundle flat-lay.
5. **Big quote + product with press styling**: Sonic Dental "I put my retainers in Sonic Pro, wait 3 mins & they're brand new." with a save badge; Holymouthwash "8 years. 4 dentists. Nobody mentioned estrogen once."
6. **Real-world sign / object with text**: a yard sign reading "THE SMELL IS MADE IN THE GUT, NOT THE MOUTH."
7. **Advertorial card with data**: "Her Periodontist Quoted £4,000… 8 Weeks Later, Her Numbers Looked Like This" (tooth-chart numbers, "Read Article").
8. **Native UI**: an iOS reminder pop-up ("Change your brush head every 3 months"), a dating-app profile, Hismile cart screenshots.
9. **Founder letter**: Remi "WE'RE SAYING GOODBYE" letter with founder signature (tariff angle).
10. **Stat pictogram**: "1 in 3 women snore every single night" with a row of people icons.
11. **News split-face**: "NEWS — DOCTORS STUNNED: the 'jawbone restore' dentists don't talk about".
12. **Offer tiles**: "53% OFF ENDS SOON" with a hand holding the product and arrows to benefits; Hismile "BUY 3 GET 2 FREE" / "BUY 4 GET 6 FREE"; dark Sonic Dental "Limited Time Sale" with award seals and "4.8/5".
13. **Objection headline**: "Yes, it's really ODORLESS".

**What to take:** rotate across these formats so no two concepts in a batch look alike. Keep ~65% top-of-funnel (problem, enemy, controversy, imaging/proof) and ~35% offer tiles.

## 8. Oct 13 user feedback (rules now in brand.json → copy_rules, naming_rule, program.appliance_mix)
- **Formats looked too similar.** Use the §7 top-impression formats plus the Notion brief formats (`notion_brief.md` §6).
- **Say "ultrasonic cleaner"**, not just "Pod", for unaware audiences.
- **Make bacteria and yellow stains explicit.** These are the #1 and #2 purchase reasons; see `feedback_deep_dive.md`.
- **Copy:** direct response, aggressive and controversial (see `notion_brief.md` §2 and §8).
- **Products:** no Travel Pod concepts. The Ultimate Cleaning Bundle appears only in offer creatives. The denture case is drawn much smaller than the cleaner, and the warranty is not shown as a physical item.
- **Appliance mix:** 50% dentures; the other 50% is night guards ~50%, retainers ~30%, aligners ~15%, apnea ~5%.
- **9:16 versions:** extended seamlessly. The generator now outpaints across the seam, and layouts keep backgrounds running to the edges.

## 9. New formats from the Oct 16 competitor pull (Atria `most_impressions`, `data/competitor_ads.csv`, 1,010 ads; sheets `competitor_ads_1/2.jpg`)
Mostly oral-care DTC (quip, usmile, LIVFRESH, hismile, GuruNanda, Smile/Snoopy). New or newly useful formats:
14. **Couple/humor hook over a real bathroom photo**: LIVFRESH "HE SAID IT WAS TOO EXPENSIVE. Now he keeps using mine." (bold yellow type, small BUY 2 GET 1 tag). Used in W43 as a denture spouse offer.
15. **Notebook-paper confession**: "I DIDN'T REALIZE HOW BAD I FELT" handwritten on lined paper with the product beside it (also the §6 cheat sheet / post-it family). Used as the denture cheat sheet.
16. **Split "healthy vs inflamed" close-up with a "you can see the difference" headline** (GuruNanda); **Reactive vs Proactive** split (LIVFRESH): good template for us-vs-them tables.
17. **Surreal mouth-head character / big-energy headline** (quip, 57-91d): pattern interrupt, not used (off-brand for 60+ denture audience).
18. **Bundle line-drawing how-to and "BUY 4 GET 6 FREE" yellow burst** (hismile, 16-17d): offer tiles; we use the gift stack instead (no invented multi-buy).
Takeaway: the longest-running tiles are still bold-type-over-real-photo and native UI (reminder pop-up, cart); keep ~65% top-of-funnel.

## 10. New formats from the Oct 23 competitor pull (Atria `most_impressions`, 1,001 ads; sheets `competitor_ads_1/2.jpg`)
Quip, usmile, hismile, LIVFRESH, GuruNanda dominate. New or newly useful formats (used in W44-fri):
19. **Breakup letter to the old product** (GuruNanda "Dear Cluttered Toiletry Bag, Goodbye."): teal letter card, sign-off line. Used as "Dear Polident, goodbye."
20. **3D cartoon workplace panic with a speech bubble** (hismile "SOMEONE CHECK THIS ORDER", Pixar-style, offer burst at the bottom): cartoon_3d scene + bold speech bubble. Used for bacteria "SOMEONE CHECK THIS BATHROOM".
21. **Comment-keyword CTA** ("COMMENT 'GUMS' BELOW TO LEARN MORE", LIVFRESH): minimal, text over product. Not used (needs a comment bot).
22. **Back-to-school / campus code tiles** (GuruNanda "SEMESTER GLOW-UP", "Good habits go where they go"): seasonal parent/teen tile; relevant to retainers.
23. **Instructional line-drawing how-to with 1-2-3 steps** (hismile SWÖSH): used as an Ikea-style how-to.
Takeaway unchanged: bold type over real photo, native UI, big offer burst. Pop-art/mouth-head characters stay off-brand for 60+ wearers.

## 11. Own top spenders + other ultrasonic cleaner brands (Atria, pulled Oct 24; user feedback: "analyze other ultrasonic brands, other dental brands and our top-spending ads")
Pulled with `atria_pull.py winners`, `current` and the new `atria_pull.py ultrasonic` (brand.json -> `ultrasonic_queries`; 2,693 ads, 1,135 relevant: Zima Dental 236, Denture Care Tips 202, Anna Janeston 176, Ploise 84, SmileTherapy 21, Sonic Dental 17, Pop On 16, Remi 20). Sheets: `winning_statics_raw_1.jpg`, `ultrasonic_top_images_1-4.jpg`.

### Our top-spend statics (lifetime, all LP_LISTICLE / ADVERTORIAL / PDP)
| Spend | ROAS | Creative | Format to iterate |
|---|---|---|---|
| $14.7K (+ 6 more variants, $5-14K each) | 1.9-2.4 | "Top 7 Ultrasonic Cleaners For Dentures" / "DentalPULSE Pod vs OTHER PODS" | blue/white split spec table, green checks vs red X; "Top 7" ranking |
| $12.0K, $11.9K, $11.6K, $7.2K | 1.75-2.3 | "Read This If You Wear Dentures" story (image: hand lowering a denture into the open Pod on a wood counter, "Never brush your dentures again") | warm lifestyle hero, 4-word headline at the bottom |
| $11.9K | **3.3** | "Denture - 40% OFF" PDP: giant repeated "40% OFF" type on sky blue + Pod | big-type offer tile (best ROAS) |
| $10.3K | 1.8-3.2 | "read this before you consider ultrasonic cleaners" kitchen-table story (dentist $2,400 quote vs drawer of products); "Dental Ultrasonic Cleaner Rankings 2026" bar chart | price-anchor paper photo; ranking bar chart |
Current 30-day winners are mostly video: "6 of 7 pods leave live bacteria" (DEN81/DEN32, $7-7.5K, ROAS 2.3-2.6), "You've Been Lied To" (DEN24), "Evil Polident" (DEN226), and static IMG_DEN64 iterations (ROAS 2.6-3.2) and IMG_DEN62 (ROAS 3.9).
**Lesson: the money is in product-forward, comparison/ranking, big-type offer and warm lifestyle statics with a plain headline. Novelty formats (gimmick UI, retro, props) are the minority and must not outnumber these.**

### Other ultrasonic brands (what they run)
- **Zima Dental (236 ads):** "NEVER BRUSH YOUR RETAINER AGAIN" with the pod colour stack + award badge or Trustpilot stars; "Which oral appliance do you wear? Take our quiz" 6-icon grid; "SAVE $60 / FREE GIFT when you buy" black tile; "This is how to do Invisalign right" GQ-style editorial card; POV / GRWM creator stills; "Yes, the Dental Pod is back" colour pattern; "Star of the clean girl starter pack" flat-lay.
- **Sonic Dental (17):** quote + "Save £20" badge + press logos; before/after split "From cloudy to crystal clear" (03:00 timer - we must show 5:00); "Limited Time Sale" purple tiles with product in a palm; "Wireless. 3 mins. No brushing!".
- **Ploise (84) / Denture Care Tips (202) / Anna Janeston (176):** same media-buyer network: advertorial masthead cards ("The Denture Brief"), lo-fi grimy denture photos (top 0.0-0.4%), "NOTHING/DOCTORS STUNNED" news split-face, tier list "Best Ultrasonic Denture Cleaners of 2025-2026" (S to F grid), "Over 40,000 Denture Wearers Switched From Tablets To This" over a pod, FB-comment wall "Real People. Real Results.", "THE CLEAN LIE" (denture in blue tablet water with a magnified circle), "Old me / New me" split, "I Stopped Using Efferdent!" with FB comment. (Counts/"dentists" claims are theirs; ours stay in approved_claims.)
- **SmileTherapy (21):** "50% OFF" in giant type (blue/orange/teal variants) with the pod, "Buy 2 for 1", incoming-call "Visible Buildup Is Calling", a cartoon-avatar quote tile.
- **Pop On (16):** dark-to-white split with callout lines to features (Removes odor-causing bacteria / Lifts deep stains / Targets plaque buildup), "VIP SALE $139 -> $89 + free gift" with a 5:00 countdown.

### What to take (numbered for routines)
1. **Us-vs-others split table** (blue vs white, checks vs X) with only approved claims. 2. **Ranking bar chart / tier list**, ours #1. 3. **Warm lifestyle hero** (hand + open Pod + wood counter), headline <= 6 words. 4. **Giant repeated offer type** on blue with the Pod (+ small gifts). 5. **Product with feature callout lines** (Pop On). 6. **Quote + "Save 40%" badge** over the product (Sonic). 7. **Quiz/appliance grid** (Zima). 8. **Lo-fi grimy denture / calculus macro** with minimal text. 9. **Kitchen-table two-papers price-anchor photo**. 10. **FB comment wall / Real People Real Results**. 11. **Before/after split cloudy to crystal clear** (5:00, not 3:00). 12. **Editorial card** (GQ/news style) for aligners. 13. **Colour-stack / pattern product shot** with a badge (use only our one white Pod).

## 12. Oct 27 Tuesday iteration pull (W44-tue)
Atria `current` (13 ads, ≥$300, ROAS ≥1.8): top spenders are still "6 of 7 pods leave live bacteria" (VID_DEN32 $7.9K / 2.22, DEN81 H3 $6.1K / 2.28), "#1 Dentures Cleaner" (I13 $5.9K / 1.80), "You've Been Lied To" (DEN24 $3.2K / 2.34), the native IMG_DEN64 "read this before you consider ultrasonic cleaners" (51_12 $2.7K / 2.58, 51_3 $1.4K / 3.33), "Top 7 Ultrasonic Cleaners" (IMG_DEN62 $0.9K / **3.44**) and "40% Off + Free Gifts" ($0.4K / 3.04). `seasonal --week 2026-W44` (Oct 20-Nov 9 2025) is tiny spend: retainer listicles "No Scrubbing Retainers" ($34 / **4.39**) and "Never brush retainer again" ($55 / 2.60); their copy said "under 3 minutes" (we always say 5).
New formats used in W44-tue (not used before): S-to-F tier list, lab-report page (FAIL x6 / PASS), police-lineup 3D cartoon, hazard-yellow text-only warning, pore cutaway flat illustration, soap-bottle hazard-label photo, night-guard diary comic, price-tag bundle, pharmacy bottle label, napkin lo-fi, magazine editorial card, anime aligner scene.

## 13. Curated inspiration (user rule Oct 28): `atria_pull.py inspiration`
**Criteria (all enforced in code):** static images only; status active; launched 7-45 days ago (anything launched in the last 7 days is excluded, `days_running` ≥ 7); impressions growing week over week (Atria `impression_trend` = rising AND reach or impression rank improved over 7 days); English. **Queries:** oral care (teeth whitening, mouthwash, bad breath, gum health, dental probiotic, electric toothbrush, water flosser, denture/retainer/night guard/aligner cleaners, grinding, Invisalign) AND health & wellness (supplements for seniors, joint/back pain, sleep apnea/snoring, hearing, vision, gut, skin, blood sugar, brain health). Oct 28 run: 2,205 ads fetched, 719 launched <7 days ago removed, 18 not growing, 47 non-English; 457 kept after the days_running check (`data/inspiration_curated.csv`, sheets `sheets/inspiration_curated_1-4.jpg`). Search is keyword-fuzzy, so ignore off-topic hits (pets, diapers, agencies).
**What the growing statics look like (formats to borrow, all real/photographic or clean type):**
1. **Real photo + plain caption, insider authority** ("I operate on senior women's bunions every day. 90% of them wear the exact same sneaker." / "I've studied foot biomechanics for 19 years. The plantar fasciitis industry doesn't want you to see this data."). Candid medical-setting photo, 2-4 lines of white caption at the bottom. Use for dentures/night guards with a real clinical or bathroom scene (no invented named dentists, no counts).
2. **Gross/macro real photo, almost no text** (extreme close-ups, tongue and nose macro with a one-line promise: "Say goodbye to bad breath in 7 days." over a real tongue + bottle). For us: macro biofilm/yellow film on a denture, night guard or aligner + one direct line.
3. **Medical imaging with a red arrow** (X-ray, scan). For us: macro/UV/microscope photo with a single arrow to the film.
4. **Big-type offer on a clean product shot** ("40% OFF" repeated giant type behind a single product; "Fall Sale - Get $408 off" over a clean white product; "SALE ENDS TONIGHT"). Matches our best-ROAS static (Denture - 40% OFF).
5. **Before/after face or product splits with bold sans headline** ("NO RELINES, JUST VITAMINS"; Invisalign "THINK INVISALIGN CAN'T FIX COMPLEX SMILES?" with a big smile photo). For us: real yellow vs white denture, cloudy vs clear aligner (labelled BEFORE/AFTER, small).
6. **Native screenshots** (a long customer text-message review, an X post with a metrics row, a Facebook-style review). Plain, real-looking, no designs around them.
7. **Spec-callout product shot** (supplement bottle with 5 ingredient callouts, "Up to 64% OFF" badge, money-back seal). For us: Pod + 4 benefit callouts (99.9% bacteria, tap water only, 5 minutes, no tablets).
8. **Deadline/urgency angle** (Invisalign "use your FSA funds before they expire Dec 31", "Fall Sale", "ends tonight"): use real urgency only (current 40% sitewide offer; no fake countdowns).
**Not used any more:** cartoon / animation / comic / mascot / meme / joke formats (several appear in the pull, e.g. a cartoon bad-breath tile, but the user ruled them out) and anything launched in the last 7 days.

## 13b. Oct 30 inspiration run (Friday W45 net-new): `atria_pull.py inspiration`
2,223 ads fetched; 1,131 launched <7 days ago removed, 35 not growing, 51 non-English; **474 kept** (`data/inspiration_curated.csv`, sheets `sheets/inspiration_curated_1-4.jpg`, all four pages read). Search is fuzzy: most hits are off-niche (pets, SaaS, apparel); formats below are the ones that transfer.
**Formats growing now (used in W45-fri):**
1. **Day 1 vs Day 30 split with bullets** (Ploise denture ad, top 46.9%, 7d) -> W45_01 cups.
2. **Real macro of upper + lower denture stack** (denture cleaner, top 43.1%, 8d) and clinical lab-bench photo (top 28.8%, 12d) -> W45_04, W45_06.
3. **Plain apology text card** ("We're sorry", 8d) -> W45_02.
4. **Clipboard grading ("I graded 5 ... only 1 passed")** (blood sugar, 9d) -> W45_03.
5. **Yellow sticky-note offer on a product shot** (back pain/skin care, 8d) -> W45_28.
6. **Big-number price tiles / "Buy 5 Get 8"** -> W45_34, W45_40.
7. **Black tile with three stacked products + "3 for $20"** (gut health, 21.4%) -> W45_16.
8. **Spec callout lines around a hand-held product** (usmile, 8d) -> W45_19.
9. **Real photo with one-line promise over a mouth/tongue macro** (bad breath, 18d) and store-window deal sign (denture cleaner, 7d) -> W45_07, W45_20.
10. **Invisalign big-smile split photo, festive gift tiles, quadrant chart** -> W45_39, W45_30, W45_13.
Skipped: cartoons/anime/memes, sexual or pet imagery, anything launched in the last 7 days.
**Own winners re-read** (`current`, Oct 30 window): VID_DEN32 $8.8K/2.16, DEN81 H3 $5.9K/2.31, TOFv1_I13 $6.4K/1.88, DEN24 $3.1K/2.34, IMG_DEN64 51_3 $1.4K/3.19, IMG_DEN62 $0.9K/3.53, Denture 40% OFF $0.3K/2.05 (lifetime $11.9K/3.3). W45-fri keeps 7 proven formats: warm hero, quote+badge, native story photo, ranking quadrant, giant 40% type, FB comment wall, us-vs-other-pods table.
**Render lesson (W45):** the image model renders "yellow" as pink-white unless the prompt says mustard/brown and "different from clean at first glance"; native UI prompts need `no_product` + "screen fills the canvas" or they come back as Pod ads.

## 13c. Oct 30 one-off rivals batch (`weeks/2026-W44-rivals`): `atria_pull.py inspiration` + `rivals`
Inspiration: 2,228 ads fetched; 1,102 launched <7 days ago removed, 22 not growing, 40 non-English; **487 kept** (sheets 1–4 read). Rivals: Zima Dental 85 ads, Sonic Dental 41 (`research/core_competitors.md`).
**New formats used (not in earlier DentalPULSE batches):**
- mass-quantity kitchen table (bad-breath brand, top 0.1%, 7d) → R44_01
- "WE'RE NOT LIKE THE OTHERS." statement (top 2.9%, 8d) → R44_02
- vertical price cascade with arrows (top 3.2%, 16d) → R44_03
- "Not Another Cream…Dermatologists Recommend" editorial + seal (top 1.3%, 15d) → R44_04
- MARCH/AUGUST photo split (top 1.3%, 7d) → R44_05
- BREAKING NEWS lower third (top 2.4%, 8d) → R44_06
- hand over sink lo-fi (top 0.6%, 7d) → R44_08
- quote + savings pill + free-gift value (top 2.4%, 8d) → R44_09
- mirror inspection (top 1.0%, 31d) → R44_11
- TAKE THE QUIZ button (top 2.4%, 8d) → R44_12
- X-ray red circles (top 1.3%, 7d) → R44_14 (UV)
- clean blue "buy one get one" layout (top 1.3%, 8d) → R44_15
- hand-written callouts (top 5.2%, 13d) → R44_16
- dark tile + round seal (top 1.1%, 9d) → R44_20

**Rival upgrades:**
- Sonic's pod-on-palm sale tile, with proof added → R44_10
- Zima "Dad's dentures" → R44_07
- Zima "Never brush again" → R44_13, R44_16
- Zima "Clean Girl Starter Pack" → R44_17
- Zima Pod Go / Sonic Pro+Go → R44_19

**Render lessons:**
- The `pod_open` reference carries an aligner, so denture ads use `pod` (closed) or say "no aligner anywhere; lid empty".
- Night guards need "THICK rigid ~3 mm tray, bulkier than an aligner".
- Every ad, offers included, needs a visibly yellow or cloudy appliance in the picture.
- Split/cascade layouts must keep the top 34–40% empty for the overlay headline.
