# DentalPULSE: Meta ad-account video performance digest (last 60 days)

- **Source:** Atria MCP, own ad account "Dentalpulse" (Atria id `af48140c86004e99b4fb85baf1c12eee`), Meta, currency CAD, account timezone America/Toronto.
- **Window:** custom 2026-09-20 to 2026-11-18 (60 days ending yesterday; Atria windows are UTC days). Nothing outside this window was read.
- **Pulled:** 2026-11-19. 559 ads delivered in the window.
- **Purpose:** data input for StefanBrain video scripts. Data only: this file contains no new copy. All quoted lines are existing ads.

## Metric definitions (Atria standard metric ids)

| Label used here | Atria id | Meaning |
|---|---|---|
| Spend | `spend` | CAD |
| ROAS | `roas` | Meta-reported purchase value / spend |
| Purch | `purchases` | Meta-attributed purchase events |
| Revenue | `purchase_value` | Meta-reported |
| CPA | `cost_per_purchase` | CAD |
| CTR | `ctr_link` | link clicks / impressions |
| CPM | `cpm` | CAD |
| Hook | `thumbstop_ratio` | 3-second plays / impressions |
| Hold (15s/imp) | `hold_rate` | ThruPlays (15s or complete) / impressions |
| 15s/3s | `video_retention_15s_3s` | ThruPlays / 3s plays (the "of those hooked, how many stayed" rate) |
| Avg watch | `video_play_avg_time` | seconds per play |
| p25/p50/p75/p100 | `video_play_rate_p25` ... `_p100` | share of impressions reaching that % of the video |

No Atria custom metrics exist on this account (`atria_custom_metric` list is empty). A separate "average watch time" at account level returns 0 (not aggregated); per-ad values exist.

**Caveats**
- ROAS/purchases are Meta-reported (platform attribution), not Triple Whale / Shopify.
- The last days of the window (mid-Nov) are still settling; recent ads are understated.
- Low-confidence flag (LC): any ad under CAD 300 spend.
- Some ads share one video file (A36 and "VID_DEN32 ... - Copy" use the same video and copy but sit in different campaigns: CPM 100.5 vs 50.5, ROAS 1.39 vs 2.28). Delivery context matters as much as creative.
- Claims spoken in existing videos (pneumonia stats, "99.95%", "orthodontists recommend", user counts, FDA warning, competitor scores) are reported here as found. They have not been checked against DentalPULSE's approved-claims list, so check each one before reuse.

## Account totals (2026-09-20 to 2026-11-18)

| Metric | Value |
|---|---|
| Spend | CAD 188,593.66 |
| Purchases | 1,777 |
| Revenue (Meta) | CAD 281,825.05 |
| ROAS | 1.49 |
| CPA | CAD 106.13 |
| AOV | CAD 158.60 |
| CTR (link) | 2.72% |
| CPC (link) | CAD 2.84 |
| CPM | CAD 77.17 |
| Impressions | 2,443,754 |
| Hook (3s/imp) | 25.8% |
| Hold (15s/imp) | 9.4% |
| 15s/3s retention | 36.4% |
| p25 / p50 / p75 / p100 (of impressions) | 6.9% / 5.1% / 4.2% / 2.1% |

## Top video ads by spend

Video length is from the creative. Status is as of the pull.

| # | Ad name (short) | Len | Spend | ROAS | Purch | CPA | CTR | CPM | Hook | Hold 15s/imp | 15s/3s | Avg watch | p100 | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TOFv1_A36 (rank-7 comparison, gifts LP) | 1:53 | 39,148 | 1.39 | 333 | 117.6 | 3.05% | 100.5 | 30.8% | 13.2% | 42.7% | 13s | 3.1% | ACTIVE |
| 2 | VID_DEN32_COMPARISON_IT_02_LP_LISTICLE_V2 - Copy (same video as A36) | 1:53 | 19,105 | **2.28** | 284 | 67.3 | 2.12% | 50.5 | 27.8% | 10.3% | 37.1% | 10s | 2.3% | ACTIVE |
| 3 | TOFv1_I13 Denture den 169 HK4 V4 (rank-7) | 2:24 | 14,713 | 1.56 | 145 | 101.5 | 3.23% | 97.6 | 26.6% | 10.4% | 39.1% | 14s | 4.1% | ACTIVE |
| 4 | _DEN_VID_DEN81_H3 REVISED_LP_LISTICLE_V1 | 3:09 | 12,726 | **2.14** | 173 | 73.6 | 3.52% | 101.6 | 35.0% | 12.0% | 34.2% | 14s | 2.7% | ACTIVE |
| 5 | TOFv1_AD2 DEN209 Most Denture Cleaners Sold Online_Comparison_AI+ExistingFootage_H2 | 1:41 | 6,581 | 1.47 | 60 | 109.7 | 4.04% | 124.3 | 27.5% | 11.2% | 40.7% | 10s | 2.4% | ACTIVE |
| 6 | VID_DEN24_COMPARISON_IT_02_LP_LISTICLE_V1 ("You've Been Lied To") | 2:41 | 6,389 | **2.39** | 97 | 65.9 | 2.74% | 67.6 | 25.9% | 10.6% | 40.8% | 14s | 3.1% | ACTIVE |
| 7 | _DEN_VID_DEN81_H4 REVISED_LP_LISTICLE_V1 | 3:06 | 5,809 | **2.11** | 81 | 71.7 | 4.27% | 109.1 | 34.6% | 12.1% | 35.0% | 14s | 2.9% | ACTIVE |
| 8 | TOFv1_CI1 Night Guards Comparison DEN256_HOOK 1 V2 | 1:40 | 3,319 | 0.97 | 21 | 158.0 | 2.17% | 122.9 | 28.9% | 7.4% | 25.5% | 7s | 2.0% | ACTIVE |
| 9 | TOFv1_CP1 DEN268_HOOK 1 V3 (gift angle, Gift PDP) | 1:19 | 2,979 | 0.79 | 16 | 186.2 | 1.55% | 78.4 | 34.3% | 7.5% | 22.0% | 6s | 0.7% | ACTIVE |
| 10 | _DEN_VID_DEN81_H3 ... - Copy | 3:09 | 2,940 | 1.81 | 34 | 86.5 | 2.19% | 47.6 | 24.1% | 7.1% | 29.4% | 9s | 1.2% | ACTIVE |
| 11 | _DEN_VID_DEN81_H1 REVISED_LP_LISTICLE_V1 | 3:00 | 2,531 | **2.64** | 42 | 60.3 | 4.53% | 93.5 | 29.0% | 10.2% | 35.2% | 6s | 5.0% | ACTIVE |
| 12 | TOFv1_I13_V2 (same video as #3) | 2:24 | 2,446 | 1.15 | 18 | 135.9 | 3.03% | 95.4 | 26.0% | 10.2% | 39.1% | 13s | 4.0% | PAUSED |
| 13 | TOFv1_BC1 DEN226 Why tablets are not good / nostalgia / Evil Polident (AI+ExistingFootage) | 3:37 | 2,327 | 1.42 | 19 | 122.5 | 1.99% | 71.1 | **62.0%** | **23.8%** | 38.4% | **27s** | 2.2% | ACTIVE |
| 14 | TOFv1_AW1 DEN 213 V2 (rank-7) | 1:57 | 1,882 | 1.34 | 17 | 110.7 | 3.34% | 100.6 | 23.9% | 10.3% | 43.1% | 11s | 3.5% | ACTIVE |
| 15 | TOFv1_BX3 DEN267_HOOK 1 (biofilm / pneumonia mechanism) | 2:10 | 1,879 | 1.16 | 13 | 144.5 | 1.93% | 82.5 | 45.4% | 19.1% | 42.2% | 13s | 0.8% | ACTIVE |
| 16 | TOFv1_DG1 DEN308_HOOK 2 V2 (night-guard ranking, appliance copy) | 2:34 | 1,821 | 1.46 | 15 | 121.4 | 3.84% | 202.3 | 35.4% | 12.0% | 34.0% | 16s | 4.5% | ACTIVE |
| 17 | VID_DEN31_COMPARISON_04 (Zima price comparison) | 1:36 | 1,550 | 1.54 | 16 | 96.8 | 1.85% | 55.5 | 18.8% | 6.1% | 32.4% | 7s | 1.0% | ACTIVE |
| 18 | TOFv1_DG3 DEN308_HOOK 1 | n/a | 1,376 | 0.95 | 9 | 152.9 | 3.80% | 148.4 | 32.4% | 12.1% | 37.4% | 16s | 4.6% | PAUSED |
| 19 | TOFv1_DC1 DEN320 VIDEO 1 V2 (rank-7, gifts LP) | 2:24 | 1,361 | 1.06 | 9 | 151.2 | 3.55% | 151.5 | 32.7% | 12.6% | 38.4% | 15s | 4.2% | ACTIVE |
| 20 | VID_DEN32 ... – Copy (third copy of A36 video) | 1:53 | 1,318 | 1.97 | 16 | 82.4 | 2.41% | 28.8 | 33.3% | 13.8% | 41.3% | 13s | 2.5% | ACTIVE |
| 21 | TOFv1_DL3 OCTWK4_VID1_JACK_DentureNightlyRoutine_Hook3 (adult-child / gift, Black Friday VO) | 2:07 | 1,171 | 0.79 | 6 | 195.1 | 2.39% | 143.0 | 41.0% | 16.1% | 39.4% | 13s | 1.6% | ACTIVE |
| 22 | TOFv1_CG2 Night Guards Comparison DEN280_V2 VER 3 | 0:47 | 774 | 0.65 | 4 | 193.5 | 1.63% | 94.6 | 35.1% | 8.6% | 24.5% | 6s | 3.0% | ACTIVE |
| 23 | TOFv1_CO2 DEN229_HOOK 2 V2 | n/a | 736 | 0.44 | 2 | 367.8 | 1.25% | 60.0 | 28.5% | 8.8% | 31.0% | 7s | 0.7% | ACTIVE |
| 24 | VID_DEN105_COMPARISON_IT_02 - Copy | n/a | 725 | 1.62 | 8 | 90.7 | 1.29% | 40.8 | 24.5% | 4.9% | 20.1% | 5s | 1.1% | ACTIVE |
| 25 | TOFv1_DT2 DEN303_HOOK 2 V2 | n/a | 652 | 0.96 | 4 | 162.9 | 1.70% | 74.7 | 31.3% | 11.0% | 35.3% | 8s | 0.5% | ACTIVE |

## Top statics by spend

| Ad name | Spend | ROAS | Purch | CPA | CTR | CPM | Status |
|---|---|---|---|---|---|---|---|
| IMG_DEN64_COMPARISON_IT_NATIVEAD_51_12_LP_LISTICLE_V1_DUPLICATED | 6,094 | 2.35 | 91 | 67.0 | 3.63% | 56.5 | ACTIVE |
| IMG_DEN64_COMPARISON_IT_NATIVEAD_51_3_LP_LISTICLE_V1 - Copy | 3,075 | 2.88 | 54 | 56.9 | 2.66% | 46.8 | ACTIVE |
| IMG_DEN62_PROBSOL_ITERATION_02_LP_LISTICLE_V1_DUPLICATED | 2,066 | **3.41** | 45 | 45.9 | 1.76% | 42.2 | ACTIVE |
| TOFv1_A30 | 1,600 | 1.85 | 18 | 88.9 | 4.39% | 98.9 | ACTIVE |
| TOFv1_F24 Denture DEN155 Winner Iteration_Comparison_Statics | 969 | 0.89 | 5 | 193.8 | 2.60% | 64.2 | PAUSED |
| TOFv1_G23 | 852 | 0.88 | 5 | 170.3 | 2.85% | 92.0 | PAUSED |
| Denture - HALF PRICE TODAY ONLY - Gift PDP | 783 | **2.81** | 14 | 55.9 | 3.11% | 55.9 | ACTIVE |
| Denture - 40% OFF _LP_PDP_V3 | 762 | 2.06 | 10 | 76.2 | 1.33% | 36.4 | PAUSED |
| TOFv1_G44 Denture (Reddit-style image) | 497 | 0.95 | 3 | 165.6 | 3.23% | 38.2 | PAUSED |
| TOFv1_AX40 Retainer O42_08 | 425 | 0.66 | 2 | 212.7 | 2.30% | 76.4 | PAUSED |
| TOFv1_AX50 Comparison Night guard (carousel/images) | 373 | 1.48 | 3 | 124.4 | 4.07% | 101.9 | ACTIVE |
| TOFv1_AX36 Denture-Native-Image-#2_12 | 333 | 1.15 | 2 | 166.3 | 2.27% | 39.9 | PAUSED |
| (LC) TOFv1_G42 Denture "independent residents... reminder to always check" | 249 | 2.33 | 2 | 124.5 | 3.95% | n/a | PAUSED |
| (LC) IMG_DEN64_..._51_12 – Copy | 239 | 2.37 | 3 | 79.8 | 3.43% | n/a | ACTIVE |
| (LC) Denture - Denture Cleaner of 2026_LP_PDP_V3 | 208 | 3.11 | 4 | 52.0 | 1.44% | n/a | ACTIVE |

The top-50-by-spend list holds about CAD 17.8k on statics. Statics using the comparison/listicle LP deliver at lower CPM (CAD 42 to 57) and have the best CPAs in the account (CAD 46 to 67).

## Best hooks (videos with CAD 300 or more spend, ranked by hook rate)

| Ad | Spend | Hook | Hold 15s/imp | 15s/3s | ROAS | Opening line (from transcript) |
|---|---|---|---|---|---|---|
| BC1 DEN226 (tablet history / "Evil Polident") | 2,327 | 62.0% | 23.8% | 38.4% | 1.42 | "90 years ago, people cleaned their dentures with a brush and water. Then one drug company changed one thing, and it's sitting in your bathroom right now." |
| CZ1 DEN299 (drama, 42-yr-old makeup artist) | 517 | 60.4% | 21.7% | 35.9% | 0.71 | "Want one? The second my client offered me gum, I thought, she can smell my dentures." |
| H9 Retainer DEN162 (sleep-apnea retainer explainer, UGC) | 382 | 58.1% | 11.3% | 19.4% | 0.48 | (not transcribed) |
| CX1 DEN265 (LFS "Tablet Conspiracy") | 454 | 48.2% | 19.2% | 39.8% | 0.31 | (transcription charged but not returned, see credits) |
| BX3 DEN267 (biofilm / pneumonia) | 1,879 | 45.4% | 19.1% | 42.2% | 1.16 | "Most denture wearers don't realize this, but if you wear dentures, cleaning it like this will ruin your life." |
| AR3 SEPTWK2 DentureRankedComparison Hook1 | 459 | 44.1% | 11.6% | 26.4% | 0.92 | (not transcribed) |
| DL3 OCTWK4 DentureNightlyRoutine Hook3 | 1,171 | 41.0% | 16.1% | 39.4% | 0.79 | "If you catch that smell when you hug your mom or dad, even though they brush and soak their dentures every night, that routine is the reason they still smell." |
| CQ1 DEN286 | 465 | 39.8% | 10.0% | 25.2% | 0.91 | (not transcribed) |
| DG1 DEN308 HOOK 2 | 1,821 | 35.4% | 12.0% | 34.0% | 1.46 | "I tested Zima, Sonic, Gurunanda, and Amazon ultrasonic cleaners over 90 days." |
| CG2 Night Guards DEN280 | 774 | 35.1% | 8.6% | 24.5% | 0.65 | "Generic Amazon ultrasonic cleaners. Five." (starts straight into the ranking) |
| DEN81_H3 | 12,726 | 35.0% | 12.0% | 34.2% | 2.14 | "If you already own an ultrasonic denture cleaner, watch this. Most have a UV light that looks like it's working but kills almost nothing." |
| DEN81_H4 | 5,809 | 34.6% | 12.1% | 35.0% | 2.11 | "If you bought expensive ultrasonic cleaners thinking they clean better than your brush, think again." |
| CP1 DEN268 (gift) | 2,979 | 34.3% | 7.5% | 22.0% | 0.79 | "This makes denture cleaning so much easier. Every denture wearer needs to see this." |
| DEN32 – Copy | 1,318 | 33.3% | 13.8% | 41.3% | 1.97 | "I tested Zima, Ploys, and Amazon ultrasonic cleaners over 90 days." |
| DC1 DEN320 | 1,361 | 32.7% | 12.6% | 38.4% | 1.06 | "So I tested seven ultrasonic cleaners for dentures. The winner, not the $180 one." |
| A36 | 39,148 | 30.8% | 13.2% | 42.7% | 1.39 | "I tested Zima, Ploys, and Amazon ultrasonic cleaners over 90 days." |
| DEN81_H1 | 2,531 | 29.0% | 10.2% | 35.2% | 2.64 | "I bought the seven most popular denture cleaners. I tested them for 90 days, so you don't have to." |
| CI1 Night Guards DEN256 | 3,319 | 28.9% | 7.4% | 25.5% | 0.97 | "I ran my night guard through 5 pods, and only one of them did this." |
| I13 den 169 HK4 | 14,713 | 26.6% | 10.4% | 39.1% | 1.56 | "So I tested seven ultrasonic cleaners for dentures. The winner, not the $180 one." |
| DEN24 | 6,389 | 25.9% | 10.6% | 40.8% | 2.39 | "Here are six ultrasonic cleaners I would never recommend to my patients struggling with cleaning their dentures." |
| AW1 DEN 213 | 1,882 | 23.9% | 10.3% | 43.1% | 1.34 | "Before you buy an ultrasonic cleaner for your dentures, watch this." |
| DEN31 | 1,550 | 18.8% | 6.1% | 32.4% | 1.54 | "Zima dental pod costs three times as much. I tested seven different ultrasonic cleaners over 90 days." |

**Low-confidence high hooks (under CAD 300, 0 purchases so far): the new "DV" long-form scroll-video series, launched in the last days of the window.** EL2 "DV02 What the death certificate said" (CAD 172, hook 77.8%, hold 30.0%, avg 26s, CTR 5.7%); EK1 "DV04 The gravy test" (CAD 138, hook 70.9%); EI2 "DV11 Three cavities before the wedding" (CAD 134, hook 68.0%); EL1 "DV03 Aspiration Pneumonia, The empty cups" (CAD 5, hook 75%); EI1 "DV10 Night Guards & Aligners, Black dots in the case" (CAD 13, hook 62%). Hooks are well above the account's 25.8%, but there is no purchase data yet.

## Top videos: transcripts, primary text, headline

Primary-text variants recur, so they are labelled once and referred to by label:

- **PT-A "90-day lab test" (long paragraph):** "A 90-day side-by-side lab test of seven leading ultrasonic dental cleaners revealed that most units available online fall short on deep decontamination. ... six out of seven machines left live bacterial biofilm active on appliances overnight. ... This engineered unit was the only system tested that completely cleared subsurface buildup without damaging the appliance material. Read the full comparison breakdown to see the raw lab findings before choosing a device." Description: "Review the full laboratory performance scores. Backed by a 120-day money-back guarantee and a 1-year product warranty." CTA Learn More.
- **PT-B "We spent 90 days testing" (emoji list + 2 reviews):** "🏆 We spent 90 days testing the most popular ultrasonic dental cleaners. Instead of trusting marketing... We tested them ourselves. 🦷 Cleaning performance ⚡ Ultrasonic power 💧 Build quality ⏱️ Daily usability 💰 Overall value. One model consistently outperformed every competitor. The DentalPulse Pod." Then two "comparison saved me" reviews and "Read the full comparison before you buy... risk-free to try! Tap 'Learn more' now." Night-guard versions swap in "cleaners for night guards" or "dental appliance cleaners".
- **PT-C "Gift" (long):** "❤️ If someone you love wears dentures, this might be one of the most useful gifts you can give them..." with benefit bullets, a "limited-time DentalPULSE sale: special introductory pricing, FREE gifts worth up to $50, money-back guarantee, limited availability", "They'll use it every single day", 3 reviews, and "Tap 'Shop now' to buy your loved one a gift..."
- **PT-D "Tablets" (medium):** "Denture cleaning tablets have been around for decades. But just because something has been used for years doesn't mean it's the best way... Most tablets fizz, change the water blue and leave behind a minty smell... 42,000 Hz ultrasonic cleaning... Clean in just 3-5 minutes... No monthly cleaning-tablet dependency."
- **PT-E "I thought my dentures were clean" (first-person, long):** "I thought my dentures were clean... until I tried this. After one cleaning cycle, I couldn't believe what came off them..." with feature bullets (45,000 Hz, 3 minutes), 3 reviews, "They're currently risk-free".

### 1-2. A36 / VID_DEN32 - Copy (video 3394580070748678, 1:53), CAD 58.3k combined
- Primary text: PT-A. Headline: "6 of 7 pods leave live bacteria". LP: `/pages/we-tested-7-ultrasonic-dental-cleaners-over-90-days-heres-what-actually-works-bundle-pod-gifts`.
- Transcript (first ~120 words): "I tested Zima, Ploys, and Amazon ultrasonic cleaners over 90 days. Generic Amazon cleaners, 2 out of 10. They clean for a week, then the ultrasonic weakens and most stop working before the 90 days are up. No UV light, no support number, no recourse. Ploys, 3 out of 10. The UV light isn't medical grade, the tank is small, and there's zero warranty on the device. None. Opro, 4 out of 10. Simple to use, but it runs hot. Too hot for soft aligners and the kind of acrylic most dentures are made of. Smile Therapy, 5 out of 10. ... Isonic, 5 out of 10. ... tank is too small to fit both upper and lower dentures at once..."
- Structure: **Hook**: "I tested [named competitors] over 90 days". **Problem**: competitors scored worst to best (Amazon 2, Ploys 3, Opro 4, Smile Therapy 5, iSonic 5, Zima 6), each with one flaw (weak ultrasonic, no or non-medical UV, small tank, runs hot, tablet subscription, 30-day returns, ship back to UK). **Mechanism**: "only one that does ultrasonic cleaning and medical grade UV light together, in one five minute cycle", stainless tank, one button, just water. **Proof**: "After one cycle, the water turns brown... Every single user sees it on the first use." **Offer**: 40% off, 120 days, 12-month warranty, US phone support. **CTA**: "If you've already wasted money on the wrong one, this is the one that gets it right."

### 3 / 12 / 19. I13 and I13_V2 (video 1749966896047629, 2:24) and DC1 DEN320 (video 3091333004537734, same voiceover), CAD 18.5k combined
- Primary text: PT-B. Headline: "#1 Dentures Cleaner (Clinical Grade At-Home)". LP: bundle-pdp listicle (DC1 points to the bundle-pod-gifts LP).
- Transcript (first ~120 words): "So I tested seven ultrasonic cleaners for dentures. The winner, not the $180 one. Now I'm going to rate them. Generic Amazon cleaners, two out of 10. These are the ones that pop up when you search for a quick option. They clean okay at the start, but reviewers consistently say the cleaning gets weaker over time. There is also no UV light to kill bacteria after the wash. And when something goes wrong, there is basically no support. Isonic, four out of 10. ... no UV light, so bacteria that gets loosened during cleaning is still just sitting on your dentures when you take them out. The basin is also quite small..."
- Structure: Hook "tested seven / the winner is not the $180 one", then a ranked teardown (Amazon 2, iSonic 4, Zima 5, Smile Therapy 5, Novapod 4, Sonic Pro 7), then DentalPulse 9/10 (ultrasonic + UV, 5 min, one button, plain water, no subscription), then coverage (120 days + 12-month warranty) and CTA "Link is right below... limited time offer". No brown-water proof in this version.

### 4 / 7 / 10 / 11. DEN81 H3, H4, H1 (videos 1433007015369759, 1784550766234920, 4293084744355564; about 3:00 each), CAD 24.0k combined, ROAS 1.81 to 2.64
- Primary text: PT-A. Headline: "6 of 7 pods can't remove bacteria". LP: bundle-pdp listicle.
- These are hook variants on one body. Hooks:
  - H3: "If you already own an ultrasonic denture cleaner, watch this. Most have a UV light that looks like it's working but kills almost nothing. I tested six to find out which ones are real and which ones are faking it." (hook 35.0%, ROAS 2.14)
  - H4: "If you bought expensive ultrasonic cleaners thinking they clean better than your brush, think again. We tested the seven most popular denture cleaners. Six of them failed to kill bacteria." (hook 34.6%, ROAS 2.11, CTR 4.27%)
  - H1: "I bought the seven most popular denture cleaners. I tested them for 90 days, so you don't have to." (hook 29.0%, ROAS 2.64, CTR 4.53%, highest p100 5.0%)
- Shared body (first ~120 words): "Most of them fail in one of two ways. Some are too weak to clean deep into the grooves. Others have a UV light that looks nice but doesn't really kill anything. I ranked all six and I'll show you the one that turned the water brown the first time I used it. Let's start at the bottom. Number seven, cheap Amazon cleaners. Two out of ten. ... Number six, Guru Nanda. Four out of ten. ... It's fine for a retainer, not for dentures. Number five, Dr. B. ..."
- Structure: **Hook** (variant), then "two ways they fail" frame (weak ultrasonic / fake UV) plus an open loop ("I'll show you the one that turned the water brown"), then a countdown 7 to 2 (Amazon 2, Guru Nanda 4, Dr. B 5, Smile Therapy 6, Sonic Dental 7, Zima 8: "one wash isn't enough... tablets you didn't ask for... 30 days... mail it back to the UK... costs about three times more"). **#1 DentalPulse 9.5**: "This is the one all my patients are using" (dentist/professional voice), deep-groove clean, real UV, steel tank, fits top and bottom set, 5 min, one button, water only, no monthly fees, US phone support. **Offer**: 120 days + full-year warranty. **Proof/guarantee**: "Put your dentures in for the first time. Watch the water. It turns brown... If you don't see it the first time, send it back and get your money back." **CTA**: "There's a deal on right now."

### 5. AD2 DEN209 "Most Denture Cleaners Sold Online" (video 2100124537248546, 1:41), CAD 6,581, ROAS 1.47
- Primary text: PT-B. Headline: "#1 Dentures Cleaner (Clinical Grade At-Home)". AI + existing footage.
- Transcript (first ~120 words): "I tested Zima, Sonic, and Amazon ultrasonic cleaners over 90 days. Find out which ultrasonic cleaner I ranked the worst. The generic Amazon cleaners get a 2 out of 10. They clean for about a week, then the ultrasonic stops working, and most break before 60 days. Doesn't turn on. Zima and Smile Therapy both land on 5. They advertise UV, but neither of them tells you the wavelength. And at the wrong wavelength, that light passes straight through the bacteria and does absolutely nothing. And both need 2 cycles for basic cleaning..."
- Structure: same ranked-comparison frame, with a UV-wavelength argument, Novapod 1/10 ("hidden monthly subscription"), Sonic Dental 7 (10-minute cycle). DentalPulse 9: "42,000 waves a second", UVC, one 5-minute cycle, "same technology dental clinics are using". Health stake: "Denture wearers who do not clean properly are twice as likely to develop aspiration pneumonia." Offer: "up to 40% off right now with free gifts", 120-day guarantee.

### 6. VID_DEN24 (video 1356117273080253, 2:41), CAD 6,389, ROAS 2.39
- Primary text: "For decades, dental patients have been given outdated advice... a standard toothbrush and a chemical tablet were enough... Under a microscope... micro-scratches that trap bacterial colonies, while tablets only mask the odor... medical-grade ultrasonic cleaning at home is the only way to safely reach 99.9% of hidden pathogens... Read our official 90-day durability report." Headline: "You've Been Lied To". Description: "See why recent clinical data proves traditional cleaning methods are outdated...". LP: bundle-pdp listicle.
- Transcript opening: "Here are six ultrasonic cleaners I would never recommend to my patients struggling with cleaning their dentures. So I bought and tested the seven most popular ultrasonic denture cleaners so you don't have to." The body then matches the I13 script (Amazon 2, iSonic 4, Zima 5, Smile Therapy 5, Ploys 4, Sonic Pro 7, DentalPulse 9; 120 days + 12-month warranty; "limited time offer"). Dentist/professional framing in the hook only.

### 8. CI1 Night Guards Comparison DEN256 (video 1327603629437100, 1:40), CAD 3,319, ROAS 0.97
- Primary text: PT-B (night-guard version). Headline: "#1 Night Guards Cleaner (Clinical Grade At-Home)". LP: bundle-pdp listicle (a denture-led page).
- Transcript (first ~120 words): "I ran my night guard through 5 pods, and only one of them did this. Okay, so my night guard has been looking cloudy and kind of funky no matter what I do. So I went down the rabbit hole and ranked the pods that say they clean them, so you don't have to. And here's what nobody tells you. Not every pod works on a night guard. Heat, tank size, how well it actually cleans, all of it matters because this thing is in your mouth every night. Cheap Amazon Ultrasonic, 2 out of 10. No UV light, and the warranty is basically nothing. Reviews keep saying it heats up the water, and heat is how you warp a nightguard..."
- Structure: first-person night-guard wearer (cloudy/funky guard), then the "not every pod works on a night guard" criteria (heat, tank size, clean), then ranking (Amazon 2, iSonic 5, Opro 7, Zima 6: UV is a separate case for clear trays), then DentalPulse 9 (ultrasonic + UVC in one unit, tank fits a full night guard, cold tap water). Credibility flaw admitted: "Only thing I'd knock, the lid feels a little delicate." Proof: brown water on the night guard. Offer: 40% off, free shipping and returns, 120 days, 12-month warranty.

### 9. CP1 DEN268 Gift (video 1692308649081525, 1:19), CAD 2,979, ROAS 0.79
- Primary text: PT-C (gift). Headline: "#1 Dentures Cleaner Gift (Clinical Grade At-Home)". CTA Shop Now. LP: `/products/dentalpulse-pod-denture-bundle-gifts` (PDP, no advertorial).
- Transcript (about 230 words, full): "This makes denture cleaning so much easier. Every denture wearer needs to see this. This is the best gift for denture wearers, and it's on sale right now for a limited time. If you wear dentures or know someone who does, you need to see this. This simple device gets rid of the bacteria, yellow plaque buildup, and removes the bad smell all within five minutes. It uses ultrasonic vibrations in water to help loosen trapped food and stubborn buildup from the surface and grooves of your denture, and the UVC light finishes it off by disinfecting your dentures [...] germs, or mold left behind. Just add water, place the dentures inside, close the lid, and start the cleaning cycle. There's no complicated setup, and you don't have to stand over the sink while it runs. Easy to use for yourself, your partner, your elderly parents, or your friend. So if you've been looking for something thoughtful for your partner or an elderly parent who wears dentures, this is a practical way to make an everyday routine easier. Especially because they're running a sale for new customers right now, which means that you can buy the Dental Pulse Pod risk-free at the lowest price they've ever offered. They're also gifts with every order, value of up to $50. And if you don't like it for any reason, you don't have to pay because you're covered by a full money back guarantee. But I don't think that's going to happen. Orthodontists recommend the Dental Pulse Pod as their number one denture cleaning method. So click now to take advantage of this special limited time discount while it's still available."
- Note: hook 34.3%, but hold 7.5%, 15s/3s 22.0%, p100 0.7% (weakest retention among top spenders) and CTR 1.55%.

### 13. BC1 DEN226 "Why tablets are not good / Evil Polident" (video 28607388745563297, 3:37), CAD 2,327, ROAS 1.42
- Primary text: PT-D (tablets). Headline: "#1 Dentures Cleaner (Clinical Grade At-Home)". LP: `/pages/brushing-dentures-still-leave-smell-behind-list`.
- Transcript (first ~120 words): "90 years ago, people cleaned their dentures with a brush and water. Then one drug company changed one thing, and it's sitting in your bathroom right now. In 1935, a drug company started selling a powder called Polident. You stirred it into a glass. You dropped your teeth in. Did it clean? You weren't sure. In the 60s, the powder became a tablet. Here's what's in it today. Pool shock. The same chemical used to shock swimming pools. Bleach from laundry detergent, then mint. ... a blue dye that fades to a clear-like solution. So it looks like it's working..."
- Structure: **Hook**: history/nostalgia plus "it's in your bathroom right now". **Villain story**: Polident origin, tablet ingredients (persulfate), big-company ad spend, free samples at dental clinics, a 2008 FDA warning ("73 severe reactions... at least one death"), "Do not place in mouth" label. **Science**: Belgium/Brazil study (tablets had no significant effect on fungus/bacteria), Scotland (film remains and grows back). **Symptoms**: "dentures still smell by lunch, your gums are still sore, that white layer of crust is back by morning". **Mechanism origin**: 1950s ultrasonic cleaning, used by jewelers, hospitals, dentists, "So we built one that fits next to your sink". **Product**: plain tap water, no chemicals, no subscription, 42,000 waves/sec, UV-C, 5 minutes, one button. **Proof**: brown water ("That's what the tablet was leaving behind"), "Over 100,000 people have made the switch". **Offer/CTA**: 120-day try, "If you don't see brown water on the first cycle, send it back" (transcript cuts off).
- Highest hook (62.0%), hold (23.8%) and avg watch (27s) among ads with real spend.

### 15. BX3 DEN267_HOOK 1 (video 1419455460290419, 2:10), CAD 1,879, ROAS 1.16
- Primary text: PT-E ("I thought my dentures were clean... until I tried this"). Headline: "#1 Dentures Cleaner (Clinical Grade At-Home)". LP: smell list page.
- Transcript (first ~120 words): "Most denture wearers don't realize this, but if you wear dentures, cleaning it like this will ruin your life. Here's why. See, every day while you eat and wear your dentures, food debris and bacteria can collect on the surface, including the grooves around the teeth and your gums. Over time, that bacteria can form a sticky layer called biofilm, and every morning, you're putting that build-up back against the tissues of your mouth, which causes irritation and potentially life-threatening infections. Most people think cleaning with a brush, soap, or using a tablet is good enough, but what they don't know is that soap isn't actually a disinfectant..."
- Structure: fear hook, then biofilm mechanism, then a stat (Canadian Medical Association Journal: "27 percent more likely to develop infections like pneumonia"), then "we invested years / tested cleaners" origin, then the ultrasonic bubbles + UVC explanation, the 5-minute routine, and social proof ("Over 20,000 denture wearers"). Offer: new-customer discount, free gifts, 120-day guarantee, 40% off, urgency ("no idea how long we'll be able to run this").

### 14. AW1 DEN 213 V2 (video 836350642867542, 1:57), CAD 1,882, ROAS 1.34
- Primary text: PT-B. Headline: "#1 Dentures Cleaner (Clinical Grade At-Home)".
- Transcript opening: "Before you buy an ultrasonic cleaner for your dentures, watch this. I bought and tested 7 different brands over 90 days, so you don't have to. Number 7. Generic Amazon Cleaners, 2 out of 10... they break within 2 months... It wasn't able to remove the smell from my dentures." Ranking: Zima 7, Sonic Dental 5, Smile Therapy 4, Dr. B 7.5, iSonic 4. DentalPulse 9: "killed 99.95% of the bacteria in just one 5-minute cycle", stainless steel, no tablets, brown water. Offer: 40% off, 120 days. Close: "If you've already wasted money on the wrong one..."

### 16. DG1 DEN308_HOOK 2 V2 (video 1460031319608091, 2:34), CAD 1,821, ROAS 1.46
- Primary text: "Think those retainers, aligners or night guards are clean? Think again... rinse it under the tap... brush it with toothpaste... soak it in a cleaning tablet... hidden biofilm... professionals have relied on ultrasonic cleaning technology for decades. Now the same technology is available at home..." Headline: "#1 Dental Appliance Cleaner (Clinical Grade At-Home)". LP: `/pages/we-tested-5-ultrasonic-cleaners-over-90-days-heres-what-actually-works`.
- Transcript: the DEN81 body adapted for night guards. Opening: "I tested Zima, Sonic, Gurunanda, and Amazon ultrasonic cleaners over 90 days. Most of them fail in one of two ways. Some are too weak to clean the hard plaque buildup that accumulated over years..." Guru Nanda "tight squeeze for a full night guard set", "Put your nightguards in for the first time. Watch the water. It turns brown." One leftover denture line: "It fits your full top and bottom set at the same time."
- CPM CAD 202 (highest in the table). CTR 3.84% and avg watch 16s are strong, but ROAS is only 1.46.

### 17. VID_DEN31_COMPARISON_04 (video 4288485298066500, 1:36), CAD 1,550, ROAS 1.54
- Primary text: PT-A. Headline: "6 of 7 pods leave live bacteria".
- Transcript opening: "Zima dental pod costs three times as much. I tested seven different ultrasonic cleaners over 90 days. Here is what you actually get for the difference." This is a compressed version: cheap Amazon 2-3, mid-range 4-5, then Zima 7 vs DentalPulse 9.5 head-to-head (Zima: "10 minutes instead of five, the tank is plastic... ship it back to the UK"). Close: brown-water guarantee. Lowest hook in the table (18.8%).

### 21. DL3 OCTWK4_VID1_JACK_DentureNightlyRoutine_Hook3 (video 1088356730701373, 2:07), CAD 1,171, ROAS 0.79 (transcribed this run)
- Primary text: PT-C (gift), with CTA type Learn More. Headline: "#1 Dentures Cleaner (Clinical Grade At-Home)". LP: smell list page.
- Transcript (first ~120 words): "If you catch that smell when you hug your mom or dad, even though they brush and soak their dentures every night, that routine is the reason they still smell. The brush, the paste, a tablet fizzing in a glass by the sink, and the set still comes out dull. So the tablets went on your shopping list and you stopped bringing it up. They're doing exactly what they were told. It's the routine that's letting them down. But their set can come out properly clean in five minutes, in plain water, with nothing scrubbing it, and nothing new for them to learn. I'm a dentist, and under my light, I can see the brush on the set..."
- Structure: **Hook**: adult child notices parent's denture smell. **Problem**: brushing scratches softer acrylic, causing haze and holding buildup; "brushing only gets about 60% of the bacteria"; Belgium trial (tablets didn't touch fungus). **Mechanism**: ultrasonic (sound too high to hear), nothing touches the set, UVC runs the whole time ("99.9% of bacteria... sterilized"). **Objection**: "if you're worried they won't take to a gadget, it's one button... matters more the less grip they've got". **Proof**: brown water, "One daughter told me that's when her dad gave up the tablets." **Offer**: "early Black Friday deal... 60% off with free gifts, a travel bag, a portable dental case, one year extended warranty... 120 days".
- Hook 41.0%, 15s/3s 39.4%, but CPM CAD 143 and CPA CAD 195.

### 22. CG2 Night Guards DEN280 (video 1976388577139970, 0:47), CAD 774, ROAS 0.65 (transcribed this run; full)
- Primary text: PT-B (dental-appliance version). Headline: "#1 Night Guards Cleaner (Clinical Grade At-Home)". LP: tested-5 page.
- Transcript (full): "Generic Amazon ultrasonic cleaners. Five. These are usually the cheapest options. If some get the job done, I'd be careful buying one without checking its specifications. Ploys. 3. An interesting option, but I'd want to see more evidence of its cleaning performance before ranking it higher. Sonic. 4. Compact and convenient, but make sure the cleaning chamber is large enough for your dental appliance. Zima Dental Pod. 2. One of the best-known ultrasonic cleaners. Sleek and easy to use, but ultrasonic cleaning alone doesn't necessarily disinfect your appliance. Dental Pulse Pod. One. My top pick. It combines ultrasonic cleaning to help loosen buildup with UV light designed to target bacteria. Two cleaning technologies in one simple daily routine."
- Structure: soft-claim ranked list with no hook line, no proof, no offer and no CTA in the VO.

### CZ1 DEN299 "Drama Ad Dentures" (video 1138016128719318, 3:26, AI), CAD 517 (low spend, high hook), ROAS 0.71 (transcribed this run)
- Primary text: "Have you ever had the feeling your breath smells but the person opposite was too kind to tell you? ... Guess what it was? My dentures..." then the PT-E bullets and reviews. Headline: "#1 Dentures Cleaner (Clinical Grade At-Home)". LP: smell list page.
- Transcript (first ~120 words): "Want one? The second my client offered me gum, I thought, she can smell my dentures. No thanks. Then I spent the rest of her appointment with my mouth closed. I'm 42. I'm a makeup artist. And I wear dentures. Most people in my life don't know. I still imagine the questions, at your age? What happened? So, I keep it to myself. I spend my days helping women feel comfortable showing their faces, but I was getting less comfortable letting anyone close to mine. And I did clean them. I used the soaking tablets, brushed them, rinsed them, but that morning, I checked them before putting them in. There was still this lingering smell..."
- Structure: scripted drama, younger hidden denture wearer (42), social-embarrassment trigger (offered gum), then a confidant scene, then "why the smell is still there" (residue/bacteria in crevices; soaking doesn't loosen every deposit), then the product (ultrasonic bubbles + UVC; fill, place, close, start, rinse), then the 120-day guarantee as purchase trigger, a routine montage, and the payoff (leans in to a client, listening instead of worrying). Soft CTA: "learn more below... 120 days to try it". No discount and no brown-water proof.
- Hook 60.4%, hold 21.7%, avg watch 22s, CTR 1.83%.

### Not transcribed
- CX1 DEN265 "LFS Tablet Conspiracy" (video 2391018344971668, 3:55, CAD 454): the paid transcription call timed out and the transcript was not in cache afterwards (see credits). Primary text: PT-D.
- H9 Retainer DEN162 (CAD 382), AR3, CQ1, CO2, DT2 and the DV series were not transcribed (kept within the 8-transcription cap and the CAD 300 floor).

## Patterns (data only)

**Format and angle**
- The ranked competitor comparison ("I tested 7 cleaners over 90 days", scores out of 10, DentalPulse #1) is the account's spine: about CAD 118.5k of spend in the top video set, blended ROAS 1.77, CPA CAD 89. This beats the account average (1.49 / CAD 106). Every video above ROAS 2.0 with real spend is this format (DEN32 copy 2.28, DEN24 2.39, DEN81 H1/H3/H4 2.64/2.14/2.11).
- Within the comparison format, the long DEN81 body (about 3:00, open loop "I'll show you the one that turned the water brown", brown-water guarantee near the end, "my patients" voice) plus the listicle LP posted the best ROAS (H1/H3/H4: 2.1 to 2.6, CTR 3.5% to 4.5%). Shorter cuts of the same idea, such as DEN31 (1:36) and CG2 (0:47), had the lowest hooks and holds.
- Story/mechanism/education videos (tablet history, biofilm fear, drama) get the highest hooks (45% to 62%) and holds (19% to 24% of impressions), plus 13 to 27s avg watch, about double the comparison ads. But they convert worse: about CAD 5.2k combined, ROAS 1.16, CPA CAD 148. BC1 (Polident history, 3:37) is the one story ad near break-even (ROAS 1.42).
- Hook rate does not track ROAS here. The highest-hook ads (BC1, CZ1, H9, CX1, BX3, DL3) all sit at ROAS 0.3 to 1.4, and the top-ROAS ads sit at hook 26% to 35%. CTR and LP type line up with ROAS better than hook does.
- Dentist/professional voice appears in the strongest comparison scripts ("all my patients are using", "I would never recommend to my patients"; DL3 "I'm a dentist"). The CP1 gift VO says "Orthodontists recommend".
- Labels in ad names: "AI+ExistingFootage" (AD2, BC1), "AI" (CZ1), "Mash-Up" (AY1, CAD 214, disapproved), "UGC" (H9), "LFS" (CX1). There is no clean UGC vs AI split in spend; AI and existing-footage cuts are among the top 15.

**Appliance / avatar**
- Dentures dominate spend and results. Night-guard-specific videos (CI1, CG2, CS1, DG1, DG3): about CAD 7.8k, ROAS 1.03, CPA CAD 152, CPM CAD 137 (highest group CPM). The night-guard static AX50 had ROAS 1.48 on CAD 373 (LC-adjacent).
- Retainer ads underperform: H9 sleep-apnea retainer video ROAS 0.48 (hook 58%), AX40 retainer static ROAS 0.66.
- Persona cues seen in transcripts: the senior denture wearer (default), the adult child buying for mom/dad (DL3, CP1), a younger hidden denture wearer (CZ1, 42-yr-old), and a night-guard wearer (CI1, "cloudy and kind of funky").

**Gift / holiday**
- Gift-angle videos underperform: CP1 (gift VO, Gift PDP, Shop Now) ROAS 0.79 with the weakest retention (15s/3s 22%, p100 0.7%); DL3 (adult-child + early Black Friday 60% off) ROAS 0.79 at CPM CAD 143. Combined about CAD 4.1k, CPA CAD 189.
- The gift static "Denture - HALF PRICE TODAY ONLY - Gift PDP" did well: ROAS 2.81, CPA CAD 56 on CAD 783.
- The top spender A36, DEN32 copy and DC1 all point to the comparison listicle "bundle-pod-gifts" variant, and those ads ran the comparison script, not a gift script (LP group ROAS 1.67).

**Offers seen in the window**
- 40% off (most comparison VOs), "up to 40% off with free gifts", 60% off "early Black Friday" (DL3), "half price today only" (static), "lowest price ever / free gifts up to $50" (CP1, BX3). The 120-day money-back guarantee + 12-month warranty appears in almost every top video. The brown-water "if you don't see it, send it back" guarantee is in the DEN81, DEN31, BC1 and DL3 scripts.

**Landing pages (from link_url)**
- Comparison listicle `we-tested-7-...-bundle-pdp` (ad names with LP_LISTICLE): about CAD 60.9k in the top video set, ROAS 1.81, CPA CAD 87. The best statics also use it (IMG_DEN64/IMG_DEN62: ROAS 2.35 to 3.41).
- `...-bundle-pod-gifts` listicle variant: CAD 59.6k, ROAS 1.67.
- `brushing-dentures-still-leave-smell-behind-list` (story ads BC1, BX3, CZ1, CX1, DL3): CAD 6.3k, ROAS 1.09.
- `we-tested-5-ultrasonic-cleaners...` (appliance/night guard): CAD 2.6k, ROAS 1.22.
- Gift PDP (CP1 video): ROAS 0.79. Gift PDP static: ROAS 2.81.

**Length**
- Top-ROAS videos run 1:53 to 3:09. The 0:47 night-guard cut (CG2) and the 1:19 gift VO (CP1) are the weakest on ROAS. Avg watch is 6 to 16s for most top ads, so most viewers see only the hook and the first ranking positions. The p100 completion rate is 0.5% to 5%.

## Atria credits used (this pull)

- Every MCP call in this session went past the plan's included MCP allowance. Atria swapped 1 workspace credit per call ("call_fee_source: credits"); the reads (summary, ad lists, ad detail, cache transcript lookups) each cost 1 credit.
- The credit-usage log for 2026-11-19, 19:34 to 19:41 UTC, shows **about 55 credits**: about 50 `open_platform_api_usage` (call fees) + 5 `video_script` (transcriptions at 1 credit each).
- **Transcriptions run: 5 (cap 8).** DC1 DEN320, DL3 nightly routine, CG2 night guard, CZ1 drama: succeeded. CX1 LFS tablet conspiracy: timed out and was still not in cache on re-check, though a `video_script` charge appears in the log. Atria says failed transcriptions are auto-refunded; check whether it completes or gets refunded.
- Atria notice: "upgrading the Atria plan includes more MCP calls" (app.tryatria.com plan page).
