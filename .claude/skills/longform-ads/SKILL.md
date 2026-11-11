---
name: longform-ads
description: Write long-form static Meta ads (one static image + a 5–14k character story in the primary text) built on the brand's OWN top-performing prospecting angles from Atria. Pulls winners with atria_pull.py longform, rolls script families up into angles, extracts the angle DNA (persona, enemy shoes or products, mechanism, proof, close), then writes new first-person stories that carry that DNA, with an angle-fidelity check. Use for "write long form copy from our winners", "long-form statics", "advertorial-style primary text", "turn our top videos into long copy", or any long-copy request for a brand under ads/brands/.
---

# Long-form statics from our own winners

The angle comes from **our ads**. The story is new. Story craft comes from `ads/research/long-form-copy/PLAYBOOK.md`.

Never pick the angle from a keyword the user mentions (for example "Disney"). Find where that keyword sits in the ranked winners, then use the winning **format** of that angle.

## 1. Pull the winners (always fresh)

```bash
python ads/atria_pull.py longform --brand <brand> --transcribe
```

**What the pull does:**
- Prospecting only, last 90 days. Retargeting is excluded, because warm-audience ROAS doesn't measure the angle.
- Groups hook variants and duplicate ad IDs into **script families**. Videos group by transcript; statics group by copy.
- A family qualifies at **≥ $3k spend and ROAS ≥ 0.95 × the account's prospecting ROAS**.
- Families are ranked by `spend × ROAS / baseline`.

**Paid transcription:**
- `--transcribe` pays Atria credits, and only for uncached videos with ≥ $2k spend (`--lf-transcribe-floor`).
- Tell the user how many were transcribed.
- "video not found" means Meta no longer serves that video. Use a sibling iteration's transcript instead and say so.

**Output:** `ads/brands/<brand>/research/data/longform_winners.md` (full copy and transcripts) and `.csv` (the ranking).

## 2. Analyze: roll families up into angles

Read **every qualifying family's full transcript and copy** in `longform_winners.md`. Then write `research/longform_angles.md`:

1. **Angle table.** Group families by persona + occasion + core argument, for example "nurse: running shoes are wrong for 12-hour shifts". For each angle, list:
   - its families, with spend, ROAS and CPA
   - the total spend
   - the most efficient member, which is often the best story seed
2. **Angle DNA**, quoted from the transcripts. These lines are already approved and already converting, so reuse them:
   - the job or occasion framing
   - the **enemy table**: each competitor or alternative, its price, and its failure mode, in the winner's own wording
   - the **mechanism**: why the reader's current choice fails
   - the solution features, mapped one-to-one to each failure
   - the price inversion
   - the outcome or identity lines
   - the openers
   - the close: offer, trial, count, HSA/FSA
3. **Below the bar.** List the angles that didn't qualify, so they aren't used as a base.
4. **Claims conflicts.** Compare the winners against `brand.json → claims_to_avoid` and flag every conflict to the user. Never silently drop a winner's element.

## 3. Write: one copy per top angle (default: the top 3 angles)

Each copy must keep the angle's **format**. If the winner is a comparison test, the story has to *be* a test: one failed shoe per day, a closet graded with a rubric, a bin of dead pairs. Don't let a mentor character replace the test.

- **Narrator:** a member of the winning persona, in the first person. Not a doctor or podiatrist persona.
- **The person who explains things:** someone from the same world as the narrator (a coworker, crossing guard, Facebook group post). They deliver the winners' mechanism lines close to verbatim.
- **Every enemy from the angle's table** shows up with its price and its failure mode, as the narrator's failed solutions.
- **Brand placement:** named at 50–65% of the copy, through a person handing it over plus a criteria check. Give the price and the price inversion.
- **Results:** shift-by-shift or day-by-day. Week one is honest. Pay off each loss planted earlier, and close on the winners' outcome line.
- **Close:** the winners' offer, then `[GUARANTEE]` and `[COUNT]` placeholders when brand.json conflicts, `[CONFIRM]` for any offer detail that isn't verified, and 3 P.S. lines (a self-test, a bundle or second pair, a share).
- **Also include:**
  - 3 alternate hooks, with at least one close to the top winner's hook
  - an image brief that follows brand.json `prompt_rules`
  - the winner's headline and landing page

Length is 8–13k characters (measure it; report the real number). Use the playbook's style rules: short lines, grade 4–6 reading level, dialogue carries the mechanism.

## 4. Angle-fidelity check (required, at the bottom of each copy)

Add a table: winner element → where it appears in the copy. It must cover:
- the format
- the persona
- every enemy and its failure mode
- the mechanism
- the features
- the price inversion
- the outcome lines
- the offer
- the brand position %

If any row is missing, fix the copy before you deliver it.

## 5. Deliver

- **File locations:**
  - copies: `ads/brands/<brand>/output/longform/LF<nn>_<angle>_<story>.md`
  - analysis: `research/longform_angles.md`
- **Commit and push** to the session branch.
- **Report to the user:**
  - the ranked angle table with spend and ROAS
  - which angle each copy uses and why
  - the claims decisions they need to make
  - any data gaps (untranscribable videos, credits spent)
