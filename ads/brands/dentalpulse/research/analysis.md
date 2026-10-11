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

## 5. Claims
- The account already uses "eliminates 99.9% of bacteria", "clinical grade", "6 of 7 pods leave live bacteria" and star ratings. Statics stay off those until the brand confirms substantiation; brand.json → `claims_to_avoid` lists them.
- Comparison iterations of the live "tested 7 pods" ads are flagged in `based_on` for sign-off.
