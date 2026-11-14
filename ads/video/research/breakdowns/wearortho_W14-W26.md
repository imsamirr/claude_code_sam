# WearOrtho own winners — W14–W26 (ComfortWear / OrthoStretch)

Source: `ads/video/research/data/wearortho_video_index.json` (each > $20k CAD lifetime spend on Meta). Analysis folders: `ads/video/research/media/wearortho_analysis/<key>_<id>/`. Every hook_sheet and shots_sheet was viewed; full-res frames pulled with ffmpeg. Text sizes are given at 1080 px width (1080×1920 for 9:16, 1080×1350 for 4:5). "Glyph line" means the cap + descender band measured with `measure_text.py`, or with the same method on a cropped x-range when the background was busy. "Pitch" means baseline-to-baseline line spacing. ROAS ≈ 0 on W14, W15, W21 and W23 comes from how those ad sets were attributed. It is reported here but not read as creative failure. Audio: the RMS level of the gaps between VO words is −22 to −31 dB in every video (true silence would be below −50 dB), so all 11 have a music bed under the VO. Tracks can't be identified.

Ad-name decoding used below: "Kyro NNN vX ssY" = editor Kyro's video NNN, version X, scene/sound Y. "Kazi zach 5" = a different editor/creator. "Kashif 627 … Hook 1/2" = one body cut with two hooks. "10 Reasons Healthcare Workers" = the advertorial landing page (`/pages/here-are-7-reasons-why-this-is-the-best-gift-for-healthcare-workers`, Spanish `/pages/10-razones-…`).

---

### W14 — "Reply to comment: can I get a better deal?" → stacked Nurses Day offer (60% off) → mechanism → week-by-week results
**Data:** $79,160 CAD · ROAS 0.02 (attribution artefact) · 1 ad ("@NF - kyro 233v1ss2 - testimonial copy - 10 Reasons Healthcare Workers") · May–Sep 2025 · CTR 4.55% · 1.47M impr · 150.6s · 95 shots · avg 1.59s / median 1.43s (37.8 cuts/min) · VO 191 wpm · EN · 9:16
**Format / angle / persona:** offer-led reply-to-comment ad. The offer is the hook, then the body justifies it. Nurse persona (12-hour shifts). Copy is the "Emily, RN" testimonial. Headline "2025's Favorite Nurse Shoes".
**Hook (0–3 s):**
- Visual: full frame, ASMR-style "oddly satisfying" foot-spa footage unrelated to the product. 0.00–~1.6 s: gloved hands massage golden gel into a foot, with a brass bowl of gel in the foreground. ~1.6 s: an uncaught hard cut (the detector missed it) to a wooden reflexology tool pressing the sole. A red hand-drawn curved arrow animates in at 0.5–1.0 s, pointing from the comment sticker to the foot. The product first appears at 3.43 s (burgundy OrthoStretch on feet, POV).
- Text hook: TikTok "Reply to realemmma comment" sticker: white rounded box with tail, avatar, grey 'Reply to…' line, black text "Can you please give me a better deal on these 12-hour shift shoes?". Font is TikTok Sans/Proxima Nova Semibold, sentence case, 4 lines. Glyph line ≈ 32 px, pitch ≈ 56 px. Box ≈ 690 × 330 px at x 75–760, y ≈ 372–700 (19–36% from top).
- Verbal hook: "Can you please give me a better deal on these 12-hour shift shoes?" (0.00), then "All right, all right, I hear this all the time." (3.42)
- Audio: VO + music bed · Hook archetype(s): reply-to-comment / objection-as-question, offer-first, ASMR pattern-interrupt
- First hard cut at ~1.6 s (visual), 3.43 s (detected) · 2 visual changes + arrow animation in first 3 s
**Beat map:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–3.4 | hook | "better deal on these 12-hour shift shoes?" | foot-gel massage → reflexology tool | comment sticker + red arrow |
| 3.4–22.4 | offer | "biggest discount ever… not 30% or 40% but a ridiculous 60% off… code NurseDay2025 another 20%" | POV feet in 6 colourways, hand-held shoe, sole | top banner from 3.4 to ~16 s: "EXTRA 20% OFF Nurseday Sale ends soon!" (white box, black bold) + "🩺 Use Code NURSEDAY2025 👩‍⚕️" (dark slate box, white); white tags "❌ 30% OFF", "❌ 40% OFF" at 11.7/13.0 s; "20%" pop at 21 s |
| 22.4–42.7 | agitate/enemy | "instead of wasting money on running shoes… swell… rubber slippers… stink" | nurse mirror selfie, empty hospital bed, shoe in falling-dollar overlay (28–30 s), beige knit sneaker with red pain dot + lightning, pink Crocs, nurse switching | |
| 42.7–78.6 | mechanism | "smart foot technology… big toe box… breathable… non-slip grip" | 3D layered shoe render (46.3), X-ray foot over sole (49.7), glowing green leg bones (57.1), split screen (59.7), red X over knit sneaker and Crocs, close-ups of toe box/knit | |
| 78.6–113 | proof (timeline) | "after a few days… by week 2… after 4 weeks… after 8 weeks… pain-free" | 14 different women in scrubs: stairs, sofa, holding shoes to camera, kicking up a leg | |
| 113–146.9 | offer restack + scarcity + CTA | "exclusive to those watching… 40% + extra 20% = 60%… sell out within 24 hours… tap below" | website collection page on laptop (5.3 s hold), nurses pointing down at shoes | |
| 146.9–150.7 | end card | — | ComfortWear "TAKE ADVANTAGE OF DISCOUNTS / ON BUNDLES", 45-day seal, Free Shipping stamp, 3-colour packshot, "Doctor-Recommended" shield | |
**B-roll inventory:** POV walking/feet ~28 · product handling ~18 · talking-head (creator, muted, used as reaction/lifestyle) ~22 · product demo ~6 · problem visualisation (pain dot, swelling feet, Crocs, knit sneakers with ✕) ~8 · anatomy/3D ~5 · lifestyle (hospital, mirror selfie) ~4 · green-screen/website ~1 · ASMR foot-spa 2 · end card 1.
**Transitions & motion:** ~98% hard cuts. A two-frame glitch/RGB tear at 46.1–46.3 s on "these shoes are designed". Split screen at 59.7 s. The red ✕ graphic is drawn on. Falling-dollar overlay. No zooms beyond handheld motion.
**Caption system:** word-by-word karaoke. Montserrat ExtraBold, ALL CAPS, white with a soft dark shadow. The active word gets a blue rounded highlight box (#0F9BF3). 2 lines, 3–5 words, glyph line ≈ 53 px, pitch ≈ 93 px, band 69–77% from top (y ≈ 1328–1474). Consistent for the whole video. The offer banner sits above it at 16–22% from top (white box glyph ≈ 44 px, box 101 px tall, full width).
**Pacing:** hook holds 3.4 s on one comment, then the offer section runs at ~1.3–2.0 s per shot, the body at a 1.55 s average, and the CTA at 1.47 s. The longest hold is the 5.3 s website shot at 113 s, where the offer is restated.
**Offer & CTA:** the offer lands at 5.5 s (the earliest in the batch) and again at 114–146 s. Price stack: 40% sitewide + 20% code = "60%". Scarcity: "sell out within 24 hours", "only available to our video viewers". No ORDER NOW button.
**Steal this:**
- Open on a fake viewer comment asking for a discount. The ad then becomes the "answer", which makes the offer feel earned rather than pushed.
- Put a persistent two-row code banner (white row + dark row, with emoji) at the top for the first ~15 s while captions run below.
- After the mechanism, run a "few days → week 2 → 4 weeks → 8 weeks" results ladder, each step on a different smiling nurse.

### W15 — "Wanna go from this to this? Then don't buy these shoes" → wear-test diary weight-loss story
**Data:** $63,591 CAD · ROAS 0.05 (attribution artefact) · 2 ads ("kyro 224v3ss3 - weight loss" + Copy 3) · Apr–Dec 2025 (9 months, longest run in batch) · CTR 4.91% · 1.11M impr · 127.7s · 64 shots · avg 2.0s / median 1.8s (30.1 cuts/min) · VO 180 wpm · EN · 9:16
**Format / angle / persona:** reverse-psychology before/after hook, then a first-person "wear-test program" diary with time-stamped chapters. Persona: "Sarah", mom of three and a nurse, plus-size, with a weight-loss angle (walking more because the feet don't hurt). Landing page is the "how curvy women are transforming their weight & foot health" advertorial.
**Hook (0–3 s):**
- Visual: full frame with a title bar pinned at 15–27% from top. 0.00–1.0 s: slim woman in a white top, hands on hips. 1.0–1.25 s: dissolve to a plus-size woman in a black top and jeans in the same pose. Hard cut at 1.97 s to a close-up of black/mint OrthoStretch on a rug, and a red ✕ scales in from large to small (2.0–2.25 s). The product is visible from 2.0 s.
- Text hook: two-tier title bar. Tier 1: "WANNA GO FROM THIS" in a black condensed heavy face (Impact/Anton-style, white hairline stroke) on a full-width white bar (y ≈ 282–399). Tier 2: "TO THIS?" in white with black stroke on a full-width red bar (#E80000, y ≈ 399–525). Glyph line ≈ 75 px. At 1.97 s the text swaps to "THEN DON'T BUY / THESE SHOES" in the same bars.
- Verbal hook: "Want to go from this to this? Then don't buy these shoes." (0.00), then "These are not just comfortable shoes. They're literally programmed to transform your body back to its natural weight." (3.4–8.9)
- Audio: VO + music · Hook archetype(s): before/after (reversed), reverse psychology ("don't buy"), transformation claim
- First hard cut at 1.97 s · 3 visual changes in first 3 s (dissolve, cut, ✕ animation)
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–3.4 | hook | "go from this to this? Then don't buy these shoes" | slim → curvy dissolve; shoe + red ✕ | title bars |
| 3.4–9.2 | big claim | "programmed to transform your body" | shoe dangled by the heel tab, foot pressure-map scan on a tablet (5.1), plus-size torso (6.4) | captions |
| 9.2–39.8 | persona + backstory | "I'm Sarah, a mom of three and a nurse… wear-test program… 15 years of nursing… feet on fire… chained to my chair" | different women as "Sarah" (kids at an SUV, scrubs, couch); ComfortWear logo over a glass office tower (13.8 s); pink insole; nurse grabbing foot; red pain dot + lightning on a knit sneaker | |
| 39.8–52.5 | authority | "my podiatrist recommended me… designed differently… keep a diary" | podiatrist (stock woman, 36.3), 3D shoe render, red ✕ over a Hoka and over Crocs | |
| 52.5–111 | proof: diary chapters | "Six hours in… Week one… heel pain gone… down 7 pounds… One month… lost 23 pounds… Six month final notes… down four sizes" | chapter cards "6 Hours In" (52.5), "Week 1" (66.0), "1 Month Update:" (80.9), "6 Month Final Notes" (92.5) over heavily blurred footage; bathroom scale (76.1); shocked face; walking outdoors; a hammer smashing an old knit sneaker (95.2); "???" over a healthy-food flat-lay (103.7) | chapter titles larger, same box style |
| 111.6–123.9 | scarcity + CTA | "only letting 100 more nurses join… Tap below if you want in or keep torturing your feet" | nurse pointing down at shoes, POV feet | white pill "ORDER NOW" (red text) + chevron at ~78% from 118.3 s |
| 123.9–127.7 | end card | — | ComfortWear "TAKE ADVANTAGE OF DISCOUNTS" | |
**B-roll inventory:** talking-head/reaction (muted UGC women) ~20 · POV walking/feet ~14 · product handling/hero ~10 · problem visualisation ~7 · lifestyle (kids, stairs, nurse station, outdoor walk) ~8 · anatomy/tech (pressure-map scan, 3D render) 2 · press-style corporate (logo on tower) 2 · ASMR/destruction (hammer) 1 · end card 1.
**Transitions & motion:** hard cuts except the 1.0 s cross-dissolve in the hook. Chapter cards use a heavy gaussian blur on the background clip. Red ✕ scale-in pops. Emoji-style sticker "???" at 103.7 s.
**Caption system:** phrase captions, 2 lines, 3–6 words. Montserrat SemiBold, sentence case, white text on a semi-opaque black box (~65%) per line. Glyph line ≈ 48 px, pitch ≈ 110 px, box per line ≈ 105 px, band 64–76% from top. Chapter titles use the same style at about 1.2× size, centred higher (≈ 45–55%).
**Pacing:** hook cut at 2 s; body averages ~2 s. Holds of 3–6 s on emotional VO lines (30.2 s "chained to my chair", 6.1 s). Chapter cards hold 2.5–3.2 s each.
**Offer & CTA:** no price or discount in the VO. The offer is scarcity of access ("100 more nurses… this month"). ORDER NOW pill in the last 6 s. The end card carries the discount.
**Steal this:**
- Reverse-psychology hook: show the outcome the viewer fears, then say "then don't buy these shoes" over the product with a red ✕.
- Use a diary-chapter structure ("6 Hours In / Week 1 / 1 Month / 6 Months") as blurred title cards. It gives a long ad a visible progress bar.
- Frame the offer as access ("wear-test program, 100 spots") instead of a discount, and end with a negative-choice CTA ("or keep torturing your feet").

### W16 — "The worst travel advice I ever got" → named sneakers failed in Lisbon/Paris → nurse-friend tip
**Data:** $61,031 CAD · ROAS 1.53 · 1 ad ("TOFv5_CV3 | Kyro373v3hook2") · May–Jun 2026 · CTR 7.01% (2nd highest in batch) · 0.76M impr · 111.3s · 58 shots · avg 1.92s / median 1.77s (31.2 cuts/min) · VO 182 wpm · EN · 9:16 · no link URL in index
**Format / angle / persona:** contrarian "worst advice" story. Persona: a well-travelled 50s woman (22 countries) who is not a nurse; the nurse is the borrowed authority. Names Hoka and Nike, censored on screen as "H0kas" and "N!kes". Headline "2026's Best Shoes For Travelling".
**Hook (0–3 s):**
- Visual: full frame, three travel postcard shots. 0–1.2 s airplane window over clouds/mountains. 1.2–2.6 s bougainvillea over Positano with a bench. 2.6 s POV down at legs in white velcro sneakers on cobbles. No product until 64.3 s.
- Text hook: "The worst travel advice I ever got was / "just wear your comfortable sneakers."" White TikTok Sans/Proxima Nova Bold, sentence case, curly quotes, 2 lines, each on a black rounded box. Glyph line ≈ 57 px, pitch ≈ 72 px, full width (x 31–1045), 17–23% from top. Stays up for 0–4.4 s.
- Verbal hook: "The worst travel advice I ever got was just wear your comfortable sneakers." (0.00)
- Audio: VO + music (gap level −24 dB, the loudest bed in the English set) · Hook archetype(s): contrarian / "worst advice", wanderlust visual, common-belief attack
- First hard cut at 1.2 s · 3 shots in first 3 s
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–4.4 | hook | "worst travel advice…" | plane window, Positano, POV sneakers | top black-box title |
| 4.4–20 | credibility | "I'm not a bitter woman… After 22 countries…" | white sneakers on rug; worn knit sneakers; Kyoto, tiger in pond, Pisa; woman in kitchen shown in black & white | captions |
| 20–43 | problem: named competitors | "I wore H0kas in Lisbon… foam bottoms out… stabbing heel pain… N!kes in Paris… narrow toe box… swollen… sitting on a bench" | black Hoka on a box; cobblestones; heel with red pain dot + lightning; red-tinted swollen foot; Eiffel Tower at night; B&W: woman on chair, sneakers in a bin | brand names censored with 0/! |
| 43–58 | lesson/mechanism | "running shoes built for smooth surfaces… travel is the opposite… ten miles a day on stone" | worn running shoes, treadmill, Rome street under a red ✕, stutter-cut cobblestones (52.9–54.9: 0.3/0.4/0.2/0.03 s) | |
| 58–72 | discovery (borrowed authority) | "A nurse friend… found ComfortWear… if they hold up through 12-hour shifts…" | nurse selfie outdoors; nurse in garage; nurse wincing tying sneaker; product page on laptop (64.3 = first product); nurse laughing with shoe | |
| 72–90 | features + results | "wide toe box… arch support… firm enough for cobblestones… three trips, no pain" | navy OrthoStretch POV, X-ray foot overlay, B&W collapsed sneaker (contrast), cobbles in colour, suitcase | |
| 90–96 | social proof | "told my sister… called me from Lisbon to say thank you" | burgundy pair held, older woman holding pair | |
| 96.3–104.7 | offer + CTA | "40% off right now with a 45-day guarantee… send them back" | nurse mirror selfie, POV, older woman tossing shoes at camera | "ORDER NOW" pill + chevron under each caption |
| 104.7–111.4 | end card (6.7 s) | — | white blurred card: logo, "TAKE ADVANTAGE OF DISCOUNTS", navy "40% OFF SITEWIDE" pill, 45-day seal, Doctor-Recommended shield | |
**B-roll inventory:** stock travel postcards ~7 · POV walking/feet ~12 · competitor product (Hoka/Nike/generic sneakers) ~10 · problem visualisation (pain dot, red foot, bench) ~5 · talking-head/reaction (nurse friend, older woman) ~8 · product hero/handling ~8 · anatomy 1 · green-screen/website 1 · end card 1.
**Transitions & motion:** hard cuts. Desaturated black & white grading for the "bad past" (kitchen, bench, bin, collapsed sneaker), with colour for the solution. One stutter micro-cut run at 52.9–54.9 s. Red ✕ over a street scene.
**Caption system:** TikTok-native. Black TikTok Sans/Proxima Nova Semibold, sentence case, on white rounded boxes, 1–2 lines, 2–6 words. Glyph line ≈ 53 px, box per line ≈ 74 px, band 67–75% from top, centred and consistent. The hook title uses the inverted version (white on black) at the top.
**Pacing:** 3 cuts in the hook, a 4.6 s hold on "I'm not a bitter woman", then 1–2.5 s shots. The longest holds are the 3.6–3.7 s "no pain" walk and the Eiffel Tower.
**Offer & CTA:** lands at 96.4 s (87%): 40% + 45-day guarantee, ORDER NOW pill for the last 8 s, then a 40% end card.
**Steal this:**
- "The worst ___ advice I ever got was '___'" over aspirational stock (plane window, Positano). It attacks a belief, not a product.
- Name the competitors in the VO and censor them on screen ("H0kas", "N!kes") to get specificity without trademark issues.
- Grade the "before / wrong shoes" part in black & white and switch to colour when the solution arrives.

### W17 — (ES) "Probamos los zapatos más populares… el más caro quedó en segundo lugar" → top-5 ranking (Hook 2)
**Data:** $59,057 CAD · ROAS 0.71 · 1 ad ("TOFv3_J6 | Nurse | 627_Kashif_Spanish_Ortho_Stretch_Shoe_Tested5ShoesWinner Hook 2") · Nov 2025–Jul 2026 · CTR 6.45% · 2.03M impr (most in batch) · 93.8s · 62 shots · avg 1.52s / median 1.53s (39.6 cuts/min, fastest in batch) · VO 186 wpm · **Spanish** · 9:16 · no end card
**Format / angle / persona:** a 5→1 countdown "we tested the 5 most popular nurse shoes", each scored out of 10 with a price. Named: Crocs Classic Clog 7.8 ($50), Skechers Go Walk 8.1, Nike Air Max 8.2 ($120), Hoka Bondi 8.3, ComfortWear OrthoStretch 9.2 ($60). Logos blurred on screen. Nurse persona. Headline "Recomendada por expertos". Same body as W24.
**Hook (0–3 s):**
- Visual: 2×2 split grid of four nurses' feet/legs in different premium sneakers (cream Brooks-type, pink Hoka-type, grey On Cloud-type, white New Balance-type) in clinic/hallway settings, each panel moving (stepping, shifting weight). The text box sits on the centre seam. At 3.1 s cut to an overhead of a circle of 7 pairs of feet in different sneakers. No ComfortWear until 46–48.6 s.
- Text hook: "Cual crees que es el mejor zapato para enfermeras?" ("Which do you think is the best shoe for nurses?"). White Montserrat/Proxima Bold, sentence case, 2 lines, on a red-orange rounded box (#FC2F17). Box ≈ 880 × 198 px at y 861–1059 (45–55% from top). Glyph line ≈ 45 px, pitch ≈ 83 px. It stays through 6.2 s (moves up slightly at 2.75–3.0 s).
- Verbal hook: "Probamos los zapatos más populares entre enfermeras y el más caro quedó en segundo lugar, no lo vas a creer." ("We tested the most popular shoes among nurses and the most expensive came second, you won't believe it.") (0.00–6.12)
- Audio: VO + music · Hook archetype(s): comparison/test, question-engagement bait, result spoiler ("most expensive came 2nd"), "you won't believe it"
- First hard cut at 3.1 s · 1 cut + 4 moving panels in first 3 s
**Beat map:**
| t | beat | VO (ES → EN gist) | visuals | text |
|---|---|---|---|---|
| 0–6.2 | hook | tested most popular; most expensive came 2nd | 2×2 sneaker grid → overhead lineup | red question box |
| 6.2–19.7 | #5 Crocs | 7.8/10, ~$50, feels fine for the first hours, no arch support, pain after 4 h | hand holding pink Crocs, feet in white Crocs, Crocs on a gym floor, woman holding Crocs, nurse walking | "Número cinco:", "Les damos un 7.8 de 10.", "Cuestan como $50" |
| 19.7–27.7 | #4 Skechers | 8.1, memory foam flattens in weeks | grey slip-on, logo blurred, foam cross-section macro (squashed insole), stutter 27.1–27.3 | |
| 27.7–39 | #3 Nike Air Max | 8.2, $120, made for running, narrow, swelling | Air Max in hand, Nike on a tile floor, runner on a road, nurse on stairs, gloved hand squeezing toes in a narrow shoe | |
| 39–46 | #2 Hoka Bondi | 8.3, cushy but heavy, legs tire | white Hoka on a deck, black sneaker, nurse leaving house | "*Hoka Bondi*. 8.3." |
| 46.2–56.5 | #1 reveal + price | ComfortWear OrthoStretch 9.2, only $60 discounted, cheapest but best | maroon sneaker step (46.1), older woman holding navy pair "9.2 de 10.", POV walking with shadow | "cuestan solo $60 con descuento." |
| 56.6–74.3 | mechanism | made for foot-pain sufferers, not athletes: wide toe, arch support for PF, anti-slip sole, adapts to swelling, lasts longer | runner (athlete contrast), woman holding red pair "ComfortWear", X-ray green skeleton in shoe, 3D foot X-ray with orange bunion glow, finger pressing toe box | |
| 74.5–82.3 | proof/risk | 45 days to try (most give 30), thousands of reviews, cheapest beat the most expensive | 4 different creators holding shoes (thumb up, shocked face), pen on knit, white premium sneaker | "Miles de reseñas lo confirman:" |
| 82.3–88 | qualifier | if your feet suffer at work or you limp home | older woman, woman walking away in a parking lot | |
| 88.1–93.8 | offer + CTA | 40% off + free shipping, try them, return if not | woman with smoke/cloud-blur face effect, woman on couch, mirror selfie, POV blue shoes | "Hoy están con 40% de descuento", "y envío gratis.", "Pruébalos.", "los devuelves." |
**B-roll inventory:** comparison vs. competitor product ~28 (more than half the video) · POV walking/feet ~8 · product handling/hero ~12 · talking-head/reaction (muted creators) ~8 · anatomy/3D 2 · lifestyle (runner, nurse leaving home) ~4 · split-screen grid 1.
**Transitions & motion:** hard cuts. Micro-stutters at 27.1–27.3 s and 53.5 s. The 2×2 grid is the only split. Competitor logos have a gaussian blur patch.
**Caption system:** small TikTok-native boxes. Black Montserrat Bold, sentence case, with periods/colons ("Número cinco:"). White rounded box, 1–2 lines, 2–6 words. Glyph line ≈ 35–45 px, box ≈ 120 px tall single-line, ≈ 500 px wide. Position floats with the composition (10–80% from top), most often 70–78%. The hook question is the only coloured (red) box.
**Pacing:** hook 6.2 s (two shots), then a metronomic ~1.5 s per shot through all five entries. The score lines get their own shot each.
**Offer & CTA:** price is used as proof inside the ranking at 46–56 s ("cheapest but best"). Guarantee at 74.5 s. Offer at 88 s (94%). No end card and no button.
**Steal this:**
- A countdown ranking with a score + price per competitor, with the hero at #1 also the cheapest. Price becomes the twist instead of a hard sell.
- Hook with a question box on a 2×2 grid of competitor shoes ("Which is the best shoe for nurses?") plus a VO spoiler ("the most expensive came second").
- Blur competitor logos but say the brand names in the VO.

### W18 — "My doctor told me there was no cure to my foot pain" → long nurse plantar-fasciitis story
**Data:** $48,193 CAD · ROAS 2.08 · 2 ads ("kazi zach 5 v1 - 73% copy - 10 Reasons Healthcare Workers" + Copy) · Jul–Nov 2024 · CTR 2.88% · 4.00M impr (cheapest reach in batch) · 257.7s · 60 shots · avg 4.3s / median 3.63s (14.0 cuts/min) · VO 205 wpm · EN · **4:5** (720×900)
**Format / angle / persona:** a 4-minute first-person mini-documentary. A nurse is dismissed by her doctor, a retired podiatrist friend diagnoses plantar fasciitis and recommends "orthopedic shoes she wears". Persona: nurse whose family relies on her income. Copy: "73% of healthcare workers experience foot pain."
**Hook (0–3 s):**
- Visual: one continuous 3.63 s full-frame shot. A curvy woman in a mustard top and leggings, barefoot in a kitchen (clock, dog in foreground), hobbles toward the camera wincing, arms out, as if each step hurts. No product until 152.6 s (59% of runtime).
- Text hook: a two-tier title block at the very top. Tier 1: "MY DOCTOR TOLD ME THERE / WAS NO CURE" in white Montserrat ExtraBold caps on a full-width red bar (#FF0000, y 0–168, 0–12%), glyph line ≈ 43 px. Tier 2: "TO MY FOOT PAIN" in black Montserrat ExtraBold caps on a full-width white bar (y 168–262), glyph line ≈ 66 px. The punch line is about 1.5× larger than the setup.
- Verbal hook: "My doctor told me there was no cure to my foot pain." (0.00)
- Audio: VO (female, conversational) + music · Hook archetype(s): authority-dismissed / "no cure", pain demonstration, story open loop
- First hard cut at 3.63 s · 0 cuts in first 3 s
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–3.6 | hook | "doctor told me no cure" | hobbling woman | title bars |
| 3.6–45 | problem story | "dagger in my heels… continuous burn… I'm a nurse… couldn't make it to my car… doctor said typical strain, pain pills" | various women as narrator: rubbing feet on a bench, nurse walking, nurse in agony on a couch (10.8 s hold), nurse at door, pill bottle into mouth | captions |
| 45–89 | agitate | "hard hospital floors… ibuprofen… lightning strike every morning… family relies on my income" | walker, nurse slumped in a doorway in mask, feet on carpet, counting cash (84 s) | |
| 89–113 | discovery | "retired podiatrist… best in the state… took a look and guess what" | woman in a garden (10.3 s hold), feet examined, hand on sole | |
| 113–161 | education | "plantar fasciitis… inflamed tissue… why am I taking pills… support and cushioning… can't ice and stretch every day" | IV pole/hospital, ice pack, pills spilled (131.8), foot stretching, "But luckily" + first shoe (152.6), feet in OrthoStretch | |
| 161.9–200 | product reveal + features | "went online… here they are… ComfortWear OrthoStretch… two weeks… clever arch support… cushioned foam pad" | Google search screen, POV navy pair, held black/purple pair on grass, sole close-up, insole showing logo | |
| 200–241 | who it's for + warning | "if you're suffering from PF, bunions… damage permanently… back and hips… knee and back pain" | X-ray foot with red glow, bunion red glow, X-ray skeleton overlays on legs (knee) and back (spine/pelvis), hammer hitting a foot | |
| 241–251.6 | risk reversal + close | "try them a few days… 45-day guarantee… exchange… I promise" | nurse holding shoe to camera, sidewalk POV | |
| 251.6–257.7 | end card | — | "TAKE ADVANTAGE OF DISCOUNTS" card, music swells (−16.6 dB vs −30 dB bed) | |
**B-roll inventory:** problem visualisation (pain, rubbing feet, limping, pills, walker) ~22 · lifestyle (nurse at work/home, car, gym) ~12 · POV walking/feet ~8 · product handling/hero ~8 · anatomy/X-ray overlays ~6 · green-screen/website (Google search) 1 · end card 1.
**Transitions & motion:** hard cuts only. No graphics apart from anatomy overlays and red pain glows. Long handheld holds, with a quick burst 146.7–150.6 s (0.5–0.9 s shots on "stretch my feet every single day").
**Caption system:** CapCut-style auto captions. White Proxima Nova/Montserrat Medium, sentence case, on a translucent dark rounded box (~50% black), 1–2 lines, 3–7 words. Glyph line ≈ 32 px (≈ 2.4% of frame height, small), band 79–84% from top (4:5 frame). Consistent.
**Pacing:** slowest English video in the batch: 4.3 s average shot, holds of 8–10.8 s on emotional beats (11.5 s, 28.9 s, 64.3 s, 74 s, 95.8 s). Speeds up only in the last 20 s (2.65 s average).
**Offer & CTA:** no discount and no "tap below" in the VO. The only risk reversal is the 45-day guarantee at 243.8 s (95%). Discount and CTA live in the end card, the copy and the advertorial.
**Steal this:**
- Two-tier red/white headline: the setup in a smaller white-on-red line, the punch in bigger black-on-white. "My doctor told me there was no cure" is an authority-dismissal hook that pre-frames the product as the overlooked fix.
- Hold the product back to ~60% of runtime and spend the first half on a credible pain diary. It worked at the cheapest CPM in the batch (4M impressions).
- Use skeleton/X-ray overlays on real bodies (knees, spine) for "it also helps knee and back pain" cross-benefit claims.

### W19 — (ES) "Mi doctor me dijo que no había cura para mi dolor de pies" → Spanish version of W18
**Data:** $47,989 CAD · ROAS 1.53 · 1 ad ("@NF - V2_Hook1_063_Spanish_OrthoStretch_5_FootPainCure - emoji copy - 10 Reasons Healthcare Spanish Workers") · Nov 2024–Jan 2025 · CTR 4.72% (vs 2.88% for English W18) · 3.14M impr · 362.4s (longest in batch) · 79 shots · avg 4.59s / median 4.36s (13.1 cuts/min) · VO 141 wpm · **Spanish** · 4:5
**Format / angle / persona:** a line-for-line Spanish VO of the W18 script, re-cut on the same B-roll pool. The hook clip is identical. Many body shots are re-ordered or new: a stock doctor at 52.8 s for "el médico", a dancing nurse, an old-woman care scene, a red muscle macro. The slower Spanish VO (141 vs 205 wpm) stretches it to 6 minutes. Copy is emoji-bullet with 40% off and "120.000 reseñas de 5 estrellas".
**Hook (0–3 s):**
- Visual: identical to W18 (barefoot woman in mustard top hobbling toward camera, 3.67 s single shot).
- Text hook: "MI DOCTOR ME DIJO / QUE NO HABÍA CURA" in white Montserrat ExtraBold caps on a red bar (y 0–172), glyph line ≈ 62 px (larger than W18's 43 px). "PARA MI DOLOR DE PIES" in black caps on a white bar, glyph line ≈ 57 px, edge to edge (x 24–1058), 14–18% from top. The setup and punch are the same size here, and the Spanish punch line is longer.
- Verbal hook: "Mi doctor me dijo que no había cura para mi dolor de pies." (0.00–3.40)
- Audio: VO (female Spanish) + music (gap −23.5 dB, louder bed than W18) · Hook archetype(s): same as W18
- First hard cut at 3.67 s · 0 cuts in first 3 s
**Beat map:** same story beats as W18, stretched about 1.4×: problem 3.7–58 s → agitate 58–118 s → discovery (podiatrist friend) 118–142 s → education (fascitis plantar, pills, ice) 142–204 s → first shoe 203.9 s ("pero afortunadamente", 56%) → reveal/features 209–275 s → who it's for + warning (bunions, permanent damage, knee/back skeletons) 275–339 s → guarantee "garantía de 45 días" 341–346 s, with an Amazon-style product listing screenshot at 343 s → close "te prometo…" → end card 356.3 s (music −14 dB).
**B-roll inventory:** same mix as W18: problem visualisation ~28 · lifestyle ~14 · POV/feet ~10 · product ~9 · anatomy/X-ray ~8 (adds a red muscle-fibre macro at 150 s and a bunion glow) · stock doctor 1 · website/Google/listing 2 · end card 1.
**Transitions & motion:** hard cuts only; holds up to 11.9 s (119.8 s, woman in garden).
**Caption system:** same as W18 (white sentence case on translucent dark box), glyph line ≈ 30 px, band 79–82%. Lower-case Spanish captions, 3–8 words, sometimes breaking words mid-line ("có / mo").
**Pacing:** 4.6 s average throughout, no acceleration until the last ~25 s.
**Offer & CTA:** guarantee only, at 341 s (94%). The rest is in the end card and copy.
**Steal this:**
- Port a proven English story ad to Spanish as a full VO re-record over the same footage. It earned 1.6× W18's CTR (4.72% vs 2.88%) at a similar spend.
- Make the Spanish hook text bigger than the English (62 vs 43 px). The longer Spanish line still fits as two bars.
- Running time doesn't need trimming for Spanish: a 6-minute cut still spent $48k.

### W20 — (thumbnail only) "ComfortWear's cushioning lasts over 12 hours" — older-woman talking head with burgundy pair
**Data:** $46,338 CAD · ROAS 2.18 · 1 ad ("Kyro 49_1-ss1 - 12h testim copy - voted 2023 best H - 10 Reasons Healthcare Advertorial - Copy") · Jan–Apr 2024 · CTR 3.30% · 2.44M impr · video no longer downloadable, so duration, cuts, VO and beat map are unknown. **Analysed from thumbnail + copy only.**
**Format / angle / persona:** talking-head testimonial / spokesperson. The ad name "voted 2023 best H" suggests a "Voted best nurse shoe" headline hook; the index headline is "Voted 2024's Best Nurse Shoe". Copy is a long first-person testimonial from a nurse working 12–14 h shifts 6 days a week whose "loving husband bought me these" (gift angle, Christmas–Q1 flight), plus 4 emoji benefit bullets.
**Hook (thumbnail):**
- Visual: 4:5 (1080×1350), medium close-up of a 55–65-year-old brunette woman in a navy top in a warm yellow dining room. She holds a burgundy OrthoStretch pair at chest height, toward the camera, mid-sentence with eyebrows raised. Product visible in frame.
- Text: "ComfortWear's cushioning / lasts over **12 hours**". Clean white sans (Roboto/Helvetica-like medium-bold, double-story "a") with a thin black outline/shadow and no box. "12 hours" is in cyan/teal. Glyph line ≈ 53–56 px, pitch ≈ 95 px, 76–86% from top.
- Hook archetype(s): spokesperson testimonial + specific claim ("12 hours").
**Steal this:**
- Older (55+) woman holding the product to camera, with a single quantified durability claim captioned and the key number in an accent colour.
- Pair it with a husband-gift testimonial in the copy for Q4/Q1. The talking head carries the claim and the copy carries the emotion.

### W21 — (ES) "Mujeres Curvy, atención: estos zapatos me salvaron los pies, la espalda y la confianza"
**Data:** $41,292 CAD · ROAS 0.00 (attribution artefact) · 1 ad ("@NF - 095_Spanish_Video_OrthoStretch_K170_H2 - emoji copy - 10 Reasons Healthcare Spanish Workers") · Feb–May 2025 · CTR 5.21% · 1.81M impr · 138.8s · 43 shots · avg 3.23s / median 3.1s (18.6 cuts/min) · VO 165 wpm · **Spanish** · 4:5
**Format / angle / persona:** persona call-out testimonial. A 250 lb warehouse worker (not a nurse), on her feet 9 h a day. The doctor said "lose weight and get surgery". She found the shoes in a forum of curvy women. Body-positivity values angle. Despite the "Healthcare" ad name, the VO persona is a warehouse worker. This is the Spanish "curvy" counterpart of W15.
**Hook (0–3 s):**
- Visual: full frame, outdoor gravel path. 0–1.8 s: a curvy blonde woman in an all-black tracksuit walks toward and past the camera (wide shot), wearing black/mint OrthoStretch. 1.8 s cut to a low tracking shot of her feet in the shoes on gravel (4.2 s). The product is on screen from 0.0 s, the only video in the batch besides W15 to show it in the first 2 s.
- Text hook: "Zapatos cómodos que / cuidan pies y espalda" ("Comfortable shoes that care for feet and back"). White Montserrat SemiBold, sentence case, on a bright blue rounded box (#3D8DFF), 2 lines. Glyph line ≈ 33 px, pitch ≈ 69 px, box ≈ 720 × 160 px at the top (4–16% from top). Persists 0–6 s. The VO, not the text, carries the call-out.
- Verbal hook: "Mujeres Curvy, atención, estos zapatos me salvaron los pies, la espalda y la confianza." (0.00–5.98)
- Audio: VO + music (bed −22.5 dB, loudest in batch; end-card swell −16 dB) · Hook archetype(s): persona call-out ("Curvy women, attention"), triple benefit (feet, back, confidence), product-on-body demo
- First hard cut at 1.8 s · 1 cut in first 3 s
**Beat map:**
| t | beat | VO gist | visuals | text |
|---|---|---|---|---|
| 0–6 | hook | curvy women, attention… | walking wide → feet tracking | blue box |
| 6–33 | problem | 250 lb, warehouse 9 h/day 40 h/week, years of unsupported shoes, doctor: lose weight + surgery | talking head (curvy woman in glasses, selfie), feet on scale, woman carrying a box, swollen foot, red X-ray leg, older doctor (in a beige highlight box: "Cuando finalmente fui al médico"), B&W face close-up | captions; key phrases get a beige or blue box |
| 33–50 | discovery | found a forum where curvy girls share tips | Google "best shoes for…" search, woman walking in a park, Reddit-style forum screen ("encontré un foro" in a blue box), woman with arms wide | |
| 50–67 | product + features | OrthoStretch cushion shoes, skeptical but tried; arch support, heel cushioning | shoe on foot, lacing, grey pair, finger pressing heel cushion with red arrow, logo in insole | |
| 67–90 | results | PF healing, no sore knees or lower back; bought two more pairs; outlasted any shoe at a fraction of the cost | heel X-ray glow, 3D heel, knee and spine skeleton overlays, talking head, POV pairs | |
| 90–106 | use cases + values | pair for work, errands, walks; supports body-positivity/women's-health initiatives | sidewalk, 3×3 grid of 9 UGC creators holding shoes (99.4 s), talking head, gym dumbbell | |
| 106.9–116 | risk reversal | 45-day money-back, return no questions | X-ray foot in shoe, close-up shoe | |
| 116–132.8 | CTA to persona | "para mis compañeras curvy… un salvavidas para sus pies… te están esperando" | nurse in scrubs, creator holding shoe, packshot on hand, woman throwing arms up outdoors | |
| 132.8–138.8 | end card | — | discounts card | |
**B-roll inventory:** talking-head (creator selfie, persona) 7 · POV walking/feet ~8 · product handling/demo ~8 · anatomy/3D/X-ray ~6 · problem visualisation ~4 · green-screen/website (Google, forum) 2 · lifestyle (warehouse, gym, park) ~5 · testimonial grid 1 · stock doctor 1 · end card 1.
**Transitions & motion:** hard cuts. Red arrow graphic on the heel cushion. 3×3 creator grid as social proof.
**Caption system:** TikTok-native. Black Montserrat SemiBold, sentence case, on white rounded boxes, 1–2 lines, 3–8 words. Glyph line ≈ 40–43 px, band 77–87% from top. Selected key phrases switch the box colour (beige/tan for the doctor line, blue for "encontré un foro") as emphasis.
**Pacing:** 3.2 s average, steady from start to end, with longest holds of 5–6 s on talking-head lines.
**Offer & CTA:** no discount in the VO. 45-day guarantee at 106.9 s (77%), then an emotional persona CTA. Discount is in the copy (40%) and the end card.
**Steal this:**
- Spanish persona call-out in the first word ("Mujeres Curvy, atención…") while the visual already shows a curvy woman walking in the shoes.
- Recolour single caption boxes (beige/blue) to flag the turning points of the story without changing caption style.
- Use a "values" beat (brand supports body positivity) before the guarantee for identity-driven personas.

### W22 — "Remember when nurses wore those crisp white uniforms and white shoes every single day?" → nostalgia origin story
**Data:** $37,268 CAD · ROAS 1.11 · 1 ad ("TOFv3_L132 | Kyro322v1_ss2") · Dec 2025–Apr 2026 · CTR 7.91% (highest in batch) · 1.03M impr · 142.4s · 82 shots · avg 1.74s / median 1.67s (34.5 cuts/min) · VO 166 wpm · EN · 9:16
**Format / angle / persona:** nostalgia / "they don't make them like they used to" myth-buster. 1960s–70s nurses in white shoes didn't hobble, athletic shoes and memory foam made nurses' feet worse, so "we rebuilt the classic nurse shoe with modern materials". Nurse persona. Copy is the Emily RN testimonial (same as W14). Headline "Expert-Recommended".
**Hook (0–3 s):**
- Visual: full frame, archival black-and-white film (soft, grainy) of two 1940s–60s nurses in white uniforms and caps walking past a brick building, laughing. One continuous 3.5 s shot, then more archival hospital-ward footage. No product until 103.3 s (73% of runtime).
- Text hook: "REMEMBER WHEN NURSES WORE / THOSE CRISP WHITE UNIFORMS AND / **WHITE SHOES EVERY SINGLE DAY?**" Poppins ExtraBold/Black caps. Lines 1–2 are black; line 3 is red (#FD0000) with a black outline. All three sit on one white box with a 2-tone border (cyan #00A9FE top half, red bottom half) spanning x 42–1037, y ≈ 1242–1557 (65–81% from top). Glyph line ≈ 37–40 px, pitch ≈ 75 px.
- Verbal hook: "Remember when nurses wore those crisp white uniforms and white shoes every single day?" (0.00–5.98)
- Audio: VO (female) + music · Hook archetype(s): nostalgia / "remember when", archival pattern-interrupt, rhetorical question
- First hard cut at 3.5 s · 0 cuts in first 3 s (camera drift only)
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–6.4 | hook | "Remember when…" | archival nurses | bordered box |
| 6.4–26.5 | nostalgia contrast | "60s and 70s, before scrubs, before Crocs, before running shoes… end of a double shift still standing tall… no one hobbling… What happened?" | archival nurse at bedside; modern nurse flipping hair; feet in white clogs (logo blurred); POV black sneakers; archival nurses in a ward, smiling; modern nurse hobbling to car; nurse screaming holding foot; doctor examining; big black "?" over a woman (25.4) | |
| 26.5–52 | what worked | "built by people who understood the job… not running shoes… not fashion sneakers… firm arch support… wide fronts… sturdy leather" | archival lab/factory; Puma running shoes on a neon floor; nurse holding a banana-yellow sneaker; old white leather nurse shoes; archival footage with burned-in timecode, stutter cuts 39.5–40.8 (0.07–0.23 s) on "bending, lifting" | |
| 52–81 | enemy | "we got convinced athletic meant better… memory foam and gel inserts… break down fast… gone by your third shift… narrow designs squeeze… modern nurses more foot, knee, back pain" | runner, nurse holding an orange Hoka, gel insert squeezed, worn sneakers, nurse grimacing, knee/back pain | |
| 81–99 | authority | "retired nurse who worked from 1965 to 1995… we just had shoes that worked" | elderly smiling woman (stock), archival nurses, archival engineer | |
| 99–106 | origin | "studied what made them effective… rebuilt them with modern materials… that's how ComfortWear OrthoStretch was born" | cobbler hammering a leather sole, stitching machine, product reveal: nurse laughing holding black/mint pair (103.3), pair on a wooden table | |
| 106–122 | features | wide toe box, firm arch, cushioning, slip-resistant, breathable | knit close-ups, X-ray skeleton in shoe, fast push-ins on soles, POV walking | |
| 122.5–129 | social proof | "over 500,000 healthcare workers have switched back" | 3×3 grid of nine UGC creators holding shoes | "OVER 500,000 HEALTHCARE WORKERS" |
| 129.6–137.8 | offer + CTA | "40% off… if they don't bring back that feeling… return them. Tap below." | nurse laughing with pair, foot in shoe, nurse dancing | |
| 137.8–142.4 | end card | — | "CHRISTMAS CLEARANCE SALE / 40% OFF SITEWIDE", 45-day seal, Free Shipping, 3-colour packshot on a tree background | |
**B-roll inventory:** stock/archival footage (B&W nurses, wards, labs) ~24 · problem visualisation (hobbling, pain, worn shoes) ~10 · competitor product (Crocs, running shoes, Hoka, gel insert) ~10 · product handling/hero ~14 · POV walking/feet ~5 · anatomy 1 · craftsmanship (cobbler) 4 · testimonial grid 1 · talking-head reaction ~8 · end card 1.
**Transitions & motion:** hard cuts. The archival clips have film-scan borders and burned-in timecodes left visible on purpose for authenticity. Stutter micro-cuts at 39.5–40.8 s. Big "?" graphic at 25.4 s. Fast handheld whips on product close-ups at 112–119 s.
**Caption system:** Poppins ExtraBold, ALL CAPS, white with a black outline/shadow, no box, 1–2 lines, 2–4 words. Glyph line ≈ 56 px, band ≈ 69–72% from top for one line (up to ~66–76% for two). Consistent. The hook box is the only boxed text.
**Pacing:** hook holds 3.5 s on archival footage, then 1.1–2.9 s shots. Archival sections cut slightly slower; the features section speeds up to ~1.2 s per shot.
**Offer & CTA:** 40% at 129.6 s (91%), "return them", "Tap below". Seasonal end card.
**Steal this:**
- Archival B&W footage as a hook pattern interrupt, with a "Remember when…?" question in a box with a cyan/red border and the last line in red.
- Reframe the product as a revival ("we rebuilt the classic nurse shoe with modern materials"), backed by cobbler craftsmanship B-roll.
- A 3×3 UGC creator grid for the "500,000 healthcare workers switched" beat.

### W23 — "87% of nurses are wearing the wrong shoes" → "Dr. Sarah Adams" expert discovery story
**Data:** $36,670 CAD · ROAS 0.00 (attribution artefact) · 1 ad ("@NF - kyro 219v3ss3 - 73% copy - 10 Reasons Healthcare Workers - Copy") · Apr–Jun 2025 · CTR 3.71% · 1.34M impr · 165.7s · 82 shots · avg 2.02s / median 1.87s (29.7 cuts/min) · VO 161 wpm · EN · 9:16
**Format / angle / persona:** expert/doctor narrator ("Dr. Sarah Adams", whose nurse mom came home in tears). Hidden-industry-secret mechanism: "shoe companies design for the first 2–3 hours". Then discovery of "biomechanical engineers", price anchor vs $200–300 medical shoes, scarcity. Nurse audience.
**Hook (0–3 s):**
- Visual: 0–1.63 s, a handheld close follow of a young woman in a "DESTIN" sweatshirt, teal leggings and tan Ugg-style boots (the "wrong shoes") stepping through a doorway. 1.63 s hard cut to a wide shot of her walking down a hallway toward the camera. 3.5 s cut to "Dr. Sarah Adams" (Asian woman in a white coat, smiling). Product first at 73.5 s (44%).
- Text hook: "87% OF NURSES" in black Montserrat ExtraBold caps on a white box (y ≈ 394–514, 21–27% from top), glyph line ≈ 55 px. It pops in with a scale/blur at 0.00–0.25 s. At 1.75 s "ARE WEARING / THE WRONG SHOES!" pops in: red (#EB0000) Montserrat ExtraBold caps on a white box (y ≈ 1190–1400, 62–73%), glyph ≈ 55–57 px, 2 lines. Both stay to 3.5 s.
- Verbal hook: "87% of nurses are wearing the wrong shoes." (0.00–3.12)
- Audio: VO + music · Hook archetype(s): stat shock, "you're doing it wrong", two-beat text reveal
- First hard cut at 1.63 s · 2 visual changes (cut + second text pop) in first 3 s
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–3.5 | hook | "87% of nurses…" | Ugg walker | 2 text boxes |
| 3.5–17.5 | authority + origin | "Hi, I'm Dr. Sarah Adams… mom came home from nursing shifts in tears… felt helpless" | doctor in white coat; nurse at a vending/teal room; older nurse with stethoscope; foot with red pain dot + lightning; heavy woman climbing a step; masked nurse with head in hands | |
| 17.5–33 | secret | "8 years in medical school… why do our feet break down… shoe companies hiding a secret… designed for the first 2–3 hours" | lecture hall, "???" over a blurred hand, glass office tower ("Most shoe companies"), knit sneaker pressed, worn sneakers in a bin with a thumbs-down emoji, woman giving a thumbs-down | |
| 33.9–46.6 | mechanism of failure | "hour 8, 10, 12, feet swell a full size, blood pools, torture devices" | pink Crocs POV (6.8 s hold), red X-ray leg with blood cells, red-glow leg | |
| 46.6–69 | expert proof | "run my own clinic… tested running shoes, clogs, expensive orthotics" | woman at clinic event, worn white sneakers under a red ✕, pile of nurse shoes, Crocs in a store, orthotic insole, sneakers in a trash can, row of worn sneakers | |
| 69–79 | new mechanism | "small team of biomechanical engineers cracked the code… first shoe that adapts to your feet" | surgeon in OR, engineer at bench, lab, first product shot (black/purple held aloft, 73.5), 3D render, X-ray skeleton in shoe | |
| 79–102 | features | "arch support prevents PF… wide toe box eliminates bunion pressure… hospital-grade slip resistance" | split screens (88.7–90.7 s: shoe / heel; red ✕ over B&W heel), 3D foot with orange bunion glow, slip on wet tile | |
| 102.5–117 | price anchor | "premium comfort at just $59.95 vs $200+ on inferior medical shoes… I've recommended $300 shoes that couldn't handle…" | product-page screenshot (strike-through $99.00 → $59.95, SALE tag), Amazon-style listing of $300/$349 work boots, falling-apart $300 sneakers | |
| 117–135 | scarcity | "nervous about sharing… about to end their 40% healthcare discount… 3,000 pairs this week… cheaper than orthotics" | nurse in scrubs, product pairs, creator talking with burgundy pair, listing screenshot again | |
| 135–151 | results + guarantee | "spend all day on my feet… try with zero risk… 45 days… full refund" | creator talking heads, mirror-selfie woman, burgundy pair, POV | |
| 151.6–161.9 | close + CTA | "40% off ends soon… selling fast… click below to secure your pair" | "Remember: The 40% OFF", shoes held up, thumbs up | ORDER NOW pill + chevron (157.6+) |
| 161.9–165.7 | end card | — | discounts card | |
**B-roll inventory:** problem visualisation ~14 · competitor/wrong shoes (Uggs, Crocs, worn sneakers, orthotics, $300 boots) ~14 · stock "authority" (doctor, lecture hall, OR, lab, engineer, office tower) ~8 · product handling/hero ~16 · POV walking/feet ~8 · anatomy/3D ~6 · offer/price screenshots 3 · talking-head creators ~10 · end card 1.
**Transitions & motion:** hard cuts. Split-screen pairs at 88.7–90.7 s. Graphic stickers: "???", thumbs-down emoji, red ✕, red pain dot + lightning. The hook text has a scale pop.
**Caption system:** TikTok-native. Black Montserrat SemiBold, sentence case, on white rounded boxes, 1–2 lines, 2–6 words. Glyph line ≈ 52–55 px, band 61–72% from top (sits higher than most). Consistent.
**Pacing:** steady at ~2 s per shot. The longest hold is 6.8 s on the Crocs POV at 33.9 s ("what happens in hour 8?"). The CTA section is slightly faster (1.87 s).
**Offer & CTA:** price first at 103.5 s (62%) with an anchor; 40% discount "ending" at 119.8 s; guarantee at 143 s; CTA at 157.7 s with an ORDER NOW pill.
**Steal this:**
- Two-beat stat hook: "87% OF NURSES" (top, black on white) then "ARE WEARING THE WRONG SHOES!" (lower, red on white) about 1.75 s later, over a person wearing the wrong shoe.
- Hidden-design-flaw mechanism ("built for the first 2–3 hours, not hour 12"), shown with a time-stamped swelling X-ray.
- Price-anchor screenshots: own product page with the $99 strike-through next to a marketplace grid of $300+ boots.

### W24 — (ES) "Analizamos cinco de los zapatos más populares…" → same top-5 ranking body as W17 (Hook 1)
**Data:** $34,288 CAD · ROAS 1.22 · 1 ad ("TOFv3_J8 | Nurse | 627_Kashif_Spanish_Ortho_Stretch_Shoe_Tested5ShoesWinner Hook 1 - Copy update 12.18.25") · Dec 2025–Jul 2026 · CTR 5.41% · 1.30M impr · 95.5s · 61 shots · avg 1.57s / median 1.53s (38.3 cuts/min) · VO 185 wpm · **Spanish** · 9:16 · no end card
**Format / angle / persona:** identical body to W17 from "Número cinco" onward (every shot and caption matches; W24 timestamps sit +1.6 s later). Only the first ~7.8 s differ.
**Hook (0–3 s):**
- Visual: 3-panel horizontal stack (three equal rows) of competitor sneaker close-ups, each moving. Top: a black running shoe on a blue mat, hands lacing from 2.5 s. Middle: a chunky white platform sneaker stepping. Bottom: a white trainer with its logo blurred. One continuous 5.0 s shot, then at 5.0 s a nurse in navy scrubs and a surgical cap dances toward the camera ("para ver cuál realmente ayuda"). No ComfortWear until ~48 s.
- Text hook: no separate headline. Live VO captions in the red-orange box style (#FC2F17, white Montserrat Bold, sentence case), centred over the 2nd/3rd panel seam at 61–70% from top. Glyph line ≈ 34–36 px, box ≈ 515 px wide. Sequence: "Analizamos cinco / de los zapatos" (0–1.6), "más populares" (1.75–2.5), "que usan las enfermeras / durante sus turnos" (2.75–5.0), "para ver cuál realmente ayuda" (5.0–7.8).
- Verbal hook: "Analizamos cinco de los zapatos más populares que usan las enfermeras durante sus turnos para ver cuál realmente ayuda con el dolor de pies." ("We analysed five of the most popular shoes nurses wear on shift to see which actually helps with foot pain.") (0.00–7.62)
- Audio: VO + music · Hook archetype(s): comparison/review promise, utility framing (no twist, no question)
- First hard cut at 5.0 s · 0 cuts in first 3 s (3 moving panels, 3 caption swaps)

**Hook 1 (W24) vs Hook 2 (W17), same body:**
| | W17 — Hook 2 | W24 — Hook 1 |
|---|---|---|
| Layout | 2×2 grid of nurses' feet in premium sneakers → overhead 7-pair lineup at 3.1 s | 3-row stack of sneaker close-ups (5.0 s) → dancing nurse at 5.0 s |
| On-screen text | One static question headline: "Cual crees que es el mejor zapato para enfermeras?" (large box, 198 px tall, centre seam 45–55%, glyph ≈ 45 px) | No headline. Running VO captions in small red boxes (glyph ≈ 35 px, 61–70%) |
| VO | Result spoiler + curiosity: "…y el más caro quedó en segundo lugar, no lo vas a creer" | Neutral method + benefit: "…para ver cuál realmente ayuda con el dolor de pies" |
| Hook length to "Número cinco" | 6.2 s | 7.8 s |
| People in hook | 4 nurses' legs (persona match) | shoes only, then a nurse at 5 s |
| Results | $59.1k spend, 2.03M impr, **CTR 6.45%**, ROAS 0.71 (Nov 2025–Jul 2026) | $34.3k spend, 1.30M impr, CTR 5.41%, **ROAS 1.22** (Dec 2025–Jul 2026, copy updated 12.18.25) |
- Read: Hook 2 won on scale and click-through. It pairs an engagement question with a VO twist ("the most expensive came second") and has a shorter run-in. Hook 1 converted better per the account's attribution, but it sits in a different ad set (J8 vs J6) with updated copy and the ROAS caveat, so treat that as weak evidence. Both ran in parallel for 7+ months, so both are worth keeping. For new tests, Hook 2's structure (question headline + spoiler VO + persona legs) is the one to iterate.
**Beat map / B-roll / transitions / captions / pacing / offer:** identical to W17 (see above), shifted +1.6 s. Offer at 89.7 s (94%), no end card.
**Steal this:**
- When hook-testing a body, vary three things at once (layout, text type, VO promise). Here the question + twist version scaled about 1.7× more spend.
- Use a 3-panel product stack as a cheap hook layout built from the competitor B-roll you already need for the body.
- Keep the hook under ~6 s before the first list item lands.

### W25 — "Cheap orthotic shoes from Tennu are not that good" → founder "Ryan" story vs. Chinese knockoffs
**Data:** $34,178 CAD · ROAS 2.03 · 1 ad ("@NF - Kyro 125v3ss3 - 73% copy - 10 Reasons Healthcare Workers") · Jul–Oct 2024 · CTR 4.68% · 1.17M impr · 206.1s · 113 shots (most in batch) · avg 1.82s / median 1.8s (32.9 cuts/min) · VO 199 wpm · EN · **4:5**
**Format / angle / persona:** founder origin story with an enemy: "Ryan" (bearded man, B&W) says his brand is "going bankrupt because of cheap copies on a Chinese site" (Temu, written "Tennu"). Origin: nurse wife with plantar fasciitis, surgery suggested, "Dr. Rowens" whose production was halted, "That's how ComfortWear was born". Then 3 mechanisms, 2 testimonials, toe box, a 45-day guarantee and 3 bonuses.
**Hook (0–3 s):**
- Visual: 0–2.74 s, a young nurse in teal scrubs leaning on an office chair tosses a pair of cheap white sneakers out of frame over her shoulder with a deadpan, sceptical face (motion at 0–1.25 s). 2.74 s hard cut to Ryan, a bearded man at a desk in black & white. 3.6 s: an anatomical overlay of legs walking in purple OrthoStretch (first product).
- Text hook: "CHEAP ORTHOTIC SHOES / FROM TENNU" in black Montserrat ExtraBold caps on a white rounded box (y ≈ 537–705, 40–52% from top), glyph line ≈ 45 px. "ARE NOT THAT GOOD" pops in at 1.75 s in white caps on a red rounded box directly below (y ≈ 709–760, 53–56%), glyph ≈ 45–50 px.
- Verbal hook: "Cheap orthotic shoes from Temu are not that good. I'm Ryan and this is how I created an orthopedic shoe brand that's now going bankrupt because of cheap copies on a Chinese site." (0.00–10.9)
- Audio: VO (male, founder) + music · Hook archetype(s): enemy/us-vs-them (Temu knockoffs), contrarian, founder confession, underdog ("going bankrupt")
- First hard cut at 2.74 s · 2 visual changes (shoe toss, red text pop) + 1 cut in first 3 s
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–2.7 | hook | "cheap orthotic shoes from Temu…" | nurse tossing shoes | white + red boxes |
| 2.7–11 | founder + stakes | "I'm Ryan… going bankrupt because of cheap copies" | B&W Ryan, legs-anatomy overlay, man with head in hands (B&W), woman dumping shoes in a bin | |
| 11–45 | origin: wife | "met my wife, a nurse… 12-hour shifts… 5 years ago she started complaining… osteopath… severe PF… surgery" | stock nurses and doctors, feet massaged, B&W nurse coming home, "Heel and Arch Pain" clinic poster, injection, foot cast, laptop search | |
| 45–68 | mentor + struggle | "found Dr. Rowens… production halted, economically inefficient… a few pairs left… relief immediate… I made a plan" | doctor with tablet, clinic team photo, man holding a foot model, warehouse drone shot, red stock-market chart (57.2), cardboard box, nurse kicking up her leg, pencil sketch of a plan | |
| 68.2–85 | birth + claims | "That's how ComfortWear was born… 5 years… thousands of positive reviews… stylish, PF, bunions, tired legs" | product held up on grass (first clear hero), 3 creators holding pairs, X-ray foot, bunion, tired-leg footage | |
| 85–112 | enemy | "cheap knockoffs flooding the market from a well-known Chinese site… fall apart… ruin our reputation… $20 shoes" | Temu-style marketplace grid screen recordings flashed in 0.0–0.6 s cuts (87.8–89.4), sceptical nurse with insole, creator holding a cheap shoe, $1 bill, hand ripping a shoe | |
| 112.4–137 | mechanism ×3 | "relieve foot pain in 3 ways: arch support… heel cushioning… slip-resistant sole" | POV navy shoe on a rail, green-glow leg bones, 3D heel cushion, walking on wood, dog on patio | |
| 137–152 | testimonials | "Nurse Mary D… 12-hour shift no pain… Kaitlynn… felt comfort immediately" | review-page screenshot, nurse with an elderly patient, creator talking heads named on screen | |
| 152–171 | toe box + price | "wide toe box… circulation… less fatigue… cost much less than other orthotic brands" | knit close-ups, muscle-anatomy overlay with green glowing shoes (159.7), creator holding a pair | |
| 171–181 | risk reversal | "45-day money-back guarantee, 15 days longer than most brands" | POV, dog leash | |
| 181–190 | bonus stack | "three bonuses: one, up to 40% off; two, free shipping with tracking; three, free returns 45 days" | "One…" / handwritten whiteboard "UP TO 40% OFF" / "Two…" unboxing / "Three…" | |
| 190–202.3 | future pace + CTA | "imagine not thinking about your feet… cradle your feet… order right now using the link below" | creator, toes wiggling, shoes, walking legs | |
| 202.3–206.1 | end card | — | discounts card | |
**B-roll inventory:** stock (doctors, clinic team, warehouse drone, stock chart) ~14 · talking-head (founder, B&W) 5 · talking-head (creators/reaction) ~14 · problem visualisation ~10 · product handling/hero ~25 · POV walking/feet ~14 · anatomy/3D ~6 · review/marketplace screenshots ~8 · offer card (whiteboard) 1 · end card 1.
**Transitions & motion:** hard cuts. A 7-cut flash burst on marketplace screenshots (87.8–89.4 s, 0.0–0.6 s each), used as a rapid-scroll effect. The founder is always in B&W (the "documentary" register). Handwritten whiteboard offer.
**Caption system:** TikTok-native. Black Proxima Nova/Montserrat SemiBold, sentence case, on white rounded boxes, 1–2 lines, 2–6 words. Glyph line ≈ 32 px, band 78–87% from top (4:5). Consistent. Named testimonials are captioned as a speaker ID ("Nurse Mary D. said", "Kaitlynn said").
**Pacing:** ~1.8–1.9 s per shot throughout. The CTA/bonus stack accelerates to 0.5–1.3 s per shot (last 20 s average 1.32 s, fastest close in batch).
**Offer & CTA:** guarantee at 176.3 s (86%), "three bonuses" stack at 181–188 s, "link below" at 198 s.
**Steal this:**
- Enemy hook: "Cheap ___ from [Temu] are not that good". A sceptical person tosses the cheap product out of frame while the red "ARE NOT THAT GOOD" box pops on beat at 1.75 s.
- Founder in B&W with stakes ("going bankrupt because of copies"). It makes a long origin story feel like a confession, not an ad.
- Close with a counted bonus stack ("One… Two… Three…"), with the discount on a handwritten whiteboard so it reads as low-production and authentic.

### W26 — (thumbnail only) Podcast clip: "How 4 nursing students from Duke University…"
**Data:** $32,692 CAD · ROAS 2.05 · 1 ad ("Kyro 41 best shoe nurses v3 - 12h shift copy - all day comfort H - 10 Reasons Healthcare Advertorial - Copy") · Dec 2023–Mar 2024 (oldest in batch) · CTR 1.87% (lowest) · 1.85M impr · video not downloadable, so duration, cuts and VO are unknown. **Analysed from thumbnail + copy only.**
**Format / angle / persona:** faux-podcast / interview clip (origin or discovery story told by a male host/guest). The ad name says "best shoe nurses v3 … all day comfort H", so the in-video hook text may differ from the thumbnail frame. Copy: "Start working your 12 hour shift pain free — or your money back", "Join the 70,000+ Nurses", "40% off limited time". Headline "All-Day Comfort & Pain-Free 👟".
**Hook (thumbnail):**
- Visual: 4:5 (1080×1350), a man in his 50s in a light-blue shirt wearing studio headphones behind a broadcast mic, in front of a deep-red velvet curtain with sparkle particles. A "podcast studio" look, glancing off camera (listening). Product not visible.
- Text: "How **4 nursing students** / from **Duke University**". Montserrat SemiBold/Bold, sentence case. Black text with the key phrases in cyan (#1BB5D0-ish), on one white rounded box (y 1005–1187, 74–88% from top, x ≈ 120–970). Glyph line ≈ 45–48 px, pitch ≈ 88 px.
- Hook archetype(s): podcast/interview authority, specific-institution story ("Duke University"), curiosity (sentence left unfinished).
**Steal this:**
- A podcast-studio frame (headphones, mic, red curtain) borrows interview credibility and suits long story VO.
- Open with an unfinished "How [number] [persona] from [prestigious place]…" caption, with the number and the institution in an accent colour.

---

## Batch patterns
(11 videos + 2 thumbnail-only entries; counts are out of the 11 videos unless stated.)

- **Every winner is long.** 11/11 run over 90 s: median 142 s, range 94–362 s, and 3/11 over 200 s (W18 258 s, W19 362 s, W25 206 s). None is a short cut-down. The spend sits on 2–6-minute VO stories that feed an advertorial: 11/13 entries point to the "10 Reasons / 7 Reasons Healthcare Workers" page by ad name or link, W15 to a "curvy women" advertorial, and W16 has no link.
- **Two editing tempos.** The 9:16 "Kyro-style" cuts (W14, W15, W16, W17, W22, W23, W24, plus 4:5 W25) average 1.5–2.0 s per shot, about 30–40 cuts/min. The 4:5 story/testimonial cuts (W18, W19, W21) average 3.2–4.6 s per shot (13–19 cuts/min) with 8–12 s holds. Both tempos reach $40k+.
- **The hook headline is always burned in and almost always boxed.** 11/11 have a hook text on frame 1; 10/11 put it in a solid box/bar (white, red, blue or black). The exception, W14, uses a TikTok comment sticker, which is also a box. 8/11 use red (#E80000–#FF0000, or the orange-red #FC2F17) as the hook accent.
- **Two-tone setup → punch headline** (setup line in one colour or box, punch line in a contrasting red/white tier, often popping in ~1.75 s later): 6/11 (W15, W18, W19, W22, W23, W25). Punch lines are equal to or up to 1.5× larger than setup lines. Headline glyph lines run 43–75 px at 1080 width.
- **Product is usually not in the hook.** Only 2/11 show the shoe in the first 2 s (W15 with a red ✕, W21 on the walker's feet), and 3/11 within 4 s (adding W14 at 3.4 s; W25 has an anatomical overlay at 3.6 s). Story ads hold the reveal to 44–73% of runtime: W23 44%, W17/W24 ~50%, W19 56%, W16 58%, W18 59%, W22 73%.
- **Hook archetypes are all belief/story openers, never feature claims.** Authority-dismissed "my doctor said no cure" (W18, W19), contrarian "worst advice" (W16), stat shock "87% wrong shoes" (W23), nostalgia "remember when" (W22), comparison test (W17, W24), reply-to-comment discount (W14), reverse-psychology before/after (W15), persona call-out "Mujeres Curvy, atención" (W21), enemy/knockoff (W25). 0/11 open on a product feature.
- **One narrator, many faces.** 11/11 are VO-over-B-roll with no sustained lip-sync. The first-person "I" (Sarah, the nurse, the traveller) is played by 5–20 different UGC women in one ad. Muted creator reaction/holding-the-shoe clips are the most common shot type after POV feet.
- **Nurse persona dominates:** 9/11 videos plus both thumbnails' copy. The non-nurse winners still borrow a nurse: W16's traveller ("a nurse friend… 12-hour shifts") and W21's curvy warehouse worker (body-positive angle).
- **Competitors are attacked by name in 5/11** (W16 Hoka/Nike censored as "H0kas/N!kes", W17/W24 Crocs/Skechers/Nike Air Max/Hoka Bondi with blurred logos, W22 Crocs/Hoka-type, W25 Temu as "Tennu"). 8/11 show competitor or "wrong" shoes as B-roll, usually under a drawn red ✕ (W14, W15, W16, W23) or graded B&W (W16, W22).
- **Shared stock-asset kit, reused in 10/11:** the green-glowing X-ray skeleton inside the shoe, the 3D foot with orange bunion glow, leg/knee/spine skeleton overlays on real bodies, a red pain dot with lightning bolts (W14, W15, W16, W23), and the 3D layered shoe render.
- **Captions: three systems, all in the 61–87% lower-third band, 1–2 lines, 2–7 words.** (a) TikTok-native black text on white boxes, 6/11 (W16, W17, W21, W23, W24, W25; glyph ≈ 32–55 px). (b) White on translucent black boxes, 3/11 (W15, W18, W19; glyph ≈ 30–48 px). (c) ALL-CAPS heavy sans with outline, 2/11 (W14 Montserrat ExtraBold with a #0F9BF3 karaoke word highlight, W22 Poppins ExtraBold; glyph ≈ 53–56 px). Captions are sentence case in 9/11.
- **The offer lands late.** In 9/11 the first discount/guarantee mention is at 77–95% of runtime; median ≈ 87%. W23 brings a price anchor in at 62% and the "40% ending" line at 72%. W14 is the outlier: it opens with the offer (5.5 s) and restates it at 77%. The 45-day guarantee is in the VO in 8/11. "40% off" is in the VO in 7/11 (W14 stacks it to "60%"), and 4/11 (W15, W18, W19, W21) never say a discount and leave it to the end card and copy.
- **Standard close:** the shared ComfortWear end card ("TAKE ADVANTAGE OF DISCOUNTS / ON BUNDLES or 40% OFF SITEWIDE", gold 45-day seal, Free Shipping stamp, 3-colour packshot, "Doctor-Recommended" shield), 3.9–6.7 s, appears in 9/11. Seasonal reskins exist: W22 "Christmas Clearance Sale", W14 a Nurses Day code banner. 3/11 add a white "ORDER NOW" pill with a chevron under the captions in the last 6–15 s (W15, W16, W23).
- **Stutter/flash micro-cuts** (0.03–0.4 s bursts) appear exactly once per ad in 6/11 (W14 glitch, W16 cobblestones, W17/W24, W22 archival "bending/lifting", W25 Temu grid) as a mid-video attention reset at about 28–48% of runtime.
- **Spanish works as a straight port.** W17/W24 (ranking), W19 (a full VO re-record of English W18) and W21 (persona) spent $182k combined. W19 out-clicked its English twin (4.72% vs 2.88% CTR) despite running 105 s longer. The highest CTRs in the batch come from the newest contrarian/nostalgia story hooks: W22 7.91%, W16 7.01%, W17 6.45%.
