# Writer spec: scrolling long-form video scripts for Comfort Wear

**Format:**
- A vertical 9:16 video, 4–5 minutes long.
- One looping background clip of the narrator's world, like a nurse at a station or a hotel hallway.
- The story scrolls up from the bottom as big bold centered text, and a voice-over (ElevenLabs) reads it word for word.

**Real examples (study the rhythm):**
- A vet ("I pulled 40 senior cats off our dental schedule")
- A hotel front-desk worker ("She looked me dead in the face and said, 'What if I just steal one?'")
- A physical therapist ("For 15 years I prescribed treatments to patients that never once worked on me")

Each is 260–320 seconds of copy, about 650–750 words.

**Product:**
- Comfort Wear, the Ortho Stretch Cushion Shoe, a women's shoe.
- About $60 (it was $120).
- Features: stretch-knit upper that gives as feet swell, arch support built into the shoe (nothing to pack flat), cushioned sole, wide toe box, slip-resistant grip, light.
- Narrators are women. Men may appear only as side characters.

## Deliverable

Write to the file path you are given. Use JSON: a list of exactly 3 objects, one per variation:

```json
[{"id": "LV01", "angle": "...", "source_ad": "name · 14d spend · ROAS",
  "title": "short story title",
  "voice": "female, ~60s, warm Southern"   // narrator voice notes
  , "background": "Veo prompt for an 8-second handheld vertical iPhone clip of the narrator's world, matching the story (people seen from behind or busy, not talking to camera; no text, no logos, no characters/landmarks, ambient only)",
  "caption": "1-3 sentence Facebook primary text (hook + curiosity), like the examples",
  "headline": "short headline",
  "landing_page": "/pages/...",
  "script": "paragraphs separated by a blank line"}]
```

## Script rules

1. **Length:** 600–720 words. Count them. Paragraphs of 1–3 short sentences, at most 35 words each, with a blank line between paragraphs. Write for the ear and the eye: no emojis, no bullet symbols, no hashtags, numbers as people say them ("twelve-hour shift", "$165").
2. **The hook is everything.** The first 2–3 paragraphs are on screen when the video starts and must stop the scroll. Use a specific scene, number, confession or contradiction, and open a loop that the story only closes near the end. Write the opening last, with the most care.
3. **Keep the source ad's DNA** (from source_transcripts.md for your angle). Keep:
   - the enemy shoes with their prices and their specific failure modes, in the winner's wording
   - the mechanism: walking vs standing, foam packing flat, feet swelling, weight, cobblestones or concrete
   - the features mapped to each failure
   - the price inversion ($60 beat the $165–180 pair)
   - the outcome lines ("not hurt less, didn't hurt", "not the one on the bench")
4. **Each of the 3 variations is a different story:** different narrator (age, job, life), different setting, season and family situation, different hook type, and a different background scene. Don't reuse these existing concepts:
   - plus-size grandma at Disney (5 shoes, 5 days)
   - ER nurse "shoe graveyard"
   - Lisbon anniversary "wish you were here"
   - night nurse Christmas morning on the couch
   - Florence mom on church steps
   - marching-band chaperone
   - 61-trip Disney passholder
   - nurse mom and nursing-student daughter
   - 71-year-old per diem nurse
   - kindergarten teacher
   - menopause feet
   - mom watching her CNA daughter in the driveway
   - church greeter June
   - 61-year-old holiday warehouse worker
5. **Structure:**
   - hook
   - "let me back up" plus identity
   - failed fixes (the enemy shoes, priced)
   - rock bottom
   - messenger or discovery, giving the mechanism in plain words
   - criteria
   - Comfort Wear named about 55–65% through
   - honest first week, then results
   - payoff that reverses the opening image
   - close
6. **Close, in this order:**
   - one line restating the enemy
   - the product line
   - "For Black Friday, Comfort Wear is 60% off sitewide until December 5th. And they're HSA/FSA eligible."
   - "Wear them for 30 days. If they don't feel different, send them back for 100% of your money back."
   - "Over 500,000 people who live on their feet have already switched."
   - "Tap below to see them."

   Also add, after the script in a separate field `offer_swaps`, the Christmas line ("For the Christmas Sale, Comfort Wear is 60% off, plus 2 free gifts when you buy 2 pairs, until December 31st.") and the New Year line ("For the New Year Sale, Comfort Wear is 40% off with free shipping until January 15th.").
7. **Claims guardrails:**
   - No doctor or podiatrist narrators, and no "podiatrist recommended".
   - No cure or treatment claims. A narrator can name her own diagnosis but never say it was cured.
   - No star ratings.
   - No "easy slip-on" or "hands-free", and no extra-wide promises.
   - No "walking on clouds".
   - No real-brand claims beyond the source ads' fit and feel statements.
   - Don't imply the reader's personal attributes (weight, health, age) in second person. For example, avoid "You're overweight". Say "If you're a bigger woman with a trip coming up…", the way the source ads do, or keep it in the narrator's voice.
8. **Also give `alt_hooks`:** 2 alternative opening paragraphs per variation.

Quality bar: read the three example openings above and the playbook at /home/user/claude_code_sam/ads/research/long-form-copy/PLAYBOOK.md (§2 hooks, §3 open loops). Report the word count of each script in your final message.
