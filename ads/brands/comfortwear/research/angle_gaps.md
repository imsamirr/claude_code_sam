# Angle gaps: what competitors test that we don't

User rule 2026-10-30: if Hike, Stepprs, Footstr or other comfort-shoe brands are testing an angle we have not tested, test it too (with OUR claims only).
Every run: `python ads/atria_pull.py rivals --wide` (writes `data/angle_rivals_<date>.csv`; brands in brand.json `core_competitors` + `angle_rivals`),
tag the angles, and compare with our concepts and account ads. Add 1-3 gap-angle concepts per batch.

## 2026-10-30: 2,182 ads from 17 brands vs 708 of our concepts and account ads

Weight = ads × days running (active ads count 1.5×). "Ours" = our concepts and ads that use the angle.

| Angle | Competitor ads | Weight | Ours | Who is pushing it | Verdict |
|---|---|---|---|---|---|
| Knee / hip / back pain | 452 | 1349 | 51 (never the lead) | Stryde, Konjoun, Footstr | **GAP**: problem framing only, no cure claims (AG_09) |
| Morning first steps (PF) | 138 | 634 | 18 | Stepprs (458-day winner), Konjoun | **GAP** (AG_03) |
| Hands-free / no bending | 177 | 428 | 4 | Armadilo, Konjoun, Hike | **GAP**: our bungee slip-on fits (AG_01, AG_02) |
| Scarcity / restock / sold out | 88 | 436 | 2 | Konjoun, Footstr, WearStand | **GAP**: only with true stock facts |
| "It's not age, it's your shoes" | (Konjoun scaling 20+ new variants in 5 days) | | 0 | Konjoun | **GAP** (AG_04) |
| Age call-out, 60+/65+ | 123 | 274 | 10 | Konjoun, Armadilo | **GAP** (AG_01, AG_05) |
| Style / doesn't look orthopedic | 125 | 338 | 18 | OrthoFit, Hike | **GAP** (AG_08) |
| Overstock reason-why discount | OrthoFit 86 days | | 0 | OrthoFit | GAP: only if true (AG_06) |
| Buy direct / anti-counterfeit | 25 | 82 | 3 | Stepprs (456 days), Stryde, Clove | GAP: only if knockoffs exist (AG_07) |
| Brand-vs-brand comparison | 124 | 479 | 17 | Stepprs, Armadilo | partly tested (W45 comparisons) |
| Posture / alignment | 138 | 321 | 0 | Footstr, Hike | skip: claim risk |
| Circulation / compression | 76 | 204 | 1 | Viasox | skip: claim risk, not our product |
| Barefoot / grounding | 197 | 641 | 1 | Konjoun, Hike | skip: opposite product (counter-angle possible) |
| Waterproof / winter | 255 | 1049 | 64 | Stryde, Konjoun | skip: knit shoe is not waterproof |
| Flat feet (kids) | 79 | 160 | 2 | Footstr | skip: kids product |
| Golf / pickleball | 24 | 101 | 1 | WearStand, OrthoFit | later test (retirees) |
| Quiz / finder | 18 | 26 | 1 | Vionic | later (needs a landing page) |
| BOGO offer | Konjoun, Stryde | | 0 | | **ask user**: not our offer |
| Plus-size | 6 | 12 | 67 | Hike | we lead here |
| Travel | 47 | 86 | 187 | Vionic | we lead here |

Format refs saved: g_over60_callouts (Armadilo), g_first_then_soon + g_asleep_wakes (Konjoun), g_face_split (Stepprs).
Batch: weeks/2026-W45-angle-gaps (AG_01-09).

## 2026-11-03: 2,219 ads from 17 brands (Hike 96, Stepprs 159, Footstr 154, Orthofeet 142, Kuru 104, Vionic 123, OrthoFit 163, Clove 81, WearStand 146, Musabela 161, Armadilo 168, Konjoun 195, Stryde 186, Foamr 163, Viasox 175)

Change vs 2026-10-30 (keyword tags on title+body; ads / weight = ads x days running, active 1.5x):

| Angle | Ads now (was) | Weight | Pushing it | Ours | Verdict |
|---|---|---|---|---|---|
| Gift for mom / holiday | 170 (105) | 2,457 | Hike, Stepprs, Footstr, OrthoFit | 5 concepts, never the lead | **GAP, tested T45_12** |
| Plus-size / "heavier women" | 56 (33) | 423 | Hike (3 new ads, 4d), Armadilo, Viasox | 67 (we lead) | Answer, T45_08/09/18 |
| Night pain / sleep | 44 (33) | 2,584 | Footstr, Konjoun, Stepprs | few | **GAP, tested T45_07** |
| Anti-counterfeit | 13 (13) | 1,831 | Stepprs 410d, Konjoun, Kuru | 3 | **GAP, T45_11, needs_confirmation** |
| Hands-free / slip-on | 63 (84) | 1,137 | Armadilo, Hike, OrthoFit | 4 | tested T45_10 (angle_gap) |
| Fall / balance | 198 (175) | 13,948 | Armadilo, Hike, Konjoun | 0 | Skip fall claims; answer with "slip-resistant grip" only, T45_20 |
| Scarcity (last 200 pairs, ends midnight) | 94 (86) | 9,002 | Footstr, Hike, Konjoun | 2 | needs TRUE stock/deadline facts: ASK USER; none used |
| Reason-why discount (overstock/mistake) | 64 (65) | 1,812 | Footstr, OrthoFit, Viasox | 0 | needs a true reason: ASK USER; none used |
| BOGO / buy N get N | 336 (347) | 17,206 | Musabela, Stryde, Viasox, Peak, Evolv | 0 | Not our offer: ASK USER, none used |
| Knee/hip/back | 460 (454) | 22,199 | Footstr, Konjoun, Stryde | 51 | tested in T45_16 as nurse mash-up |
| Morning first steps | 134 (145) | 21,658 | Hike, Konjoun, Stepprs | 18 | tested T45_05 |
| Wide feet | 311 (292) | 15,543 | Armadilo, Musabela, OrthoFit | few | tested T45_17 (roomy toe box wording only) |
| Posture, grounding, circulation | - | - | Hike (ROOTSIE grounding, new) | 0 | skip: claim risk / other product |

Gap concepts in the batch: T45_07 night pain, T45_12 gift for mom, T45_11 counterfeit (needs_confirmation), T45_10 hands-free. Black Friday: Stepprs and Hike are already running 60-75% BF; our BF batches come with the Nov 6 / Nov 10 runs.

## 2026-11-06: 2,161 ads from 17 brands (keyword tags, ads now (was 11-03); weight = ads x days running)

| Angle | Ads now (was) | Weight | Pushing it | Ours | Verdict |
|---|---|---|---|---|---|
| Black Friday / Cyber Monday | 147 (71) | 349 | Stepprs 91, Konjoun 32, Footstr 16, Armadilo 6 | whole batch | Answered: all W46 ads carry our BF offer |
| Gift for mom / holiday | 60 (32 on narrower tag) | 730 | Hike, Stepprs, Footstr | W46_21 | **GAP tested W46_21** |
| Reason-why discount (overstock / "oops") | 47 (65) | 959 | Evolv (growth rank 5), Footstr, OrthoFit | 0 | **GAP W46_23, needs_confirmation** (true reason required) |
| Hands-free / slip-on | 58 (63) | 745 | Armadilo, Hike Stride | few | tested W46_20, W46_37 |
| Style / not orthopedic-looking | 115 (126) | 3,799 | OrthoFit, Hike letter | 18 | **GAP tested W46_09** |
| Scarcity (last 200 pairs, ends midnight) | 35 (42) | 745 | Hike, Konjoun | 2 | ASK USER: no true stock/deadline fact; none used |
| BOGO / buy N get N | 430 (414) | 12,558 | Stepprs 5-for-2, Evolv, Sorviq | gifts offer B | Our BF offer B (buy 2 pairs, 2 free gifts), no BOGO price math |
| Anti-counterfeit | 12 (13) | 1,687 | Stepprs, Konjoun | 3 | skip: no true knockoff fact |
| Morning first steps | 143 (134) | 14,501 | Stepprs, Konjoun | 18 | tested W46_01/02/22 |
| Knee / hip / back | 651 (597) | 19,489 | Footstr, Konjoun, Stryde | 51 | W46_11 problem framing only |
| Fall / balance, posture, grounding | 192 / - | 5,983 | Hike, Armadilo | 0 | skip: claim risk |

## 2026-11-10: 2,061 ads from 17 brands (keyword tags on title+body; ads now (was 11-06); weight = ads x days running, active 1.5x)

Atria note: the Hike "most impressions" image query failed after retries in the wide pull (Hike is covered by the dedicated `rivals` pull, 100 ads).

| Angle | Ads now (was) | Weight | Pushing it | Ours | Verdict |
|---|---|---|---|---|---|
| Guarantee / risk-free as the headline ("30 days. Zero risk.", "Walk on clouds or it's FREE") | 614 (654) | 30,691 | Stepprs, Konjoun, Stryde, Orthofeet, Hike (whole-ad risk reversal, new 11-10) | punch card, small lines | **GAP: guarantee as the whole ad, tested T46_07** (our 30-day wording only) |
| Golf / pickleball / hobby comfort | 51 (84) | 3,159 | Kuru, WearStand, OrthoFit, Viasox | 1 | **GAP: tested T46_20** (retiree "just comfort") |
| Reason-why discount (overstock / "oops") | 73 (54) | 1,684 | Footstr, OrthoFit, Viasox, Konjoun | 0 live | GAP, **needs a TRUE reason: ASK USER**; none used |
| Black Friday / Cyber Monday | 209 (147) | 760 | Stepprs, Konjoun, Armadilo, Foamr | whole batch | answered (our BF offers A/B) |
| BOGO / buy N get N | 334 (326) | 17,101 | Armadilo, Konjoun, Stryde | offer B (buy 2 pairs, 2 free gifts) | no BOGO price math |
| Gift for mom / holiday | 104 (119) | 2,045 | Clove, OrthoFit, Viasox, Hike | tested W46_21 | covered; not repeated |
| Style / not orthopedic-looking | 94 (102) | 4,099 | OrthoFit, Foamr, Viasox | tested W46_09 | covered |
| Hands-free / slip-on | 54 (52) | 1,195 | Armadilo, Musabela, OrthoFit | tested | covered |
| Morning first steps | 76 (93) | 18,551 | Stepprs, Konjoun, OrthoFit | 18+ | covered |
| Plus-size / heavier women | 6 (9) | 113 | Hike (new "Last chance, built for heavier women", 2d), Musabela | 67 | we lead; answered T46_13 |
| Night / sleep pain | 85 (125) | 3,592 | Footstr, Hike, Konjoun | tested | covered |
| Swelling | 174 (170) | 4,143 | Armadilo, OrthoFit, Viasox | few | test slot T46_18 (comfort-fit wording only) |
| Ball of foot / burning | 3 (6) | 53 | Armadilo, OrthoFit | few | tiny for competitors; our customers say it: test slot T46_17 |
| Fall / balance / posture / grounding / doctor-clinical / anti-counterfeit | 391 / - / 186 / 11 | 18,568 / - / 7,133 / 2,632 | Hike, Armadilo, Kuru, Stepprs | 0 | skip: claim risk or no true fact |
| Knee / hip / back | 385 (418) | 17,299 | Footstr, Konjoun, Stryde | 51 | problem framing only, T46_04 |

Gap concepts this batch: T46_07 (guarantee as the whole ad, Hike "30 days. Zero risk." format), T46_20 (golf / pickleball comfort, WearStand/OrthoFit angle). No reason-why or scarcity concept (no true fact): **ask Samir whether there is a true overstock/inventory reason or a real BF end time**.

## 2026-11-17: 2,152 ads from 17 brands (Hike 96, Stepprs 152, Footstr 133, Orthofeet 145, Kuru 117, Vionic 139, OrthoFit 169, Clove 73, WearStand 145, Musabela 133, Armadilo 154, Konjoun 197, Stryde 188, Foamr 140, Viasox 169; 706 new since 11-13). Keyword tags on title+body; weight = days running x (1.5 if active). "Ours" = all weeks/*/concepts.json headlines+angles.

| Angle | Ads | Weight | Pushing it | Ours | Verdict |
|---|---|---|---|---|---|
| Guarantee / risk-free as the headline | 556 | 35,753 | Konjoun, Orthofeet, Stryde, Stepprs, Hike ("No pain relief = FULL REFUND", new) | 14 | covered (T46_07); answered again T47_12 |
| Age call-out (over 60, seniors, retirees) | 439 | 34,308 | Kuru, Armadilo, Konjoun, OrthoFit, Hike | 20 | **GAP (combined with wet/winter): T47_19** |
| Knee / hip / back | 574 | 30,441 | Stryde, Konjoun, Kuru, Footstr | 43 | covered (T47_02, T47_05 nurse framing) |
| Morning first steps | 143 | 22,045 | Stepprs, Konjoun, Viasox, Hike | 12 | covered (T47_11) |
| BOGO / buy N | 381 | 19,752 | Stryde, Viasox, Musabela, Konjoun | 15 | offer we don't run: no |
| Fall / balance / stability | 284 | 16,089 | Stryde, Armadilo, Konjoun, Hike | 9 | skip: claim risk (grip wording only) |
| Winter / cold / wet | 289 | 9,064 | Viasox, Footstr, Konjoun, Orthofeet, Hike winter boots | 34 (mostly "warm"/"ice" matches) | **GAP: wet fall sidewalks + grip, T47_19** |
| Scarcity / restock / sold out | 56 | 7,285 | Konjoun, Clove, Footstr, WearStand, Hike (sold out 5x, last 190 pairs) | 3 | **GAP: T47_20, needs_confirmation (true restock?)** |
| Style | 94 | 4,708 | Vionic, Viasox, OrthoFit, WearStand | 32 | covered |
| HSA/FSA | 44 | 3,483 | WearStand, Kuru, Clove | 10 | covered |
| Pickleball / golf | 31 | 2,388 | WearStand, OrthoFit, Kuru | 2 | tested T46_20 |
| Counterfeit | 7 | 2,272 | Stepprs, Konjoun, Stryde | 2 | skip: needs a true fact (ask user) |
| Reason-why discount (overstock) | 38 | 1,980 | Viasox, Footstr, OrthoFit, Konjoun | 13 | needs a TRUE reason: ask user |
| Swelling | 57 | 1,970 | Viasox, Hike, Armadilo | 22 | test slot T47_13 (stretch-knit wording only) |
| Neuropathy / diabetic | 30 / 13 | 1,290 / 688 | Konjoun, Stepprs, Viasox | 3 / 0 | skip: medical/personal-attribute risk |
| Chef / kitchen / server | 34 | 751 | Footstr, Armadilo, WearStand | 8 | tested W47_22 |
| Plus-size / heavier women | 5 | 105 | Hike, Musabela | 84 | we lead |

Gap concepts this batch: **T47_19** (over 60 + wet fall sidewalks, slip-resistant grip only, no fall-prevention claim) and **T47_20** (Black/Purple "back in stock", Hike sold-out/restock format) **needs_confirmation: launch only if Black/Purple truly sold out and was restocked**.

## 2026-11-20: 2,136 ads from 17 brands (Hike 93, Stepprs 161, Footstr 143, Orthofeet 138, Kuru 118, Vionic 141, OrthoFit 168, Clove 68, WearStand 141, Musabela 137, Armadilo 161, Konjoun 176, Stryde 189, Foamr 134, Viasox 165, Snibbs 2, Bright 1; 479 new since 11-17). Keyword tags on title+body; weight = days running x (1.5 if active). "Ours" = all weeks/*/concepts.json headlines+angles (58 files). Keyword map tightened this run ("rain" no longer matches "strain", "free gift" split from holiday gifting, travel bag excluded), so winter/gifting weights are lower than 11-17 and not comparable.

| Angle | Ads | Weight | Pushing it | Ours | Verdict |
|---|---|---|---|---|---|
| Nurse / healthcare / 12h shifts | 301 | 30,562 | Stepprs, Stryde, WearStand, OrthoFit | 290 | covered (we lead) |
| Plantar fasciitis / heel pain | 216 | 29,933 | Stepprs, Kuru, OrthoFit, Foamr, Orthofeet | 85 | covered |
| Knee / hip / back | 453 | 22,287 | Stryde, WearStand, Konjoun, Footstr | 34 | covered |
| Guarantee / risk-free headline | 553 | 21,894 | Stryde, Konjoun, OrthoFit, Orthofeet, Hike ("Better balance or you don't pay") | 28 | covered (T47_12) |
| Morning first steps | 141 | 21,694 | Stepprs ($42 → $11 "Morning heel pain"), Konjoun, Viasox | 15 | covered (T47_11) |
| Fall / balance / stability | 374 | 20,270 | Stryde, Armadilo, WearStand, Konjoun, Hike | 24 | skip: claim risk (grip wording only) |
| BOGO / buy N | 471 | 19,697 | Stryde, Armadilo, Viasox, Konjoun, Hike BF 1+1 | 15 | offer we don't run: answer with BUY 2 PAIRS, GET 2 FREE GIFTS |
| Bunions / wide toe box | 385 | 9,934 | OrthoFit, Armadilo, Hike, Musabela | 32 | covered (room for bunions; no extra-wide promise) |
| **Doctor / podiatrist recommended as the lead** | 194 | 8,301 | Stepprs ("Dr. Thomas", podiatrist-recommended), WearStand ("Podiatrist-approved. HSA/FSA eligible."), Orthofeet ("Reasons to try" grid, 118d), OrthoFit ("My podiatrist said it's not my knees", 100d) | 2 (only as badges inside prompts) | **GAP: approved claim we barely headline. Ref `rv420g_orthofeet_reasons_grid_podiatrist.jpg`** |
| Style | 147 | 6,724 | WearStand, Kuru, OrthoFit, Vionic | 36 | covered |
| Scarcity / restock / sold out | 121 | 6,164 | Konjoun, WearStand, Stepprs, Hike | 3 | needs_confirmation (T47_20 pending) |
| Grounding / barefoot | 125 | 5,682 | Konjoun, Hike (ROOTSIE), Armadilo | 2 | skip: wrong product + claim risk |
| Age call-out (over 60, retirees) | 124 | 4,548 | Konjoun, OrthoFit, Armadilo, Hike ("Retirement without sore feet", new) | 23 | covered (AG_ series, T47_19) |
| Hands-free / slip-in | 105 | 3,736 | Stepprs, Armadilo, Konjoun, Hike | 5 | covered (W46_37, W45_31) |
| Swelling | 143 | 3,520 | Viasox, OrthoFit, Armadilo, Hike ("14 days to relieve swollen ankles") | 48 | covered (stretch-knit wording only) |
| HSA/FSA | 42 | 3,215 | WearStand, Kuru | 15 | covered (pair with podiatrist gap) |
| Counterfeit | 13 | 2,774 | Stepprs, Kuru, Stryde, Konjoun | 2 | needs_confirmation: needs a true fact (ask user) |
| Pickleball / golf | 29 | 2,338 | WearStand, OrthoFit, Kuru | 3 | tested T46_20 |
| BF free gift / bundle bonus | 89 | 2,068 | OrthoFit, Stepprs (free gift + $20K/$25K giveaway), Konjoun, Clove | 20 | covered (our 2 free gifts); giveaways: skip |
| Holiday gifting (mom, Christmas) | 52 | 1,024 | Footstr, Viasox, Clove ("The Gift of Comfort"), Hike ("Coziest gift", "Best gift for mom") | 41 | covered |
| Holiday travel | 41 | 784 | WearStand, Vionic, Viasox | 236 | we lead |
| Neuropathy / diabetic | 15 | 778 | Orthofeet, Viasox, Stepprs | 4 | skip: medical/personal-attribute risk |
| Winter / cold / wet | 94 | 735 (+ Hike Cozely, 0-5d) | Footstr, Musabela, Orthofeet, Hike | 5 | covered by T47_19 (wet sidewalks); boots = wrong product |
| Chef / kitchen / server / retail | 27 | 470 | WearStand, Footstr, Orthofeet | 13 | covered |
| Reason-why discount (overstock / mistake) | 17 | 265 | Footstr, OrthoFit ("We Are Sorry! We overstocked"), Stepprs ("We f*cked up", on-image) | 8 | needs_confirmation: TRUE reason only (ask user) |
| Plus-size / heavier women | 4 | 106 | Hike, Musabela | 99 | we lead |
| GLP-1 / weight loss | 0 | 0 | none | 1 | skip: nobody tests it, claim risk |
| **Walking again / walks cut short** | 14 (+10 new Stepprs statics, 1-2d, on-image) | 24 (all new) | Stepprs ("Tired of being the one who turns back early?", "You never wanted to quit walking", "It wasn't the walk, it was the aching after"), Hike ("I now walk farther", Margaret, 63) | 0 daily-walk headlines (10 "steps" headlines are travel) | **GAP (new test by Stepprs, 10 variants at once). Ref `rv420g_stepprs_walks_turn_back_early.jpg`** |
| **Brand humor: "We're sorry" side effects (no offer)** | 1 by keyword; 5 new Stepprs statics on-image (1d) | 22 | Stepprs ("We're Sorry. Your daily step count has become your entire personality"), OrthoFit | 9 apologies, all discount reason-why | **GAP (format: comfort side-effects, no discount reason needed). Ref `rv420g_stepprs_were_sorry_side_effects.jpg`** |

Gap picks for the 2026-11-20 Friday batch (tag `angle_gap`): (1) **podiatrist-/doctor-recommended as the headline** with a reasons grid (approved claims only: podiatrist-recommended, HSA/FSA eligible, 30-day money-back guarantee, free shipping & returns, 500,000+; no "approved", no named doctor, no counts); (2) **walking again** for the daily-walker persona who cuts walks short (comfort / arch support wording, no "pain-free"); (3) **"We're sorry" comfort side-effects** humor card (e.g. step count, longer walks; no offer reason needed). None needs_confirmation. Not repeating T47_19 (over-60 wet sidewalks) or T47_20 (back in stock).

## 2026-11-24: 2,271 ads from 17 brands (Hike 95, Stepprs 136, Footstr 148, Orthofeet 138, Kuru 119, Vionic 144, OrthoFit 159, Snibbs 109 (new in the pull: slip-resistant work shoes), Clove 77, WearStand 149, Bright 16, Musabela 137, Armadilo 158, Konjoun 200, Stryde 188, Foamr 132, Viasox 166; 885 new since 11-20). Keyword tags on title+body; weight = days running x (1.5 if active). "Ours" = all weeks/*/concepts.json headlines+angles (962 concepts). Snibbs entering the pull inflates nurse, guarantee and fall/slip counts vs 11-20.

| Angle | Ads | Weight | Pushing it (ads) | New since 11-20 | Ours |
|---|---|---|---|---|---|
| Nurse / 12h shifts | 370 | 31,046 | Snibbs 85, Stryde 82, Stepprs 61, Musabela 47 | 159 | 319 |
| Plantar fasciitis / heel | 211 | 27,530 | Kuru 106, Stepprs 46, Foamr 38, Footstr 12 | 28 | 87 |
| Knee / hip / back | 428 | 21,319 | Stryde 184, Konjoun 98, WearStand 56, Footstr 47 | 217 | 35 |
| Guarantee headline | 720 | 37,057 | Konjoun 153, Snibbs 109, Stepprs 91, Stryde 86 | 350 | 30 |
| Morning first steps | 81 | 20,236 | Stepprs 46, Konjoun 17, OrthoFit 12, Hike Footwear 3 | 24 | 19 |
| Fall / balance | 463 | 21,320 | Snibbs 109, Stryde 88, Konjoun 63, Armadilo 54 | 231 | 25 |
| BOGO / buy N | 391 | 18,437 | Stryde 183, Konjoun 57, Viasox 46, Musabela 45 | 213 | 19 |
| Bunions / toe box | 358 | 9,006 | Musabela 135, OrthoFit 135, Hike Footwear 39, Armadilo 34 | 80 | 29 |
| Doctor / podiatrist | 241 | 7,261 | Musabela 85, WearStand 56, Footstr 35, Konjoun 24 | 82 | 5 |
| Scarcity / sold out | 57 | 7,521 | Konjoun 45, Hike Footwear 5, Bright Footwear 3, WearStand 3 | 44 | 4 |
| Grounding | 8 | 18 | Konjoun 6, Hike Footwear 2 | 8 | 0 |
| Age call-out 60+ | 65 | 2,244 | Armadilo 31, OrthoFit 24, Hike Footwear 9, Kuru 1 | 14 | 27 |
| Hands-free | 38 | 1,066 | Hike Footwear 11, OrthoFit 10, Snibbs 7, Armadilo 6 | 13 | 5 |
| Swelling | 103 | 1,769 | Viasox 97, Hike Footwear 3, Armadilo 2, OrthoFit 1 | 100 | 28 |
| HSA/FSA | 75 | 3,338 | WearStand 64, Kuru 11 | 37 | 18 |
| Holiday gifting | 23 | 604 | Footstr 16, Konjoun 4, Armadilo 1, Bright Footwear 1 | 6 | 17 |
| Winter / cold / wet | 85 | 522 | Footstr 52, Bright Footwear 9, Orthofeet 9, Hike Footwear 5 | 52 | 7 |
| Heavier / plus-size | 4 | 105 | Hike Footwear 2, Musabela 2 | 1 | 107 |
| Walking again | 0 | 0 |  | 0 | 1 |
| Adult child worried about parent | 0 | 0 |  | 0 | 1 |
| Reason-why / apology | 3 | 76 | OrthoFit 2, Bright Footwear 1 | 1 | 10 |
| Neuropathy | 26 | 1,746 | Viasox 16, Konjoun 4, Stepprs 3, Orthofeet 2 | 22 | 4 |

Verdicts this run:
- **Adult child worried about mom in winter: GAP.** Hike launched it on-image this week (0-1d: "Worried about mom slipping this winter? Get her these.", "Your mom will never trip & fall wearing these boots", "My Mom's Falls Stopped After Wearing These"); the keyword pull misses it because the words are on the image. We have 1 concept that touches it. Test with slip-resistant grip + support wording only (no fall/balance claims): **T48_17** (`angle_gap`).
- Doctor / podiatrist as the lead: still under-used (5 ours vs 241 ads); tested once in W48_37 (Fri), plus T48_06 (podiatrist-recommended + HSA/FSA) this run.
- Heavier / plus-size: Hike is now testing it hard on-image (4+ new statics); we still lead (107) and answer with T48_01/02/10.
- Reason-why / scarcity / counterfeit / BOGO: not used this run (no confirmed facts; BOGO not our offer).
- Walking again: tested W48_38 (Fri); not repeated.


## 2026-11-27: 2,315 ads from 17 brands (Hike 97, Stepprs 151, Footstr 155, Orthofeet 143, Kuru 133, Vionic 146, OrthoFit 160, Snibbs 109, Clove 75, WearStand 153, Bright 24, Musabela 137, Armadilo 156, Konjoun 196, Stryde 187, Foamr 121, Viasox 172; 670 new since 11-24). Keyword tags on title+body; weight = days running x (1.5 if active). "Ours" = all weeks/*/concepts.json headlines+angles (1,014 concepts). New rows this run: grandkids, walking group, shopping cart / independence, travel, teacher. Sheet of gap refs: `sheets/angle_gap_refs_1127.jpg`.

| Angle | Ads | Weight | Pushing it (ads) | New since 11-24 | Ours |
|---|---|---|---|---|---|
| Nurse / 12h shifts | 390 | 31,995 | Stryde 74, Snibbs 73, Stepprs 71, Musabela 46 | 71 | 307 |
| Plantar fasciitis / heel | 227 | 27,452 | KURU Footwear 109, Stepprs 54, Foamr 28, Footstr 12 | 90 | 88 |
| Knee / hip / back | 442 | 21,694 | Stryde 149, Konjoun Barefoot 79, Footstr 41, WearStand 29 | 177 | 35 |
| Guarantee headline | 677 | 27,361 | Konjoun Barefoot 133, Snibbs 95, Footstr 86, Stryde 74 | 199 | 30 |
| Morning first steps | 109 | 20,989 | Stepprs 54, OrthoFit Store 18, HIKE Footwear 14, Konjoun Barefoot 9 | 33 | 22 |
| Fall / balance | 520 | 22,760 | Snibbs 95, Stryde 74, Armadilo 56, Konjoun Barefoot 50 | 134 | 88 |
| BOGO / buy N | 421 | 22,564 | Stryde 152, Konjoun Barefoot 57, Musabela 44, Viasox 43 | 139 | 18 |
| Bunions / toe box | 356 | 8,944 | Musabela 134, OrthoFit Store 88, HIKE Footwear 35, Armadilo 34 | 72 | 29 |
| Doctor / podiatrist | 266 | 9,269 | Musabela 85, Footstr 35, Konjoun Barefoot 30, WearStand 26 | 65 | 5 |
| Scarcity / sold out | 227 | 12,691 | Stepprs 59, Konjoun Barefoot 46, OrthoFit Store 29, Footstr 25 | 102 | 9 |
| Age call-out 60+ | 87 | 3,050 | Armadilo 31, OrthoFit Store 28, Konjoun Barefoot 12, HIKE Footwear 8 | 18 | 42 |
| Hands-free | 40 | 920 | OrthoFit Store 7, Snibbs 7, Armadilo 6, HIKE Footwear 5 | 6 | 5 |
| Swelling | 152 | 1,159 | Viasox 121, Armadilo 11, OrthoFit Store 10, HIKE Footwear 4 | 95 | 52 |
| HSA/FSA | 80 | 3,010 | WearStand 34, johntoftecreates with WearStand 15, alexandereasley with WearStand 7, KURU Footwear 6 | 43 | 27 |
| Holiday gifting | 24 | 593 | Footstr 16, Konjoun Barefoot 3, Viasox 2, Armadilo 1 | 4 | 22 |
| Winter / cold / wet | 197 | 1,866 | Footstr 85, OrthoFit Store 35, Bright Footwear 20, Konjoun Barefoot 15 | 114 | 20 |
| Heavier / plus-size | 5 | 50 | HIKE Footwear 3, Musabela 2 | 3 | 107 |
| Neuropathy | 90 | 1,712 | Footstr 64, Konjoun Barefoot 8, Viasox 6, Stepprs 4 | 60 | 12 |
| Grandkids | 8 | 438 | OrthoFit Store 3, aiugcboris with OrthoFit Store 1, kiya davelaar with OrthoFit Store 1, _bymaku with OrthoFit Store 1 | 0 | 7 |
| Walking group / club | 17 | 197 | HIKE Footwear 12, OrthoFit Store 3, Peteyrific with OrthoFit Store 1, bodycams4 with OrthoFit Store 1 | 7 | 3 |
| Shopping cart / independence | 26 | 663 | Konjoun Barefoot 16, OrthoFit Store 5, HIKE Footwear 4, Musabela 1 | 14 | 14 |
| Travel | 43 | 845 | Viasox 11, OrthoFit Store 10, Vionic Shoes 10, Paul The Podiatrist with KURU Footwear 2 | 18 | 277 |
| Teacher | 2 | 22 | Footstr 1, WearStand 1 | 1 | 22 |

Verdicts this run:
- **Knee / hip / back: GAP** (442 ads, 177 new; Stryde 149, Konjoun 79 vs our 35). Tested: W49_30 (nurse knees, ref Stryde "For the knee that keeps telling you to stop", 83d). Also W49_11 (hard floors) and W49_29 (servers) carry knee/back.
- **Doctor / podiatrist lead: GAP** (266 vs our 5). Tested: W49_31 (housekeeper, ref OrthoFit "My podiatrist said it's not my knees. It's my shoes.", 108d). Podiatrist-recommended is approved; no named doctor.
- **Winter / cold / wet: GAP, rising** (197 ads, 114 new; Footstr 85, OrthoFit 35 vs our 20). Tested: W49_32 (home health aide on a wet porch, ref OrthoFit winter boot), plus winter scenes W49_21/35/36. Approved "slip-resistant grip" only, never fall prevention.
- Guarantee headline (677 vs 30): still open; W49_23 and W49_30 carry a guarantee line. Next run candidate.
- Fall / balance (520), scarcity (227), BOGO (421): skip (fall-prevention claims, no confirmed stock facts, BOGO is not our offer). No reason-why/scarcity/counterfeit concept this batch, so nothing needs confirmation.
