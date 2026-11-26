# Comfort Wear: customer feedback mined for long-form angles

Source: Google Sheet "ComfortWear Customer Feedback (Responses)" (fileId 1qX2aoUaOvjqh40EQkhY3kYNcgm1nj2Lpjybes2J6FKI), tab "Form Responses 1". Read-only: it was exported to CSV and analyzed locally, and the sheet was not changed.
**Coverage: 100% of rows (18,493 responses).** Counts come from keyword classification of every row. Quotes come from a full read of the ~600 long answers (80+ characters) from customers who rated comfort 4–5, plus keyword pulls across all ~14,000 answers of 40+ characters. The sheet holds emails and order numbers, so none are reproduced here.

Cross-checked against `research/analysis.md` §4 (Trustpilot), §9 (survey) and §11 (personas). Anything already listed there is marked "known".

---

## 1. What the sheet contains

- **18,493 responses, 15 Apr 2023 → 11 Nov 2026.** The last response is from today, so the form is still live. By year: 2023 1,748; 2024 4,406; 2025 8,892; 2026 3,447.
- **16 columns (A–P).** The form changed over time, so most questions only exist for part of the range:

| Col | Question | Filled | Live from → to |
|---|---|---|---|
| A | Timestamp | 18,493 | whole range |
| B | How comfortable were our shoes? (1–5) | 18,493 | whole range |
| C | How was your experience with our website? (1–5) | 1,974 | Apr 2023 → Jan 2024 |
| D | What foot problem do you have? (choice + Other) | 18,490 | whole range |
| E | Where did you find us? | 18,491 | whole range |
| F | "What is your order # or email?" (**in practice a free-text "what should we improve" box**) | 2,681 | Apr 2023 → Apr 2024 |
| G | What is the #1 reason you purchased our shoes? (free text) | 18,004 | Jul 2023 → now |
| H | What is your job? (free text) | 18,003 | Jul 2023 → now |
| I | Shoe size (v1) | 900 | Jan → Apr 2024 |
| J | What are you looking for when buying shoes? (free text) | 15,712 | Jan 2024 → now |
| K | How was the size you received? | 15,559 | Apr 2024 → now |
| L | Shoe size (v2) | 15,554 | Apr 2024 → now |
| M | Current solution for foot pain or comfort? (free text) | 12,620 | Aug 2024 → now |
| N | Age (bands) | 7,437 | Jun 2025 → now |
| O | What other product should we start selling? | 2,040 | Nov 2025 → now |
| P | What industry do you work in? | 0 | never used |

- **Comfort ratings:** 1 = 8,444 (46%), 2 = 3,170, 3 = 2,817, 4 = 1,435, 5 = 2,627. **22% (4,062) rated comfort 4–5.** analysis.md calls this a "1–3★ only" survey. The low-star bias is real, but a fifth of respondents liked the shoe and were unhappy about something else (usually shipping or returns). Those 4,062 are where the story material is.
- **Where they found us:** Facebook 62.7%, Google 17.5%, word of mouth 2.3%, Instagram 2.2%, plus a few dozen each for YouTube, "game ad" and email.

## 2. Counts

### Jobs (column H, n = 18,003; keyword buckets can overlap)
| Job | n | % |
|---|---|---|
| Retired | 4,734 | 26.3 |
| Nurse / RN / LPN | 1,803 | 10.0 |
| Other healthcare (MA, tech, pharmacy, dental, therapist, hospital) | 1,790 | 9.9 |
| Retail / cashier / sales / grocery | 1,680 | 9.3 |
| Food service (server, cook, bartender, restaurant) | 1,252 | 7.0 |
| Office / admin / manager | 1,138 | 6.3 |
| Teacher / education / para | 1,037 | 5.8 |
| CNA / aide / caregiver / home health | 443 | 2.5 |
| Disabled / unemployed / none | 432 | 2.4 |
| Housekeeping / cleaning / janitor | 396 | 2.2 |
| Warehouse / factory | 363 | 2.0 |
| Security / police / postal / driver | 270 | 1.5 |
| Homemaker / stay-at-home | 245 | 1.4 |
| Hair / beauty | 166 | 0.9 |
| Church / volunteer | 155 | 0.9 |

**New finding: 1,327 of the 3,461 respondents aged 65+ (38%) give a working job, not "retired".** The top ones are nurse, cashier, teacher, retail, RN, caregiver, cook, realtor, customer service and bartender. Their comfort score (2.26) is close to retired 65+ respondents (2.35).

### Ages (column N, n = 7,437, Jun 2025 onward): known
65+ 46.5% · 50–65 38.5% · 40–50 10.0% · 30–40 3.7% · 20–30 1.3%

### Foot problems (column D, n = 18,490)
Plantar fasciitis 26.0% · "no foot pain, only need comfort" 23.5% · arthritis 11.8% · neuropathy 10.8% · bunions 8.3% · flat feet / fallen arch 1.7% · heel pain or spurs 1.6% · knee/back/hip 1.5% · Morton's neuroma 1.4% · Achilles 0.8% · high arch 0.8% · wide feet 0.7% · foot surgery/fusion/amputation 0.7% · hammer toe 0.5% · swelling/edema 0.3%.

### What they wore or used before (column M, n = 12,620)
- **Named brands:** Skechers 324 · Hoka 281 · Brooks 125 · New Balance 83 · Crocs 53 · Orthofeet 45 · On/Cloud ~38 · Oofos 34 · Vionic 32 · Nike 31 · Good Feet Store 30 · Asics 26 · Dr. Scholl's 26 · Dansko 25 · Birkenstock 22 · Kuru 15 · Altra 11 · Saucony 10 · Ryka 10 · Clarks 8. Single mentions include Keen, Sanita, True Grit, Brooks Ultra/"Torin" (Altra), Grounded barefoot shoes, "Wal-Mart shoes" and steel-toe boots.
- **Other fixes:** "good/supportive shoes" generally 10.7% · insoles/inserts 8.3% · "still looking / nothing works" 6.5% · stretching, massage, ice, Epsom soaks 6.3% · barefoot, rest, putting feet up 3.5% · Tylenol, ibuprofen and other painkillers 3.4% · custom orthotics 2.3% · podiatrist, injections or PT 1.8% · night splints, braces or compression 1.8% · creams, CBD or Biofreeze 1.6%.

### Life moments (all free-text columns; rows mentioning)
| Moment | Rows |
|---|---|
| Standing all day / long shift at work (G alone) | 2,168 |
| Walking for exercise or daily walking (G alone) | 1,304 |
| Grocery, deli, Walmart, Costco or Amazon worker | 644 |
| Travel (vacation, trip, cruise, Europe, Hawaii) | 365 |
| Concrete or cement floors | 325 |
| After surgery or a broken foot/ankle | 284 |
| Balance or fear of falling | 211 |
| Swelling by end of day | 150 |
| Bought as a gift (G alone) | 93 |
| Spanish-language answers | 91 |
| Dog walking | 74 |
| Bought for a daughter | 73 |
| Volunteering (hospital, food pantry, library, shelter, camp) | 67 |
| Walks a stated number of miles or steps a day | 67 |
| Double shifts, two jobs, 16-hour days, 6–7 days a week | 58 |
| Bought for husband, wife, mom or friend | 49 |
| Grandkids (babysitting, chasing, school bus) | 36 |
| Old brand "only lasts N months" | 29 |
| Cobblestones or uneven streets (Italy, Greece, Paris, Edinburgh) | 28 |
| Casino floor workers | 27 |
| Airport, TSA or cruise port | 21 |
| Disney/Disneyland or a theme park | 9 |

## 3. Verbatim quotes for hooks and story beats

Spelling is the customer's own. Format: job / age band / comfort score.

1. "I am 72 years old . I am on my feet all night . I need shoes that are supportive. Since I'm only 4 foot 8 inches tall, I'm always looking for shoes that will give me a boost." (deli, grocery store, c5)
2. "Usually I work alone because of our shortage of staff. That means that I am running back and forth between slicing meat and serving salads… By the end of the evening my feet are noticeably larger." (same deli worker, c5)
3. "My shoes hurt my feet. I'm almost 70 and work in a restaurant. I walk several miles." (dining room attendant, c5)
4. "12 hours without pain… Before these I couldn't wait to get shows off. Now they stay on til I go to bed." (retail, c5)
5. "I purchased them because every other shoes and sneekers hurt to walk in except Comfort wear I took my brace off and put those shoes on as as soon as the mailman placed them in my hand to see if they really worked and they did!" (admin assistant, Achilles sprain, c5)
6. "Had 3 surgeries on right foot making it a different size than left foot. Yet one pair was roomy enough for the larger foot and just right for the smaller one!" (retired but active, 65+, c5)
7. "My bunion surgery went bad so my toes are not straight. I needed a supportive walking shoe easy to put on that had a wide toe box and helps balance. I'm 81 years old." (retired, c5)
8. "My Middle toe is longer than my big toe. Every shoe I have ever purchased has been a problem, until now!" (retired, two volunteer jobs, 65+, c5)
9. "I am retired, but I go up and downstairs two flights to take my grandchild to the school bus" / "Take Tylenol and try not to go down those stairs too much" (retired, 65+, c4)
10. "To see if it would help with my plantar fasciitis which it did , can now climb the stairs without any problem." (caregiver, 50–65, c5)
11. "My daughter's birthday present. She is a Marine & her feet/knees hurt from training the troops." (therapist, c5)
12. "They were purchased for my daughter who is a CNA. She's on her feet 10 hours and many times longer if she works a double shift. She loves these shoes." (c5)
13. "I bought the shoes for my Wife. She loves them and is considering ordering a bundle. They reduced pain and swelling in her legs and feet. The next order is for me!" (retired, 65+, c5)
14. "I'm in my 70's, walk 3 miles per day, 6 days per week in all kinds of weather. Need a shoe that provides support and stability." (retired educator, c5)
15. "Good walking shoes I'm older but I walk my dog about 3 Mi a day and if the shoes aren't Orthopedic my feet will hurt" (retired, 65+, c4)
16. "I am now retired but I have to walk my dog now that I live in an apartment four times a day." (retired, bunions removed, c4)
17. "Hip pain and these shoes have alleviated at least 70 % of my pain and I previously had been in agony....I just turned 70 and honestly the moment I put these shoes on they were the most comfortable shoes that I have worn" (retired, c5)
18. "I work an 8 hour day on concrete floors . With in 4 hours my back is on fire ! … I'm praying your shoes help !" (food prep, c5)
19. "Working in the fast food hospitality industry with bad shoes has been a nightmare for my feet. Puss leaking toe nails and bruising, aching pains making it hard to walk." (fast food, c5)
20. "Work fast food for 35 years and this is the best my feet has been" (fast food, c5)
21. "Was hoping for comfort and able to do my 16hour days without tears" (restaurant, 30–40, c3)
22. "Grocery store - deli worker and cleaning lady. I work 67 - 72 hrs , 7 days a week" (50–65, c5)
23. "I was in extreme pain. I felt as if I was stepping on a nail with my heel… My dad was also having the same symptoms so I told him I would order a pair for him. … I like to match my shoes to my clothes." (teacher, c5)
24. "Have been buying sketchers for years. Love their shoes.but they only seem to last 2 1/2 - 3 months." (retail, c4)
25. "I used Sketchers shoes for about 14 years but they discontinued a lot of their work shoes. They're regular are meh." (bartender, 40–50, c4)
26. "Spending hours a day working in Aged Care, walking kilometres a day, I could barely walk in brand name sneakers after work & into the next day." (aged care, c5)
27. "Shoes aren't my friends anymore , but our shoes re very friendly and comfortable." (DSP at an adult group home, c5)
28. "I'm a chef, and couldn't find any shoes that were comfortable enough to last 8-10hours a day." (chef, c5)
29. "Im runnimg like 27 machines on concrete feom 11 to 7am and I really need something very comfortable foe mu feet" (factory night shift, c4)
30. "Retired except work as a day for 10 hours shifts 5 days a week x 7 weeks in health center of an coed overnight summer camp" (retired nurse, c5)
31. "I volunteer at our Hospital, and am on my feet for a 3 plus hour shift...and would like my feet to be comfortable...because then my shift doesn't tire me out!" (retired high-school teacher, c4)
32. "I'm going to Edinburgh, Scotland with a lot of cobblestones… walking out a lot of cobblestones between Scotland and Ireland" (systems analyst, 65+, c3)
33. "I walk and take the bus everywhere. I'm in a walker and just needed shoes that would be comfortable the whole time I was out running around." (c5)
34. "Since this product was made for nurses by nurses i felt i needed to support my fellow nurses.no one else knows what its like for us but them." (LPN, c4; see the claims warning in §5)
35. "Was a lucky moment. Had bunion surgery and needed confort immediately and saw your shoes… so far the best shoe I have ever purchased . Love the fit....the color ( my favorite by the way)." (dealership, c5)
36. "Sentía dolor en el talón y no podía firmar bien para caminar… Tan pronto los empecé a usar ADIOS dolor" (homemaker, Spanish, c5)
37. "Porque tengo la esperanza de que tu zapato me ayude con este dolor de mis talones porque ninguno zapato me a ayudado hasta hoy" (grandmother caring for grandkids, c5)
38. "It was food safety but I lost my career due to my lack of balance and concern of liability." (65+, c4: a balance/fear-of-falling stake)
39. "I have a love hate relationship with these shoes. They are VERY difficult to put on. They are comfortable once they are on." (retired, c5: the main objection in one line)

## 4. Candidate long-form angles we have NOT used

None of these repeats the Disney grandma, the ER nurse shoe graveyard, the Lisbon anniversary or the Christmas night nurse. Where a static concept or persona row already exists in analysis.md, it says so. None of these has been written as long-form.

### A1. "Still on the clock at 72": the 65+ woman who never got to retire
- **Persona:** a woman aged 68–75 who still works a standing job (deli, cashier, restaurant floor, retail) because she has to.
- **Situation and trigger:** a short-staffed shift where she works alone. She comes home with feet "noticeably larger" and her daughter says "Mom, you can't keep doing this."
- **Core pain:** her body is 70 but the shift is still 8–9 hours. Swelling, heel pain, and fear that her feet will force her to quit.
- **Wrong-shoe enemy:** the cheap store-brand sneaker she replaces every few months, or "nurse shoes" that are too stiff and heavy for her.
- **Story seed:** at 4'8" she's running between the meat slicer and the salad case alone at 9 pm, and for the first time in years she doesn't count the minutes until she can sit in the car.
- **Supporting quotes:** #1, #2, #3, #22.
- **Frequency:** 1,327 working respondents aged 65+ (38% of that age band); the largest unclaimed group in the data. It's the opposite of concept C23 ("Retired from 12-hour shifts"), and the two can coexist.

### A2. "She's my daughter, and she's limping": the mom who buys for her working daughter
- **Persona:** a mother aged 55–75 who buys for her adult daughter (CNA, nurse, server, Marine, retail night shift). She is often a former nurse herself.
- **Situation and trigger:** the daughter visits after a double shift and kicks her shoes off at the door, or her birthday or Christmas is coming up.
- **Core pain:** watching your child go through the same foot pain you did, and knowing she won't spend money on herself.
- **Wrong-shoe enemy:** the daughter's worn-out Walmart work shoes or "whatever was on sale".
- **Story seed:** a retired nurse sees her CNA daughter sitting in the car in the driveway after a double, too sore to walk inside, and orders two pairs that night: one for the daughter, and one, she admits, for herself.
- **Supporting quotes:** #11, #12, #13, plus "My daughter works 12hrs every night as a nurse"; "My neice needed Orthopedic shoes and wouldn't buy them so. I ordered these for her an got a pair for myself."
- **Frequency:** 73 for a daughter, 49 for a spouse or parent, 93 "gift" in column G (about 200 rows). The volume is small, but it brings in a new buyer: a 55+ Facebook user buying for a younger worker. analysis.md lists "adult child buying for a parent", and this is the reverse direction.

### A3. "The day the brace came off": recovering from foot surgery or a fracture
- **Persona:** a woman aged 50–80 with a broken ankle, bunion surgery, fusion hardware, or a foot that never healed right ("one foot different size").
- **Situation and trigger:** the surgeon clears her out of the boot or brace, and every shoe she owns hurts the healed foot.
- **Core pain:** she's afraid to walk normally again. Shoes rub the scar or the bone, and her two feet are different sizes now.
- **Wrong-shoe enemy:** the post-op boot, and the shoes in her closet from "before".
- **Story seed:** she takes the brace off on the porch the minute the mail carrier hands her the box and walks to the mailbox and back without holding the rail.
- **Supporting quotes:** #5, #6, #7, #35, plus "I broke my ankle almost 3 years ago and had surgery… shoes can be painful"; "Had surgery on both feet and haven't found a shoe that gives me support and comfort until now."
- **Frequency:** 284 rows. Not in analysis.md.
- **Care:** no medical claims. Do not say "doctor-recommended for recovery" or "approved post-surgery". Keep it to her own experience.

### A4. "Two flights to the school bus": the full-time grandma
- **Persona:** a retired grandmother aged 62–78 who watches the grandkids every weekday: school runs, stairs, chasing toddlers. This is daily routine, not a vacation.
- **Situation and trigger:** her son or daughter goes back to work and she becomes the childcare, or a stair-filled apartment.
- **Core pain:** knee and heel pain on stairs. She takes Tylenol before the school run and worries she can't keep up or will fall while holding a child.
- **Wrong-shoe enemy:** slippers and flat canvas sneakers ("I wear them because they're easy to get on").
- **Story seed:** every morning at 7:40 she takes the stairs one at a time, holding the rail and her grandson's hand, until the morning he says "Grandma, you're fast today."
- **Supporting quotes:** #9, #10, #37, plus "A 74 year old grandmother who takes car of her grandchild every day!"; "Retired with many grandchildren to chase after."; "Retired but care for disabled spouse and babysit great grandchildren!!"
- **Frequency:** 36 grandkid rows, 8 stairs, and many more under "retired" with no detail. This is a specific scene inside the largest segment (retired, 26%), and it differs from the Disney grandma.

### A5. "Retired nurse, still on her feet for free": the volunteer
- **Persona:** a retired nurse or teacher, 65+, who volunteers (hospital, food pantry, animal shelter, library, summer camp health center).
- **Situation and trigger:** a volunteer shift on concrete. She notices she's more tired after 3 hours of volunteering than she was after a 12-hour shift at 40.
- **Core pain:** pride, and not wanting to give up the thing that keeps her useful.
- **Wrong-shoe enemy:** the old nursing clogs she kept "because they were good enough then", or Hokas that are too pricey to replace.
- **Story seed:** 30 years as an ER nurse, and what nearly made her quit was a 3-hour Thursday shift at the food pantry.
- **Supporting quotes:** #30, #31, #8, plus "Retired RN. Now volunteer at hospital and animal shelter"; "I run a food pantry, and walking all day on concrete flooring"; "After retiring I chose to help at a clinic and on those days I'm on my feet for at least 8 hours."
- **Frequency:** 67 volunteer rows. Retired healthcare and teacher answers are common ("Retired nurse" alone 62 in column H). It extends the nurse winner into the 65+ majority, and the static concept C23 points the same way.

### A6. "Three miles, six days a week, any weather": the 70+ daily walker and dog walker
- **Persona:** a woman aged 68–86 whose daily walk (often with the dog) is her health plan.
- **Situation and trigger:** the doctor says "keep walking" after a knee surgery or a weight-loss goal, or the dog needs walking four times a day after a move to an apartment.
- **Core pain:** if her feet hurt she stops walking, and if she stops walking she knows what comes next.
- **Wrong-shoe enemy:** heavy "walking shoes" that feel like bricks, and the old pair worn down at the heel.
- **Story seed:** at 86, the only thing on her calendar every single day is the dog, and she's not about to let her feet cancel it.
- **Supporting quotes:** #14, #15, #16, #17, plus "86 years of age… Just good fitting shoes for walking my dog!"; "I had knee surgery and I'm trying to walk more to lose weight."
- **Frequency:** dog 74, stated miles/steps 67, and "walking" as the #1 reason 1,304. It differs from the GLP-1/"20,000 steps" winner because the motivation is independence, not weight.

### A7. "Skechers every 3 months, Hokas at $160": the replacement treadmill
- **Persona:** a working woman aged 40–65 (retail, bartender, salon owner, pet sitter) who has a go-to brand and keeps paying for it.
- **Situation and trigger:** the brand discontinues her work shoe ("14 years of Skechers"), or her receipt shows a fourth pair this year.
- **Core pain:** spending money she doesn't have, plus loyalty to a brand that isn't loyal back.
- **Wrong-shoe enemy:** named by customers: Skechers memory foam (324 mentions) and Hoka (281). Name them only as a category ("the big-name memory-foam sneaker", "the $150 running shoe"), not as trademarks.
- **Story seed:** she lines up the receipts on the kitchen table, four pairs of the same sneaker in 12 months, and does the math.
- **Supporting quotes:** #24, #25, #26, plus "Skechers memory foams air cooled shoes the only thing is i have to buy a new set every 5months"; "Have been wearing Hokas ~2 years, want to find similar comfort and stability at a more reasonable price."; "Your pricing made trying them a no brainer."
- **Frequency:** brand mentions about 1,200 in total; lifespan complaints 29.
- **Care:** do NOT claim ours lasts longer. 204 rows complain about cheap quality or falling apart. Make it a price and comfort angle ("try it for the price of half a pair"), not a durability one.

### A8. "Every shoe I've ever bought has been a problem": the odd-shaped foot
- **Persona:** a woman aged 50–80 with a foot shape no shoe fits: middle toe longer than the big toe, crooked healed toes, one foot bigger, scoliosis and leg-length difference, splayed or "Hawaiian" wide feet.
- **Situation and trigger:** one more shoe-store visit where nothing fits, or a wedding or event she needs real shoes for.
- **Core pain:** a lifetime of embarrassment ("I guess they just cater to the young ones"), toes rubbed raw, and a closet of shoes that "fit" in the store.
- **Wrong-shoe enemy:** narrow, pointed shoes and the store clerk who says "it'll stretch".
- **Story seed:** at 68 she wiggles all five toes inside a shoe for the first time she can remember and laughs out loud in the hallway.
- **Supporting quotes:** #6, #7, #8, plus "I have an scoliosis and one leg longer than the other… plenty of room to move your toes"; "You all weren't kidding when you said the toe box was spacious"; "I had a accident years ago and I broke a few toes, so they help me spread them out more."
- **Frequency:** "wide/toe room" is a top-3 "looking for" answer (766 in column J, 506 in column G). Bunions are 8.3%.
- **Care:** "wide toe box" is fine, but there is no wide-width size. 364 rows complain "not wide enough / need wide widths", so don't promise "fits extra-wide feet".

### A9. "The jackpot attendant": casino, airport and theme-park floor workers
- **Persona:** a woman aged 35–65 who walks a huge floor all shift: casino jackpot or cage attendant, airport crew, TSA, cruise-port agent, SeaWorld, usher.
- **Situation and trigger:** a holiday weekend or peak-season double where her smartwatch shows 9+ miles.
- **Core pain:** carpet over concrete, kneeling and squatting at machines, a dress code that bans running shoes, and heels that are "unbearable" by hour 9.
- **Wrong-shoe enemy:** black dress flats required by the dress code, or "hiking shoes, work shoes made for nurses and food service workers" swapped day to day.
- **Story seed:** on New Year's Eve at the casino, 1 a.m., the slot floor is packed, and she realizes she hasn't thought about her heels since 6.
- **Supporting quotes:** "The pain in my heels was unbearable and my job is walking more than 9 hours a day." (casino supervisor); "Arch support, ankle freedom (no rubbing), good heel cushioning, wide toe box for squatting and kneeling." / "Different shoes for each day, hiking shoes, work shoes made for nurses and food service workers." (jackpot attendant); "Airport employee walking on concrete for 12 hours"; "I work for Tsa so I stand"; "I work as an agent for Intercruises. Boarding and unboarding cruise ship passengers."; "I work at SeaWorld… I'm on my feet a lot and I do a lot of walking"
- **Frequency:** about 48 named (casino 27, airport/TSA/cruise 21). It's small but vivid, and part of the 325 concrete-floor rows. Test it as a single ad, not a pillar.

### A10. "35 years of fast food": the veteran kitchen worker
- **Persona:** a woman aged 45–65 who has worked fast food, a deli or a school kitchen for decades ("31 years working for McDonald's", "pizza crust maker for 19 years").
- **Situation and trigger:** a new manager adds hours, or her toenails are bruised and she can't hide the limp from her grandkids.
- **Core pain:** "16-hour days without tears". Concrete plus heat plus back pain that's "on fire".
- **Wrong-shoe enemy:** cheap black non-slip work shoes from the big-box store, or steel toes.
- **Story seed:** after 35 years behind the fryer, the first shift she didn't cry in the walk-in cooler.
- **Supporting quotes:** #18, #19, #20, #21, #28.
- **Frequency:** food service 7% (1,252). analysis.md has the server persona, but not long-form copy.
- **Care:** HIGH RISK on grip. 44 rows say the shoe is "not slip resistant" in restaurant use ("basically socks with soles"). Don't make slip resistance the hero claim in a kitchen story. Lead with cushion and standing comfort instead.

**Ranked for testing:** A1 (biggest volume, newest insight) > A3 > A2 > A6 > A5 > A4 > A8 > A7 > A10 > A9.

## 5. Objections and complaints to handle, and claims to avoid

### Objections, ranked (rows mentioning; regex counts are approximate)
1. **Refunds and returns** (~1,600 rows mention refund/return/exchange/discount). "You only want to give me 30%", "offered discounts til you wore me down", "There is no money back only exchange". Known.
2. **Shipping slow or not received** (~1,100). "I love how I get this survey before I get the shoes." Shoes not arriving before a vacation or cruise comes up repeatedly (Amazon cruise, Hawaii, "Leave on vacation tomorrow without these shoes"). Known.
3. **Wrong size, in both directions** (column K, n = 15,559): good fit 39.7%, small or too small 33.0%, big or too big 27.2%. Comfort averages 2.98 with a good fit, against 1.51 "too small", 2.12 "small", 2.35 "big" and 1.84 "too big". Some customers say "order a half size bigger", others "they actually felt bigger" as the knit stretched. **EU sizing confusion:** "I ordered a size 8, and instead I got a 39.5… If you had told me they were in European sizes". No half sizes, and no wide widths (~364 mentions of "need wide / extra wide"). Partly known; the EU sizing and stretch-over-time points are new.
4. **Hard to put on (NEW, not in analysis.md):** about 280 rows. The tight knit collar and soft heel collapse, so customers need a shoehorn, and it's "impossible" for seniors with knee replacements, braces or swelling. "These are the HARDEST shoes I have ever tried to put on." This matters because the core buyer is 65+ and many ads imply "slip right on". **Handle it in copy:** "the first time takes a minute, then the knit gives". Never claim "easy slip-on" or "hands-free".
5. **Insole too thin / "feels like walking on cement"** for some people, and some feel the arch is too low or in the wrong place (~150–250 rows across phrasings). "Your insoles are very cheap. I shall have to tear them out." Note that removable insoles are liked by orthotic users ("great that the insole is removable so I can put a heel cup under").
6. **Too wide / foot slides / unstable for narrow feet** (~140): "my bad foot rolls around inside the shoe", "would not hold up on uneven surfaces like the dirt road", "no side support". This can conflict with the cobblestone angle.
7. **Cold or not waterproof** (~110): the breathable knit is cold in winter for neuropathy and circulation customers, and it isn't rain-proof.
8. **"Not really orthopedic" / misleading** (~180): "Be honest about your product. Not orthopedic shoes."; "Owner claimed he made it for his mother and that nurses swear by it"; "When I read nurses wear them, although I dont believe those statements". Known.
9. **Not slip-resistant in kitchens or wet floors** (~44): "They are not slipper resistance", "basically socks with soles", "NOT slip resistant as advertised". This is new as a specific failure.
10. **Made in China vs "Made in USA" expectations, and currency shock** for AU/CA buyers charged in USD (~10–20): "U said they were made in the USA if they are then why are they being transported from across seas".
11. **Heel higher than forefoot / toes pushed forward** (small): "These heels are higher than the rest of the shoe pushes her toes up??"

### Claims to avoid in long-form
- Money-back guarantee, "45-day no-questions returns", "free easy exchanges", fast or "arrives in X days" shipping (known).
- "Orthopedic", "podiatrist-recommended / approved", "doctor-approved", "made for nurses by nurses", "the founder made it for his mother" unless verified. Customers repeat these back as reasons for distrust.
- "Slip-resistant" as the main promise for kitchen, restaurant or wet-floor stories. Keep "grippy outsole" low-key or omit it.
- "Easy slip-on", "hands-free", "just slide your foot in".
- "Fits wide AND narrow feet", "extra-wide sizes": there are no width options.
- "Instant / immediate relief", "cures plantar fasciitis / neuropathy", "12 hours pain-free" as a guarantee ("I was disappointed I didn't receive immediate relief like the testimonials"). Keep relief as one person's experience, with a timeline.
- "Waterproof" or all-weather.
- "Made in USA".
- "Lasts longer than Skechers/Hoka". Durability is a complaint for us too.
- Prices shown without currency for non-US audiences.

**Story-craft tip from the data:** the most believable 5★ voices admit a flaw ("love hate relationship… VERY difficult to put on… comfortable once they are on"; "at first they felt tough but as I walked they mold to my comfort"). Building that small admission into the story protects the brand from the #4 objection and reads as more honest than flawless praise.

---

## 2026-11-19 update (newest 200 rows)

**Access:** Google Drive connector worked. `read_file_content` only returns a sample of the first rows, so I exported the sheet as CSV with `download_file_content` (18,523 rows, 2023-04-15 to 2026-11-18) and read the newest 200 rows (2026-09-08 to 2026-11-18, about 2.8 responses a day). Order emails were masked and are not quoted here.

**Counts in these 200 rows:**
- **Comfort score:** 1 = 99, 2 = 48, 3 = 21, 4 = 11, 5 = 21. That is 74% at 1–2, more negative than the all-time picture (avg 2.98 with a good fit). Treat recent responses as complaint-heavy, not as a quality trend, until someone checks how the survey is triggered.
- **Age:** 50–65 = 83, 65+ = 69, 40–50 = 31, under 40 = 13.
- **Jobs mentioned (keyword counts, approximate):** nurse/RN about 18, teacher/educator 14, retail 9, cashier 4, deli 4, CNA 3, food service/cook several, plus single rows for a stadium courtesy team, a tire-picking DC, a thermoformer and a pet boutique.
- **Trip mentions:** 12 (Disney 3, Europe 3, other trips or travel 6).
- **"Wide":** 32 rows. Most are a reason for buying. A few say the shoe was too wide or hard to get into.

**New moments and phrases (verbatim, newest first):**
- Stadium worker, 65+, 5★: "I stand for long periods of time and I do a lot of walking around our stadium during football games." (job: "Courtesy Team member for the Jaguars"). **New: game-day and stadium staff over 65.**
- Distribution center, 40–50, 2★: "12 hours a day order picking tires at the local distribution center … Trying to find a good work shoe with a composite toe that's actually comfortable." (Our shoe isn't a safety toe, so this is a "don't promise" case.)
- Two jobs, 50–65, 5★: "Head Cashier for HOMEDEPOT and cashier for Kroger … standing and walking on concrete floor for 8+ hours for 5-6 a week." Current solution: "New Balance and Saucony." **New: two employers, two floors.**
- Nanny, 65+, 5★: "Needed support for Disney vacation." Current solution: "Your shoes."
- Nurse, 65+, 5★, arthritis: "To reduce pressure on right hip." Current solution: "These shoes."
- Manufacturing, 50–65: "Stand all day, basically in one area." Job: "Thermoformer. Make plastic medical parts at a machine." (Planted standing, not walking.)
- Concrete with mats, 5★: "Stand on concrete with mats for 10 hr shifts … hoping it would help with lower back& hip pain." Current: "Taking Celebrex, wearing brace part time, insiles from my Dr."
- Retail merchandiser, 1★: "On my feet on cement for 10 hours a day." Current: "Buy expensive shoes every 3 months."
- Pet boutique clerk, 65+, 5★: "my feet ache at end of 6 hour shift." Current: "Soak, feet up."
- Semi-retired hairdresser, 65+, 5★: "Being off my feet is the only solution."
- Elementary school lunch lady, 65+, 4★: current solution "Take my shoes off."
- Retired teacher, 65+: "Planning to do a lot of walking for a trip coming up." Current: "Elevating my feet."
- Foot pad atrophy, 50–65: "I have none. I live with constant pain."
- RN, 50–65: "I wear flux sneakers for the zero drop and wide toe box but was looking for something else." (Competitor: Flux.)

**Objections that came up again (keep as "don't promise" rules):**
- Distrust of founder and nurse claims: "Owner claimed he made it for his mother and that nurses swear by it" (10/24). An ORTHO ad caused confusion: "Misleading ad attached to ORTHO ad" (11/9).
- Hard to get into: "They were supposed to be for women with wider feet and I can't even get my foot in the shoe" (dog groomer, 10/29).
- Too wide for a narrow foot: one nurse passed hers on to "my granddaughter who has a very thin foot" (11/16). This is also an unplanned hand-down/gifting moment.
- Shoes didn't arrive in time for the trip: "Disney vacation but the shoes never arrived I want a refund" (nurse, 11/11). Never promise delivery before a trip date.
- Grip and safety toe expectations: "They have steel toe, and WERE supposed to have non slip" (fast food, 9/17). "They said great arch support, cushioned and slip resistant" (deli, 10/4).

**What's new compared with the 2026-11-12 deep dive:** (1) people over 65 doing event and stadium work, and (2) two-job holiday cashiers. Both fit December. The 5★ voices are still mostly 65+ women in light-standing jobs (boutique, nanny, hairdresser, home health aide); the 1★ voices are mostly 40–65 on concrete for 10–12 hours.

## 2026-11-26 update (24 new rows, 2026-11-18 16:35 to 2026-11-25 20:37)

**Access:** the Google Drive connector worked again. `read_file_content` returned only the sheet's first rows, so I exported it as CSV with `download_file_content` (18,546 rows, 2023-04-15 to 2026-11-25) and read every row after the 11-19 cut-off. That is about 3.4 responses a day, slightly up (Black Friday orders arriving). No emails or order numbers are quoted.

**Counts (24 rows, small sample):**
- **Comfort score:** 1 = 15, 2 = 2, 3 = 3, 4 = 1, 5 = 3. 71% at 1–2, the same complaint-heavy mix as last week.
- **Age:** 65+ = 10, 50–65 = 10, 40–50 = 3, 30–40 = 1.
- **Foot problem:** neuropathy 5, "no pain, only comfort" 5, plantar fasciitis 4, bunions 2, plus one each of heel spur, Morton's neuroma, arthritis, and "balance issues from double knee replacement".
- **Source:** Facebook 15, Google 5, Instagram 1, "Just scrolling through my phone" 1, "News" 1.
- **Size received:** good fit 9, too big or big 9, too small or small 6. Sizing complaints are 15 of 24 this week, higher than usual. The comments don't say whether the BF orders were sized up.

**New moments and phrases (verbatim, newest first):**
- Medical receptionist, 65+, bunions, 1★: "It had a wide box which I like but you I couldn't get my heel in the back which is very unusual." (Hard to get on, again.)
- Retired teacher, 50–65, neuropathy, 5★: #1 reason "Going on cruise". Wants us to sell "Leggins". **Cruise is new in the 5★ voices.**
- Teacher, 65+, 3★: "You advertised that it would be a good shoe for a day at Disney. Since that's our plan, I ordered two. But I don't feel the comfort and I don't feel that they are designed to support heavy women." **Two pairs bought for one Disney trip; "heavy women" is a new self-description. Don't promise heavier-body support.**
- Dog groomer, 50–65, Morton's neuroma, 1★: looking for "Pain free". (Second dog groomer in two weeks.)
- Remote worker, 65+, 5★: "Saw on the ads and it is said to be the best rubber shoes."
- Warehouse non-profit work, 50–65, neuropathy, 1★: "They were the most uncomfortable shoes I've ever worn. And someone that already has issues getting them on was a challenge. The back kept collapsing so almost impossible." Looking for: **"Comfort that last all day and want to wear the next day too."** Current solution: "Haven't found it yet." Wants us to sell: "A shoe horn to actually put your shoes on."
- Packer, 50–65, arthritis, 1★: current solution "Extra socks". Wants us to sell a "Heated massage cushion for automobile".
- Standing 7–9 hours a day, 50–65, neuropathy, 1★ (answered twice): #1 reason "Need new ones"; current solution "Ordered new shoes, but they are to small".
- Property management, 65+, plantar fasciitis, 1★: "Better comfort for my right heel." Current: "Inserts and lifts."
- 80-year-old buyer, 65+, 2★: "i thought they look great and comfy but how is an 80yearold suppose to use the back of the shoe its very difff shoee to slip on great for a younger crowd". Suggests a "hard back shoe which you can hold up while you slip in". **The 80+ buyer exists, and the collapsing heel is her deal-breaker.**
- Retired, 65+, neuropathy, 1★: "I needed a comfortable shoe to be able to walk without pain." Current: "Walking and pain medicine."
- Processing support specialist, 50–65, 1★: "The advertisement was convincing but when I received and tried the product, it was unco uncomfortable and the material was not of good quality."
- Nursing assistant, 50–65, plantar fasciitis, 1★: current "Orthopedic sneakers".
- Nurse, 40–50, 1★: "The shoe that I received does not have cushion it feels flat and I am walking on a heel."
- Housewife, 65+, 5★: "Flat feet. Fir walking." Current: "Massage".
- Elevator mechanic, 30–40, plantar fasciitis, 1★: "Comfort and safety toe I'm on my feel a lot at work … I've tried several different pairs of boots, nothing has eased the pain." (Safety-toe expectation again: don't target trades that need one.)
- Retired, 65+, plantar fasciitis, 3★: "The add made them sound super comfortable and supportive." Wants "Good Arch support, quality material, comfort." Current: "Orthotic inserts".
- Dental assistant, 40–50, 2★: "My feet are not tired as before" (a partial win, written as her current solution), and "it should have more memory foam at the front part".
- Customer success manager, 50–65, double knee replacement, 4★: "Advertised as supportive and good for standing all day-NO SUPPORT AT ALL!" Looking for "Support, comfort, stability".
- Disability, 40–50, 1★: "Comfort, and any shoe to make my feet look smaller."
- Retired, 65+, heel spur, 1★: wanted "soft cushion back and arch support"; current solution "injections".

**What's new and usable:**
1. **"Wear them the next day too."** The warehouse worker's phrase names a second-day test, a different outcome from "lasts all day". It is a good outcome line for StefanBrain to consider; it isn't a claim.
2. **Cruise and Disney trips with two pairs.** Two people bought for a trip this week, and one bought two pairs for a single trip. Holiday travel is in the voice now, but the trip buyer is also where the "not as comfortable as advertised" complaints come from, so keep the expectations modest.
3. **The 80-year-old who can't get the heel on.** That makes 3 hard-to-get-on complaints in 24 rows (receptionist, warehouse, 80-year-old), the same objection as the 11-12 deep dive. Keep it as a "don't promise easy slip-on" rule. A story could show her using a shoehorn the first time; never "hands-free".
4. **"Don't feel they are designed to support heavy women."** This is new wording. Avoid body-weight claims.
5. **Job list this week:** dog groomer, packer, warehouse non-profit, property management, elevator mechanic, dental assistant, medical receptionist, nurse, nursing assistant, teacher and retired teacher, CS manager. These are the same standing and walking jobs as before; there is no new segment.

**Objections (for the "don't promise" list):** "Advertised as supportive and good for standing all day" with "NO SUPPORT AT ALL"; "feels flat … walking on a heel"; "the advertisement was convincing but…" (3 rows blame the ad's promise directly); a collapsing heel collar; heavier women. Read together, they say the long-form should under-promise on cushion and support feel at first wear.
