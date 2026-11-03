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
