# Comfort Wear static ad research (WearOrtho ad account)

Pulled 2026-10-10 from Atria (WearOrtho Meta account, Jan 2024 to Oct 2026), the Atria ad library, and Trustpilot (ca.trustpilot.com/review/comfortorthowear.com).

| Input | What was pulled | File |
|---|---|---|
| Winning statics | 38 unique static creatives with **$5k+ lifetime spend** (C$4.16M combined, duplicates merged by image) | `data/winning_statics.csv` |
| Losing statics | 90 statics that spent **under $200** and were **paused at ad level** (last 12 months; C$9,975 combined) | `data/losing_statics.csv` |
| Video scripts | Atria transcripts of the 10 top video ads (spend $15k+ and ROAS 1.4+) | `data/video_transcripts.md` |
| Inspiration | 72 Atria library image ads: **launched in the last 30 days, impressions rising**, still active, foot-pain and footwear queries | `data/inspiration_rising_30d.csv` |
| Reviews | Trustpilot: 3.7 TrustScore, 3,141 reviews. 52% 5★, 21% 1★ | (summarized below) |
| Notion | Scripts 2026, Creative Tracker (old) with learnings, Ad Angle Databank (100 angles) | `data/notion_angles.md` |
| Brand inspiration | 167 long-running image ads: Vessi, Stepprs, ComfoFeet, Orthora, Orthofeet, KURU, Clove, WearStand, HIKE + non-footwear pain/nurse/bunion/arthritis brands | `data/brand_inspiration_longrunning.csv` |

> **Data caveat:** from about Feb 2025, many high-spend ads show ROAS near 0.02 in Atria (e.g. "Kyro 154v2ss2" image, $500k spend at 0.04). That looks like a purchase-tracking or attribution break, not real performance, so ROAS from that period isn't reliable. Spend (Meta's own allocation) is the ranking signal, as you asked.

---

## 1. What the $5k+ statics have in common

**1. They speak to nurses on 12-hour shifts, and the audience is in the headline.**
Seven of the top 10 statics open with the shift or the job title: *"12-HOUR SHIFT SHOES"* ($858k), *"Shoes for 12-Hour Shifts. Made for Nurses"* ($457k), *"Dear Nurses, Work 12-hour shifts pain-free"* ($230k, **4.34 ROAS**, the best efficiency of any big static), *"Game-Changer For Long Shifts At The Hospital"* ($120k), *"Healthcare Workers Top Rated Orthopedic Shoes"*.

**2. Each benefit is tied to a named condition, with arrows pointing at the shoe.**
Plantar fasciitis → arch support · bunions/hallux valgus → wide toe-box · wet floors → slip-resistant grip · blood circulation. The layout is a white or lavender background, one shoe in side profile, and four arrowed callouts. It is your most reused template (#1–#4, #14, #20, #23).

**3. Competitor call-outs.**
*"HOKA / SKECHERS / ORTHOFEET / CROCS / INSOLES"* crossed out, with a *"SOLUTION"* panel ($90k). Every top video script makes the same argument: *"running shoe cushioning lasts about 2 hours, ComfortWear lasts 12."*

**4. Social proof with real comments works best for retargeting.**
*"Didn't buy yet? Read what customers are saying"* with Facebook-style comment bubbles: $50k at **3.05 ROAS** and still active, the most efficient static running now.

**5. Offer and urgency statics scale, but only with a clear offer.**
"40% OFF ENDS TODAY + SAVE10" ($152k, $115k), "LAST CHANCE TO SAVE" ($125k), "WARNING: Only 48 hours left" warehouse photo (**3.31 ROAS**, active), "ALMOST SOLD OUT" (3.97 ROAS).

**6. Transformation hooks.**
*"I Lost 50lbs+ After Walking 20,000+ Steps Daily"* ($93k).

## 2. What the losers (under $200, paused) have in common

Many losers reuse the *same layouts* as winners, so the layout alone isn't what decides it. The patterns:

- **The audience moved away from nurses.** Cashiers, seniors, errands, teachers, gifting, travel, weight loss, neuropathy, arthritis. The *"Dear Nurses"* template, re-headlined as *"A pharmacist in Rome told me…"* (L9, $46) and *"Why 50,000 frequent travelers won't fly without these"* (L80), died. Travel works in **video** (the Kyro 293 / 369 / 373 scripts) but not as a static.
- **Holiday and sale-only creative with no reason to believe.** Black Friday, July 4th, Prime Day, Halloween, "VIP Access", countdown timers. About 20 of the 90 losers are pure promo graphics.
- **Too much text, or tall 9:16 layouts** (wall-of-text testimonials, comparison tables like *"Built for nurses, not runners"* scorecard L17, email-screenshot L70).
- **Lo-fi props didn't land** (napkin sketches L40/L51, sticky notes L86, bare-feet photos L13/L38). Be careful copying "native lo-fi" inspiration one-to-one.
- **Unanchored big claims** ("Relief instantly or your money back", "14 days to relieve arthritis", "Doctor recommended" badge). They also attract disapprovals: 186 of the ~1,100 ads pulled show DISAPPROVED, including several big winners.

## 3. Script angles from the top videos (Atria transcripts)

| Angle | Line to steal | Ad |
|---|---|---|
| Doctor dismissal | "My doctor said I'll have to live with this foot pain forever." | Kyro 141 ($108k) |
| Running shoes fail | "ComfortWear offers over 12 hours of comfort, while running shoes' cushioning lasts about two hours." | Kyro 141/99/154 |
| Price anchor | "I spent $60 on these… way cheaper than the $300 orthotics my podiatrist wanted me to buy." | 203 UGC ($100k, **3.05 ROAS**) |
| Peer contagion | "Three other nurses on my floor ordered them after seeing mine." | 203 UGC |
| Industry secret | "Three things the healthcare industry doesn't want you to know." | Kyro 172 ($70k) |
| Shift payoff | "No more limping to my car after a 12-hour shift." | 203 UGC |
| Tested and ranked | "We tested five of the most popular [travel] shoes…" | Kyro 293 ($58k, 2.15 ROAS) |
| Body-type identity | "My doctor said I'd never walk normally again because of my weight." | Kyro 170 ($106k) |

## 4. Trustpilot: customer language to use, and a warning

**Language to use (5★):** "Great for my 12 hour shifts", "fits my extra-wide feet", "the toe room sold me", "my feet aren't tired after a busy day", "traveling teacher… feet no longer hurt", "didn't worsen my diabetic nerve pain", "instant balance and stability" (78-year-old), "HSA payment accepted".

**Warning (21% 1★):** almost all 1★ reviews are about **refunds and the money-back guarantee not being honored** (partial refunds, gift cards, "proof of donation"), plus inconsistent sizing, "cheap materials" and "drop-shipping scam". Recommendations:
- Don't lead creatives with "45-day money-back guarantee / no questions asked" until operations actually honor it. It's the promise behind most of the 1★ reviews and makes ads read as deceptive.
- Sizing is the #2 complaint, so add "true-to-size guide" or "fits wide & narrow feet" messaging.
- Atria also shows a "Nurse Finds" page running ads with your exact shoe. If it isn't one of your pages, it's worth checking for knockoffs or affiliates.

## 5. Inspiration: rising image ads launched in the last 30 days

Formats worth adopting (refs match `data/inspiration_rising_30d.csv`):

| Format | Example | Why it fits Comfort Wear |
|---|---|---|
| **Stage-progression infographic** | I14 "4 Stages of Leg Swelling", I66 "4 Stages of Bone-on-Bone Knee Pain" | Maps directly to the 12-hour shift (hour 2 / 6 / 8 / 12) |
| **Symptom checklist** | I59 Senzio "Do you have plantar fasciitis?" | Self-qualification in customer words |
| **Short identity headline + lifestyle** | I25 ComfoFeet "Still mows his own lawn." | Nurse version: "Hour 12. Still smiling." |
| **Anatomy marker** | I44/I70 Neurotoned "This tissue is making my plantar fasciitis worse" | Proven mechanism story; your plantar-fascia anatomy static already won |
| **Native Facebook post / comments** | I54 "Has anyone else with swollen feet tried these?" | Same mechanic as your 3.05-ROAS comments static |
| **"5 reasons" on a real scene** | I3 Nurse Finds "5 reasons to wear these shoes for 12-hour shift" | Your $858k checklist, made photographic |
| **Sole-forward hero** | I5 The Clog Shop "Bold print. Real arch support.", I0 Musabela | Proves slip-resistance visually |

## 6. Your Notion angles (full notes: `data/notion_angles.md`)

- **2026 production is mostly video:** ranking, "podiatrist rates", Hoka/Skechers attacks, nurse identity, body-type/age, retail/servers, travel/Disney. Only 6 statics are in the pipeline (Disney ×2, teacher comparison, nurse coworkers, nurse rating website, healthcare + teachers), even though statics made up a large share of historical $5k+ spend.
- **What your own learnings say kills a concept:** a generic "rates shoes" or tier list with no ComfortWear payoff, too much on-screen text, stock footage, and "only the product, not the real problem". The concepts below follow those rules: one problem, one payoff, legible at a glance.
- **Databank angles not yet tested** that fit statics: 12-hour countdown, foam dies at hour 4, annual cost math, cashiers on concrete, vertical toe box/bunions, arthritis no-tie laces, cobblestones.

## 7. Brand inspiration: long-running image ads (`data/brand_inspiration_longrunning.csv`)

These are ads still being paid for after months, a better signal of profitability than "new and rising". B-refs match the CSV.

| Brand | Proven format | Runtime | What to take |
|---|---|---|---|
| **Stepprs** | Words written on the sole of a foot: "12 years of plantar fasciitis pain gone" (B8/B11). Old-vs-new insole split (B14). Sticky notes on product (B9). "Finish 12 hour shifts with ZERO foot pain" in a warehouse (B12) | 386 days | Pain written on the body (C18), the collapse proof (C17). Their sticky notes work, while your L86 didn't, so execution matters |
| **ComfoFeet** | "Swollen feet \| Solution" symptom split (B18). Quote headline "Ok I did it. I bought the $39 orthopedic shoe" (B20). "1 sold every 5 seconds" | 340–360 days | Symptom→solution split, quote-as-headline |
| **Orthora** | "Built for hard concrete floors" checklist incl. "cushioning that doesn't collapse mid-shift" (B38). "For her. By workers who get it." "92% of shift workers…" stat badge | 160–170 days | Concrete-floor framing for retail (C13) |
| **KURU** | "They're not cheap. It's true." 1★ reversal (B49). "KURU knows feet. Other shoes… not so much." "Are your heels in hell?" | 180–409 days | Price-objection reversal (C19) |
| **Clove** | "Healthcare's not new. The right shoe for it is." "#1 Shoe for Doctors + Nurses." Back-to-nursing-school locker shot | 50–100 days | Premium nurse identity; seasonal nursing-school moment |
| **WearStand (STAND+)** | Letter-style "You'll forget us" copy. "New life for kitchen days" chef quote. "Use your FSA/HSA" | 110–170 days | Occupation quotes (chef/kitchen), FSA framing |
| **Vessi** | "Float over cobblestones" checklist on a real street. "No more backup shoes. One pair. Door to desk." | 70–100 days | Real-scene travel (C16) |
| **Orthofeet** | Lifestyle + "Built-in orthotic insoles" callout, exploded feature diagrams | 70–165 days | "No insoles needed" message (C17/C19) |
| **HIKE** | BOGO clearance, "14 days to relieve plantar fasciitis" icon grid | ~390 days | Offer-led retargeting only |
| Non-footwear | Treatmedy "Fix bunions without surgery" (794 days). Everstride "Diabetic women are replacing their tight socks with these" (761 days). OrthoFit "1 in 3 women over 50 have a bunion" (B121). Nimbao "Hammer toes don't disqualify you from cute shoes." Lumbowrap Facebook-comment screenshot over a person (607 days). Nuvra "Day 0 / Day 7 / Day 14" | months to years | Bunion framing (C14), "women are replacing X with these", comment-over-photo (C04) |

**Nurse Babes and Snibbs** returned no image ads in Atria's library, and Atria only surfaced unrelated brands for WearStand's lookalikes.

> **Your second page:** "ComfortOrtho Shoes" (yours) has run the "Dear Nurses", "Last chance for pain-free walking" and "$59.95 12-hour shift shoes" statics for **235 days** (B91–B93). That is more evidence these templates are durable. Separately, "Foot Health Daily / Hike Balance" runs a "Dear Hikers, tackle every trail pain-free" copy of the same template (B108) plus "Best shoes for NURSES", so competitors are copying your format.

## 8. Concepts (`concepts.json`)

The first 12 come from your $5k+ winners; C13–C19 add the Notion angles and brand inspiration:

| ID | Concept | Built from |
|---|---|---|
| C01 | Dear Nurses v2 (navy, review-language callouts) | #1 efficient winner (4.34 ROAS) |
| C02 | 12-HOUR SHIFT SHOES checklist on a hospital photo | $858k winner + I3 |
| C03 | Running shoes / $300 orthotics / insoles struck out → SOLUTION | $90k winner + scripts |
| C04 | "Didn't buy yet? Read what nurses are saying" (Trustpilot) | 3.05 ROAS retargeting winner |
| C05 | The 4 stages of a 12-hour shift | I14/I66 stage format + scripts |
| C06 | Do you have "shift feet"? checklist | I59 + reviews |
| C07 | Why your heels hurt at hour 8 (anatomy split) | PF anatomy winners + I70 |
| C08 | "They wanted $300 for orthotics. I spent $59.95." | 203 UGC script (3.05 ROAS) |
| C09 | Spills happen. Slips don't. (sole macro on wet floor) | Slip-resistant callout + I5 |
| C10 | First it was me. Then 3 more nurses on my floor. | 203 UGC script + reviews |
| C11 | Hour 12. Still smiling. | I25 identity format |
| C12 | WARNING: Last restock (only with a real deadline) | Warehouse winner (3.31 ROAS) |
| C13 | "You don't walk miles. You stand on concrete for 8 hours." (retail) | Winner callout layout + Orthora + databank cashiers |
| C14 | 1 in 3 women over 50 has a bunion | OrthoFit + Nimbao + winner toe-box callout |
| C15 | Her hands don't work in the morning (arthritis, no-tie laces) | Databank + Malvay/Nuvra |
| C16 | We tested 4 shoes on cobblestones (scorecard) | Kyro 293/369 travel videos + Vessi |
| C17 | Your foam gives up at hour 4 | Stepprs split + databank + scripts |
| C18 | "12-hour shifts did this" written on the heel | Stepprs (386 days) + Neurotoned |
| C19 | Receipt: what your feet cost this year | Databank cost math + 203 UGC + KURU |

**Testing plan:**
1. **Core (nurses, highest confidence):** C01, C02, C03, C05, C07, C17 in prospecting. These are direct descendants of the $5k+ statics.
2. **Retargeting:** C04, C08, C12, C19.
3. **Audience expansion (one static per audience, kept in the winning layout):** C13 retail, C14 bunions, C15 arthritis, C16 travel. Given the losers, judge these against their own audience benchmarks, not the nurse winners.
4. **Format swings:** C06, C09, C10, C11, C18.

---

## 9. Negative-rating survey (1–3★ customers), added 2026-10-10

Source: "ComfortWear Customer Feedback (Responses)" Google Sheet, **18,406 responses, Apr 2023 – Oct 2026**, from customers who gave a 1–3 rating. The raw sheet holds emails and order numbers, so only these aggregates are kept in the repo.

> **Read this as "who ends up unhappy, and why", not "who buys".** Only negative raters see the survey, so job and age mixes are skewed toward the people the shoe or the experience failed.

**1. Sizing is the #1 product problem, and the shoe is fine when it fits.**
60% got the wrong size (33% too small, 27% too big; nurses are about the same at 59%). Average comfort among these unhappy customers is **2.98/5 when the fit was right vs 1.71 when it was too small** and 2.13 when too big. Since the miss goes both ways, "size up" isn't the fix. The fix is a better way to choose. Quotes: *"don't offer a half size option if it is the same as the whole size"*, *"your guide don't give the right sizes"*, *"I should have ordered a 1/2 size larger, when I walk my toes hit the tip"*.

**2. The free-text complaints are mostly operational.**
Of 2,666 written answers: refunds/returns 25%, size/fit 24%, shipping/delivery 19%, cheap quality 11%, no arch support 11%, "not really orthopedic / misleading" 7%. This matches the Trustpilot 1★ pattern. **Ads must not promise fast shipping, easy returns or a money-back guarantee**, and claims like "orthopedic" or "podiatrist-approved" invite *"Be truthful about how they're orthopedic approved"*.

**3. Who they are.**
Age: 47% are 65+ and 38% are 50–65. Job: retired 27%, nurse/healthcare 18%, retail/cashier 8%, food service 6%, teachers 4%. Foot problem: plantar fasciitis 25%, **"no foot pain, only need comfort" 22%**, arthritis 11%, neuropathy 10%, bunions 7%. Where they found us: Facebook 63%, Google 17%.

**4. What they already use.**
11% are on insoles, inserts or orthotics, 6% stretch/ice/massage, 4% painkillers, and 2–3% each wear Skechers or Hoka. 71% say "comfort" is what they shop for, 20% "support", 12% fit or width.

**5. Arch complaints are specific:** *"the heel had more support than the arch, kept pushing my foot forward"*, *"made me walk on the balls of my feet"*. The rocker sole surprises some buyers, so it's worth setting expectations ("rocker sole: feels different for the first day").

### New concepts from the survey

| ID | Concept | Built from |
|---|---|---|
| C20 | "Between sizes? Measure, don't guess." 3-step fit finder | #1: 60% wrong size, comfort 2.98 vs 1.71 |
| C21 | "Still moving your insoles from shoe to shoe?" | #4: 11% on insoles/orthotics |
| C22 | "You don't need a diagnosis to want comfortable feet." | #3: 22% "no pain, only comfort" |
| C23 | "Retired from 12-hour shifts. Not from walking." | #3: 85% are 50+, 27% retired (test against the seniors-loser finding in §2) |

**Ops note for whoever owns CX:** fixing the size guide (a cm/inch chart by foot length, a clear call on half sizes) is probably worth more than any ad. Every wrong-size order is a likely 1–2★.

---

## 10. Spanish-language ads, added 2026-10-10

Spanish has a track record in the pulled data (a live Atria re-pull wasn't possible this session):

| Ad | Format | Spend | ROAS |
|---|---|---|---|
| "@NF - V2_Hook1_063_Spanish_OrthoStretch_5_FootPainCure", nurse script *"Mi doctor me dijo que no había cura para mi dolor de pies… Soy enfermera"* | Video | C$47,989 | 1.53 |
| "Spanish Nurse image V5", headline *"Los zapatos de enfermera favoritos de 2024"* | Static | C$22,149 | 1.79 |
| "spanish mage V5" (same creative, second ad set) | Static | C$11,439 | **2.14** |
| One Spanish static in the losers list | Static | C$112 | n/a |

The two Spanish statics sit at or above the median ROAS of the $5k+ winners (1.71), and there's a
Spanish landing page (`comfortorthowear.com/es`). The existing Spanish copy reads like a translation
from Spain ("Consigue el tuyo", "120.000 reseñas"). The new concepts are written natively for US Latinos instead:
`tú`, "los pies me mataban", "parado todo el día", "doble turno", "comadre", "porfa", family and
coworker framing, and US number formats.

## 11. Personas, added 2026-10-10

Built from the 1–3★ survey (job, age, problem, current fix), the winning-ad history, forum research
and category knowledge. Reddit itself couldn't be read from the cloud environment (fetch blocked,
search returned no threads), so the forum input came from r/Serverlife via a mirror and Mayo
Clinic Connect. Colorway rules per persona live in `brand.json`.

| Persona | Evidence | Colors |
|---|---|---|
| Hospital nurse, 12-hr shifts | Top historical winners; survey nurses: PF 27%, "just comfort" 26% | black/purple, all black, black/white, navy ("WhiteBlue") |
| CNA / home health aide / caregiver | Survey n=380, 30% "just comfort"; lifting, low pay so price matters | same as nurse |
| Server / line cook / bartender | Survey n=1,055, mostly under 50; r/Serverlife: "cheap shoes will kill your ankles, knees & back", Hoka Bondi SR praised but "very pricey" | all black, black/white, black/purple, navy |
| Cashier / retail / warehouse on concrete | Survey n=1,377, PF 27–33% | all black, navy, black/mint, black/white, light grey |
| Housekeeping / janitorial | Survey n=375, **highest PF share (35%)**; strong Spanish-speaking overlap | all black, black/purple, navy, black/mint |
| Teacher / para | Survey n=775, PF 29%; forums: shoes are "comfortable or cute, hardly ever both" | navy, burgundy, all black, black/purple; test purple, grey/pink, black/mint |
| Hairstylist / salon | Survey n=152, "on my feet all day", PF 31% | black/mint, purple, grey/pink, black/white |
| Active retiree 65+ | Largest job group (27%), 47% of respondents 65+ | light grey, grey/pink, purple, navy, burgundy |
| Balance / swelling / neuropathy (older) | Neuropathy 10%; Mayo Clinic Connect: slip-ons that "accommodate daily foot swelling", grip, side support | light grey, navy, grey/pink |
| Adult child buying for a parent | Category knowledge (gifting); core wearer is 65+ | grey/pink, light grey, purple |
| Traveler (theme parks, Europe) | Travel videos 2.15 ROAS; team "Paris/Barcelona" statics | black/white, navy, burgundy, black/mint |
| New walker / weight loss (incl. GLP-1) | Winner "I lost 50lbs+ walking 20,000 steps" ($93k); team GLP-1 statics | purple, black/mint, grey/pink, navy |
| Comfort only, no diagnosis | 22% "no foot pain, only need comfort" | any |

## 12. Rising winners (iteration rule), added 2026-10-11

Rule: any ad launched in the last 30 days with **≥ $300 spend and ROAS ≥ 1.8** gets static iterations of
its concept and angle in the next weekly batch (`atria_pull.py rising`). ROAS is readable again for
recent ads (the near-zero ROAS affects the 2025 history), so spend stays the reference for older ads.

First pull (Sep 11 – Oct 10, 2026), all videos, all prospecting:

| Ad | Angle | Spend | ROAS |
|---|---|---|---|
| COM225 Kyro390, Spanish version | "Los zapatos de enfermería favoritos de 2026", 73% of healthcare staff have foot pain | $1,047 | 2.57 |
| COM211 travel | "2026's Favorite Shoes For Traveling", 50,000+ steps, long flights | $967 | 2.50 |
| Com255 | "2026's Best Shoes For Weight Loss", vicious cycle of foot pain vs. walking more | $417 | 2.18 |
| Senior page, side by side | "Podiatrist Rates Safest Shoes for Seniors": stability, slip-resistance, no laces | $477 | 1.89 |
| COM174 Kyro362 teacher mash-up | "2026's Favorite Shoes For Teachers": 5 shoes compared over 480+ hours of classroom wear | $2,157 | 1.83 |

The "2026's Favorite/Best Shoes For <audience>" headline format appears in 4 of 5. Some source copy uses
claims we avoid ("recommended by podiatrists", "free returns"); iterations keep the angle but drop those.
