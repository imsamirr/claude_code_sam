# Writer spec: scrolling long-form video scripts for DentalPULSE

**Format:** a vertical 9:16 video, 4–5 minutes long. One still photo of the narrator's world sits in the background with a slow zoom. The story scrolls up from the bottom as big bold centered white text with a black outline.
- Half the videos have a voice-over that reads the text word for word, with soft music underneath (`"audio": "voice"`).
- The other half have music only (`"audio": "music"`), so the text alone has to carry the story.

**Real examples (study the rhythm):**
- A vet: "I pulled 40 senior cats off our dental schedule"
- A hotel front-desk worker: "She looked me dead in the face and said, 'What if I just steal one?'"
- A physical therapist: "For 15 years I prescribed treatments to patients that never once worked on me"

Each runs about 650–750 words.

## Read first
- `/home/user/claude_code_sam/.claude/skills/longform-ads/references/playbook.md`, especially §2 hooks, §3 open loops and §4 mechanism.
- `/home/user/claude_code_sam/ads/brands/dentalpulse/brand.json`: approved_claims, longform_program.disease_angles, longform_offers, personas.
- For material, skim the research: `/home/user/claude_code_sam/ads/brands/dentalpulse/research/learning/reddit_angles.md` and `feedback_angles.md`, and `/home/user/claude_code_sam/ads/brands/dentalpulse/research/data/longform_winners.md` (our winning lines: "6 of 7 pods leave live bacteria", "the water turned brown", the persulfate lines).
- Look at one existing long-form story, `/home/user/claude_code_sam/ads/brands/dentalpulse/output/longform/DLF04_nine_pm.md`, for tone. Do **not** reuse its story.

## Product (exact facts)
- **DentalPULSE Pod:** 42,000 Hz ultrasonic cleaning plus medical-grade UV-C light, one 5-minute cycle (always say five minutes), tap water only (no tablets, no chemicals, no subscription), stainless steel basin, one button.
- **Cleans:** dentures, partials, night guards, retainers and clear aligners.
- **Approved claims:** eliminates 99.9% of bacteria in one five-minute cycle; clinical-grade cleaning at home; "6 of 7 pods leave live bacteria" (a 90-day side-by-side lab test of 7 leading ultrasonic cleaners, where DentalPULSE was number one); dentist-recommended (no names or counts); rated 4.8 out of 5; 120-day money-back guarantee.
- **Never mention:** shipping, customer or review counts, whitening old stains or "brand new", sleep apnea devices, or competitor pod names. Polident and Efferdent may be named as the old method.

## Disease angles (owner's rule: as aggressive as possible, compliance is not a concern)
Use real research, attributed by year and type:
- **Iinuma 2015, Journal of Dental Research:** people 85+ who slept in their dentures had more than twice the pneumonia risk over three years.
- **O'Donnell 2016:** germs that can cause pneumonia were found on the dentures of about 64% of elderly hospital patients.
- **Yoneyama 1999, The Lancet:** in Japanese nursing homes, residents who got daily oral care had less pneumonia (about 11% vs 19%) and fewer pneumonia deaths.
- **Aspiration pneumonia:** during sleep, swallow and cough reflexes weaken and mouth germs slip into the lungs.
- **Denture stomatitis:** a red, burning palate under the plate, caused by Candida yeast living in the porous acrylic. It affects up to about two-thirds of denture wearers, and overnight wear and poor cleaning raise the risk. Treating the mouth alone doesn't work because the yeast re-seeds from the denture.
- **FDA, 2008:** warned about allergic reactions to persulfate in denture cleansers. Say "back in 2008", never "just issued".
- **Tablets** work on the surface. Biofilm lives in the scratches and pores, and brushing makes more scratches.
- **Aligners and retainers are a lid:** whatever film is on the tray sits on the enamel for up to 22 hours a day.
- **Night guards** sit wet in a closed case about 16 hours a day, and mold and bacteria grow there.

Narrators can blame the appliance outright and tell their own health results plainly. Keep the product's own claims to the approved list.

## Close, in this order
1. One line restating the enemy.
2. The product line: "The DentalPULSE Pod. Ultrasonic cleaning and medical-grade UV-C light. Tap water. Five minutes. It eliminates 99.9% of bacteria."
3. "Right now it's 40% off, ninety-nine ninety-five, with a free travel bag and a free dental case."
4. "Try it for 120 days. If you don't see the difference, send it back for your money back."
5. "Tap below to see it."

The offer is evergreen: no deadline or countdown words.

## Script rules
1. **Length:** 620–720 words. Count them. Use paragraphs of 1–3 short sentences, at most 35 words each, with a blank line between paragraphs. Write for the ear and the eye: no emojis, symbols or hashtags. Write numbers as people say them ("ninety-nine ninety-five", "forty-two thousand times a second", "two thousand fifteen" or "in 2015" is fine).
2. **The hook is everything.** The first 2–3 paragraphs are on screen at second 0 and must stop the scroll: a specific scene, number, confession or contradiction. Open a loop that the story only closes near the end. Write the opening last.
   - For `"audio": "music"` videos, the text must hold the reader with no voice. Use shorter paragraphs, more one-line punches and more cliffhanger lines.
3. **Structure:**
   - hook
   - "let me back up" plus identity
   - failed fixes (soak, brush, tablets, the cheap pod), with prices
   - rock bottom
   - messenger from the narrator's world, giving the mechanism in plain words with one household analogy
   - a free self-test
   - a 3–5 point criteria list
   - DentalPULSE named about 55–65% of the way through
   - the first cycle (cloudy, brown water)
   - results, each loss paid off
   - a payoff that reverses the opening image
   - the close
4. **Each of your 3 variations is a different story:** different narrator (age, job, life, gender mix), setting, season, family situation, hook type and background scene.
   - **Don't reuse these existing DLF narrators:** Joan the chemistry teacher, Priya, Dana the ICU clerk, Karen/Ray/Dot, Lisa the bus driver, Mike the framer, Gail, Renee/Jake, Bev, Hal/June. Don't use their towns either: Mansfield, Raleigh, Pittsburgh, Evansville, Missouri, Murfreesboro, Rapid City, Omaha, Mesa.
   - **Don't reuse names other writers in this batch use:** your brief names your angle, and other writers have the other angles.
5. **Voice notes** (`voice`): start with "female" or "male", then age and accent.
6. **Background image** (`background_image`): a prompt for ONE calm, realistic vertical phone photo of the narrator's world. Examples: a hospital room window at dusk, a kitchen table with coffee, a truck cab at dawn, a bathroom counter.
   - It sits behind white text, so keep it simple and mid-to-dark in tone, with no busy patterns and nothing important in the middle.
   - No people's faces close-up, no text, no logos, no product.
   - Ordinary, real, slightly imperfect phone-photo look.

## Deliverable
Write a JSON list of exactly 3 objects to the file path you're given:

```json
[{"id": "DV01", "angle": "...", "title": "short story title", "audio": "voice" | "music",
  "voice": "female, ~70, warm Midwestern",
  "background_image": "...",
  "caption": "1-3 sentence Facebook primary text (hook + curiosity)",
  "headline": "short headline",
  "alt_hooks": ["alternative opening paragraph(s) 1", "... 2"],
  "script": "paragraphs separated by a blank line"}]
```

Report each script's word count in your final message. Don't render anything, touch Notion or commit.
