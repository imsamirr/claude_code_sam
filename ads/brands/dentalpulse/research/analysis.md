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
