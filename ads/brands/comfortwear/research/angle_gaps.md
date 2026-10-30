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
