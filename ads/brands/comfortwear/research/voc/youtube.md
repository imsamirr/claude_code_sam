# YouTube VoC: comfort, plantar-fasciitis, travel and wide-foot shoe videos

Pulled 2026-11-18 with StefanBrain `scrape_social_comments` (the cap is about 500 comments per call, so the larger videos got 100 comments each). Video discovery used `web_search`.
- Raw data: `voc/raw/yt_*.csv` (1,487 unique comments, 1,109 of them non-creator; reading file `voc/raw/yt_read.txt`).
- **How I read**: I read in full up to the 55 most-liked substantive comments per video (797 comments). I then keyword-scanned all 1,109 non-creator comments for personas (nurse/shift, plus-size, senior, neuropathy/swelling, Disney/travel) and objections (price, scam, returns, slip-on).
- **Not found**: no YouTube video about Comfort Wear / comfortorthowear.com, or about "orthopedic shoes from Facebook ads", turned up in search. Stepprs results were blog posts, not videos. Facebook-ad comfort-shoe sentiment below comes from the Hike videos and from mentions in other videos.

---

## 1. Videos read

| # | Video | Channel type | URL | Scraped / read |
|---|---|---|---|---|
| 1 | The TRUTH about the BEST shoes for plantar fasciitis | MD (sports medicine) | https://www.youtube.com/watch?v=MW0tAUIAr4Q | 100 / 55 |
| 2 | Best and WORST shoes for plantar fasciitis – 4 things to AVOID | Same MD | https://www.youtube.com/watch?v=rfotyiQkz9M | 100 / 55 |
| 3 | Best & Worst Shoes for Plantar Fasciitis – Walking, Standing, Running | Foot specialist / shoe reviewer | https://www.youtube.com/watch?v=pSlno1IXMSA | 87 / 55 |
| 4 | Best Walking Shoes 2026 by a Foot Specialist | Foot specialist | https://www.youtube.com/watch?v=1v17GoOoo0k | 100 / 55 |
| 5 | Why Superfoam Shoes Are Wrecking Your Knees – Kuru Atom 2 | Shoe/gear review channel | https://www.youtube.com/watch?v=HYdJ20jXgME | 100 / 55 |
| 6 | KURU Footwear Review – Must-haves for Arthritis | Physical therapist (arthritis) | https://www.youtube.com/watch?v=OFLrYkKCi2A | 44 / 29 |
| 7 | Hoka Clifton 10 vs Bondi 9 – Which to Choose? | Running-shoe review channel | https://www.youtube.com/watch?v=q6_zwDLH43I | 54 / 34 |
| 8 | HOKA Bondi 9 vs Clifton 10 | Shoe reviewer | https://www.youtube.com/watch?v=ST2QyDeUzV0 | 23 / 14 |
| 9 | Best Shoes for Healthcare Workers: Hoka Bondi & Gaviota | Healthcare-worker creator | https://www.youtube.com/watch?v=DOd45C3C028 | 25 / 10 |
| 10 | Best Skechers for Plantar Fasciitis by a Foot Specialist | Foot specialist | https://www.youtube.com/watch?v=cce6oZWiAOc | 53 / 32 |
| 11 | Best Skechers for Seniors? Arch Fit 2.0 Full Review | Foot specialist | https://www.youtube.com/watch?v=eIyMJmrP9PE | 50 / 31 |
| 12 | Skechers Arch Fit Review by a Podiatrist | Podiatrist | https://www.youtube.com/watch?v=dw_6c_ZSUos | 19 / 14 |
| 13 | 21 Stylish Shoes for 20,000 Steps on European Cobblestones | Women's travel creator (50+ audience) | https://www.youtube.com/watch?v=FypZvM7jtmI | 100 / 55 |
| 14 | Europe Travel Shoes (supportive) | Same travel creator | https://www.youtube.com/watch?v=nPlRcVdWGR8 | 100 / 55 |
| 15 | 11 Supportive Shoes for Travel | Same travel creator | https://www.youtube.com/watch?v=Ozsh8fM7naQ | 69 / 36 |
| 16 | Best Wide Shoes for Walking & Running | Foot specialist | https://www.youtube.com/watch?v=WYLQMxhA88Q | 68 / 35 |
| 17 | 15 Shoe Brands for Big Feet & Wide Feet, up to Size 14 | Women's fashion creator (big/wide feet) | https://www.youtube.com/watch?v=Hwq5KOztjN8 | 55 / 39 |
| 18 | Hike and Peak Barefoot Shoe Haul and Review | Older-woman lifestyle vlogger | https://www.youtube.com/watch?v=rAIIVFW7A0E | 80 / 41 |
| 19 | Best Shoes for Disney World and Disneyland – Top 4 | Theme-park creator | https://www.youtube.com/watch?v=YUHnylWKtvQ | 20 / 8 |
| 20 | Did I Just Find the BEST Shoe for Theme Parks? | Theme-park creator | https://www.youtube.com/watch?v=4wi5GLQhfGg | 16 / 8 |

Smaller videos (all comments read):
- [Kuru Apogee plantar-fasciitis features](https://www.youtube.com/watch?v=1R2YgBrkyGw) (podiatrist, 20)
- [Best walking shoes for city streets](https://www.youtube.com/watch?v=w2tGzYGhgZY) (podiatrist, 20)
- [Heel pain / fat pad shoes](https://www.youtube.com/watch?v=UEwnT625bGY) (19)
- [HOKA vs Brooks vs New Balance](https://www.youtube.com/watch?v=TekVuVDwtvk) (10)
- [Hands-free slip-in sneakers](https://www.youtube.com/watch?v=TTvHGuH6i4c) (9)
- [12 walking shoe brands robbing you](https://www.youtube.com/watch?v=KdStNAQKzd0) (8)
- Orthofeet [Yari](https://www.youtube.com/watch?v=ZMqUnqFuNF4) (7) and [Venice](https://www.youtube.com/watch?v=_cHjkZQsui8) (6)
- Hike [sizing](https://www.youtube.com/watch?v=Ay8E1z_yVMI) (7) and [legit?](https://www.youtube.com/watch?v=pHzHfgV2TvI) (5)
- [Women's walking and standing shoes 2026](https://www.youtube.com/watch?v=u0zwRs3RikQ) (5)
- [Top 4 PF shoes](https://www.youtube.com/watch?v=h3h2xfdnmE8) (100 scraped, mostly creator replies; 5 substantive)

---

## 2. Objections and hesitations (ranked by how often they came up)

1. **"Every expert says something different."** Buyers are confused by max cushion vs zero-drop/barefoot vs arch support. "So confusing as to what to do. Every 'expert' says different things." This creates an opening for a simple, confident message.
2. **Too much squishy foam makes it worse or unstable**, especially for seniors (51 cushion/stability mentions). The top comment on the walking-shoe video (52 likes) warns that high-stack squishy shoes are "inherently unstable especially for senior citizens where a fall c[ould]…". Others write "Walking on marshmallows killed my feet, ankles, and knees" and "Them cushy shoes make my feet hurt worse." Buyers want **cushion + stability** at the same time.
3. **Price.** Topo/Altra at $150+, Kuru at $170-200, Orthofeet "pricey": "Who has the kind of money to buy phase 1 then Phase 2 and the Phase 3 shoes." "These are all very expensive… what are the mid budget options £40 to £80?" A **~$60 price is a real lever**.
4. **Wide feet / toe box not truly wide** (114 mentions, the biggest single topic). "Most shoes today are designed too narrow in the toe area, even when they are labeled as Wide." "Wide fit and wide toe? Not the same thing." Buyers also want a wide midfoot/instep, not only wide toes.
5. **Durability.** "Clifton 9 foam died after 100 miles… like a brick." Gaviota "worn out in 7 months." Kuru eyelets breaking at $170. Skechers Arch Fit "worn out after a few months."
6. **Distrust of reviewers and affiliates.** "It says he earns commission so is biased!" "Are you being compensated to endorse these brands?"
7. **Online/FB-ad brands: returns and legitimacy** (Hike videos). "DO NOT Buy. You can not return." "No phone #. Chat is automated." "Less than $20.00 on Amazon." Knock-offs are compared openly.
8. **Fit and put-on issues**: heel slippage, can't tighten the laces, "fake laces that are stationary/stitched" on Skechers slip-ins (a swelling concern), and wanting laces you can loosen for swelling.
9. **Looks**: "They are so bulky, look like a brick or a weapon." Frumpy vs stylish is a live debate on the travel videos.

## 3. Why people like each competitor

| Brand | What commenters credit it for |
|---|---|
| **Hoka (Bondi 9 / Clifton 10 / Gaviota / Transport)** | Max cushion for standing; "Bondi 9 is what I have for 12hrs shift… Add an insole"; Gaviota H-frame ankle stability; recommended by doctors; available in wide and extra-wide. **Against**: foam dies fast, "mushy with no support", "Hoka Bondi gave me plantars", narrow toe box, slipping. |
| **Brooks (Ghost / Glycerin / Adrenaline GTS)** | "For older folks that need more stability, choose Brooks over Hoka." Adrenaline helped "during the WORST of my Plantar Fasciitis"; wide versions. **Against**: toe-box creasing (Glycerin), intrusive support bar, Glycerin 23 "hurt my heels". |
| **Skechers (Arch Fit, Go Walk, slip-ins)** | Cheap and familiar, "Great for a 70 year old", "never slipped" on wet marble in Tuscany (Go Walk), hands-free slip-ins. **Against**: max-cushion models triggered plantar issues, the arch is too narrow for over-pronation, wears out, poor ankle support, toes compressed; "Any thing by skeeters, is garbage." |
| **Kuru** | Heel cup, "saved my heels", plantar-fasciitis relief, wide forefoot, the parents of one commenter were sent by their podiatrist, held up on trails, dog-walker sandals. **Against**: the name (a prion disease, mocked at length), heel drop, $170 for EVA, eyelets breaking, "did nothing… caused me to start having knee pain". |
| **Orthofeet** | "Six pairs… At 77… the best"; plantar-fasciitis relief; extra-wide; Kita slip-ons for temples and mosques while traveling; included inserts. **Against**: "insoles feel like you are standing on the edge of a cliff"; pricey. |
| **Hike** | Wide toe box, barefoot feel, light; one 65-year-old with neuropathy and plantar fasciitis "walked 8 miles a day for 4 days". **Against**: returns, sizing, no phone, knock-offs at $20, "need more support". |
| **Travel favorites** (Ecco, Merrell, Taos, Vionic, Dansko, Teva, Keen, Vessi) | Waterproof, cobblestone-proof, no break-in, "look good" with outfits, arch support plus a wide toe box. A nurse persona: "my old nurse's feet love them". |
| **Others named for pain** | Altra and Topo (wide toe box, adjustable drop), New Balance More/1080/860 (4E widths), Asics Kayano and Nimbus, Oofos, Birkenstock, SAS, Good Feet Store inserts. |

## 4. Features and benefits commenters ask for or praise
- **Wide toe box** + **wide midfoot/instep** + narrow, locked heel ("narrow at the heel with a wide toe bed").
- **Heel cushioning plus a firm, stable base**: soft but not wobbly, especially for seniors and balance.
- **Arch support that is "enough but not poking"** (several people hate arch bumps), plus a removable insole for orthotics.
- **Moderate heel drop** (8-10 mm) is valued for plantar fasciitis; many complain about zero-drop or high-stack extremes.
- **Slip-resistant tread** for nurses, kitchens and wet cobblestones.
- **Easy on/off** (slip-in, hands-free) **but adjustable for swelling** (real laces, not stitched).
- **Lightweight, breathable**, no break-in, "look normal / not orthopedic".
- **Waterproof** options for travel and Disney: "You did not mention anything about waterproof."
- **Durable** for concrete: "even the most expensive shoe only lasted me 2-3 months."
- **Affordable**, with a mid-budget option.

## 5. Complaints about current shoes (pain language people use)
- "pain on the bottom of my foot or in the ankle"
- "feet were killing me"
- "like walking on boards"
- "first steps in the morning"
- "pain when I stand up after sitting"
- "heel spur"
- "fat pad"
- "toes compressed / black toenail"
- "foot slides forward"
- "heel slippage"
- "knee pain from soft foam"
- "back pain after shifts"
- "swollen ankles in new pair"
- "burning feet"

## 6. Persona notes
- **Nurses / 12-hour shifts / standing workers** (27 explicit mentions, plus warehouse, teacher and cashier). They choose by brand (Hoka Bondi, Brooks Ghost Max, Kuru) and often add an insole. Pains: heel and arch pain while standing, back pain after shifts, and shoes that wear out every 3 months. Questions: "Women 12 hr hospital which would be best", "any safety toe shoes for standing all day?" Cashiers say Hoka "accelerated the pain… bc my feet were sinking."
- **Plantar fasciitis / heel pain** (the largest group). They have tried many shoes and inserts and are frustrated by conflicting advice. They respond to "phase-based" explanations (cushion and drop first, then transition). They want one specific recommendation.
- **Seniors (60-84)**: stability and fall fear outrank softness. "As a 68yo senior who often walks up to ten miles…", "Feeling great, I wear HOKA and enjoy walking at 84", "I need to make sure I don't fall as a Sr." Comments mention Parkinson's, bunions, leg-length difference and slip-on needs.
- **Neuropathy / diabetes / swelling** (fewer mentions on YouTube than on Trustpilot): want adjustable laces for swelling, ask "which sketchers would be beneficial for diabetic neuropathy?", and find Hike balance helpful.
- **Plus-size / heavy / big feet**: "100kg… flat feet and wide toe", "I weigh 245 pounds… heel spurs… polyneuropathy", "Overweight Overpronation… 10+hrs". Women with size 11-14 wide feet complain that "nobody sells half sizes" and that "wide width shoes are still kinda narrow". They want stylish, not orthopedic-looking.
- **Travelers (Europe, cruise, Disney)**: on the travel creator's videos the audience is 50+ women who buy on her recommendation (Ecco, Taos, Vionic, Merrell). They care about **cobblestones, wet weather, no break-in, packability and looking put-together**. Tips: "break them in before you go!" (21 likes). Disney commenters ask about waterproof options, socks and sizing up.
- **FB-ad / online comfort-brand buyers** (Hike videos): mostly older women who love the barefoot feel and wide toe box but get burned on returns and sizing, and who compare with Amazon knock-offs.

---

## 7. Verbatim comments (no usernames)

| # | Quote | Theme | Persona | URL |
|---|---|---|---|---|
| 1 | "high stack height plus squishy foam makes these shoes inherently unstable especially for senior citizens" | Stability objection | Senior | https://www.youtube.com/watch?v=1v17GoOoo0k |
| 2 | "So confusing as to what to do. Every “ expert” says different things" | Conflicting advice | Plantar fasciitis | https://www.youtube.com/watch?v=rfotyiQkz9M |
| 3 | "Who has the kind of money to buy phase 1 then Phase 2 and the Phase 3 shoes. They all are expensive." | Price | Plantar fasciitis | https://www.youtube.com/watch?v=MW0tAUIAr4Q |
| 4 | "Topo and Altra shoes are & $150 or more. These aren’t really affordable options." | Price | Plantar fasciitis | https://www.youtube.com/watch?v=MW0tAUIAr4Q |
| 5 | "These are all very expensive… what are the mid budget options £40 to £80?" | Price | Plantar fasciitis | https://www.youtube.com/watch?v=pSlno1IXMSA |
| 6 | "Very well said! Hoka Bondi 9 is what I have for 12hrs shift. I'm good! Add an insole" | Why Hoka | Nurse/12h | https://www.youtube.com/watch?v=DOd45C3C028 |
| 7 | "I have a hoka gaviota 5. It was the best until 7 months later its already worn out. I just use for work and stand all day." | Durability | Standing worker | https://www.youtube.com/watch?v=pSlno1IXMSA |
| 8 | "I tried the Hoka Clifton 10 and Bondi SR and they accelerated the pain early into my shift bc my feet were sinking." | Too soft | Cashier | https://www.youtube.com/watch?v=UEwnT625bGY |
| 9 | "Walking on marshmallows killed my feet, ankles, and knees." | Too soft | Walker | https://www.youtube.com/watch?v=1R2YgBrkyGw |
| 10 | "Them cushy shoes make my feet hurt worse. Feel like my feet were in a boxing match." | Too soft | Plantar fasciitis | https://www.youtube.com/watch?v=MW0tAUIAr4Q |
| 11 | "Hoka Bondi gave me plantars. I do better with Clifton" | Hoka complaint | Plantar fasciitis | https://www.youtube.com/watch?v=MW0tAUIAr4Q |
| 12 | "The Brooks Adrenaline DID help me during the WORST of my Plantar Fasciitis!!!" | Why Brooks | Plantar fasciitis | https://www.youtube.com/watch?v=MW0tAUIAr4Q |
| 13 | "For older folks that need more stability, choose Brooks over Hoka" | Stability | Senior | https://www.youtube.com/watch?v=TekVuVDwtvk |
| 14 | "Clifton 9 foam died after 100 miles for me, like a brick." | Durability | Walker/runner | https://www.youtube.com/watch?v=q6_zwDLH43I |
| 15 | "Kuru shoes work. I used to get injections in my heals. Not anymore. All I wear is Kuru!" | Why Kuru | Heel pain | https://www.youtube.com/watch?v=rfotyiQkz9M |
| 16 | "Kuru shoes saved my heels… Between their shoes and regular calf stretches, my fasciitis is gone." | Why Kuru | Plantar fasciitis | https://www.youtube.com/watch?v=HYdJ20jXgME |
| 17 | "I’m a nurse and I work 12 hour shift so I nee[d]…" (Kuru mostly helped, last pair didn't) | Nurse needs | Nurse/12h | https://www.youtube.com/watch?v=HYdJ20jXgME |
| 18 | "An EVA midsole in shoes that sell for $170 is a robbery." | Price/value | Skeptic | https://www.youtube.com/watch?v=HYdJ20jXgME |
| 19 | "DO NOT BUY THE ATOM 2. No way any sneaker should fail like that at this price point" | Durability | Kuru owner | https://www.youtube.com/watch?v=HYdJ20jXgME |
| 20 | "Here is a HUGE MARKET you are missing! WIDE shoes for WOMEN!!! PLEASE DO IT." | Wide women's | Wide feet | https://www.youtube.com/watch?v=HYdJ20jXgME |
| 21 | "Most shoes today are designed too narrow in the toe area, even when they are labeled as Wide." | Toe box | Arthritis | https://www.youtube.com/watch?v=OFLrYkKCi2A |
| 22 | "I stand on warehouse machines for 10 and 12 hours every day. No shoe helps." | Standing pain | Warehouse | https://www.youtube.com/watch?v=OFLrYkKCi2A |
| 23 | "I have been trying to replace my shoes every 3 months or so because of walking on concrete for 10 hours a day… these are about double what I usually pay." | Durability + price | Concrete worker | https://www.youtube.com/watch?v=OFLrYkKCi2A |
| 24 | "I have such bad foot heel pain but have spent hundreds of dollars in expensive shoes just afraid to go for another disappointment. My pain is so bad I just want to cry sometimes" | Pain + risk | Heel pain | https://www.youtube.com/watch?v=OFLrYkKCi2A |
| 25 | "Strangely the skechers elite max cushioning gave me plantar tendon issues" | Skechers complaint | Walker | https://www.youtube.com/watch?v=cce6oZWiAOc |
| 26 | "Love my Skechers. Have 3 pairs. Never buy anything else. Great for a 70 year old." | Why Skechers | Senior | https://www.youtube.com/watch?v=eIyMJmrP9PE |
| 27 | "I have Parkinson’s… I also have plantar fasciitis… That’s why I’m considering slip on shoes" | Slip-on need | Senior | https://www.youtube.com/watch?v=eIyMJmrP9PE |
| 28 | "Are the shoe laces tie-able so you can tighten them up or loosen them up to accommodate foot swelling?" | Swelling, adjustability | Swelling | https://www.youtube.com/watch?v=TTvHGuH6i4c |
| 29 | "I have six pairs of Orthofeet shoes. At 77 yo with several issues with my feet… found them to be the best." | Why Orthofeet | Senior | https://www.youtube.com/watch?v=ZMqUnqFuNF4 |
| 30 | "The insoles feel like you are standing on the edge of a cliff though" | Orthofeet complaint | Senior | https://www.youtube.com/watch?v=ZMqUnqFuNF4 |
| 31 | "3 weeks in the Balkans and Istanbul in my Orthofeet Kitas. Easy to take off and put on for temples and mosques." | Travel slip-on | Traveler | https://www.youtube.com/watch?v=nPlRcVdWGR8 |
| 32 | "my old nurse’s feet love them. They’ve been through many cobblestone streets" | Travel + nurse | Retired nurse/traveler | https://www.youtube.com/watch?v=FypZvM7jtmI |
| 33 | "I don't care about looking frumpy… I'm too old to think people are looking at my shoes." | Function over style | Senior traveler | https://www.youtube.com/watch?v=FypZvM7jtmI |
| 34 | "If I have a choice between stylish or not stylish, I know which one I will pick every time." | Style matters | Traveler | https://www.youtube.com/watch?v=FypZvM7jtmI |
| 35 | "I had foot surgery 3 years ago… I'm taking Asics to Europe and I don't care if people judge me!" | Travel, post-surgery | Traveler | https://www.youtube.com/watch?v=FypZvM7jtmI |
| 36 | "I love Skechers Go Walk shoes. I walked all over Tuscany… on slanted marble steps… and never slipped." | Slip-resistance | Traveler | https://www.youtube.com/watch?v=nPlRcVdWGR8 |
| 37 | "The most important thing about getting shoes to wear on a vacation is to break them in before you go!" | No break-in | Traveler | https://www.youtube.com/watch?v=Ozsh8fM7naQ |
| 38 | "I need to make sure I don’t fall as a Sr. Your shoes look very stable" | Fall fear | Senior traveler | https://www.youtube.com/watch?v=nPlRcVdWGR8 |
| 39 | "You did not mention anything about waterproof or water shoes though in this video. :(" | Waterproof | Disney | https://www.youtube.com/watch?v=YUHnylWKtvQ |
| 40 | "Is sizing up good idea if will be using for walking?" | Sizing | Disney | https://www.youtube.com/watch?v=YUHnylWKtvQ |
| 41 | "I have heel spurs… polyneuropathy in my legs. I weigh 245 pounds… definitely overweight." | Needs | Plus-size, neuropathy | https://www.youtube.com/watch?v=1v17GoOoo0k |
| 42 | "I can't find any good walking shoes for women." | Unmet need | Women walkers | https://www.youtube.com/watch?v=1v17GoOoo0k |
| 43 | "Size 11.5 wide. Nobody sells half sizes and I'm not wearinga 12😢" | Half sizes | Big/wide feet | https://www.youtube.com/watch?v=Hwq5KOztjN8 |
| 44 | "My only complaint about Dolce Vita shoes is their wide width shoes are still kinda narrow." | Wide not wide | Big/wide feet | https://www.youtube.com/watch?v=Hwq5KOztjN8 |
| 45 | "I need a shoe for feet that have a wide mid foot. Not just the toe. The in step" | Fit need | Wide feet | https://www.youtube.com/watch?v=WYLQMxhA88Q |
| 46 | "I have neuropathy really bad as well as plantar fasciitis and I walked and kept up with two gals half my age. (I’m 65)." | Why Hike | Senior, neuropathy | https://www.youtube.com/watch?v=rAIIVFW7A0E |
| 47 | "I tried and failed to return some Hike shoes. They replied after several weeks that clearance shoes cannot be returned" | FB-brand returns | Online buyer | https://www.youtube.com/watch?v=rAIIVFW7A0E |
| 48 | "I have been wearing these Hike Barefoot shoes for over a year. LOVE them. Less than $20.00 on Amazon." | Knock-off price | Online buyer | https://www.youtube.com/watch?v=rAIIVFW7A0E |
| 49 | "I’ve had a problem with hike & their shipping… ordered these over the facebook Buyer Beware" | FB-ad trust | Online buyer | https://www.youtube.com/watch?v=rAIIVFW7A0E |
| 50 | "DO NOT BUY. They sent me the wrong size. Customer service is non-existent… No phone #. Chat is automated." | Service | Online buyer | https://www.youtube.com/watch?v=Ay8E1z_yVMI |
| 51 | "It says he earns commission so is biased! This is a salesman not a reviewer." | Reviewer distrust | Skeptic | https://www.youtube.com/watch?v=w2tGzYGhgZY |
| 52 | "Women 12 hr hospital which would be best" | Nurse ask | Nurse/12h | https://www.youtube.com/watch?v=pSlno1IXMSA |

---

## 8. Implications for Comfort Wear
- **Gap to own**: "**cushioned heel + stable base + truly wide toe box + slip-resistant + easy on, at ~$60**". YouTube commenters say they can't find this combination under $150.
- **Pre-empt the top objections**:
  1. stability, not mush (seniors and fall fear)
  2. a toe box that is wide in practice, with a "wide midfoot too" proof
  3. honest sizing guidance
  4. no-break-in plus a travel/cobblestone use case
  5. adjustable elastic laces for swelling (a contrast with Skechers' stitched fake laces)
- **Trust is the conversion blocker** for FB-ad shoe buyers: Hike's return complaints and Amazon knock-off comparisons, and OrthoFit-style scams. Trustpilot shows the same objection about Comfort Wear. A visibly easy return process, with Kuru's 90-day wear test as the benchmark, would neutralize the "FB ad scam" frame.
