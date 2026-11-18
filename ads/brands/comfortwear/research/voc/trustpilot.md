# Trustpilot VoC: Comfort Wear (comfortorthowear.com) and competitors

Pulled 2026-11-18. Sources: StefanBrain `scrape_social_comments` (review text and dates, no star field) and `web_extract` of the Trustpilot pages, including the star-filtered pages (`?stars=1..5`), which show star ratings.
Raw files: `voc/raw/tp_ours500.csv` (our 500), `voc/raw/tp_comp.csv` (5 competitors x 100), `voc/raw/tp_extract*.txt` (page text with stars).

**How to read the numbers**
- The scraper does not return star ratings. Theme percentages come from tagging all 500 scraped reviews by keyword and then checking them against a full read-through. They are minimums, because a review can describe a problem without using any of the keywords.
- For sentiment, each review was tagged negative (121), mixed (42) or positive (337) from its text. This tagging is approximate.
- Star tags on quotes:
  - **★ = verified**: the quote came from a Trustpilot star-filtered page (1★ p1-2, 2★, 3★, 4★ and 5★ p1-2).
  - **~★ = inferred**: the quote is from the scraped CSV, and the rating is my estimate from the text.
- The 500 reviews run from 2025-12-19 to 2026-11-18. Trustpilot shows 530 reviews in the last 12 months, so this sample covers almost all of the past year.

---

## 1. Our page: headline numbers

| Item | Value |
|---|---|
| TrustScore | **3.7 / 5 ("Average")** |
| Total reviews | **3,151** (530 in last 12 months) |
| Star split | 5★ 52% · 4★ 21% · 3★ 4% · 2★ 2% · **1★ 21%** |
| Profile flags | Claimed Jan 2023 · "No recent history of asking for reviews" (Trustpilot notes this means the reviews may not be representative) · **"Hasn't replied to negative reviews"** |
| Trustpilot AI summary (545 reviews) | "Most reviewers were somewhat happy… simple online purchasing… items arrive promptly… extremely comfortable… helps reduce foot fatigue during long work shifts." Return policy: "**extremely frustrating and misleading**, reporting that support agents refuse…" |
| Top mention chips | Product, Quality, Order, Delivery service, **Return policy, Refund**, User experience, Customer service, Price, Response time |
| "People also looked at" | HIKE Footwear 3.5 (52K), Orthora Footwear 3.9 (3K), Resilia 4.5, Senarah 2.8, FlyHugz 3.0 |

The rating is bimodal. Almost nobody gives 2 or 3 stars: buyers either love the comfort or are angry about the return process.

---

## 2. Praise themes, ranked (share of all 500 reviews read; positive and mixed reviews)

| # | Theme | ~% of 500 | Notes |
|---|---|---|---|
| 1 | **Comfortable / "walking on clouds/air"** | 43% (213) | Usually the first word in 5★ reviews, often with "from day one" and "no break-in". |
| 2 | **All day on my feet / long shifts / concrete** | 15% (76) | Nurses, CNAs and CMAs, hospital and prison healthcare, hairstylists (for 39 years), teachers, restaurant workers, cleaners, dog walkers. "8 / 9½ / 10 / 12 / 14 hours." |
| 3 | **Helpful service on an exchange or wrong size** | 10% (48 positive) | Happy buyers mention a fast reply, a replacement size sent, or an e-gift card at 100%. Customers who wanted only an exchange are often satisfied. |
| 4 | **Looks / colors / "doesn't look like diabetic shoes"** | 9% (46) | Burgundy, red, black/aqua. "Attractive enough to wear anywhere." |
| 5 | **Easy ordering / arrived on time** | 8% (39) | Usually short 4 and 5★ reviews. |
| 6 | **Price / value / HSA-FSA accepted / veteran discount** | 7% (33) | "Cheaper than other named brand shoes." HSA/FSA eligibility is a real purchase driver. |
| 7 | **Wide, roomy toe box / wide feet / bunions** | 6% (31) | "Toe box looks narrow but isn't." "Truly wide fitting." Some reviewers say the opposite (see complaints). |
| 8 | **Lightweight / breathable / no sweating or swelling** | 5% (27) | "Feels like there is nothing there." |
| 9 | **Pain relief for a named condition** | 4% or more (19 by keyword; more on read-through) | Plantar fasciitis, diabetic neuropathy, arthritis, bunions and hammer toes, bone spurs, heel pain, knee and back pain, post-surgery ankles and legs. |
| 10 | **No-tie elastic laces / easy on and off** | 3% (14) | "Love the shoelaces, so easy to use!" "Not having to worry about my shoes coming untied." |
| 11 | **Travel use** (Italy, Paris, Hawaii, cruise, Europe cobblestones, dog-show fairground) | 3% (13) | Buyers bought for an upcoming trip. |
| 12 | **Stability / balance (seniors)** | 2% (9) | Buyers aged 77 and 78 cite "great balance and stability for my daily walks". |

## 3. Complaint themes, ranked (share of all 500 reviews read)

| # | Theme | ~% of 500 | What exactly |
|---|---|---|---|
| 1 | **Return / money-back guarantee not honored** | **~20% (98 negative reviews; 123 mention returns)** | This is the dominant 1★ driver. Reviewers describe the same sequence: (a) "why are you returning?", (b) "send a photo of the size label", (c) "wear them for 30/45 days", (d) **30%, 20% or 50% partial refund to keep them**, (e) **gift card or a different pair instead**, (f) "**donate to Salvation Army/Goodwill and send the receipt**", then (g) slow or no reply. Excuses quoted: "hygiene", "pro-sustainability", "a waste of material", "cost a lot of money to produce". Reviewers mention both 30-day and 45-day guarantees. |
| 2 | **Sizing inconsistent** | 18% (90; 28 in negative reviews) | Reported both ways: "way too big" and "a full size small". "EU sizes when received." Two pairs of the same size fit differently. "1 shoe way tighter than the other." People who bought the "size correction fee" or "correct size guarantee" still couldn't exchange. |
| 3 | **Partial-refund offers** (30%, 20%, 50%) | 10% (48) | Reviewers call this a "negotiation". |
| 4 | **Service unresponsive / runaround / scripted** | 8% (39) | "Phone goes to an automated recording that tells you to email." "Only respond once a day." "Seemed to be AI." One response per day, plus repeated questions. |
| 5 | **Cheap quality / chemical smell / plastic** | 7% (36) | "Smelled like chemicals." "Plastic knockoff." "Size number on the outside." "Looked unfinished." One reviewer froze the shoes to kill the smell. |
| 6 | **Hard to put on** (soft collar collapses, needs a shoe horn, narrow opening) | **7% (34), and 21 of these are in positive reviews** | A product issue that even fans raise: "comfortable once I get them on". High arches, wide feet, swollen feet, knee replacements. "Tongue comes up too far." |
| 7 | **Ships from China / slow delivery** | 7% (35) | "Didn't realize they were made in China." "I thought this was an American company!" 2-4 weeks. "No tracking." "Had to download another app." |
| 8 | **Donate-for-refund demand** | 7% (33) | Elderly buyers who can't drive, Quebec donation centres that don't issue slips, refunds not paid after donating. |
| 9 | **No support / no cushion / no structure** | 6% (28) | "I could fold the shoes in half." "Sock-type material on the sides." "Zero arch support." Nurses report knee and foot pain after 2 shifts. |
| 10 | **Not as advertised** (wide toe box narrow, not slip-resistant, "wing" stretch missing, color differs) | 4% (20) | "they ARE NOT slip resistant like they claim as I walked into work about about hit the floor" [sic] · "Toe box too narrow. False advertisement." |
| 11 | **Gift card / store credit instead of a refund** | 3% (17) | |
| 12 | **Chargeback / BBB complaint filed** | 3% (13) | "ComfortWear's BBB Score is an F." "BBB had 132 complaints." |
| 13 | **Heel lift pushes toes into the front** | 2% (10) | "The heel design pushes the foot forward and my toes pushed into the toe cap." This also appears in 3★ reviews. |
| 14 | **Packaging: plastic bag, no box** | 2% (9) | Some positive ("saves space"), some negative. |
| 15 | **Unwanted add-ons / charges** (compression socks, VIP membership, second charge, "free socks" charged $20) | 1% (6) | |
| 16 | **"Same shoes $20 on AliExpress / $22 on Amazon" / drop-ship** | 1% (6) | |
| 17 | **Wrong item or color sent** | 1% (5) | |
| 18 | **Order never arrived** | ~1% | One case in NZ, one in Flower Mound TX tracking. |

### Specific areas the brief asked about
- **Sizing**: this is the main product-side reason buyers start a return. Advice in reviews conflicts: "size up ½", "size down ½", "order 1-2 sizes larger". Buyers ask for a reliable size guide (one called the size chart "a bit off"). Socks change the fit noticeably.
- **Quality**: the split is stark. Fans say "well made", "sturdy" and "solid". Detractors say "cheap plastic", "chemical smell", "no structure" and "rock-hard heel bed". Lightweight and breathable are praised by both.
- **Shipping**: most reviews say it arrived on time or quickly. A sizable minority report 2-4 weeks, China origin, weak tracking, and paying for express without getting faster delivery.
- **Returns**: see complaint #1. This is the single biggest reputation problem. Several reviewers say they bought **because of** the guarantee ("I purchased these runners based on the company's 100% guarantee").
- **Service**: polar. Exchange requests are often handled well (agents praised by name; "replaced… at no extra cost"). Refund requests are scripted and slow. The phone line goes to voicemail or recordings.
- **Expectation vs ad**: buyers came via FB/Instagram ads, "your videos" and on-site reviews. Gaps they report:
  - toe box not as wide as shown
  - "slip-resistant" not true for some
  - "slip on easily" not true
  - color or look differs from photos
  - "orthotic" claim doubted
  - US brand image vs China shipping
  - suspicion that the 5★ reviews are "FAKE" or "AI"

  Positive surprise: "This is the first time I have purchased shoes that are exactly as advertised."

---

## 4. Competitor Trustpilot pages

| Brand | Score | Reviews | Star split (5/4/3/2/1) | Review-solicitation / replies |
|---|---|---|---|---|
| **Kuru** (kurufootwear.com) | **4.8 Excellent** | 964 | 84 / 2 / 2 / 2 / 10 | No recent invitations; **replied to 100% of negatives** |
| **Orthofeet** (orthofeet.com) | **4.4 Excellent** | 39,097 | 77 / 8 / 6 / 3 / 6 | Invites reviews; hasn't replied to negatives |
| **Stepprs** (stepprs.com; insoles) | 3.8 Great | 3,192 | 57 / 8 / 5 / 5 / 25 | Invites; replied to 60% of negatives (within 2 weeks) |
| **HIKE Footwear** (hike-footwear.com) | 3.5 Average | **51,552** | 55 / 9 / 6 / 5 / 25 | Invites; **replied to 99% of negatives within 24h** |
| **OrthoFit** (orthofitstore.com) | **1.1 Bad** | 323 | n/a | Unclaimed; Trustpilot notes the "website has closed" |
| (Comfort Wear, for reference) | 3.7 Average | 3,151 | 52 / 21 / 4 / 2 / 21 | No invitations; no replies to negatives |

The 100 most recent reviews per brand were scraped. I read about 45 per brand in full and keyword-scanned all 100.

**HIKE Footwear** (closest model: FB-ad comfort shoe; 20 of 100 reviews hit negative keywords)
- *Praise*:
  - barefoot/ground feel
  - **balance and stability**: "I have not fallen once", "can step off a curb without looking for a pole", diabetic neuropathy, hip replacement
  - wide toe space
  - lightweight
  - morning heel pain gone
  - easy on with a stiff heel
  - price/deals
  - frequent order updates
- *Complaints*:
  - returns are hard: they reply "give shoes away"; on YouTube, "clearance shoes cannot be returned"
  - no phone
  - long back-and-forth
  - "size up" advice backfires
  - ships from overseas
  - not enough cushion for plantar fasciitis
  - "look and feel just like water shoes"
  - can't tighten the laces

  Trustpilot AI summary: "exceptionally lightweight, comfortable… practical wide toe box… return policy… frustrating."

**Stepprs** (insole; 15 of 100 negative)
- *Praise*:
  - customer service praised by agent name (Charli, Kelly, Monique, Ash, Martha)
  - "like walking on thick pillows"
  - plantar fasciitis and neuropathy relief
  - warehouse workers
  - fast problem fixing
- *Complaints*:
  - delays or "never delivered"
  - ad misleading: "you were showing the two insoles on top of each other"
  - don't fit every shoe
  - price dropped after purchase
  - deceptive checkout upsell (AI-summary snippet)
  - "the inserts are just ok"

**OrthoFit** (cautionary tale; 91 of 100 negative)
- name confusion with Orthofeet ("Do not confuse this China based business with Orthofeet")
- ad showed HOKA shoes
- ships from China in 3-6 weeks, eating the 30-day window
- returns must go to China ($30 to $200+)
- "double order scam"
- $4-5 store-credit offers
- chemical smell and "crunchy" material
- hard plastic soles
- emails claiming 5★ on Trustpilot

This is the same complaint pattern as Comfort Wear's 1★ reviews, at a more extreme level.

**Orthofeet** (23 of 100 with negative keywords, mostly mild)
- *Praise*:
  - support
  - **true wide widths** for "square feet"
  - quality that lasts
  - easy exchanges and returns ("made it soo easy")
  - slip-in styles ("Made the mistake last time of buying tie sneakers!")
  - included inserts
  - stylish
  - repeat buyers for over 10 years
- *Complaints*:
  - expensive ("wait until a sale")
  - "clunky and boxy"
  - heavier
  - some say "no better than any other shoe"

**Kuru** (28 of 100 with negative keywords; the period sampled skews toward service interactions)
- *Praise*:
  - **customer service with real people** ("Kuru Gurus")
  - **90-day wear-test return** ("unheard of")
  - free replacement insoles
  - easy exchanges with a QR code
  - comfort and help with plantar fasciitis
- *Complaints*:
  - **durability at about $200** (stitching, lace loops breaking, sole separating, "can't make it through a season")
  - "waterproof" Atom got soaked
  - stock availability

**Takeaway**: the top-rated brands (Kuru, Orthofeet) win on **easy, honest returns and exchanges**, not only on product. Hike and Stepprs keep 3.5-3.8 despite a 25% 1★ share by inviting reviews and replying to every negative. Comfort Wear does neither.

---

## 5. Verbatim quotes (no reviewer names)

### Praise
1. "As a nurse I would have to say, these are great shoes at a great price." (Nurse, value) ~5★
2. "I work 12 hour shifts and my feet and back don't hurt." (12h shift, back pain) ~5★
3. "Got my shoes with 8 business days and they are wonderful! They fit my extra wide feet perfectly, and I can work my 12 hours shift without horrible pain." (Wide feet, 12h) ~5★
4. "I have nerve pain in my feet from my diabetes, and these shoes are the only shoes I've put on that didn't make the pain worse." (Neuropathy) ~5★
5. "I have arthritis in my feet and it's very difficult to find anything that I can walk in… These are the best so far." (Senior, arthritis, price on a fixed income) **5★**
6. "At first I thought they would look like diabetic shoes, but to my surprise they are really nice looking." (Looks/style) **5★**
7. "Ordering was easy, HSA accepted, timely delivery and the shoes are great!" (HSA) **5★**
8. "I told my sister about how comfortable the shoes are and she is a RN too. Long days on our feet." (Nurse, word of mouth) **5★**
9. "First time my feet haven't hurt in years after standing all day long!" (Travel/trial, dog-show fairground) **5★**
10. "These shoes are miraculous! I wish Id never spent $350 on inserts from the doctor!" (Hairstylist, vs custom orthotics) ~5★
11. "I have bunions and balance issues...my new shoes made me forget my feet have any issues." (Bunions, balance) ~5★
12. "The stretch material helped alleviate friction to my bunion." (Bunion, stretch knit) ~5★
13. "There is plenty of room for my feet to expand(swell) in my 8 hr. Shift." (Swelling) ~5★
14. "At 78 y.o. … They gave me great balance and stability for my daily walks." (Senior, stability) ~5★
15. "Love the non-slip bottom and most of all, my feet didn't hurt after day 1!" (No break-in, slip-resistant) ~5★
16. "The toe box looks narrow but isn't at all. Plenty of room for your toes to wiggle around." (Toe box) ~5★
17. "These are the most comfortable shoes I have ever worn and been working in restaurants for years!" (Restaurant worker) ~5★
18. "I'm a CMA… today is the first day I haven't limped in 2 months." (Healthcare, knees) ~5★
19. "I was pleasantly surprised that they provided the needed relief of my plantar facititis." (Plantar fasciitis) ~5★
20. "This is the first time I have purschased shoes that are excatly as advertised." (Expectation met) ~5★
21. "Saw your ad on FB… Who knew if these were real or fake… I will be taking it with me as I travel Europe." (FB-ad skepticism, travel) ~4-5★
22. "comfortable enough to wear for an 8 hour work day, on concrete floors!! Kudos, ComfortWear, for making shoes that are true to my feet width, size, and arch" (Concrete, fit) ~5★

### Mixed (product and fit)
23. "The shoes are beautiful. I had a hard time getting my left foot in shoe… LOVE the shoelaces, so easy to use!" (Hard to put on, laces) **4★**
24. "So far so good… the wide fit is good but as shoe goes towards toes it tapers too much for my sore feet." (Toe taper) **4★**
25. "The heel padding is too high and pushes my toes forward to a tight fit despite the wide toe box. Also there is little arch support." (Heel lift) **3★**
26. "I find the shoes difficult to get on depending on what type of sock I'm wearing." (Hard to put on) **3★**
27. "The shoes are nice but I had to put an insole in them to wear all day at work." (Support) **3★**
28. "They feel great once on but boy do I struggle in the process." (Hard to put on) ~4★
29. "Very comfortable and less pain but they for sure don't last all day… my feet start to hurt around 7 hours in." (Long shifts) ~3-4★

### Complaints
30. "As a nurse I'm on my feet a lot… This is not a better shoe… this 8.5 was more like a 9." (Nurse, sizing) **2★**
31. "Toe box too narrow. False advertisement" (Not as advertised) **1★**
32. "They promised that they had 'wing' sized around the wide part of the foot… that technology was not there." (Wide-fit claim) **2★**
33. "Here's the thing. The shoes have NO structure. What gives this shoe stability?" (Support/quality) **2★**
34. "I was very excited to receive the shoes- great reviews.... I think they ALL must be FAKE." (Review trust) **2★**
35. "They do ship from China. They won't let me return even though they say we have 45 return policy." (FB ad, returns) **2★**
36. "Then they asked if I would take a 30 per cent refund. I said no. Still waiting for instructions on how to return." (Returns) **1★**
37. "Customer service… suggested I donate the sneakers… After donating… I never heard from ComfortWear again." (Donate-for-refund) **1★**
38. "I bought what was supposed to be a stretch fit shoe… I can't get my feet into them!" (Stretch claim, hard to put on) **1★**
39. "Looking up the shoes, they go for under $20 on aliexpress, FOR THE SAME SHOES they're selling for $60+" (Drop-ship) **1★**
40. "I could fold the shoes in half… I bought them for plantar fasciitis." (No support, plantar fasciitis) **1★**
41. "they ARE NOT slip resistant like they claim as I walked into work about about hit the floor" [sic] (Slip-resistance claim) ~1★
42. "I am an elderly person who uses pickups to donate so this is inconvenient." (Senior, donate demand) ~1★
43. "For us, it would be a shame and a waste of material…" (Customer-service script, quoted by a reviewer) ~1★
44. "As a nurse, I rely on comfortable and supportive shoes to get through long, 12-hour shifts… I experienced significant knee and foot pain." (Nurse, support) ~1★
45. "I cannot even put these on my feet, both knees replaced and since they don't lace up…" (Senior, hard to put on) ~1★
46. "Not everything advertised on Instagram is real" (Ad trust) ~1★
47. "They are advertised as being good shoes to wear all day as a nurse. I'm not sure if that's true." (Nurse claim, arthritic knees) ~3★
48. "ComfortWear's BBB Score is an F!!" (Trust) ~1★

### Competitor quotes
49. "As someone with beginning diabetic neuropathy and numerous falls… I have not fallen once since wearing my Hike shoes." (Hike, balance)
50. "In the video you show that they are thick insoles but when I received them… you were showing the two insoles on top of each other" (Stepprs, ad mismatch)
51. "The 90 day return policy after wearing is unheard of. Koodoos to Kuru." (Kuru, returns)
52. "It doesn't make it any better that the $200 shoes can't make it through a season before falling apart." (Kuru, durability)
53. "Love thr true Wide for my square feet!" (Orthofeet, width)
54. "Do not confuse this China based business with Orthofeet." (OrthoFit, name confusion)
55. "Their boots took 29 days to ship, nearly consuming the entire 30-day return window" (OrthoFit, shipping vs return window)
