# DentalPULSE: customer feedback angles (long-form story mining)

Source: Google Sheet "DentalPULSE Feedback (Responses)", tab "Form Responses 1" (file `1xepNvWovrheKwSm76mchUfZbJ_GfF2f6uIwk5HLOKKU`, gid 1964641186). Read in full via a CSV export (read-only). Mined 2026-11-11.

## 1. Dataset

- **Rows:** 198 responses, all decoded with no gaps.
- **Date range:** 4 May 2026 to 11 Nov 2026. By month: May 43, Jun 17, Jul 21, Aug 38, Sep 34, Oct 32, Nov (to the 11th) 13.
- **Columns (11):** Timestamp | Satisfaction (1-5) | Appliance owned | Previous cleaning method | Biggest frustration with old routine | Why did you buy (multi-select: Bacteria / Yellow Stains / Food Debris / Smell, plus free text) | What almost stopped you | Biggest difference since switching | Who noticed | Age (added around July, so 61 rows are blank) | "Who are you buying this for?" (**blank in all 198 rows**, so the buyer-vs-recipient question cannot be answered from this data)
- **Gender:** not collected. Indirect signals: 9 mention "my husband" and 7 "my wife".

**Satisfaction:** 5★ 81 · 4★ 35 · 3★ 25 · 2★ 19 · 1★ 38. Average 3.52. 59% rate 4-5 and 29% rate 1-2. This survey is far more negative than a typical review page, which makes it useful for finding objections.

## 2. Counts

### Appliance type (n=198)
| Appliance | n | Avg sat | 1-2★ |
|---|---|---|---|
| Denture (full) | 97 | 3.72 | 24 |
| Night guard | 48 | 3.12 | 17 |
| Retainer | 28 | 3.29 | 9 |
| Aligner / Invisalign | 15 | 4.00 | 3 |
| Sleep apnea / snore / tongue-stabilizing device | 6 | 2.83 | 3 |
| Partial | 3 | 4.67 | 0 |
| Night guard + retainer | 1 | 2.0 | 1 |

### Age (asked from about July; 137 answered)
60+ **113 (82%)** · 50-60 17 · 40-50 2 · 30-40 1 · 20-30 4 · blank 61. Even retainer, night-guard and aligner owners are mostly 60+.

### Previous cleaning method (multi-tag; keyword-coded)
| Method | n | Avg sat of this group |
|---|---|---|
| Tablets / soaks of any kind | **82** | 3.65 |
|   named Polident/Polydent ("poledent", "police") | 20 | |
|   named Efferdent | 3 | |
|   named Steradent (tabs and paste) | 2 | |
|   "Retainer white tablets", "Smile retainer cleaner", powder, pellet | 4 | |
| Brushing / toothpaste / denture cream | 55 | 3.87 |
| **Another ultrasonic pod / device** | **44** | **2.91 (lowest)** |
|   named Amazon cleaner | 7 | |
|   named Zima | 6 | |
|   "Dental Pod (Pro)" | 4 | |
|   Haneuul, NovaDent, NovaT, "cheaper version", "three previous buys" | many | |
| Water / rinse only | 15 | |
| Soap (Dove, Softsoap, dish soap; 2 on dentist advice) | 9 | |
| Nothing yet / brand-new appliance | ~18 | |
| Vinegar | 1 | |
| Hydrogen peroxide (night guard) | 1 | |
| Alcohol / mouthwash | 2 | |

### Why they bought (multi-select)
Bacteria **125 (63%)** · Yellow stains **74 (37%)** · Food debris 47 · Smell 33 · plaque/tartar/build-up 6 · "sterilization/sanitizing" 4 · adhesive / Fixodent slime 1 (plus 4 more adhesive mentions elsewhere).
- Buyers who ticked **only "Bacteria"** (45) average **4.16★**.
- Buyers who ticked **Yellow stains** (74) average **3.22★**.
- **Night guard owners who ticked yellow stains** (32) average **2.75★**.

### What almost stopped them
Price/cost **79 (40%)**, including 3 on a fixed income and 2 confused about Canadian vs US currency · Skepticism that it works, "too good to be true", or distrust of ads/fake reviews **~45** · Earlier pods failed them ~10 · Too many choices ~8 · Nothing 26+ · Company origin unknown 2 · Fit worry (apnea device) 1.

### Who noticed
No one / nobody / none / N/A: ~140 (71%). Spouse/partner: **~22** (husband 9, wife 7, partner 2, spouse 2, whanau 2). Family 1, **grandchildren 1**, daughter 1, social friends 1, "everyone" 1, **dentist 2**. Lives alone 2.

### Life moments
- New appliance just fitted (first denture, new night guard, new retainer, starting Invisalign/aligners): **10**. Of these, Invisalign/aligner starts: 3.
- Dentist recommended an ultrasonic, soap, or a special brush: 4. Dentist cleans it at visits: 2.
- A partner wanted it for their own night guard, or the household shares the device (husband, daughter, spouse): 5.
- Travel / "on the go": 1. Gift: 1. Hospital / nursing home / caregiver: **0**.

### Result reported ("biggest difference")
- No or little difference, too soon, defective, or never arrived: **~73 (37%)**.
- Clearly positive (cleaner, whiter, clear again, no smell, no slime, fits better): ~110.

## 3. Verbatim quotes by theme (spelling as written)

### Disgust / "gross" moments
1. "My old night guard looked gross yellow and cloudy" (Night guard, 5★)
2. "You could still see food on the denture" (Denture, 5★)
3. "Half the time when I took them out in the morning they still hadn't cleaned them properly" (Denture, 5★)
4. "Always seeing something, like a film, left on my appareille even after brushing" (Invisalign, 20-30, 5★)
5. "Could never get rid of the gooey paste completely" / reason: "Fixodent slime" (Denture, 60+, 1★)
6. "Time consuming getting old adhesive off" (Denture, 5★)
7. "My night guard was cloudy and rough feeling" (Night guard, 5★)
8. "Retainer was dull and buildup inside crevice" (Retainer, 60+)
9. "Crud in the interior corners that's pretty impossible to reach manually" (Tongue-stabilizing device, 60+, 1★)
10. "Wasn't getting them clean enough and could se the building up." (Aligner, 60+, 5★)
11. "Dentures felt slick" → "Dentures were not slick" (Denture, 60+, 5★)
12. "Denture isn't slimy" (Denture, 60+, 5★)
13. "There was visible debris at the bottom of the bowl after the cycle completed." (Retainer, 60+, 5★). This is the "see what came off" proof moment.

### Smell / taste / breath
14. "cloudy aligner and bad breath" → "Very clear aligner and bad breath is diminished" (Aligner, 60+, 5★)
15. "No more smell, cleans very well." Noticed by: "My family, especially my grandchildren." (Denture, 60+, 5★)
16. "The color is clear a g ain't and the odor is gone." (Retainer, 60+, 5★)
17. "No more smell & that they are clean as if I just got them" (Invisalign, 20-30, 5★)
18. "Clean, clear and odor free" (Retainer, 50-60, 4★)
19. "They look much cleaner and smell better" (Night guard, 60+, 5★)
20. Old routine frustration: "Bad taste" (Polident on a night guard, 1★). Another: "Taste" → "No bad taste" (Polident to Pulse, Denture, 4★)

### Partner / family / dentist noticing
21. "The denture lost its whiteness and was turning yellow. Now it is as white as it was when I first got it!" Noticed by: "My husband noticed they were white again." (Denture, 60+, 5★)
22. "Cleaner denture and for some reason fitting better" (noticed by: Spouse, 4★)
23. "Daughter got one too for retainer. Noticed cleaned better" (Night guard, 50-60)
24. "Spouse has mouth guard and it is cleaner too" (Aligner, 5★)
25. Noticed by: "Dentist" (Denture, 60+, 5★)
26. "My Denturs are cleaner, they feel fresh." Noticed by: "My social friends." (Steradent switcher, 5★)
27. "No one so far. It just feels cleaner in my mouth." (Retainer, bought because "My husband wanted it for his night guard appliance", 5★)

### Health worries (thin; see Section 4)
28. Frustration: "repeated infections" (Denture, 1★, but the unit was defective)
29. Why bought: "Afraid of the risk for infection" (Night guard, NovaT switcher, 60+, 4★)
30. "Not sure aboutfully clean eg biofilm" (Polident user, 5★). Noticed by: "My wife"
31. "Wasn't sure if it was killing all of the bacteria." (Sleep apnea guard, 50-60, 4★)
32. "I wa worried about bacteria" (Vinegar user, 1★)
33. "you saying that bacteria gets into the cervices that a brush leaves" (an ad line repeated back as their frustration, 1★)
34. "Nothing really, I just figured it would be a healthier option." (Sensodyne user, 3★)
35. "Can't remove blood stained retainer from a bad tooth" (Retainer, 2★)

### Chemicals / tablets
36. "Stains won't come out, tablets made the retainer fragile" (Retainer, 3★)
37. "Myself fill fresh without chemicals" (Retainer, tablet switcher, 5★)
38. "having to purchase the tablets." → "that no need for other procedures to keep dentures clean." (Polident, 5★)
39. "Buying dental tablets." → "So much easier" (Retainer, 5★)
40. "The need for tablets" → "Cleans well without tablets" (Aligner, switched from "Another dental pod that needed tablets", 5★)
41. "Wasn't frustrated because I didn't know anything else, until I found Dentalpulse pod." → "My dentures now are impeccable, no bacteria 100% Recommended" (Polident, 5★)
42. "To many items that I had to use." (Steradent tabs and paste, 5★)

### Failures of other pods / devices
43. "Three previous buys and none worked" → "It worked better than the rest but it still takes time to get all the glue out" (3★)
44. "Dentures weren't free of plaque.. so not CLEAN" (cheaper pod) and "Deep clean and took all the plaque off." (another cheaper-pod switcher, 5★)
45. "I lost a lot of confidence in the one I bought from a different company" → "Cleaned a lot better" (Amazon switcher, lives alone, 5★)
46. "The cleaners didn't last long" (several ultrasonic cleaners, 5★)
47. "The power just got poor, so I tried this one..." (Dental Pod switcher, 2★)
48. "Felt like the cleaning wasn't very strong any more." (Amazon rechargeable, 3★)
49. "No UV Light" (Zima, 2★). "Second pulse button stopped working" (Zima, 5★). "stopped turning on" (Zima, 5★)
50. **Counter-evidence:** "Not much of a difference in cleaning from the pod purchased from Amazon for $30." / "This machine does not clean any better than the device I had that was 1/3 of the cost." / "Every brand is same."

### Appliance cost / protecting the investment
51. "wanted to keep my new retainers in good condition" → "They fit tighter as intended." (Retainer, 4★)
52. "Just got the denture" / "First time, new denture" / "Nothing brand new guard" / "Aligners are new"
53. "I don't know yet just started I have a new night guard" (5★)

> No respondent states what an appliance costs or describes replacing one. The cost-of-replacement angle has to come from category research, not this sheet.

## 4. Evidence check on the owner's three ideas

| Owner idea | Hits in 198 rows | Verdict |
|---|---|---|
| **Tablets / chemicals controversy** | ~7 direct ("tablets made the retainer fragile", "without chemicals", "having to purchase the tablets", "need for tablets", "bad taste" with Polident, "taste", "healthier option"), plus 82 former tablet users (41% of buyers) | **Supported as a switching story, weak as a fear story.** Tablet users are the largest group and are reasonably happy (3.65★). Their stated pain is "didn't really clean / had to brush anyway / buying tablets / too many items", not toxicity. Use the chemical-free angle as the payoff ("just tap water"). Allergy and toxicity would be outside evidence; no customer reports a reaction. |
| **Cavities / root canals from dirty aligners, retainers, night guards** | **0** mentions of cavity, decay, root canal or gum disease. Nearest: "bad tooth" with a blood-stained retainer (1), "bad breath" (1), "biofilm" (1), "plaque/tartar/build-up" (~12) | **No customer evidence.** Plaque and build-up on the appliance is real customer language. Any link to cavities has to come from dental sources and must not be presented as a customer outcome. |
| **Respiratory / throat issues from dirty night guards or dentures** | **0** mentions of throat, cough, pneumonia, thrush, sore or sick. Nearest: "repeated infections" (1, unspecified), "afraid of the risk for infection" (1), 6 sleep-apnea/snore-device owners (they breathe through the device all night) | **No direct evidence.** The concern exists only as generic "infection" fear. If used, frame it as a worry the narrator read about, not a diagnosis, and source it externally. |

Other health terms searched with zero hits: thrush, gum irritation, sore throat, allergy, rash, sick, pneumonia, fungus/yeast.

## 5. Ten unused angle ideas (frequency → story seed)

1. **"The bacteria I couldn't see"** (Bacteria 125/198; bacteria-only buyers average 4.16★, the happiest group). *Seed:* A 68-year-old who soaked in Polident for 11 years reads the word "biofilm", realises a fizzing tablet can't reach the cracks, and for the first time stops wondering whether her teeth are really clean.
2. **"Three cleaners in the drawer"** (44 came from another pod; ~10 say earlier ones failed or died). *Seed:* A man lines up the three cheaper pods that died or "just bubbled", and explains why he paid more for the fourth. Write it honestly: "it worked better than the rest." Never claim "no other pod works" (see Section 6).
3. **"White again — my husband noticed first"** (husband/wife/partner noticed 22; "white again" and "lighter in color" ~6). *Seed:* Her husband looks across the breakfast table and says "your teeth look like when you first got them", and she realises how yellow they had become.
4. **"The grandkids stopped pulling a face"** (smell 33 buyers, 36 smell/taste/breath mentions; grandchildren 1). *Seed:* A grandmother notices her grandson leans away when she kisses him goodnight, finds the smell is coming from her plate, not her mouth, and then gets "no more smell".
5. **"Fixodent slime"** (adhesive/glue/paste residue 5). *Seed:* Ten minutes every night scraping gummy adhesive off with a fingernail, then the morning the cycle lifts it off.
6. **"Brand-new appliance, old mistakes"** (10 new appliances; "keep my new retainers in good condition"). *Seed:* Fresh from the orthodontist with a $500+ retainer, she remembers her first one turning cloudy and milky within a year, and decides this one won't.
7. **"My dentist cleans it in a machine twice a year — why not every day?"** (dentist mentioned 6; "never got clean until I went to dentist where it went into some similar type of machine"). *Seed:* The hygienist hands back her night guard sparkling after an ultrasonic bath, and she wonders why she settles for that once every six months.
8. **"The night guard I was ashamed to put in"** (48 night guards; "gross yellow and cloudy", "rough feeling"). *Seed:* She hides the case when her husband walks in, and the story is about the feel and the smell, not whitening. Night-guard stain results are the weakest in the data, so promise cleanliness and freshness, not "like new".
9. **"Tablet fatigue"** (82 tablet users; "too many items", "having to purchase the tablets", "had to still brush my dentures"). *Seed:* A cupboard of half-used boxes, a monthly tablet bill, and still brushing afterwards. Switching to tap water means nothing to restock. The chemical worry is a secondary note ("made the retainer fragile").
10. **"The couple who share one pod"** (5 households: husband wanted it for his night guard, daughter got one for her retainer, spouse's mouth guard). *Seed:* She bought it for her dentures; within a week her husband's night guard was in there too. Light open-loop humour, and it pushes a second purchase.

Bonus seeds with thin evidence (1-2 mentions each): "fit better / the hold" after cleaning (3: "for some reason fitting better", "The hold", "fit tighter as intended"); "film I could see even after brushing" for young Invisalign users (2, both 20-30).

## 6. Objections and complaints → "don't promise" rules

| Complaint | Count | Rule |
|---|---|---|
| No or little visible difference | ~73 (37%) | Don't promise dramatic overnight transformations. Frame results as gradual ("lighter each week") and the bacteria and freshness benefit as the core. |
| **Old yellow stains / discoloration don't budge**, especially on night guards (NG + yellow buyers average 2.75★). "Stains did not budge", "still yellow", "more yellowing and more mineral deposit", "blood stains" | ~15 | **Don't promise to remove set-in yellowing, tartar, coffee or blood stains, or to make an appliance "look brand new".** Promise it keeps a clean appliance clean and lifts fresh film and debris. "Lighter over time" has some support (~6). |
| Plaque / tartar / glue removal slow | 5 ("working but very slow", "still takes time to get all the glue out") | Don't say "one cycle removes all plaque/adhesive". |
| **Not better than a cheaper pod** | ~8 ("$30 Amazon pod", "1/3 of the cost", "every brand is same", "makes the same claims") | **Don't claim "X times more powerful than other pods" or "the only one that works".** Former-pod users are the least satisfied group (2.91★). Lead with design and reliability ("didn't last long", "power got poor"), not raw power. |
| **Noise** ("loud screeching", "too loud", "very loud", "louder than other one") | 6 | Don't call it silent or quiet. Say "you'll hear it working" if anything. |
| "No vibrations in the water, just makes noise" | 2 | Don't promise visible bubbling or swirling. Show debris in the water after the cycle instead. |
| Doesn't heat | 1 ("water is still cold") | Never imply heated cleaning. |
| **Size / fit**: upper denture doesn't fit; apnea device doesn't fit; "awful small"; but also "almost 2x the size of the other pod" | 4 | Don't promise "fits every appliance". State the interior dimensions. Large upper dentures and apnea devices are at risk. |
| Corded / not rechargeable / needs outlet | 2 ("having to plug it in everytime", "no outlet in my bathroom") | Don't imply cordless or battery travel use unless true. |
| Defective / dead on arrival / "blinks 3 times" / never received | ~6 | Ad should not lean on "lasts forever". |
| Returns and refunds hard, no response | ~6 (including a $79.95 "cleaning bundle" upsell refund) | Don't promise "easy returns" unless operations support it. |
| **Upsell / tablets in checkout contradict "tap water only"** | 3 ("a mention of tablets in the buying portion when advertised as not needed", "promotion tried to get me to buy... additional products") | Keep the "no tablets needed" claim consistent with the checkout. Flag this to the owner. |
| Currency confusion (CAD vs USD) | 2 | Show the currency clearly. |
| Distrust of ads / "too good to be true" / fake reviews / company origin | ~15 | Avoid overclaiming. Narrators should be specific and modest. Origin story may help. |
| Before/after images not matching reality ("does not come out as clean as the nightguards in the advertisements") | 2 | Use realistic before/after images on denture plaque and film, not stain-whitening. |
| No removable tray | 1 | Don't show or imply a basket. |
| Health outcomes | 0 customer evidence | Don't claim to prevent infections, cavities, thrush or respiratory illness. Any health framing must be the narrator's own worry, with external sources. |

## 7. Notes for the long-form writer

- **Core persona:** 60+ denture wearer (49% of rows; 82% of known ages are 60+), switching from Polident tablets plus a brush, buying for "bacteria" and invisible cleanliness. Usually alone with the result ("no one noticed" 71%), so a partner noticing is a rare, valuable story beat; use it as a payoff, not a promise.
- **Second persona:** 60+ night guard owner (24%): the least satisfied segment. Write for freshness and hygiene, not stain removal.
- **Real customer phrases to borrow:** "impeccable", "white again", "as white as when I first got it", "no more smell", "isn't slimy", "clear not milky", "clean as if I just got them", "without scrubbing", "fill fresh without chemicals", "gross yellow and cloudy", "film left even after brushing", "crevices a brush leaves".
- The empty "Who are you buying this for?" column suggests a form bug. Worth telling the owner.
