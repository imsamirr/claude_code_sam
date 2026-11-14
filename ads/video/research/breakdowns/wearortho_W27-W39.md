# WearOrtho winning video ads: frame-by-frame breakdown, W27–W39

Source: `data/wearortho_video_index.json` ranks 27–39 (each > $20k CAD lifetime Meta spend). Analysis folders are under `media/wearortho_analysis/`. Text sizes are given at 1080 px width, as `measure_text.py` normalises them (9:16 = 1080×1920; W34 and all thumbnails are 4:5 = 1080×1350). CPM = spend / impressions × 1000, in CAD. ROAS ≈ 0.0 (W29, W35) is an attribution artefact of how those ad sets were set up. It is reported, but it does not mean the creative failed.

Music/SFX check: no audio was listened to. Mean loudness in VO gaps of 0.35 s or more (ffmpeg volumedetect) is used as a proxy. −20 to −25 dB = a clear music bed. −28 to −36 dB = a faint bed or room tone. Below −45 dB = silence.

Five entries (W27, W30, W31, W36, W38) have only `thumbnail.jpg`. They are analysed from the thumbnail and ad copy only. All five are 2023–24 "Kyro NNN" edits in 4:5 that link to healthcare/nurse advertorials.

---

### W27 — "Why is it DANGEROUS to NOT wear ortho shoes as a nurse" (doctor authority), thumbnail only
**Data:** $30,566 CAD · ROAS 2.06 · 1 ad · Jan–Mar 2024 · 1.73M impr · CTR 2.92% · CPM ≈ $17.7 · duration n/a · ad name `Kyro 48_1-ss1 - 12h testim copy - voted 2023 best H - 10 Reasons Healthcare Advertorial` → editor Kyro, video 48, version 1, sound/scene 1, "12-hour testimonial" primary text, "Voted best" headline, sends to the "7 reasons… best gift for healthcare workers" advertorial.
**Format / angle / persona:** doctor/expert explainer on why nurses get hurt · nurse persona · authority + fear.
**Hook (from thumbnail only):**
- Visual: 4:5. A white header band takes the top ~18% (y 0–245). Below it, a male doctor in a white coat with a stethoscope and tie, chest-up, looking straight at the camera in front of a hospital-ward background. The background looks keyed in (green-screen / stock-doctor look). No product visible.
- Text hook: "Why is it **DANGEROUS** To **NOT** / Wear Ortho Shoes As A Nurse". Two lines, black on white, with "DANGEROUS" and "NOT" in red ALL CAPS. Font: Montserrat Bold/ExtraBold (geometric round "o", flat-topped "t"). Cap height ≈ 46–48 px, line pitch ≈ 80 px, centred at 4–13% from top. Title Case except the red words.
- Copy carries the testimonial ("Working 12–14 hour shifts 6 days a week… My loving husband bought me these…") and the gift angle. Headline: "Voted 2024's Best Nurse Shoe".
**Steal this:** a white header bar with a two-colour (black + red) Montserrat question, sitting above an expert face; a negative-frame question ("why is it dangerous NOT to…"); expert video paired with a spouse-gift testimonial in the copy.

---

### W28 — "If you bought from ComfortWear yesterday, I am sorry" (Early Black Friday 60% montage)
**Data:** $28,837 CAD · ROAS 3.57 · 1 ad · Nov 2025–Jun 2026 · 535k impr · CTR 5.03% · CPM ≈ $53.9 · 88.7 s · 50 shots · avg 1.77 s / median 1.70 s · VO 192 wpm · EN · ad name `RTGv1_K30 | Kyro_299_2_V1` (retargeting set, Kyro video 299 v2).
**Format / angle / persona:** sale-announcement VO over a UGC montage · "apology" reverse-psychology hook · women 35–65 and nurses.
**Hook (0–3 s):**
- Visual: full-frame UGC, 9:16. 0.00–1.77: a woman lies on a leather sofa with her cheek resting on the black/purple OrthoStretch like a pillow, eyes closed (product visible from frame 1). Hard cut at 1.77 to a nurse in lavender scrubs holding up a pair of black/purple shoes with both hands, waving them. Hard cut at 3.13 to a nurse in blue scrubs tossing shoes toward the camera. A persistent sale banner sits on top throughout.
- Text hook: sale banner at y 290–430 (15–22%). Line 1 is a white box (65 px tall) reading "Early Black Friday Sale **ENDS SOON!**" (black + red text, ~34 px glyphs). Line 2 is a black box (79 px) reading "🏷️ 60% OFF SITEWIDE 🎁" (white ~44 px glyphs). Font: Poppins/Montserrat Bold. Running caption: "If you bought from ComfortWear" in white Montserrat ExtraBold with a soft drop shadow. The active word sits in a blue (#1E7FC0-ish) rounded box. Line height ≈ 70 px (cap+desc 55–70), 2 lines, at 70–77% from top.
- Verbal hook: "If you bought from ComfortWear yesterday, I am sorry, because today we just launched our biggest sale ever." (0.00)
- Audio: VO plus a clear music bed (gaps ≈ −22 to −24 dB) · Hook archetypes: apology / fear of missing a better price, a sale announcement, and a pattern-interrupt image (cuddling a shoe).
- First hard cut at 1.77 s; 2 cuts and 3 distinct images in the first 3.5 s.
**Beat map:**
| t | beat | VO (short) | visuals / B-roll | on-screen text |
|---|---|---|---|---|
| 0–5.4 | hook | "If you bought… yesterday, I am sorry… biggest sale ever" | shoe-pillow, nurse waving pair, nurse tossing pair | banner + word-highlight captions |
| 5.7–13 | offer/agitate | "could have saved 60%… timing sucks" | POV walking on deck with a surfboard; woman on sofa with a red "pop" burst graphic on her face; outdoor leg-kick | — |
| 13.4–30.6 | offer + scarcity | "$150 shoes down to just $59.95… next 18 hours… last sale sold out in under 6 hours" | putting on shoe, nurse holding a pair at the face, porch walk, leaves walk, kitchen gift reveal, asphalt walk | "down to just $59.95" |
| 30.9–37 | bridge | "first pair or stocking up… quick reminder" | older women holding red pairs, nurse tying | — |
| 37.5–56.3 | mechanism vs. competitor | "aren't fancy running shoes… special foam bounces back… wide toe box… grippy sole" | blurred-logo running shoes (Hoka-style), 3D foam animation (#28), white canvas shoes "going flat", foot-skeleton X-ray overlay on shoe (#31), gloved hand pulling a bunion toe out of a narrow shoe (#32), heel-drop and sole grip on wood | captions only |
| 56.7–59.5 | proof | "over 500,000 women" | 3×3 grid of 9 UGC faces (#36) | caption |
| 59.5–74 | timeline / transformation | "relief within days… by week two… after a month…" | older women walking: sidewalk, garden path, stairs, hallway, cold room | — |
| 74.4–83.6 | urgency + CTA | "60% ends at midnight… Click below… $59.95 before sold out… Your feet deserve better" | POV pavement, sole held up at the face, blue pair on feet | blue circle with down-chevron under the caption from 77.2 s |
| 83.9–88.7 | end card | — | black→white gradient card: "EARLY / **BLACK** (red) / FRIDAY / SALE IS HERE!" + red bar "60% OFF SITEWIDE", gold "45 DAYS MONEY BACK" seal, "FREE SHIPPING FOR ALL ORDERS" badge, 3 shoes (navy/burgundy/black), red paint-splash | — |
**B-roll inventory:** lifestyle/walking (~16), product handling/showing pair to camera (~14), POV feet (~6), comparison vs. competitor (4: blurred running shoes ×2, canvas "flat" shoe, narrow-toe bunion clip), anatomy/3D (2: foam animation, X-ray foot), social-proof grid (1), offer card (1). No talking head lip-sync: it is pure VO over silent UGC.
**Transitions & motion:** 100% hard cuts. One "pop" starburst sticker (red lines, #5). Blue chevron button at the CTA. No zooms or whips.
**Caption system:** word-by-word highlight, 2-line phrase blocks of 2–5 words. White Montserrat ExtraBold, sentence case, soft shadow. Active word in a blue rounded box. Line ≈ 55–70 px at 70–77% from top. Consistent across all shots. The persistent top sale banner appears on ~26 of 49 shots (missing on runs of clips such as #5–7 and #17–23), so it is applied inconsistently.
**Pacing:** hook avg 1.8 s, body 1.63 s, last 15 s 2.9 s (end card 4.8 s). The only hold over 3 s is the end card.
**Offer & CTA:** the offer is the hook (0 s). Price anchor $150 → $59.95 at 18–25 s. Time scarcity "next 18 hours" (22 s) and "sold out in under 6 hours" (26 s) restated at 74 s ("ends at midnight tonight"). "Click below" at 77 s with the chevron. End card adds the 45-day guarantee and free shipping. Copy and headline: "EARLY BLACK FRIDAY - 60% OFF!".
**Steal this:** (1) The "If you bought yesterday, I'm sorry" hook turns a sale into news and a mild loss. (2) A two-line boxed sale banner (white "…ENDS SOON!" over black "60% OFF SITEWIDE") stays on top while the UGC rotates underneath. (3) Feature claims each get a 1–2 s proof clip (foam animation, X-ray foot, bunion-pull, sole grip), and then a 9-face grid for the "500,000 women" line.

---

### W29 — "Women over 65 hate this orthopedic shoe deal" (green-screen presenter + summer-sale montage)
**Data:** $28,214 CAD · ROAS 0.05 (attribution artefact) · 1 ad · Aug–Sep 2025 · 518k impr · CTR 4.20% · CPM ≈ $54.5 · 119.5 s · 66 shots · avg 1.81 s / median 1.60 s · VO 176 wpm · EN · ad name `Kyro_251_1_V1 sale`.
**Format / angle / persona:** "X hate this deal" reverse-psychology sale ad · presenter cut-out over B-roll for the hook, then a VO montage · women 65+ and nurses.
**Hook (0–3 s):**
- Visual: one 5.9 s opening shot. Full-frame B-roll of a hand lifting a purple OrthoStretch by its stretch laces on grass (product visible at 0.0). A keyed-out female presenter (black top, long dark hair) sits in the lower-left ~40% × 40% and talks to camera (green-screen PiP). At 0.25–0.5 s a red arrow (upper-left, pointing down-right) appears and a thick red circle draws itself around the laces/upper. Both stay through 5.9 s. The B-roll inside the circle keeps moving (hand rotates the shoe). At 3.5 s (inside the same detected shot) there is a cut to POV black shoes on wood under "BECAUSE THEY'RE BUYING EVERY".
- Text hook: "WOMEN OVER 65 / HATE" → "THIS ORTHOPEDIC / SHOE DEAL!". ALL CAPS white Montserrat ExtraBold/Black with a soft shadow. Active word in a blue (#1A8FE3-ish) box. Line height ≈ 68–70 px, 2 lines at 68–77% from top, centred on the presenter's chest.
- Verbal hook: "Women over 65 hate this orthopedic shoe deal because they're buying every single pair we have left." (0.00)
- Audio: VO with a faint bed (gaps −30 to −36 dB) · Hook archetypes: age call-out, reverse-psychology "hate", deal/scarcity.
- First hard cut at 5.9 s per detection (a visual change at ~3.4 s inside the shot); about 3 visual changes in the first 3.5 s (arrow, circle, word highlights).
**Beat map:**
| t | beat | VO (short) | visuals / B-roll | on-screen text |
|---|---|---|---|---|
| 0–6.8 | hook | "Women over 65 hate… buying every single pair" | presenter PiP + circled purple shoe | caps word-highlight |
| 7–16 | offer | "biggest summer sale… basically stealing, but totally legal for the next 18 hours… under $40 with our secret code" | nurse showing a pair to camera, grey shoe on rug, woman on porch, POV burgundy shoes, putting on shoe, orange soles up | "$40 WITH OUR SECRET" |
| 16–34 | problem → discovery | "we get why… regular shoes feel like torture devices… we figured out something crazy… feel better the longer you wear them" | nurse arms-wide in kitchen, slippers, woman rubbing her foot on the floor, mirror selfie, POV navy pair, hospital bed POV | — |
| 34.6–56.8 | mechanism vs. competitor | "special foam bounces back… mall orthopedic shoes use cheap foam… wide front part… grippy bottom" | 3D foam animation (#21, same asset as W28 #28), white canvas shoes, worn grey shoes "from the mall", Crocs, red "pain" spark graphic on a worn shoe (#26), wide-toe POV, red heels "squishing", sole flip | — |
| 56.8–80 | proof + ease + timeline | "500,000 nurses… no weird inserts, no complicated lacing… within a few days stabbing heel pain disappears… couple of weeks" | nurse sniffing an old shoe (disgust, #33), 3D shoe cut, insole held up, slip-on demo, low-angle sky walk, woman holding her foot on bed, X-ray skeleton over shoe (#41) | — |
| 80–104 | offer stack | "marked everything down 40%… secret code SAVE10… extra 10%… 50% off deepest discount… last time sold out in under six hours" | 7 nurses in quick posing shots, burgundy pair, "50%" sticker over shoe (#52), quick 0.6–0.9 s sole/product cuts (#53–56) | "50% OFF" |
| 104.7–115.6 | urgency + CTA | "sale ends at midnight… use code SAVE10… your feet will thank you" | nurse pointing at a navy pair, putting on, holding up | red "ORDER NOW" pill + down-chevron from 108.7 s |
| 115.6–119.5 | end card | — | white card: ComfortWear logo, "TAKE ADVANTAGE OF DISCOUNTS / ON BUNDLES" (black condensed + navy), 45-day seal, FREE SHIPPING badge, 3-shoe stack, blue shield "DOCTOR-RECOMMENDED" | — |
**B-roll inventory:** lifestyle (nurses at home/porch/kitchen, ~22), product handling/hero (~20), POV feet/walking (~10), comparison vs. competitor (~6: canvas, mall orthopedic, Crocs, heels, worn shoes), anatomy/3D (3), problem visualisation (2: foot rub, holding foot), green-screen presenter (1), offer card (1).
**Transitions & motion:** hard cuts only. Animated red arrow + draw-on circle in the hook. "50%" sticker. ORDER NOW pill + chevron in the last ~10 s.
**Caption system:** ALL CAPS Montserrat ExtraBold, white, active word in a blue box, 2–4 words over 2 lines, ≈ 68–70 px lines. Position moves between 40% and 89% from top to clear products (e.g. 52–54% and 86–89% measured at 30 s). Same caption template as W28 but upper-case.
**Pacing:** 5.9 s held hook (the presenter + circle carry it), then body avg 1.73 s. A tight burst of 0.6–0.9 s cuts at 97.6–100.6 s on "deepest discount of the year". Last 15 s avg 2.1 s.
**Offer & CTA:** offer at 7 s ("biggest summer sale"), price "under $40" at 16 s, code SAVE10 stack at 88 s ("extra 10%… 50% off"). Deadline "midnight tonight" at 104.7 s. ORDER NOW + "use code SAVE10" at 108.7 s. End card is bundle-led.
**Steal this:** (1) The "[Age group] hate this deal because they're buying every pair" hook (call-out + reverse psychology + scarcity in one line). (2) A green-screen talking-head PiP in the lower-left over a circled, moving product shot for the first 6 s, then drop the presenter and go full B-roll. (3) A "secret code" stack (40% + code = 50%) that adds a second reason to click late in a long ad.

---

### W30 — "My wife works…" couple gift testimonial (Kyro 27 Gift v4), thumbnail only
**Data:** $28,114 CAD · ROAS 1.82 · 1 ad · Nov 2023–Jan 2024 · 1.11M impr · CTR 2.49% · CPM ≈ $25.2 · duration n/a · ad name `Kyro 27 Gift v4 (wife works) - 73% healthcare workers copy - 2023 best H - Nurse advertorial`.
**Format / angle / persona:** couple selfie (husband speaks, wife beside him) · gift-for-your-nurse-wife angle in holiday season · healthcare-worker persona via copy ("73% of healthcare workers experience foot pain").
**Hook (from thumbnail):**
- Visual: 4:5 selfie two-shot. A man (beard, navy tee) talks to camera, smiling. A woman in a sage zip-up has her arm around his neck. Window blinds behind. No product in this frame.
- Text: TikTok-native caption "Is they have a 40% / statewide sale right now" (auto-caption error for "sitewide", shipped uncorrected). White rounded box, black Proxima Nova/TikTok Sans Semibold. Glyph line ≈ 46–48 px, box ≈ 180 px for 2 lines, at 75–88% from top. This is a mid-video caption (offer beat), not necessarily frame 0.
- Copy: "73%… ComfortWear changes that" + 5 ✅ bullets. Headline: "2023's Best Shoes For Nurses". LP: "Nurse reveals the secret… how I fixed my painful swollen feet".
**Steal this:** a male gift-giver as the speaker (gift season, a different face than the usual nurse); a TikTok white-box caption at the bottom; a "73% of healthcare workers" stat in the copy as the problem frame.

---

### W31 — "Orthotic insole with arch support" shoe-over-face demo (Kyro 63), thumbnail only
**Data:** $27,885 CAD · ROAS 2.32 · 1 ad · Feb–Apr 2024 · 1.79M impr · CTR 2.30% · CPM ≈ $15.6 (cheapest in batch) · duration n/a · ad name `Kyro 63_2-ss2 - 73% healthcare workers copy - 2023 best H - 10 Reasons Healthcare Advertorial - Copy 2`.
**Format / angle / persona:** UGC product demo / feature walkthrough · nurse persona via copy.
**Hook (from thumbnail):**
- Visual: 4:5. A black/purple OrthoStretch is held sideways across the creator's face, so the sole and midsole cover her eyes and only her nose/mouth show below the tread. Her hand points at the shoe. A playful, odd framing that keeps the product at full size.
- Text: "Orthotic insole / with arch support". Two separate white boxes per line (TikTok "per-line box" style), black Proxima Nova/TikTok Sans Semibold. Glyph ≈ 50–55 px, each box ≈ 85 px tall, at 73–86% from top.
**Steal this:** a "shoe over face" framing (product dominates, face still human); one feature per caption in TikTok per-line boxes; ran at ~$15.6 CPM, so this plain native look delivered cheaply.

---

### W32 — "Probamos los zapatos más populares entre enfermeras" (Spanish "Tested 5 shoes", Hook 2), duplicate of W17
**Data:** $27,252 CAD · ROAS 1.71 · 1 ad · Feb–Jun 2026 · 662k impr · CTR 7.13% · CPM ≈ $41.2 · 93.9 s · 62 shots · avg 1.52 s / median 1.53 s · VO 186 wpm · ES (US-Spanish) · ad name `627_Kashif_Spanish_Ortho_Stretch_Shoe_Tested5ShoesWinner Hook 2`.
**Hook-variant note:** the mp4 is **byte-identical to W17** (same md5 `d6821259…`, same 62 cuts, same transcript). W17 is the same "Hook 2" ad name ($59,057, Nov 2025–Jul 2026, ROAS 0.71). W32 is the same creative relaunched under a new video ID / ad set, not a new edit. Combined spend for this exact cut is ≈ $86.3k. W24 ("Hook 1") is the sibling body. It opens with "Analizamos cinco de los zapatos más populares… para ver cuál realmente ayuda con el dolor de pies" and has a 5.0 s first shot vs. 3.1 s here, with the body shifted ~1.6 s later. Hook 2's line ("the most expensive came second, you won't believe it") is the more curiosity-driven of the two and got more spend.
**Format / angle / persona:** ranked listicle "Top 5 shoes for nurses" with scores · comparison vs. named competitors (Crocs, Skechers GoWalk, Nike Air Max, Hoka Bondi) · nurse persona · Spanish-speaking US audience.
**Hook (0–3 s):**
- Visual: 2×2 split screen of four nurses' feet in four competitor shoes (top-left white/grey Brooks-style in a clinic, top-right pink Hoka-style POV, bottom-left grey On Cloud, bottom-right white New Balance). Each panel is a separate moving clip. A thin white divider sits at ~50% height. 0–3.1 s. Then 3.1–6.2 s: an overhead circle of ~8 pairs of nurses' feet in competitor sneakers. Our product is not shown until "Número uno" at 46.1 s.
- Text hook: "Cual crees que es el mejor / zapato para enfermeras?" (no accents or opening ¿). White Proxima Nova/TikTok Sans Semibold on a solid red-orange (#F2361E-ish) rounded box. Glyph line ≈ 44–46 px, box ≈ 199 px tall (y 861–1060, 45–55%), centred over the split seam. The text asks a question while the VO says something different (dual hook).
- Verbal hook: "Probamos los zapatos más populares entre enfermeras y el más caro quedó en segundo lugar, no lo vas a creer." (0.00)
- Audio: VO + faint bed (gap −31 dB) · Hook archetypes: question/quiz, "we tested", price-paradox curiosity.
- First hard cut at 3.1 s; four simultaneous moving panels give constant motion in the first 3 s.
**Beat map:**
| t | beat | VO (short) | visuals / B-roll | on-screen text |
|---|---|---|---|---|
| 0–6.1 | hook | "Probamos… el más caro quedó en segundo lugar" | 2×2 split → overhead feet circle | red question box |
| 6.2–19.6 | #5 Crocs 7.8 | "les damos un 7.8… no tienen soporte de arco… después de 4 horas…" | pink Crocs in hand, white Crocs on feet, beige Crocs, nurse holding pink Crocs, nurse limping | "Número cinco:", "Les damos un 7.8 de 10.", "Cuestan como $50" |
| 19.8–27.7 | #4 Skechers Go Walk 8.1 | "espuma de memoria, pero se aplana rapidísimo" | Skechers (logo blurred), memory foam cross-section, 3 micro-cuts 0.04/0.16/0.64 s on "en semanas" (stutter) | "Número cuatro:", "Un 8.1." |
| 27.7–38.9 | #3 Nike Air Max 8.2 | "120 dólares… diseñados para correr… no para estar de pie 12 horas… angostos" | Air Max in hand, on feet, runner on road, nurse walking, gloved bunion-pull clip | "Cuestan unos $120." |
| 39.1–46.0 | #2 Hoka Bondi 8.3 | "muy acolchonados pero super pesados" | black Hoka, white Bondi, nurse leaving house | "*Hoka Bondi*. 8.3." |
| 46.2–56.5 | #1 ComfortWear 9.2 | "9.2 de 10… solo 60 dólares con descuento… los más baratos pero los mejores" | stepping in red pair, older woman holding blue pair "9.2 de 10.", nurse tying, POV walking | "9.2 de 10.", "cuestan solo $60 con descuento." |
| 56.7–74.3 | mechanism | "para quienes sufren de dolor de pies… punta más ancha… soporte de arco… fascitis plantar… antideslizante… se adapta si se hinchan" | runner (contrast), woman with burgundy pair, 3D X-ray skeleton on shoe, 3D foot-bunion animation (#45), sole, swollen-foot POV | one caption per feature |
| 74.5–82.3 | risk reversal + proof | "45 días… la mayoría solo te da 30… miles de reseñas" | 6 quick nurse reaction/thumbs-up shots (0.6–1.6 s) | "Miles de reseñas lo confirman:" |
| 82.3–93.9 | CTA | "si terminas cojeando… 40% de descuento y envío gratis… si no te ayudan los devuelves" | older women walking, woman tossing hands with a "cloud" overlay, mirror leg-lift, blue POV pair | "Hoy están con 40% de descuento", "Pruébalos.", "los devuelves." |
**B-roll inventory:** comparison vs. competitor (~22 shots of Crocs, Skechers, Nike, Hoka, others), product handling/reaction with pair (~12), POV feet/walking (~10), lifestyle nurse walking (~8), anatomy/3D (3), stock running (2), texture macro (memory foam, 1). No talking head: VO-only.
**Transitions & motion:** hard cuts. A 3-frame stutter at 27.1–27.9 s. A split-screen hook. Competitor logos blurred on several shots. No end card (ends on POV feet + "los devuelves.").
**Caption system:** TikTok-native white rounded box, black Proxima/TikTok Sans Semibold, sentence-case fragments of 2–6 words, 1–2 lines. Glyph ≈ 35–45 px, box ≈ 120 px (one line). Position changes per shot (≈ 30% top or 75–78% bottom) to avoid the product. Scores and prices are always typed on screen.
**Pacing:** hook shots 3.1 s each, body 1.43 s avg, last 15 s 1.48 s. Fastest of the batch (6.6 cuts/10 s). Each rank gets ~7–13 s.
**Offer & CTA:** price is part of the ranking ($50, $120, "$60 con descuento"). The 45-day vs. "most give 30" line is at 74.5 s. 40% + free shipping at 88 s. No end card. LP is a Spanish "10 razones…" healthcare advertorial.
**Steal this:** (1) A dual hook: the on-screen quiz question plus a different spoken curiosity claim ("the most expensive came second"). (2) Give competitors respectable scores (7.8–8.3) so the 9.2 looks fair, and make the winner also the cheapest. (3) A 2×2 split of four real nurses' feet in recognisable competitor shoes for the first 3 s.

---

### W33 — "$180 Hokas, $200 Danskos, $150 Brooks… don't waste your money" (nurse "3 lessons", Hook 03)
**Data:** $26,772 CAD · ROAS 1.48 · 1 ad · Jul–Nov 2026 (active) · 428k impr · CTR 5.10% · CPM ≈ $62.5 · 143.7 s · 40 shots · avg 3.59 s / median 2.97 s · VO 192 wpm · EN · ad name `TOFv1_HF2 | 807_Aubrey_New UGC_Ortho_Stretch_Shoe_Don't Waste Spent Money_9X16 HOOK 03` (creator Aubrey, hook variant 3).
**Format / angle / persona:** creator talking head, "what I learned so you don't waste your money" · 3 numbered lessons, then discovery story · comparison vs. expensive named brands (Hoka, Dansko, Brooks) · ER nurse persona.
**Hook (0–3 s):**
- Visual: full-frame selfie talking head. A nurse in royal-blue scrubs, short auburn hair, at home (kitchen cabinets, yellow bottle), arm's-length framing with her head at 25–55%. She wags her index finger "no" from frame 0 and counts on her fingers. No product until 15.5 s.
- Text hook: top title "‼️These expensive shoes are / bad Nursing Shoes‼️". TikTok white box, black Proxima/TikTok Sans Semibold, red ‼️ emoji both ends. Glyph ≈ 28–38 px, box ≈ 140 px (y 356–496, 19–26%). It persists through the 8.7 s first shot. A price stack builds on the right, right-aligned, in white bold sans with a black shadow and no box. Each line ≈ 43 px at 43–53%: "$180 H0kas" (0.25 s) → "$200 Dansk0s" (1.75 s) → "$150 Br0oks" (3.5 s) → a rule line + yellow "$530 TOTAL" (~4.6 s). Brand names are masked with zeros.
- Verbal hook: "$180 for Hokas, $200 for Danskos, $150 for Brooks… all sitting in my closet, literally garbage after just two months." (0.00)
- Audio: VO is on-camera sync. Faint bed (gaps −28 / −21 dB) · Hook archetypes: money-wasted receipt, named-competitor callout, expert peer (nurse).
- First hard cut at 8.67 s; ~4 visual changes in the first 4.6 s come from text builds, not cuts.
**Beat map:**
| t | beat | VO (short) | visuals / B-roll | on-screen text |
|---|---|---|---|---|
| 0–8.5 | hook | price stack → "garbage after two months" | talking head, finger wag | title + price stack + "$530 TOTAL" |
| 8.5–20.5 | promise | "finally found the pair that survives the 12-hour shift… here's what I've learned" | TH, holds shoe (unbranded) at 15.5 s, shows sole | running captions start ~4.7 s |
| 20.5–33 | Lesson 1 | "running shoes are the wrong type… forward motion… we're standing on concrete 12 hours" | TH; leg-kick demo against wall; walking to car | white-box "LESSON #1 / Running shoes are not for / nursing" (3 lines ≈ 213 px block, 42–53%) |
| 33.8–50 | Lesson 2 | "arch support needs to last hours… foam collapses… reinforced" | TH; shoe with yellow arrows at arch (#11); POV and street walks with green ✓ stickers (#13–14) | "LESSON #2 / You need an anatomical arch support" |
| 50–75 | Lesson 3 + agitate | "toe box needs to be wide… feet swell… bunions worse… nerve pain… ready to give up my career" | TH; shoe with yellow ↔ arrows over toe box (#18); jump on the spot | "LESSON #3 / You need a wide toe box" |
| 75.3–91 | discovery + checklist | "came across ComfortWear… met every single standard" | laptop screen of the ComfortWear product page (#23); unboxing bag with logo + ComfortWear wordmark sticker (#24); green ✓ on shoe | 4-row ✅ checklist building top-left (one row per claim, white boxes ≈ 25–40% from top) |
| 91.4–117 | results timeline | "first shift… by hour 8… by week 2 back pain… stopped ibuprofen… 7 months… picked up an extra shift" | long TH holds of 5.6–7.5 s, door shot | captions only |
| 117–138.2 | CTA | "if you have wasted money… half a million healthcare workers… 40% off… 45-day money back" | TH with shoe, laptop scroll of the review page (#38), shoe held to camera | captions |
| 138.6–143.7 | end card overlay | — | shoe stepping on wood | yellow "GET YOURS NOW!" (Montserrat Black), spaced "45-DAY MONEY BACK GUARANTEE", green browser-bar box "comfortorthowear.com" + cursor |
**B-roll inventory:** creator talking head (~22 of 40 shots, ~65% of runtime), product handling (5), POV feet/walking (5), lifestyle (car, door, wall-kick; 4), review/website screenshot filmed on a laptop (2), unboxing (1), offer overlay (1).
**Transitions & motion:** hard cuts and a few jump cuts within the TH. Graphics: yellow arrows, green check stickers, a progressive ✅ checklist, "$530 TOTAL" tally line.
**Caption system:** running captions in white Montserrat SemiBold with a dark outline/shadow, no box, sentence case, 2–4 words on 1 line, ≈ 35–45 px at 59–61% from top (chest). A separate "chapter title" system (white TikTok box, black text, "LESSON #N" + rule) sits above the captions at 42–53%. The checklist reuses the transcription typo "Slipper-resistant for vet hospital floors" (= slip-resistant, wet floors). It shipped and still spent $26.8k.
**Pacing:** first shot 8.7 s, second 6.8 s. Body avg 3.2 s. Results section holds 5.6–7.5 s. Slowest of the English ads except W37. 2.8 cuts/10 s. Retention comes from the numbered lessons and the text builds.
**Offer & CTA:** offer only at 128.7 s (90% through): "40% off… 45-day money-back… link's below". The end overlay has a URL in a fake browser bar.
**Steal this:** (1) A "receipt" hook: typed prices of named competitors stacking up to a yellow TOTAL, with brand names masked (H0kas, Dansk0s, Br0oks). (2) Three "LESSON #N" white-box chapter cards turn a 2.4-minute talking head into a skimmable listicle. (3) A ✅ checklist that builds one row per claim when the product is revealed, mapping back to the lessons.

---

### W34 — "Not enough grip? 🤔" (fall fail-clip hook + arthritis testimonial VO), 4:5
**Data:** $26,678 CAD · ROAS 2.03 · 1 ad · Oct 2024–Jan 2025 · 706k impr · CTR 3.76% · CPM ≈ $37.8 · 72.2 s · 39 shots · avg 1.85 s / median 1.63 s · VO 212 wpm · EN · **4:5, 360×450 source** · ad name `@NF - kyro 162v1ss2 - tesitmonial copy - 10 Reasons Healthcare Workers`.
**Format / angle / persona:** testimonial VO (first person, arthritis) over a UGC montage · grip/slip-safety angle · active older woman, with nurses in the B-roll.
**Hook (0–3 s):**
- Visual: 0.00–1.20: viral fail clip, a woman in black slipping and sliding down a carpeted staircase (full fall by 0.75 s). Hard cut at 1.20 to a woman sitting on a rug pulling on the black/green OrthoStretch (product at 1.25 s). Hard cut at 2.57 to the same woman dancing/kicking in the living room.
- Text hook: "Not enough grip? 🤔". TikTok white rounded box, black Proxima/TikTok Sans Semibold. Glyph ≈ 55–60 px, box ≈ 130 px, ~81% of width, centred at 45–55% from top of the 4:5 frame.
- Verbal hook: "Not enough grip?" (0.00), then "From the minute I put them on, I knew I had found my new favorite walking shoe." (≈1.3)
- Audio: no music (first gap −56 dB, others −28 to −43 dB = room tone) · Hook archetypes: fail/shock clip, problem question, then an instant testimonial.
- First hard cut at 1.20 s; 3 shots in the first 3 s.
**Beat map:**
| t | beat | VO (short) | visuals / B-roll | on-screen text |
|---|---|---|---|---|
| 0–1.2 | hook | "Not enough grip?" | stair fall | "Not enough grip? 🤔" |
| 1.2–5 | answer | "From the minute I put them on… new favorite walking shoe" | putting on, dancing, shoe on foot by bricks | white-box captions |
| 5.3–8.5 | problem | "I have arthritis… certain shoes uncomfortable" | nurse rubbing her foot, hand pressing a shoe | — |
| 8.5–23.5 | product + mechanism | "not the case with this sneaker… OrthoStretch by ComfortWear… support incredible… grip… even slippery ones" | flex shoe, sidewalk walk, grass, sole close-up, POV on a wet patio, nurse walking | "by ComfortWear are built differently!" |
| 23.5–47 | benefit + 2nd pair | "soft cushion and stretchy material adapt… bought a second pair… changed how I feel about life" | thumb into knit, grocery-store walk, nurse holding pair, unboxing bag with logo (#20, 4.4 s), silver pair | — |
| 47–61 | recommendation + offer | "highly recommend… 40% off from this link… 45-day money-back" | woman pointing at shoe, sole, stairs step-up, insole branding | — |
| 61.6–68.4 | CTA | "no questions asked… go to comfortorthowear.com" | burgundy feet POV, dog, beach with dog | red "ORDER NOW" pill + chevron from 64.3 s; "Go to comfortorthowear.com and get yours!" |
| 68.4–72.2 | end card | — | "TAKE ADVANTAGE OF DISCOUNTS ON BUNDLES" (same card as W29) | — |
**B-roll inventory:** POV/feet walking (~12), product handling/demo (~10), lifestyle (grocery, dog, stairs; ~8), stock fail clip (1), unboxing (1), problem (1), offer card (1). No on-camera speaker: VO only.
**Transitions & motion:** hard cuts only. ORDER NOW pill + down-chevron in the last ~8 s.
**Caption system:** TikTok-native white rounded box, black Proxima/TikTok Sans Medium (double-storey "a", single-storey "g"), sentence case, 3–7 words over 1–2 lines. Glyph ≈ 50–55 px, 2-line box ≈ 195 px, at 68–83% from top. One phrase per shot; consistent throughout.
**Pacing:** hook shots 1.2–1.8 s, body 2.0 s avg. Holds of 3.5–4.4 s on the sole close-up and unboxing. Last 15 s 1.55 s (quick burst to the CTA).
**Offer & CTA:** offer at 51.3 s (71%): "40% off if you purchase directly from this link" + 45-day guarantee + "no questions asked" + URL read out. The post's primary text includes the product URL (no separate link_url).
**Steal this:** (1) Open on a 1.2 s viral "fail" clip (a fall on stairs) captioned with the problem question ("Not enough grip? 🤔") before anything about the product. (2) Read a real-sounding first-person review as VO over many different women's clips, so it plays like a collective testimonial. (3) Read the URL aloud plus "no questions asked" right before the ORDER NOW sticker.

---

### W35 — "Why did nurses in the 1960s rarely complain about foot pain?" (archival-history angle)
**Data:** $24,516 CAD · ROAS 0.07 (attribution artefact) · 1 ad · Oct–Dec 2025 · 695k impr · **CTR 8.42% (highest in batch)** · CPM ≈ $35.3 · 110.3 s · 59 shots · avg 1.87 s / median 1.57 s · VO 193 wpm · EN · ad name `TOFv3_A19 | Kyro_296_2_V3 updated`.
**Format / angle / persona:** "lost wisdom / it used to be better" history explainer · B&W archival footage → modern problem → product as the revival of old principles · nurse persona.
**Hook (0–3 s):**
- Visual: full-frame black-and-white 1960s newsreel of 4–6 nurses in white caps and dresses walking arm-in-arm toward the camera on a London-style street. 0–1.75: tighter shot. 1.75 (soft cut inside the archival clip): wider line of nurses at a railing. Hard cut at 2.87 to a close-up of smiling nurses' faces. No product until 58.9 s.
- Text hook: "HAVE YOU EVER WONDERED WHY / NURSES IN THE 1960S RARELY / **COMPLAINED ABOUT FOOT PAIN?**". ALL CAPS Poppins ExtraBold/Black (geometric, round "O"), lines 1–2 white, line 3 yellow (#FFF200-ish), thin dark shadow. Set on a full-width solid red (#E8100F-ish) bar y 1284–1584 (300 px, 67–82%). Cap height ≈ 42–43 px per line, pitch ≈ 85 px. Shown for 0–4.8 s (2 shots).
- Verbal hook: "Have you ever wondered why nurses in the 1960s rarely complained about foot pain?" (0.00)
- Audio: VO + low music bed (gaps −27 to −31 dB) · Hook archetypes: curiosity question, nostalgia/history, contrarian "it was better before".
- First hard cut at 2.87 s; 3 distinct images in the first 3 s.
**Beat map:**
| t | beat | VO (short) | visuals / B-roll | on-screen text |
|---|---|---|---|---|
| 0–4.4 | hook | "Have you ever wondered why…" | B&W nurses marching | red bar headline |
| 4.8–18 | evidence + contrast | "look at old hospital photos… simple white shoes… no fancy athletic technology, no memory foam, no gel inserts… weren't limping home like nurses do today… what changed?" | B&W ward, corridor with timecode burn-in "01:12:37:06" (adds authenticity), modern Nike/Saucony-type shoe, foam squeeze, gel insert press, B&W hospital, modern nurse limping, nurse screaming holding her foot | captions with yellow keyword |
| 18.5–31.3 | old principles | "built by companies that understood… firm arch support… wide toe boxes… sturdy construction that lasted years" | old leather nurse shoes, B&W man walking, 3D X-ray foot with orange bunion (#15), red-glow toe overlay, white leather nurse shoe | — |
| 31.7–54 | modern villain | "today's running shoes… designed for people who run for an hour, not stand for 12… cushioning compresses by your third shift… narrow designs squeeze" | blurred-logo running shoes, nurse groaning, runner on road, operating room, foam squeeze, bunion glove-pull (shared clip), swollen legs on bed, nurse face-palm, back pain | — |
| 54.5–62.3 | product origin | "we studied vintage nurse shoes… brought principles back with modern materials… That's how ComfortWear OrthoStretch was created" | white sneakers on black (#34–35), burgundy pair overhead, first ComfortWear at 58.9 s (blue pair), black/purple pair, nurse holding pair | — |
| 62.7–76 | features | "wide toe box… firm arch… cushioning… slip-resistant… breathable" | hand on toe box, woman spinning in garden, finger on arch, nurse arms-wide, 3D insole layers (#44), sole, walking, nurse hugging shoe, older woman twirl | — |
| 76.2–93.4 | proof + testimonial | "over 500,000 healthcare workers… Believe me… after the first week my foot pain… back pain decreased" | 3×3 UGC face grid (#49, shared asset), 3 creator talking-heads with 6.6–6.8 s holds (#51–52) | — |
| 93.7–104.9 | offer + CTA | "fall sale, 40% off… if they don't… return them… Click below… USA's most comfortable shoes" | woman with shoe, 2 lifestyle clips with an orange "40% OFF" sticker (Poppins Black, white outline), kitchen gift, step close-up, woman at front door | blue down-chevron from 99.8 s |
| 105.2–110.3 | end card | — | "EARLY BLACK FRIDAY SALE IS HERE! 60% OFF SITEWIDE" (same card as W28). **Contradicts the VO's "40% off fall sale"** | — |
**B-roll inventory:** archival/stock B&W (~9), comparison vs. competitor/modern sneakers (~8), problem visualisation (pain, limping, swelling, back; ~8), anatomy/3D (3), product handling/hero (~10), lifestyle (~8), creator talking-head testimonial (4), social-proof grid (1), offer card (1).
**Transitions & motion:** hard cuts only. Burned-in archival timecode left visible. Red glow overlays on pain points. "40% OFF" stickers. Chevron at CTA.
**Caption system:** white Montserrat SemiBold, soft shadow, no box, sentence case, 2–5 words over 1–2 lines. One keyword per caption in pale yellow (#FFF59D-ish), not boxed. Line ≈ 50 px at 70–77% from top. Unlike the bold Kyro captions in W28/W29, these are lighter and smaller.
**Pacing:** archival hook shots 2.9 / 1.9 / 2.1 s. Body is a steady 1.4–1.8 s. The two longest holds (6.6, 6.8 s) are talking-head testimonials at 80–93 s. Last 15 s avg 2.2 s.
**Offer & CTA:** offer at 93.7 s (85%): "fall sale, 40% off" + return promise. The end card says 60% Black Friday (inconsistent). Headline: "Orthopedic Shoes | 40% OFF". LP: healthcare-worker advertorial.
**Steal this:** (1) The archival "it used to be better" hook: B&W period footage + a red full-width caps bar with a yellow payoff line; nostalgia skews old and stops the scroll. (2) Brand origin as a revival ("we studied what made those vintage nurse shoes work, then brought them back"), which reframes a cheap shoe as heritage. (3) Leave archival texture (timecode burn-in, grain) visible as proof it's real.

---

### W36 — "With thousands of positive reviews" nurse UGC (Kyro 125), thumbnail only
**Data:** $23,845 CAD · ROAS 2.37 · 1 ad · Jul–Sep 2024 · 1.17M impr · CTR 3.72% · CPM ≈ $20.4 · duration n/a · ad name `@NF - Kyro 125v1ss1 - 73% copy - 10 Reasons Healthcare Workers`.
**Format / angle / persona:** nurse-creator UGC review · healthcare worker (royal-blue scrubs) · social proof.
**Hook (from thumbnail):**
- Visual: 4:5. A Black nurse creator in royal-blue scrubs and a long blonde wig, seated, smiling down at a black/purple OrthoStretch pair she holds at chest height. Soft indoor light, dark panelled wall.
- Text: "with thousands of / positive reviews". TikTok white rounded box, black TikTok Sans/Proxima **Regular** (lighter than W30/W31). Glyph ≈ 60–65 px, box ≈ 190 px, at 68–83% from top. A mid-video caption, not the hook.
- Copy: "73% of healthcare workers…" + ✅ list. Headline: "2024's Favorite Nurse Shoes". LP: the 10 Reasons advertorial (with Triple Whale UTM).
**Steal this:** a nurse in scrubs cradling the pair with a "smell/admire" reaction; a social-proof line as a native white-box caption; the same 73% copy reused across W30, W31 and W36 (a long-running copy winner).

---

### W37 — "Podiatrist rates safest shoes for seniors" (near-static expert ranking)
**Data:** $22,371 CAD · ROAS 1.50 · 1 ad · May–Jun 2026 · 514k impr · CTR 5.75% · CPM ≈ $43.5 · 88.7 s · 18 detected shots (≈ 20 real, see below) · avg 4.93 s / median 2.57 s · VO 173 wpm · EN · ad name `TOFv5_AR20 | Senior | 929_Kashif_New UGC_Ortho_Stretch_Shoe_PodiatristRateShoes_@Samir Patel_SeniorAngle`.
**Format / angle / persona:** expert-rates-products listicle · comparison vs. 6 named competitors · podiatrist authority · seniors (headline "2026's Best Shoes For Seniors").
**Hook (0–3 s):**
- Visual: 0.00–2.55: green-screen composite. A smiling podiatrist (curly hair, beard, royal-blue scrubs) is keyed into the lower-right ~50% and raises his index finger ("number one" / "listen"). The background is a heavily blurred close-up of a burgundy ComfortWear pair on a granite counter (the product is there from 0.0 but unreadable, a teaser). At ~2.55 a zoom-blur transition (punch-in with motion blur, missed by scene detection) leads into a full-frame seated interview: the same doctor in a clinic chair, beige wall, chest-up, centred. At 2.75 a cut-out photo of a black Skechers GoWalk pops onto his chest.
- Text hook: "Podiatrist Rates Safest / Shoes For Seniors". TikTok white rounded box, black Proxima/TikTok Sans Semibold, Title Case. Glyph ≈ 55–60 px, box ≈ 198 px (y 380–578, 20–30%). Only on 0–2.55 s.
- Verbal hook: none for 2.5 s. The first word is at 2.51 s: "Skechers GoWalk? Two out of ten." The first 2.5 s run silent (mean −36 dB, room tone/very soft bed), so text + face + finger carry the hook.
- Audio: on-camera speech, no clear music (gaps −28 to −40 dB) · Hook archetypes: expert authority, rating/ranking, persona call-out ("seniors"), "safest" safety frame.
- First real transition at 2.55 s (a zoom-blur); the next hard cut is a jump cut at 39.1 s. Two visual changes in the first 3 s.
**Beat map:**
| t | beat | VO (short) | visuals | on-screen text |
|---|---|---|---|---|
| 0–2.5 | hook (silent) | — | keyed doctor over blurred CW shoe | title box |
| 2.5–9.6 | #1 Skechers GoWalk 2/10 | "no arch support… heel is going to hurt within a week" | static doctor + black shoe cut-out on chest | "Skech\*rs GoWalk", "2/10", phrase captions |
| 9.9–17.1 | Hoka Bondi 3/10 | "cushioning so high it shifts your balance… knees" | grey shoe cut-out | "H0ka Bond", "3/10" |
| 17.4–24.3 | New Balance 3/10 | "too heavy… wears your hips and knees out" | grey NB cut-out | "NewBal\*nce", "3/10" |
| 24.6–31.5 | Brooks 4/10 | "arch compresses… plantar fasciitis does not get better" | teal shoe cut-out | "4/10" |
| 31.5–39 | Vionic 4/10 | "toe box too narrow… bunions or arthritis" | grey shoe cut-out | "Vion\*c", "4/10" |
| 39.1–46.5 | Orthofeet 3/10 | "two hundred dollars… arch still in the wrong position" | jump cut, black shoe cut-out | "Orth0feet", "3/10", "Two hundred dollars" |
| 46.6–56.3 | ComfortWear 10/10 | "ComfortWear OrthoStretch? Ten out of ten. Why ten out of ten? …feet that have changed with age" | burgundy CW cut-out (46.6–49.5), then clean doctor frame | "ComfortWear Ortho Stretch", "10/10", "Why ten out of ten?" |
| 56.3–75 | features (B-roll starts) | "firm arch support, not foam… wide toe box… balance… bunions or arthritis… lightweight… slip resistant… breathes" | tying shoe with green-glow sole (#3), product on bed, older woman walking a sidewalk, green ↔ arrows on toe box POV (#6), older woman rubbing her knee with red pain glow (#7), shoe on scale (lightweight, #8), heel-step slip demo ×3, older woman walking in garden | phrase captions |
| 75.2–85.2 | proof + offer | "over 500,000 women… under sixty dollars… forty percent off… only shoe on this list with a 45-day money-back guarantee… link is below" | Trustpilot-style review cards (#13), stepping into blue pair, older women holding pairs (55–70 look), gold "45 DAY" seal sticker | "Over 500,000 women have already switched", "Under $60", "40% off right now" |
| 85.5–88.7 | end card | — | white card with grey bubbles: ComfortWear logo, "TAKE ADVANTAGE OF DISCOUNTS" + navy bar "40% OFF SITEWIDE", 45-day seal, free-shipping bubble, navy shoe, "DOCTOR-RECOMMENDED" shield | — |
**B-roll inventory:** talking-head (pro/podiatrist) ≈ 56 s (63% of runtime) with 7 product cut-out swaps; product demo (sole glow, scale, toe-box arrows, slip step; 6); lifestyle senior walking (3); problem visualisation (knee pain glow; 1); review screenshot (1); product handling by older women (3); offer card (1).
**Transitions & motion:** one zoom-blur at 2.55 s, one jump cut at 39.1 s, then hard cuts in the B-roll section. Graphics: product PNG cut-outs on the doctor's chest (≈ 45% frame width, centred at ~55–60% height), green-glow and red-glow overlays, green arrows, gold seal.
**Caption system:** small TikTok-native plain captions, white TikTok Sans/Proxima Medium with a soft shadow, no box, 2–5 words, 1 line, ≈ 38–45 px at 71–74% from top (just under the shoe cut-out). Scores ("2/10", "3/10", "10/10") get their own caption beat. Competitor names are masked (\*, 0).
**Pacing:** 0–56 s is effectively one static camera set-up (avg 7 s per product segment). Then the B-roll section averages 2.25 s per shot (56–85 s). The only "speed-up" is after the verdict.
**Why a near-static ad works here:** (a) **Audience:** senior women decide on trust and comprehension, not stimulation. A credentialed face looking at the camera for 56 s reads as a consultation, not an ad. Slow VO (173 wpm, short sentences, pauses) is easy to follow. (b) **The list does the editing:** each competitor segment is a mini open loop (name → score → reason). The scores stay low (2, 3, 3, 4, 4, 3), so viewers keep watching to learn what earns a high score. The swap of the shoe cut-out every ~7 s provides the visual change a cut would. (c) **Self-identification:** the named shoes (Skechers GoWalk, Orthofeet, Vionic, New Balance) are what this demo already owns or considers, so "your shoe gets 2/10" is personal. (d) **Reveal and pay-off:** the product gets 10/10 at 46.6 s, the static set-up ends, and fast proof B-roll (older women, slip demo, scale) arrives exactly when the viewer wants evidence. (e) **Silent text-only open:** the first 2.5 s are a title box, a smiling doctor and a raised finger, which suits sound-off feeds. The high CTR (5.75%) shows that slow editing did not cost attention.
**Offer & CTA:** offer at 78 s (88%): "Under $60, 40% off, only shoe with a 45-day money-back guarantee". "Link is below" at 84.6 s. The "only shoe on this list" framing ties the guarantee back to the ranking.
**Steal this:** (1) A podiatrist seated in one locked-off shot, with product PNG cut-outs swapped on his chest and a bare "N/10" caption per product (cheap to make, very clear). (2) Mask competitor names in text (Skech\*rs, H0ka, Orth0feet) but say them in full. (3) Close the ranking by making the guarantee "the only one on this list", which turns the risk reversal into one more comparison win.

---

### W38 — "They also let your feet move naturally" sole demo (Kyro 45, 12h-shift copy), thumbnail only
**Data:** $21,648 CAD · ROAS 2.26 · 1 ad · Jan–Mar 2024 · 1.04M impr · CTR 1.94% (lowest) · CPM ≈ $20.9 · duration n/a · ad name `Kyro 45_2-ss3 - 12h shift copy - all day comfort H - 10 Reasons Healthcare Advertorial - Copy`.
**Format / angle / persona:** UGC product-demo walkthrough (hands only) · nurse 12-hour-shift copy ("Start working your 12 hour shift pain free — or your money back… 70,000+ nurses… 40% off").
**Hook (from thumbnail):**
- Visual: 4:5 close-up of two hands holding the OrthoStretch outsole up to the lens, with a fingertip on the arch-flex zone. Black lugs, tan rubber pods. Patterned rug background. No face.
- Text: "They also let your / feet move naturally". White rounded box, black Montserrat Bold (geometric round "o", wide letterforms). Glyph ≈ 60 px, box ≈ 180 px (y ~1008–1187, 75–88%). A mid-video feature caption.
- Headline: "All-Day Comfort & Pain-Free 👟".
**Steal this:** a sole-to-lens macro with a finger pointing at the flex point as a feature beat; copy that leads with a money-back promise plus a nurse head-count (70,000+), which later grows to 500,000 in the 2025–26 ads.

---

### W39 — "Nobody wants to tell teachers this!!" (teacher-persona shoe test, 2:52)
**Data:** $20,828 CAD · ROAS 1.66 · 1 ad · Aug–Sep 2026 · 350k impr · CTR 7.97% · CPM ≈ $59.5 · 172.4 s (longest) · 87 shots · avg 1.98 s / median 1.87 s · VO 234 wpm (fastest; no gaps ≥ 0.35 s, likely sped-up AI/VO) · EN · ad name `TOFV1_HJ27 | JULYWK2_VID1_JACK_Teacher_Hook1` (July week 2, video 1, editor Jack, teacher persona, hook 1).
**Format / angle / persona:** "we tested the shoes teachers wear" editorial comparison (Brooks, Hoka, Dansko, Vionic → ComfortWear) · standing-not-walking insight · teacher persona (back-to-school timing).
**Hook (0–3 s):**
- Visual: 0.00–2.33: static wide shot of a teacher (denim jacket, black skirt) standing still at a rolling standing desk in a real classroom (bean bags, whiteboard, posters). This is the "standing in one spot" insight shown before it is said. Hard cut at 2.33 to a woman in a red cardigan in a home office who reaches for an office chair (the urge to sit). No product until the mystery silhouette at 112.9 s and the reveal at 116.2 s (67% through).
- Text hook: "Nobody wants to / tell teachers this!!". White rounded box (large radius), black TikTok Sans/Proxima Bold. Glyph ≈ 61–62 px, box ≈ 296 px (y 314–610, 16–32%), ~76% width. Persists 0–5.1 s across 2 shots.
- Verbal hook: "Here's what no one wants to tell teachers. Your feet aren't wrecked from walking, they're wrecked from standing." (0.00)
- Audio: wall-to-wall VO (no gaps ≥ 0.35 s), tail −57 dB = no music bed · Hook archetypes: secret/withheld truth, persona call-out, reframe insight.
- First hard cut at 2.33 s; 2 shots in the first 3 s.
**Beat map:**
| t | beat | VO (short) | visuals / B-roll | on-screen text |
|---|---|---|---|---|
| 0–12.5 | hook + insight | "no one wants to tell teachers… wrecked from standing… 6 hours a day on concrete and linoleum… we put the shoes teachers wear to the test" | classroom standing, chair, teacher at whiteboard, linoleum floor, teacher with a pile of shoes (test set-up), teacher pinning paper | keyword boxes "6 hours", "on concrete and linoleum" |
| 12.8–27.6 | agitate the day | "you're planted… at the whiteboard, over a student's shoulder, on duty in the hallway… hardest floors" | whiteboard writing, leaning over a student, hall duty with STOP sign, bare foot standing, shoe on hard floor, closet of sneakers | one keyword box per shot |
| 27.8–51 | #1 running shoes (Brooks) | "talked into at the running store… engineered to move a runner forward… narrow tapered toe box… worn a hole where the bunion sits" | shoe-store wall, "the Br0Oks", thumbs-down creator with worn pair, running treadmill aisle, 3D foot with red pressure points + arrows (#24), worn-out pair with a hole (#27) | masked brand |
| 51.4–70.5 | #2 max cushion (Hoka) | "feel amazing through first period… taller and softer the stack, the less steady… plush foam packs down" | Hoka on feet ×3 (0.8–1.1 s), unboxing, crouching at a desk, 3D X-ray leg in shoe with red heel glow (#38–39), flattened foam | "like H0ka" |
| 70.6–87 | #3 clogs (Dansko) | "rigid footbed rock hard… heaviest… too aware of the shoe" | unboxing tan clogs, crouch, leopard clogs ("Dansk0 wearing teachers") | masked brand |
| 87–112.7 | #4 Vionic | "credit where it's due, real arch support… but rigid molded footbed… feet swell… by dismissal pressing" | closet, "orthopedic brand", insole flex, sneaker try-on, counting cash ("you paid a premium") | — |
| 112.9–116 | reveal tease | "the one we thought was the best all around" | black shoe silhouette with a red "?" floating in an empty school hallway (#64, 3.3 s) | — |
| 116.2–148.5 | ComfortWear mechanism | "OrthoStretch from ComfortWear… built for people who stand on hard floors… like nurses and teachers… firm but flexible… grips a wet hallway… knit stretches as feet swell… polished enough for parent-teacher night" | navy CW pair, shelf, gym treadmill, sole, knit stretch (5.0 s), nurse with clipboard, woman holding burgundy pair to camera ×2 | — |
| 148.6–164 | transformation | "after a couple of weeks… getting to the last bell with something left… actual energy" | unboxing branded bag, grey pair, closet kick, teacher dancing in front of a US flag, hallway, feet up on sofa | — |
| 164.3–172.4 | CTA | "Your feet are going to carry you to that last bell either way… how much of you is left… Tap below" | teacher at chalkboard, burgundy pair, nurse walking in garage | "tap below!" (no end card) |
**B-roll inventory:** lifestyle teacher/classroom (~20), comparison vs. competitor product (~30: Brooks, Hoka, Dansko, Vionic, generic sneakers), product handling/unboxing (~12), anatomy/3D (4: pressure-point foot, X-ray leg ×2, silhouette reveal), problem visualisation (~4: bare foot standing, worn hole, crouch), POV feet (~6), reaction/thumbs-down (1). No talking head with lip-sync: VO-only.
**Transitions & motion:** 100% hard cuts. Graphics: red arrows and pressure dots on the 3D foot, a "?" silhouette reveal. No stickers or offer card.
**Caption system:** keyword-only TikTok-native boxes. A white rounded box with black TikTok Sans/Proxima Semibold holds 1–4 words, not the full transcript ("6 hours", "the Br0Oks", "tap below!"). Glyph ≈ 44 px, 1-line box ≈ 95 px, 2-line ≈ 133 px, at 69–76% from top. With 234 wpm VO, showing fragments avoids a caption wall.
**Pacing:** hook 2.3 / 2.8 s, body steady 1.9 s (77 shots), last 15 s 2.9 s. Each competitor segment runs 16–25 s. The product appears only at 2/3 of the runtime, yet CTR was 7.97%: the test structure holds attention.
**Offer & CTA:** no price or discount in the VO at all. The CTA is an emotional close ("how much of you is left") + "Tap below" at 169.5 s. The offer (up to 40% off) lives only in the copy. LP: a teacher-specific advertorial ("teaching job means standing all day…").
**Steal this:** (1) A persona-specific insight hook ("your feet aren't wrecked from walking, they're wrecked from standing"), shown first as a static standing shot. (2) Credit-where-due competitor critiques ("genuinely well made for running… that's the problem") make the test feel fair. (3) A mystery silhouette with "?" in the persona's environment (school hallway) right before the product reveal.

---

## Batch patterns

- **Two production eras with different economics.** The 2023–24 Kyro edits (W27, W30, W31, W36, W38: 4:5, single-feature UGC with white-box captions, CTR 1.9–2.9%) bought cheap reach (CPM $15.6–25.2, 1.0–1.8M impressions each). The 2025–26 9:16 edits (W28, W29, W32–W35, W37, W39) run CTR 3.8–8.4% at CPM $35–63. Every ad live in 2026 has CTR ≥ 5.0%.
- **Length went up, not down.** The 8 videos run 72–172 s (mean ≈ 111 s); 7 of 8 are ≥ 88 s (only W34 is shorter, at 72 s). The longest (W39, 2:52) has a CTR of 7.97% with the product revealed at 67%.
- **Cut rate clusters at ~1.5–2.0 s.** 6 of 8 have median shot length 1.53–1.87 s (5.0–6.6 cuts/10 s). Only the two expert/creator formats are slow: W33 (median 2.97 s) and W37 (5 s+ talking-head holds). The Spanish listicle (W32) is the fastest at 1.52 s avg.
- **VO over silent UGC is the default.** 6 of 8 videos have no on-camera lip-sync for the body (W28, W29, W32, W34, W35, W39). They are VO at 176–234 wpm over a library of creator clips. Only W33 (nurse creator) and W37 (podiatrist) are true talking heads.
- **Hook archetypes:** curiosity/secret question 4 of 8 (W32 quiz, W35 1960s, W39 "nobody wants to tell", W34 "not enough grip?"). Comparison/ranking of named competitors 4 of 8 (W32, W33, W37, W39). Sale/reverse psychology 2 of 8 (W28 "I'm sorry", W29 "women over 65 hate"). Persona call-out in the first text or VO line 6 of 8 (nurses ×3, seniors/65+ ×2, teachers ×1).
- **Text hook = a box at the top or middle; the VO says something else or more.** 7 of 8 put a boxed headline in frame 1: TikTok white box ×4 (W33, W34, W37, W39), red box ×1 (W32), full-width red caps bar ×1 (W35), sale banner ×1 (W28). Box heights run ≈ 130–300 px with glyph lines ≈ 45–62 px. They sit at 16–30% from top (W33, W37, W39, W28) or 45–82% (W32, W34, W35).
- **Two caption families dominate.** (a) The Kyro sale template: white Montserrat ExtraBold, the active word in a blue box, 2 lines, ≈ 55–70 px (W28, W29). (b) TikTok-native white rounded box, black Proxima/TikTok Sans, ≈ 35–60 px glyph (W32, W34, W39, plus all 5 thumbnails). W33, W35 and W37 use unboxed white captions with a shadow at ≈ 38–50 px. Every video is fully captioned, and all captions sit at 59–83% from top.
- **Competitor brands are named in VO but masked on screen** in 4 of 4 comparison ads: "H0kas/Dansk0s/Br0oks" (W33), "Skech\*rs/H0ka/NewBal\*nce/Vion\*c/Orth0feet" (W37), "Br0Oks/H0ka/Dansk0" (W39), with logos blurred on B-roll (W28, W32, W35).
- **A shared B-roll library is reused across editors and years:** the 3D foam-bounce animation (W28 #28 = W29 #21), the X-ray skeleton-on-shoe overlay (W28, W29, W32), the gloved hand pulling a bunion toe out of a narrow shoe (W28, W32, W35), the 3×3 nine-face "500,000 women" grid (W28, W35), the 3D foot with an orange bunion (W32, W35), and the same nurses holding pairs to camera. New ads mostly come from a new script plus a new hook clip over the existing library.
- **Late offer except in sale ads.** Sale-led W28 and W29 put the discount in the first 7 s. The other 6 hold the offer to 71–98% of runtime (W34 71%, W35 85%, W37 88%, W33 90%, W32 94%, W39 copy-only). The recurring offer stack is 40% off + 45-day money-back + free shipping, often framed "under $60" / "$59.95".
- **CTA furniture:** a red "ORDER NOW" pill and/or a blue down-chevron circle appears 8–12 s before the end in 4 of 8 (W28, W29, W34, W35). End cards come from 3 shared templates: Black Friday 60% (W28, W35; W35's contradicts its own 40% VO), bundles (W29, W34), and 40% sitewide (W37). W32, W33 and W39 have no end card.
- **Core claim set** (at least 4 of these 5 in every script): wide toe box, firm/real arch support that doesn't collapse, slip-resistant grip, cushioning built for standing (not running), and swelling-friendly stretch knit. Plus "500,000 women/nurses/healthcare workers" social proof (5 of 8: W28, W29, W33, W35, W37) and a relief timeline ("within days… by week two… after a month") (5 of 8).
- **"Built for standing, not running" is the core mechanism.** 5 of 8 explicitly position running/athletic shoes (Brooks, Hoka, Nike) as the wrong tool (W28, W32, W33, W35, W39). W29 and W37 attack "mall orthopedic" and max-cushion shoes instead. This anchors the comparison against the expensive premium brands the audience already trusts.
- **Polish is not the variable.** Ads shipped with ASR typos ("statewide sale" in W30, "Slipper-resistant for vet hospital floors" in W33), end cards that contradict the VO (W35), and inconsistent banners (W28), and each still spent $20k+. The concept and hook carry the result.
- **Hook variants of one body scale.** W32 is a byte-identical re-launch of W17 ("Tested 5 Shoes" Spanish, Hook 2), ≈ $86k combined. Names like "HOOK 03" (W33) and "Hook1" (W39) show the standard practice: one body, 2–3 hooks, scale the winner and relaunch it in new ad sets.
