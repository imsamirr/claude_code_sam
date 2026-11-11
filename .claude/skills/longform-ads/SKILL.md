---
name: longform-ads
description: Long-form static Meta ads for any brand. Each ad is one realistic phone-photo image plus a 5–14k character first-person story in the primary text. Covers onboarding a new brand, research (the brand's own top prospecting ads in Atria with transcripts, same-category competitors' long-form, the library's newest long-form, customer feedback, Reddit), an ideas table, writing (hook and open loops first, the winning angle's DNA, dated offers), 4 story images per concept with Kie.ai, Notion cards and a weekly schedule. Use for "long form copy", "long-form statics", "advertorial primary text", "turn our winners into long copy", "set up long-form for <brand>", "this week's long-form batch", or any long-copy request for a brand under ads/brands/.
---

# Long-form statics

A long-form static is **one image plus a long story in the primary text**. The story is a first-person narrator who hits rock bottom, meets a messenger, learns why the usual fix fails, finds the product through a person or a checklist, and pays off every loss set up earlier. The opening matters most.

All brand facts live in `ads/brands/<brand>/brand.json`. Nothing brand-specific is hard-coded here.

**Scripts:** in this repo, use `ads/atria_pull.py` and `ads/longform_images.py`. Portable copies are in `scripts/` for use in another repo: put them in `<repo>/ads/` with the `ads/brands/<brand>/` layout. They need `requests`, `python-dotenv` and `pillow`, plus `ATRIA_API_KEY` and `KIE_AI`.

**References** (read when the step says to):
- `references/playbook.md`: the craft, from about 95 winning long-form ads and a swipe file. Structure with % positions, 14 hook formulas, open-loop patterns, mechanism and bridge patterns, length norms, and what separates long runners from short-lived ads.
- `references/brand_config.md`: the `brand.json` fields this skill reads, and how to fill them for a new brand.
- `references/copy_template.md`: the exact file layout for one concept, including the fidelity table.
- `references/research_sources.md`: exact Atria, Drive and Reddit calls, filters and fallbacks.
- `references/image_prompts.md`: the image style, prompt recipe, overlay use, and the failure list for QA.
- `references/scroll_videos.md`: the **scrolling long-form video** format (a background loop, the story scrolling bottom to top, a voice-over and music) built with `ads/scroll_video.py` and Kie.ai Veo and Suno. Use it for "text scrolling video", "long form copy in a video", "make videos of our top video ads".

## 0. Non-negotiables

These are the lessons learned while building this program. Each one came from a correction.

1. **The angle comes from the brand's own winners, ranked by data.** Never pick an angle from a keyword the user mentions. Find where that keyword sits in the ranked winners, then use its winning **format**. Building on the weak cuts of a theme, or dropping the format (for example a competitor-teardown test), is the most common failure.
2. **Prospecting ads only.** Retargeting ROAS reflects a warm audience, not the angle. Group hook variants into script families: videos by transcript, statics by headline plus copy. Never group by shared primary text alone, because many different videos share one caption.
3. **Look at lifetime winners too.** A 90-day window can hide the brand's biggest historical angle (in Comfort Wear's case, Europe travel at about $370k lifetime). Read `research/data/video_transcripts.md` or pull lifetime winners.
4. **Study same-category competitors' long-form every run** (`competitors_longform`), plus the new long-form launched in the library. Borrow formats, never their lines or story details. A competitor ad launched days ago is a format test, not a proven winner.
5. **The hook and the opening open loops get the most effort.** Write the first 10 lines last, after the story works. Give 3 alternate hooks.
6. **The story is new; the DNA is kept.** Every enemy and its failure mode, the mechanism, the features mapped to each failure, the price inversion and the outcome lines carry over in the winners' own wording. Vary the narrator, age, job, setting, season, family situation, hook type and image scenes across a batch.
7. **Real offers, no placeholders.** Use `brand.json → offers` for the launch date, name the end date, and add ready-to-paste swaps for every later sale. Follow each offer's combination rules (for example "never combine 60% with gifts"). If a detail is missing, write the line without it and ask. Never put a bracketed placeholder in deliverables.
8. **Claims come from `confirmed_claims` only.** No doctor or specialist personas, no cure or treatment claims, no unconfirmed counts or star ratings. Don't promise a feature customers complain about (check the feedback research). Never imply the reader's religion, health condition or other personal attribute (Meta's personal-attributes policy). Tell it as the narrator's story.
9. **Images must look like real phone photos** and show a different story moment each. No logos (product, competitor or car), no characters, no fake app interfaces, and season and clothing must match the story. Look at every image and re-render the failures.
10. **Show the user the copy.** When they ask, paste the full primary text in chat. Every file and card includes the full text.

## 1. Onboard a new brand (once)

1. **Create the brand folder** by copying `ads/brands/_template/` to `ads/brands/<brand>/`. Fill `brand.json` (product, price, audience, personas, `prompt_rules`, `claims_to_avoid`, `confirmed_claims`, `offers`) and its `longform_program` block, following `references/brand_config.md`. Ask the user for anything you can't find:
   - the Atria ad account name
   - the confirmed guarantee, customer count and other claims
   - the sale calendar with exact wording and combination rules
   - the Notion board
   - the feedback sheet
   - direct competitors
   - schedule, batch size and split
2. **Check access:**
   - `ATRIA_API_KEY`, and that the `atria_pull.py` account resolves
   - the Atria MCP (`list_ad_accounts`, `search_library_ads`)
   - `KIE_AI` (`GET https://api.kie.ai/api/v1/chat/credit`)
   - Notion (fetch the board's data source)
   - Drive (`search_files` for the feedback sheet)

   Report anything missing.
3. **Baseline research,** following `references/research_sources.md`:
   - `python ads/atria_pull.py longform --brand <brand> --transcribe`, plus lifetime top videos
   - saved long-form ads (scope=saved, image, min_body_length 2000)
   - competitors' long-form
   - feedback sheet mining with a subagent
   - Reddit with a subagent

   Write:
   - `research/longform_angles.md`: ranked angles with spend, ROAS, CPA, and the angle DNA quoted from the transcripts
   - `research/learning/feedback_angles.md`
   - `research/learning/reddit_angles.md`
4. **First batch:** the ideas table (§2.2). Write after the user approves it or asks you to proceed.
5. **Schedule it,** if the user wants a recurring batch (§5).

## 2. A batch run (weekly or on request)

### 2.1 Research (every run)
- **Our winners:** `python ads/atria_pull.py longform --brand <brand> --transcribe`. Update `research/longform_angles.md`: the angle table, the angle DNA, angles below the bar, and claims conflicts.
- **Market long-form:**
  - new image ads with at least 2k characters of copy, launched in the last 7 days
  - new video ads of 60s+ in the category and adjacent categories (transcript: `get_library_ad_transcript` first; `transcribe_library_ad` only if missing, and only when the user has authorized credits)
  - saved ads
  - `competitors_longform`

  Log each ad's hook, first 10 lines, open-loop type and run days to `research/learning/hook_loop_bank.csv`. Re-check earlier entries at 7, 14 and 30 days; the survivors are the signal.
- **Customer voice:** the feedback sheet (`feedback_sheet`) and reviews. **Reddit:** `reddit.subreddits` (see the access notes).

### 2.2 Ideas table (show it to the user before writing a new batch)
Use the `longform_program.split` mix (default for a 10-concept batch: **6 iterations + 4 net-new**). One row per concept:

| ID | Type | Angle (source ads: spend · ROAS) | New story | Hook | Image scenes A/B/C/D |
|---|---|---|---|---|---|

- **Iterations:** spread them across the top angles by spend. Each one keeps its source's DNA in a different story. A competitor's proven format applied to our angle counts as an iteration.
- **Net-new:** directions never tested, checked against every LF file, `longform_angles.md` and account ad names. Each needs evidence: feedback counts, Reddit quotes or library long-runners. Score them on evidence, audience size, mechanism clarity and claims fit.
- **Variety check:** note the hook type of each concept. Don't repeat a narrator, setting or season within a batch or against earlier batches.
- **Save the table** to `research/learning/ideas_backlog.md` under the batch date, with the backlog below it. If the user swaps an idea, update the row and move the old idea to the backlog.

### 2.3 Write
Follow `references/playbook.md` and lay out each file exactly as in `references/copy_template.md`.
- **Format:** if the source winner is a test or comparison, the story *is* a test (one failed product per day, a graded closet, a bin of dead pairs). Don't let a mentor character replace the format.
- **Narrator and messenger:** the narrator comes from the winning persona. The messenger is from the narrator's world (a coworker, patient, stranger, group post) and says the mechanism close to the winners' wording.
- **Enemies:** every enemy appears with its price and failure mode, as the narrator's failed fixes.
- **The product:** brand at 50–65% through, handed over by a person or a criteria check, or held back to a late "EDIT:" in an organic-post format. Give the price and the price inversion.
- **Results:** day by day or shift by shift, with an honest week one. Pay off each loss set up earlier, then reverse the opening image.
- **Close:** the live offer with its end date, the confirmed guarantee, count and other claims, and 3 P.S. lines (a self-test, a second unit or gift, a share). Then **offer swaps** by date, **3 alternate hooks**, and the **fidelity table**.
- **Length:** 8–13k characters, grade 4–6 reading level, short lines. Measure the length and the brand's position (%) and report the real numbers.

### 2.4 Images (4 per concept)
Write specs in `<output_dir>/images/specs.json` (`<ID>_A` main, `_B`, `_C`, `_D`), one story moment each. Then:

```bash
python ads/longform_images.py --brand <brand> <IDs>
```

The script uses Kie.ai `nano-banana-pro` with an iPhone-realism prompt, renders at 3:4 and crops to a 4:5 1080×1350 JPEG. Use the spec's `overlay` for exact on-image text such as a text-message thread. Build a contact sheet, **look at every image**, and fix it against the failure list in `references/image_prompts.md`.

### 2.5 Notion
Create one card per concept in `longform_program.notion.data_source`. Use the title format and properties from the config. The body, in order:
1. type and sources, headline, CTA, landing page, live offer
2. the 4 images: upload each with `notion-create-file-upload`, POST the file, then put each `![…](file-upload://…)` on its own line with blank lines around it
3. the full primary text
4. the offer swaps
5. the alternate hooks

Existing image blocks can't be matched by `update_content`. To replace images, add a new images section above the old one and relabel the old one as superseded. Plain-text edits, like changing an offer line, match fine.

### 2.6 Deliver
Commit and push to the session branch. Reply with:
- a table: LF id, type, angle and source ad, the story in one line, the hook
- a contact sheet of the images (send it with SendUserFile)
- Notion links
- claims or offer questions
- data gaps and credits used

## 3. Updating live copy
When an offer, claim or calendar changes:
1. Update `brand.json` first.
2. Update every copy file, both the live close and the swaps.
3. Update the matching text on the Notion cards with `update_content`.
4. Confirm no placeholders remain (`grep -n "\[" <file>`).
5. Commit.

## 4. Learning loop
- **Ad names:** LF IDs go in ad names, so the next `longform` pull ties results back to each copy.
- **Each run:** mark backlog ideas as `written`, then add next batch's table.
- **Weekly:** fold what's working in `hook_loop_bank.csv` into `references/playbook.md`. That means hook types and open-loop types that survive, and which formats beat which in our account.

## 5. Scheduling
Use `mcp__claude-code-remote__create_trigger` with `create_new_session_on_fire: true` and a standalone prompt that includes:
- the clone and branch steps
- "follow the longform-ads skill for brand <brand>"
- reading the plan from `ideas_backlog.md`
- the research steps, batch mix, offers, images and Notion steps
- "say clearly if Notion is unavailable"

Start early enough to finish by the requested time (a 10-concept batch with 40 images takes about 2 hours), and keep the minute off :00. Connectors can't be attached from a session without them. Tell the user to add the Notion, Atria MCP and Google Drive connectors to the routine in claude.ai, and store the trigger ID in `longform_program.schedule_trigger_id`.
