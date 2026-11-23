# Market study: other brands' long-form ads, 2026-11-23

This is the second weekly study. It builds on `market_study_2026-11-16.md` and does not repeat it.

**Scope**
- **27 new ads from 19 brands,** all logged in `hook_loop_bank.csv` (rows dated 2026-11-23):
  - 21 long-form statics, 2.2k to 24.5k characters
  - 3 long videos: Orthora 310 s, ComfoFeet 153 s, and a 222 s fiction-app video
  - 2 scrolling-text videos
  - 1 dead Orthora tier list, kept as counter-evidence
- **Launch window:** 2026-11-16 to 11-22. The one older ad is ComfoFeet, which our team saved on 11-20.
- **Brands:** Auniva (run under 7 persona and "community" pages), Elvera, Pet Organica, Primal Remedies, The Health Insider, Finones, KIN, PhotoStick, a psychic reading service, Miracle Sheets, Provitalean, Sculptique, TrueForm, Amala, Susan Miller, Ageless Beauty Secrets, New World Publications, Orthora (and its "2026 Best Work Shoes" page), ComfoFeet (Healthcare Heroes).
- **Re-checks:** all 57 earlier rows. The 7-day status for the 11-16 rows is in `status_7d`; notes on the 11-19 rows are dated "chk 2026-11-23".

**Sources**
- **Atria MCP:** `search_library_ads` (library, advertiser and saved scopes), transcripts, and a paid transcription of 2 ads. Both transcription calls timed out and neither returned a transcript.
- **Atria Open API:** `ad-library/{id}` and `ad-library/search?brand_id=` for full bodies, re-checks and each brand's other ads.
- **Video files:** frames and audio from ffmpeg.
- **Meta Ad Library:** blocked again (WebFetch returned HTTP 403), so step 2 used Atria only.

**Rank is not survival.** Every new static here was at #1 on its page when pulled. Lessons rest on the 100+ day runs of the same advertisers' earlier ads and on last week's re-checks. Launch rank alone is not evidence.

---

## Top 10 lessons, ranked by evidence

### 1. Launch rank #1 is not a winner: 7 of last week's #1-ranked launches (plus one more) were dead within 10 days
Last week's study put a lot of weight on ads at their page's #1. The 7-day re-check:

| Ad | Peak rank | Fate |
|---|---|---|
| Volosso RV relaunch m29887040324237298 | 1/69 | dead after 5 days |
| EverWell 22.8k m2271699710358426 | 1/3 | dead after 3 days |
| PhotoStick 16.3k m1521996796617216 | 1/165 | dead after 5 days |
| Whisp / Amanda Grace m4531125787106064 | 1/85 | dead after 6 days |
| Koprez m1545555414044869 | 1/172 | dead after 10 days |
| Inflammation Fix 22k m2485271655333553 | 1/23 | dead after 6 days |
| Sculptara Airbnb m1732794365132737 | 1/51 | dead after 3 days |
| Julia Bennett 14.7k m1780221543188967 | 56/814 | dead after 2 days |

**Survivors at 7–12 days:**
- Jessica Whitney m2618847348628015 (rank 1/62)
- the Fleece nanny ad m1127959909841855 (1/136)
- Steadfast (1/31)
- YouthRite
- all three Sculptara bodies (21k at rank 4/36)
- Balmve
- TerraShell (4/2,426)
- Estella's scroll video (**#1/549 at 113 days**)
- Naturva's scroll video (2/131 at 21 days)
- **all 4 Orthora blog stories** (see lesson 7)

**Why it matters:** a rank in a pool of 3–80 ads at day 2 is noise. The playbook now says to judge market ads at **14+ days**. Last week's "rank 1" rules are marked *unproven* until they survive.

### 2. The 120–180-day long runners in health story ads are 15–24k characters
**Strongest new evidence.** The Auniva page network's earlier bodies, from each page's run history:
- **Arthritis Support Community:** 16.6k / 19.1k / 19.5k bodies ran **136–144 days**; 21.5k ran 137; 18.8k ran 131; 20.8k ran 125.
- **Nerve Support Community:** 15.5k ran 127; 15.4k ran 126; 19.3k ran 125; 18.4k ran 124; **24.0k ran 123**.
- **Jessica Bennett page:** 16.6k ran 139–144; **23.6k ran 120**; 18.1k ran 116.
- **Wellness Insider:** 18.0k ran 144–145.

Other long runners:
- **Elvera's gastroenterologist page:** one hook in a **12.5k cut and a 16.7k cut, both 145–180 days**, plus a 13.6k body at 159–160 days.
- **Pet Organica:** a 24.3k body **active at 107 days** (m1598289028617052, page "Riverside Veterinary Clinic").

**Why it matters:** this is the second week running that very long bodies are among the long runners. The 5–14k "sweet spot" is still a safe default. But for a proven story, the long cut (15–20k) is a **standard test, not an exception**. The Elvera pair shows the long and short cuts of one hook can both live for six months.

### 3. Open on someone else's moment, a dated domestic incident, then turn to the narrator
**The Auniva long runners' hooks are almost all small, dated domestic scenes,** often about someone else:
- "My father dropped a coffee mug on his kitchen floor in El Paso last March…" (126 days)
- "My son Dale repaved my driveway for Mother's Day…" (125 days)
- "I found a notebook in my husband's truck last March…" (124 days)
- "I found 11 unopened bottles of arthritis cream in a Rubbermaid bin in my dad's garage…" (125 days)
- "I pulled my mother of the bride dress out of the garment bag on a Tuesday afternoon in March…" (139–144 days)
- Pet Organica: "The one who gave me my dog back wasn't a vet. It was the kid I hired to pull my weeds." (107 days, active)

**This week's launches push it further.** The hook belongs to a stranger or relative, and the narrator's own pain arrives at 8–12%:
- a stranger frozen over a broken jar in a Kroger aisle (m1853666412318686)
- a cousin who now wears shorts (m1448257453488454)
- a father crying over a recipe card (m1450228956570288)
- a mystery snowplough driver (m1460351462153639)

**Counter-evidence on the same page:** "my mother's pickles in the back of my pantry" (m1667105185142600) was killed at 0 days. The Kroger-stranger version of the same jar idea is alive at day 7.

**The formula:** an ordinary object + a weekday and month + a place + one small physical failure. This is added as **hook type 20**.

### 4. One mechanism block, many conditions and pages; one body on two pages
Auniva bolts the same ingredient and mechanism block onto many conditions:
- knees, hands, bruising and perimenopause (amla and pomegranate)
- blood sugar
- ED, told by a urologist and separately by a wife

**One body ran on two pages at the same time:** the 16,595-char "mother of the bride dress" story, on Arthritis Support Community and on Jessica Bennett, **139–144 days on each**.

**This is CUURT's modular system turned sideways.** CUURT keeps the back half (mechanism, bridge, proof, offer, P.S.) and changes the narrator. Auniva changes the **condition and the narrator**.

**Our version:** a Comfort Wear back half (the cushioning and fit mechanism, the bridge, the offer, the P.S.) with front halves for:
- shift workers
- travelers
- grandparents
- people who walk a lot after 65

Comfort claims only; no conditions treated.

**Don't copy:** the fake "community", "clinic" and persona page names.

### 5. When a long ad dies, keep the back half and rebuild the front half
- **PhotoStick:** the 16.3k ad (rank 1, dead at 5 days) came back as m1127648890268432 (21.2k, rank 1 at day 1). The back half is line for line the same: timestamped failed fixes with prices, a relative with a cake at 39%, brand at 43–45%, a 3-point block, a log, the same offer and P.S. order. What changed:
  - **Trigger:** narrow and situational (a parents' estate cleanout) → universal (anyone who trusts the cloud).
  - **Headline:** now calls out a belief ("If You Trust iCloud… Read This").
  - **Dates:** synced to the launch week.
- **Volosso** relaunched its 294-day RV body last week. **Nerve Support** relaunched a byte-identical 19.1k body one day after the first launch faded (m29780612371559067 → m1450228956570288, now rank 1/24).

**Why it matters:** this extends non-negotiable 11. A dead LF concept isn't a dead body: if the back half was the account's DNA, rewrite only the trigger and the front 30%.

### 6. The messenger predicts the slow start, the narrator lives it, and the guarantee matches it
Appears in 6 of this week's statics:
- **Elvera:** "For about ten days, nothing obvious", then "Fern was right" (m28161283220215359).
- **The urologist** (m1618765572775417): the cardiologist friend predicts the week-by-week timeline. It is lived "just like he said", then reused as the guarantee terms and the P.P.S.
- **Bette's cousin** ("give it 6–8 weeks") and the others in the batch-A breakdown.

**Why it matters:** it pre-empts "it didn't work in week one" and makes the guarantee feel built around the story. It is the next step after last week's "reframed first result".

**Our version:** the messenger tells the narrator what the first shift will and won't feel like and when the second-week change shows up. The 30-day guarantee is framed as "four weeks of real shifts".

**Evidence level:** launches only, but the device appears across 3 advertisers. Recheck at 14 and 30 days.

### 7. Footwear: Orthora's blog stories are the first footwear long-copy statics to survive past 10 days; its tier lists keep dying
- **All 4 "2026 Best Work Shoes" stories are active at 12 days**, launched 11-11:
  - m4924210697806221, 5.4k, rank 27/199
  - m1598795165622572, 2.1k, rank 36
  - m1132103902647418, 6.9k, rank 42, rising
  - m1643871270551897, 1.8k, rank 48
- **For comparison:** Stepprs' long statics lasted ≤2 days, Koprez 10, and Hike's best 38.
- **Their tier-list cuts died again:** 7 tier-list video and static cuts dead at 0–1 days. Only one video cut (m1440472118256242) is alive at 10 days.
- **ComfoFeet's ranked video** (m1636971491222213, saved by our team) has run **42+ days at rank 44/538**. A Disney park worker counts down named brands she sees on struggling men over 60.
- **Orthora's new 310 s 3D-cartoon video** (m1794541261839977) uses a suspected-affair loop: a nurse sees her husband texting at night. Her best friend is the messenger, rivals are named in the voice-over, and the brand comes in at 58%.
- **No long copy this week from Hike, Stepprs or Nimbao.** All three are running short Black Friday copy.

**Why it matters:** a footwear story static of 2–7k with the brand late can survive. The "ranked shoe types" idea works as an insider video, not as a static.

### 8. Scroll videos: slower pace and square format are live too; the 4–4.5 words-a-second rule was too strict
**New this week, both music-only scrolls of a full static body:**

| Ad | Format | Length | Pace | Rank |
|---|---|---|---|---|
| Susan Miller m1662443618619314 | **720×720 square**, white condensed text with a dark outline over a blurred still | 1,035 s | **2.8 words/s** | 1/34, rising |
| Ageless Beauty m1543429487624419 | 9:16, text over a looping clip | 538 s | **2.5 words/s** | 7/310, rising |

- **The fast survivors stand:** Estella's 4 words/s is still #1/549 at 113 days, and Naturva's 4.3 words/s is rank 2 at 21 days.
- **Pace band for Mode B:** 2.5–4.5 words a second. Test both ends.
- **A "chapter one" video format (fiction app, m1475300441229556):**
  - The voice-over reads the first ~25% of an 18k story at about 3.6 words/s over a "satisfying" ASMR clip, with word-by-word captions.
  - It stops at a cliffhanger, and the primary text carries the full story.
  - Ranks 1, 2, 3, 6 and 10 of 34, with 6+ duplicates.
- **Our version:** this is a cheap Mode C. Voice-over the opening of a proven LF body up to its master loop, then point to the caption.

### 9. Concealment rituals as the symptom, and a public record that reverses
Appears in 5 or more of this week's statics:
- **The concealment:** the narrator *hides* the problem.
  - a cardigan in 84°F (m1127200210091088)
  - getting up "in stages" when nobody's looking (m1853666412318686)
  - a lie to a coworker ("I'm always cold")
- **The moral:** the confession becomes the close ("the hiding is worse than the thing").
- **The public record of the decline:**
  - a viral video with 41 replies (m1460351462153639)
  - a drawer of photos she cropped herself out of (m29018590564477226)
  - sitting in the wedding photos
- **The reversal:** a new record shows the change (37 replies; Darlene asks to stand next to her).

**Our version:**
- taking shoes off under the Thanksgiving table
- sitting on a bench "to hold the bags"
- being the one who takes the photos
- a new photo or a new group-chat reply as the payoff

### 10. Seasonal, live-dated stories, and offers that fit the month
- **PhotoStick's** story dates land in the launch week ("Thursday, November 12th… yesterday, Saturday Nov 21").
- **Finones** sets its story at Thanksgiving and closes on Black Friday "Buy 2 Get 4".
- **The psychic ad** has a Thanksgiving "empty chair" P.S.
- **Two Sculptique ads** carry "Black Friday" only in the headline.

**For Thursday 11-26 (Thanksgiving):** stories set at Thanksgiving or Black Friday shopping, the Black Friday offer to Dec 5, and Christmas swaps.

**Caveat:** this is launch-only evidence. The playbook's §10.3 still holds: softer closes survive and the story sells the click.

---

## New hook, open-loop and bridge patterns (short quotes, research only)

**Hooks**
- **20. Dated domestic incident / someone else's moment:** "My father dropped a coffee mug… in El Paso last March" (126 days).
- **21. Point-of-no-return near-miss:** "my finger was half an inch above the… signature pad" (PhotoStick).
- **22. Rule-break stress test as a static:** "I ate… a glazed donut… one hour before my fasting glucose test" (m3374935496026377).
- **23. Anonymous benefactor + promised answer:** "somebody plowed her driveway before dawn… explained it in eight words" (m1460351462153639).
- **24. Sale spotted in the wild** (short presells only, brand in line 1): "Saw this at my bus stop this morning…" (m1128424843303749).

**Open loops**
- **Prophesied timeline:** the messenger predicts it, the narrator lives it, and the guarantee reuses it.
- **Concealment → confession.**
- **Public record → new record.**
- **Deadline birth:** "can't be like this when that baby gets here", which closes at 75% (Elvera).

**Bridges**
- **A second-hand expert chain:** therapist → daughter → stranger. The expert stays clean and off-screen.
- **The two-messenger split:** an expert gives the criteria and refuses to name a brand, then an unrelated peer names it (Finones m29018590564477226).
- **An unrelated tradesman whose trade is the analogy:** a salt-truck driver's wet vs dry salt (m1460351462153639).
- **The villain's playbook as the scorecard:** the con's 5 moves are graded with a red pen (m1136559069269572).

**Proof**
- **On-off-on:** the symptom goes away from home and comes back at home (Miracle Sheets).
- **Disaster after the rescue:** the device dies after the save (PhotoStick).
- **A deliberate rule-break before the test.**

## What the long runners have in common (this week's evidence)
- **15–24k bodies** with a **small dated domestic hook,** often a relative or stranger.
- **The brand at 49–74%,** spoken by a messenger.
- **A guarantee-led close,** often with no price (Auniva).
- **The same body re-hooked,** relaunched and syndicated across pages.
- **The footwear survivors are short (1.8–7k) blog-voice stories** with the brand late.

## What died fast
- **Last week's 7 rank-1 launches, plus Julia Bennett's new body** (lesson 1).
- **Orthora's tier lists,** again (7 cuts at 0–1 days).
- **Volosso's CellGel+ "silent spouse" body** (m2196690051278068), dead after 1 day. The playbook's silent-spouse loop (§3.11) loses its only evidence and is marked unproven.
- **Auniva's "my mother's pickles" hook,** dead at 0 days.
- **British Health Blogs' rule-break video,** dead after 1 day. The rule-break hook is now tested in a static (m3374935496026377) to see whether it survives there.

**Compliance flags this week (don't copy):**
- medication stopped by the narrator or doctor (m2519293525263446, m3374935496026377)
- "clinically proven" and invented study numbers
- dementia claims
- NASA and Ritz-Carlton name-drops
- fake clinic and community page names
- explicit sex
- named competitor brands in our copy: ComfoFeet and Orthora do it, but we use **categories** instead ("the max-cushion runner", "the memory-foam slip-on").

---

## Test ideas for Thursday 2026-11-26 (Comfort Wear, Thanksgiving)

**Live offer:** Black Friday Sale, **60% off sitewide** or buy 2 pairs and get 2 free gifts (never combined), ending **Dec 5**. Add swaps for the Christmas Sale (Dec 6–31: 60% off plus 2 free gifts when you buy 2 pairs). **Claims:** 30-day money-back guarantee, 500,000+, HSA/FSA eligible, doctor- and podiatrist-recommended. No cure or treatment claims. StefanBrain writes all copy.

1. **MS9 Dated-domestic-incident re-hook (statics).**
   - Take our best LF body and keep it unchanged.
   - Write 3 new openers of type 20. Each is a small dated scene about *someone else*: a parent, a coworker, a stranger in a checkout line.
   - The narrator's own story starts by line 6.
   - Lessons 2, 3 and non-negotiable 11.
2. **MS10 Long cut vs short cut (statics).**
   - Write a 16–19k long cut of the strongest current LF body and launch it the same day as the current cut.
   - Evidence: Elvera's 12.5k and 16.7k cuts each ran 145–180 days; the Auniva pages' 15–24k bodies ran 120–145 days.
3. **MS11 Prophesied first month (statics).**
   - A nurse or traveler story where the messenger predicts the first shift and the first two weeks.
   - The narrator lives it "just like she said".
   - The 30-day guarantee is framed as "four weeks of real shifts".
   - Lesson 6.
4. **MS12 Thanksgiving concealment (statics, seasonal).**
   - The narrator hides the pain at Thanksgiving: shoes off under the table, "I'll sit with the kids' table", taking the photos instead of being in them.
   - The payoff is a December photo or a group-chat reply.
   - Close on the Black Friday offer to Dec 5.
   - Lessons 9 and 10.
5. **MS13 Scroll-video pace and format test (scroll video).**
   - Take one proven LF body, music only, and render 3 cuts:
     - 9:16 at 1 px/frame (about 2.5 words/s)
     - 9:16 at 2 px/frame (about 4 words/s)
     - **1:1 square** at 2.5–3 words/s for feed
   - The full body is the primary text in all three.
   - Lesson 8.
6. **MS14 Chapter-one voice-over video (new Mode C).**
   - An ElevenLabs voice-over reads the first 20–25% of a proven LF body, to its master loop, over a calm on-topic clip.
   - The video ends on "the rest is below", and the full story is the primary text.
   - Stay within the 5k-credit cap.
   - Lesson 8 (fiction app, 5 duplicates in its top 10).
7. **MS15 The insider who sees the shoes fail (video first, not a static).**
   - A theme-park, airport or hospital worker ranks the *types* of shoe she sees on people who struggle: max-cushion runner, memory-foam slip-on, clog, running shoe.
   - Comfort Wear is "the pair I started noticing on the ones who weren't sitting down".
   - **Categories only, no rival brand names.**
   - Lesson 7 (ComfoFeet, 42+ days). Orthora's tier-list statics died, so make it as a video or a scroll video.
8. **MS16 Back-half relaunch of a fast-dying LF concept.**
   - Pick a past LF concept that died fast and keep its back half: mechanism, bridge, results, offer, P.S.
   - Swap the narrow trigger for a universal one, plus a belief-callout headline ("If you think more cushion is the answer… read this").
   - Lesson 5 (PhotoStick).

**Re-check dates:**
- 2026-11-30 for the 14-day status of the 11-16 rows and the 7-day status of the 11-23 rows.
- 2026-12-16 for 30 days.

**The rows to watch:**
- the 4 Orthora blog stories
- ComfoFeet m1636971491222213
- the Arthritis Support Community Kroger hook m1853666412318686
- Elvera m28161283220215359
- PhotoStick relaunch m1127648890268432
- the two scroll videos m1662443618619314 and m1543429487624419
- Laura Peterson's rule-break static m3374935496026377

## Credits and access
- **Atria:** the plan's MCP-call and API-call allowances for this period were already used up, so every call this run was billed in AI credits. That was about 20 MCP calls, about 200 Open API calls for re-checks and brand scans, and 2 paid transcription attempts that timed out (charge unknown). The balance after the run was 12,930 of 14,000 monthly credits.
- **Meta Ad Library:** HTTP 403.
