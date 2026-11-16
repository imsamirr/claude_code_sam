# Market study: other brands' long-form ads, 2026-11-16

**The first weekly study.** There was no earlier `market_study_*.md` and no `hook_loop_bank.csv`, so this run creates the baseline.

**Scope**
- **39 ads from 22 brands,** logged in `hook_loop_bank.csv`:
  - 20 long-form statics
  - 16 long videos
  - 3 scrolling-text videos
- **Launch window:** 2026-11-09 to 11-16, plus 8 older reference winners pulled in step 2.
- **Per-ad breakdowns** (short quotes, % maps, loops) are in `market_study_2026-11-16_breakdowns/`:
  - `footwear_and_competitors.md`
  - `longform_statics.md`
  - `longform_videos.md`

**Sources**
- The Atria MCP:
  - `search_library_ads` (library, advertiser and saved scopes)
  - `get_library_ad`
  - `get_library_ad_transcript`
- **The Meta Ad Library was blocked:** WebFetch returned HTTP 403. Each brand's other ads were studied in Atria instead.
- **Video frames:** pulled from the ad CDN files with ffmpeg to confirm each video's format.

**How to weigh the evidence**
- **This week's launches are 0–7 days old.** They show which formats brands are testing now; they are not proof.
- **The proof comes from each brand's own long runners** (step 2): ads that ran 60–316 days, and ads that died within 10 days.
- **Every lesson below names its long-runner evidence.**

---

## Top 10 lessons, ranked by evidence

### 1. Scale a winner by keeping the body and changing the hook
**Strongest evidence this week.**
- **Jessica Whitney:** the "Linda Marsh" body ran 132–140 days with 3 different openers (13,675 / 13,687 / 13,698 chars). The new 911 pair has an identical body from line 3 on (m2618847348628015 and m1163955472954663).
- **Volosso:** the "ER nurse asked…" body ran 284–306 days with 3+ openers. The RV body (m2341229039664190) ran 294 days and was relaunched this week as m29887040324237298, now the brand's #1.
- **Sculptara (Dr. Amanda Kirsten):** 2 bodies × 3 hooks (m1723350862509872 and m1641789797959057 are the same body; only the first paragraph changes).
- **Balmve (Denise Hughes):** 1 template with the location swapped 5 ways (Bavaria m1419518233370292 is rank 4 and Heidelberg rank 2).

**Why it matters:** we write a new story for every concept. The market's long runners treat a winning body as the asset and test hooks on top of it.

### 2. Long statics get re-cut as music-only scroll videos once they've proven themselves
**Three brands do it.** The scroll video carries the full body, unchanged.

| Brand | Static | Scroll video of the same body |
|---|---|---|
| American Health Support Community (Naturva) | "My Wife Passed by Choking…", 17,124 chars, 197 days, best rank 1 | 795 s, launched 10 days later, ran 188 days |
| Herbal Health Findings (Estella) | "wasn't really gout", 117–124 days | m3736136016541332, 469 s, launched 2026-08-01, now **#1 of 551 at 106 days** |
| Emma Livy (Bloomin) | hysterectomy story, 47 days | 718 s, 43 days |

- **The text moves fast:** about 4.0–4.5 words a second (Estella; Naturva m1130129209949753 at 843 s / 21.9k chars). The full 11–29k body, P.S. stack included, scrolls over **one still photo**, with **music only** (empty transcripts and volume checks).
- **The primary text holds the same full story.** It is not a 1–3 sentence caption.
- **The slow one has stopped:** Emma Livy's video at about 1.5 words a second ran 43 days and is inactive.

**Why it matters:** our scroll videos are a separate 600–720 word write at 2.5 words a second. Re-cutting a proven LF static is cheaper and is what the long runners do.

### 3. Very long copy is not capped at about 18k
- **Julia Bennett:** "My mom's home health nurse asked why the bathroom still smelled…", **31,653 chars, active at 268 days.**
- **Jessica Whitney:** "labeled non-compliant…", 16,409 chars, 172 days.
- **Naturva:** 17,124 chars, 197 days.
- **This week's new ads at rank 1:**
  - EverWell, m2271699710358426, 22,830 chars
  - PhotoStick, m1521996796617216, 16,312 chars
  - Kirsten, 20.9k, rank 2 (it outranks the same advertiser's 9.2k body)
- **Counter-evidence:** Olivia Taylor's 3.9k "mom scratches herself raw" story died at 13–16 days, while the same page's 16k story climbed to #1.
- **The median across the 20 statics this week is 10.8k chars; 8 of the 20 are over 14k.**

### 4. The brand still lands at about 60% on median, but footwear brands often never say it at all
- **Measured over the 19 statics:** a median of 59% (range 2–92%). The videos have a median of 61.5%. This matches the playbook.
- **The difference is in the footwear and foot-pain set,** which holds the brand back or never names it:
  - **Koprez (Sarah Mitchell, m1545555414044869):** the product is revealed at 59% as one feature line ("The sleeve has straps."), and the brand appears only in the URL. It reached **rank 1 of 160 in 5 days.** Koprez's likely winner ("My plantar fasciitis treatment was working…", 14.6k) has run 63–65 days and is active.
  - **Orthora's blog page ("2026 Best Work Shoes"):** criteria first, then "I found one built that way" (about 68%), then an **"EDIT: Since people are asking"** with the brand at about 90%.
  - **Volosso RV:** never names the brand; a listicle landing page does the selling.
- **What makes an early brand work** (Volosso CellGel+ at 60%, BeetWise at 49%) **is who says it:** the brand is read off a tag, or spoken by the messenger.

### 5. "Week one, nothing" is no longer the norm; the stronger move is a reframed first result
- **"Week one, nothing" or near it:** only 3 of 10 adjacent statics (BeetWise, EverWell, Volosso CellGel+, the last with a day-4 relapse).
- **Fast small wins:** YouthRite day 3, Whisp day 2, Fleece night 1, Koprez "9 to a 5".
- **The best footwear version is Orthora's** (m4924210697806221): the first shift "I didn't notice anything, which was the point", and "sore isn't broken".

**Why it matters:** in shoes, comfort shows up on the first shift. Write "the absence of pain I'd stopped noticing" as the week-one beat instead of pretending nothing happened.

### 6. Revenge and social vindication is the hottest story engine this week, and the payoff scene is long
- **The new ads:**
  - Whisp (Amanda Grace, m4531125787106064): bathroom-stall gossip, rank 1
  - EverWell (m2271699710358426): "excluded from the trip / went anyway / they needed me / didn't pick up", rank 1
  - Emma Livy (m1677827350508231): Christmas-party fall leading to a New Year's Eve dance, rank 2
  - Orthora (m1926820028726353): "left me for the nurse I trained", 429 s, rising
  - Hike (m1910868523628134): 612 s
- **The vindication scene takes 15–20% of the body,** more than the results.
- **Caveat:** these are all 0–7 days old. The long-runner support for hook type 13 is the playbook's earlier evidence.

### 7. Five hook types not in our 14

| New type | Example ads |
|---|---|
| **Sunk-cost object** ("I've had an $87,000 RV in my driveway for 13 months. Haven't driven it once.") | Volosso RV body, 294 days in its first run |
| **Insider voyeur / the one thing the rich family has** ("I'm a nanny in the Hamptons…") | Fleece, m1127959909841855, rank 1 |
| **Hard deadline + found object** ("anything left in the closets by Friday 8 AM…") | PhotoStick, rank 1 |
| **Professional irony** (a 911 dispatcher who can't get a word of the script out when the call is about her own husband) | BeetWise, rank 1 |
| **Historical secret + heirloom** ("what US Army nurses wore… in 1944") | YouthRite, rank 1 of 204 |

Smaller new types seen in videos:
- **A deliberate rule-break as proof** (a doughnut before a fasting blood test; British Health Blogs, m2303460290510028)
- **An insult overheard from behind** (Forge, m1117556854368511)
- **Abroad-clinic revelation** (Balmve, Bavaria / Heidelberg)
- **Found-footage rescue** (TerraShell, m1131997602799573, rank 3 of 4,161)

### 8. Proof through measurement and logs, with the narrator's own doctor as the one who checks
Examples:
- a pressure map in the PT clinic (Volosso CellGel+)
- a BP notebook (BeetWise)
- a device-by-device recovery log with counts (PhotoStick)
- named competitor products as the failed fixes (BeetWise)

The narrator's own doctor appears late, as the person who checks the log, never as the messenger. **This fits our rule against doctor personas.**

### 9. The physical self-test as discovery and close: the thumb press
- **Orthora's blog stories** (m4924210697806221 and siblings): the messenger presses her thumb into the heel of the narrator's shoe. The close repeats it as the reader's task: "press your thumb into the heel of the shoes you wore today."
- **History:** the 11-06 versions were killed at 4 days. The 11-11 relaunches are active and **rising (up 31–51 ranks in 7 days)**, and our team saved them on 11-10.
- **Status:** moderate evidence; recheck at 14 and 30 days.

### 10. In footwear, long-form statics are rare and fragile; long story video is where competitors are spending
- **Stepprs:** 8 long-copy statics ever, each lasting at most 2 days.
- **Hike:** 84 long-copy ads, each lasting at most 38 days.
- **Orthora's main page:** no ad above 2,000 chars, ever.
- **Long video:** Hike launched 231 creatives since 11-09, many of them 100–612 s story videos. Oobend is testing about 350 videos of 120 s+, many in 3D cartoon. Orthora's 306 s Barcelona blind-date video ran 52 days at best rank 1, and its 125 s "Still in pain after every shift?" has run **188 days, active**.
- **Died fast:**
  - Orthora's senior-home / knee video (m1142023151666578): 3 variants dead in 0 days
  - Orthora's tier-list ads: 0–1 day
  - Koprez's third-party narrators (a coworker, a 91-year-old mother-in-law): 4–6 days
- **None of these competitors use scrolling text.** That gap is open for us.

---

## New hook, open-loop and bridge patterns (short quotes, research only)
- **Hook iteration on one body:** change only lines 1–2 (Jessica Whitney: "stay calm, help is on the way" vs "puts the caller's address on your screen").
- **A refrain on each failed fix:** every failed treatment ends with the same short line. Kirsten uses "Built for swelling" (m1723350862509872).
- **Phase-shift mechanism:** "it's not inflammation any more, it's breakdown", or foam that is flat "by hour 6" (Koprez, Sculptara, Orthora). The current fix was right for an earlier stage.
- **The silent-spouse loop:** "She hasn't said one word about it. That's the part that's killing me." (Volosso CellGel+). It opens at 0% and closes at 88%, when she cuts back her shifts.
- **A deadline event as the master loop:** a Friday 8 AM truck (PhotoStick), a New Year's Eve dance (Emma Livy), "my appointment was in nine days" (older).
- **Feature-as-reveal bridge:** "The sleeve has straps." (Koprez, at 59%). One mechanical feature on its own line stands in for the brand.
- **Tag-read bridge:** "CellGel+, by a company called Volosso", read off the product by the narrator.
- **"Almost forgot the link"** before the CTA, and an "I won't fake scarcity" P.S. (Naturva, Estella).
- **Gift close:** "one for each person you love" (TerraShell). This suits Christmas.

## What the long runners have in common
- **The body is the asset.** Brands relaunch it after a pause (Volosso RV after 294 days), re-hook it, and re-cut it as a scroll video.
- **One named loved one carries the emotion:** Nancy stopped asking, a wife's silence, a son's drawing.
- **Safer medical framing:** "with your doctor, not instead". Jessica Whitney's new body moved away from its riskier medication-refusal winner.
- **The full story sits in the primary text,** even on video.

## What died fast
- **Orthora:** the senior-home knee video (0 days) and the tier lists (0–1 day).
- **Stepprs:** every long-copy static (≤2 days).
- **Koprez:** third-party narrator stories (4–6 days).
- **Olivia Taylor:** the 3.9k sympathy story (13–16 days).
- **Orthora's blog stories, first launch:** killed at 4 days (11-06), then relaunched with the same copy, and now rising. A quick kill doesn't always mean the copy failed.

---

## 8 test ideas for Thursday 2026-11-19 (Comfort Wear)

**Live offer for all of them:** Black Friday Sale, **60% off sitewide** or buy-2-get-2-gifts (never combined), ending Dec 5. Add swaps for the Christmas Sale (Dec 6–31). Claims come from `confirmed_claims` only.

1. **Re-hook our best LF body (statics).**
   - Take the top-spending LF concept and ship it with 3 new opening paragraphs only, body unchanged.
   - The new openers are a sunk-cost object (a "$2,400 Europe trip booked and…" scene), professional irony (a nurse who tells patients to "stay off your feet") and a silent spouse.
   - Lesson 1.
2. **Scroll-video re-cut of a proven LF static (scroll video).**
   - Put the full LF body in a music-only scroll video with a still of the story's world, at about 4 words a second (whole-pixel scroll at 1080p).
   - Use the full LF body as the primary text too.
   - Test it against our current 2.5 words a second, 700-word cut.
   - Lesson 2.
3. **Long cut vs short cut.**
   - Write one Europe-travel story at about 18–22k chars and cut it to 9k, with the same hook, and launch both the same day.
   - Lesson 3 (Julia Bennett 31.6k at 268 days; EverWell 22.8k at rank 1).
4. **Nurse story with the brand held back to an EDIT.**
   - A story that discloses the brand late: criteria-first bridge, then "the one pair that passed", then an `EDIT:` with Comfort Wear at about 90%.
   - Use a new narrator and a new opening image; never the frozen peas, the kid's drawing or the passed-out-on-the-couch scene.
   - Lesson 4.
5. **Self-test close (statics).**
   - A self-test the reader can do tonight on their own shoes, used as the messenger's discovery and repeated as the CTA.
   - It must be **our own test**, not Orthora's thumb press. For example: bend the shoe at the arch and see where it folds, or check the wear pattern on the outsole.
   - Lesson 9.
6. **Revenge / vindication travel story.**
   - The narrator is left out of a group trip ("you'll slow us down"), goes anyway, and walks the cobblestones while the others need rest days.
   - Give the vindication scene about 15% of the body.
   - Lessons 6 and 7 (EverWell-style structure, our travel DNA).
7. **The rich client's one thing (net-new).**
   - A housekeeper or private nurse notices the one thing in a wealthy client's closet that the staff copy.
   - It is aspirational, not about pain, so it suits women's shoes.
   - Lesson 7 (Fleece nanny, rank 1).
8. **Christmas gift close (iteration on any winner).**
   - Close on "a pair for each person you love who stands all day".
   - Use the Dec 6+ swap (60% off + 2 free gifts when you buy 2).
   - TerraShell's gift close.

**Re-check at 7, 14 and 30 days** (2026-11-23, 11-30 and 12-16) for every row in `hook_loop_bank.csv`. These rows matter most:
- Orthora blog relaunches m4924210697806221, m1132103902647418, m1598795165622572
- Koprez m1545555414044869
- Sculptara m1723350862509872 vs m1141013728574763 (21k vs 9k)
- EverWell m2271699710358426 (22.8k)
- Estella m1665310724979818 (28.8k scroll)
- Naturva m1130129209949753
