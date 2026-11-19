# DentalPULSE: YouTube voice-of-customer research

**Date:** 2026-11-19
**Brand:** DentalPULSE (at-home ultrasonic cleaner for dentures/partials, night guards, retainers, aligners, sleep-apnea/snore guards)
**Scope:** research only. Nothing below is ad copy. Every quote is verbatim from a YouTube comment or reply (typos kept), with the commenter's name or handle removed. Comments from channel owners and brand accounts are excluded from the quotes.

## 1. Method and sources

- **Discovery:** 17 searches through StefanBrain `web_search` covering denture cleaning, tablets vs DIY, denture whitening, adhesive removal, stomatitis, caregivers, night-guard yellowing, retainer white film and calcium, Invisalign cleaning, ultrasonic and Zima reviews, sleep-apnea appliances and Shorts.
- **Scraping:** 9 runs of StefanBrain `scrape_social_comments` (sorted by relevance, replies capped at 3–4 per thread on later runs). The CSVs were downloaded to `research/yt_raw/batch1-8.csv` and deduplicated by comment ID.
- **Corpus:** 1,261 unique comments and replies across 49 videos that had comments. 1,080 are from viewers (not channel owners).
- **View counts:** read from the YouTube watch page with `web_extract`, or from search metadata. "n/a" means the page did not return a count.
- **Scraper ceiling:** the scraper returns at most about 500 comments per run and splits them across URLs. The high-view retainer videos have thousands of comments, so this is a relevance-ranked sample, not a census.

### Videos scraped (comments retrieved > 0)

| # | Title | Channel | URL | Views | Comments pulled |
|---|---|---|---|---|---|
| 1 | Testing an Ultrasonic Retainer Cleaner from Amazon! (Short) | Hey It's Honeysuckle | https://www.youtube.com/watch?v=o0ofgyeUTP0 | 668K | 51 |
| 2 | How to Clean a Clear Retainer & Other Retainer Instructions | Premier Orthodontics | https://www.youtube.com/watch?v=DOnVF62J_c8 | 503K | 50 |
| 3 | How to Clean Retainers (Hawley, Essix, Clear, etc) | Braces Explained | https://www.youtube.com/watch?v=VP3Wpwhek3M | 396K | 50 |
| 4 | Cleaning Dentures | Robert Loney (Dalhousie prosthodontics) | https://www.youtube.com/watch?v=IdmkzfPwzhg | 232K | 26 |
| 5 | Do Dentures need to be in water over night? Does it really matter? | The Denture Clinic Canberra | https://www.youtube.com/watch?v=CftugRA4r_w | 203K | 100 |
| 6 | How to clean dentures & false teeth | Electric Teeth | https://www.youtube.com/watch?v=nI7uaeO1BZk | 177K | 26 |
| 7 | How To Clean Your Dentures Daily | Dental Concepts | https://www.youtube.com/watch?v=5ukrrO2yozo | 164K | 60 |
| 8 | How To Clean Retainers and Night Guards | Teeth Talk Girl | https://www.youtube.com/watch?v=rhmE1C9zQAg | 164K | 100 |
| 9 | Cleaning Partial Dentures | Robert Loney | https://www.youtube.com/watch?v=LRpL8ke3pgE | 161K | 30 |
| 10 | How To Clean Your Invisalign Trays | Teeth Talk Girl | https://www.youtube.com/watch?v=8PEaKmSRBis | 160K | 104 |
| 11 | Zima Dental Pod Ultrasonic Cleaner Review | Electric Teeth | https://www.youtube.com/watch?v=-aQ90sBhaNc | 135K | 100 |
| 12 | How to Remove Denture Adhesive From Gums | ehowhealth | https://www.youtube.com/watch?v=e8lRMxSU_sE | 116K | 25 |
| 13 | How to whiten yellowed false teeth & dentures | Electric Teeth | https://www.youtube.com/watch?v=QbdUwz7kKIU | 115K | 44 |
| 14 | Dental Pod Pro Honest Review - Is It worth It? | Catherine OMT, RDH | https://www.youtube.com/watch?v=0suU3t16vuE | 43K | 40 |
| 15 | How to Stop Teeth Grinding { Mouthguard for Sleeping } | Smile Influencers | https://www.youtube.com/watch?v=k4u33Vwxj7Q | 41K | 27 |
| 16 | How long can dentures stay out of water? | Electric Teeth | https://www.youtube.com/watch?v=LlyTzhI0FMU | 41K | 18 |
| 17 | Zima Pod Pro Tested / Better Than Traditional Retainer Cleaning? | Conor The Dentist | https://www.youtube.com/watch?v=h-QuD3UCUf8 | 36K | 30 |
| 18 | How To Remove DENTURE ADHESIVE from your GUMS | Real Life With Michelle | https://www.youtube.com/watch?v=rA867myU05s | 32K | 25 |
| 19 | Dental pod vs Sterilising tablets (30-second test) | Zima Dental | https://www.youtube.com/watch?v=1Jz-Hd-828k | 28.3K | 14 |
| 20 | DENTIST REVIEW OF DENTAL POD INVISALIGN/RETAINER CLEANER | thecheshirecat | https://www.youtube.com/watch?v=_w32husS6Js | 27K | 52 |
| 21 | Learn how to clean dentures... (Dentist Explains) | Bio-Hack Your Smile | https://www.youtube.com/watch?v=mGGpadhifO0 | 19K | 7 |
| 22 | How To Remove Denture Adhesive From Your GUMS | Real Life With Michelle | https://www.youtube.com/watch?v=c4B4MUz99Sc | 17K | 46 |
| 23 | Retainer Brite Review | Dr. Nathan Coughlin | https://www.youtube.com/watch?v=_pvgmfAnxN8 | 16K | 15 |
| 24 | How to Clean and Remove Calcium Deposits and Stains From Clear Retainers | Scott's Projects | https://www.youtube.com/watch?v=PJo3zO3-Ihw | 14K | 9 |
| 25 | Dentist Retainer Cleaning Routine! (Short) | Kathryn Mueller | https://www.youtube.com/watch?v=wHm1nWJg3Tk | 11.8K | 11 |
| 26 | Can an Ultrasonic Cleaner Melt Your Aligner? (Short) | invisalign journey club | https://www.youtube.com/watch?v=qG47wvUBTrA | 3.7K | 5 |
| 27 | How To Remove Denture Adhesive from your Dentures | Real Life With Michelle | https://www.youtube.com/watch?v=-oA5Fq-qsCA | 3.3K | 25 |
| 28 | How to clean your Removable Clear Retainers | n/a | https://www.youtube.com/watch?v=xW_SAulzmTU | n/a | 100 |
| 29 | How I Clean My Dentures: Polident Vs. DIY Baking Soda & White Distilled Vinegar | n/a | https://www.youtube.com/watch?v=DqcsERKyP4c | n/a | 14 |
| 30 | Zima Dental Pod Pro Ultrasonic Cleaner Review | My Private Dentist | https://www.youtube.com/watch?v=70E-0QxJrxo | n/a | 9 |
| 31 | Ultrasonic cleaner for your nightguard? (Short) | n/a | https://www.youtube.com/shorts/cT0wMvlOLNE | n/a | 10 |

The following videos had 1–5 comments each, used only where cited: Ip-74pYH2H8 (How to Clean Aligners), uDTn70wLjEQ (Retainer Cleaner 2-Month Test), qkuR75r8SZs (Retainer Brite demo), _Hrqe9PEbiQ (Honest Review of the Ultrasonic Denture Cleaner), AjddKX1_Zoc (Denture Stomatitis), aJvsFUtRL9k (Mouth Care Matters), 2DFy22Egp4Y (Clean Mouthguard Naturally), 9ntwml4NzR4 (Clean A Mouth Guard From A Dentist), NwmyKq4kIJo (Ultrasonic Cleaner Review), wuwfTB2XO2Y (SomnoDent oral appliance), Usn4rHGosoM, OJI8ygZNd0U, 0iQ1v-pWtJo, leW-MrQF-DM (Sentinel night guard yellow), Ihu9fKzkrqE (Sypnotix Zima, 5.7K views), A_NwODL5dHc, Lg0B8N6N8Mo (Short).

The following videos returned no comments (comments off, or none): ueLNqc-cl64, X8M1TizcGeI (caregiver denture care), dEOlTxPwdQs (Aspen Dental), iEnrAywfvjE, d6nxifCN_to, avsa5NUC6pc (night-guard deep clean), 5XK1eB20lGk (WebMD), 7i_2Ua6qqkw and oqj_d-5Fh1M (retainer Shorts), DhdrlPH1-QQ, 6nbZKEWTQ3g, nGQx1PxcARY (oral sleep appliance), _BOUfs89eh4.

These videos failed to scrape: tHAzd_zb1no, KD_iC9iZ3xo (hydrogen peroxide retainer Short), qqfs0prQSgY (tablets vs Dental Pod microscope test), SXAKyCmpQRw.

---

## 2. Pain points by avatar

Within each avatar, themes are ranked by how often they appear and how many likes those comments drew. Like counts are shown as (n likes) where they help.

### 2a. Denture wearer (full and partial)

**1. Nobody told them how to care for the denture, and the advice they find contradicts itself.** This was the loudest denture theme.
- "I'm sick of all the different information on cleaning the dentures" (https://www.youtube.com/watch?v=nI7uaeO1BZk)
- "just watched a video claiming never leave dentures in a glass of water over night. that video from another professional in the industry. so who is right? who is wrong? so much misinformation out here. makes it hard for us to know truth from fiction." (49 likes; https://www.youtube.com/watch?v=CftugRA4r_w)
- "I got my partial today & my dentist said to not put them in water overnight but everywhere online says you should ... I'm so confused lol" (40 likes; https://www.youtube.com/watch?v=CftugRA4r_w)
- "why does one professional say "never use bleach" and another one says "use diluted bleach" ??? hellpppppppp lol" (https://www.youtube.com/watch?v=IdmkzfPwzhg)
- "My dentist did not provide any instructions on how to care for my partial." (https://www.youtube.com/watch?v=LRpL8ke3pgE)
- "I was fitted with dentures and was told absolutely nothing about what to expect wearing or caring for them... How come there is no "what to expect list" or "how to care list" with dentures, are people supposed to mind read this?" (https://www.youtube.com/watch?v=LlyTzhI0FMU)
- "My dentist said don't use polident, it can leech into your system. True?" (https://www.youtube.com/watch?v=IdmkzfPwzhg)
- "Dentists don't know anything about dentures. They don't wear them so how they know?" (https://www.youtube.com/watch?v=rA867myU05s)

**2. Yellowing and stains, and anger when told it can't be fixed.** The whitening video drew the most-liked denture comments in the set.
- "If she's saying that they can't be whiten then how is it that they get darker??" (23 likes; https://www.youtube.com/watch?v=QbdUwz7kKIU)
- "You are purposely misleading people with the title of your video. As SOON as they begin watching, you slap the hope right out their mouths by saying the OPPOSITE of the title." (26 likes; https://www.youtube.com/watch?v=QbdUwz7kKIU)
- "Totally useless video. There ARE ways to remove stains from dentures at home." (21 likes; https://www.youtube.com/watch?v=QbdUwz7kKIU)
- "Ohhhh, just go buy a new set, that's how you accomplish whiter dentures. WOW! Thanks so much for that insight. Obvious AND expensive." (https://www.youtube.com/watch?v=QbdUwz7kKIU)
- "I smoke drink coffee my dentures get stained" (67 likes; https://www.youtube.com/watch?v=QbdUwz7kKIU)
- "Can someone please tell me how to whiten my fails teeth" (https://www.youtube.com/watch?v=QbdUwz7kKIU)
- "My dentist made them with a yellow tint" (https://www.youtube.com/watch?v=QbdUwz7kKIU)

**3. Adhesive left on the gums and palate: time, pain and frustration.** This is an adjacent pain, not a cleaner claim. It comes up nightly and drives high-intent searches.
- "This video shows NOTHING about removing denture adhesive from your GUMS." (70 likes; https://www.youtube.com/watch?v=e8lRMxSU_sE)
- "By the time I've wiped, scrubbed, picked, and gargled with scorching hot water, my gums are red, inflamed and in pain." (https://www.youtube.com/watch?v=e8lRMxSU_sE)
- "Usually im picking denture glue out for half hour or more!!!" (https://www.youtube.com/watch?v=rA867myU05s)
- "the biggest pain has absolutely been getting the glue out of my mouth... hope that it saves me an hour of time" (https://www.youtube.com/watch?v=rA867myU05s)
- "Cleaning that gunk out at night has been driving me crazy and takes me 10-15 mins to get it all." (https://www.youtube.com/watch?v=rA867myU05s)
- "it's been driving me nuts trying to get denture glue off the roof on my mouth" (https://www.youtube.com/watch?v=c4B4MUz99Sc)
- "In short has anyone figured out how to get this slime yes slime out of your mouth" (https://www.youtube.com/watch?v=e8lRMxSU_sE)

**4. Fear of damaging an expensive denture.** Scratches, dulling, warping, metal clasps, teeth coming loose.
- "Waters cheap, dentures aren't lol" (https://www.youtube.com/watch?v=5ukrrO2yozo)
- "Today a dental assistant used an abrasive cleaner and a hard brush... some of the clear shiny coating came off my brand new pearly white tooth part... they were perfect now they look flat and dull" (https://www.youtube.com/watch?v=nI7uaeO1BZk)
- "Please do not use hydrogen peroxide it will dissolve the glue that sticks the teeth to the base, over time. It has happened with me." (https://www.youtube.com/watch?v=CftugRA4r_w)
- "tablets have for me lightened the "gum" line to an unacceptable artificial looking shade" (https://www.youtube.com/watch?v=CftugRA4r_w)
- "Can denture be soaked in disinfecting cleaner overnight if it has metal clasps? Any corrosion or other damage can occur?" (https://www.youtube.com/watch?v=IdmkzfPwzhg)
- "Can you clean Titanium dentures mine went black" (https://www.youtube.com/watch?v=LRpL8ke3pgE)
- "The brush that I was given... is so abrasive it could clean a grill or oven." (https://www.youtube.com/watch?v=nI7uaeO1BZk)

**5. Bacteria and illness worry.** Present but less frequent than stains or confusion.
- "because of what the dentures are made of, they are very porous and will trap bacteria. That's why people who wear partials/dentures are at a much higher risk of getting bronchitis and pneumonia." (https://www.youtube.com/watch?v=5ukrrO2yozo)
- "I used daily toothpaste for my denture bt jerms are not clean , suggest me wht I doo" (https://www.youtube.com/watch?v=5ukrrO2yozo)
- "I keep mine in a solution of vodka and water the alcohol keeps mine from getting mold in any tiny holes in my soft liner." (https://www.youtube.com/watch?v=CftugRA4r_w)
- "I'm wondering if this problem that I have Denture Stomatitis is from using Mounjaro. I clean my teeth every night and I take my dentures off at night." (https://www.youtube.com/watch?v=AjddKX1_Zoc)
- "Will this remove h pylori from denture I have h pylori and trying to get rid of it ." (https://www.youtube.com/watch?v=LRpL8ke3pgE)

**6. Emotional weight of new dentures, and attachment to wearing them.** This is the context the cleaning routine sits in.
- "I got dentures about a month ago and I'm so depressed. I've tried to snap out of it, but some days I just can't." (https://www.youtube.com/watch?v=rA867myU05s)
- "I HATE my dentures." (https://www.youtube.com/watch?v=rA867myU05s)
- "I've a real psychological thing about not having them in my mouth!" (https://www.youtube.com/watch?v=CftugRA4r_w)
- "Thank you for mentioning you CAN keep dentures in your mouth over night! Usually dentists say strictly "no" , I just simply can not sleep without." (57 likes; https://www.youtube.com/watch?v=CftugRA4r_w)
- "Being horrified and embarrassed, I removed the dentures and left them in the glove box for over half a year" (https://www.youtube.com/watch?v=LlyTzhI0FMU)
- "I hate my immediate dentures. I have horse lip going on." (https://www.youtube.com/watch?v=-oA5Fq-qsCA)

**7. Dexterity and effort.** Thin, but relevant to the 60+ buyer.
- "I also have RA in my hands and don't think I could take them out and put them back in daily." (https://www.youtube.com/watch?v=CftugRA4r_w)
- "I can't do that I gag easily I don't like the feel of microfiber." (https://www.youtube.com/watch?v=-oA5Fq-qsCA)
- "Gosh, that's a lot of domestic water waste to brush lower dentures, especially if you brush them 3 times a day as I do" (https://www.youtube.com/watch?v=5ukrrO2yozo)

### 2b. Denture caregiver (adult child, spouse, care staff)

The signal here is thin (see Gaps), but every quote found points to the same need: someone else is doing it, or should be.
- "I'm trying to help my granny keep her dentures clean but she can't see too well." (https://www.youtube.com/watch?v=_w32husS6Js)
- "Is Dettol hand wash good for cleaning it? Asking for a relative. She has been told to use the tablet once a month for cleaning." (https://www.youtube.com/watch?v=5ukrrO2yozo)
- "I'm planning to share this with caregivers of seniors in an assisted living facility" (12 likes; https://www.youtube.com/watch?v=IdmkzfPwzhg)
- "My mother never put her dentures in water. She cleaned them at night and she put thim back in her mouth... So that way her mouth wouldn't become incaved." (88 likes, the top comment on that video; https://www.youtube.com/watch?v=CftugRA4r_w)
- "My mum always kept her dentures in her mouth over night. She only ever removed them to clean." (https://www.youtube.com/watch?v=CftugRA4r_w)
- "My husband just got a temporary denture type appliance... I told him to put water in it and keep it moist at night" (https://www.youtube.com/watch?v=CftugRA4r_w)
- "My husband does that. I thought he was just being gross." (https://www.youtube.com/watch?v=OJI8ygZNd0U)

### 2c. Night guard (bruxism) wearer

**1. White buildup and yellowing that soaks won't shift.**
- "my night guard has white buildup on it. i clean them everyday using foaming soap... i have also done a weekly clean with White Vinegar (30 min) then Peroxide (30 min) and none of the white (calcium? Plaque?) build up ever goes away. what can i do? this is so gross! please please PLEASE HELP!!!!!" (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "My guard bcm yellow how I don't m using washing tablets also" (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "it seem like some yellow stuff is bulding and my dentist usually clean it with ultrasound before covid and not anymore. I am looking for a way to deep clean it" (https://www.youtube.com/watch?v=8PEaKmSRBis)
- "staining increased over the years" (from a long-time guard wearer; https://www.youtube.com/watch?v=-aQ90sBhaNc)
- "I got a night guard and I got both the cleaner and the tablets cause the thing grosses me out" (https://www.youtube.com/watch?v=1Jz-Hd-828k)

**2. Cracking and breakage from grinding, and the cost of replacing.**
- "Fifth night in and i have fractured my guard in two places." (https://www.youtube.com/watch?v=k4u33Vwxj7Q)
- "my essix + retainer is cracked because I grind through it" (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "my night guard, it looks like is cracking already has a long crack on the outside where I bite down." (https://www.youtube.com/watch?v=rhmE1C9zQAg)

**3. Confusion over cleaning products.**
- "My dentist told me not to use denture cleaner because it just turns it yellow" (https://www.youtube.com/shorts/cT0wMvlOLNE)
- "Can I put my night time mouth guard in my ultrasonic jewelry cleaner?" (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "once a week a soak it in mouthwash all day and scrub it with toothpaste and a toothbrush" (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "Cleaning the guard with toothpaste seemed like the 'of course' ... right, back into the bathroom I go!" (https://www.youtube.com/watch?v=rhmE1C9zQAg)

**4. Grinding context: stress, pain, and a guard that has to last.**
- "living with this is like hell since at times I do grind them while awake" (https://www.youtube.com/watch?v=k4u33Vwxj7Q)
- "My teeth already damaged from night grinds" (https://www.youtube.com/watch?v=k4u33Vwxj7Q)
- "I've been using a night guard since 1994... That guard lasted from 1994-2018, not a bad run! Of course, it was not very pretty but it was clean every night going in" (https://www.youtube.com/watch?v=-aQ90sBhaNc)

### 2d. Retainer wearer (adult)

**1. Spit, stink and the gross-out factor.** These are the most-liked comments in the whole corpus.
- "I have the clear retainers .I hate how they always fill up with spit..it's so gross" (1,600 likes; https://www.youtube.com/watch?v=VP3Wpwhek3M)
- "they stink in the morning" (342 likes; https://www.youtube.com/watch?v=VP3Wpwhek3M)
- "Yep, and they STANK afterwards." (https://www.youtube.com/watch?v=VP3Wpwhek3M)
- "SO TRUE AND IT STINKS WHEN YOU REMOVE AND WEAR AGAIN UGH" (https://www.youtube.com/watch?v=VP3Wpwhek3M)
- "I need that so bad my retainer is just ICK" (33 likes; https://www.youtube.com/watch?v=o0ofgyeUTP0)
- "the morningbreath smell on it.. yuck." (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "I hate the smell of the retainer and case" (https://www.youtube.com/watch?v=xW_SAulzmTU)

**2. Their provider never told them how to clean it, or told them wrong.**
- "My dentist didn't tell me how to clean my retainers so this really helps" (1,100 likes; https://www.youtube.com/watch?v=VP3Wpwhek3M)
- "after a year of scrubbing my retainers with the same toothbrush I use for my teeth and using toothpaste, I figured out I've been doing it wrong all THIS TIMEE... My orthodontist did me dirty" (554 likes; https://www.youtube.com/watch?v=VP3Wpwhek3M)
- "I'm so stupid... I've been using tooth paste the whole time." (330 likes; https://www.youtube.com/watch?v=xW_SAulzmTU)
- "My orthodontist told me to clean my retainers with toothpaste and now they look nasty? How to I fix that" (33 likes; https://www.youtube.com/watch?v=xW_SAulzmTU)
- "My orthodontist gave me a paper that said NOT to brush my retainers with toothpaste, in all caps. But they told me I SHOULD wash them with toothpaste. What do I do????" (https://www.youtube.com/watch?v=xW_SAulzmTU)
- "My dentist told me to use toothpaste on my clear retainers. I ended up with build up and 4 cavities. I'm so angry at him." (https://www.youtube.com/watch?v=rhmE1C9zQAg)

**3. White film, cloudiness and calcium crust.**
- "i have retainers clean them everyday but they had this white powder any clue what it is?" (https://www.youtube.com/watch?v=VP3Wpwhek3M)
- "I have white spots on my retainers, how do I get rid of them?" (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "Toothpaste turned my retainer white" (https://www.youtube.com/watch?v=xW_SAulzmTU)
- "My bleaching trays have developed a white film over the years. Is that bacteria?... It will cost me $400 to replace the trays" (https://www.youtube.com/watch?v=-aQ90sBhaNc)
- "do you have any advice for cleaning my extremely dirty retainers? i'm afraid that continued use of them will eventually cause infection" (https://www.youtube.com/watch?v=-aQ90sBhaNc)

**4. Cost of replacing, and lifelong wear.**
- "I just got mine today and I didn't realise it was a lifelong thing" (1,100 likes; https://www.youtube.com/watch?v=DOnVF62J_c8)
- "my teeth shifted like tectonic plates. I had to get braces for a second time!" (362 likes; https://www.youtube.com/watch?v=DOnVF62J_c8)
- "adult me just had to spend almost $4k to do all that over again." (https://www.youtube.com/watch?v=DOnVF62J_c8)
- "At £750 to replace them (set of three) this isn't something I can afford" (https://www.youtube.com/watch?v=-aQ90sBhaNc)

**5. Soap taste.** Recommended methods leave a taste, which pushes people toward other methods.
- "I just cleaned my retainers using the soap method. Gross! Don't do it, unless you don't mind the soapy after taste." (104 likes; https://www.youtube.com/watch?v=xW_SAulzmTU)
- "i hate having a soapy taste in my mouth…. what should i do?" (https://www.youtube.com/watch?v=xW_SAulzmTU)
- "Why does my retainer taste so soapy" (https://www.youtube.com/watch?v=DOnVF62J_c8)
- "they make the retainer taste like cleaning supplies which is nasty lol" (about tablets; https://www.youtube.com/watch?v=rhmE1C9zQAg)

### 2e. Retainer parent (parents of teens)

There are no direct parent comments in the sample (see Gaps). Teen commenters do describe the dynamics a parent pays for:
- "I don't want my mom to be paying the treatment again." (https://www.youtube.com/watch?v=DOnVF62J_c8)
- "Fr don't put it in a napkin lmao I've lost them so many times like that" (324 likes; https://www.youtube.com/watch?v=DOnVF62J_c8)
- "my dad threw the cup out not knowing that my retainers were in there... I still kind of hold that against him." (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "I spent the next days dumpster diving before finding it and saving $500." (https://www.youtube.com/watch?v=rhmE1C9zQAg)
- "I dont wear my retainers cause i wanna keep them clean" (314 likes; https://www.youtube.com/watch?v=xW_SAulzmTU)
- "Looks like a lot of work looking after a retainer" (https://www.youtube.com/watch?v=rhmE1C9zQAg)

### 2f. Aligner (Invisalign) wearer

**1. Odor and staining despite rinsing.**
- "my invisalign smell bad what can i do for that" (https://www.youtube.com/watch?v=8PEaKmSRBis)
- "the first week with only rinsing and brushing my aligners, they developed an odor." (https://www.youtube.com/watch?v=8PEaKmSRBis)
- "as it was an "emergency" I drank some coffee with the aligners in - oh oh they stained!" (https://www.youtube.com/watch?v=8PEaKmSRBis)
- "I used to use toothpaste and then i thought why are there stains" (https://www.youtube.com/watch?v=8PEaKmSRBis)

**2. No guidance from the brand or the office.**
- "What's weird is that Invisalign offers no info." (25 likes; https://www.youtube.com/watch?v=8PEaKmSRBis)
- "My dental assistant said just rinse them with water 🙃🙃 it's like nobody knows" (https://www.youtube.com/watch?v=8PEaKmSRBis)
- "Mine told me to use toothpaste 😞 they just be lying" (https://www.youtube.com/watch?v=8PEaKmSRBis)

**3. Routine overload. Cleaning has to fit around meals, so they look for a drop-in step.**
- "I feel it's a hassle to remove them just for a snack and then floss and brush and put them back in." (https://www.youtube.com/watch?v=8PEaKmSRBis)
- "I clean my Invisalign aligners each evening while I eat supper using an ultrasonic cleaner and a Polident tablet." (https://www.youtube.com/watch?v=8PEaKmSRBis)
- "I can simply just drop these in here, press the button, walk away" (this is the video's own transcript, not a comment; listed as an angle signal only; https://www.youtube.com/watch?v=_BOUfs89eh4)
- "The Invisalign ultrasonic cleaner has been sold out for months so I am looking for a good alternative." (https://www.youtube.com/watch?v=8PEaKmSRBis)

**4. Fear of heat, warping and chemicals.**
- "I noticed that even if I put cold water in it, while it cleans the aligners, it warms the water. I'm bothered if the aligners can be damaged or deformed" (https://www.youtube.com/watch?v=-aQ90sBhaNc)
- "Did you use warm or cold water? Concerned about melting my retainer if it gets too warm" (https://www.youtube.com/watch?v=h-QuD3UCUf8)
- "I'm trying to avoid using my retainer tablets due to a possible allergic r[eaction]" (truncated in source; https://www.youtube.com/watch?v=8PEaKmSRBis)
- "My dentist told me to only use a little bit of the cleaning crystals everyday so they last long. I got sick." (https://www.youtube.com/watch?v=8PEaKmSRBis)

### 2g. Sleep-apnea / snore appliance wearer

Very little on YouTube (see Gaps). Everything found:
- "My splint is for sleep apnoea...tablets work fine but, I'm trying the pod...it made NIL difference over 2 days." (https://www.youtube.com/watch?v=-aQ90sBhaNc)
- "I have a tap3 sleep apnea night guard that has some metal parts in it. Will this word for that?" (https://www.youtube.com/watch?v=_w32husS6Js)
- "Can it be stored through the day in water after cleaning?" (https://www.youtube.com/watch?v=wuwfTB2XO2Y)
- "For some reason, It gets harder for me to breathe when I lay down." (denture wearer explaining why she sleeps in them; https://www.youtube.com/watch?v=-oA5Fq-qsCA)

---

## 3. Failed fixes people describe

| Fix | What they did | What happened (verbatim) | Source |
|---|---|---|---|
| **Toothpaste** | Brushed retainers, aligners or dentures with toothpaste | "Now my retainers are all scratched up." | rhmE1C9zQAg |
| | | "Toothpaste turned my retainer white" | xW_SAulzmTU |
| | | "I ended up with build up and 4 cavities." | rhmE1C9zQAg |
| | | "I used to use toothpaste and then i thought why are there stains" | 8PEaKmSRBis |
| | | "I used daily toothpaste for my denture bt jerms are not clean" | 5ukrrO2yozo |
| **Denture tablets (Polident, Efferdent) on retainers or guards** | Soaked clear plastic in denture tabs | "After a few uses, the upper retainer started cracking (and disintegrating)." | rhmE1C9zQAg |
| | | "They got pretty foggy" | rhmE1C9zQAg |
| | | "My dentist told me not to use denture cleaner because it just turns it yellow" | shorts/cT0wMvlOLNE |
| | | "Well, I've used tablets religiously and my retainers are now badly discoloured" | h-QuD3UCUf8 |
| **Denture tablets on dentures** | Nightly tabs | "tablets have for me lightened the "gum" line to an unacceptable artificial looking shade" | CftugRA4r_w |
| | | "My doctor recommended not using the efferedencent tablets at all. She said dentures are pourius and these tablets will eventually ruin them." (27 likes) | CftugRA4r_w |
| **Tablets in general** | Short soak | "it looked like it only cleaned half of it, which is the issue i'm dealing with while using this" (Retainer Brite) | _pvgmfAnxN8 |
| | | "I have this and it doesn't work. It may reduce bacteria, but the yellowing doesn't come clean. I clean mine nightly with tablets." | -aQ90sBhaNc |
| **Vinegar + peroxide** | Weekly soak, 30 min each | "none of the white (calcium? Plaque?) build up ever goes away" | rhmE1C9zQAg |
| **Vinegar** (believers) | White vinegar soak | "A white vinegar soak did the trick for mine." | PJo3zO3-Ihw |
| | | "1 part cleaning vinegar, 2 parts warm water and touch baking soda... I have cleaned up my yellow retainers" | -aQ90sBhaNc |
| **Hydrogen peroxide** (split) | Soak or brush | Pro: "i use peroxide to clean them mixed with poligrip tablets in a cup over night... they sparkling clean." (67 likes) | QbdUwz7kKIU |
| | | Con: "Please do not use hydrogen peroxide it will dissolve the glue that sticks the teeth to the base, over time. It has happened with me." | CftugRA4r_w |
| **Bleach** | Advised by dentist | "They told me to clean mine with bleach dilution in water and everyone online is saying NOOOOO" | CftugRA4r_w |
| **Baking soda** | Overnight soaks | "I soak my dentures overnight in vinegar and baking soda. Is this safe" (no answer about results) | IdmkzfPwzhg |
| | Taste problem | "the reason I use toothpaste is to get rid of the vinegar and baking soda taste" (video creator reply) | DqcsERKyP4c |
| **Soap (dish or hand)** | Recommended routine | "Gross! Don't do it, unless you don't mind the soapy after taste. It remained, even after the heavy rinsing." (104 likes) | xW_SAulzmTU |
| | | "I used soap but now my retainer tastes like soap" | rhmE1C9zQAg |
| | | "You are kidding me, dish washing liquid. No" | 5ukrrO2yozo |
| **Brushing only** | Daily brush | "over time I've found I still get a bit of build up where the toothbrush just cant get to." | _w32husS6Js |
| | | "I have had my retainers for 2 years, i brush and clean them after every meal religously, and they are still yellow" | 1Jz-Hd-828k |
| **Rinsing only** | Water rinse | "It already felt not clean enough and the morningbreath smell on it.. yuck." | rhmE1C9zQAg |
| **Mouthwash** | Soak | Mixed: "I tried the mouthwash cleaning method and it worked for me!" vs "Don't use mouth wash! The alcohol in it could mess it up" | xW_SAulzmTU |
| **Fringe DIY** | Various | "STAIN AWAY... I've even left them in the solution for a week" (38 likes); "stain away and magic eraser"; "hydrogen peroxide and put under a uv light for 24hrs"; "vodka and water" | QbdUwz7kKIU, CftugRA4r_w |

**Pattern.** Three things repeat. Toothpaste scratches clear plastic and clouds it. Denture tablets used on retainers and guards are blamed for cracking, fogging and yellowing. Soap leaves a taste. Viewers swap remedies endlessly (vinegar, peroxide, Stain Away, Magic Eraser, UV, vodka) and contradict each other, which makes the "nobody agrees" confusion worse.

---

## 4. Ultrasonic cleaner comments

### Believers
- "My retainers went from embedded brown and yellow stains and covered constantly in plaque, to looking pristine and crystal clear. I never saw plaque on them again after buying this unit." (https://www.youtube.com/watch?v=-aQ90sBhaNc)
- "I have one and love it! I use mine once in the morning and once at night. I've seen the junk come off them while using it" (18 likes; -aQ90sBhaNc)
- "my badly stained brown and yellow aligners that I had to literally scrape plaque off of with a toothpick, became crystal clear and pristine." The same commenter adds that they soaked overnight with a whitening denture tablet before running it. (-aQ90sBhaNc)
- "it works wonders with my dentures/ nightguard." (8PEaKmSRBis)
- "My 6 year old invisalign retainer that I have to wear nightly is clean now. I don't even use the cleaning tablets" (0suU3t16vuE)
- "Since I've been using Polident with an ultrasonic cleaner daily, that problem has been eliminated." (about odor; 8PEaKmSRBis)
- "Ultrasonic cleaner would do the job perfectly" (on a denture video; IdmkzfPwzhg)

### Conditional believers: "works on new, not on old"
This is the most common nuanced view.
- "it works well for keeping aligners looking new, not so great for cleaning well-worn dirty ones." (41 likes; -aQ90sBhaNc)
- "I think it may only marginally improve very old and stained appliances, but keep new ones very clean since they never get the chance to build up grime." (-aQ90sBhaNc)
- "Maybe it's best to use this from new. As soon as you have cleaned with a brush or have built in dirt it will be hard to get rid off." (-aQ90sBhaNc)
- "Better clean than just washing for sure, but don't expect it to completely clean an older discoloured retainer back to brand new." (_w32husS6Js)
- "ik this thing is a gimmick if their extremely dirty but for regular everyday cleaning it dosent look so bad" (0suU3t16vuE)

### Skeptics
- "I've been contemplating whether to buy this but after watching your video, no thank you... You have saved me from spending £70" (141 likes, the top comment; -aQ90sBhaNc)
- "As a dentist I often find that the staining is not always on the appliance itself, but on/in the calcified deposits... Ultrasonic baths will not do this." (125 likes; -aQ90sBhaNc)
- "You would think for $100 this one would work well, but as I expected, it doesn't work any different than a $20 cleaner. Oh well... i give up." (-aQ90sBhaNc)
- "Just get a ultrasonic cleaner for jewelry for a fraction of the price, exactly the same thing" (0suU3t16vuE)
- "From what I understand it's the tablet that does all the work." (h-QuD3UCUf8)
- "When it worked I didn't notice any better than just using tablets vs the machine." (h-QuD3UCUf8)
- "Yeah I bought one too, it doesn't work, brushing your oral appliance is wayy better and cleaner" (-aQ90sBhaNc)
- "I tried he highest rated Amazon one and felt it did sweet F all." (-aQ90sBhaNc)
- "no plain water is added to this. Disinfectant liquid and possibly deionized water should be added" (545 likes; o0ofgyeUTP0)
- "Isn't it just as effective (and cheaper) to just soak my vivera trays in vinegar?" (70E-0QxJrxo)
- "Your guard has no yellow at all so how do we know how good it is that matches the miraculous videos?" (h-QuD3UCUf8)
- "I have taken my appliance to the dentist and he cleaned it perfectly and at no cost" (-aQ90sBhaNc)

### "Is it even working?" (the buzzing-water doubt)
- "I can hear a very gentle buzzing but can't feel a thing. Certainly no Jurassic park style vibrations visible. Is this right? Does this sound like it's working properly?" (-aQ90sBhaNc)
- "Mine makes a buzzing noise, too. Is that normal?" (shorts/cT0wMvlOLNE)
- "How can an object get fully cleaned if it is resting on the bottom of the tank?" (70E-0QxJrxo)
- "How well does it work without the tablets (just water)?" (_w32husS6Js)
- "Its just water correct? Do i I have to rinse it or anything prior to putting them in my mouth?" (-aQ90sBhaNc)
- "She's still traumatized by the dentist's drilling 😂" (1,000 likes, about the noise; o0ofgyeUTP0)

### Durability and warranty: a strong negative cluster against Zima specifically
- "Mine only lasted 8 months. Still under warranty but you have to jump through a ton of hoops... I've never had to fight a company this hard to get them to honor a warranty." (31 likes; 0suU3t16vuE)
- "Mine broke after just 8 months. Past the 6 months warranty. Don't waste your money." (_w32husS6Js; the same text also appears on -aQ90sBhaNc)
- "Mine stopped working after 7 months. Disappointed." (0suU3t16vuE)
- "My Dental Prod Pro has just died after 14 months of daily use" (0suU3t16vuE)
- "This is the second time I've bought this product and it has become broken both times." (-aQ90sBhaNc)
- "Don't waste your money, mine stopped working after te first month of use." (h-QuD3UCUf8)
- "I got a cheap $50 dollar version that the timer crapped out in three days" (h-QuD3UCUf8)
- "After reading comments. I realized i'm not the only one who is getting temporary joy before those devices decide to not work anymore." (0suU3t16vuE)
- "The device is not durable at all and that will likely brick it." (_w32husS6Js)

### Trust and sponsorship skepticism
- "Was this a sponsored video? Seems like it" (42 likes; 0suU3t16vuE)
- "Thank you for stating that you did not receive any payment or incentive for the review. Gives you a lot of credibility" (64 likes; h-QuD3UCUf8)
- "Very bias... I don't appreciate this misleading marketing." (on Zima's own tablets-vs-pod test; 1Jz-Hd-828k)
- "Except the tablets are supposed to be used for 15 mins 😅 so of course they "didn't work" (yet)." (25 likes; 1Jz-Hd-828k)
- "Anyone else getting bombarded with ads for this product now?" (h-QuD3UCUf8)

### Practical friction
- Counter space and looks: "But they look ugly on my countertop"; "An item like this will have to do better than 30% to get on my vanity."
- Power cord: "it is an ugly, permanently coiled, cheap-as-it-gets power cord"
- Pod hygiene: "I heard that the pods don't really dry... which creates bacteria"
- Tablet cost lock-in: "no tablets...hmmm...but you need their tablets at 4x the price."
- Denture fit: "Can a set of full dentures fit in the original pod?" (0suU3t16vuE). Also "Hi DIma would this work for dentures?" (_w32husS6Js)

### Comparisons named by commenters
Zima Dental Pod and Pod Pro, Zima Go UV, "Invisalign ultrasonic cleaner", iSonic, generic Amazon or Temu units, jewelry ultrasonic cleaners, Retainer Brite, Polident 3-Minute, Efferdent, Crest, Stain Away, Cleanadent / Dr. B sonic cleaner, "ion sanitizer", UV pods ("Do UV pods work better than this?").

---

## 5. Video angles: which pull views and comments (pattern notes, not copy)

1. **The gross reveal or live test beats instruction.** The single highest-view video was a creator testing an Amazon ultrasonic cleaner in a Short (668K). Its top comments are about the noise and the dirty water ("ICK", "disgusting"), not about cleaning method. The visual of dirty water after a cycle drives engagement, and it also triggers "add solution, not plain water" corrections (545 likes).
2. **Orthodontist "how to clean your retainer" explainers are the traffic giants** (Premier Orthodontics 503K, Braces Explained 396K). Their top comments are confessions and complaints: "my dentist didn't tell me", "I've been doing it wrong", "it fills with spit", "lifelong?!". These carry 300–1,600 likes, far more than any comment on the denture videos.
3. **Denture videos hold steady at 115K–232K views over 6–8 years.** The most heated comments land where a title promises a fix and the video denies it (the whitening video: "slap the hope right out their mouths") or answers the wrong question (adhesive "from gums" that shows dentures: 70 likes). Unmet-promise titles generate anger and long threads.
4. **"Myth vs. what your dentist says" debates go deep.** The overnight-water video (203K) has the deepest denture threads. People share family rituals and contradicting dentist advice.
5. **"Honest review / is it worth it" for Zima pulls skeptic-heavy threads.** Electric Teeth's lukewarm Zima review (135K) has a top comment of "saved me £70" (141 likes). Durability failures and "sponsored?" accusations dominate the Pod Pro reviews.
6. **Dentist or hygienist authority plus a disclosure earns trust** ("did not receive any payment" got 64 likes). Brand-run comparison clips (Zima's 30-second tablet test, 28K) draw "misleading" pushback.
7. **Denture-life creators (Real Life With Michelle)** have smaller view counts (3K–57K) but very warm, high-trust 50+ commenters. The adhesive-removal pain shows up here most clearly.
8. **Shorts on night guards and ultrasonic cleaners** returned few comments in this sample. Their engagement looks driven by the visual, not discussion.

---

## 6. Language bank (short verbatim phrases)

**Disgust**
- "it's so gross"
- "they stink in the morning"
- "they STANK afterwards"
- "my retainer is just ICK"
- "the morningbreath smell on it.. yuck."
- "this is so gross!"
- "the thing grosses me out"
- "Why is your retainer so disgusting?"
- "covered constantly in plaque"
- "embedded brown and yellow stains"
- "had to literally scrape plaque off of with a toothpick"
- "this slime yes slime"
- "Cleaning that gunk out at night"
- "I feel like my mouth is a pool of saliva"
- "the spit is super thick"
- "now they look nasty"

**Shame and embarrassment**
- "I'm so stupid... I've been using tooth paste the whole time."
- "I've been doing it wrong all THIS TIMEE"
- "Being horrified and embarrassed"
- "something to laugh at for the next 8 months"
- "I thought he was just being gross."
- "If only I knew"
- "I wish I had seen this video a long time ago."
- "Gosh where was this tutorial when I was on tray 1"

**Fear and worry**
- "I'm afraid that continued use of them will eventually cause infection"
- "Is that bacteria?"
- "it can leech into your system"
- "much higher risk of getting bronchitis and pneumonia"
- "I doubt if the dentures are any good now."
- "Concerned about melting my retainer"
- "Waters cheap, dentures aren't"
- "It will cost me $400 to replace the trays"
- "this isn't something I can afford"
- "my teeth shifted like tectonic plates"

**Frustration and confusion**
- "I'm sick of all the different information"
- "so who is right? who is wrong?"
- "so much misinformation out here"
- "I'm so confused lol"
- "hellpppppppp lol"
- "it's like nobody knows"
- "My orthodontist did me dirty"
- "What's weird is that Invisalign offers no info."
- "are people supposed to mind read this?"
- "none of the white... build up ever goes away"
- "it's been driving me nuts"
- "my gums are red, inflamed and in pain"
- "takes me 10-15 mins to get it all"
- "I HATE my dentures."
- "Oh well... i give up."

**Skepticism**
- "saved me from spending £70"
- "it doesn't work any different than a $20 cleaner"
- "a fraction of the price, exactly the same thing"
- "it's the tablet that does all the work"
- "did sweet F all"
- "it made NIL difference"
- "this thing is a gimmick if their extremely dirty"
- "Was this a sponsored video?"
- "misleading marketing"
- "matches the miraculous videos?"
- "Is this right? Does this sound like it's working properly?"
- "temporary joy before those devices decide to not work anymore"
- "Mine broke after just 8 months."
- "Don't waste your money"

**Relief and delight**
- "it's a game changer"
- "pristine and crystal clear"
- "I've seen the junk come off them"
- "I can't even imagine how I made it without it"
- "don't know how I survived without it"
- "couldn't be loving it more"
- "My mouth never felt this good"
- "This is God sent advice!!!"
- "I now feel confident in caring for my partial."
- "clean every night going in"
- "Since I've been using Polident with an ultrasonic cleaner daily, that problem has been eliminated."

---

## 7. Gaps and caveats

1. **The 60+ denture voice is under-represented compared with teen retainer voices.** The high-like comments come from retainer videos with young audiences. Denture comments are fewer and carry fewer likes, but they are more emotional. Facebook groups, Reddit (r/Dentures), Amazon reviews and the brand's own survey data are better sources for the core buyer.
2. **Caregivers and adult children** appear in only a handful of comments. Caregiver how-to videos (X8M1TizcGeI, CNA skill videos) had comments disabled or none. A Facebook or caregiver-forum pass is needed.
3. **Parents of teens:** no direct parent comments were found. Teen comments imply the parent pays for replacements but don't speak for the parent.
4. **Sleep-apnea and snore appliances:** almost no YouTube discussion (two oral-appliance videos had 0–2 comments). Try Reddit r/SleepApnea, CPAP forums and Amazon reviews of SomnoDent and similar devices.
5. **Denture stomatitis and thrush, "what happens if you don't clean":** these videos had 0–3 comments. The bacteria and infection fear exists but is rarely stated on YouTube. The brand's 68% "bacteria" buying reason is not mirrored here; YouTube skews to stains, smell and confusion.
6. **Sonic Dental** was not named by any commenter. Generic "cheap Amazon" units come up only through skeptic and durability comments.
7. **Scraper limits:** about 500 comments per run, relevance-sorted, so the sample is biased toward top-liked threads. Four target videos failed to scrape, including the dentist's microscope test of tablets vs Dental Pod (qqfs0prQSgY). View counts are missing for 4 scraped videos.
8. **The ultrasonic-on-dentures question** ("Can a set of full dentures fit in the original pod?", "would this work for dentures?") shows denture wearers are unsure whether these devices are meant for them. Only one low-comment denture-specific ultrasonic review was found (_Hrqe9PEbiQ, 3 comments, all complaints about the review itself).
9. **No claims verified.** Commenter statements about peroxide dissolving glue, tablets corroding metal, pneumonia risk and so on are viewer opinions recorded as voice-of-customer data, not facts.

**Raw data:** `/tmp/claude-0/-home-user-claude-code-sam/b14e6468-d10c-5406-98b7-38996103101c/scratchpad/research/yt_raw/batch1-8.csv` (untrusted scraped data; contains commenter handles, so do not publish). The merged, deduplicated file is `.../research/all_comments.tsv`.
