# DentalPULSE: long-form market swipe (Atria, 2026-11-11)

Goal: find formats, hooks and open loops that have lasted (60+ days) so we can build 10 net-new long-form static Meta ads (one image plus a 5-14k character first-person story) for the DentalPULSE Pod ($99.95, tap water only, 5-minute cycle; dentures, aligners, retainers, night guards).

Read-only research. Nothing was saved, no boards were made, and no paid transcription was used. Transcripts are the free ones that already existed.

---

## 1. Method and queries

Tool: Atria `search_library_ads` (library, advertiser and saved scopes), `get_library_ad` (full copy), `get_library_ad_transcript` (free transcripts only), `resolve_advertiser`.

Default long-form filter: `media_format=["image"]`, `min_body_length=2000`, `language=["en"]`. I sorted with `most_active` (longest-running first, `collapse_variants=true`) for broad terms and `best_match` (with `min_days_running` 45 or 60) for multi-word terms, because `most_active` with a multi-word query returns loose matches.

| Bucket | Queries / scope |
|---|---|
| Direct competitors | resolve: MyNovaPod, mynovapod.com, NovaPod, Ploise, Zima Dental, Remi, shopremi.com, Sonic Dental. Advertiser scope, `most_active` and `most_impressions` (active), all formats. Library query "NovaPod" long-form. |
| Dental long-form | denture, dentures (all + active only), night guard, retainer, teeth grinding TMJ, Invisalign aligners, gum disease bleeding gums, bad breath tongue, toothpaste fluoride hydroxyapatite, my daughter's retainer orthodontist |
| Angle evidence (any length/format) | persulfate denture tablets, Polident tablets, retainer bacteria cavities aligner, candida yeast dentures pneumonia, mold night guard case |
| Cross-niche | CPAP mask cleaning mold, "I threw out after learning what's in it", my mother hearing aids, water filter tap water contamination |
| Saved swipe file | `scope=saved`, image, 2000+ chars, `saved_newest`, 2 pages (40 ads) |
| Long video (dental) | dentures retainer cleaner ultrasonic, `video_length` 60-120 and 120-, 30+ days; free transcripts pulled for 4 ads |

Limits:
- Remi: only the "Remi" page (shopremi.com, 8 ads) was checked. resolve also returned "Remi Wellness" (430 ads) by link URL, but I did not confirm it is the same company.
- Sonic Dental and Zima have no copy longer than about 700 characters, so their "long-form" is only their 60-90 second videos.
- In the table, "excerpt" means I logged it from the 320-character search excerpt and did not read the whole ad.

---

## 2. Competitors: what they actually say

### MyNovaPod (NovaPod), the closest long-form competitor
- **How it runs:** it is not in Atria under its brand name. It runs through made-up persona pages that link to mynovapod.com advertorials: Carrie Wickers (518 ads; the same page also runs "NovaPaw" puppy pads, so it is the same operator), Margaret Montgomery (179), Lucille Adams, Keira James, Callie Kelly, Daphne Butler and about 10 more. Main market GB and AU ("I called 000"); it targets AU, CA, GB, NZ and US. Headline on every ad: "The #1 Dentist-Recommended Denture Cleaner."
- **Longest runners:** the long-form static "I'm fucking furious writing this" (11,176 chars), 99 days, best rank 4-5 of 77, now inactive (ended 2026-11-04). Its rank-1 asset now is a 134-second video, "What's the best thing to clean dentures with? ... let me rate them": active 87 days, rank 1 of 206.
- **Angle:** a caregiver's anger, a hospital scare, and a young doctor who asks "How does he clean his dentures?" The mechanism is that denture acrylic is porous: microscopic scratches, biofilm anchored *inside* the material, and the tablet "works on the surface". It names **denture stomatitis**, a metallic taste, constant tiredness, and the cloudy water after the first cycle ("That was in my mouth this morning").
- **Claims:** 42,000 pulses per second; "true germicidal UV-C at about 253nm" against "a decorative blue LED"; "built by a prosthodontist" (named "Dr. Matthew Collins, Sydney" in the newer ad); a buyer's guide that cheap pods "are built for jewellery".
- **Offer/close:** soft. "I am not selling anything... There is a full explanation... Read it today. Click below." No price or discount in the copy.
- **Newer template (Lucille Adams, launched 2026-10-08, in our saved file):** "By the end of this you are going to be furious. Because there are three things happening right now. One... Two... Three... The insecurity is not a confidence problem. It is a biofilm problem." This is the same skeleton as the saved GLP-1 ad (Nicole Stanley, rank 1 of 206).

### Ploise (Denture Dome), the longest long-form runner in the category
- **How it runs:** the Ploise page plus an "education" page called **Denture Care Tips** (9.4k likes), with Vercel landers (ilp4, ilp5, ilp10, ilp11, lp3, ddlp). The product is the "Denture Dome", a small black ball ("shaped kind of like a Magic 8 Ball"). It now also sells **Bone Support Strips** (D3+K2 dissolving strips, the "Sunken Face-Eraser").
- **Longest runners:** the heart-attack story, 265 days; the stroke story, 264 days; "I wasn't planning on sharing this publicly... I love my dentures", 262 days. More than 20 versions of 10-15k character stories are still active at 148-156 days. The top-ranked ones are the Ricky veteran stroke version (rank 1 of 210), the cancer survivor (rank 3 of 210) and Dr. James Mitchell the prosthodontist (rank 12).
- **Angle:** almost entirely **disease scares**: stroke, heart attack, aspiration pneumonia ("denture wearers are 2.3 times more likely to develop aspiration pneumonia"), systemic inflammation, brain fog and dementia. A doctor in hospital asks about the dentures. Secondary threads: smell and isolation, arthritis that makes brushing hard, $30k implants out of reach.
- **Claims:** "hospital-grade", "kills up to 99.99%", "ultrasonic + UV-C", "Recommended by 5,000+ dentists", "sold out three times this year", "don't buy on Amazon/Walmart, knockoffs lack the frequency", a veterans and retirees discount, 50% off, a 90-day money-back guarantee, a US company with a warranty. The close is a hard CTA plus scarcity.
- **Also:** short-lived **persulfate/FDA** videos (see section 5).

### Zima Dental (Dental Pod), the biggest spender, with short copy
- 10,726 Meta ads all-time. Copy is never longer than about 250 characters. Older ads ran 1,000-1,130 days ("Enjoy a hygienically clean retainer every single day"). The current top ads (rank 1-15 of 1,443) are 57 days old.
- **Claims:** "Trusted by 20,000+ Dentists", "Dental Product of the Year" / "best dental product two years in a row", "Accredited by the Oral Health Foundation", "1M+ customers", "Free shipping from the US", 30-day money-back. Focus on retainers and aligners first, guards second.
- **Long videos (60-92s), dentist point of view:** "My patient's retainer smelt like mouldy cheese!" (decay drilled at the same appointment; tablets are "like cleaning your teeth with just mouthwash"), rank 32. "That sour retainer taste is not normal and tablets don't fix it... pH is off... Porphyromonas gingivalis", rank 27, 71 days. "My patient swore lemon juice would clean her retainer." "Don't let dirty retainers undo years of wearing braces."

### Sonic Dental (Sonic Pro / Sonic Spa / Sonic Odyssey)
- 1,469 ads, no copy over 700 characters. Evergreen line: "Clinical grade cleaning for your Aligners, Retainers, Guards, Dentures & more ✨" / "Cutting Edge Ultrasonic & UVC technology". The #1 ad (an image) has been active 464 days. Offers: "Save up to 30% on the Sonic Pro", "$35 off", "trusted by over 500,000 customers", "just add water". Its bundle includes tablets.
- Its longest runner ever (998 days, video): "47.2% of people using aligners suffer from periodontal diseases caused by... dirty aligners". This is the only aligner disease claim I found.

### Remi (shopremi.com, night guards)
- 8 ads, all short, longest 66 days. The ultrasonic cleaner is an add-on in a bundle: "Keep your night guards clean and remove harmful bacteria in just 5 minutes... Prevent plaque buildup, reduce bad breath, and promote gum health". Other lines: "HSA & FSA can help you pay", "custom night guards for 80% less". No long-form at all.

### Others seen
Swissklip "ShinePod" (42kHz plus 4 UV lights, tablets "leave the gunk", brushing scratches "and leaves you with a $500 dental bill") runs short ads only. usmile, Smyle and Hismile are not long-form.

**Takeaway:** in this category, long-form belongs to two denture-only operators (NovaPod and Ploise), and both lean on the same mechanism (porous acrylic, biofilm inside, tablets on the surface, cloudy water). Zima and Sonic out-spend everyone with short claims plus dentist videos. **Nobody runs long-form for retainers, aligners or night guards.**

---

## 3. 25-ad log (long runners prioritized)

Columns: ID = Atria ad id. Rank = best (or current) impression rank within the advertiser. % = how far through the copy the product is first named. Read = full copy read (F), excerpt only (E), or transcript (T).

| # | Advertiser (page) | Ad ID | Niche | Days | Status | Chars | Rank | Hook (first lines, verbatim) | Open loop | Narrator | Enemy / old method | Mechanism (why the usual fix fails) | Product at | Close | Read |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NovaPod (Carrie Wickers) | m2272273613613475 (dup m3575106039309560) | Dentures | 99 | inactive | 11,176 | 4-5/77 | "I'm fucking furious writing this. / But my husband said if it stops even one person going through what we went through, it's worth it. / ...Eight weeks ago I was sitting in a hospital corridor at 2 in the morning" | Rage + hospital cliffhanger + "the question nobody asked in 11 years" | Wife of a 74-year-old | "That box of tablets on our bathroom shelf"; GP says the bloods are fine | Porous acrylic; biofilm anchored inside; the tablet dissolves in water and works on the surface; denture stomatitis | Mechanism at ~60%, name "NovaPod" at ~82% | Week 1-4 and month 2 timeline; jewellery-cleaner/blue-LED buyer's guide; sister's "The water." / "Nine years."; soft "read the explanation, click below" | F |
| 2 | NovaPod (Carrie Wickers) | m2659710207819136 (video 134s) | Dentures | 87 | active | 82 (copy) | **1/206** | "What's the best thing to clean dentures with? I get asked that a lot. So let me... rate them. Soak tablets. Worth it? Two out of ten." | Rate every method /10 | Clinician-style voice | Tablets 2/10, brushing 2/10 ("might be worse than nothing"), soaking 3/10, bleach/vinegar 1/10, clinic 8/10 | Brushing carves scratches where bacteria anchor; soaking doesn't break up biofilm | ~85% | "Ultrasonic 9/10... the one I kept seeing the best results with was the Nova pod"; day 4-5 the metallic taste is gone | T |
| 3 | NovaPod (Lucille Adams) | m2347274285677239 | Dentures | 0 (launched 10-08) | active | 7,614 | n/a (saved) | "If your dentures are affecting your confidence, your gums are always sore, and you have quietly started pulling back... By the end of this you are going to be furious. Because there are three things happening right now." | Promised anger + numbered 3-part reveal | Wife of a 72-year-old (former coach) | "Every hygienist said they looked good" | Same porous-acrylic biofilm; "the insecurity was not a confidence problem. It was a biofilm problem" | ~70% (no brand name; "a prosthodontist from Sydney") | Photo from Sunday dinner, "Dad seemed like himself tonight"; "read the full explanation" | F |
| 4 | Ploise | m2031431081019223 | Dentures | **265** | inactive | 4,288 | n/a | "My doctor said it wasn't a panic attack. It was a heart attack. A real one... / I was standing at the bathroom sink, brushing my dentures like I always do" | Diagnosis cliffhanger | Denture wearer | Brushing | n/a (same template as #5) | n/a | n/a | E |
| 5 | Ploise | m1326546802140882 | Dentures | **264** | inactive | 6,151 | n/a | "My doctor said the stroke could've killed me. Not later. That night. / I was brushing my dentures in the bathroom—like I always do—when my right arm went numb" | In medias res + doctor's question | Woman, wife | Brush, rinse, soak 3x a week; "tablets alone? Useless" ("like rinsing a dirty sponge") | Biofilm in micro-grooves leads to systemic inflammation, clot | ~55% (forum quotes, then "Denture Dome") | Inflammatory markers better; "every night you wait..."; discount | F |
| 6 | Ploise / Denture Care Tips | m544280862104080 (active variant m4618693531744850, rank 10/44) | Dentures | 262 / 148 | inactive / active | 6,183 | 10/44 | "I wasn't planning on sharing this publicly. / But I realized that what I went through might help others — especially fellow denture wearers... / I love my dentures. They fit great, they look great." | Reluctant confession + "never imagined something I wore every day would almost kill me" | Denture wearer | Routine cleaning | Biofilm | n/a | n/a | E |
| 7 | Denture Care Tips (Ploise) | m1320113750329087 (orig m1356338409179081, 185d) | Dentures | 151 (185) | active | 12,527 (11,014) | **1/210** | "My daughter told me to post this. / I said no. Too personal. Too embarrassing. / She said: 'Dad, you almost died. And nobody warned you.'" | Reluctant confession + stroke | Ricky, 67, retired Air Force | "Those blue tablets"; the VA wouldn't cover cleanings; arthritic hands can't scrub | "Biofilm... brushing and soaking tablets can't remove"; "2.3x aspiration pneumonia" | ~65% (daughter brings the device) | One-time purchase, no subscription; buy only from the official site; veterans discount; "sold out 3x" | F |
| 8 | Denture Care Tips (Ploise) | m1353823560018993 | Dentures (young wearer) | 153 | active | 12,884 | 19/239 | "My sister called me from the ER at 2 a.m. / She couldn't breathe. / The doctor said bacteria from her dentures had gotten into her lungs while she slept." | ER phone call + "I knew I was next" | Sarah, 34, who has worn dentures for 3 years | Tablets "just mask the smell"; toothpaste scratches; "the instructions were wrong" | Biofilm the care instructions ignore; **aspiration pneumonia** | ~65% (Facebook group replies) | Gift a second one to her sister; US company with a warranty; "don't buy on Amazon"; "Murphy's Law" ending | F |
| 9 | Denture Care Tips (Ploise) | m882432138205185 | Dentures | 153 | active | 10,957 | **3/210** | "I beat cancer twice. / Breast cancer at 58. Mastectomy. Colon cancer at 66. / I'm 75 now... Getting dentures was one of the hardest things I've ever been through." | Resilience contrast (beat cancer, beaten by dentures) | Woman, 75 | n/a | n/a | n/a | n/a | E |
| 10 | Denture Care Tips (Ploise) | m991331390480828 | Dentures | 152 | active | 12,003 | 12/210 | "My name is Dr. James Mitchell. / I'm a prosthodontist... / And I need to tell you something that might save your life. / But before I do, I need to ask you a few questions. / Do you wear dentures?" | Self-diagnosis quiz | Prosthodontist (claimed) | n/a | Inflammation symptoms (sleep, stiffness, anxiety, fog, bloating) | n/a | n/a | E |
| 11 | Denture Care Tips (Ploise) | m1995124777947651 | Dentures | 200 | inactive | 7,376 | n/a | "Did you know that if you wear dentures and you're constantly anxious, can't sleep at night, always want sweets and feel tired all the time, you might have too much silent inflammation...? / But people don't believe me when I tell them this." | Contrarian "#1 food is not turmeric" | Educator | Diet fixes | Silent inflammation from the mouth | n/a | n/a | E |
| 12 | Denture Care Tips (Ploise) | m2089916771902422 / m923364834091269 | Dentures | 151 | active | 9,939 / 9,564 | 42-59 | "I'm breaking doctor-patient confidentiality to write this." / "I was a cardiologist for 28 years... And I missed something that killed hundreds of them. Including my wife." | Guilty-expert confession | Retired cardiologist | Missed by doctors | Oral bacteria and the heart | n/a | n/a | E |
| 13 | Denture Care Tips (Ploise Strips) | m2853810198303880 | Dentures (loose fit) | 156 | active | 5,611 | 30-36/284 | "My dentures needed a reline every six to eight months for years. Here's what finally changed that. / My dentist said it was normal." | "Dentist says normal, but I noticed things he wasn't mentioning" | Karen, 57, nurse | Relines, adhesive, swallowed D3/K2 pills | Jawbone loss; the pill route goes through a wrecked gut | ~75% | "Change the route. Try it for three months. Let your dentist decide." | F |
| 14 | Deborah Rustad (SPNutrition) | m810729212062930 | Teeth grinding / night guard | 99 | active | 11,067 | **20/1069** | "I am a 48 year old woman who wears a mouth guard to bed. Like a linebacker. My husband won't kiss me goodnight when it is in. He says he doesn't mind. He also turns his head." | "Nobody told me the guard was never supposed to stop me grinding" | Woman, 48 | 6 guards, custom guard, 3 doctors, ENT, physio, chiro, Botox | Every fix "aimed at the wrong end": the guard sits between the teeth, magnesium lets the muscle release | ~80% | Week 1-5 diary; the hygienist says "Did you get a new guard?"; "the article is below" | F |
| 15 | Deborah Rustad | m1022815634008355 | Dentures/oral | 97 | active | 8,773 | 113/1069 | "I fitted a 24 year old woman for dentures last month. She has seven real teeth left. And she isn't the first." | Shocking clinical observation | Denture maker, 26 years | n/a | n/a | n/a | n/a | E |
| 16 | Dr. Richard Calloway (NOURI) | m2569520453486634 | Bad breath | 111 | active | 4,578 | **4/166** | "For 18 years I treated my patients' guts. Their breath got better along the way. That wasn't a coincidence — and it's why every mouthwash you've ever tried has failed." | Accidental discovery by a specialist | Gastroenterologist | Mouthwash | Odor source is systemic | n/a | n/a | E |
| 17 | Mark Sullivan (NOURI) | m1842392843398763 | Bad breath | 146 | active | 5,610 | **1/4** | "I spent 16 years turning my head during every conversation. Then at 1 a.m. on a random Wednesday I found something that made me realize I'd been treating the wrong organ." | "Treating the wrong organ" | Man, 42, manager | Brushing 3x a day, tongue scraping, SmartMouth/TheraBreath/Listerine | 3 sources (gut, mouth, liver); "cleaning the exhaust pipe... the engine was thirty feet south" | ~70% | Week 1-4, month 2; wife leans in; "full story at the link" | F |
| 18 | Better Living Daily (Modern Hearing) | m2801947713476602 | Hearing aids, seniors | **221** | active | 13,884 | **4/110** (now 7/308) | "\"I Almost Didn't Buy Them. Thought It Was Another Hearing Aid Scam.\" / Facebook ad. $249 hearing aids. \"Revolutionary technology.\" \"Same as $5,000 brands.\" / Yeah, right." | Skeptic investigates | Brian, 69, retired logistics manager | Miracle-Ear $4,995, Costco $1,499, $79 Amazon amplifiers | No clinic overhead; the same components | ~25% named as the "scam" he investigates; full pitch ~70% | Worst case vs best case; 34 cents a day; 45-day returns; "I've seen the warehouse myself"; 5-option comparison article | F |
| 19 | Better Living Daily | m1034429656050402 | Hearing aids | 118 | active | 11,929 | 31/44 | "My hearing almost cost me a 42-year marriage. And it nearly ended at our anniversary dinner." | Relationship stakes | Husband | n/a | n/a | n/a | n/a | E |
| 20 | Uproot Clean | m1437586644931964 | Washer cleaner tablets | 60 | active | 6,326 | 242/2012 | "Affresh is not a cleaning product for pet households. It's a cleaning product for houses without pets, and the box doesn't mention that." | Insider names the category's blind spot | Danny, appliance repair tech for 19 years | Oxygen-bleach tablets "tablet after tablet" | Tablets handle ~20% of the buildup; protein, starch and oil need enzymes; "that's the biofilm" | ~70% | "It wasn't you... It was the tablet"; Walmart availability; "take it from a guy who's seen thousands" | F |
| 21 | Rejuveen (Uflora) | m1704758737432718 | BV / women's health | 85 | active | 10,599 | 15/288 | "My doctor said after 16 rounds of Metronidazole for BV, the meds might not work anymore / That there's a slimy biofilm coating my vaginal tissue, trapping antibiotic-resistant mutant bacteria inside / Where they MULTIPLY" | Fear diagnosis + "even ChatGPT gave up on me" | Woman, 38 | Doctor 1, 2, 3 and 19 antibiotic rounds | **Biofilm fortress** the treatment can't penetrate | ~75% | Day 3/7/14/21/30 diary, month 4 lab numbers; 90-day guarantee; P.S. "187 days" | F |
| 22 | PAP MD | m1845822613469247 | CPAP | 109 | inactive | 3,071 | 8/379 | "When I first started CPAP everything was great. / I started sleeping better... / But after a month or so I noticed it was becoming less effective." | It got worse and the doctor's fix made it worse | CPAP user | "Increase the pressure" | The machine pulls in mold and bacteria and pushes them into the lungs | ~55% | 60-day money-back; lowest price ever | F |
| 23 | Raising Toddlers with Bec | m1487999738960847 | Parenting | **322** | active | 8,300 | **1/319** | "My 4-year-old is still in diapers. / And I genuinely don't understand why. / My name is Bec I'm 31 years old." | Baffling problem in a smart kid | Mom, 31 | n/a | n/a | n/a | n/a | E |
| 24 | Artuvate | m2736746953361191 | Neck pain, seniors | 166 | active | 4,418 | **3/654** | "I'm Michael. I started Artuvate five years ago. / I started it because of my mother. Her name is Arianna. / I watched her stop living because of her neck pain." | Founder's personal reason | Founder (son) | n/a | n/a | n/a | n/a | E |
| 25 | Margaret Davis ("Dr. Andy") | m1677206286847023 | Edema | 106 | active | 9,574 | **2/1134** | "I've been an edema specialist for 19 years and if your feet, ankles, or legs have been swelling up... Then what I am about to share with you is going to OUTRAGE you." | Expert promises outrage | Specialist | n/a | n/a | n/a | n/a | E |
| 26 | Dr. Sarah Mitchell | m1678021367355976 | Pet water | 63 | active | 16,962 | 125/511 | "Please STOP giving your cat tap water. / I know that sounds insane coming from a veterinarian." | "Please STOP + it sounds insane coming from me" | ER vet | Tap water | "Treated to be safe for you. Not for your cat." | n/a | n/a | E |
| 27 | Zima Dental (video 69s) | m1641516337598211 | Retainers | 57 | active | short | 32/1051 | "When I tell my patients their retainer smells like spoiled cheese, they laugh until it's not funny. Because at the same appointment, I was drilling caries off her teeth." | Gross-out + consequence | Dentist | Fizzing tablets "like cleaning your teeth with just mouthwash" | No scrubbing action, no penetration through plaque | ~55% | Dental Product of the Year | T |

Also noted but not in the table: Primals fluoride ("Don't use fluoride toothpaste again until you see this", 122 days, 2,293 chars); Better Living Daily "Roy, 74, retired electrician" (134 days, rank 11); Active Court Community "Please STOP sizing up your tennis shoes" (saved, 29 days, rank 13); Melissa Hayes "I don't give a f*ck if it upsets you" (33k chars, rank 1, 32 days).

**What the long runners have in common:**
- The narrator is a family member or a reluctant poster, not the brand.
- A doctor asks a question nobody had asked before.
- The old method is named as "everything the box said".
- The mechanism is about *where* the problem lives (inside the material, the wrong organ, the wrong end).
- The product appears at 55-85% of the copy.
- The proof is a dated week-by-week timeline plus a "someone noticed" moment.
- The close is soft ("read the explanation") for advertorial traffic, or comes with a guarantee and a cost-per-day line.

---

## 4. 12 transferable formats and hook formulas

| # | Format | Source (days) | Formula | DentalPULSE version (example hook) |
|---|---|---|---|---|
| 1 | **Furious caregiver, hospital or crisis corridor** | NovaPod #1 (99d) | "I'm [furious] writing this. But [person] said if it stops one person... [Time] ago I was [scene at 2am]" | "I'm so angry writing this. My mum said if it stops one family going through what we did, post it." (Change the crisis to a non-disease one: a dentist appointment where a sore gums diagnosis was blamed on her routine.) |
| 2 | **Reluctant confession, "family made me post"** | Ploise/DCT (150-265d, rank 1) | "I wasn't planning on sharing this publicly. / My [daughter] said if I didn't, she would." | "My granddaughter typed this for me. I said no twice." |
| 3 | **The question nobody asked in N years** | NovaPod #1, Ploise stroke and ER ads | Midpoint pivot: a professional stops and asks "How do you clean them?" | A hygienist turns the night guard over: "How are you cleaning this?" |
| 4 | **"Please STOP ___. I know that sounds insane coming from a ___"** | Dr. Sarah Mitchell (63d), Active Court (rank 13) | Expert tells you to stop the thing their own trade sells | "Please STOP soaking your retainer in fizzing tablets. I know that sounds insane coming from someone who sold them for 11 years." |
| 5 | **Insider names the category's blind spot** | Uproot Clean (60d) | "[Common product] is not made for [your situation]. The box doesn't mention that." + "It wasn't you. It was the tablet." | "Soak tablets were designed for dentures sitting in a glass, not a night guard you clench on for 8 hours." (Don't name a tablet brand; check with legal.) |
| 6 | **Skeptic investigates the 'scam'** | Better Living Daily (221d, rank 4) | "I almost didn't buy it. Thought it was another ___ scam." + an investigation + worst case vs best case + cost per day | "I Almost Didn't Buy It. Thought It Was Another Facebook Denture Gadget." This answers the survey's top objection ("too good to be true", "every brand is the same"). |
| 7 | **"By the end of this you'll be furious. Three things are happening right now"** | NovaPod Lucille Adams; GLP-1 (rank 1) | Promised emotion + a numbered reveal + "not a ___ problem, a ___ problem" | "Your retainer smell is not a hygiene problem. It's a cleaning-method problem." |
| 8 | **"I'd been treating the wrong ___" / "aimed at the wrong end"** | Mark Sullivan (146d, rank 1); SPNutrition (99d) | List every fix, then reframe: they all hit the surface, the problem lives elsewhere | "Twelve years of scrubbing the outside of a night guard. The gunk was in the grooves the brush physically can't fit into." |
| 9 | **Ritual inventory, private daily habit** | SPNutrition grinding (rank 20 of 1,069) | "Every morning, before I open my eyes, I [ritual]... never said it out loud to another human being" | "Every morning I sniff my retainer case before I open it. I've never told anyone that." |
| 10 | **Rate every method /10** | NovaPod video (rank 1, 87d) | "Best way to clean X? Let me rate everything I've seen." Tablets 2/10... ultrasonic 9/10 | Long-form static version: hygienist narrator rates tablets, toothpaste, vinegar, peroxide, a cheap pod and a 5-minute tap-water pod. |
| 11 | **Doctor-dismissal ladder plus dated diary** | Rejuveen (85d, rank 15); grinding ad | Doctor 1 / 2 / 3 brushed me off, then a specialist explains biofilm, then Day 3, 7, 14, 30 | Aligner wearer: orthodontist 1 says "brush them", the clinic says "just replace them"; then Day 1 cloudy water, Day 14 no sour taste. |
| 12 | **Founder or adult child "because of my mother/father"** | Artuvate (166d, rank 3); Ploise Ricky's daughter | "I started this because of my [mother]. I watched her stop [doing X]." | Adult child: "Dad stopped taking his teeth out in front of the grandkids." (Caregiver persona; gift angle.) |

Extra openers worth testing: the ER phone call from a sibling (#8 in the log); "I beat cancer twice... dentures were the hardest thing" (resilience contrast); "My dentist said it was normal. But I noticed things he wasn't mentioning" (#13).

---

## 5. Evidence for specific angles

**Tablet / chemical fear (persulfates)**
- The only examples are two short Denture Care Tips (Ploise) videos: m1759536091704322 (23 days, inactive) and m1668754845253706 (11 days). Transcript: "If you use fizzy denture cleaning tablets, the FDA just issued warning about them... it's called persulfate and it's a known allergen linked to serious reactions rash respiratory distress gum damage... Just water and 5 minutes... 50% off... 90-day money-back guarantee."
- Both stopped quickly, which suggests the angle did not hold.
- Every long runner attacks tablets on **reach** (they work on the surface and only mask smell), not on chemistry. Zima uses "tablets just mask the smell for a few hours". Uproot Clean (a washer cleaner) proves the "tablet after tablet, and it was never designed for your situation" story works at length.
- Cautions:
  - The FDA's persulfate communication dates from 2008 and is about allergic reactions and labeling. "Just issued" is false. Cite it accurately or not at all.
  - DentalPULSE's own Ultimate Bundle includes a 30-tablet box, so "tablets are dangerous" contradicts the bundle. Keep the frame at "tap water only, nothing to fizz" and "tablets can't reach".

**Cavities and decay from dirty aligners/retainers**
- Only in Zima video m1641516337598211 (57 days, active, rank 32): "at the same appointment, I was drilling caries off her teeth, decay caused directly by the bacteria living on her retainer."
- Also Zima: sour taste, "pH is off... Porphyromonas gingivalis" (71 days, rank 27); "Don't let dirty retainers undo years of wearing braces" (44 days, rank 6-8).
- Sonic's 998-day video: "47.2% of people using aligners suffer from periodontal diseases caused by dirty aligners."
- **No long-form exists.** The angle is open, but keep it to "my dentist found..." rather than a causal medical claim.

**Respiratory, pneumonia and Candida from dentures or night guards**
- Dentures: heavily used by Ploise/DCT. The ER aspiration-pneumonia story (153 days, active, rank 19). Ricky: "denture wearers are 2.3 times more likely to develop aspiration pneumonia."
- NovaPod: "bacteria and yeast move into those scratches... denture stomatitis" (named, but not "Candida").
- **Night guards: none found.**
- These are disease claims. brand.json bans medical treatment claims, and Meta health policy applies. Use them only as symptoms the narrator noticed (sore red gums, morning taste, smell) plus "my dentist told me", never "it prevents pneumonia".

**Mold in night guards or cases**
- No ad found for night guards or cases.
- Nearest: Zima "retainer smelt like mouldy cheese" (smell, not mold), and PAP MD's CPAP "air contaminated with mold, dust, toxins" (109 days, rank 8). Hidden contamination in a sleep device is a proven story in CPAP.
- **Open.** The case and the guard live in a dark, damp bathroom drawer: "I opened the case after a week away" is a natural scene.

---

## 6. White space nobody is running

1. **Long-form for retainers, aligners and night guards.** All 30+ long-form stories in the category are about dentures. Zima and Sonic speak to retainers and aligners only in short copy and dentist videos.
2. **Night-guard grinders (30-55).** SPNutrition proves this audience reads 11k-character stories (rank 20 of 1,069, 99 days). Nobody sells them a cleaner in long form. The hooks are a yellow, cloudy, smelly guard, a husband who turns his head, and the drawer of old guards.
3. **Parent of a teen with a retainer.** Orthodontic investment ("$6,000 of braces") plus teen breath and bullying. Only Zima's 55-character "Don't let dirty retainers undo years of wearing braces" touches it.
4. **The skeptic investigator who "thought pods were a scam".** Proven by the 221-day hearing aid ad. No pod brand answers the "every brand is the same / fake reviews" objection in a story.
5. **A tablet cost-math story.** "$20-something a box... month after month" appears as one line in NovaPod. Nobody makes the receipts or cost-per-day math the spine of the story (the hearing ad's "34 cents a day").
6. **Insider exposé from a hygienist or dental lab tech** in the Uproot repairman voice ("19 years... I pull this out of appliances on Tuesday mornings").
7. **Non-disease stakes.** Competitors escalate to stroke, heart attack and death, which carries policy and compliance risk. Dignity, intimacy and social stakes (photos, kissing, grandkids, the dinner table, dates) are proven (NovaPod's Lucille, Ploise's Sarah, the NOURI breath ad) and compliant.
8. **"Tap water only, nothing to buy again" as the hero.** Only Sonic says "just add water", and only in passing.
9. **The travel case and a week away.** The mold/case scene, "the smell when I opened it in the hotel".

Compliance notes for writing:
- No disease causation or cure claims.
- No invented counts ("5,000 dentists", "sold out 3x").
- Don't name competitor pods. It is fine to say "a cheap pod" or "a jewellery cleaner".
- The cycle is always 5 minutes.
- If tablets come up, remember that our bundle includes them.
