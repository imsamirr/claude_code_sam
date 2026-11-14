# WearOrtho (ComfortWear / OrthoStretch) winning video ads, W01–W13

Source: `data/wearortho_video_index.json` plus `media/wearortho_analysis/<key>_<id>/` (cuts.json, hook_sheet, every shots_sheet, transcript). I extracted full-res frames with ffmpeg and measured text with `measure_text.py`. All px values are **normalised to 1080 px width**: 9:16 ads become 1080×1920 and 4:5 ads become 1080×1350. "Line ≈ N px" is the glyph band of one text line, cap height plus descenders. Spend is lifetime CAD as given in the index. ROAS near 0 (W04, W06, W09) comes from how those ad sets were attributed (TOF/duplicate set-ups) and is reported as is. It does not mean the creative failed. W01/W02 ROAS (0.8/0.95) also reflect a TOF+RTG split.

Audio note: none of the transcripts has gaps of silence. The 100 ms RMS floor between words sits at −30 to −44 dB in every video, so each one most likely carries a low music bed under a single continuous VO. I can't identify the track, and there are no obvious SFX hits.

Recurring brand assets referenced below:
- **End card v1**: a white background builds in over ~4–6 s. It shows the ComfortWear logo, "TAKE ADVANTAGE OF DISCOUNTS" in a condensed black face (Bebas/Oswald-like), "ON BUNDLES" in navy Montserrat ExtraBold, a gold "45 DAYS MONEY BACK GUARANTEE" seal, a "FREE SHIPPING FOR ALL ORDERS" badge, a 3-shoe stack (navy/burgundy/black) and a blue "DOCTOR-RECOMMENDED" shield.
- **End card v2** (W08, W12, the newest): the same text on a pale-blue background with floating white spheres, one large burgundy shoe and a bigger seal and shield.
- **"ORDER NOW" pill**: white rounded pill with red bold caps "ORDER NOW", plus a small white circle with a down-chevron underneath that bobs. It sits just under the caption during the CTA section.

---

### W01 — "Top 5 shoes for nurses" scored ranking vs. named competitors
**Data:** WearOrtho: $799,877 CAD, ROAS 0.80 (TOF+RTG), 2 ads (`Kyro_293_1_V1`), Oct 2025–Jul 2026, CTR 5.03 %, 15.7 M impr · 111.9 s · 70 shots · avg 1.60 s / median 1.53 s · VO 224 wpm · EN · 9:16 (720×1280)
**Format / angle / persona:** ranked listicle "We looked at five popular shoes nurses wear", with scores out of 10, prices and named competitors (Crocs Classic 7.8 → Skechers Go Walk 8.1 → Nike Air Max 8.2 → Hoka Bondi 8.3 → ComfortWear OrthoStretch 9.2). The winner is also the cheapest ($60). Nurse persona, third-person "tester/reviewer" voice. Lands on the "7 reasons … best gift for healthcare workers" advertorial.
**Hook (0–3 s):**
- Visual: **3-panel horizontal stack** (each ≈ 1/3 height) of competitor sneakers with logos blurred.
  - Top panel: black knit runner on blue mat, being laced. There is an internal cut to a hands-lacing close-up at 1.5 s.
  - Middle panel: chunky white platform sneaker stepping on grey tile, continuous.
  - Bottom panel (below the bar): white sneaker with logo blurred. Internal re-frames at ~0.75 s and ~1.25 s.
  - At 3.03 s the layout becomes 2-panel: a nurse in navy scrubs and a floral scrub cap doing an excited shimmy (top), and a pink Croc being handled (bottom). This runs to 5.4 s, then the ad goes full-frame.
  - ComfortWear is **not visible** until 48.8 s.
- Text hook: "TOP 5 SHOES **FOR NURSES**". Montserrat ExtraBold, all caps. "TOP 5 SHOES" is black. "FOR NURSES" is red (#E00) with a thin black outline. Full-width white bar y=1280–1420 (140 px, 67–74 % from top), sitting between panels 2 and 3. Cap line ≈ 45–54 px. On screen 0–5.4 s.
- Verbal hook: "We looked at five popular shoes that nurses wear during shifts to see which one actually helps with foot pain. And what we found was pretty surprising." (0.00–10.2 s)
- Audio: VO + low bed · Hook archetype(s): numbered ranking / "we tested" + curiosity gap ("pretty surprising") + identity call-out (nurses)
- First hard cut at 3.03 s (layout change). ~4 visual changes in the first 3 s if you count the panel-internal cuts.
**Beat map:**
| t | beat | VO (short) | visuals / B-roll | on-screen text |
|---|---|---|---|---|
| 0–5.4 | hook | "We looked at five popular shoes… pretty surprising" | 3-panel → 2-panel competitor shoes, excited nurse | bar "TOP 5 SHOES FOR NURSES" |
| 5.4–18.3 | #5 Crocs | "7.8/10… $50… no arch support… hurt after 4 hours" | hands with pink/white Crocs, POV feet in Crocs, gym floor, creator holding pink Crocs, nurse walking | white-box card "Number 5: / Crocs Classic Clogs / scores 7.8 out of 10" (TikTok Classic box, black text, 44–58 % from top) |
| 18.3–28.3 | #4 Skechers | "8.1… $65 memory foam… gets flat in weeks" | navy Skechers walking ×4, foam-layers macro | card "Number 4…8.1" |
| 28.3–36.7 | #3 Nike | "8.2… $120… made for running… too narrow, swell" | Air Max close-ups, jogger, nurse in hallway, gloved hand pinching narrow toe box | card "Number 3…8.2" |
| 36.7–49.6 | #2 Hoka | "8.3, $165… heavy and bulky" | Hoka lacing, white Hoka on porch, nurse leaving house | card "Number 2…8.3" |
| 49.6–59 | reveal #1 | "ComfortWear OrthoStretch 9.2… $60 with the discount… cheapest… beat everything" | creator in pink top holding navy pair, nurse on couch, POV lacing/walking | card "Number 1: ComfortWear Ortho Stretch scores **9.2** out of 10" (9.2 in green) |
| 59–81.4 | mechanism | "made for people with foot pain… widest toe box… real arch support… grips… stretches… last longer" | runner on road ("while other companies…"), creators holding shoe, toe-spread x-ray overlay on sole, 3D insole with red/orange plantar highlight, sole grip on wood, knit stretch | captions |
| 81.4–94.8 | risk-reversal + proof | "45 days… most brands 30… thousands of reviews… cheapest beats 3× price" | 5 UGC creators holding shoes, ~1 s each | captions |
| 94.8–105.7 | offer/CTA | "40% off with free shipping… 45 days… send them back. Tap to get yours." | excited creators, woman on couch | orange "40% OFF" italic sticker (≈48 px, 16–18 %), captions |
| 105.8–111.9 | end card v1 | — | animated end card | "TAKE ADVANTAGE OF DISCOUNTS ON BUNDLES" |
**B-roll inventory:** comparison vs. competitor product ≈ 26 (shots 1–31) · talking-head/creator holding product (no lip-sync, VO over) ≈ 14 · POV walking/feet ≈ 9 · product handling/demo ≈ 8 · lifestyle (nurse leaving house, runner, walking) ≈ 7 · anatomy/3D (x-ray toes, insole render) 2 · problem visualisation (toes squished, swollen feet) 3 · end card 1
**Transitions & motion:** 100 % hard cuts. The split-screen is used only for the first 5.4 s. Graphics: scorecards, an orange "40% OFF" sticker, a pen pointing at the sole, and blurred competitor logos throughout. No zooms or whips.
**Caption system:** phrase captions, 2 lines, 2–5 words. White **TikTok Sans/Proxima Bold**, sentence case, with a ~3 px black outline and no box. Line ≈ 38 px x-height band (≈ 51 px with descenders), ~90 px line pitch. Centred at 67–75 % from top. Scorecards switch to the TikTok "Classic" white rounded box with black text (line ≈ 48–51 px, 3 lines).
**Pacing:** the hook holds 3.0 s, then 2.3 s. The body runs steady at 1.2–1.8 s. The "Number N" scorecard shots hold 1.4–2.0 s. The end card holds 6.1 s.
**Offer & CTA:** the price anchor arrives early (at 54 s: "$60 with the discount", against $50–$165 competitors). The hard offer lands at 94.8 s (85 %): 40 % off + free shipping + 45-day try, then "Tap to get yours".
**Steal this:**
- A scored, priced countdown of named competitors where the hero is #1 **and** cheapest. The "9.2" is coloured green on the reveal card.
- Open on a 3-panel stack of competitor shoes under a single red/black title bar. That sells "comparison" in one frame before any VO.
- Delay the product to ~45 % of runtime. The countdown structure keeps viewers watching to the reveal.

### W02 — "We tested 5 travel shoes" (travel-persona twin of W01)
**Data:** WearOrtho: $617,035 CAD, ROAS 0.95 (TOF+RTG), 2 ads (`Kyro_293_3_V2`), Oct 2025–Nov 2026 (still running), CTR 5.28 %, 8.2 M impr · 119.5 s · 81 shots · avg 1.47 s / median 1.37 s · VO 223 wpm · EN · 9:16
**Format / angle / persona:** myth-bust question plus a "we tested 5" category comparison (Nike sneakers → Hoka → Skechers memory foam → sandals → ComfortWear). Unlike W01 there are no scores. European-trip traveller persona.
**Same project as W01 (Kyro 293, v1 vs v3):** same template (test N shoes → each fails for a stated reason → ComfortWear reveal → identical "40 % off / free shipping / 45 days / send them back" close), same outlined-caption style, same end card, and shared creator clips. The woman on the brown couch in pink shorts is W01 #66 and W02 #4. The scrubs creator holding the black/mint shoe is W01 #57 and W02 #57.
**The hooks differ in every dimension:**
- W01: 3-panel product stack, red/black bar at 67 %, "Top 5 shoes for nurses".
- W02: one full-frame night city-street shot (Madrid, Gran Vía-style, illuminated façade, crowd) with a 4-line boxed question.
- The nurse version spent ~30 % more ($800k vs $617k).
**Hook (0–3 s):**
- Visual: handheld night street, tilting down from a lit building to the crowd (0–2.6 s). At 2.6 s it hard-cuts to a futuristic white/pink-sole racing shoe on a foot (logo blurred), then at 4.0 s to a silver shoe in hand. Product not visible until 71.9 s.
- Text hook: "THINK SNEAKERS ARE THE MOST COMFORTABLE SHOES FOR TRAVEL?" (black) / "WE TESTED FIVE OF THE MOST POPULAR ONES TO FIND OUT" (red with black outline). Montserrat ExtraBold caps, 4 lines, line ≈ 38–49 px. White box with a **two-tone border: blue on the upper half, red on the lower half**. Box y≈1195–1560 (63–81 % from top), on screen 0–5.2 s.
- Verbal hook: "Think sneakers are the most comfortable shoes for travel?" (0.00 s), then "We tested five of the most popular ones to find out." (2.62 s)
- Audio: VO + bed · Hook archetype(s): myth-bust question + "we tested" + destination aspiration ("dream trip to Europe")
- First hard cut at 2.6 s. 1 visual change in the first 3 s.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–8.1 | hook | "Think sneakers… we tested five… if you're planning that dream trip to Europe" | night street → racing shoe → silver shoe → couch creator → Park Güell | boxed headline until 5.2 s |
| 8.4–15.6 | frame | "not just walking… different surfaces… tested what travelers actually wear" | Versailles cobbles, selfie creator, alley, cobble POV, suitcase full of sneakers | captions |
| 15.9–29.7 | Nike | "designed for gym floors… every tester complained" | black-clad walker, white Keds, gym mirror, sole macro, tester rubbing shins on stairs | "First up, regular sneakers like Nike" (white-box label) |
| 29.8–44.6 | Hoka | "too cushioning… less stable… heavy in suitcase" | chunky sneakers, Colosseum, suitcase up escalator, uphill steps | label box |
| 44.9–57.4 | Skechers | "memory foam compresses… least support by afternoon" | Skechers in hand, foam squeezed, Versailles crowd | label box |
| 57.6–69.3 | sandals | "great for the beach, terrible for everything else… touristy" | suitcase with sandals, beach feet, slides with socks | label box |
| 69.7–93.5 | reveal + mechanism | "Finally… ComfortWear… sole firm enough for cobblestones, flexible… breathes… nice enough for restaurants" | burgundy shoe with "ComfortWear" label tag, sole bend, nurse sniffing shoe, red-circle "X" over a sweaty sock, women walking | captions |
| 93.8–101 | proof | "everyone said the same thing… walk further, longer" | 7 UGC creators ~1 s each, one red-circle X | captions |
| 101.4–113.2 | offer/CTA | "40% off with free shipping… 45 days… perfect timing… send them back… you'll pack them for every trip" | kitchen creator, stairs creator with orange "40% OFF" sticker, Sagrada Família | captions |
| 113.4–119.5 | end card v1 | — | — | — |
**B-roll inventory:** travel/landmark lifestyle ≈ 18 · comparison vs. competitor shoe ≈ 18 · POV walking/feet ≈ 14 · talking-head/creator with product ≈ 14 · product handling/demo ≈ 8 · problem visualisation (rubbing legs, red X) ≈ 4 · end card 1
**Transitions & motion:** all hard cuts at the fastest rate in the batch (median 1.37 s). Translucent red circle + white X overlays at 86.2 s and 97.5 s, an orange "40% OFF" sticker at 103.4 s, and blurred competitor logos.
**Caption system:** identical to W01. White bold sans with black outline, no box, 2 lines, 2–5 words. Line ≈ 51 px, centred at 67–75 %. Competitor names get a small white-box label (TikTok Classic) placed higher, at 50–60 %.
**Pacing:** hook 2.6 s, body 0.9–2.4 s, end card 6.1 s. There are no long holds. The VO is fast (223 wpm), so every phrase gets its own shot.
**Offer & CTA:** at 101.4 s (85 %): 40 % off + free shipping + 45-day try, framed as "perfect timing if you're planning a trip".
**Steal this:**
- Reuse a winning comparison template across personas (nurse → traveller): same cut rhythm, same close, swapped hook and competitor list.
- Use the blue-top/red-bottom bordered box to separate the question (black) from the promise (red).
- Use a night, crowded European street as the hook plate. It reads as "travel" in a few frames with no product needed.

### W03 — "3 things I stopped doing after leaving nursing" (ex-nurse listicle, travel turn)
**Data:** WearOrtho: $286,049 CAD, ROAS 1.80, 2 ads (`Kyro 154v2ss2`, testimonial copy, "10 Reasons Healthcare Workers" LP), Sep 2024–Jan 2026, CTR 6.36 % · 172.8 s · 75 shots · avg 2.30 s / median 1.97 s · VO 164 wpm (slowest in batch) · EN · 4:5 (720×900)
**Format / angle / persona:** numbered "3 things I stopped doing" first-person listicle: (1) running shoes, (2) painkillers, (3) $400 Amazon "orthopedic" shoes. Then an authority mechanism ("orthopedic company ComfortWear with leading orthopedists and chiropractors"), social proof, BOGO/40 % offer. Ex-nurse (15 years) who now travels.
**Hook (0–3 s):**
- Visual: one held top-down clip, 0–3.7 s, of a gloved clinician running a **steel IASTM scraping tool along a bare sole**. Clinical, ASMR, "what is that?". The product is not visible until 41.6 s.
- Text hook: "3 THINGS I STOPPED DOING" (white) appears at 0 s. The second line "AFTER LEAVING NURSING" (red with dark outline) **reveals at 2.25 s**. Montserrat ExtraBold caps, no box, dark drop shadow, line ≈ 49 px, at 29–37 % from top (upper-middle, over the image).
- Verbal hook: "Three things I stopped doing after leaving nursing. Number one, I stopped wearing running shoes" (0.00 s)
- Audio: VO + bed · Hook archetype(s): numbered listicle + identity (ex-nurse) + oddly satisfying medical visual
- First hard cut at 3.67 s. 0 cuts in the first 3 s; 1 text reveal.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–3.7 | hook | "Three things I stopped doing after leaving nursing" | IASTM scraping on sole | headline, 2-step reveal |
| 3.7–41.3 | #1 running shoes + agitate | "stopped wearing running shoes… 15 years on my feet… 20,000 steps… cobblestones… exhausted… secret weapon" | woman tossing sneakers into a bin with a big **orange outlined "1"** popped over it, Barcelona alley, selfie, plane window, nurses in OR, beach POV, cobbles, woman holding back, nurse asleep | captions |
| 41.6–52.9 | reveal | "same orthopedic shoes I used to wear at the hospital… life completely changed" | POV black/mint OrthoStretch on wood floor, airport lounge creator, feet up on suitcase | captions |
| 49.4–61.4 | #2 painkillers | "don't take pills, creams, massages" | orange "2" over pills into trash bag, **B&W** pills, cream, massage | captions |
| 60.9–77.3 | #3 $400 shoes | "stopped trusting $400 orthopedic shoes from Amazon… same materials" | orange "3" over an Amazon results grid, torn-up worn shoes, gel insole | captions |
| 77.3–96 | authority mechanism | "So what's the solution? The orthopedic company ComfortWear with leading orthopedists and chiropractors…" | patient on crutches, **stock businessman in glass office with "Comfort Wear" logo**, stock doctor team, spinning 3D shoe on psychedelic orange/blue background, pen on shoe, sole macro, 3D translucent cushion render | captions; one inverted black-box caption "full-load distribution" |
| 96–126 | features | "12 hours vs 2… big toe box… circulation… wash… breathable… non-slip" | woman with dog, creator with green ✓ over new shoe, x-ray hand/foot with green toe-box glow, stretching woman with **glowing green leg x-ray**, washing machine, knit macros | captions |
| 126.7–151 | social proof | "more than 10,000 positive reviews… knit is flexible… game changer… obsessed" | **9-up grid of UGC creators**, nurses at work, creator testimonial held 12.8 s | captions |
| 151.3–167.2 | offer/CTA | "40% off… or buy one get one 50% off… USA's most comfortable shoes" | burgundy shoe macro, handwritten "UP TO 40% OFF" whiteboard, website on laptop, walking shots | **"ORDER NOW" pill + bobbing chevron** under every caption from 151 s |
| 168.9–172.8 | end card v1 | — | — | — |
**B-roll inventory:** lifestyle/travel ≈ 12 · talking-head/creator with product ≈ 10 · product handling/demo/macro ≈ 16 · problem visualisation (B&W pills, pain, crutches) ≈ 9 · anatomy/3D/medical animation ≈ 6 · stock footage (businessman, doctors, OR) ≈ 6 · testimonial grid 1 · website/offer ≈ 3 · ASMR (scrape) 1
**Transitions & motion:** hard cuts. Large orange numerals with black outline scale-pop in at each list item (3.7 / 49.4 / 60.9 s). B&W grade marks the "old life" (pills). Green ✓ and glow overlays. A 3D shoe spins on a psychedelic background.
**Caption system:** TikTok Classic: **black regular-weight TikTok Sans on white rounded box**, sentence case, 1–2 lines, 2–6 words. Line ≈ 45 px, 2-line box ≈ 190 px tall, at 68–83 % from top. Very consistent.
**Pacing:** slow for this batch. The hook holds 3.7 s and the body runs 1–3 s, with several 3–5 s holds (12.3 s cobblestones 3.9 s, 37 s 4.6 s). The 12.8 s testimonial hold at 133.6 s is the longest shot in W01–W12.
**Offer & CTA:** 151 s (87 %): 40 % off sitewide **or BOGO 50 %**, "use this link". The ORDER NOW pill only appears in the CTA section.
**Steal this:**
- "3 things I stopped doing after ___": a negative-list format whose items are the objections (running shoes, pills, expensive orthopedics).
- Open on a clinical/ASMR foot-treatment clip with no product. Reveal the second headline line at ~2.25 s to re-hook.
- Turn on a persistent "ORDER NOW" pill only in the last 15 % of the ad.

### W04 — "3 things I stopped doing after I turned 72" (age re-skin of W03)
**Data:** WearOrtho: $250,518 CAD, ROAS 0.09 (attribution artefact, set up under @TSSS), 3 ads (`Kyro_258_2_V3`, emoji copy, "all day H", Miracle advertorial "women over 52"), Aug 2025–Jan 2026, CTR 6.79 % · 140.8 s · 83 shots · avg 1.70 s / median 1.53 s · VO 176 wpm · EN · 9:16
**Format / angle / persona:** **the same script as W03** ("Three things I stopped doing… Number one, I stopped wearing running shoes… secret weapon… Number two… painkillers… Number three… $400 orthopedic shoes from Amazon… So what's the solution?"). The persona is re-skinned to a 72-year-old retired nurse (35 years) "for women over 65". The mechanism is rewritten for aging feet: bunions, hammer toes, arthritis, heel spurs, fall-prevention grip, afternoon swelling. The authority/orthopedists block is dropped.
**Same body as W03, different hook (explicit comparison):**
- W03 hook: IASTM sole-scraping ASMR, Montserrat white/red free text with no box at 29 %, "after leaving nursing" revealed at 2.25 s.
- W04 hook: an older woman in a plaid shirt **walking away from camera on a cracked sidewalk at sunset** (one 4.4 s take). A **white box with condensed font** (Oswald/League Gothic-style) reads "3 THINGS I STOPPED / DOING AFTER I TURNED 72" (black line, then red line with black outline) at 62–75 %. Both lines show at once.
- Shared B-roll: the woman in snake-print trousers at the kitchen bin (W03 #2 = W04 #17), the thumbs-up airplane selfie (W03 #4 = W04 #5), the airplane window/engine, the pills-into-trash-bag shot, and the Amazon grid with the orange "3". New in W04: older-women UGC, skeleton/x-ray overlays, red pain glows, red X stamps.
- W04 has the higher CTR (6.79 % vs 6.36 %) and a 9:16 frame. W03 spent more over a longer life.
**Hook (0–3 s):**
- Visual: full-frame continuous back-view walk, slightly hesitant gait, no cut until 4.37 s. Product not visible until 36.5 s.
- Text hook: "3 THINGS I STOPPED / **DOING AFTER I TURNED 72**". Condensed grotesque caps (Oswald Bold-like: narrow, tall, flat terminals). Line 1 black; line 2 red (#D00) with a black outline. White rounded box y=1197–1432 (235 px, 62–75 %). Each line ≈ 69 px.
- Verbal hook: "Three things I stopped doing after I turned 72." (0.00–3.94 s)
- Audio: VO + bed · Hook archetype(s): numbered listicle + age call-out (70+) + relatable struggle visual
- First hard cut at 4.37 s. 0 visual changes in the first 3 s.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–4.4 | hook | "Three things… after I turned 72" | woman walking on sidewalk | boxed headline |
| 4.4–33.7 | #1 running shoes + agitate | "35 years as a nurse… 20,000 steps… feet, legs, back ache… secret weapon" | sneaker in bin with a **red X + orange "1"**, Paris street, selfie, plane engine, nurse from behind, red glow on foot, **step-counter watch graphic "20,177"**, x-ray knees and spine overlaid on real people | captions |
| 34–50.3 | reveal | "ortho shoes designed specifically for women over 65… lightweight… life has completely changed" | laptop product page, POV blue shoes, **3 × 0.4–0.5 s shots of 65+ women** "for women over 65!", split-screen "Not those running shoes" | captions |
| 50.7–62 | #2 painkillers | "I don't take pills, creams, massages" | orange "2" + red X over pills, red X over limping, red X over creams/massage | captions |
| 62.3–77.6 | #3 $400 Amazon | "paying for the brand… insoles won't help" | Amazon grid with red X + "3", worn shoes, creator with insole, foam foot model | captions |
| 77.9–118.7 | mechanism for aging feet | "aging feet… cushioning doesn't flatten… wide toe box… bunions/hammer toes… arthritis, heel spurs… grip… lightweight… breathes" | 3D sole render, x-ray toes in shoe, bunion on clipboard, stilettos, thumb on arch, green-glow skeleton foot, shoe stepping on steel floor ×3, red X over swollen feet, green-leg stretch | captions |
| 113.7–122.6 | proof | "50,000 women like us… just look at all the reviews" | women walking (London, Buckingham Palace), **Trustpilot-style review card on crumpled-paper background** | captions |
| 123–134.7 | offer/CTA | "40% off during their summer sale… click the link, discount applied automatically… don't let your feet stop you" | three 0.8 s shoe shots "ComfortWear is giving 40% OFF", creators | ORDER NOW pill + chevron from 129.4 s |
| 134.8–140.8 | end card v1 | — | — | — |
**B-roll inventory:** talking-head/creator with product (older women) ≈ 16 · problem visualisation (red glow, red X, swelling) ≈ 14 · anatomy overlays on real people (skeleton spine/knees, green leg, x-ray foot) ≈ 8 · product handling/demo ≈ 16 · lifestyle/travel ≈ 12 · review/UGC screenshot 1 · website 1 · step-counter graphic 1
**Transitions & motion:** hard cuts. **Red translucent X stamps** over every "stopped doing" item (6+). Orange numerals. Red radial pain glows. Skeleton overlays composited onto live footage. A split-screen at 39.2 s. Machine-gun 0.4–0.5 s triplets at 37.7 s, 100.1 s and 114.8 s.
**Caption system:** TikTok Classic, **semibold black on white box**, 1–2 lines. Line ≈ 47 px, 2-line box ≈ 160 px, at 67–78 % from top.
**Pacing:** 4.4 s hook hold, body 0.4–2.5 s, a 5.5 s hold on the Amazon grid (#3 item), 6 s end card.
**Offer & CTA:** 123 s (87 %): "40 % OFF during their Summer Sale", auto-applied discount.
**Steal this:**
- Re-skin a proven script by swapping only the identity number in the hook ("after leaving nursing" → "after I turned 72"), then rewrite the mechanism around that persona's ailments.
- Stamp a red translucent X on every old habit shown. It is a cheap, consistent "stop doing this" visual language.
- Put skeleton/x-ray overlays on real UGC people to make the pain anatomical without stock medical footage.

### W05 — "Why I'll never wear running shoes on my trips to Europe again" (nurse-in-Barcelona story)
**Data:** WearOrtho: $241,706 CAD, ROAS 1.87, 1 ad (`Kyro 99v3ss1`, testimonial copy, "10 Reasons Healthcare Workers"), May 2024–Jun 2025, CTR 5.90 % · 114.5 s · 52 shots · avg 2.20 s / median 1.80 s · VO 201 wpm · EN · 4:5
**Format / angle / persona:** first-person story testimonial. A nurse on vacation in Barcelona swapped running shoes for "orthopedic shoes", walked 50,000 steps in 2 days with no pain. Then it runs **the same mechanism module as W03, word for word** (orthopedists + chiropractors, "thoughtful orthopedic design, excellent foot support, full load distribution, very affordable price", "12 hours vs 2 hours", "big toe box is the most popular feature…", wash/breathable/non-slip, "lots of fantastic reviews from women like nurses"). W05 (Kyro 99) predates W03 (Kyro 154), so W03 inherited this module.
**Hook (0–3 s):**
- Visual: top-down shot of **running shoes being dropped into a white bin** (0–1.8 s). Hard cut to a sunny Barcelona Gothic-Quarter street with tourists (1.8–3.1 s). Then a nurse in a patient room with an "I'm a nurse" caption. Product not visible until 20.1 s.
- Text hook: "WHY I'LL NEVER WEAR / RUNNING SHOES" in white Montserrat Bold caps with a soft drop shadow on a **full-width red banner** (0–198 px, 0–15 % from top; line ≈ 52 px). Directly under it, a white strip with "ON MY TRIPS TO EUROPE AGAIN" in black Montserrat Bold caps (smaller, ≈ 30 px). The title-bar crops the top of the 4:5 frame and stays until 5.8 s.
- Verbal hook: "Why I'll never wear running shoes on my trips to Europe again." (0.00–3.00 s)
- Audio: VO + bed · Hook archetype(s): contrarian "never again" + destructive action (shoes in trash) + destination
- First hard cut at 1.8 s. 2 visual changes in the first ~3.2 s.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–5.8 | hook | "Why I'll never wear running shoes… I'm a nurse" | shoes into bin, Barcelona street, nurse | red banner + white strip |
| 5.8–26.5 | story setup | "escape to Barcelona… explore… walk many km… brought those same shoes… one day I swapped" | Barcelona square, nurse, Montserrat funicular and cliffs, hospital corridor, black/mint shoe on orange chair | captions |
| 26.5–47.96 | transformation | "life changed… shifts not so hard… felt 20 again… 50,000 steps in two days… advise everyone" | creator kicking leg, nurse showing sole, Barcelona trees, dancing woman, airport lounge | captions |
| 47.96–89.7 | mechanism module (= W03) | "orthopedic company ComfortWear… orthopedists and chiropractors… 12 hours vs 2… big toe box… circulation… wash… breathable… non-slip" | doctor holding foot (stock), x-ray, 3D shoe, skeleton-foot overlay, 3D cushion render, worn running shoes, bin, lacing grey sneaker, glowing green-leg stretch, washing machine, nurses holding shoes | captions |
| 89.7 | **white flash (0.1 s)** | — | — | — |
| 89.8–98.6 | testimonial talking heads | "Now I can easily… able to be on my feet for hours… No heel pain" | 3 lip-synced selfie testimonials (5.3 / 3.5 / 1.5 s) | captions |
| 98.6–110.3 | offer/CTA | "limited time 40% off… purchase directly from this link… Get yours now!" | feet on suitcase, nurse pointing at shoe, creator with shoe | ORDER NOW pill + chevron from 103.3 s |
| 110.6–114.5 | end card v1 | — | — | — |
**B-roll inventory:** travel/lifestyle (Barcelona, Montserrat, airport) ≈ 12 · talking-head/creator (incl. 3 real testimonial clips) ≈ 12 · product handling/demo ≈ 13 · anatomy/3D ≈ 5 · stock (doctor, nurses, hospital) ≈ 5 · problem (shoes in bin) 2
**Transitions & motion:** hard cuts. One white flash frame into the testimonial block (89.7 s). Glow overlays. A motion-blurred whip in a couple of zero-length shots (7.9 s, 26.6 s, 42.3 s, 53.0 s: zero-length "shots" in cuts.json are blur/flash frames).
**Caption system:** TikTok Classic, **bold** black TikTok Sans on white box, 1–2 lines. Line ≈ 49 px, 2-line box ≈ 205 px, at 72–87 % from top.
**Pacing:** 1.8 s first shot, body 1–4 s, with longer holds on travel scenery (32.3 s Barcelona 7.5 s, 82.1 s non-slip demo 5.6 s, 89.7 s testimonial 5.3 s).
**Offer & CTA:** 98.6 s (86 %): limited-time 40 % off + link.
**Steal this:**
- A two-tier title bar (red banner + white sub-strip) that eats the top 20 % of a 4:5 frame. It works as a newspaper headline.
- "Never again" plus a destructive action shot (dumping the competitor category into a bin) as the opening image.
- Build a reusable "mechanism module" (a ~40 s block of VO + B-roll) and bolt it onto different story openers (W05 → W03 → W11).

### W06 — thumbnail only: "ComfortWear might just change…" product-hero, "More Than" shoe
**Data:** WearOrtho: $161,076 CAD, ROAS 0.06 (attribution artefact), 2 ads (`kyro 229v2ss3`, emoji copy, "10 Reasons Healthcare Workers"), May–Nov 2025, CTR 4.95 % · video not downloadable, so this entry is **analysed from thumbnail.jpg + ad copy only** · 9:16 (1080×1920)
**Format / angle / persona:** the headline "2025's Favorite Nurse Shoes" and the copy "Finally! A shoe that offers More Than just cushioning exists!" with a ✅ benefit list and a 45-day risk-free trial. Nurse audience.
**Thumbnail:** clean product hero of the black/mint OrthoStretch pair on a cream shag pouf in front of sunlit vertical blinds (natural light, shallow depth of field). Caption: "COMFORTWEAR / MIGHT **JUST** CHANGE" in white all-caps geometric bold sans (Proxima Nova/Montserrat Bold: round O, flat terminals), no box, faint shadow. The active word "JUST" sits inside a **solid blue (#1E7BD8-ish) rounded highlight box**. Cap height ≈ 63 px, 2 lines at 69–78 % from top, highlight box 112 px tall. This is a **word-by-word karaoke caption** (CapCut/Submagic style), which no other video in W01–W12 uses. VO probably reads "ComfortWear might just change [your…]". Not verifiable.
**Steal this:** the product-hero opener with no person, and the karaoke caption with a single-word colour box as an alternative to the TikTok white box.

### W07 — "My doctor said I'd never walk normally again because of my weight" (curvy warehouse worker)
**Data:** WearOrtho: $147,747 CAD, ROAS 1.69, 3 ads (`kyro 170v2ss1`, "73% copy", "10 Reasons Healthcare Workers"), Nov 2024–Feb 2026, CTR 5.52 % · 122.6 s · 46 shots · avg 2.67 s / median 2.51 s (slowest cut rate) · VO 177 wpm · EN · 4:5
**Format / angle / persona:** a real UGC creator's talking-head testimonial (plus-size warehouse worker, 250 lb, 9 h shifts) intercut with B-roll. The story runs: insulted by doctor → found tip in a "curvy girls" forum → skeptical → transformed. The close is values-led (body positivity, women's health) with a 45-day guarantee. **No discount is mentioned.**
**Hook (0–3 s):**
- Visual: the same creator, barefoot, struggling to step up her porch/garage step. She grips the door frame and turns her back (one 5.4 s take). This is genuine problem visualisation; the product is not visible until 38.8 s.
- Text hook: "MY DOCTOR SAID I'D NEVER WALK / NORMALLY AGAIN BECAUSE OF MY WEIGHT!" (0–3.25 s), then **swaps to "IT WAS SO RUDE, / I ACTUALLY CRIED"** (3.25 s →). Condensed bold caps (Oswald/Roboto Condensed Bold-like), black on a white rounded box at the **top** (11–22 % from top), line ≈ 42 px.
- Verbal hook: "My doctor said I'd never walk normally again because of my weight." (0.00 s), then "It was so rude, I actually cried." (3.24 s)
- Audio: creator's own voice (sync talking head) + bed · Hook archetype(s): shocking authority quote / injustice + emotional confession + body-type call-out
- First hard cut at 5.41 s. 0 cuts in the first 3 s; 1 headline swap at 3.25 s.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–5.4 | hook | doctor quote → "so rude, I cried" | creator struggling on step | top headline, swaps at 3.25 s |
| 5.4–30.1 | backstory/agitate | "250 pounds… warehouse 9 h/day, 40 h/wk… unsupportive shoes… doctor said lose weight and get surgery" | talking head ×4, bathroom scale, warehouse stock, forklift, swollen foot, red pain line on leg, stock old doctor, **B&W** close-up, Google "best shoes for…" search | captions |
| 30.5–44.7 | discovery | "forum where other curvy girls… tips… orthostretch cushion shoes by ComfortWear… skeptical" | woman walking in park, **Reddit-style dark forum screenshot**, curvy woman posing, first product shot (black/mint on carpet), talking head | captions |
| 45.3–65 | transformation/mechanism | "arch support, heel cushioning… plantar fasciitis healing… no aching knees or lower back" | lacing grey shoe with **red curved arrows**, ComfortWear insole logo, burgundy knit macro, heel-pain illustration with red glow, 3D foot, blue x-ray knees | captions, black-box label "My plantar fasciitis" |
| 65.5–84.7 | proof of use | "bought another two pairs… outlasted… fraction of the cost… pair for work, errands, walks" | sneaker on lap, sole, POV feet, talking head, POV walking | captions |
| 85.1–96 | values | "supports body positivity and women's health" | talking head, 9-up creator grid | captions |
| 96.5–105.6 | risk reversal | "45-day money back guarantee… zero risk… return them" | gym woman with dumbbell, skeleton-foot overlay, handling | captions |
| 106–118.1 | CTA | "to my fellow curvy women… a lifeline for their feet… game changer!" | talking head held 6.7 s | captions |
| 118.8–122.6 | end card v1 | — | — | — |
**B-roll inventory:** talking-head (creator, sync) 14 · problem visualisation ≈ 6 · stock (warehouse, forklift, doctor) 3 · anatomy/medical illustration 4 · product handling/demo ≈ 9 · POV feet/walking 4 · screenshot (Google, forum) 2 · testimonial grid 1 · lifestyle 2
**Transitions & motion:** hard cuts. Red arrow and glow overlays. B&W for the "low point". The talking head is the A-roll, cut back to every 2–3 shots.
**Caption system:** TikTok Classic, bold black on white box, 2 lines. 2-line box ≈ 199 px at 72–87 % from top, line ≈ 45 px.
**Pacing:** slowest in batch. 5.4 s hook take, A-roll talking-head segments 2.4–6.7 s, B-roll 1.3–3.8 s.
**Offer & CTA:** no price or discount. 45-day guarantee at 96.5 s (79 %), then an identity-based CTA ("to my fellow curvy women"). The primary text carries the "73 % of healthcare workers" stat and FREE shipping.
**Steal this:**
- An insult-from-authority quote as the headline, then swap the headline at ~3 s to the emotional payoff ("It was so rude, I actually cried").
- Show the real physical struggle (stairs/steps) as the hook plate, filmed by the actual creator.
- Use a values/identity close (body positivity) in place of a discount. It still scaled to $148k at 1.69 ROAS.

### W08 — "I spent $60 on these shoes for my nursing job and I regret not buying them sooner" (UGC price-regret)
**Data:** WearOrtho: $146,292 CAD, **ROAS 2.21 (best in batch)**, 2 ads (`203_Iteration_UGC_OrthoStretch_H1 V1`, TOF + RTG), Nov 2025–Nov 2026 (running), CTR 4.10 % · 71.1 s (shortest) · 33 shots · avg 2.15 s / median 2.03 s · VO 219 wpm · EN · 9:16
**Format / angle / persona:** a short UGC-style nurse review: price + reverse "regret" hook → who it's for (healthcare, 12 h shifts on concrete) → feature list → value vs. $300 orthotics → durability → social contagion ("three other nurses on my floor ordered") → guarantee + 40 % off urgency. Named "iteration UGC … H1" (hook 1).
**Hook (0–3 s):**
- Visual: a woman crouching to lace a **grey OrthoStretch** on a wood floor. Product visible at 0.0 s, the only video in the batch that opens on the product. From 0.25 s an **animated neon-green glow traces the midsole outline** and pulses through 2.5 s. At 2.57 s she hard-cuts into a high-kick that **flings a shoe at the lens** (3.0–3.5 s, the sole fills the frame).
- Text hook (= caption, timed to VO): "I spent **$60**" (0–1.25 s) → "on these shoes" → "for my nursing job" → "and I **regret**" → "not buying them sooner". **TikTok Sans Bold black on a white rounded box.** Keywords ("$60", "regret") are in **neon green (#2BFF2B) with green glow**. Box ≈ 140 px tall, text ≈ 60 px. The **position jumps**: top (20–28 %) for the first three captions, then lower (~70 %) after the cut.
- Verbal hook: "I spent $60 on these shoes from [for] my nursing job and I regret not buying them sooner." (0.00–4.00 s)
- Audio: VO + bed · Hook archetype(s): price reveal + reverse-psychology regret + identity (nurse) + product-first
- First hard cut at 2.57 s. 3 caption changes + 1 glow animation + 1 cut in the first 3 s.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–4.0 | hook | "I spent $60… I regret not buying them sooner" | lacing with green sole glow → kick at lens | captions, green keywords |
| 4.3–15.8 | qualify | "12-hour shifts on concrete… most comfortable… if you're in healthcare… you need to try these" | nurse holding navy pair, nurse in kitchen, nurse walking on a wet road, shoe in clear bag on grass | captions |
| 16–31.8 | features | "designed by nurses for nurses… arch, superior heel cushioning, wide toe box… easy to clean, slip resistant, anti-sweat" | burgundy shoe walking, **green-glow x-ray foot inside shoe**, **green double-arrows over toe box**, nurse with elderly patient, 3D foot + water splash, **washing machine in 0.2–0.6 s flashes**, sole on wet wood, knit macro | captions |
| 32–48.4 | value + proof | "way cheaper than the $300 orthotics… six months, still new… no more limping to my car… walking on clouds… three other nurses ordered" | **dollar bill dropped on worn shoes**, burgundy pair, nurse on couch, nurse getting out of SUV, woman in park, **delivery box at door ×2** | captions |
| 48.6–64 | offer/CTA | "free US shipping… 45-day money back guarantee… 40% off but only for a limited time… don't wait" | navy pair on grass, POV shoe on concrete, **website product grid on a MacBook** (5.2 s hold), creator kicking leg | captions; **"Don't wait" in an orange box** |
| 64.4–71.1 | end card v2 | — | — | — |
**B-roll inventory:** talking-head/creator with product (VO over) ≈ 6 · product demo/macro ≈ 12 · anatomy/3D overlays 3 · lifestyle (nurse with patient, car, walking) ≈ 5 · problem (worn shoes + cash) 1 · social-proof (delivery boxes) 2 · website/offer 2 · end card 1
**Transitions & motion:** hard cuts. A **throw-to-lens** shoe as the hook's second beat. Animated green glow on the sole, green arrows, a 3D splash. Rapid sub-0.6 s micro-cuts on "easy to clean / slip resistant / anti-sweat" (27.2–30.0 s, 6 shots in 2.8 s).
**Caption system:** TikTok Classic bold black on white box, 1–2 lines. Keyword highlight in neon green (hook only). The position varies by shot (top / mid / low). Orange box for the final imperative.
**Pacing:** tight 71 s. The hook is 2.6 s, then a 3.6 s kick shot. The body runs 0.2–4.7 s. The offer screen holds 5.2 s.
**Offer & CTA:** the price is in the first second ($60). The guarantee lands at 51.3 s (72 %) and 40 % off at 58.4 s (82 %), with a "limited time / don't wait" urgency close.
**Steal this:**
- Lead with the price as the first two words. Green-highlight the price and the emotion word.
- A product-in-hand opener with an animated glow tracing the sole tells people "this is the tech" without VO.
- Keep it under 75 s, use one creator voice, and cut sub-second through the hygiene features.

### W09 — "The day I walked 23 miles through Paris changed how I think about shoes forever" (nurse Europe-trip story)
**Data:** WearOrtho: $121,537 CAD, ROAS 0.03 (attribution artefact; @TF set-up, travel LP), 2 ads (`Kyro_253_1_V3 travel`), Aug–Nov 2025, **CTR 7.46 % (highest in batch)** · 178.1 s (longest) · 104 shots · avg 1.71 s / median 1.53 s · VO 198 wpm · EN · 9:16
**Format / angle / persona:** long-form narrative testimonial ("I'm Sarah, a nurse from Denver"). The story moves through a 3-week, 5-country trip with specific step counts and cities (Amsterdam 18,000 steps; Prague 287 steps; Vienna shoe-shop lady hands her a box; Salzburg 26,000; Barcelona 31,000), then back to hospital shifts. Price anchor $99 → $59, 500,000 nurses.
**Hook (0–3 s):**
- Visual: low-angle Eiffel Tower (with Olympic rings) behind pink roses, a gentle push (0–3.2 s). At 3.2 s it hard-cuts to a POV of a foot on a car pedal (black shoe). Product brand not shown until 60.6 s.
- Text hook: "THE DAY I WALKED 23 MILES / THROUGH PARIS **CHANGED HOW** / **I THINK ABOUT SHOES FOREVER**". Heavy condensed caps (Oswald/Anton-like). Black plus **red underlined** text on a full-width white bar at y≈1301–1550 (68–81 %). 3 lines, line ≈ 47–50 px. On screen 0–5.8 s.
- Verbal hook: "The day I walked 23 miles through Paris, changed how I think about shoes forever." (0.00–5.40 s)
- Audio: VO + bed · Hook archetype(s): specific-number story ("23 miles") + transformation promise + aspirational place
- First hard cut at 3.2 s. 0 cuts in the first 3 s.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–5.8 | hook | "The day I walked 23 miles…" | Eiffel + roses, car pedal POV | white bar |
| 5.8–27.2 | setup | "I'm Sarah, a nurse from Denver… five countries, 12 cities… brought my hospital shoes… 14-hour shifts" | selfie nurse, couple at Eiffel, Trevi tourist, London Eye at night, crowd, worn shoes, **AI-generated nurse-with-patient images** (letterboxed), shoe on carpet | captions |
| 27.8–53.3 | agitate | "Amsterdam 18,000 steps… like concrete… Prague 287 steps… legs killing me… feet on fire… 14 more days" | Amsterdam night street, **red-glow foot**, woman grimacing, Prague cathedral, glowing knee, nurse with burning-foot glow, **B&W** crying/selfie shots | captions |
| 53.5–75.6 | discovery | "something happened in Vienna… lady who owned a shoe shop… handed me a box… ComfortWear OrthoStretch… made by foot doctors… nurses love them" | Vienna Votivkirche, **AI shoe-shop owner + AI box hand-off**, swollen foot massage, purple OrthoStretch on grass, **AI male and female doctors**, nurses posing | captions |
| 76–107.8 | transformation | "Salzburg… heels weren't beat up… wide front part… 26,000 steps… Barcelona 31,000" | Salzburg rooftops, shoe on pouf, POV cobbles, 3D sole render, red X over squished toes, **Apple-Watch-style step ring "26,077"**, Mozart's house, Paris opera at dusk, Colosseum, Barcelona | captions |
| 108–128.6 | mechanism | "special technology… arches… stretches… grips wet hospital floors" | 3D layered sole, green-leg stretch, shoe on hair, knit stretch, steel-floor steps ×4 | captions |
| 129–137.8 | results | "foot pain gone… back pain gone too… two shifts in a row and walk my dog" | nurse on stool, **B&W pain shots** (crying, back), nurse holding sole, hospital room | captions |
| 137.8–152 | social proof | "Over 500,000 nurses… made them for people who stay on their feet" | **15-up creator grid**, nurses, skeleton spine/knee overlays | captions |
| 152.2–160.3 | offer | "usually cost $99, now only $59… 45 days, all your money back" | creators with shoes | captions |
| 160.6–174 | CTA | "told every nurse… three bought their second pair… try ComfortWear… saved my European trip" | creators, burning-feet glow, night-street selfie | ORDER NOW pill from ~171 s |
| 174.2–178.1 | end card v1 | — | — | — |
**B-roll inventory:** travel/landmark ≈ 22 · talking-head/creator (VO over) ≈ 26 · AI-generated stills/scenes (hospital, shop owner, doctors) ≈ 8 · problem visualisation (red glows, B&W pain) ≈ 12 · product demo/handling ≈ 14 · anatomy overlays/3D ≈ 7 · graphic (step ring, grid) 2 · POV feet ≈ 8
**Transitions & motion:** hard cuts. **AI images letterboxed inside a blurred copy of themselves** (picture-in-picture panels). B&W grading for the low points. Red pain glows, a red X, and the step-ring graphic, which is the same asset style as W04's.
**Caption system:** TikTok Classic **bold, per-line white boxes** (each line its own rounded box), 1–2 lines, 2–5 words. Line ≈ 50 px, at 67–76 % from top.
**Pacing:** fast for a 3-minute story. Most shots run 0.8–2.7 s, a scene per clause; the longest is 4.0 s (Eiffel/couple). Holds come on the city/landmark establishing shots.
**Offer & CTA:** 152 s (85 %): strike-through-style "$99 → $59" (verbal only) + 45-day money back.
**Steal this:**
- Hook with an exact distance or number ("23 miles"). Then stack exact numbers (18,000 / 287 / 26,000 / 31,000 steps) as story beats with matching landmark B-roll.
- A third-party "wise stranger" discovery scene (the Vienna shop owner) built from AI stills when you can't film it.
- Use B&W plus red glow as a two-tool grammar for "pain/past" versus colour for "after".

### W10 — "My doctor said I'll have to live with this foot pain forever" (nurse myth-bust + podiatrist story)
**Data:** WearOrtho: $107,754 CAD, ROAS 1.94, 1 ad (`Kyro 141v1ss2`, testimonial copy, "10 Reasons Healthcare Workers"), Aug–Nov 2024, CTR 3.44 % · 110.3 s · 52 shots · avg 2.12 s / median 1.90 s · VO 204 wpm · EN · **4:5 at only 360×450 px** (low-res upload still scaled)
**Format / angle / persona:** a doctor-quote hook, then a rhetorical myth-bust ("Think expensive insoles will help? Nah. Avoiding activity? Nope."). Backstory of a nurse with pain → podiatrist says running shoes aren't suited → frustrating search (expensive/ugly) → found ComfortWear on a forum → features → guarantee "15 days longer than 90 % of brands" → 40 % off.
**Hook (0–3 s):**
- Visual: a high, CCTV-like **top-down shot of a woman descending a concrete stairwell** carrying a water bottle, cautious steps, one take to 3.0 s. Product not visible until 57 s.
- Text hook: "MY DOCTOR SAID I'LL HAVE TO / LIVE WITH THIS FOOT PAIN / FOREVER 😨". **TikTok native text, uppercase bold TikTok Sans, black on white rounded box**, 3 lines at the top (17–33 % from top), line ≈ 40 px, with an emoji.
- Verbal hook: "My doctor said I'll have to live with this foot pain forever." (0.00–2.66 s)
- Audio: VO + bed · Hook archetype(s): authority quote / hopelessness + emoji emotion
- First hard cut at 3.04 s. 0 cuts in the first 3 s.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–3.0 | hook | doctor quote | stairwell overhead | TikTok top text + 😨 |
| 3.2–11.8 | myth-bust | "expensive orthopedic insoles? Nah… avoiding activity? Nope." | insoles in hand, nurse slumped on stairs, woman at shelves | captions |
| 12.3–24.9 | backstory | "two years ago… tried everything, insoles, massages… feet still hurt" | nurse on stairs with neon sneakers, nurse in OR, foot close-up, insole macro, foot massage, woman barefoot with dog | captions |
| 25.1–38.8 | podiatrist | "not enough breaks… running shoes weren't suitable… I was shocked" | podiatrist hands on foot, anatomy wall chart, nurse, bin, woman with dog putting on sneaker | captions |
| 39.2–56.5 | search | "expensive… terrible reviews… plain ugly… another forum… came across ComfortWear" | **Temu/AliExpress-style shoe grid** with a black-box caption, **TikTok "Reply to comment: bad sneakers 😩" sticker** over a shoe store, worn shoes, laptop, Google "People also ask" screenshot | captions; black inverted box "But when I started" |
| 57–91.7 | product + mechanism | "as soon as they arrived… 100% premium orthopedic design… 12 h vs 2 h… arch, toes, heels… weight evenly… wet surfaces… by nurses for nurses… five-star reviews" | delivery bag, black/mint shoe, **split-screen nurse + walking feet**, creator with sole, x-ray foot with toe-box glow, 3D anatomy heel (green), 3D shoe, nurse on couch, wet floor, scrubs creator, nurse with patient, **review screenshot with black caption box** | captions; black boxes for key claims |
| 92–105.8 | offer/CTA | "45-day money back… 15 days longer than 90% of brands… 40% off and free shipping… choose your size and color… link below" | unboxing ×3, burgundy pair, phone on product page, **product carousel graphic with "Choose your size"** | captions |
| 106.5–110.3 | end card v1 | — | — | — |
**B-roll inventory:** talking-head/creator ≈ 7 · problem visualisation ≈ 10 · professional (podiatrist hands, chart) 3 · screenshots (marketplace grid, Google, review, TikTok comment) 5 · product handling/unboxing ≈ 12 · anatomy/3D 4 · lifestyle (nurse with patient) 2 · offer graphic 1
**Transitions & motion:** hard cuts. A split-screen at 62.7 s. A native TikTok comment-reply sticker. **Inverted black-box captions mark key claims** (39.1, 74.1, 85.4, 102.7 s).
**Caption system:** TikTok Classic, black regular/semibold on white box, 1–2 lines. Glyph ≈ 32 px x-height (≈ 45 px with ascenders), 2-line box ≈ 111 px, at 74–83 %. Black box with white text for emphasis lines.
**Pacing:** 3 s hook hold, body 1–3 s. 6.2 s hold on the Google screenshot (reading time) and 5.8 s on the split-screen claim.
**Offer & CTA:** 92 s (83 %): the guarantee comparison "15 days longer than 90 % of brands", then 40 % off + free shipping, "choose your size and color".
**Steal this:**
- An authority-hopelessness quote in native TikTok text (uppercase, emoji) over an anonymous "struggling on stairs" overhead clip.
- A rapid myth-bust triad right after the hook ("Insoles? Nah. Rest? Nope.") to pre-kill alternatives.
- Quantify the guarantee competitively ("15 days longer than 90 % of brands") and invert to a black caption box for each claim.

### W11 — "3 things the healthcare industry doesn't want you to know" (conspiracy-listicle)
**Data:** WearOrtho: $96,540 CAD, ROAS 1.68, 2 ads (`kyro 172v1ss1`, "73% copy"), Nov 2024–Feb 2025, CTR 4.07 % · 100.5 s · 41 shots · avg 2.45 s / median 2.17 s · VO 181 wpm · EN · 4:5
**Format / angle / persona:** numbered "secrets" listicle aimed at nurses. Its items are **the same three objections as W03/W04** (running shoes lack support; painkillers are temporary; you don't need $400 shoes), reframed from "I stopped" to "industry doesn't want you to know". Then the **shared mechanism module** (orthopedists/chiropractors, 12 h cushioning, toe box, breathable, slip-resistant, wash, 10,000 reviews). The close is a Black Friday sale at 55 % off.
**Hook (0–3 s):**
- Visual: extreme close-up of a **wooden massage tool pressing into an oiled sole** (manual therapy/ASMR), slow continuous, 0–2.97 s. At 2.97 s it hard-cuts to a woman on a couch with a pile of sneakers as an orange "1" scales up (3.0–3.5 s). Product not visible until 34.1 s.
- Text hook: "3 THINGS THE / HEALTHCARE INDUSTRY" in white Montserrat Bold caps on a **full-width red banner** (0–149 px, 0–11 %), line ≈ 45 px. Below it, "DOESN'T WANT YOU TO KNOW" in black caps on a white strip (150–230 px), line ≈ 43 px. This is the same two-tier banner template as W05.
- Verbal hook: "Three things the healthcare industry doesn't want you to know." (0.08–2.78 s)
- Audio: VO + bed · Hook archetype(s): forbidden-knowledge / enemy + numbered listicle + ASMR foot visual
- First hard cut at 2.97 s. 0 cuts before it; the "1" pops just after.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–3.0 | hook | "Three things the healthcare industry doesn't want you to know" | oiled-sole massage | red banner + white strip |
| 3.0–13 | #1 running shoes | "great for workouts, not hours on end" | orange "1" scale-pop over couch woman, runners, nurse with red pain glow, nurse selfie, worn shoe | captions |
| 13–28.2 | #2 painkillers | "pills/creams are temporary… real support… real cause" | orange "2" over pills into trash, nurse with pills, woman, **blue glowing legs with up-arrows**, red-glow office worker, 3D foot heel | captions |
| 28.2–41.4 | #3 $400 shoes | "expensive brands ≠ comfort… arch support, roomy toe box, cushioning without breaking the bank" | orange "3" over woman counting cash, **cash on worn shoes**, grey OrthoStretch with **green sole glow**, **white double arrows on toe box**, grey pair | captions |
| 41.4–60.2 | solution/mechanism | "ComfortWear created these with top American orthopedists and chiropractors… 12-hour cushioning… toe box… breathable… slip resistant… easy to wash" | **same stock as W03**: businessman with ComfortWear logo, doctor team, MRI room; 3D shoe on purple pattern "affordable", skeleton-foot overlay, green ✓ new vs worn, green-leg stretch, knit macro, washing machine | captions |
| 60.6–67.5 | proof | "10,000 positive reviews from nurses" | **9-up creator grid** (4.4 s) | captions |
| 68–80 | soft sell | "one of the best things you can do as a nurse is swap your shoes… give these a try" | nurse holding two shoes (5.5 s), creator talking (7.4 s) | captions |
| 80.7–95.9 | offer/CTA | "limited-time Black Friday sale… 55% off… USA's most comfortable shoes" | website on laptop, walking feet ×3, creators holding shoes | **scrolling black marquee "BLACK FRIDAY SALE • BLACK FRIDAY SALE"** at 88–94 % from 80.7 s; offer captions in **black boxes with white text** |
| 96.7–100.5 | end card v1 | — | — | — |
**B-roll inventory:** talking-head/creator ≈ 9 · problem visualisation ≈ 6 · stock (businessman, doctors, MRI) 3 · anatomy/3D ≈ 5 · product demo/handling ≈ 10 · testimonial grid 1 · website 1 · ASMR macro 1
**Transitions & motion:** hard cuts, with animated scale-in numerals (the "1" grows over ~0.5 s). Glow/arrow overlays, a green ✓, and a persistent ticker during the offer.
**Caption system:** TikTok Classic, regular black on white box, 1–2 lines. Line ≈ 45 px, 2-line box ≈ 163 px at 70–82 %. **Switches to black box / white text for the offer section.** Marquee text ≈ 46 px on an 81 px black band.
**Pacing:** 3 s hook, body 1.1–3 s, then the longest holds come right before the offer (5.5 s and 7.4 s talking heads, 5.1 s walking). A deliberate slow-down into the pitch.
**Offer & CTA:** 80.7 s (80 %): Black Friday, 55 % off, with a persistent scrolling ticker. This is the only sale-event framing in the batch.
**Steal this:**
- The same three objections, sold three ways: "I stopped…" (W03), "after I turned 72" (W04), "the industry doesn't want you to know" (W11).
- A seasonal scrolling marquee band at the bottom for the last 20 %. It changes the offer without re-cutting the body.
- Flip caption colours (white box → black box) when the ad switches from story to offer.

### W12 — "Think your sneakers can handle 20,000 steps in Europe? We tested 4 shoes" (hook 2, rewrite of W02)
**Data:** WearOrtho: $92,029 CAD, ROAS 1.40, 1 ad (`Kyro369v2 hook2`), Jul–Nov 2026 (running, newest), CTR 6.17 % · 175.9 s · 71 shots · avg 2.48 s / median 2.26 s · VO 215 wpm · EN · 9:16
**Format / angle / persona:** travel "we tested" comparison. It is **a longer, more specific rewrite of W02**: same opening frame ("When you're exploring a new city, you're not just walking… cobblestones"), same order (Nike → Hoka → Skechers → ComfortWear) with sandals dropped, same reasons (gym-floor design, unstable cushioning and weight, memory foam compresses by afternoon), same "sole firm enough… but flexible", same close ("40% off with free shipping… 45 days… send them back… you'll never pack anything else"). New in W12: prices ($130 / $165 / $70), hour-by-hour failure timestamps ("by hour five", "by hour seven", "at 2 pm… hour nine"), and a payoff line, "Not hurt less, didn't hurt".
**Hook comparison vs. W02:**
- Both open on a **night European shopping street** (W02 Madrid façade vs. W12 a London street with hanging lantern cubes and **tourists dragging suitcases**) under a boxed question headline.
- W12's headline sits at the top (19–30 %); W02's sits low (63–81 %).
- W12 adds a concrete number ("20,000 steps") and a count ("4 shoes"), plus a **second-beat text "RESULTS WERE EMBARRASSING" at 5.7 s** over a creator holding the ComfortWear shoe. This is the "hook2" element.
- Footage shared with W02: the cobblestone POV with the white stone line (W02 #10 = W12 #25), the glasses creator against a green lattice (W02 #8 = W12 #4), the creator holding chunky beige sneakers (W02 #22 = W12 #29), the Versailles cobblestone plaza (W02 #38 = W12 #41), Sagrada Família, and the kitchen creator with burgundy shoe.
**Hook (0–3 s):**
- Visual: handheld walk down a night street (lantern installations, shop lights), people with roller suitcases, 0–2.53 s. Hard cut to a low-angle Sagrada Família with stairs (2.53–5.7 s). Product appears at 5.7 s (creator holds a black/mint shoe).
- Text hook: "THINK YOUR SNEAKERS / CAN HANDLE 20,000 STEPS IN / EUROPE? WE TESTED 4 SHOES". **Montserrat ExtraBold caps, all black, on a plain white rectangle** (y≈371–582, 19–30 % from top). 3 lines, cap ≈ 48 px, line pitch ≈ 69 px. On screen 0–5.7 s. Then "RESULTS WERE / EMBARRASSING" in the same style at 5.7–7.4 s.
- Verbal hook: "We tested four of the most popular travel shoes to see which one actually survives a full day of sightseeing, what we found will change how you pack." (0.00–8.68 s). The **VO and the on-screen question differ**: the text asks, the VO states.
- Audio: VO + bed · Hook archetype(s): challenge question + specific number + "we tested" + travel + embarrassing-result curiosity
- First hard cut at 2.53 s. 1 change in the first 3 s.
**Beat map:**
| t | beat | VO | visuals | text |
|---|---|---|---|---|
| 0–8.7 | hook | "We tested four… will change how you pack" | night street → Sagrada Família → creator with product | top box headline → "RESULTS WERE EMBARRASSING" |
| 8.7–19.2 | frame | "not just walking… cobblestones, old staircases, museum lines, uneven ground for 8, 9, 10 hours" | selfie creator, Versailles cobbles, rock steps, museum line, Park Güell, street | captions |
| 19.2–44.3 | Nike Air Max $130 | "built for running tracks… narrow toe box… by hour five, testers looking for a seat… beaten up" | lacing black shoes, creator with clogs, cobble POV, Nike close-ups, palm promenade, cobbles, Porto viewpoint, **B&W** tired walker | captions |
| 44.3–77 | Hoka $165 | "fool you… foam absorbs straight down… foot rolls side to side… less stable… twice the weight… knees hurt" | Hoka on foot, selfie, track runner, **foot-anatomy sculpture**, Hoka walking, chunky sneakers, B&W tester at door | captions |
| 77–104.5 | Skechers $70 | "memory foam compresses… doesn't recover… least support when you're climbing to the view" | Skechers in hand, alley, **foam squish macro**, Versailles, Sagrada Família, Versailles gardens, Dolomites hiker, 3D foot on insole | captions |
| 104.5–138.9 | ComfortWear | "where the tests stop being a competition… for nurses, healthcare workers and travellers… sole firm… toe box wide… arch support doesn't quit at 2 pm" | creator with burgundy shoe, burgundy pair in scrubs, nurse, travellers, sole cross-section, x-ray toes, arch thumb, lake/fountain, statue | captions |
| 139–152 | results | "22,000 steps… didn't hurt. Not hurt less, didn't hurt… you're still going" | Park Güell steps, creator selfies at Stonehenge/Windsor/Colosseum, night-street blur | captions |
| 152.1–169 | offer/CTA | "40% off with free shipping… 45 days… more than enough for a real trip… send them back… you'll never pack anything else" | couch creator, woman on driveway, misty fjord, POV feet | captions |
| 169.2–175.9 | end card v2 | — | — | — |
**B-roll inventory:** travel/landmark ≈ 24 · comparison vs. competitor shoe ≈ 18 · talking-head/creator selfie (VO over) ≈ 12 · POV feet/walking ≈ 8 · anatomy/3D 3 · product demo/handling ≈ 6 · end card 1
**Transitions & motion:** hard cuts. B&W for "tester suffering" moments. Competitor logos blurred. No stickers, numerals or arrows: cleaner than the 2024–25 cuts.
**Caption system:** a newer, smaller spec. A **single-line** white rounded box with black TikTok Sans Bold, sentence case, one whole phrase (4–7 words) per caption. Box ≈ 78 px tall, glyph ≈ 38 px, at 68–73 % from top. The smallest captions in the batch.
**Pacing:** 2.5 s and 3.2 s hook shots, body 1–3 s, several 4–5 s holds on landmarks (21.1 s rock wall 5.0 s, 115.1 s sole render 5.9 s). The end card holds 6.7 s.
**Offer & CTA:** 152 s (86 %): 40 % off + free shipping + 45-day try framed around "a real trip".
**Steal this:**
- When a comparison body works (W02), ship a long-form rewrite with prices and hour-stamped failures, and test new hooks on it ("hook2").
- Add a second text beat at ~5–6 s ("RESULTS WERE EMBARRASSING") to carry the curiosity past the first cut.
- Write the reframe line "Not hurt less, didn't hurt" as a specific payoff instead of "more comfortable".

### W13 — thumbnail only: "…and special exercises" (failed-remedies beat, 73 % copy)
**Data:** WearOrtho: $89,410 CAD, ROAS 1.93, 1 ad (`Kyro 155v3ss3`, "73% copy", "10 Reasons Healthcare Workers"), Oct 2024–Feb 2025, CTR 4.04 % · video not downloadable, so this entry is **analysed from thumbnail.jpg + ad copy only** · 4:5 (1080×1350)
**Format / angle / persona:** the copy is the "73 % of healthcare workers experience foot pain. ComfortWear changes that." ✅ list (same as W07/W11), headline "2024's Favorite Nurse Shoes". Kyro 155 sits next to Kyro 154 (W03) and was cut in the same Oct-2024 batch.
**Thumbnail:** stock-style close-up of a bare heel rolling on an **orange massage/lacrosse ball** on a light wood floor (shallow depth of field). This is a "things I tried that didn't work" agitation beat, like W10's "insoles, massages" section. Caption: "and special exercises", **TikTok Classic white rounded box (110 px tall, 74–83 % from top) with black TikTok Sans Semibold, glyph ≈ 45 px**, single line, the same spec as W03/W10/W11 of that era. No hook headline is visible in this frame, so the hook can't be assessed.
**Steal this:** list failed remedies (insoles, massages, exercises) visually before the reveal. The thumbnail Meta chose is a problem frame, not a product frame.

---

## Batch patterns
(n = 11 videos with footage, plus 2 thumbnail-only)

- **Length: long.** 71–178 s, mean 129 s. 10/11 run over 100 s and 4/11 over 140 s. Only W08 (71 s), the best ROAS at 2.21, is short. Long-form is the house format and it scales: the top-2 spenders are 112 s and 119 s.
- **Hook = one held shot (~3 s) plus a static headline.** The first hard cut is at a median 3.0 s (range 1.8–5.4). 8/11 hold the first shot ≥ 2.5 s, and 6/11 have zero cuts in the first 3 s. Energy comes from the headline and the VO, not from cutting. Body cut rate averages 2.1 s per shot (range 1.47–2.67).
- **11/11 have a burned-in hook headline that matches the first VO sentence**, and 7/11 use a black + red two-colour headline (W01, W02, W03, W04, W05, W09, W11). Three families:
  - (a) White bar/box with black + red caps, sitting low at 62–81 %: W01, W02, W04, W09.
  - (b) Red banner + white sub-strip pinned to the top 15–17 % of a 4:5 frame: W05, W11.
  - (c) Plain white box with all-black caps at the top: W07, W10, W12.
  Headline fonts are Montserrat ExtraBold (W01, W02, W03, W05, W11, W12) or a condensed Oswald-like face (W04, W07, W09). Line ≈ 40–69 px.
- **Hook archetypes:** numbered/listicle 6/11 ("Top 5", "tested 5/4", "3 things" ×3) · "My doctor said…" authority-injustice quote 2/11 (W07, W10) · first-person story/confession with a specific number or price 3/11 (W05 "never again", W08 "$60… regret", W09 "23 miles"). The "3 things" objection list (running shoes / painkillers / $400 shoes) recurs in 3 videos (W03, W04, W11).
- **Twins and re-skins in this batch:**
  - W01/W02: Kyro 293 v1/v3, same comparison template, nurse vs. travel hook.
  - W03→W04: same script; the hook swaps "after leaving nursing" → "after I turned 72".
  - W03/W05/W11: share a ~40 s verbatim mechanism module and its stock B-roll.
  - W02→W12: travel comparison rewritten longer, with a hook2.
  The account iterates by keeping bodies and swapping hooks/personas.
- **The hook visual is rarely the product.** 1/11 shows ComfortWear in the first 3 s (W08). Hook plates are problem/ASMR (W03 sole scraping, W11 sole massage, W07 struggling on steps, W10 stairwell, W04 slow walk, W05 shoes in a bin) in 6/11, or a European landmark/street in 3/11 (W02, W09, W12). The median product reveal is ~38 s, and 8/11 reveal after 20 s.
- **Personas:** nurse/healthcare 8/11 (W01, W03, W04, W05, W08, W09, W10, W11). Travel/Europe is the lead angle in 3/11 (W02, W09, W12) and a sub-plot in 3 more (W03, W04, W05). Specific outliers: 72-year-old (W04) and curvy warehouse worker (W07). Competitors are named in 4/11 (W01, W02, W12, plus "Amazon" in W03/W04), always with logos blurred.
- **Caption spec that dominates:** TikTok "Classic" (black TikTok Sans on a white rounded box, sentence case, 1–2 lines, 2–6 words, at ~67–87 % from top, line ≈ 45–50 px) in **9/11**. The exceptions are both Kyro 293 cuts, W01/W02: white bold text with black outline and no box. The 2026 cut (W12) shrinks to single-line boxes (≈ 38 px glyph). Emphasis devices: neon-green keyword (W08), black inverted box for claims/offer (W10, W11), orange box for the imperative (W08).
- **Shared B-roll library across editors and years:** glowing green-leg stretching woman (5/11: W03, W04, W05, W09, W11) · washing-machine "easy to wash" (4/11) · 9-to-15-up creator grid for "10,000 / 500,000 reviews" (4/11: W03, W07, W09, W11) · 3D translucent cushion/sole render (5/11) · x-ray toe-box glow (4/11) · stock businessman with ComfortWear logo plus doctor team (W03, W11) · skeleton overlays on real people (W04, W09). This UGC-creator-holding-shoe library forms ~25–35 % of every body.
- **Graphic grammar:** orange outlined numerals 1/2/3 (3/11) · red translucent X stamps over old habits (W02, W04, W09) · red radial pain glow (W04, W07, W09, W11) · B&W grade for the "before/pain" moments (W03, W07, W09, W12) · step-counter ring graphic (W04, W09) · green ✓ on the hero (W03, W11). No whip pans or speed ramps; ~100 % hard cuts. The only transitions are a white flash (W05) and a throw-to-lens (W08).
- **Offer timing:** the hard offer lands at 80–87 % of runtime in 10/11 (W08 starts at 72 %). It is 40 % off in 9/11 (W09 phrased as "$99 → $59"), 55 % Black Friday in W11, and **no discount at all in W07** (guarantee + identity close). A 45-day money-back is named in 7/11, free shipping in 6/11, and BOGO 50 % once (W03).
- **CTA hardware:** 11/11 end on the ComfortWear "TAKE ADVANTAGE OF DISCOUNTS ON BUNDLES" end card held 3.8–6.7 s (v1 white in 9, v2 bubble background in the newest two, W08/W12). A red "ORDER NOW" pill with a bobbing chevron appears over the last 10–15 % in 4/11 (W03, W04, W05, W09).
- **Format drift over time:** every 2024–early-2025 winner is 4:5 (W03, W05, W07, W10, W11, W13). Every cut first run from May 2025 on is 9:16 (W06 May 2025, W04, W09, W01, W02, W08, W12). W10 scaled at 360×450 px, so resolution was not a blocker.
- **VO pace:** mean 198 wpm (164–224). The highest spenders are the fastest (W01 224, W02 223), and the slow ones (W03 164) compensate with longer runtime. One continuous narrator plus a low music bed; only W07 (and W05's testimonial inserts) is sync-sound creator audio.
- **Steal-list for the next brief:** a 3 s held problem/ASMR or landmark plate + a black/red headline + a number in the first line → a numbered or "we tested" body that names and dismisses the alternatives → product at 35–50 % → bolt on the proven mechanism module → offer at ~85 % (40 % off + 45 days + free shipping) → 5–6 s end card.
