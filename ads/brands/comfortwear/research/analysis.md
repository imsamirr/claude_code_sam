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
Of 2,666 written answers: refunds/returns 25%, size/fit 24%, shipping/delivery 19%, cheap quality 11%, no arch support 11%, "not really orthopedic / misleading" 7%. This matches the Trustpilot 1★ pattern. **Ads must not promise fast shipping or easy returns** (update 2026-10-13: the user approved the offer stack "40% OFF + 30-DAY MONEY-BACK GUARANTEE + FREE SHIPPING", so those exact words are allowed), and claims like "orthopedic" or "podiatrist-approved" invite *"Be truthful about how they're orthopedic approved"*.

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


## 12. Creative-director feedback, 2026-10-13 (applied to brand.json, generate.py and the routine)

1. **Shoes looked compressed.** Cause: `generate.py` stretched the API image when its aspect ratio differed from the target. It now center-crops instead, and a prompt rule forbids squashed or shortened shoes.
2. **9:16s had cut or blurred tops and bottoms.** Cause: the 9:16 was a 4:5 ad with outpainted background. Now the 9:16 is composed for its full height and the 4:5 is re-laid out from it (`--layout native`).
3. **Too much purple text.** Cause: the palette asked for purple headlines. Text is now black, navy or white; purple is a small, occasional accent.
4. **Colors:** test all colors, weighted to the best sellers (in order): Black/Purple, All Black, White Blue, Black/White, Red, Turquoise/Black, about 80/20 (`colorway_priority`).
5. **Offer creatives:** ~30% of each batch shows "40% OFF + 30-DAY MONEY-BACK GUARANTEE + FREE SHIPPING".
6. **Angles:** nurses, travel, teachers, plus-size (mix and match), and ≥40% of each batch leads with a foot-pain problem from the survey and reviews.

## 13. Quality benchmarks, 2026-10-13 (`reference/benchmarks/`, keys in brand.json → `benchmarks`)

18 images: 10 the creative director picked as the quality bar, plus 8 top $5k+ winners pulled from Atria. Performance from Atria (WearOrtho, monthly top-50 windows since Jan 2024) where the ad name could be matched:

| Benchmark | Proven by |
|---|---|
| Dear Nurses callouts (`callouts_white`) | $208k at 2.92 ROAS, $27 CPA, plus a $22k ad set at 17.8 ROAS: the most efficient big static |
| Didn't buy yet comments (`comments_offer`, `comments_social`) | $50k at 3.05 ROAS, still active (RTGv1_C3) |
| Almost sold out (`lifestyle_urgency`) | $8.7k at 3.97 ROAS, $25 CPA |
| 12-hour shift list (`list_white`) | $858k across 8 ads |
| Shoes for 12-hour shifts diagram (`diagram_grey`) | $457k |
| Warning warehouse (`warehouse_urgency`) | $19k at 3.31 ROAS |
| HSA/FSA, Brooks split, Morton's, Built for 12h, teachers.org, Ditch the Hokas, PF anatomy | recent/creative-director picks (newer names don't match the older ad naming; spend not attributed) |

**What every benchmark shares (the bar):**
1. **The shoe is real studio-grade product photography**: crisp knit, exact colorway, true proportions, usually 40–60% of the frame. When a person appears it's only legs/feet, and the shoe still dominates.
2. **One message, read in 1 second**: a big headline (often 2 lines with a weight or color change on the key words), then at most one supporting line.
3. **Structure from solid shapes**: solid headline bars (Brooks, Morton's), solid pills with check icons (Built for 12h), a solid offer block or circle (Ditch the Hokas, 40% OFF circle), thin hand-drawn arrows (Dear Nurses). No translucent overlays.
4. **Backgrounds are plain or quiet**: white, soft grey, soft gradient (HSA), or a real room or street softly out of focus.
5. **Proof devices are native and specific**: real-looking Facebook comments with names and reactions; competitor named in the headline with X vs check rows; condition named in the headline with a small pain inset.
6. **Offer elements are compact**: a circle, ribbon, block or single line ("40% OFF", "Try risk-free"), never the whole canvas.
7. **Two text colors max**: black/white plus one accent (brand purple, royal blue or red) as a solid fill or for the key words of the headline.

## 14. Single-size 4:5, higher quality, 2026-10-18

User rule: ship one size only, 4:5, rendered once at high quality (`generate.py --layout feed`, default quality `high`). No 9:16. Measured cost ≈ $0.22 per ad (3-ad test), vs ≈ $0.13 for the old medium 9:16 + 4:5 pair. Sheets (`review.py csv`) now have one "Image (4:5)" column.

## 15. One 4:5 file and trend-first research, 2026-10-23

1. **One file per ad:** 4:5 only (`--layout feed`, the default). No 9:16, no duplicate sizes. (The 2026-W44-fri batch was rendered with native 9:16 + 4:5 per an older routine prompt; the `_v1.png` 9:16 files there are unused.)
2. **Trending static formats:** every run, mine Atria for the newest static formats (inspo + competitors, newest and fastest-rising first), contact-sheet them, and list 'formats trending now' here with who runs them, days running and what to borrow. Net-new batches use at least 5 of them.

### Formats trending now (Atria inspo pull 2026-10-24, statics ≤3 days old)

Shoe-in-the-trash lo-fi UGC (hand + old shoe in a bin) · "Would You Rather? A vs B" poll · "Hour One / Hour Six / Hour Twelve" 3-band stack (foam collapse, Stand+/Flexitec) · struck-through quote "Foot pain is just part of the job. It doesn't have to be." (STAND+) · story-text testimonial on a solid color/confetti card · Problem vs Answer two-column table (neuropathy) · Ice packs vs X split with X/check rows · woman pointing at shoe + "10 reasons" advertorial (Wide Comfort Shoes) · lo-fi real-life photos (break room, car after shift, worn insoles on a table) · BOGO full-bleed color block · customer-quotes bullet list ("We keep hearing the same thing…"). Carol Bennett story-post statics ("not wearing real orthopedic shoes", "$4,200 trip") jumped +50 ranks in 7 days.

## 16. Two-week focus and Black Friday week, 2026-10-26

- **Oct 26 – Nov 8 runs:** nurse and travel (Disney, Europe) only; analyze previous winners first; each concept gets a Spanish twin (`_es` id, `twin_of`).
- **Week of Nov 9:** Black Friday concepts. One offer per concept: "60% OFF SITEWIDE" OR "BUY 2 PAIRS, GET 2 FREE GIFTS" (3-pack cushioned socks + free travel bag). The 40% / 30-day / free-shipping stack is not used that week.
- Full rules: `brand.json` → `program.focus_2026_10_26`, `program.black_friday_week_2026_11_09`.

### Formats trending now (Atria inspo pull 2026-10-27) and Tue 2026-W44 sources

Newest/fastest-rising statics and story ads: Carol Bennett story posts (+240 ranks in 7 days, "F*ck this comfort sneaker", podiatrist-style senior sneaker), Glov Beauty "It's fluid, not fat" swelling explainer (11 days), Stepprs "Walk on Clouds, or it's FREE" insole quote cards, Cuurt customer-quote checklist ("Wake up pain-free, not hobbling down stairs"), VIVAIA "10,000 steps and beyond" minimal lifestyle, Buy-1-Get-1 color blocks (Konjoun, True Nutra, Tiny Explorings), 8-week timeline/plan lists. Used in T44: three-band hour timeline, swelling explainer (flight), customer-quote native cards.

Tue 2026-W44 iteration sources (`current` 2026-09-27..10-26, 18 ads; `seasonal --week 2026-W44`, 2025 ROAS unreadable): Emily RN video $4,005 / 2.99 and Kyro390 $4,841 / 2.01 (nurse PF), H3 40% OFF static $2,517 / 3.08, C3 reviews static $1,844 / 2.84, I6 warehouse $1,160 / 4.24, C1 Trusted By Nurses $860 / 3.40, TOFV1_KW1 plus-size travel $2,243 / 4.39, Kyro293 travel $2,230 / 3.09, JV1/JW1 travel $1,897 / $784, seasonal Kyro253 travel $32.6k.

## 17. New rules and wellness inspiration, 2026-10-28

User rules: English only; angles = nurse (~35%), travel incl. Disney (~25%), plus-size mash-ups (~20%), test slot for new pains (~20%); plantar fasciitis then bunions lead the pains; teacher paused (re-enable only on an Atria `current` winner); Poppins for all text; realistic, not AI; headline on the image, not in a band; direct-response copy; offer = 40% OFF + FREE SHIPPING + 30-DAY MONEY-BACK GUARANTEE, HSA/FSA ELIGIBLE up to 30% savings. Inspiration comes from ALL health & wellness brands (`atria_pull.py wellness`), and every run must bring formats not yet in `format_ledger.json`. Full rules: `brand.json` → `program.focus_2026_10_28`, `wellness`.

### Patterns in our $10k+ statics (winning_statics.csv)
Nurse is the whole top: "2024's Favorite Nurse Shoes" images at $858k / $457k / $230k / $120k / $90k, "2023's Best Shoes For Nurses" $198k, then offer statics ("Save Up To 40% OFF" $152k / $125k / $115k, "Walk Pain-Free or Money Back" $93k, "500,000+ Happy Customers" $50k, "40% OFF TODAY + FREE Shipping" $33k, "48 HOURS LEFT" $19k). Shared: white or very light ground, one big shoe, the occupation or condition named in a heavy geometric sans (Poppins/Montserrat), 3-6 body-part benefits as arrows, checks or plus-bullets, offer as one line or a compact seal.

### Formats found 2026-10-28 (45 days, image, active, 10+ days running; read 48)
| Format | Brand (category, days) | Why it works | Our version (tested in weeks/2026-W44-wellness-inspo) |
|---|---|---|---|
| Blame-shift + 3 reasons + guarantee | Osteva (joint supplement, 11d) | Takes the blame off her and names a cause | "It's not your age. It's your shoes." |
| 4-stage ladder of failed fixes | Linda Baker (edema mineral, 33-38d) | Walks her own failed attempts in order | "4 stages of nurse heel pain" |
| Symptom checklist + wooden mannequin | Osteva (knee sleeve, 15d) | Self-diagnosis quiz, crafted not AI look | "5 signs it's plantar fasciitis" |
| Thermal heat-map + money-back headline | Hollow Socks (socks, 21d) | Makes invisible pain visible; risk reversal | "Comfortable 12-hour shifts, or your money back" |
| What-to-expect timeline, product in hand | The Outgoing Co (supplement, 42d) | Sets honest expectations | "What to expect at Disney" |
| We-tested counter photo + sticky note | Lumexa (supplement, 27d) | Static version of our "we tested 5" videos | "We tested the top 4 nurse shoes." |
| Not yet used: Week 1/2/3 progression + seal (Lymphoria, 42d), apology founder letter (RYZE, Tiny Explorings), shock headline + customer results (Rhea, 28d), persona-page off-topic real photo + story (Linda Baker etc.), X-ray on lightbox (Melissa Hayes), mirror-selfie progression (50 Plus and Fabulous), age-bracket program grid (Muscle Booster). |


## 18. Feedback sheet mined, 2026-10-28

Full results: `feedback_pain_points_2026-10-28.md`. 18,452 answers (22% are 4–5★, so §9's 'only 1–3★' note is outdated). Plantar fasciitis 27% (down from 34.5% in 2023–24), 'no pain, just comfort' 22% and rising to 32% in 2026, arthritis 12%, tired feet 12%, neuropathy 11%, bunions 9%, wide feet rising to 4.4%. Insoles/orthotics are the #1 thing they tried (13%). Guardrails: sizing (only 40% good fit), don't overclaim the toe box, explain the rocker sole, guarantee is 30 days.


### Formats found this run, 2026-10-28 (net-new batch 2026-W45-fri; wellness pull, 367 kept, read the top 160)
| Format | Inspiration (category, days running) | Our concept |
|---|---|---|
| night_clock_photo | Vitality Extracts (sleep spray, 32d) + Budpop (sleep, 20d) | W45_01 5:12 AM. The first step hurts most. |
| two_beat_nurse_corridor_photo | WELLX 'Night shift. Morning legs.' (compression, 15d) | W45_02 Night shift. Morning feet. |
| timestamp_result_list | NorthAlpine 'Put it on at 8am. By 8 | W45_03 Put them on at 7 AM. At 7 PM: |
| reddit_thread | Señorita Drinks r/AlcoholFree thread (27d) | W45_04 What shoes survive 3 12s in a row? |
| group_photo_peer_proof | Maggie's Tanks / Dr. Margaret Foster (apparel, 33d) | W45_05 Half our unit wears them now. |
| trash_can_toss | Adam Herman (supplement, 21d) | W45_06 Done moving insoles from shoe to shoe. |
| struck_phrase_headline | NeuroMD 'Your back needs another failed solution' (TENS, 24d) | W45_07 Your feet don't need bigger shoes. They need room. |
| pain_glow_feet_checklist | OrthoFit Store 'Senior Womans Comfort Sneaker that may target' (footwear, 24d) | W45_08 Over 60? Which one is you? |
| quote_condition_checklist | Sweet Home Australia '"My only Nurse shoes that lasted 14hrs."' (footwear, 41-42d) | W45_09 "No back or feet pain after a 13-hour shift." |
| quote_feature_branches | FineRoot Organics 'I haven't felt this good in years' (turmeric, 31d) | W45_10 "My first Disney trip where my feet kept up." |
| mirror_selfie_triptych | 50 Plus and Fabulous (collagen, 31d) | W45_11 3 park days. Same shoes. |
| landmark_snapshot_caption | Natalie Brooks / persona pages (19-23d) | W45_12 Lisbon, day 4. My heels? Fine. |
| fridge_note_photo | Rosabella Beetroot (supplement, 19d) | W45_13 Disney packing list, item #1. |
| conditional_guarantee_headline | Grünanda 'If your balance doesn't improve after 2 walks, we'll buy your boots back' (footwear, 44d) | W45_14 Heels still sore after your trip? Send them back. |
| hand_held_price_drop | Aurivita (supplement, 12d) | W45_15 $90 $59.95: built for long days on your feet. |
| ms_paint_window | Manna Vitality '71% OFF' (supplement, 29d) | W45_16 40% OFF the nurse shoe. |
| color_swatch_row | Cosy House Collection 'Goodbye night sweats' (bedding, 18d) | W45_17 Room for your toes. In 9 colors. |
| sticker_speech_bubbles_photo | Dr. Woof Apparel 'Bye-Bye, Varicose Veins! / Hello, Healthy Legs' (socks, 35d) | W45_18 Bye-bye, squeezed toes. |
| tilted_sticker_headline | Diabetic Sock Club 'SOCK MARKS? GONE FOR GOOD.' (socks, 13d) | W45_19 Swollen by 3 PM? Stretch to fit. |
| writing_on_skin | Natural Wellness Journal (fascia supplement, 14d) | W45_20 9 miles in Rome. Heels didn't hurt. |
| sketch_symptom_quadrant | Purvival (detox, 42d) | W45_21 Heel pain? Squeezed toes? Swollen feet? |
| engraved_anatomy_etching | Yoga International 'Anatomy Trains' (course, 29d) | W45_22 Why your heel hurts most in the morning. |
| vintage_engraving_scene | Tiffany Mccomb 'The dangerous mistake in barefoot shoes?' (footwear, 39d) | W45_23 The shoe mistake most nurses make. |
| three_moment_line_icons | Balmbare 'Stiff joints? Try it risk-free' (collagen, 31d) | W45_24 Heel pain? Try them risk-free. |
| advertorial_listicle_cover | Secrets of Herbs 'The 6 Best Ways to Drain Lymph Fluid Naturally' (lymph, 29d) | W45_25 5 things nurses with plantar fasciitis wish they knew. |
| two_column_spec_list | Everlab 'Is your current health check telling you anything?' (health test, 38d) | W45_26 Built for a 5K, or a 12-hour shift? |
| number_claim_minimal | Kintoe '100 MILES. NO BLISTERS.' (socks, 42d) | W45_27 22,000 steps. One pair. |
| yes_this_is_statement | Fresh Reveal 'YES, THIS IS A COVER. IT COMES IN FIVE COLORS.' (home, 29d) | W45_28 Yes, these are comfort shoes. They come in 9 colors. |
| unboxing_handwritten_card | Mystery Shirt in a Box (apparel, 26d) | W45_29 "For your 12s. Thank me at hour 10." |
| body_part_pill_lifestyle | Pain Relief Australia 'YOUR NECK DESERVES A MASSAGE' (massager, 14d) | W45_30 Your heels deserve a better 12 hours. |
| minimal_two_word_benefit | Outback 'Opens fully.' (bag, 10d) | W45_31 No laces. No bending. |
| age_bracket_grid | Tkofitlife / Muscle Booster '28-Day Chair Tai Chi at my age' (knee sleeve, 11-18d) | W45_32 What your feet need at 50, 60 and 70. |

Patterns shared by the inspiration ads: real phone photos of ordinary objects or people (clock, fridge, trash can, group photo), a single surprising statement or a question as the headline, a timestamp or number, sticker/tilted text blocks over a real photo, and illustration styles (pencil sketch, engraving) for mechanism ads. Our $10k+ statics share: white ground, one big shoe, occupation or condition named, 3-6 body-part benefits, small offer line. Each W45 concept pairs one inspiration format with one winner or script.

## 15. Trending statics deep dive (2026-10-30, Atria MCP)

Searches: image, active, launched since Sep 1, running 7+ days, impression trend rising / rank climbing over 14 days, queries foot pain shoes, nurse shoes 12-hour shift, walking shoes travel, shoes + themes (before/after, us vs them, post-it, negative marketing, testimonial, statistics, comparison). Read 25 creatives.
What is rising right now in footwear/foot pain (and why it beats our plain layouts):
| Format | Advertiser (signal) | Device |
|---|---|---|
| "Dear Chefs, work doubles pain free" + strike-through feature list | Armadilo (+52 places in 7d) | named audience letter + ~~problem~~ → benefit pairs |
| "Dear Chefs, your clogs weigh a ton. These don't." | Armadilo (+45 in 14d) | insult the current shoe, 4 hand arrows, price bar |
| Week 0 / 4 / 9 alignment panels, "gone or your money back" | Footstr (+19 in 14d) | red→green line on legs, progress over time |
| iPad photo of side-by-side feet + sticky note "How I fixed…" | Footstr | real-life proof photo, handwritten story |
| Big banner + time-step pills (5 min / 15 min / 5 days / 2 weeks) | Foot Health Club | outcome timeline |
| "In 2026 I felt every rock… first time in 20 years" | Konjoun | first-time-in-years + illustrated cross-sections |
| "ANTI-GRANDPA WALKING SHOES" | OrthoFit | identity negation, plus list |
| "You didn't outgrow your shoes. Your feet swelled." | Senior Health Guide (+101 in 14d) | real phone before/after feet |
| "DON'T BUY BAREFOOT SHOES" engraving | Tiffany Mccomb (+30 in 14d) | negative marketing, vintage illustration |
| Colorway collage + "This offer won't last forever" | Musabela (+39 in 14d) | lifestyle grid + urgency |
| Shoes fanned in a circle, "Stabbing heel pain? There's a fix" | Bright Footwear | product burst + question headline |
| Candid nurse at the nurses' station | Kirsty Phillips advertorial | real scene, no text |
Takeaway: winners pair a NAMED audience or a sharp insult/negation with visible proof (lines, before/after, timeline) and real-life photography; plain "shoe + labels" layouts are not in the rising set.
