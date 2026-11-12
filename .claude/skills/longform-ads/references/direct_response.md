# Direct-response playbook

This is how we decide **what** to say before writing **how** to say it. The frameworks come from the direct-response canon: Hopkins, Caples, Schwartz, Ogilvy, Sugarman, Halbert, Kennedy, Masterson/Forde, Georgi, Brown, Hormozi. They're rewritten here as decisions and checks for our brands. The account's own results always win over any framework: tag every concept with these decisions (§9) so the data can overrule them.

---

## 1. Start from the market: awareness and sophistication

**Awareness** (Schwartz) decides where the ad has to start. Pick it per audience, not per brand.

| Level | The reader… | So the ad opens with… | Our example |
|---|---|---|---|
| Unaware | doesn't connect their life to the problem | a story or moment they recognize ("I sat on a bench at Disney and watched…") | most cold scroll-video and long-form traffic |
| Problem-aware | feels the pain and doesn't know a fix exists | the pain, named precisely, then the reason it happens | "my heels throb the second I sit down" |
| Solution-aware | knows "good shoes" or "cleaning tablets" exist | why the usual solutions fail (the enemy), then the new mechanism | "$165 running shoes are built for a flat road" |
| Product-aware | knows us but hasn't bought | proof, the offer, risk reversal | retargeting, reviews, the guarantee |
| Most aware | wants it and is waiting for a reason | the deal and its deadline | "60% off until December 5th" |

**Sophistication** decides how big a claim can be, and how it has to be framed:
1. **First to market:** say the claim plainly ("comfortable all day").
2. **Competitors repeat it:** enlarge it ("12 hours on concrete without heel pain").
3. **Claims are tired:** introduce a **mechanism** that explains why this one works ("arch support built in, so there's nothing to pack flat").
4. **Mechanisms are copied:** make the mechanism bigger or more specific ("running shoes roll you forward; you stand still").
5. **Readers are numb:** sell **identification**: a person, an experience, a world ("the woman who stayed on the boat"). Story-led long-form wins here.

Comfort footwear and denture care are both at stage 4–5. That's why story, enemy and mechanism beat plain feature claims for us. Re-check this every Monday against what competitors are running.

## 2. Find the one belief

Before writing, write one sentence: **"This [new opportunity] is the key to [desire], and it's only attainable through [our mechanism]."** Everything in the ad either builds that belief or removes an objection to it. If a paragraph does neither, cut it.

- Comfort Wear: *"The reason your feet quit isn't your age or your weight. It's foam built for running. A shoe with built-in arch support and a stretch upper is the only way to stand all day without paying for it at night."*
- DentalPULSE: *"Brushing and soaking leave a living film on dentures that you can't see. Medical-grade UV-C cleaning is the only way to know it's actually gone."*

## 3. The mechanism: why it fails, then why this works

A strong ad sells two mechanisms:
- **The problem mechanism:** the real, specific reason earlier fixes failed. It moves blame away from the reader ("it's not you, it's the design") and makes the old solution the enemy.
- **The solution mechanism:** the specific feature that defeats that cause, named in plain words, with a picture the reader can see ("the knit gives when your feet swell at hour nine").

**Rules:**
- Each failure in the story must map to a feature that fixes it (the fidelity table).
- The mechanism must be **simple enough to repeat to a friend**. If it takes a diagram, it's too complex.
- The mechanism is delivered by a **messenger** with earned authority (a 30-year mail carrier, a retired flight attendant, a patient), never a fake doctor.

## 4. Choose the lead (the first 10–15% of the copy)

There are six proven lead types (Masterson/Forde). Choose on purpose, and rotate across a batch.

| Lead | Best for | Hook shape |
|---|---|---|
| **Story** | unaware, stage 5 markets (our default) | a specific scene mid-moment, with a contradiction |
| **Secret / revelation** | solution-aware, tired claims | "What a 30-year flight attendant told me about…" |
| **Problem–solution** | problem-aware | the precise symptom, then "it isn't what you think" |
| **Promise** | early sophistication, strong proof | a concrete, specific result |
| **Big proclamation** | jaded markets that need a jolt | a bold, provable, counterintuitive statement |
| **Offer / invitation** | most aware, sale periods | the deal first, then the reason it exists |

**Hooks must have:**
- **specificity:** numbers, names, prices, places ("$4,800 to watch Germany slide past a window")
- **a contradiction or tension**
- **an open loop** that's only closed late in the copy

Write 3 alternate hooks, each with a **different lead type**, so tests teach us something.

## 5. Proof: stack it, and make it believable

Ranked roughly by persuasive power for our audiences:
1. **Demonstrated outcome in a story:** a specific before and after scene ("I walked past my old bench").
2. **Social proof with detail:** a named type of person and situation, counts we can confirm (500,000+), review language.
3. **Mechanism proof:** it makes logical sense why it works.
4. **Comparison:** priced enemies and the price inversion ($60 beats $165).
5. **Risk reversal:** the guarantee, stated so it feels generous ("wear them for 30 days…").

**Believability rules (Hopkins, Caples):**
- Specifics beat superlatives. "Twenty-one thousand steps" beats "all day".
- An honest flaw raises trust ("the first week they felt firmer, less squish").
- One clear claim beats five vague ones.

## 6. Objections: answer them inside the story

List the top objections before writing, from the feedback sheet, reviews and Reddit, and assign each one to a story beat:
- **"It's too cheap to be good":** the price inversion and the messenger's own use.
- **"I've tried everything":** the failed-fixes montage, with priced enemies.
- **"It's my age, weight or condition":** the reframe ("it was never my age").
- **"Will it fit or work for me?":** a narrator like the reader, plus the guarantee.
- **"Not now":** the dated offer, plus a payoff scene that makes waiting feel costly.

## 7. The offer: value equation and close

Perceived value goes up with **dream outcome × likelihood of success**, and down with **time to result × effort or sacrifice** (Hormozi). The close should do all four:
- **Dream outcome:** restate the payoff image.
- **Likelihood:** proof and the number of switchers.
- **Time:** "the first week…"; results show up at "hour eight".
- **Effort:** nothing to break in, no inserts.

**Close order:**
1. Restate the enemy.
2. Name the product.
3. The offer, with its real deadline.
4. The guarantee.
5. Social proof.
6. One clear CTA.

Urgency must be true: use only the dated offers in brand.json.

## 8. Craft rules for the line level

- Reading grade 4–6. Short paragraphs. One idea per paragraph.
- Concrete nouns and sensory detail. The reader should *see* each scene.
- Every paragraph earns the next: end beats on a question, a turn or a reveal.
- Use the reader's own words, taken from reviews, feedback and Reddit.
- Keep the voice and personality of the narrator. No copywriter clichés ("game-changer", "walking on clouds").
- Compliance: no cure or treatment claims, and nothing that implies personal attributes in the second person. Use only the claims in brand.json.

## 9. Tag every concept so the data can teach us

Add this block to every concept file and Notion card:

```
DR tags: awareness=<unaware|problem|solution|product|most> · lead=<story|secret|problem|promise|proclamation|offer>
         belief="<one-belief sentence>" · problem_mechanism=<short> · solution_mechanism=<short>
         messenger=<type> · proof=<top 2> · offer=<live offer>
```

The weekly study and the batch research pull results by LF/DLF id. When enough concepts have spend, compare ROAS, CPA and hook rate by **awareness**, **lead** and **mechanism**, and write what wins for each brand into `research/longform_angles.md` → "What wins (DR tags)". Those findings beat any rule in this file.

## 10. Copy scorecard: grade before shipping

Score each item 0–2 (0 = missing, 1 = weak, 2 = strong). **Ship at 16/20 or above, and nothing scored 0 on items 1–4.** Otherwise rewrite the weak parts and score again. Put the score in the concept file.

| # | Check | 2 = strong |
|---|---|---|
| 1 | **Hook** | specific, tense, with an open loop. You'd stop scrolling. |
| 2 | **Awareness match** | the opening matches the chosen awareness level |
| 3 | **One belief** | every section builds it, nothing off-belief |
| 4 | **Mechanism** | the problem and solution mechanisms are clear and repeatable |
| 5 | **Proof** | at least 3 proof types, with specifics instead of superlatives |
| 6 | **Objections** | the top 4 are answered inside the story |
| 7 | **Enemy and price inversion** | failures are priced, mapped to features, and inverted |
| 8 | **Payoff** | the opening image is reversed, and every loop is closed |
| 9 | **Offer and close** | value equation covered, true deadline, guarantee, one CTA |
| 10 | **Line craft and compliance** | grade 4–6, sensory, the reader's words, claims-safe |
