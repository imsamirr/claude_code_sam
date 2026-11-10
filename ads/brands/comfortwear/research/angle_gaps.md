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
