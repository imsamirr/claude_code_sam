# Comfort Wear: what people say in the comments on our own Meta ads

Source: Atria, Meta ad account "WearOrtho" (a829d015648d481fb70eb471556cdb77, CAD). The comments were pulled on 2026-11-18. The ads were ranked by spend over the last 30 days and over a 92-day window (2026-08-18 to 2026-11-17).
Atria calls used: **46** (2 `list_ad_account_ads` + 44 `get_ad_account_ad`). There were no rate-limit errors.

## Method and caveats

- **Ads read:** 31 high-spend ads on Facebook, one page each (up to 100 items per call). A second Facebook page was pulled for the 3 biggest ads that had one (HF7, Nurse Kyro390v1_H5, RTG B6). Instagram was read for 8 ads, including 2 pages for RTG B6.
- **Comments read:** about **795 user comments** in total, roughly **613 on Facebook** and **182 on Instagram**. I also read about 560 brand replies on Facebook, but they are not counted in any total. On Facebook, close to half of everything returned is a brand reply. On Instagram there are almost none.
- **Sample size:** Atria's `total_count` is larger than what it returns. RTG B6, for example, reports 987 total but returned about 140 Facebook user comments. Treat the counts below as a large sample, not a census. The counts are approximate tallies from reading the comments. One comment can count toward more than one theme.
- **5 ads returned no readable comments:** MZ1 COM374_HO2, LR2 COM316 Spanish, JV1 COM211, AR20 Senior, and C1 528 (C1 came back "unsupported").
- **Big platform gap:**
  - On **Facebook**, comments are mostly questions plus owner praise, and almost every comment gets a brand reply.
  - On **Instagram**, the same ads draw overwhelmingly negative owner comments. About 75 to 80% of Instagram owner comments on the retargeting UGC ads (RTG B6, RTG B3) are negative: no support, refunds refused, hard to get on.
  - The likely explanation is that negative Facebook comments are hidden or moderated, so the API does not return them. Instagram is not moderated that way. This is an inference; I could not confirm it.
  - Either way, what prospects see on Instagram is a wall of "don't buy, can't return."
- **Brand reply page names:** comments are answered under page identities such as "Nurse Finds", "Travel Finds", "Teacher Finds", "Foot Health Journal", "Shoes Review Insider", "ComfortOrtho Shoes", and **"Asociación Nacional de Enfermeras Hispanas"**. The last one reads like a real professional association, which is a trust and compliance risk worth reviewing.
- **Likely bots, spam, or low-signal comments (about 14):**
  - "Baaack to baaack": the same account posted it on RTG B6 and RTG B3, and the brand replied both times.
  - "Someone like this comment", "You can have mine", ")", a blank comment, "👏👏👏👏💃🕺".
  - "Happy birthday Nelson hope you have a great day", "Fat" (a troll), "@", "Next", "ANKKLE ON FOOT", "Yes my can".
  - On Instagram (RTG B6), "The best shoes ever for all day comfort 😍" and a "The best 👌" reply were posted about 2 minutes apart, which looks seeded.
  - About 35 bare friend tags (a name only) are counted as sharing, not as content.
- **Privacy:** one commenter posted an order number and a tracking number publicly (RTG I19). This file leaves them out. No commenter names or profile details are included.

---

## 1. Ads read

Spend is the 92-day spend in CAD unless marked (30d). The concept is the part of the ad name after "|". "User comments read" is Facebook plus Instagram.

| # | Ad (code) | Concept | Spend 92d | User comments read (FB / IG) |
|---|---|---|---|---|
| 1 | TOFv1_HF7 | Kyro369v2 hook2 (travel, "50,000+ steps", 40% off) | $75,654 | 39 / 13 |
| 2 | TOFv1_HF2 | 807_Aubrey New UGC Ortho Stretch "Don't Waste Spent Money" H03 (Emily RN copy) | $20,028 | 22 / 18 |
| 3 | TOFV1_JW1 | COM320_HO1 (avatar), Disney/Florida rain plus travel copy | $13,931 | 10 / 3 |
| 4 | INT_05.28.26 | Nurse Page Kyro390v1_H5 (nurse shoe-ranking; ranks Hoka below Crocs) | $13,326 | 87 / 18 |
| 5 | RTGv1_B6 | 203_Iteration_UGC_OrthoStretch_H1 (retargeting UGC, "40% OFF") | $12,556 | 87 / 86 |
| 6 | TOFV1_HJ27 | JULYWK2_VID1_JACK_Teacher_Hook1 (teachers "standing all day") | $11,642 | 50 / 1 |
| 7 | TOFV1_NH3 | OCTWK4_VID4_JACK_GeneralOverweightParkDay_Hook2 (Disney park day) | $9,607 | 1 / – |
| 8 | TOFV1_HL60 | AUGWK1_VID2_JACK_TeacherTested_Hook2 (5 best teacher shoes, 480h) | $9,458 | 10 / – |
| 9 | TOFV1_HI16 | Nurse, COM225_Kyro390 Spanish (doctor expert, "73% personal sanitario") | $9,209 | 23 / – |
| 10 | RTGv1_H3 | Ortho-Stretch-Cushion-Shoe-#753 static (40% off + free shipping) | $7,882 | 42 / 3 |
| 11 | JULYWK3 | VID1_JACK_NurseNotRunners_Hook1 | $7,805 | 13 / – |
| 12 | TOFV1_KW1 | COM284_HO1 ("Plus-Sized Traveling", Disney) | $7,169 | 17 / – |
| 13 | RTGv1_B3 | Kyro_293_3_V2 (retargeting UGC, "Podiatrist Recommended") | $6,792 | 28 / 40 |
| 14 | RTGv1_C3 | 661 Real Static ObjectionHandling CustomerReviews ("500,000+ ALL be wrong?") | $6,332 | 33 / 0 |
| 15 | TOFV1_MZ1 | COM374_HO2 (fix) (plus-size Disney) | $5,576 | 0 / – |
| 16 | RTGv1_O1 | Ortho Stretch static (40% off sitewide) | $4,580 | 13 / – |
| 17 | TOFV1_MO2 | OCTWK3_VID2_JACK_TravelRetiree_Hook1 | $4,044 | 1 / – |
| 18 | RTGv1_I6 | Warning-task_Warehouse static ("48 HOURS LEFT") | $3,384 | 38 / – |
| 19 | TOFv1_HF5 | Teacher Page COM51 Teachers Iteration ("More Than" shoe, 45-day trial) | $3,077 | 42 / – |
| 20 | TOFV1_HZ1 | COM204 Shoe ranking feet only (nurse, AI) | $2,987 | 3 / – |
| 21 | TOFV1_LR2 | COM316 "Hokas and Brooks the worst shoes for work" (Spanish) | $2,922 | 0 / – |
| 22 | TOFV1_LI1 | COM296 Nurse wants to quit drama (AI) | $2,824 | 7 / – |
| 23 | TOFV1_JV1 | Travel, COM211_h2 | $2,812 | 0 / – |
| 24 | TOFV1_HG | Task158 DesignedNeuropathy FeatureCallout, Comfort Shoes Listicle | $2,475 | 6 / – |
| 25 | TOFV1_LZ1 | COM338 Husband tired of nurse wife complaining drama | $2,406 | 3 / – |
| 26 | RTGv1_I19 | SellingOut4Days static | $2,286 | 33 / – |
| 27 | TOFV1_MI3 | COM337_HO3 (Spanish, cleaners "20,000 pasos") | $2,265 | 2 / – |
| 28 | RTGv1_C1 | 528 Static ObjectionHandling ("Trusted By Nurses") | $2,220 | unsupported |
| 29 | COM174 | Kyro362Teacher (teachers with arthritis) | $2,157 | 2 / – |
| 30 | INT_07.03.26 | General Foot Pain COM55 AR20 Senior 929 Iteration | $1,847 | 0 / – |
| 31 | TOFV1_NL1 | COM376_HO1 (5 best shoes for Disney) | $756 | 1 / – |

The ad copy reused across most nurse ads is the "Emily, RN" testimonial. Retargeting statics promise "Relieves Plantar Fasciitis, Bunions, Neuropathy Pain / Podiatrist-Recommended / 120,000 5-star reviews / Free shipping & returns". Video ads say "500,000+ customers, 4.9 stars", with a 30-day or 45-day risk-free trial depending on the ad. **The trial length and refund promise differ from ad to ad, and owners say the promise is not honored.**

---

## 2. Objections and doubts, ranked

These are pre-purchase doubts from prospects, plus owner experiences that act as objections because other people read them.

| Rank | Objection | Approx. count | Where it concentrates | Typical wording |
|---|---|---|---|---|
| 1 | **Refunds and returns not honored, no customer service** (credit-only, "donate to Salvation Army / Red Cross and send the slip", 20 to 30% partial refund offers, emails unanswered, "BBB F"). Prospects then cite it: "read the comments" | **~55** (about 34 on IG, 18 on FB, plus 5 readers saying "this saved me from buying") | IG on RTG B6 and B3; FB on RTG C3, H3, I6 | "Don't be fooled by the free returns. They use every excuse not to refund you." |
| 2 | **"I can't wear sneakers" (dress code, needs a professional, dressy or all-black look; white sole looks unprofessional)** | **~53** (about 46 from teachers) | Every teacher ad (HJ27, HL60, HF5); also nurses, office, courtroom, correctional officers, flight attendants, uniforms | "Except they're sneakers. What about dressier shoes for when we wear dresses or dress pants??" |
| 3 | **"It's not comfortable / no support / made my pain worse"** (owners, used as a warning to others) | **~55** (about 47 on IG) | IG retargeting UGC | "Shoes were like walking on cardboard NO SUPPORT!!" |
| 4 | **Scam, fake reviews, "lies", AI ads, distrust of rankings** | **~38** | IG on Nurse Kyro390 (AI), HF2 ("LIES"), RTG B3 ("internet scam") | "I wouldn't trust any online shoe claiming for nurses" / "AI strikes again lol." |
| 5 | **Width and toe box** (not a true wide, needs 2E/4E or 9 Wide, "toe box looks narrow", bunions) | **~38** | All ads | "Are they actually wide? The pictures don't look very wide and I have very wide feet." |
| 6 | **Men can't find their shoe** ("only for women?", size 13 and up, men nurses and teachers) | **~31** | Nurse and teacher ads, Spanish ads | "Ya know, men teach too. These seem to be only in the women's line." |
| 7 | **Not suited to the job's safety needs** (slip resistance not certified, kitchen-safe tread, steel or composite toe, leather or fluid-proof, needle-resistant, mesh not OK in hospital) | **~30** | Nurse ads, Spanish kitchen ads, factory and warehouse workers | "if you built them for nurses, you wouldn't have made them mesh." |
| 8 | **Not waterproof** (rain at Disney, travel weather, recess duty, spills) | **~25** | Travel and Disney, nurse | "Too bad they're not waterproof" |
| 9 | **Price and the checkout total** ("how much?", "$150 for what?", "$59 then over $100 at checkout", BOGO doubling, USD vs AUD/CAD, "can't afford $70+", free shipping only on 2+) | **~19** | Spanish HI16, RTG B6, I19, teacher | "Me dice q $59 y al final más de 100" |
| 10 | **Hard to get on / sock-liner / elastic laces** (as a warning) | **~14** | RTG B6, B3, C3, H3, HF7 | "Super comfortable but hard to put on. Even with a shoe horn the inner sock is a challenge." |
| 11 | **Hook or claim doesn't match their reality** ("teachers don't stand still", "6 hours??", "park day is 35k steps", "most nurses sit") | **~13** | Teacher HJ27, Disney NH3, nurse | "Tell me you've never taught without telling me you've never taught." |
| 12 | **Doubts about high heel stack, soft cushioning, or instability** ("heel is 2 inches", "spongy heel dangerous for seniors", "ultra padded shoes damage knees", "feet tilt forward", "like a wedge heel") | **~13** | Nurse, retargeting, IG | "Do they have the soft spongy heel ... so dangerous for seniors with balance issues." |
| 13 | **Shipping** (slow, never received, tracking, "where do you ship from") | **~12** | Retargeting | "I pray they help with my Neuropathy and it doesn't take a month to get here!" |
| 14 | **Where it's made / China / dropship** ("why are these on so many sites") | **~6** | RTG B3, teacher HF5, I19 | "Where are they made? ... it's a shame you didn't get a direct answer." |
| 15 | **Insoles sold separately / "you need insoles anyway"** | **~4** | IG RTG B6 | "So, I buy the shoes but then need to purchase the insoles separately??? ... your ad is completely misleading" |

**Not found at any meaningful level:** "looks like Skechers" (Skechers is mentioned as the alternative people prefer, not as a lookalike) and "old lady shoes". The style complaints are "ugly", "wish they were cuter" and "need better colors", about 5 comments.

---

## 3. Questions people ask, ranked

| Rank | Question | Approx. count | Notes |
|---|---|---|---|
| 1 | **"Will these help my ___?"** Plantar fasciitis (about 12), neuropathy or diabetes (about 7), back pain (about 6), bunions (about 6), high arches (about 6), flat feet (about 4), knees or knee replacement (about 4), Achilles (2), overpronation (3), RA, Morton's, sciatica, hEDS, stroke | **~50** | The single biggest category. Brand replies are hedged ("results vary, consult a professional"). |
| 2 | **Sizing and width:** true to size? size up? wide or 2E/4E? US vs CA/AU sizes? small sizes (5) or big sizes (men's 13/14) | **~55** | An Ortho Stretch half-size-up rule is mentioned by owners and even a podiatrist. Owners say both "runs big" and "runs small". |
| 3 | **Men's styles?** | ~31 | Often frustrated. Men's max size 10.5 to 11.5 is noticed. |
| 4 | **Work suitability:** slip-resistant? kitchen, restaurant, factory, warehouse? steel toe? | ~30 | Very heavy in Spanish ads (cocina, restaurante, fábrica). |
| 5 | **Waterproof or fluid-resistant?** | ~25 | |
| 6 | **Where to buy:** in stores? Amazon? what brand or name is this? link? | ~22 | "Whats the name of them? I can never find" shows the ads don't brand the shoe clearly. |
| 7 | **How much?** | ~15 | |
| 8 | **Colors:** white? black-on-black? brown or beige? pink? orange? | ~15 | White is requested 6 times. Black-on-black, for uniforms and dress codes, about 6 times. |
| 9 | **Removable insole, orthotic-friendly, replacement insoles?** | ~8 | |
| 10 | **Shipping time, tracking, Canada shipping, currency** | ~10 | |
| 11 | **Practical details:** socks or no socks? slip-on vs tie? washable or wipeable? good in hot weather? cobblestones? hiking? running? | ~12 | |

---

## 4. What owners praise (benefits), ranked

About 80 owner-praise comments, about 70 of them on Facebook.

| Rank | Benefit | Approx. count | Proof language |
|---|---|---|---|
| 1 | **"Most comfortable shoes I've ever worn / love them"** (general) | ~40 | "They are more comfortable all day than any other shoe I have ever worn!! Love them!!!" |
| 2 | **Repeat purchase / multiple pairs / every color** (2, 3, 4 or 5 pairs; "3 pairs in two years") | ~20 | "Best shoes EVER, I have a pair in EVERY color" |
| 3 | **Pain-free through long shifts** (10, 12 and 14+ hour days, "4:39 AM to 5 PM", retail 10 to 12 h, "not limping to my car") | ~14 | "I work 14 plus hours on my feet and they really help" |
| 4 | **Specific pain relief:** plantar fasciitis, neuropathy plus knee replacements, "feet, knees, hips and back", "back walking again" | ~8 | "First time in years my feet, legs, and back have not hurt by midday." |
| 5 | **Room for toes / wide fit** ("wiggle my toes", "room for bunions", "toes don't hurt on 3-mile walk", "come in wide width") | ~5 | "The shoes hug my feet, and I love being able to wiggle my toes!!" |
| 6 | **Non-nurses love them too** (retail manager, bookseller, childcare, table games dealer, home) | ~6 | "I'm not a nurse… I'm a retail manager… the only shoes I can wear for 10+ hours" |
| 7 | **Gifted, or family converted** (95-year-old mother, husband ordering his own, daughter took them) | ~4 | "I bought a pair for my 95 year old Mother… she loves them!!" |
| 8 | Lightweight; arch support; a podiatrist approved them; easy on and off (1 person); "best return policy" (1 person) | ~6 | |

How long owners have worn them: "2 years" and "3 pairs in two years", "about 3 years" (still loves them but they "squish my toes"), versus "fell apart within 6 months" and "suck after a few months".

---

## 5. Owner complaints, ranked

| Rank | Complaint | Approx. count | Typical wording |
|---|---|---|---|
| 1 | **Uncomfortable, no arch or side support, pain got worse** (including "developed plantar fasciitis", "back hurt worse", "fine for 2 to 3 hours, not long walks") | **~55** | "These felt great around the house. The first time I wore them on a long walk ... I couldn't continue to walk!" |
| 2 | **Returns and refunds refused** (credit only; donate to charity and send the receipt; partial refunds of 3%, 20% or 30%; "sanitation reasons"; no reply) | **~46** | "they said they can't take returns because of sanitation reasons and I needed to donate them ... so I am out $60" |
| 3 | **Sizing inconsistent** (too big or too small despite measuring, wrong size shipped, left and right shoes different sizes) | ~22 | "The left and right shoe were different sizes and the smell of them is so offensive." |
| 4 | **Hard to get on** (sock-liner collar collapses, a 10-minute struggle, high instep, elastic laces too long, people trip on the toggles) | ~14 | "kept tripping over the strings and stepping on the little plastic pieces" |
| 5 | **Cheap materials and durability** ("plastic" soles, smell, insoles wear out, falls apart in 6 months, "$10 shoes", blisters) | ~13 | "I rotated mine with other shoes and they fell apart within 6 months!" |
| 6 | **Delivery problems** (never received, missing insole, wrong product, arrived squashed, slow) | ~7 | "Just received two pairs, one ... didn't have the comfort wear insole in it" |
| 7 | **Fit shape** (toe box too deep or wide, foot slides forward, heel sits wrong) | ~5 | "The toe area is much wider and deeper than i need." |
| 8 | **Checkout and site** (discount form errors, payment won't go through, "hard to order anymore", no order history for an HSA receipt) | ~4 | "I can't print an Itemized receipt for my HSA ... No one to contact either" |
| 9 | **Slip resistance claimed but not real** | 2 | "they say slip resistant but theyre not" |

---

## 6. Competitor mentions

| Brand | Mentions | What people say |
|---|---|---|
| **Hoka** | **~28** (about 22 positive) | This is the default "I already have the answer" brand. On IG Nurse Kyro390, "Love my Hoka's. Wear them all day and no feet pain" got **29 likes**, "Hoka saved my legs" got 21, and "Hoka is the BEST" got 16. Ranking Crocs above Hoka was mocked: "Rating crocs above Hokas is wild 😂". Hoka has wide options. Price anchor: "I just dropped 160 on a pair." Negatives: wears out in about 6 months, made one person overpronate, a podiatrist said no to squishy Hokas for PF, one person found inconsistency between pairs. A Hoka-loyal teacher wants to try ComfortWear for a review. |
| **Skechers** | ~13 | This is the fallback for detractors: "I was fine with my sketchers", "will go back to my sketchers", "Sketchers work for me up to 20km", "Glide Step Max Cushioning". It also came up as a durability anchor ("4 pairs a year of sketchers") and on travel (fine for 2 days of Disneyland, then pain). **Nobody said our shoes "look like Skechers."** |
| **Brooks** | ~9 | Split. "Brooks are hard!!! They suck" versus "Brooks adrenaline are the best!" and "Glycerin Brooks with success". People cite Brooks for back help and for its **warranty**. |
| **On / Cloud** | ~6 | Travel and Disney: "On cloud was awesome at Disney", "I swear by my on clouds", "Ons are the only shoes that work". |
| **Kuru** | 3 | "Kuru beats them all hands down", "KURU 100% better…more expensive yet well worth the money", "right out of the box the best I've tried". |
| Orthofeet | 2 | "Orthofeet"; "Ortho Feet sandals. NEVER did my feet hurt". |
| Clove | 2 | Nurse alternative ("I wear Cloves"). |
| Vessi / Orthora Pro | 3 | "I've seen this ad before and two other brands like this too; Orthora Pro and Vessi" (category fatigue). |
| Warranty and refund comparisons | 3 | "Brooks, Skechers and Hokas have a good warranty"; Timberland Pro has "a month to try ... full refund, 7 years"; JackShibo has "Amazon 30 day guarantee". |
| Others | 1 each | Crocs, Dansko, Birkenstock, Oofos, Converse with orthotics, Topo or Altra (true wide toe box), Rockport, MBT, Zeba, Kizik, ASICS, Keen, barefoot shoes, Hike Feet, "$36 Costco tennis shoes", G-Defy, NurseBabes (cited as a similar "garbage" nurse brand). |

**Takeaway:** Hoka is the incumbent our audience trusts, and the "Hoka is the worst" or "ranked below Crocs" angles cause pushback (Nurse Kyro390, COM316). The trust gap is about **warranty and refunds**, which is exactly where competitors are seen as safer.

---

## 7. Tagging and sharing behavior

- **Bare friend tags:** about 35, most on nurse and teacher ads. The brand answers with a template: "Thanks for tagging your friend, excited to have you and your friend as our customer."
- **"Report back" threads:** friends tag a buyer and ask for proof. Examples: "Deb ... update?", "how do you like them", "hi did it help?", "follow up tomorrow please seriously considering these but not completely sold yet", "how were they all night?". One owner comment ("They come pretty quick, I have two pairs") drew 7 replies asking about sizing, Italy and Canadian funds. Prospects want peer proof, not brand proof.
- **Forwarding and gifting:** "Forwarded to my nurse son", buying for a 95-year-old mother, a husband buying a pair to try, "Gift".
- **Negative social proof spreads on IG:** "All these comments are making my decision not to buy them way easier 😂", "Thank you ALL for your honesty ... saved me from making a HUGE MISTAKE!", "MK, did you read the negative comments?", "I almost ordered ... but I decided to read the feedback ... and what it takes to get refunded".

---

## 8. Notes on the top 5 ads

### 1. HF7, Kyro369v2 hook2 (travel, "50,000+ steps", 40% off): $75.7k over 92 days

- **What the angle draws:** mostly logistics questions (waterproof about 8 times, white color about 5, men, store, wide or high arches, bunions) and travelers' stories ("cobblestone fatigue is real", Spain and Portugal cruise, Ireland and Scotland weather).
- **Doubt about the step claim:** "50,000 steps is nothing!!!", "That's one single day in my shoes. They'd better be able to handle it!"
- **Competitors:** "Vessi!!!", "ZEBA", "try sketchers arch support finally found my shoe", and "Orthora Pro and Vessi ... still looking for the ultimate travel shoe for decades". On IG: Hokas through Portugal and Spain, Keens, On, "$36 Costco tennis shoes did just fine in Europe".
- **Owner pain:** "Super comfortable but hard to put on ... the inner sock is a challenge."
- **Refund pain:** "the return policy is misleading. They just want to give credits no actual return and refund"
- **Funnel friction:** "Can't get past the 'special offer' I just want to see if there is a men's light color! Guess I'll look elsewhere!"
- **Read:** the travel angle works for attention, but travelers immediately ask about weather-proofing and get competitor suggestions from others. Waterproof and cobblestone answers belong in the creative and on the landing page.

### 2. HF2, 807_Aubrey "Don't Waste Spent Money" (nurse UGC, Emily RN): $20.0k

- **On Facebook:** practical nurse requirements dominate: "Are they non slip", "Don't they need to be leather, blood proof", "Toes need to be needle resistant". People also ask about waterproofing, men's black, sizes 5 and 5.5, extra-extra-wide for neuropathy, and "$150 for what?". There is a true-wide-toe-box comparison to Topo and Altra.
- **On Instagram:** much harsher. "Shoes were like walking on cardboard NO SUPPORT!! ... medical field for 50 yrs worse shoes ever", "they were going bankrupt!! ... I got half of the money back", "LIES!!!!", "Do not buy these. Hard to get on!", "My hokas are amazing", "Kuru beats them all". A self-described podiatrist recommends a $50 Amazon shoe. One nurse explains that fabric uppers are unsafe around fluids and sharps.
- **Read:** the nurse-UGC angle invites workplace-spec scrutiny. The creative should address fluid resistance, slip resistance and upper material head-on, or switch nurse ads to a fluid-resistant model.

### 3. JW1, COM320_HO1 avatar (Disney and Florida rainy season, travel copy): $13.9k

- **Volume:** few comments (13).
- **Rain angle:** it triggers "Are they water proof for the daily rain at Disney World?" and a local's pushback ("Such blather. Anyone that actually lives here knows about rainy season").
- **Incumbents defended:** "I still prefer my HOKAS ... Solimar 2", "On cloud was awesome at Disney", and on IG "My Hokas have been all over Europe and Vegas ... the shoes you recommended are junk!!"
- **Owner:** "it pushes my feet forward and my toes were killing me".
- **Other asks:** "Well what about the guys?", "They have to come in orange."
- **Read:** the Disney audience is loyal to Hoka and On. Comparing against them invites defense. A pain-at-hour-8 story without naming brands may fare better.

### 4. INT Nurse Page Kyro390v1_H5 (nurse shoe-ranking; Hoka ranked below Crocs): $13.3k

The richest Facebook thread (about 87 user comments read).

- **Ranking credibility backlash:**
  - Facebook: "Hoka have less rating than crocs?? lols", "Hokas are the best brand! ... Businesses will say anything because of competition" (6 likes).
  - IG: Hoka praise piles up (29, 21 and 16 likes), with "AI strikes again lol" (8), "Ai -100" and "I would never buy these because the awful AI use".
- **Non-nurse workers feel excluded but want in:** retail, childcare, correctional officers (6 likes; they need all-black shoes that can shine), hairdressers, barbers, a busser, a flight attendant, warehouse and factory (steel toe, about 6), aged-care kitchens. In Spanish: "Yo quería comprar un par pero no soy enfermera 😪".
- **Men:** "These shoes are for only women. We have men nurses also"; "How about a shoe made for men Size13? I work in the hospital with the women!"
- **Owners:** "I've got 3 pairs soooo much better on my feet, no pain at all" (**10 likes**, the top comment), versus "the smell are awful the material is very cheap".
- **Read:** the shoe-ranking format drives engagement but costs credibility (Hoka loyalty plus AI detection). The "anyone on their feet" demand is large and goes unanswered by nurse-only framing.

### 5. RTGv1_B6, 203_Iteration_UGC_OrthoStretch (retargeting, Emily RN, 40% OFF): $12.6k

Largest comment pool (987 per Atria).

- **Facebook (about 87 read):** warm, mostly owners. "I have them, it's comfortable, and lightweight", "I used to change my shoes to my slippers ... Since wearing these I keep them on until I am getting in bed ... wiggle my toes", "Best shoes EVER, I have a pair in EVERY color", "Immediately my Planterfasilist felt much better ... I was not limping to my car."
- **Facebook complaints:** "hardest shoe to get on", "They will not take them back or give a refund", currency confusion (AUD vs USD), $59.95 doubled at checkout, "Are the sole's plastic?"
- **Instagram (about 86 read):** about 75% negative. The returns horror stories cluster here: Salvation Army or Red Cross donation receipts, credit only, 3%, 20% or 30% partial refunds, "sanitation reasons", "Will report this company to Better Business". Also "made my plantar fasciitis way worse", "I order 2 pairs and I get 10 dollars shoes", and "So, I buy the shoes but then need to purchase the insoles separately??? ... misleading".
- **Read:** retargeting audiences include past buyers, who use these ads as a complaint channel. The Instagram threads under the top retargeting ads now work as anti-testimonials. The fix is operational: honor the posted refund policy and moderate or respond on Instagram. A creative fix alone won't solve it.

---

## 9. Notes by persona

- **Nurses and healthcare** (RN, ER, CNA, therapists, 40-year and 50-year veterans)
  - Needs: 12-hour shifts, PF, back pain, compression socks with POTS, fluid-proof ("No one wants soaked socks during a code!"), slip-resistant, needle-resistant or leather uppers, all-black or fun colors.
  - Objections: mesh not allowed in hospitals, AI ads, Hoka loyalty, "most nurses sit at computers" pushback.
  - Male nurses can't find size 13.
  - Veterans validate the category ("Support stockings and good shoes. Been a nurse for 50 years. These work", 6 likes).
- **Teachers** (K-2, PreK, SpEd, paras, Home Ec, retired)
  - **Dress code is the number one barrier:** sneakers allowed only on Fridays or with a doctor's note. They want a dressy shoe, flat, heel or boot, with the same support. Recoloring the white midsole to match the upper would help.
  - The "standing still / 6 hours" hook offends; they walk 10 to 20k steps.
  - Other asks: recess duty in rain or snow, teacher discount, FSA (the brand says HSA/FSA works through Truemed).
  - A Hoka-loyal teacher volunteered to review the shoe for teacher friends.
- **Travel, Disney, cruise, Europe**
  - Step counts are a badge ("park day 35,000 steps"); cobblestones; rain; heat.
  - Heavy Hoka, On and Skechers defense.
  - Wants waterproof options and a white option.
- **Plus-size**
  - "Are they ok for heavy ppl that are on their feet a lot?"; a 2X commenter with RA wearing Hoka 10W wants more heel cushion.
  - A troll ("Fat") appears on the plus-size travel ad.
  - The ad title literally says "Plus-Sized Traveling", which is a risk of on-screen labeling.
- **60+, seniors, mobility**
  - 95-year-old mother, stroke plus heart failure, knee replacements (3 mentions), "spongy heel dangerous for seniors with balance issues", retired teachers and nurses.
  - They need stability messaging, not "cloud-like" messaging.
- **Neuropathy and diabetes**
  - "I need something good for neuropathy because I be in agony at work"; "I pray they help with my Neuropathy"; diabetics asking about a wide toe box and circulation.
  - The detractors are loud: "Yo tengo neuropatía y fibromialgia ... lastiman mucho ... Si tienes alguna condición médica NO LOS RECOMIENDO."
  - Ads claim "Relieves ... Neuropathy Pain" while brand replies hedge, which is a claims-risk gap.
- **Plantar fasciitis**
  - The most-asked condition. Outcomes are split: "Best shoes I got for my plantar fasciitis it's getting better" versus "I got planters fasciitis after using this shoe" and "made my plantar fasciitis way worse".
- **Blue-collar and service workers** (retail, warehouse, factory, kitchen, cafeteria, restaurant, cleaners, hair, casino, childcare, correctional officers)
  - They see nurse ads and ask "what about us?"
  - Their needs: steel toe, certified slip resistance, all-black uniform shoes, concrete floors.
  - Very strong in Spanish ads ("trabajo en cocina", "fábrica ... 12 horas de pie").
- **Spanish-speaking**
  - Kitchen and restaurant work, flat feet, diabetics, men's sizes.
  - Price shown versus checkout total ($59 to over $100).
  - The doctor actor is liked ("No está muy mal este señor", "es verdad lo que él dice").
- **Men**
  - Repeated "only for women?"; men's max of 10.5 or 11.5 is noticed; steel toe interest.
- **International** (Canada, Australia)
  - Currency confusion (USD charged), CA and AU size conversion, shipping to Canada.
- **Chronic and complex conditions** (EDS/hEDS, fibromyalgia, POTS, RA, Morton's, sciatica, a prosthesis)
  - High hope and high disappointment. The prosthesis owner could not fit it and was refused a return.

---

## 10. Language bank

Short verbatims. Typos are kept. Names are removed. Tags are theme, then ad concept, then platform.

1. "I've got 3 pairs soooo much better on my feet, no pain at all. I love them" — *praise/repeat*, Nurse Kyro390v1_H5, FB
2. "I used to change my shoes to my slippers the moment I got home. Since wearing these shoes, I keep them on until I am getting in bed." — *praise/all-day*, 203 UGC OrthoStretch, FB
3. "The shoes hug my feet, and I love being able to wiggle my toes!!" — *praise/toe box*, 203 UGC OrthoStretch, FB
4. "Immediately my Planterfasilist felt much better at the end of my shift ... I was not limping to my car. Try Them!" — *praise/PF*, 203 UGC OrthoStretch, FB
5. "First time in years my feet, legs, and back have not hurt by midday. I won't buy anything else from now on." — *praise/pain relief*, Kyro_293, FB
6. "I have two pairs and I love them. Big difference in feet, knees, hips and back." — *praise/pain relief*, Warning-task_Warehouse, FB
7. "I use to walk alot then I couldn't anymore, my husband bought me these to try I'm back walking again" — *praise/mobility*, SellingOut4Days, FB
8. "Best shoes EVER, I have a pair in EVERY color" — *praise/repeat*, 203 UGC OrthoStretch, FB
9. "I work 14 plus hours on my feet and they really help" — *praise/long shifts*, Ortho-Stretch #753 static, FB
10. "The purple ones rock..12 hours no problem." — *praise/long shifts*, Ortho-Stretch #753 static, FB
11. "I'm not a nurse… I'm a retail manager… the only shoes I can wear for 10+ hours" — *praise/non-nurse*, 203 UGC OrthoStretch, IG
12. "I bought a pair for my 95 year old Mother… she loves them!!" — *praise/gift, 60+*, Warning-task_Warehouse, FB
13. "Support stockings and good shoes. Been a nurse for 50 years. These work" — *praise/nurse*, COM296 Nurse quit drama, FB
14. "Super comfortable but hard to put on. Even with a shoe horn the inner sock is a challenge." — *complaint/donning*, Kyro369v2 travel, FB
15. "They are great once you get them on your feet. They are the hardest shoe to get on." — *complaint/donning*, 203 UGC OrthoStretch, FB
16. "kept tripping over the strings and stepping on the little plastic pieces" — *complaint/laces*, Ortho-Stretch #753 static, FB
17. "I rotated mine with other shoes and they fell apart within 6 months!" — *complaint/durability*, Ortho-Stretch #753 static, FB
18. "These offer no support ... my husband had to leave me sitting on a bench half way through our walk to go home and get the car" — *complaint/support*, Kyro_293, IG
19. "Shoes were like walking on cardboard NO SUPPORT!!" — *complaint/support*, 807 Don't Waste Spent Money, IG
20. "These are so uncomfortable and made my plantar fasciitis way worse! The refund policy is a complete lie" — *complaint/PF + refund*, 203 UGC OrthoStretch, IG
21. "Don't be fooled by the free returns. They use every excuse not to refund you." — *objection/returns*, Kyro_293, IG
22. "they said they can't take returns because of sanitation reasons and I needed to donate them ... so I am out $60" — *objection/returns*, 203 UGC OrthoStretch, IG
23. "Easy return? Now that's funny!!!! Donate to Salvation Army, send the donation receipt, maybe you'll get a credit for some socks or a pillow!!" — *objection/returns*, 203 UGC OrthoStretch, IG
24. "Better like em the return policy is misleading. They just want to give credits no actual return and refund" — *objection/returns*, Kyro369v2 travel, FB
25. "how can I test them out in the 30 days if I just walk around my house" — *objection/trial terms*, Warning-task_Warehouse, FB
26. "What's your warranty on these if I decide to try them? Brooks, Skechers and Hokas have a good warranty" — *objection/warranty vs competitors*, NurseNotRunners, FB
27. "All these comments are making my decision not to buy them way easier 😂" — *social proof flip*, Kyro_293, IG
28. "I almost ordered because of the advertisement, but I decided to read the feedback" — *social proof flip*, 203 UGC OrthoStretch, IG
29. "are these comments true or just to sell the product...someone pm me and be honest" — *objection/fake reviews*, Ortho-Stretch #753 static, FB
30. "If they are so wonderful why the recommended thick socks at check out?" — *objection/skeptic*, Kyro_293, FB
31. "Why are these shoes on so many sites" — *objection/dropship*, SellingOut4Days, FB
32. "I would never buy these because the awful AI use" — *objection/AI*, Nurse Kyro390v1_H5, IG
33. "Rating crocs above Hokas is wild 😂" — *objection/ranking credibility*, Nurse Kyro390v1_H5, IG
34. "Love my Hoka's. Wear them all day and no feet pain." — *competitor/Hoka*, Nurse Kyro390v1_H5, IG
35. "Kuru beats them all hands down" — *competitor/Kuru*, 807 Don't Waste Spent Money, IG
36. "I was fine with my sketchers but after wearing this my both feet aching" — *competitor/Skechers*, 203 UGC OrthoStretch, IG
37. "Except they're sneakers. What about dressier shoes for when we wear dresses or dress pants??" — *objection/dress code*, Teacher COM51, FB
38. "If I was allowed to wear jeans every day this would be great! But sneakers with slacks look tacky." — *objection/dress code*, Teacher COM51, FB
39. "I wear heels daily...now make those comfortable for teachers" — *objection/dress code*, Teacher COM51, FB
40. "Need a doctor's note to wear sneakers pretty much across the board." — *objection/dress code*, Teacher COM51, FB
41. "make the foam on the bottom that is white all the same color as the body of the shoe. It's very distracting." — *request/all-black*, Teacher COM51, FB
42. "Tell me you've never taught without telling me you've never taught. Trust me, we aren't standing still." — *hook mismatch*, JACK Teacher Hook1, FB
43. "A park day is 20,000 steps....lmao. My last park day was 35,000 steps." — *hook mismatch*, GeneralOverweightParkDay, FB
44. "if you built them for nurses, you wouldn't have made them mesh. No nurse is going to wear a mesh sneaker in the hospital." — *objection/work spec*, Nurse Kyro390v1_H5, IG
45. "BUT ARE THEY BODY FLUID PROOF?! No one wants soaked socks during a code!" — *question/fluid-proof*, COM204 Shoe ranking, FB
46. "Correctional Officer's feet need love too ... they have to be all black and able to shine the toe area." — *persona/CO + all-black*, Nurse Kyro390v1_H5, FB
47. "Yo quería comprar un par pero no soy enfermera 😪" — *persona exclusion*, Nurse Kyro390v1_H5, FB
48. "Tengo facitis plantar y trabajo en cocina qué me recomienda" — *question/kitchen PF*, COM225 Spanish, FB
49. "Me dice q $59 y al final más de 100" — *objection/price at checkout*, COM225 Spanish, FB
50. "They apparently only come in woman sizes. What about for male healthcare workers?" — *objection/men*, Nurse Kyro390v1_H5, FB
51. "Are they actually wide? The pictures don't look very wide and I have very wide feet." — *objection/width*, JACK Teacher Hook1, FB
52. "too bad I don't see it in extra wide I wear a 4E" — *objection/width*, Kyro_293, FB
53. "Too bad they're not waterproof" — *objection/waterproof*, Kyro369v2 travel, FB
54. "Having just comeback from a 14 day cruise to Spain and Portugal, I can attest that cobblestone fatigue is real." — *persona/travel pain*, Kyro369v2 travel, FB
55. "Do they have the soft spongy heel that seems all the rage now? The one that's so dangerous for seniors with balance issues." — *objection/stability, 60+*, 661 CustomerReviews static, FB
56. "I need something good for neuropathy because I be in agony at work" — *persona/neuropathy*, Nurse Kyro390v1_H5, FB
57. "I ordered these just now. I pray they help with my Neuropathy and it doesn't take a month to get here!" — *hope + shipping fear*, Nurse Kyro390v1_H5, FB
58. "So, I buy the shoes but then need to purchase the insoles separately??? ... your ad is completely misleading" — *objection/insole upsell*, 203 UGC OrthoStretch, IG
59. "Whats the name of them? I can never find" — *question/brand recall*, 203 UGC OrthoStretch, FB
60. "Can't get past the 'special offer'. I just want to see if there is a men's light color! Guess I'll look elsewhere!" — *funnel friction*, Kyro369v2 travel, FB

---

## 11. So what (for creative and ops)

1. **Fix refunds, or stop promising them.** "Free shipping & returns", "30-day" and "45-day risk-free" sit beside dozens of credit-only and donate-to-charity stories. This is the number one conversion killer on Instagram and on retargeting ads. Make the terms one consistent, honored policy, then answer Instagram comments the way Facebook comments are answered.
2. **Build creative for "I can't wear sneakers."** Teachers alone generated about 46 dress-code comments. Show an all-black version with a black sole, show it with slacks, and say "approved for dress codes" if true. If no dress model exists, stop targeting teachers with sneaker visuals.
3. **Broaden past nurses.** Retail, kitchen, factory, warehouse, cleaning, childcare and corrections workers are raising their hands. Write "anyone on their feet 10 to 12 hours" variants and Spanish kitchen and restaurant ads, and be precise about slip-resistant certification.
4. **Answer the top questions in the creative:** true wide (and men's sizes), waterproof or fluid-resistant, slip-resistant, the brand name on screen, and the real price at checkout.
5. **Stop picking fights with Hoka.** Rankings that bury Hoka draw likes for Hoka and "AI strikes again". Compare on fit, toe room and price instead ("Hoka-level comfort without the $160").
6. **Handle donning in the creative.** Demonstrate putting the shoe on easily, or fix the collar and laces. "Hard to get on" shows up even among people who love the shoe.
7. **Watch the claims.** "Relieves neuropathy pain" and "Podiatrist Recommended" sit next to "made my PF worse". Brand replies already hedge. Also review whether the reply page name "Asociación Nacional de Enfermeras Hispanas" implies an endorsement that doesn't exist.
