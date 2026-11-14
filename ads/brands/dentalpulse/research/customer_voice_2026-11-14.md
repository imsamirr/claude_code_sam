# DentalPULSE Customer Voice, 14 Nov 2026

**Purpose:** Collect the exact words wearers of dentures, night guards, retainers and aligners use for their pains, gross moments, fears, failed fixes and doubts, for use in Meta static ad copy.
**Builds on:** `feedback_deep_dive.md` (sections 1-9 cover 167 responses; section 10 is the Oct 28 refresh at 180). This file does not repeat that work. It adds the new survey responses and outside forum and review language.
**Privacy:** Survey data appears here only as aggregates and short anonymous quotes. No names, emails, order numbers or raw rows. Forum and review usernames are left out too; each quote is cited by site and thread only.
**Method:** Survey free text was keyword-coded and then checked by hand. One response can count toward several themes. Counts marked "~" are keyword counts, so treat them as rough. Quotes are verbatim, apart from small typo fixes in survey answers (for example "invisilign" became "Invisalign").

---

## (a) Sources and what was reachable

| Source | Reachable? | Notes |
|---|---|---|
| Feedback sheet "DentalPULSE Feedback (Responses)" (Drive) | **Yes** | The CSV export and `read_file_content` both show a single tab, "Form Responses 1", range A1:K202, so **201 responses** from 4 May to 14 Nov 2026. No other tab exists, so the export covers every row. |
| reddit.com (www, old.reddit, `.json` endpoints) | **No** | WebFetch says "unable to fetch from www.reddit.com / old.reddit.com". curl returned HTTP 403, and the sandbox then blocked further direct attempts. WebSearch with `allowed_domains: reddit.com` returned "domains not accessible to our user agent". Open web searches for "reddit ..." queries returned **no reddit.com results**, so this file contains **no Reddit quotes**. |
| ThriftyFun forums | Yes | "Smelly Mouth Guard" and "Cleaning a Mouth Guard" threads, about 35 replies. This is the richest outside source for night-guard smell language. https://thriftyfun.com/Smelly-Mouth-Guard.html, https://thriftyfun.com/Cleaning-a-Mouth-Guard.html |
| Hometalk | Yes | "How to clean plastic nightguard?" https://www.hometalk.com/39119020/diy/tile |
| Straight Dope boards | Yes | "Denture care" https://boards.straightdope.com/t/denture-care/604889 and "Ask the 25 Year Old with Dentures" (p.2, thin) |
| Mumsnet | Yes | "To ask if anyone has partial dentures (please don't laugh)" and "stinky breath" threads (embarrassment language) |
| SIGforum | Yes | "Teeth Grinding--Bruxism" (night guard cost and replacement) |
| Trustpilot | Partly | Zima Dental UK, 1-3★ filter and pages 4/8 (https://uk.trustpilot.com/review/zimadental.co.uk); Zima Dental .co (10 reviews). No DentalPULSE Trustpilot profile was found. |
| Loox review wall (Zima US) | Yes | https://loox.io/s/VkWk-zlv9q. These are competitor-hosted reviews and skew positive, but they are useful for before-state language. |
| The Gadgeteer review of an ultrasonic retainer cleaner ("Shaking the ewww away") | Yes | https://the-gadgeteer.com/2025/06/15/ueofen-ultrasonic-retainer-cleaner-review-shaking-the-ewww-away/ |
| RealSelf (Invisalign reviews) | Search snippets only | The pages themselves returned 403. Snippets are used for aligner smell and cloudiness and are marked as snippets. |
| Amazon review pages, Kimola Amazon summaries, Desertcart (mirrors of Amazon reviews), Fakespot, Apartment Therapy, MetaFilter, Dental Fear Central | **No** | Amazon 503; Kimola 410; Desertcart/RealSelf/MetaFilter/Dental Fear Central 403; Fakespot redirects (shut down). A few Amazon-style fragments survived in search snippets and are marked as snippets. |

**Bottom line:** The survey is complete. Reddit could not be reached at all. Outside language comes from older forums (ThriftyFun, Hometalk, Straight Dope, Mumsnet), from Trustpilot and Loox reviews of the main competitor (Zima), and from search snippets. Night guard and retainer language is well covered. Outside denture language is thin; the survey covers dentures well.

---

## (b) Feedback sheet update vs the Oct 28 refresh

**Labelling note:** The Oct 28 refresh says "180 responses ... to 11 Oct", but its star counts and quotes match the responses up to **26 Oct**. The first pass, 167 responses, did end on 11 Oct. This update therefore compares against 180 and also shows the **34 responses after 11 Oct**, as requested.

### Totals

| | Oct 28 refresh | **Now (14 Nov)** | Change |
|---|---:|---:|---:|
| Responses | 180 | **201** | +21 since the refresh (28 Oct to 14 Nov); 34 since 11 Oct |
| 5★ / 4★ / 3★ / 2★ / 1★ | 74 / 33 / 22 / 14 / 37 | **82 / 35 / 26 / 20 / 38** | +8 / +2 / +4 / +6 / +1 |
| Average ★ | ~3.53 | **3.51** | flat |
| % 4-5★ / % 1-2★ | 59% / 28% | **58% / 29%** | flat |

### Appliance split (normalized; "night guard & retainer" counted as night guard; apnea and snore devices as other)

| Appliance | All 201 | % | Oct 28 | Post-11 Oct (34) | Since 28 Oct (21) | Avg ★ (all) |
|---|---:|---:|---:|---:|---:|---:|
| Denture / partial | 100 | 50% | 99 (55%) | 5 (15%) | 1 | 3.75 |
| Night guard / mouth guard | 50 | 25% | 41 (23%) | **16 (47%)** | **11 (52%)** | 3.14 |
| Retainer | 29 | 14% | 25 (14%) | 7 (21%) | 4 | 3.24 |
| Aligner / Invisalign | 15 | 7% | 12 (7%) | 4 (12%) | 3 | 4.00 |
| Sleep apnea / snore / other | 7 | 3% | 3 | 2 | 2 | 2.86 |

**The mix has shifted.** About half of new respondents own a **night guard**, and dentures have fallen from 55% of responses to 15% of new ones. This is most likely an effect of ad targeting or creative and should be checked against Meta delivery. Night guard owners are now the largest group writing in, and they remain the least satisfied main segment.

### Reasons to buy (multi-select; all 201)

| Reason | All | % | Oct 28 | Night guard (50) | Retainer (29) | Aligner (15) | Denture (100) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bacteria (incl. sterilization, infection, healthy) | 131 | 65% | 116 | 32 (64%) | 10 (34%) | 11 (73%) | 73 (73%) |
| Yellow stains / brighter | 82 | 41% | 70 | **33 (66%)** | 13 (45%) | 4 (27%) | 29 (29%) |
| Food debris | 47 | 23% | 46 | 3 | 9 | 2 | 32 |
| Smell | 33 | 16% | 28 | 12 (24%) | 5 | 4 (27%) | 12 |

New free-text reasons: "Afraid of the risk for infection", "wanted to keep my new retainers in good condition", "very clean without a lot of work", "Best quality and reviews", "My husband wanted it", "dark stains".

**Yellow-stain night guard buyers are still the weak spot:** 33 buyers averaging **2.82★**, compared with **3.76★** for night guard buyers who came for other reasons. Among the 9 such buyers after 11 Oct, the average is **2.56★**.

### What they used before (all 201, ~keyword)
Tablets/soaks ~95 (overlaps with brushing), toothbrush/toothpaste/cream ~57, soap/Dawn ~10, **another ultrasonic pod ~30-32 (avg 3.0★)**, nothing/water ~16.
**After 11 Oct, 10 of 34 (29%) came from another pod**, compared with about 15% before, and they average **2.5★**. Pods named in the new rows: Zima, NovaT, Dental Pod, Dental Pod Pro, an "off brand Amazon ultrasonic, rechargeable", and "a similar cleaner". Other new methods: "toothbrush and Dawn daily, Efferdent weekly", "Toothbrush and soap as recommended by dentist", "Soap and a special toothbrush from my dentist".

### Frustrations with the old routine (all 201, ~keyword; same order as the deep dive)
Never clean / not sure it worked ~37+ (hand-coded earlier as 56 of 167); time/scrubbing/hassle ~25; yellow/stain/brown ~19; build-up (plaque, tartar, calcium, glue) ~18; bacteria/infection ~10; cloudy/film ~7; smell/taste/breath ~3.
New in the last 34 responses: "alkali/calcium buildup", "Never looked clean. Brownish.", "cloudy aligner and bad breath", "too hands on", "Taste" (from Polident), "Felt like the cleaning wasn't very strong any more" (aging Amazon pod), "the power just got poor" (aging Dental Pod).

### Objections ("What almost stopped you", all 201, ~keyword)
**Price/cost ~77 (38%)**, skepticism (does it work, true, scam, reviews, needed) ~39 (19%), too many brands / hard to choose ~9 (5 of these in the last 34 responses), nothing ~23%.
New wording: "Cost and difficulty choosing brand", "Price and confusion with all brands", "So many competing cleaning machines on the market", "There were many products advertised it was difficult to choose", "Mixed reviews on product", "Was it really needed?", "unsure if it was effective or necessary", "Price and no personal testimony from friends", "Having to plug it in everytime".

### Wins (new, after 11 Oct)
- Night guard: "It's clear looking now!" (husband noticed), "Appliance looks and feels cleaner", "Much cleaner!", "Clearest appearance", "Looks cleaner. Still not clear but looks better.", "Somewhat lighter in color"
- Retainer: "The color is clear again and the odor is gone. There was visible debris at the bottom of the bowl after the cycle completed.", "Retainers appear clearer ... They fit tighter as intended.", "I don't see much left on the retainer", "Stain is getting better"
- Aligner: "Very clear aligner and bad breath is diminished", "Smell" (as the main difference)
- Denture: "No bad taste", "Cleaner", "Looks cleaner", "Everything good" (wife noticed)

### 1-2★ complaints since 11 Oct (13 of 34)
| Theme | n | Words |
|---|---:|---|
| No difference / nothing | 7 | "Nothing!!!", "No difference at all.", "Not much, to be honest.", "nothing yet", "not much yet", "None" |
| No better than my old / cheaper pod | 3 | "does not get any cleaner or look any cleaner than using my cheaper ultrasonic cleaner", "does not clean any better than the device I had that was 1/3 of the cost", "more yellowing and more mineral deposit on my dental device than before" (ex-Dental Pod Pro) |
| Stain not removed (night guard / retainer) | 4 | "Stains did not budge. I even took the step with Dawn DW liquid to no avail.", "They are cleaner but haven't removed the stain", "stain was not cleared", "The 2 retainers stain didn't come all the way clear" |
| Fades after a few days (aligner) | 1 | "It's clean the first few days, then doesn't clean as well" |
| Form factor | 1 (3★) | "It isn't rechargeable and I don't have an outlet in my bathroom." |

### Survey quotes, grouped (all anonymous, all 201 responses)

**Dentures**
- Not clean: "You could still see food on the denture." / "Half the time when I took them out in the morning they still hadn't cleaned them properly." / "Didnt feel clean" / "Dentures weren't free of plaque.. so not CLEAN"
- Hassle: "Time consuming getting old adhesive off" / "Somewhat messy" / "COULDN'T GET INTO THE TIGHT SPOTS"
- Taste and bacteria: "Taste" -> "No bad taste" / "repeated infections" / "Not sanitary" / "Not sure about fully clean e.g. biofilm"
- Wins: "Much cleaner without scrubbing" / "SO CLEAN N ZERO STAINS" / "dentures are cleaner and smell cleaner" / "Don't need to brush as often"

**Night guards**
- Gross / stained: "My old night guard looked gross yellow and cloudy" / "My night guard was cloudy and rough feeling" / "Never looked clean. Brownish." / "It did not stop the guard from discoloring"
- Never clean: "Not being sure if it was working." / "I would always forget to do it and it never felt clean." / "Never got clean until I went to dentist where it went into some similar type of machine" / "Not getting clean enough"
- Fear: "Afraid of the risk for infection" / "Not sure of the control on bacteria"
- Disappointment: "Stains did not budge." / "Unfortunately, nothing my night guard is still dirty" / "still yellow, but hopefully it kills bacteria" / "Some cleaner but still a slight odor"
- Wins: "It's clear looking now!" / "They look much cleaner and smell better" / "Looks cleaner and doesn't smell" / "Night guard has less build up and looks cleaner"

**Retainers**
- Before: "Yellowing and alkali/calcium buildup" / "Retainer was dull and buildup inside crevice" / "Stains won't come out, tablets made the retainer fragile" / "Not sure it was actually clean. I would brush with toothpaste after." / "Not efficient, missed a lot"
- Wins: "My retainer is clear again!" / "Retainer clear not milky" / "Clean, clear and odor free" / "The color is clear again and the odor is gone" / "visible debris at the bottom of the bowl"

**Aligners / Invisalign**
- Before: "cloudy aligner and bad breath" / "White film" / "Trays looked cloudy" / "Always seeing something, like a film, left on my appliance even after brushing" / "could see the building up"
- Wins: "No white film!" / "Very clear aligner and bad breath is diminished" / "No more smell & that they are clean as if I just got them" / "Cleans well without tablets"

**Sleep apnea / other**
- "Wasn't sure if it was killing all of the bacteria." / "too hands on, did not clean thoroughly" / "didn't get a single bit of the crud off" / "Guard feels fresher"

---

## (c) Top 12 pain themes, ranked by frequency across survey and outside sources

Ranking combines how often a theme appears in survey free text with how often it appears in the forum and review sources. "Survey" means the DentalPULSE feedback sheet.

### 1. "Never felt clean" / not sure it's working
The top survey frustration for every appliance.
- Dentures: "Half the time when I took them out in the morning they still hadn't cleaned them properly." (Survey)
- Night guards: "Not being sure if it was working." / "Never was totally clean." (Survey)
- Night guards: "overnight, mouth goo still sticks to it" (The Gadgeteer review)
- Retainers: "Not sure it was actually clean. I would brush with toothpaste after." (Survey)
- Aligners: "they would get cloudy within days and would never feel clean" (Trustpilot, Zima UK 5★)

### 2. Smell, bad taste, bad breath
Rare in survey free text but the loudest theme in forums. People describe it in gross, specific terms.
- Night guards: "Mine has gotten stained and smells terrible." / "My mouthguard ends up smelling like poop everyday." / "the only thing to get rid of the rotten smell" (ThriftyFun, "Smelly Mouth Guard")
- Night guard / splint: "it smells like dog poo, not good when you have to put it in your mouth." (ThriftyFun, "Smelly Tooth Splint?")
- Retainers: "the weird white residue and horrifying smell off my retainers" / "starting to develop a semen smell (I know, disgusting)" / "that nasty unclean taste" (Loox Zima US reviews; Trustpilot Zima UK)
- Aligners: "cloudy aligner and bad breath" (Survey); RealSelf snippet: "the weird smell trays start to have after wearing them for couple of days"
- Dentures: "Taste" (frustration with Polident) -> "No bad taste" (Survey); "dentures are cleaner and smell cleaner" (Survey)
- Night guards: "Some cleaner but still a slight odor" (Survey, 3★)

### 3. Yellow, brown and set-in stains
The main trigger for night guards (66% of night guard buyers) and the main cause of disappointment.
- Night guards: "My old night guard looked gross yellow and cloudy" / "Never looked clean. Brownish." (Survey)
- Night guards: "my son's clear plastic niteguard has become stained yellow" (Hometalk); "No luck, still ugly" after dishwasher, OxiClean and peroxide (ThriftyFun)
- Retainers: "lots of yellow stains and scale on them" / "starting to look stained and unattractive" (Loox Zima US)
- Aligners: "my first Invisalign ... had a yellowish tint" (Loox Zima US)
- Dentures: "My dentures had become somewhat stained after wearing them all day for several years" (Trustpilot Zima UK); "brown stains on my dentures" (Trustpilot Zima UK)
- **Copy rule:** for night guards and retainers, sell keeping them from going yellow, plus bacteria and smell. Survey 1-2★ reviews say "Stains did not budge".

### 4. Bacteria, germs, infection, thrush
The number-one checkbox reason (65%). In free text it shows up as worry rather than something people can see.
- Dentures: "repeated infections" / "Not sanitary" (Survey)
- Night guards: "Afraid of the risk for infection" / "Not sure of the control on bacteria" (Survey, new)
- Night guards: "I have been having problems with bacterial infections in my sinuses." (ThriftyFun)
- Apnea: "Wasn't sure if it was killing all of the bacteria." (Survey)
- Dentures (thrush thread, title only): "painful thrush after getting temporary dentures" (Dental Fear Central, via search)

### 5. Time, scrubbing, hassle, forgetting
- Dentures: "Time consuming getting old adhesive off" / "Having to brush them" (Survey)
- Night guards: "I would always forget to do it" (Survey); "it was tedious to brush it with baking soda" (ThriftyFun)
- Aligners: "I would spend 5+ minutes each night brushing each tray to get them clean and not cloudy." (Loox Zima US)
- Dentures: "if I'm really tired ... it's all I can do to put them in their cup of water" (Straight Dope, "Denture care")
- Apnea / repositioner: "too hands on" (Survey)

### 6. Build-up: plaque, tartar, calcium, scale, glue
- Retainers: "Yellowing and alkali/calcium buildup" / "buildup inside crevice" (Survey)
- Night guard + retainer: "more yellowing and more mineral deposit" (Survey, 2★, ex-pod)
- Night guards: "tartar buildup on it that my dentist has to clean off using the ultrasound machine and scraping" (Straight Dope)
- Dentures: "All the glue was still there." / "Could never get rid of the gooey paste completely." (Survey)
- Night guards: "It is a soft guard with lots of crevices and is very hard to clean." (Trustpilot Zima UK)

### 7. Cloudy, white film, milky, dull
- Aligners: "White film" / "Trays looked cloudy" (Survey); "get cloudy within days" (Trustpilot Zima UK)
- Retainers: "weird white residue" (Loox); "dull retainer" (Survey); win: "Retainer clear not milky" (Survey)
- Dentures (metal clasps): "developed a patchy white 'film' on the metal parts" (Straight Dope)
- Night guards: "cloudy and rough feeling" (Survey)

### 8. Tablets and soaks: taste, cost, re-buying, "did nothing"
- Night guards: "The denture tabs did nothing" (ThriftyFun)
- Retainers: "leaves it brown, but tastes terrible" (Loox Zima US); "tablets made the retainer fragile" (Survey)
- All: "Having to purchase the tablets." / "The need for tablets" (Survey)
- Competitor pod owners: "aggressive marketing of their own cleaning tablets" / "very little difference between their tablets and generic tablets" / "a new subscription order was shipped a few months later without notice" (Trustpilot Zima UK)
- Retainers: "I did not realize that I needed to order the tablets and consequently I ran out" (Loox Zima US)

### 9. "My last pod didn't work" / all pods look the same
More common among new buyers (29% after 11 Oct).
- Night guards: "does not clean any better than the device I had that was 1/3 of the cost" (Survey)
- Night guards: "Not much of a difference in cleaning from the pod purchased from Amazon for $30" (Survey)
- Competitor: "never cleaned my trays as well as the cheaper plug-in ultrasonic unit" / "no better than a cheap one I got from Amazon" / "a definite case of over promising and under delivering" (Trustpilot Zima UK)
- Durability: "stopped working after a month" / "only lasted 13 months" / "there is zero vibration" (Trustpilot Zima UK / .co)
- Aging pods: "the power just got poor" / "Felt like the cleaning wasn't very strong any more." (Survey)

### 10. Home remedies that risk the appliance (bleach, boiling, peroxide, vinegar, Listerine)
- Night guards: "I tried it all including bleach!!!" / "I can't get the bleach taste to go away." / "boiling ... could ruin it" / "I've tried the peroxide but it just doesn't seem to do the job." (ThriftyFun)
- Night guards: "I haven't tried bleach or Borax as I don't want to harm this $250 dental device." (Hometalk)
- Night guards: "I even took the step with Dawn DW liquid to no avail." (Survey)
- Retainers: "For years I've had my retainer degrade, weaken, and crack on me." (Loox Zima US)

### 11. Cost of the appliance and replacing it
- Night guards: "It was $700." / "~$200 total" / "I wear through them every few months and replace them." (SIGforum bruxism thread)
- Night guards: "don't want to harm this $250 dental device" (Hometalk)
- Ties into the price objection (38% of survey buyers): "Cost. I am on a fixed budget." (Survey)

### 12. Embarrassment and other people noticing
Weak in the survey (77% say "no one noticed"). It shows up in forums as worry.
- Dentures: "I feel rather embarrassed as I am only 26" / "Just hope to get used to them soon and nobody notices" (Mumsnet, partial dentures thread)
- Dentures (kissing): "How can I kiss and be intimate?" (Mumsnet, via search snippet)
- Breath: "I'm so embarrassed" / "Caused horrid breath in an ex." (Mumsnet, "stinky breath")
- Night guards: "My mouth smell all time" and it affects being around people (ThriftyFun)
- Retainers: "if you dont want to have a gnarly mouth guard" (Trustpilot Zima UK)
- When someone does notice, it is the spouse: "It's clear looking now!" (husband), "Everything good" (wife) (Survey)

---

## (d) Glossary: words customers actually use

**Gross / state:** gross, nasty, gnarly, yucky, ugly ("still ugly"), crud, gunk ("clean out the gunk"), goo ("mouth goo"), slimy, slick, gooey (paste), crusty (not seen verbatim, but implied by "scale"), cloudy, milky, dull, rough feeling, film / white film, white residue, white stuff, patchy white film, build-up / buildup, scale, tartar, plaque, calcium buildup, mineral deposit, debris, residue, "stuck in tight spots", crevice / crevices.
**Color:** yellow, yellowish tint, yellowness, gross yellow, brownish, brown stains, dark stains, discolored, blood stained, lost its whiteness, lighter in color, clear again, crystal clear, "clear looking now".
**Smell / taste:** stinks, stinky, smells terrible, rotten smell, smells like poop, smells like dog poo, horrifying smell, weird smell, odor, odor free, bad taste, nasty unclean taste, tastes terrible, bleach taste, bad breath, morning breath, fresher, "doesn't smell like anything".
**Doubt / feeling:** never felt clean, not sure it was working, not sure it was actually clean, didn't help, ineffective, did nothing, didn't budge, no difference at all, nothing, still dirty, not convinced, too good to be true, scam, fake reviews, over promising and under delivering, ripped off, "was it really needed?".
**Effort:** time consuming, tedious, scrubbing, brushing every night, too hands on, messy, always forget, buying tablets, ran out of tablets, subscription.
**Fear:** bacteria, germs (rare), not sanitary, infection(s), thrush, biofilm, "risk for infection", "control on bacteria".
**Products named:** Polident ("Poly tabs", "Polydent"), Efferdent, Steradent, Retainer Brite, "Invisalign cleaner", Dawn, Dove soap, soft soap, Listerine, OxiClean, hydrogen peroxide, vinegar, baking soda, bleach, Borax, Zima, Dental Pod / Dental Pod Pro, NovaT / Nova Dent, "Amazon pod", "cheaper ultrasonic".

---

## (e) Objections and skepticism about ultrasonic cleaners, in their words

**Does it actually work / is it needed**
- "Was it really needed?" / "unsure if it was effective or necessary" (Survey, new)
- "efficacy of the product, does it do what it claims" / "Wasn't convinced on what it was supposed to do" (Survey)
- "Didn't know if everything about it was true" / "Seemed too good to be true" (Survey)
- "I have to admit to being a bit sceptical." (Trustpilot Zima UK, denture wearer)
- "Was it perfect? Absolutely not." (The Gadgeteer review)
- "I don't see any vibrations in the water, just makes the noise" (Survey); "there is zero vibration" (Trustpilot Zima .co)

**They're all the same / my last one didn't work**
- "So many competing cleaning machines on the market" / "confusion with all brands" / "difficulty choosing brand" (Survey, new)
- "Every brand is same. Not see difference." (Survey)
- "no better than a cheap one I got from Amazon" (Trustpilot Zima UK)
- "Three previous buys and none worked." (Survey)

**Trust in reviews and ads**
- "Mixed reviews on product" / "no personal testimony from friends" (Survey, new)
- "I'm always scared products with such big sales are fakes or phony." / "The fake reviews." (Survey)
- "feel perhaps the others aren't genuine" / "which I think might be untrue or fake" (Trustpilot Zima UK)

**Price and hidden costs**
- "Cost. I am on a fixed budget." / "Expense" (Survey)
- "aggressive marketing of their own cleaning tablets" / "tablets are consumable" / "sneakily sign you up for a subscription" (Trustpilot Zima UK)
- "Expensive cleaning for one week!" (Trustpilot Zima .co)

**Durability**
- "stopped working after a month" / "only lasted 13 months" / "both units I owned broke within seven months" / "I'm sure it will break in six more months when the warranty is up." (Trustpilot Zima UK)

**Form factor (new)**
- "Having to plug it in everytime" / "It isn't rechargeable and I don't have an outlet in my bathroom." (Survey)

**Stains (the objection that becomes a refund)**
- "Stains did not budge." / "They are cleaner but haven't removed the stain" (Survey)
- "removed next to nothing" (Trustpilot Zima UK, "doesn't clean stains")
- "my night guard showed no change" (Trustpilot Zima UK, via search summary)

**How to answer each objection, using only approved claims:** For "does it work", use 99.9% of bacteria in one 5-minute cycle, together with a demo of moving water and debris in the bowl. For "all the same", use the result that 6 of 7 pods left live bacteria in a 90-day lab test. For tablets and subscriptions, use "tap water only". For price and fake-review doubts, use the 120-day money-back guarantee. For "just noise", use 42,000 Hz.

---

## (f) 30 ad headline candidates (customer language, approved claims only)

Approved claims: 99.9% of bacteria in one 5-minute cycle · 42,000 Hz · tap water only · 6 of 7 pods left live bacteria in a 90-day lab test · 120-day money-back guarantee. No headline promises that set-in yellow on a night guard or retainer goes away.

**Night guards**
1. "Smells like poop every morning?" Your night guard is telling you something.
2. Your night guard sits in your mouth for 8 hours. When did you last *really* clean it?
3. Gross, yellow and cloudy didn't happen overnight. Neither should the bacteria.
4. Brushed it. Soaked it. Tried peroxide. Still never felt clean?
5. Don't bleach a guard you paid hundreds for. Tap water. 5 minutes.
6. Afraid of what's growing on your night guard? 99.9% of bacteria, gone in one 5-minute cycle.
7. "It only got clean at the dentist." Now it gets a 5-minute clean every morning.
8. Keep your new night guard from going gross. Tap water only.

**Retainers and aligners**
9. That weird white residue on your retainer isn't "normal."
10. Cloudy trays. Bad breath. Sound familiar?
11. "Clear again. And the odor is gone." 5 minutes, tap water.
12. Stop spending 5 minutes a night scrubbing each tray.
13. Retainer tastes nasty when it goes back in? That's bacteria, and one 5-minute cycle takes out 99.9% of it.
14. No tablets to run out of. Just tap water and 42,000 Hz.

**Dentures**
15. Half the time they still aren't clean in the morning.
16. Polident every night, and they still don't feel clean?
17. Still tasting the tablets? Tap water only.
18. Stop scrubbing old adhesive off with a toothbrush.
19. Food stuck in the spots a brush can't reach.
20. You can't see bacteria. That's exactly the problem.
21. "Repeated infections"? Start with what's on your dentures. 99.9% of bacteria, one 5-minute cycle.

**Ultrasonic skeptics and pod switchers**
22. "Does it actually work?" 6 of 7 pods left live bacteria in a 90-day lab test.
23. Your last pod "just makes noise"? 42,000 Hz you can see in the water.
24. "No better than the cheap one from Amazon"? 6 of 7 pods left live bacteria.
25. "So many pods, so much confusion." In a 90-day lab test, 6 of 7 left live bacteria behind.
26. Too good to be true? You've got 120 days to find out.
27. Skeptical? Good. 120 days to prove it, or your money back.
28. Fixed budget? No tablets to keep buying. Tap water only.

**Universal**
29. Not sure it's actually clean? Now you'll know: 99.9% of bacteria, 5 minutes.
30. No scrubbing. No tablets. No guessing. Drop it in for 5 minutes.

---

## (g) What is new compared with `feedback_deep_dive.md`

1. **Mix shift to night guards.** About 47% of responses after 11 Oct (52% since 28 Oct) are from night guard owners, compared with 20-23% before. Only 15% of new respondents own dentures. Night guard creative is now the main source of reviews, so the night guard yellow-stain disappointment matters more. New night guard yellow buyers average 2.56★.
2. **More buyers are switching from another pod, and they are the least happy.** 29% of buyers after 11 Oct came from another pod (Zima, NovaT, Dental Pod, Dental Pod Pro, Amazon rechargeable) and average 2.5★. Their complaints are new and specific: "1/3 of the cost", "cheaper ultrasonic", "more mineral deposit than before". Their reasons for switching were that the old pod got weaker ("power just got poor", "cleaning wasn't very strong any more") or a button broke.
3. **New objection: too many brands to choose from.** "Confusion with all brands", "difficulty choosing brand", "so many competing machines", "mixed reviews". The answer is the 6-of-7 lab test, used as a way to choose between brands.
4. **New objection: is it even necessary?** "Was it really needed?" and "unsure if it was effective or necessary". Bacteria and infection framing ("Afraid of the risk for infection") answers this better than appearance does.
5. **Cordless / no-outlet friction.** "Having to plug it in everytime" and "I don't have an outlet in my bathroom". This is the first time it has come up. Do not show the pod in a bathroom with no outlet, and expect "rechargeable" comparisons from competitors.
6. **Mineral-deposit language.** "alkali/calcium buildup" and "mineral deposit" (retainers and night guards) join tartar and plaque.
7. **Bad breath shows up as a separate aligner pain** ("cloudy aligner and bad breath" became "bad breath is diminished"). This is new survey evidence for a breath angle on clear appliances.
8. **The dentist's machine as a reference point.** "Never got clean until I went to dentist where it went into some similar type of machine." Forums say the same ("my dentist has to clean off using the ultrasound machine"). This is a credible framing, but it must not claim to be the same as the dentist's machine.
9. **Taste is a frustration with Polident** ("Taste" became "No bad taste"), and forums back it up ("tastes terrible", "bleach taste").
10. **Outside sources add gross smell language the survey lacks.** The survey almost never describes smell vividly, but forums do: "smells like poop", "dog poo", "rotten smell", "horrifying smell", "semen smell", "nasty unclean taste", "mouth goo", "gnarly". Use these for scroll-stopping hooks. Buyers do not volunteer this language in surveys.
11. **Competitor weak points in customers' own words:** tablet upsells, surprise subscriptions, units dying in 1-13 months, and "zero vibration". Without naming a competitor, "tap water only" and the 120-day guarantee answer these directly.
12. **Fading results:** "It's clean the first few days, then doesn't clean as well" (aligner). This is a single report, so watch for more before acting on it.
13. **Reddit could not be reached** by direct fetch or search. If Reddit language is needed, someone with normal browser access would have to pull it, for example top posts of the year in r/Dentures, r/bruxism, r/Invisalign and r/orthodontics.
