# Competitor video breakdowns — Stepprs & The Xstance (insoles)

Source: `ads/video/research/data/competitor_videos.json` (video, running ≥ 30 days, ranked by impressions, variants collapsed). Analysis folders: `ads/video/research/media/competitor_analysis/<key>/`. All 20 ads: status **active**, trend **stable** at pull date (2026-11-14). Rank pools: Stepprs 638 ads, Xstance 352 ads. "Dupes" = number of near-identical variants the library collapsed into the entry (a proxy for how hard the brand is iterating on it).

Method notes:
- Text sizes are glyph-line heights at 1080 px width (1080×1920 for 9:16, 1080×1350 for Xstance 4:5), measured with `measure_text.py`. A "glyph line" is the cap + descender band.
- Transcripts: the shared background job had not reached these keys, so I ran the same faster-whisper "base" settings into my scratchpad (not into the shared folders). "VO wpm" = words ÷ (last VO word − first VO word). This matters for Stepprs, where the VO starts 8–23 s into the ad. Brand names come out as "Steppers" and "X-dance/extant" = Xstance.
- Stepprs videos are 720×1280 (9:16). Xstance long-forms 01/02/03/06/08/09 are 720×900 (4:5). Xstance 04/05/07/10 are 9:16.

---

# STEPPRS (massage/cushion insoles, orange + white foam; "Walk on Clouds — Or It's FREE", up to 60% off, 90-day guarantee)

All 10 run the same headline ("Walk on Clouds—Or It's FREE.") over one of two bodies. Eight use a Michelle plantar-fasciitis testimonial with a ✅ list, and two (02/09) use "Free Gift. 60% off… You've seen the ads." The video carries the creative. The copy barely changes.

### stepprs_01 — Egg-drop test: generic vs Nike vs Stepprs (silent 12 s demo, VO lands late)
**Data:** 472 days running · active · impression rank **1 / 638** (brand's most-shown ad) · stable · 21 dupes · 41.9s · 8 shots (one 29.5 s take) · avg 5.24s / median 1.6s · VO 171 wpm (VO only 12.6–36.5 s) · EN
**Format / angle / persona:** physical torture-test demo ("egg drop") comparing a generic black insole, a teal Nike insole and Stepprs → brand VO with an ailment list → guarantee → CTA. Broad persona: plantar fasciitis, flat feet, pronation, "running, working, on your feet all day".
**Hook (0–3 s):**
- Visual: one continuous handheld POV, top-down, over a granite kitchen island in a high-rise apartment. A black generic insole pair sits left, teal Nike insoles right, and a hand holds 4–5 brown eggs at bottom-left. At 0.00 an egg is mid-air. It lands on the black insole at 0.25 and sits there. At 1.75–2.5 a second egg is held up to the lens, then dropped. At 2.75–3.0 it cracks and yolk splashes on the black insole. An orange Stepprs insole first peeks in at the right edge at 1.75 s. It is fully in frame by ~8 s, and the orange retail pouch appears at ~10 s.
- Text hook: **none** (no on-screen text until 12.6 s).
- Verbal hook: none. The first VO is at 12.59 s: "This is Stepprs, the viral insoles that relieve your foot pain instantly…"
- Audio: natural room sound with egg-crack transients only (mean −34 dB before VO vs −24 dB after) · Hook archetype(s): physical test / "will it break?" curiosity loop, comparison vs named competitor (Nike swoosh visible), no-language visual hook
- First hard cut at 29.5 s; 0 cuts in first 3 s. Visual changes in first 3 s come from in-frame action: 2 egg drops, 1 crack, the product edge entering.
**Beat map:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–8 | hook / test | — | eggs dropped on black then teal Nike insoles, crack and splatter | — |
| 8–12.6 | open loop | — | orange Stepprs pair + pouch now in frame but untouched; eggs keep breaking on the others | — |
| 12.6–17.5 | reveal | "This is Stepprs, the viral insoles that relieve your foot pain instantly" | **first egg on Stepprs at ~15.5–16 s, it survives** | THIS IS STEPPRS / THE VIRAL INSOLES / THAT RELIEVE / YOUR FOOT / PAIN INSTANTLY |
| 17.5–20.8 | mechanism | "innovative technology, shock absorption and massage points" | more drops on orange, intact | TECHNOLOGY, / AND MASSAGE |
| 21.2–29.0 | ailment list + use cases | "say goodbye to plantar fasciitis, flat feet, pronation, poor posture… running, working, on your feet all day" | camera tilts to show the egg graveyard on generic + Nike | PLANTAR FASCIITIS, / PRONATION, / AND DISCOMFORT. / OR ON YOUR |
| 29.3–33.0 | risk reversal | "Try risk-free with their 90-day money back guarantee" | white flash 29.5 → 3 macro insole-texture shots (0.7–1.6 s) | TRY RISK FREE / 90-DAY MONEY / BACK GUARANTEE. |
| 33.0–34.3 | brand line | "step into comfort, step into Stepprs" | man in navy blazer + black jeans strides down a city pavement | STEP INTO STEPPRS. |
| 34.3–38.7 | CTA + offer | "tap shop now and save up to 60%" | orange + grey insoles on orange backdrop; red pill button "SHOP NOW!" with animated cursor tapping | TAP SHOP NOW / TO 60% |
| 38.7–41.9 | dead end | — | 3.2 s black | — |
**B-roll inventory:** product demo (egg-drop torture test) ×1 long take (29.5 s) · comparison vs. competitor product (Nike + generic) inside the same take · ASMR/texture macro (foam pods, massage nodes) ×3 · lifestyle (model walking street) ×1 · offer/price card (CTA button + cursor) ×1
**Transitions & motion:** 1 white flash (end of test → macro). Otherwise hard cuts. Camera is a moving handheld POV (slight tilt and reframe). Animated "SHOP NOW!" pill with a pointer-cursor tap. No zooms or graphics during the test.
**Caption system:** karaoke phrase captions in Montserrat ExtraBold (geometric round "O", wide caps), ALL CAPS, white with a soft drop shadow. The active word sits on a solid **orange rectangle** (brand orange ≈ #E8561E). 2–3 words per caption, 1 line, glyph line ≈ 40 px, centred at 49–51% from top (dead centre, over the countertop). CTA pill: white bold on red rounded rectangle ≈ 68% from top.
**Pacing:** a 29.5 s single-take test with no cuts, then a 12 s close at ~1.4 s per shot. The hold works because each egg is a mini-payoff, every 1.5–3 s.
**Offer & CTA:** guarantee at 29.3 s, "save up to 60%" at 36 s, tap-to-shop button at 34.3 s. No price shown.
**Steal this:**
- Run a torture test where the hero product is placed in frame early but **tested last**. Viewers stay to see the orange one. For WearOrtho: drop a weight or press a palm into a generic flat shoe, a Skechers and OrthoStretch, or do a side-by-side "egg under the heel" stomp.
- Put no text and no VO over the demo for the first 10+ s. Let natural sound (cracks) carry it, then add a modular 20 s VO that can be rewritten per persona (see 07).
- Reuse the same 12 s end-stack (guarantee macro → brand walk → tap-button CTA) across every concept.

### stepprs_02 — "My 14-hour shift felt like 2" UGC POV hook → founder "selling everything" sale montage
**Data:** 132 days · active · rank **3 / 638** · stable · 53.8s · 39 shots · avg 1.38s / median 1.0s · VO 236 wpm (7.3–53.5 s) · EN
**Format / angle / persona:** fake-organic TikTok POV result caption, then a founder-voice "closing-down / 2 days left" sale over a montage of 30+ different UGC creators. Shift worker persona (14-hour shift, work boots).
**Hook (0–3 s):**
- Visual: full-frame POV looking down at own feet in black leather work boots and black trousers, on hallway lino by a doormat. At 1.0 s a hand reaches in. 1.25–2.25 pulls the boot off (white Nike sock). At 2.5 s the boot is held up showing the **orange Stepprs insole inside**. The boot goes back down at 3.0–3.5. Product visible from 2.5 s.
- Text hook: "my 14 hour shift really just felt like 2 😮‍💨🙏" / "Money well spent 👏". TikTok "Classic" text (white TikTok Sans regular, thin dark outline/shadow), lowercase. 2 lines + 1 line, glyph line ≈ 46 px, block 21–28% from top, centred.
- Verbal hook: none until 7.34 s: "Only two days left until we have to sell everything."
- Audio: low background track/ambience, no VO for 7.3 s (−24 dB vs −16 dB in VO section) · Hook archetype(s): POV result testimonial, "money well spent" social proof, product reveal inside the shoe
- First hard cut at 7.63 s; 0 cuts in first 3 s (motion only).
**Beat map:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–7.6 | hook | — | POV boot-off reveal | caption block above |
| 7.6–13 | urgency + offer | "Only two days left until we have to sell everything… giving away our insoles at up to 60% off" | sock foot stepping on insole; man in field with sneaker; woman in pink inserting insole; man in tank top; woman kissing insole + purple sneaker | only two days left / that's why / we're giving / insoles / 60% off 🤑 |
| 13–21.4 | founder story + scale | "Our startup Stepprs… one mission to relieve and end all foot pain… over 300,000 customers worldwide" | orange pouch in grass; suited man by river; foam macro; man in car with pouch; warehouse woman; blonde with "Instant Relief" pouch; **Earth from space** on "worldwide" | our startup / one mission / to relieve / foot pain / over 300,000 / worldwide |
| 21.6–25 | enemy | "Most competitors are selling expensive insoles that hurt and don't even last long" | woman with purple gel insole; **Amazon listing screenshots (Dr. Scholl's $14.97, another $29.99)**; walking legs; blue gel insole flexing | competitors / expensive / and don't even 😫 / last long 😩 |
| 25–31 | origin | "By asking customers… we developed the Stepprs massage insoles" | man in shop aisle; lacing white sneaker; walking feet; white foam insole | by asking / put a lot of / on walking / we developed |
| 31–38.3 | mechanism + price | "custom-made orthopedic massage insole that aligns with your foot shape… at more than half the price" | flexing insole; hand-in-insole; suited man with insoles on ground; dress shoes; smiling worker with tumbler; boot soles up | custom made / orthopedic / that aligns / and guarantees / whole day / at more than |
| 38.6–43.5 | versatility | "any shoe or work boot without having to buy new shoes" | bending insole on lawn; orange insole; insert into slip-on; insert into boot | we made sure / the right shape / you can / or work boot |
| 43.9–50.4 | guarantee + outcome | "up to 12 hours of relief… risk-free 90-day trial… walking on clouds" | sock-shoe on floor; suited man with insole pair; heels walking away | so get up to / risk-free / and experience |
| 50.6–53.8 | close | "if you don't like them you'll get your money back. No questions asked." | insole washed in colander; pouches on an orange car bonnet | don't like them / you'll get your |
**B-roll inventory:** testimonial clip / creator holding product ×~18 (different people, ages 25–70, men + women) · product handling/insert ×8 · ASMR/texture macro ×4 · lifestyle (warehouse, car, shop aisle, walking) ×6 · review/UGC screenshot (Amazon competitor listings) ×1 · stock footage (Earth) ×1 · POV feet ×2
**Transitions & motion:** 100% hard cuts at ~1 s. No graphics apart from emoji in captions. Each shot is a different creator, so the montage reads as "everyone has these".
**Caption system:** 1–2 words per caption, lowercase, white TikTok-classic text with dark shadow, glyph line ≈ 41 px, centred at 61–64% from top. Emoji carry emotion (🤑 😫 😩). There is no headline after the hook.
**Pacing:** 7.6 s POV hold, then a metronomic ~1.0 s median body. The VO is fast (236 wpm) and the shots change on almost every phrase.
**Offer & CTA:** offer in the **first VO line** (7.6–13 s, "up to 60% off" + "2 days left"). Guarantee at 46 s and 50.6 s. No on-screen CTA button.
**Steal this:**
- Use a POV "my 14-hour shift felt like 2 / Money well spent 👏" caption over a nurse pulling off her clog to show the OrthoStretch insole/footbed. It reads as an organic post, not an ad.
- Build a "faces wall" montage: 1 s per real customer holding the shoe, one VO, to show scale ("300,000 customers").
- Show the enemy with Amazon/price screenshots of the competitor ("expensive") instead of naming them in the VO.

### stepprs_03 — "You after 12 hours 🤮 / My feet 😮‍💨" step-in meme → creator show-and-tell
**Data:** 64 days · active · rank **4 / 638** · stable · 5 dupes · 31.0s · 6 shots · avg 5.17s / median 4.42s · VO 215 wpm (2.2–30.7 s) · EN · landing page `/pages/long-shift-li-02`
**Format / angle / persona:** meme caption over a step-in ASMR shot, then a single creator's handheld show-and-tell (old insole vs 3 colourways). Long-shift worker persona.
**Hook (0–3 s):**
- Visual: static camera at shin height behind two legs in white crew socks and black trousers, on a wood-floor kitchen. The left foot stands flat. At 0.5–2.25 s the right foot lifts and presses down onto a thick orange-top/white-foam Stepprs insole lying on the floor, and the foam visibly squashes. Product visible from frame 1.
- Text hook: two white TikTok boxes, one over each leg: "You after / 12 hours 🤮" (left) and "My feet 😮‍💨" (right). Black TikTok Sans semibold on white rounded box, ~26–31% from top. At 2.75 s "OH, MY!" appears: white caps with black outline, ≈ 57% from top.
- Verbal hook: "Oh my…" (2.19 s, sigh of relief), then "this is what you're stepping on every day you go to work…"
- Audio: creator VO (male, casual) · Hook archetype(s): relatable meme format (you vs your feet), ASMR squish, sigh-of-relief reaction
- First hard cut at 4.05 s; 0 cuts in first 3 s.
**Beat map:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–4.0 | hook | "Oh my" | step-in squish | meme labels + OH, MY! |
| 4.0–8.3 | enemy | "this is what you're stepping on every day… causes plantar fasciitis" | flattened grey factory insole held up in a kitchen | THIS IS WHAT |
| 8.3–12.8 | solution | "grab yourself these insoles… walking on a cloud" | orange pair held to camera | INSTEAD, GRAB YOURSELF |
| 12.8–18.6 | features | "great arch support, pressure point placement, lots of cushion" | black colourway, nodes visible | YOU HAVE GREAT |
| 18.6–22.8 | fit | "ankle support… trim them down to fit any shoe or boot" | grey colourway | YOU'VE EVEN GOT |
| 22.8–31.0 | offer / CTA | "These were so cheap, I got one for every pair of shoes I own… 60% off, I'll link them here" | 3 colourways + orange pouch on counter | THESE WERE SO CHEAP |
**B-roll inventory:** POV/feet close-up (step-in) ×1 · comparison vs. competitor product (old factory insole) ×1 · product handling ×4 (one per colourway)
**Transitions & motion:** 5 hard cuts. Each shot is a 4–8 s handheld hold of one product, with no graphics.
**Caption system:** Montserrat Bold/ExtraBold caps, white with black outline, 2–4 words, glyph line ≈ 40 px, centred 62–64% from top.
**Pacing:** slow cut rate (median 4.4 s). The VO carries the pace. Holds work because the product is always in the hand, centre frame.
**Offer & CTA:** "60% off" plus a soft "I'll link them" at 27 s. Multi-pair seeding: "one for every pair of shoes I own".
**Steal this:**
- Split a two-leg shot with labels ("You after a 12-hr shift 🤮" / "My feet in OrthoStretch 😮‍💨"), the foot sinking in, and an audible "oh my".
- Open with the old flat insole from the nurse's current clog ("this is what you're standing on all shift").
- Seed the multi-pair upsell with "I got one for every pair I own".

### stepprs_04 — "Finish 12 hour shifts with ZERO FOOT PAIN" creator review on a lawn
**Data:** 472 days · active · rank **8 / 638** · stable · 13 dupes · 27.9s · 17 shots · avg 1.64s / median 1.46s · VO **271 wpm** · EN
**Format / angle / persona:** UGC voiceover review: old crusty insole vs Stepprs, price anchor vs expensive shoes. 12-hour shift worker.
**Hook (0–3 s):**
- Visual: low angle on grey asphalt. A thick orange/white insole sits on the ground, and a foot in a black ankle sock steps onto it at 0.25–1.0 s, squashing the foam (product in frame 1). Hard cut at 2.6 s to hands bending a flattened, crusty brown old insole over green grass.
- Text hook: "Finish 12 hour shifts with / ZERO FOOT PAIN". Black TikTok Sans medium (line 2 caps) on a white rounded box, glyph line ≈ 45 px, box 16–24% from top (166 px tall). Plus karaoke captions underneath.
- Verbal hook: "I was working on my feet for 12 hours a day, and I was doing it in this." (0.00)
- Audio: creator VO, no audible music · Hook archetype(s): outcome-promise headline + step-in squish + old-vs-new reveal ("doing it in *this*")
- First hard cut at 2.6 s; 1 cut in first 3 s (+ the step-in action).
**Beat map:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–2.6 | hook | "12 hours a day… in this" | step-in on asphalt | headline + I WAS WORKING… |
| 2.6–5.2 | enemy | (cont.) | crusty old insole bent on grass | DOING IT IN THIS. |
| 5.2–7.8 | product | "picked up these Stepprs… walking on clouds" | white foam pods; step-in again | UP THESE STEPPERS, / I FELT LIKE I WAS |
| 7.8–12.2 | price frame | "spent hundreds of dollars on shoes that have terrible insoles" | old insole peeled out of a navy running shoe; macro of a destroyed shoe bed | I SPENT HUNDREDS / TERRIBLE INSOLES |
| 12.2–15.7 | price anchor | "could have picked these up for around 20 bucks" | squeezing old vs new foam | AROUND 20 BUCKS. |
| 15.7–23.1 | features | "super breathable, great arch support… thickest and most comfortable" | squeeze, bend, macro pods | SUPER / GREAT / MOST COMFORTABLE |
| 23.5–27.9 | CTA | "I highly recommend them, I'll leave them right here in the link" | blurred pouch on grass | RECOMMEND THEM / I'LL LEAVE THEM RIGHT |
**B-roll inventory:** POV/feet step-in ×2 · comparison vs. old insole ×4 · product demo (squeeze/bend/trim) ×9 · ASMR/texture macro ×2
**Transitions & motion:** 100% hard cuts at 1.1–2.6 s. Every shot is the same green-lawn background, so orange and white pop.
**Caption system:** karaoke Montserrat ExtraBold caps, white with shadow, active word on an orange box. Glyph line ≈ 46 px, 2–3 words, centred 56–58% from top. Headline box stays for the first 2.6 s only.
**Pacing:** fast VO (271 wpm) and a 1.5 s median. 28 s total, no holds.
**Offer & CTA:** price anchor "~$20 vs hundreds on shoes" at 12 s. CTA is a soft "link right here".
**Steal this:**
- Use a headline box with an outcome + number: "Finish 12-hour shifts with ZERO FOOT PAIN".
- "I was doing it in *this*": the reveal of the old worn insole or shoe is the hook's second beat (cut at 2.6 s).
- Anchor price against what the viewer already wasted ("hundreds on shoes with terrible insoles").

### stepprs_05 — Egg-drop test, reshoot #2 (black granite kitchen, 23 s silent)
**Data:** 472 days · active · rank **9 / 638** · stable · 25 dupes · 48.6s · 8 shots (one 39.7 s take) · avg 6.08s / median 1.83s · VO 177 wpm (VO only 23.1–46.2 s) · EN
**Format / angle / persona:** same concept and VO script as 01, shot in a different kitchen (black sparkle granite, white units, French doors to a garden).
**Hook (0–3 s):**
- Visual: static-ish POV over a black counter, a grey generic insole pair centre-left, a teal Nike insole at the right edge. 0.0–1.75 a hand dangles an egg high above. Release at 2.0 s, crack and splatter on the generic insole at 2.25 s. A hand reaches for the next egg at 3.25 s.
- Text hook: none (no text until ~24 s). Verbal hook: none until 23.09 s ("This is Stepprs, the viral insoles…").
- Audio: natural sound only · Hook archetype(s): physical test, delayed hero
- First hard cut at 39.7 s; 0 cuts in first 10 s.
**Beat map:** 0–8 eggs on generic + Nike · ~8 orange Stepprs enter right · 8–23 more breaks (open loop, ~15 s longer than 01) · 23.1–38.7 VO + karaoke captions over drops on orange (THE VIRAL INSOLES / SHOCK ABSORBING / SAY GOODBYE TO / PRONATION, / WORKING, / TRY RISK FREE) · 39.7–41.6 macro "WITH THEIR / 90-DAY MONEY" · 41.6–42.5 founder walk "STEP INTO COMFORT." · 42.5 "STEP INTO STEPPRS." macro · 43.6–46.2 CTA "TAP SHOP NOW" + grey "SHOP NOW!" pill + cursor · 46.2–48.6 orange insole on black granite (no black end).
**B-roll inventory:** product demo (egg test) ×1 take · comparison vs. competitor ×1 (in take) · ASMR macro ×3 · lifestyle walk ×2 · offer card ×1
**Transitions & motion:** as 01, with a light flash into the end-stack.
**Caption system:** identical to 01 (Montserrat ExtraBold caps, orange word box, ≈ 40 px, mid-frame).
**Pacing:** 39.7 s single take, the longest silent stretch in the batch (23 s with no words).
**Offer & CTA:** guarantee at 38.9 s, "save up to 60%" at 45 s.
**Steal this:**
- A winning test concept can be **reshot in new locations** to beat fatigue. The script and end-stack stay frozen.
- If the demo is watchable, the VO can wait. Here it waited 23 s and still ran for 472 days.
- Keep the end-stack modular (guarantee → brand walk → tap CTA → packshot).

### stepprs_06 — Egg-drop test, reshoot #3 (river-view flat) + dog-eats-egg button
**Data:** 421 days · active · rank **11 / 638** · stable · 25 dupes · 33.2s · 8 shots · avg 4.15s / median 1.27s · VO 186 wpm (8.4–30.0 s) · EN
**Format / angle / persona:** egg test, faster variant. Two eggs in the first 3 s, VO in at 8.4 s, 24.6 s take, humour button at the end.
**Hook (0–3 s):**
- Visual: POV in a bright flat ("MONEY / TUNNEL VISION" posters, river view, dog on the balcony). A black counter holds teal Nike insoles left and black insoles right, with a hand of eggs bottom-left. Egg 1 lands on Nike at 1.25 s and breaks at 1.5. Orange Stepprs appear at the right edge at 1.75 s. Egg 2 splatters at 2.0–2.25. A third is in hand at 3.0.
- Text hook: none. Verbal hook: "This is Stepprs, the viral insoles…" (8.37 s)
- Audio: natural sound · Hook archetype(s): physical test, faster escalation
- First hard cut at 24.6 s.
**Beat map:** 0–8.4 test · 8.4–22.9 VO + captions over drops · 24.6–25.9 orange insole held against the river skyline "THEIR 90 DAY MONEY / BACK GUARANTEE." · 25.9 insoles fanned on pouches on balcony decking "STEP INTO COMFORT." · 26.8 founder walk "STEP INTO STEPPRS." · 27.8–30.1 "TAP SHOP NOW" + red "SHOP NOW!" pill + cursor · 30.1 white flash · **30.2–33.2 the dog licks the broken egg off the floor**.
**B-roll inventory:** product demo ×1 take · comparison ×1 · packshot ×2 · lifestyle walk ×1 · reaction/humour (dog) ×1
**Transitions & motion:** hard cuts plus 2 white flashes. Cursor-tap animation.
**Caption system:** same karaoke spec (Montserrat ExtraBold caps, orange active-word box, ≈ 40 px, mid-frame).
**Pacing:** VO starts 2.7× earlier than 05. The test is denser (2 breaks by 2.25 s).
**Offer & CTA:** guarantee at 23 s, 60% at 29 s, then the dog clip after the CTA. It rewards people who stay to the end and makes the ad loop well.
**Steal this:**
- Add a post-CTA "button" clip (pet, blooper, reaction) that re-rewards viewers and helps the ad loop.
- Show two failures in the first 2.5 s, not one.
- Place the product on a branded surface (pouches, brand-colour backdrop) for the end-stack packshots.

### stepprs_07 — Egg-drop 01 footage, VO re-written for steel-toe / concrete-floor workers
**Data:** 53 days · active · rank **12 / 638** · stable · 14 dupes · 41.2s · 10 shots · avg 4.12s / median 1.4s · VO 165 wpm (12.6–38.8 s) · EN · landing page `/pages/steel-toe-li-02`
**Format / angle / persona:** **same 30.3 s egg take as 01**. Only the VO's use-case line changes: "perfect for steel toe boots, 12-hour shifts, and standing on hard concrete floors". Trades persona.
**Hook (0–3 s):** identical to 01 (eggs on black then teal Nike, orange at the edge from 1.75 s, no text, no VO until 12.56 s).
**Beat map:** 0–30.3 egg take with VO from 12.6 s · 30.3–30.8 **construction framers on a timber frame** "CONCRETE FLOORS" · 30.8 orange insole on pouches "TRY RISK-FREE" · 32.2 3 colourways fanned by river "90 DAY MONEY" · 33.9 founder sits on a bench lacing black boots "STEP INTO COMFORT." · 34.4 boots walking on paving · 34.9 founder walk "STEP INTO STEPPRS." · 36.2 "TAP SHOP NOW" + pill · 38.8 white flash → egg-smeared insoles on the balcony (2.3 s end card).
**B-roll inventory:** product demo (egg) ×1 · lifestyle (construction, boots) ×4 · packshot ×2 · offer card ×1
**Transitions & motion:** hard cuts and 1 white flash.
**Caption system:** same karaoke spec. Key persona word ("CONCRETE FLOORS") gets its own B-roll cut.
**Pacing:** as 01.
**Offer & CTA:** as 01 (90-day, up to 60%).
**Steal this:**
- **Re-voice a proven demo per persona** (nurse: "12-hour shifts on hospital floors"; teacher: "on your feet all day in class") and send each to a persona landing page.
- Add one persona B-roll insert exactly on the persona phrase.
- Use the mess (broken eggs on the competitors) as the end-card image.

### stepprs_08 — "If you have neuropathy from type 2 diabetes, use these for 7 days…" Day 1 / 3 / 7 timeline
**Data:** 72 days · active · rank **15 / 638** · stable · 7 dupes · 49.1s · 34 shots · avg 1.44s / median 1.3s · VO 207 wpm · EN · landing page `/pages/neuropathy-adv-01`
**Format / angle / persona:** conditional "If you have X, do Y for 7 days, this is what would happen" with a day-by-day outcome timeline. Heavy AI-generated anatomy and persona B-roll. Diabetic neuropathy persona (older men, trades workers).
**Hook (0–3 s):**
- Visual: 0.00–0.47 real dissected foot (fascia/tendons) lifted with tweezers (shock). 0.47–1.1 AI-rendered sole with red nerve fibres, on a bed. 1.1–2.5 an older woman's swollen white foot with red toenails, a hand gripping the ankle, on a wood floor. 2.5–4.1 hands squeezing the white Stepprs massage-node foam (product at 2.5 s).
- Text hook: none beyond captions. Single-word captions: "if" "have" "neuropathy" "from" **"TYPE 2 DIABETES"** "but" "use" "these" "massage".
- Verbal hook: "If you have neuropathy from type 2 diabetes, but use these massage insoles for 7 days, this is what would happen." (0.00)
- Audio: VO (male, steady) · Hook archetype(s): condition call-out + gross-out anatomy + "this is what would happen" open loop + time-bound promise
- First hard cut at 0.47 s; 3 cuts in first 3 s.
**Beat map:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–4.1 | hook | "If you have neuropathy… 7 days… this is what would happen" | cadaver foot, AI nerve foot, swollen foot, squeeze product | TYPE 2 DIABETES |
| 4.1–6.1 | setup | (cont.) | grey-bearded man tying shoes on porch steps | 7 DAYS |
| 6.1–16.8 | Day 1 | "massage nodes activate circulation and wake your nerves… burning stops in minutes" | white flash → hi-vis worker carrying pipes with **AI orange glow on feet**; 3D foot on Stepprs; thumb on nodes; 3D foot with lightning; red vein foot; flaming foot; glass foot on insole; warehouse walker glowing | DAY 1 / ACTIVATE / WAKE / burning / STOP |
| 16.8–27.6 | Day 3 | "deep throbbing and swelling would vanish… shock absorption…" | sock feet on insoles with **green glow**; bare swollen feet; warehouse worker walking; **egg-drop clip re-used** "SHOCK ABSORPTION"; man with egg-test table on a rooftop | DAY 3 / DEEP / SHOCK ABSORPTION |
| 27.8–37.3 | Day 7 | "you can actually feel your toes again… cooling ventilation… speeds healing" | man on lawn; boot stamping dust; hi-vis worker with tablet; foam macro on orange; 3D leg with green healing glow | DAY 7 / FEEL / cooling / SPEEDS |
| 37.3–39.5 | outcome | "you'd essentially have your life back in a week" | road worker with cones; smiling worker close-up | WEEK |
| 39.5–49.1 | offer + CTA | "bundle up to 60% off only for people who watch this video. Click the link… without pills or surgery" | 4 colourways fanned by river; pouches on balcony; hand on packs | CLICK THE LINK / NUMB ACHING FEET / neuropathy |
**B-roll inventory:** anatomy/3D/medical animation ×8 (AI renders: nerves, flames, glass foot, healing glow) · problem visualisation (swollen feet, cadaver) ×4 · lifestyle (trades/warehouse workers, AI-generated look) ×9 · product demo/handling ×5 · egg-test re-use ×2 · packshot/offer ×4
**Transitions & motion:** hard cuts at ~1.3 s, 1 white flash at "Day 1". **Glow overlays** (orange for pain on Day 1 → green for healing on Day 3/7) show the progress visually. Flaming/lightning foot renders.
**Caption system:** single words, lowercase white with black outline (rounded sans, Proxima Nova Bold-like). **Keywords switch to ALL CAPS** (TYPE 2 DIABETES, DAY 1/3/7, ACTIVATE, WAKE, STOP, DEEP, FEEL, SPEEDS, WEEK, CLICK THE LINK). Glyph line ≈ 38 px lowercase / ≈ 57 px caps, centred 66–70% from top.
**Pacing:** 1.3 s median throughout. "Day" markers every ~10 s act as retention checkpoints.
**Offer & CTA:** "bundle up to 60% off **only for people who watch this video**" at 39.5 s. "Without pills or surgery" closes.
**Steal this:**
- "If you have [plantar fasciitis / bunions], wear these for 7 days. Here's what happens: Day 1… Day 3… Day 7…", with a caption marker per day.
- Use an orange-to-green glow overlay on the foot to show pain becoming relief across the timeline.
- "Only for people who watch this video" makes the discount feel exclusive without changing the real offer.

### stepprs_09 — "5 years of plantar fasciitis pain gone instantly" stairwell POV → same sale montage as 02
**Data:** 132 days · active · rank **23 / 638** · stable · 3 dupes · 56.4s · 39 shots · avg 1.45s / median 1.0s · VO 236 wpm (9.9–56.1 s) · EN
**Format / angle / persona:** **hook-swap of 02**. Shots 2–39 are identical to 02 (shifted +2.7 s), with a new 10.3 s POV hook. Plantar fasciitis persona.
**Hook (0–3 s):**
- Visual: handheld POV walking down a grey stairwell (black/white sneakers, ribbed black trousers), bouncing and tilting. **No product visible** until 10.3 s (sock foot stepping onto an insole).
- Text hook: "5 years of / plantar fasciitis pain / gone instantly 😮‍💨🙏" + "Money well spent 👏". TikTok classic white text with thin outline, glyph line ≈ 49 px, block 18–27% from top.
- Verbal hook: none until 9.92 s ("Only two days left…").
- Audio: low background track · Hook archetype(s): POV result testimonial (duration of suffering + "instantly")
- First hard cut at 10.27 s; 0 cuts in first 10 s.
**Beat map:** 0–10.3 POV stairs · 10.3–56.4 = 02's body (urgency/60% off → founder mission → 300,000 customers → enemy Amazon screenshots → developed → mechanism → any shoe/boot → 90-day risk-free → money back).
**B-roll inventory / Transitions / Caption system:** as 02 (lowercase 1–2-word captions ≈ 41 px at 61–64%; ~1 s hard cuts).
**Pacing:** 10.3 s POV hold (2.7 s longer than 02) before the first cut.
**Offer & CTA:** as 02.
**Steal this:**
- Hook-swap tests on a frozen body are cheap. Note that the version whose hook **shows the product in the shoe at 2.5 s (02, rank 3)** out-ranks the stairwell version with no product for 10 s (09, rank 23).
- Put the condition, the years suffered and the speed of relief in one caption ("5 years… gone instantly").
- Keep POV hooks under ~7–8 s.

### stepprs_10 — "You after 12 hours / My feet" step-in, long version with old insole on screen
**Data:** 384 days · active · rank **24 / 638** · stable · 13 dupes · 32.9s · 6 shots · avg 5.48s / median 5.88s · VO 216 wpm (4.1–32.5 s) · EN
**Format / angle / persona:** **the original long cut of 03**. Same creator VO and colourway shots, with a 5.9 s hook (03's is 4.0 s).
**Hook (0–3 s):**
- Visual: same shin-height kitchen shot. Here both insoles are visible: a thin grey factory insole (left) and a thick Stepprs (right). 0.25–1.0 s the left foot slams onto the old flat insole. 2.5–3.5 s the right foot steps onto the Stepprs and the foam squashes. Product in frame 1.
- Text hook: "You after / 12 hours 🤮" / "My feet 😮‍💨" (TikTok white boxes, black text, ~27–31% from top).
- Verbal hook: "Oh my!" (4.14 s), "This is what you're stepping on…" (5.9 s)
- Audio: creator VO · Hook archetype(s): meme label + side-by-side old vs new step-in
- First hard cut at 5.88 s.
**Beat map:** 0–5.9 hook · 5.9–10.2 old insole "THIS IS WHAT" · 10.2–14.6 orange "INSTEAD, GRAB YOURSELF" · 14.6–20.5 black "YOU HAVE GREAT" · 20.5–24.6 grey "YOU'VE EVEN GOT" · 24.6–32.9 3 colours + pouch "THESE WERE SO CHEAP" / "60% off, I'll link them".
**B-roll inventory:** POV step-in ×1 · old insole ×1 · product handling ×4
**Transitions & motion:** 5 hard cuts, no graphics.
**Caption system:** Montserrat Bold caps, white with black outline, ≈ 40 px at 62–64%.
**Pacing:** 4–8 s handheld holds.
**Offer & CTA:** "60% off", soft link CTA.
**Steal this:**
- The brand **re-cut its own 384-day winner 1.9 s tighter** (03, launched 64 days ago, now rank 4 vs rank 24). Trimming the hook is the cheapest iteration.
- Keep the old-vs-new step-in visible in one frame. The tighter cut drops the explicit old insole and still wins, so the meme labels carry it.
- Single-creator show-and-tell (one product per shot) with zero graphics can run for over a year.

---

# THE XSTANCE (green "Triple Support System" orthotic insoles; 90-day guarantee; up to 42–55% off multi-pair)

Nine of ten are **4–6.5 min long-form VSL-style ads**. The tenth is a 28 s Black Friday cut. They are built from three reusable script bodies, each with many hooks, plus one shared **UGC review tail** (~80–135 s) that sits after the CTA behind a persistent green "Click Below ↓" banner:
- **Body A, "presenter explainer"** (01, 03, 08): a suited man talks selfie-style to camera, then mechanism (overpronation) → failed fixes → Triple Support System → multi-pair → 42% off.
- **Body B, "customer story"** (02, 06, 09, 07): a first-person 300-lb worker or plus-size woman tells the same scripted odyssey (work shoes, concrete floors, cancelled Disneyland/Six Flags, podiatrist, Amazon insoles, $600 orthotics, forum testimonial, "Xstance Insoles 2.0 developed with foot surgeon Dr. Gregory Pomeroy", 90-day, ships from Utah, results timeline, bought 3–5 more pairs).
- **Body C, "doctor at a podcast mic"** (04, 05): "If I wanted to stop morning heel pain starting today, here's what I'd do." An anti-list ("I wouldn't…"), then "fascia collapse" mechanism, then product.

Per the brief, the first 60 s of each is analysed shot by shot, and the rest is summarised by section from the shot sheets and transcript.

### the_xstance_01 — "3 Plantar Fasciitis MYTHS making the pain worse" → presenter explainer (Body A)
**Data:** 409 days · active · impression rank **1 / 352** · stable · 12 dupes · 308.9s · 147 shots · avg 2.10s / median 1.47s · VO 195 wpm (200 wpm in first 60 s) · EN · 4:5 (720×900) · LP `/article/5-reasons` (advertorial)
**Format / angle / persona:** myth-busting listicle hook → presenter explainer VSL → offer → UGC review reel. Persona: plantar fasciitis, morning heel pain, people who stand or walk all day, 50+.
**Hook (0–3 s):**
- Visual: full-frame close-up of a bare forefoot/sole with **red marker dots** on pressure points. A zig-zag steel-wire foot-acupressure tool is pressed and rocked across the toes (motion every frame). Hard cut at 3.2 s to a man in a teal tee and grey shorts doing a wall calf stretch. **No product until 89.3 s.**
- Text hook: "3 Plantar Fasciitis MYTHS" (black) / "making the pain worse" (red). Bold sans (Montserrat/Inter Bold-like: double-story "a", geometric "o"), sentence case + "MYTHS" caps, on a white rounded pill. Glyph line ≈ 60 px, pill 4–15% from top, centred. It persists through the myth list. Each myth is added as a smaller white sub-pill below (≈ 30 px): "Stretching calves relieves tension" / "Putting ice stops the problem" / "Soft sneakers give proper support".
- Verbal hook: "Three plantar fasciitis myths making the pain worse…" (0.00)
- Audio: male VO (presenter); faint music bed (not verified) · Hook archetype(s): myth-buster / "you're doing it wrong", numbered list (3), pain-point gross-out (marker dots on sole)
- First hard cut at 3.2 s; 1 visual change in first 3 s (tool motion), 3 cuts by 10 s.
**First 60 s, shot by shot:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–3.2 | hook | "3 plantar fasciitis myths making the pain worse" | acupressure tool on marked sole | headline pill |
| 3.2–4.8 | myth 1 | "stretching calves relieves tension" | man wall-stretching calves | + sub-pill myth 1 |
| 4.8–7.2 | myth 2 | "putting ice on feet stops the problem" | man on sofa, feet on blue ice pack | sub-pill myth 2 |
| 7.2–11.2 | myth 3 + pivot | "wearing soft sneakers gives proper support. Do this instead." | older man squeezing a soft sneaker | sub-pill myth 3 |
| 11.2–14.6 | symptom call-out | "Most people don't realize this. If you wake up with stabbing heel pain," | grey-haired woman limping by car, hand on car; woman in pyjamas on bed edge | grey caption boxes begin |
| 14.6–20.9 | symptoms | "feet ache after standing… barefoot across hard floors feels unbearable" | woman with garden hose; bare feet on hard floor; blonde wincing | "feels unbearable…" |
| 19.9–24.6 | reframe | "it's NOT just aging, NOT just wear and tear, definitely NOT…" | man head in hands; heavy man limping; **presenter selfie (suit, blue tie, home office) first at 22.1** | NOT in caps |
| 24.6–30.8 | truth | "The truth is… doesn't actually start in your heel" | X-ray with blue-gloved hand; foot with fascia overlay + red target; hands massaging heel | |
| 30.8–39.9 | mechanism | "It starts with the way your foot moves… thick band… plantar fascia… feet roll too far inward" | presenter; 3D X-ray shoe glowing red; 3D fascia; skeleton foot model with pen | |
| 39.9–47.8 | mechanism | "overpronation… tiny tears… inflammation, stiffness, pain with every step" | presenter; 3D tissue stretching; glowing X-ray foot; limping man; woman walking to car | |
| 47.8–56.5 | analogy | "like pulling a rubber band until it snaps… arch collapses… irritated again and again" | presenter; **rubber band stretched across a slipper**; 3D arch collapse; foot on treadmill | |
| 56.5–60 | re-agitate | "That's why so many people… stabbing heel pain in the morning" | presenter; woman in car park; man grimacing | "with Plantar Fasciitis struggle with:" |
**Rest by section:** 60–72 symptom recap (orange fire overlay on the sole, "burning") + "not because they're getting older". 72–89 **failed fixes with red ❌ stickers** (ice pack, new shoes, cortisone shot, stretch, shoe, shot, "is going to fix PF for good"). **89.3 product reveal** "That's exactly why we created Xstance Insoles" (green insoles floating on a sparkle background), then a before/after heel-alignment graphic (red tilted line → green straight line). 95–139 "most insoles are soft OR hard, Xstance does both" → **"THE TRIPLE SUPPORT SYSTEM"** (green caps chapter title on a 3-panel split) with 3 named parts, each over its own B-roll and labelled in small spaced caps ("A PRECISION ARCH STABILIZER", "THE IMPACT CUSHIONING HEEL PAD", "A SOFT SILICONE COMFORT LAYER"). 139–153 "Still skeptical?" objection → "most insoles only solve PART of the problem". 153–162 90-day risk-free (cash handover, box packing, $100 bills). 162–190 **multi-pair logic**: "if you switch between sneakers, work shoes, slippers… progress gets undone", with an overpronation protractor graphic. 190–219 **offer**: "special multi-pair discount… up to 42% off" over a checkout screenshot (4 pairs save 41%, 5 pairs save 42%), a wall clock "For a LIMITED TIME", warehouse/boxes "thousands of orders per day… can't guarantee that'll be true tomorrow", PDP screenshot "$39.95 ~~$59.95~~" with "Click the link below", yellow "42% OFF" circle badge, red ✗ over a limping woman "Don't wait…", before/after heel graphic "FIX the root cause of Plantar Fasciitis today!" (7.8 s hold). **226.8–308.9 UGC review tail**: 4 selfie testimonials (9–37 s each). Captions switch to Oswald Bold white with black stroke (2 lines). A **persistent green bottom banner** "Click Below ↓ / UP TO 42% OFF FOR 24H" (white bold on #4CC97A-ish, arrows both sides, 85–97% from top). The last clip ends on a green-box "IT'S IMPROVING!".
**B-roll inventory:** talking-head (presenter) ×~20 · problem visualisation (limping, wincing, holding feet, fire/red overlays) ×~25 · anatomy/3D/X-ray ×~12 · comparison/failed fixes with ✗ ×8 · product demo (finger pressing arch, insert into shoe, flex) ×~20 · lifestyle walking (diverse 50–70 y/o) ×~20 · offer/price card (checkout + PDP screenshots, 42% badge, clock) ×5 · testimonial clip (UGC selfie) ×4 long · stock (warehouse, cash, delivery) ×6
**Transitions & motion:** ~97% hard cuts. Sticker graphics (red ✗ circles, red/green alignment lines, 42% badge, protractor). Split-screen 2–3 panel for the Triple Support System. No whip transitions.
**Caption system:** body: white sentence-case rounded geometric sans (Google Sans/Outfit-like, regular) on a **semi-transparent dark-grey rounded box**, 2 lines, 3–7 words, glyph line ≈ 45–50 px, box 75–87% from top. Emphasis via CAPS words (NOT, PART, BOTH, RISK-FREE, LIMITED TIME, FIX). Hook uses a white pill headline. Tail uses Oswald stroke captions plus the green banner.
**Pacing:** hook shots 1.6–4.1 s, body median ~1.5 s, offer holds 2–3 s, final FIX graphic 7.8 s, UGC tail 9–37 s per clip (one-take holds).
**Offer & CTA:** guarantee 153 s, multi-pair rationale 162 s, **42% off at 194 s** (63% through), scarcity 199–209 s, "Click the link below" 209 s, banner restates "UP TO 42% OFF FOR 24H" for the last 90 s.
**Steal this:**
- "3 [condition] MYTHS making the pain worse" pill headline with myths stacked as sub-pills, then "Do this instead". The numbered list buys ~10 s of retention.
- Put a persistent offer banner over a long UGC review reel after the CTA. It turns viewers who stay into a second CTA zone.
- Use a "one pair isn't enough, you switch shoes" script beat to justify a multi-pair bundle (perfect for "a pair for work and a pair for home").

### the_xstance_02 — "Don't put ice on Plantar Fasciitis — do this instead!" → 300-lb worker's story (Body B)
**Data:** 369 days · active · rank **2 / 352** · stable · 10 dupes · 336.2s · 142 shots · avg 2.37s / median 1.64s · VO 188 wpm (191 in first 60 s) · EN · 4:5
**Format / angle / persona:** "don't do X, do this instead" hook → first-person customer odyssey (heavy-set work-boot worker, concrete floors, dad) → discovery of Xstance via a testimonial → results → UGC tail. Persona: male worker 40s–50s (the women's version is 06/09).
**Hook (0–3 s):**
- Visual: 0–2.8 s close-up of bare legs stepping down into a blue plastic tub of ice water, with handheld wobble. Hard cut at 2.8 s to a bearded heavy man (charcoal Polo tee) talking head in a stone-fireplace living room. 3.3 s cut to him walking down garden steps with a **red circular heel-pain icon** sticker on his heel.
- Text hook: "Don't put ice on Plantar Fasciitis" (appears 0.25 s), then "Do this instead!" (pops in at 2.0 s, scaling up). Black bold sans on white rounded boxes (TikTok-native style), glyph line ≈ 35 px, boxes 6–13% from top.
- Verbal hook: "Don't put ice on plantar fasciitis, do this instead." (0.00)
- Audio: male first-person VO (the "customer") · Hook archetype(s): "don't do X" contrarian warning + "do this instead" curiosity, relatable home remedy
- First hard cut at 2.8 s; 2 cuts in first 3.5 s.
**First 60 s, shot by shot (condensed):**
| t | beat | VO (short) | visuals/B-roll | on-screen text (word-by-word) |
|---|---|---|---|---|
| 0–2.8 | hook | "Don't put ice… do this instead" | feet into ice tub | white-box headlines |
| 2.8–6.7 | intro | "I've struggled with heel pain from my work boots for about a year" | TH; walking down steps with red heel icon; POV boot on concrete; kneeling worker with hard hat | I've / struggled / **HEEL PAIN** (red caps) / my work / a year. |
| 6.7–13.4 | who + why | "bigger guy at almost 300 pounds walking all day on concrete floors" | TH; man walking city pavement; hi-vis worker legs on wet concrete; man by van clutching foot (red icon) | bigger / walking / concrete |
| 13.4–20.7 | first attack | "The first time… incapacitated me for a month… kept coming back" | **X-ray overlay on an ankle with red arrows**; man on sofa holding foot; TH; **yellow lightning bolts + red glow** on foot | The first time, / incapacitated / coming |
| 20.7–26.4 | everything failed | "over the past 14 months I tried everything" | calendar macro; TH; **3-panel collage** (massage gun, splint, foot massager); man walking by fence | over / I tried / **EVERYTHING** (yellow) / nothing |
| 26.4–33.7 | emotional cost | "We had to cancel our family trip to Disneyland… kids looking forward to it" | plane with red **CANCELED** stamp; Disneyland castle with red CANCELED stamp; TH; sad girl on suitcase; sad boy | to cancel / to Disneyland. / because / forward |
| 33.7–43.6 | identity crisis | "Is this the life I'm going to live? Sidelined, frustrated, a burden to my family… I refused to accept this" | TH; **re-enacted moody shots** of him (maroon shirt, dim room, by truck) | "Is this / "Sidelined, / frustrated / my family? (all red) / I refused |
| 43.6–55.2 | diagnosis + standard advice | "A podiatrist told me… ligament inflamed… suggested rest, icing, stretching, orthopedic shoes, braces" | doctor in white coat; 3D foot "Plantar Fasciitis." red; 3D fascia red with **PiP of the TH (bottom-right)**; legs; ice; stretch; orthopedic shoe; brace | A podiatrist / Plantar Fasciitis. / It's when / suggested / icing, / stretching, / orthopedic |
| 55.2–60 | escalation | "next step was cortisone shots and custom orthotics" | syringe; plaster casting of foot; TH | If those / and / I tried |
**Rest by section:** 60–104 failed purchases: orthopedic sneakers, **Amazon listing screenshot of Dr. Scholl's with TH PiP** "I ordered 5 brands from Amazon", red ✗ over flimsy/rigid insoles, night splints, painkillers, "$600 custom orthotics" (cash), forums/Facebook/YouTube/journals (laptop typing). 104–155 discovery: "stumbled across a testimonial… hundreds of comments… **Xstance Insoles 2.0**… with foot & ankle surgeon Dr. Gregory Pomeroy" (product first at ~116 s on a sparkle background). Features over hands-on demos with **green keyword captions** (arch, padding, Deep, heel-cup diagram with a coloured "shock wave"). 149–170 "what's a few more bucks" → website screenshot + review card ("Timothy Kernell, Gas Station Worker ★★★★★") → **90-day** (green) cash handoff → "shipped from Utah, received in 2 days". 170–212 results timeline: "by the end of my shift… next day 80% gone… after a week" → even knees and hips → "bought three more pairs so I wouldn't have to switch them". 212–247 mechanism recap + "don't make the same mistake I did… don't rely on pills" (red ✗ over pills/limping) → "**If Xstance insoles are still available, get yours now**". 254–336 UGC tail with green "Click Below / UP TO 42% OFF FOR 24H" banner.
**B-roll inventory:** talking-head (customer) ×~35 · re-enactment of the narrator (moody alt wardrobe) ×6 · problem visualisation ×~20 · stock emotional (kids, castle, plane, calendar) ×6 · anatomy/3D/X-ray ×6 · competitor/failed fixes (Amazon screenshot, ✗ insoles, splints, orthotics) ×~12 · review/website screenshot ×3 · product demo ×~15 · testimonial clip ×4 (tail)
**Transitions & motion:** hard cuts. Graphic stickers: red heel icon, yellow lightning, red CANCELED rubber stamps, red ✗, yellow arrows, product-feature icon bubbles. **Picture-in-picture talking head** over B-roll and screenshots. 3-panel collage for "EVERYTHING".
**Caption system:** **word-by-word Oswald Bold** (tall condensed sans), white with black stroke + drop shadow, 1–2 words, glyph height ≈ 75–90 px incl. stroke, lower third (~81–88% from top). Colour-coded keywords: **red = pain/emotion**, **yellow = emphasis**, **green = product benefit / relief**. Hook uses TikTok-native white boxes.
**Pacing:** 1–2 s cuts throughout the story. The TH is never on screen for more than ~2.5 s before cutting to illustrative B-roll. Tail clips hold 9–37 s.
**Offer & CTA:** no discount spoken in the body. Guarantee at 155–166 s, CTA at 243 s ("if still available"), and the 42%/24H offer lives only in the tail banner.
**Steal this:**
- Colour-code word-by-word captions: red for pain words, green for relief and product words. Viewers read the emotional arc without sound.
- Use an emotional-cost beat with stock + stamp graphics ("we had to cancel the family trip" + red CANCELED stamp). For WearOrtho: a grandchild's recital or a cruise excursion skipped.
- Show a "failed fixes" montage with the Amazon competitor screenshot + PiP narrator, then the $600 custom-orthotic anchor.

### the_xstance_03 — "Stop resting if your HIPS HURT — do this instead!" → hip-pain version of Body A
**Data:** 385 days · active · rank **3 / 352** · stable · 11 dupes · 289.6s · 142 shots · avg 2.04s / median 1.36s · VO 204 wpm (229 in first 60 s) · EN · 4:5
**Format / angle / persona:** Body A with the problem moved up the kinetic chain: hip pain caused by the feet ("7 out of 10 people overpronate"). Persona: 55+ women and men with hip, knee or lower-back ache. Ad copy: "Hips still aching no matter how much you rest, ice, stretch… or even take a pill?"
**Hook (0–3 s):**
- Visual: grey-haired woman in a white sweater with an orange shoulder bag bends stiffly over a stone garden bench, hands on the bench, and slowly lowers herself (0–2.47 s). Hard cut at 2.47 s to the same woman walking by a black car with a **red glow on her hip**.
- Text hook: "Stop resting / if your **HIPS HURT**". Black bold sans + red heavy caps on a white rounded box, 4–14% from top, glyph line ≈ 55–60 px. At 1.75 s "Do this instead!" pops in as a sub-pill (≈ 30 px).
- Verbal hook: "Stop resting if your hips hurt, do this instead." (0.00)
- Audio: presenter VO · Hook archetype(s): counter-intuitive "stop doing X" + body-part call-out
- First hard cut at 2.47 s.
**First 60 s:** 2.5–14.3 symptom call-out with red hip glows (woman by car "Most people don't realize this…", man in a garden "hips ache when you stand or walk", woman with hose, man wincing in a chair "sharp pinch", hip close-up "deep soreness near the groin or outer hip", woman walking "stiff and tight", man rising from bed "when you get up from a chair", woman on stairs "or climb stairs") → 14.3–19.5 "NOT just aging / NOT just wear and tear / definitely NOT…" (man head in hands, limping man, presenter) → 19.5–24.2 "The truth is… doesn't actually start at your hips. It starts at your feet." (hip X-ray held up, **blue 3D skeleton**, hands on foot) → 24.2–36.3 mechanism (glowing X-ray shoe, presenter "for seven out of ten people", skeleton foot "roll far too inward", bare feet "This hidden problem", 3D weight-line foot "shifts your weight the wrong way", woman walking with **knee/hip anatomy bubble icons** "puts constant strain", knee X-ray overlay, hip glow) → 36.4–49.7 "like knocking over the first domino… foundation is off" + symptom re-list → 49.8–60 "Not because their hips are weak, but because their feet are out of alignment… worst part… limiting their mobility. So what do most people do?"
**Rest by section:** 60–78 failed fixes (pain creams, anti-inflammatory pills, ice, hip braces, orthopedic shoes, red ✗) → 78 product "Xstance Insoles… take pressure off your hips" → 81–121 soft-vs-hard → Triple Support System → 121–141 skeptic + 90-day → 141–175 multi-pair logic → 175–200 **42% off**, checkout, clock, warehouse, PDP $39.95, "Don't wait until your **hip** pain gets worse", "Stop masking the symptoms", "FIX the real problem today!" (7 s) → 207.5–289.6 UGC tail + green banner (42% / 24H).
**B-roll inventory:** same library as 01, plus hip-specific problem shots (red hip glows ×8, hip/knee anatomy ×4, domino).
**Transitions & motion / Caption system / Pacing:** as 01 (grey translucent box captions ≈ 45–50 px at 75–87%; hard cuts; median 1.36 s, the fastest of the long-forms).
**Offer & CTA:** as 01 (42% off at ~177 s, banner in tail).
**Steal this:**
- **Re-skin one script for a new body part** ("Stop resting if your HIPS / KNEES / BACK hurt"): swap ~25% of the B-roll and keep the mechanism → product → offer.
- A red glow on the painful joint is cheap and makes the problem readable in 0.5 s.
- The domino/foundation analogy works to sell "it starts in your feet" to hip or knee sufferers.

### the_xstance_04 — "STOP CUSHIONING YOUR PLANTAR FASCIITIS" → doctor-at-podcast-mic anti-list (Body C, 9:16)
**Data:** 298 days · active · rank **4 / 352** · stable · 3 dupes · 245.8s · 110 shots · avg 2.23s / median 1.47s · VO 184 wpm in first 60 s · EN · 9:16 · ad title "$40 vs $400 same support"
**Format / angle / persona:** a white-coat "doctor" (grey hair, stethoscope, podcast mic, office) delivers "If I wanted to stop morning heel pain starting today, here's what I'd do" → 6 things he wouldn't do → "fascia collapse" mechanism → product → UGC tail. Body copy: custom orthotics $300–500 vs Xstance $40. Persona: morning heel pain, the "cushioned sneaker" crowd (Hoka/On).
**Hook (0–3 s):**
- Visual: **letterboxed**: top ~22% is a white title bar, video below. Extreme close-up of two thumbs digging into a heel/arch (deep massage, slightly gross). 2.7 s hard cut to a grey sculpted anatomical foot/ankle model with red calf muscle on a dark plinth. 5.2 s **split screen "INSTEAD, TRY THIS"**: left, a thick white foam insole under a pink sock; right, a bare heel standing on the Xstance green-rim insole (product at 5.2 s, unbranded).
- Text hook: "STOP CUSHIONING YOUR" (black) / "**PLANTAR FASCIITIS**" (red, underlined), Arial Black / Helvetica Black caps, glyph lines ≈ 59 px and ≈ 65 px, 4–14% from top on white. 2.7 s it swaps to "THIS CAN / MAKE IT **WORSE**" (red WORSE). 5.2 s "INSTEAD, TRY THIS".
- Verbal hook: "Stop cushioning your plantar fasciitis. This can make it worse and prevent you from recovering. Instead, try this." (0.00)
- Audio: male doctor VO · Hook archetype(s): contrarian enemy (the cushioning everyone buys), authority, "instead, try this" visual answer
- First hard cut at 2.67 s; 2 headline swaps in first 7 s.
**First 60 s:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–7.1 | hook | (above) | massage → anatomy sculpture → split screen | 3 title-bar headlines |
| 7.1–11.0 | promise | "If I wanted to stop morning heel pain starting today, here's what I'd do" | woman on bed rubbing heel (red glow); **"MORNING HEEL PAIN" red caps overlay**; 3D fascia; **doctor at mic** (10.0) | small captions |
| 10.9–15.7 | anti-list 1 | "I wouldn't rely on cortisone shots. They quiet pain, not the cause." | injection into heel (red glow); syringe | First, / They quiet pain, / not the cause. |
| 15.7–19.1 | anti-list 2 | "I wouldn't rely on therapy… not a muscle issue" | therapist hands on heel; doctor | |
| 19.1–22.2 | anti-list 3 | "I wouldn't ice it. Numbing pain doesn't stop damage." | foot in ice bucket (frost overlay); ice pack; foot in ice | |
| 22.2–25.7 | anti-list 4 | "I wouldn't use sleeves. Compression doesn't correct movement." | pulling on a blue compression sleeve; wrapping bandage | |
| 25.7–35.8 | anti-list 5–6 | "soft insoles or cushioned sneakers… feel good at first, sure… too much cushioning can make the foot unstable" | squishy white foam insole; **HOKA sneaker on foot**; doctor; ripping foam; runner on road; 3D fascia stress | |
| 35.8–42.3 | close loop | "Do I really need to say more? If the cause is still there, the pain always comes back." | doctor; woman walking in woods; woman on couch | |
| 42.3–60 | mechanism | "here's what's actually happening… plantar fascia acts like a strong support band… foot rolls inward… repeatedly overloaded… micro tears… Cleveland Clinic calls this overpronation" | X-ray with pen; 3D foot red fascia; bone model; leg with weight-line + red heel; 3D fascia; sculpture; **Cleveland Clinic article screenshot "What is overpronation?"** | |
**Rest by section:** 60–80 "I call it fascia collapse" → night repair / **morning re-tear** story (sleeping man, 3D tissue repair, woman waking, slipper first step, re-tear arrow, men wincing on bed edge) "Morning pain isn't the cause, it's the result". 80–92 all treatments miss the mark. 92–114 product ("That's why I recommend Xstance insoles"): stabilise arch, cushion heel, silicone layer. 114–128 proof: "300,000 people trust Xstance" (Trustpilot-style review screenshot + **6-face UGC grid**), shift workers (electrician, warehouse, linesman). 128–139 "**CONSISTENCY**" (green caps over a nurse in scrubs inserting insoles) → support in every pair. 139–157 90-day guarantee (checkout screenshot with "100% NO-RISK 90-DAY MONEY BACK GUARANTEE", pack, "you can return them within 90 days", cash) → "click below and try Xstance today". 157.7–245.8 UGC tail with green "Click Below / UP TO 55% OFF" banner.
**B-roll inventory:** talking-head (pro/doctor) ×~14 · anatomy/3D/X-ray/sculpture ×~18 · problem visualisation ×~15 · failed treatments (shots, ice, sleeves, foam insoles, Hoka) ×~12 · press/authority screenshot (Cleveland Clinic) ×1 · review screenshot + UGC grid ×2 · lifestyle workers ×~8 · product demo ×~8 · offer (checkout) ×1 · testimonial clips ×6 (tail)
**Transitions & motion:** hard cuts. Letterbox title bar for the first 7 s only. Split-screen comparison. Red glow overlays, frost overlay on ice shots.
**Caption system:** small TikTok-auto-caption look: white sentence-case sans (SF/Proxima-like medium) with drop shadow, no box, 3–6 words in 1–2 lines, glyph line ≈ 30 px, **centred ~45–50% from top** (mid-frame). Single emphasis overlays in big red or green caps ("MORNING HEEL PAIN", "CONSISTENCY").
**Pacing:** 0.9–2.5 s shots, doctor shots 1.5–2.4 s, the shortest body (157 s) of the long-forms.
**Offer & CTA:** guarantee 139 s, CTA 155.6 s, no % in the body. "UP TO 55% OFF" only in the tail banner. The ad copy carries the "$40 vs $400" anchor.
**Steal this:**
- "Stop [the thing they already bought]": "STOP CUSHIONING YOUR PLANTAR FASCIITIS". The enemy is soft/memory-foam shoes, which is exactly WearOrtho's chance to sell *support + comfort*.
- "If I wanted to fix X starting today, here's what I'd do… I wouldn't…" anti-list from a credentialed speaker. Each "I wouldn't" is a 3 s retention beat with its own B-roll.
- Show a third-party authority screenshot (Cleveland Clinic page) on the mechanism claim.

### the_xstance_05 — "This is the Plantar Fasciitis life hack I wish I knew sooner" (hammer on sole) → Body C, second doctor
**Data:** 242 days · active · rank **5 / 352** · stable · 4 dupes · 300.1s · 111 shots · avg 2.70s / median 1.50s · VO 195 wpm in first 60 s · EN · 9:16
**Format / angle / persona:** new 12.7 s hook + 04's doctor script re-shot with a **different presenter** (grey-haired man in a dark button-down, same podcast-mic set-up, open-plan office). Longer UGC tail (134 s).
**Hook (0–3 s):**
- Visual: a bare sole lying on a desk, marked in pen with 3 circled ✗ points joined by lines. A hand **taps/hammers the sole with a claw hammer** (motion blur on each strike, 0–3.9 s).
- Text hook: "This is the Plantar Fasciitis / life hack I wish I knew sooner". Black bold sans on a white rounded box (TikTok-native), 2 lines, glyph ≈ 35–40 px, box ~22–31% from top.
- Verbal hook: "This is the plantar fasciitis life hack I wish I knew sooner." (0.00)
- Audio: male VO · Hook archetype(s): "life hack I wish I knew sooner", absurd/shock visual (hammer), pattern interrupt
- First hard cut at 3.93 s.
**First 60 s:** 3.9 man doing wall stretch "Doing this" → 5.9 man with ice pack under feet "Doing this" → 8.1 bright orange chunky cushioned sneaker "And this one?" → 10.4 **black text card** "Avoid those traps / and / do this instead" (white bold, centred) → 12.7 woman on bed rubbing heel (red glow) "If I wanted to stop" → 13.9 "MORNING HEEL PAIN" red overlay → 14.8 3D fascia "starting today," → 15.7 doctor #2 "here's what I'd do" → 16.6–41.4 the anti-list exactly as 04 (shots, therapy, ice, sleeves, soft insoles, Hoka) → 41.7–60 "Do I really need to say more?" + mechanism start (X-ray, fascia band).
**Rest by section:** as 04 (+5.6 s): mechanism / fascia collapse → product → 300,000 → consistency → 90-day guarantee (green "MONEY BACK 100% GUARANTEE" seal on cash) → "click below and try Xstance today" (165.5 s) → **165.7–300 UGC tail** (5 selfie testimonials 19–39 s each, e.g. "So my name is Casey… game changer") with a **mid-frame green rounded box "UP TO 55% OFF / Tap below to try them risk-free for 90 days"** (~65–72% from top) and small white captions above it.
**B-roll inventory / Transitions / Caption system:** as 04 (small centred white shadow captions ≈ 30 px; black text card transition; red glows).
**Pacing:** 4 setup shots of 2.0–3.9 s before the doctor appears. The tail is 45% of runtime.
**Offer & CTA:** guarantee ~150 s, CTA 163 s, 55% + "risk-free for 90 days" in the tail box.
**Steal this:**
- "Doing this… / Doing this… / And this one?" → black card "Avoid those traps and do this instead". A 10 s triple-mistake montage before the expert speaks.
- Absurd-but-relevant demo as thumb-stop (hammer on a marked sole). For WearOrtho: a marker-drawn bunion or heel spot on a foot.
- **Cast the same script with two different experts** to double the creative pool (04 + 05 both rank top 5).

### the_xstance_06 — "Watch my PLANTAR FASCIITIS recovery" Day 1/7/14 split screen → woman's story (Body B)
**Data:** 370 days · active · rank **6 / 352** · stable · 3 dupes · 378.9s · 161 shots · avg 2.35s / median 1.77s · VO 177 wpm in first 60 s · EN · 4:5
**Format / angle / persona:** before/after recovery hook → plus-size woman (40s–50s, work shoes, concrete floors, mum) tells Body B → UGC tail. **Closest persona match to WearOrtho** (women, on feet all day, family stakes).
**Hook (0–3 s):**
- Visual: **side-by-side split screen** (thin white divider). Left: the woman in a grey tee and grey shorts limping down a dirt path with a red heel-pain icon on her foot. Right: the same woman in a navy tee and turquoise shorts striding confidently along a wooden deck with a US flag behind. Both walk toward camera. 2.6 s hard cut to full-frame "Day 1: Struggling to walk." (gravel yard, slow gait).
- Text hook: "Watch my / **PLANTAR FASCIITIS** / recovery". Black bold small lines (≈ 35 px) + big red heavy caps (≈ 58 px) on a white rounded box, 5–16% from top. Day labels: black text on small white TikTok boxes at ~75% from top.
- Verbal hook: "Watch my plantar fasciitis recovery. This is me on day one, day seven, and on day 14." (0.00)
- Audio: female first-person VO · Hook archetype(s): before/after transformation, time-stamped progress (Day 1/7/14), "watch my…" vlog framing
- First hard cut at 2.64 s; white flash transitions at 4.3 s and 5.6 s.
**First 60 s:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–2.6 | hook | "Watch my plantar fasciitis recovery" | split before/after | headline box |
| 2.6–7.1 | progress proof | "This is me on day one, day seven, and on day 14" | Day 1 limping on gravel → white flash → Day 7 walking dog on a path → white flash → Day 14 playing with dog on deck | "Day 1: Struggling to walk." / "Day 7: Walked three blocks." / "Day 14: Pain completely gone." |
| 7.1–8.2 | bridge | "Here's how I did it." | **black card** | "Here's how I did it…" (white bold, centred) |
| 8.2–14.8 | backstory | "heel pain from my work shoes for nearly a year… plus-size woman walking all day on concrete floors" | TH in kitchen; limping on gravel with red heel icon; burgundy leggings + black sneakers at work; TH; legs walking in shop aisle; POV sneaker on concrete | Oswald 2-line captions |
| 14.8–23.9 | first attack | "excruciating… sharp stabbing pain put me out of commission for a month" | on sofa with **yellow lightning + red glow**; TH; bare feet on bed edge → **red lightning bolt up the leg**; limping on dirt path with red icon | |
| 23.9–31.4 | tried everything | "kept coming back… past 14 months I have tried everything" | TH; pink sneakers on path; TH; walking gravel; **3-panel collage** (massage ball, foam roller, massager) | "I have tried EVERYTHING" |
| 31.4–42.6 | emotional cost | "cancel our family trip to Disneyland… our kids had been looking forward to that" | TH; passport + tickets with red CANCELED stamp; Disneyland castle; TH; boy close-up; bored girl | |
| 42.6–54.5 | identity | "Is this what my life is going to be like? Always in pain, frustrated, a burden… I vowed to find a solution" | TH with **floating "?" graphics**; TH; slumped on sofa; TH | "Is this what my life is going to be like?" |
| 54.5–60 | diagnosis | "A podiatrist diagnosed me with plantar fasciitis… ligament… inflamed" | doctor in white coat; fascia overlay with red target; 3D foot; 3D blue fascia | |
**Rest by section:** 60–106 standard advice + failed fixes (rest, icing, stretching, orthopedic shoes, braces, cortisone, custom orthotics; On Running sneakers "I tried highly-rated orthopedic sneakers with cushioned soles"; Amazon screenshot "I bought five different brands"; red ✗ over flimsy/rigid insoles; night splint; painkillers; "$600 for the custom orthotics" with a cash pile and big yellow "600"; praying hands "hoped for a miracle"). 106–138 search online (laptop, forums) → testimonial discovery → "Xstance Insoles 2.0… with foot and ankle surgeon Dr. Gregory Pomeroy". 138–180 features (presenter woman holding the insole, heel-cup diagram, feature icon bubbles). 180–200 "I visited their official website" (website + review card) → **90-day** → "NO RISK!" → "They shipped from Utah, got them within 2 days" (warehouse, courier). 200–250 results (swapped insoles in work shoes → "felt comfortable right away" → end of shift → next day → week) → bought 3 more pairs. 250–288 mechanism recap + "If Xstance insoles are still available, get yours right now". 288–378.9 UGC tail with green banner.
**B-roll inventory:** talking-head (customer, kitchen) ×~40 · re-enactment of narrator (limping, sofa, Day 1/7/14) ×~15 · stock emotional ×6 · anatomy ×5 · failed fixes ×~15 · website/review screenshots ×3 · product demo ×~15 · testimonial clips (tail) ×4
**Transitions & motion:** hard cuts + white flashes between "Day" clips + black text card. Graphics: red heel icon, lightning, CANCELED stamp, floating "?" marks, $600 cash pile, 3-panel collage.
**Caption system:** Oswald Bold white with black stroke/shadow, **2-line phrases** (4–8 words), glyph line ≈ 55–65 px, ~77–87% from top. "EVERYTHING" and "NO RISK!" set in caps.
**Pacing:** hook 2.6 s, progress clips 1.3–1.7 s, body median 1.8 s, TH max ~4.4 s.
**Offer & CTA:** guarantee ~184 s, multi-pair seeded at ~244 s ("bought three more pairs"), CTA ~284 s, 42%/24H in the tail banner.
**Steal this:**
- A **side-by-side before/after walking split** of the same woman, plus a "Watch my [condition] recovery" box. It is instantly understandable and very hard to scroll past.
- Time-stamped progress labels ("Day 1: Struggling to walk. / Day 7: Walked three blocks. / Day 14: Pain completely gone.") with white-flash transitions, then a "Here's how I did it…" black card.
- Plus-size, work-shoes, mum persona with a family-stakes beat. This maps directly to WearOrtho's nurse and teacher personas.

### the_xstance_07 — "PLANTAR FASCIITIS HEALING JOURNEY: This is James's foot 4 weeks ago" → men's story (Body B, 9:16)
**Data:** 114 days · active · rank **7 / 352** · stable · 13 dupes · 391.4s · 142 shots · avg 2.76s / median 1.70s · VO 229 wpm in first 60 s · EN · 9:16 · ad title "Stop stretching. Do this instead."
**Format / angle / persona:** third-person before/after hook ("James's foot") → first-person story by a white-bearded man in a red plaid shirt (Six Flags instead of Disneyland). Persona: 300-lb work-boot man, 55+. The ad copy carries a separate nurse testimonial ("Sarah, 44, nurse").
**Hook (0–3 s):**
- Visual: 0–1.9 a man in a black work jacket and cap walks stiffly along a snowy garden path toward camera, with a **hand-drawn red circle** tracking his right foot. 1.9 cut to the same man in a red plaid shirt walking briskly down a carpeted hallway ("And this is now."). 2.9 cut back to the garden, walking freely past a pergola. Note: the hook man and the later talking head look similar but are not obviously the same person (likely assembled footage).
- Text hook: title bar "**PLANTAR FASCIITIS**" (red Arial Black caps on white) / "**HEALING JOURNEY**" (black caps on white), two stacked white boxes, glyph ≈ 50–54 px, 5–11% from top. Word captions centred ~29%: "This **is** James's **foot** 4 **weeks** ago." (karaoke red) → "And **this** is **now.**" (yellow) → "**His** Plantar Fasciitis" (green).
- Verbal hook: "This is James's foot four weeks ago, and this is now. His plantar fasciitis 100% healed." (0.00) → 5.7 "Here's what he did."
- Audio: male VO · Hook archetype(s): before/after with tracked circle, named third-party proof, time-bound (4 weeks), "here's what he did" open loop
- First hard cut at 1.9 s; 2 cuts in first 3 s.
**First 60 s:** 5.8–6.9 **black card "Here's what he did."** → 6.9 TH (white beard, plaid, living room with flowers) "I started dealing with crippling heel pain from my work boots" (walking path with red heel glow; muddy work boots) → 10.0 "I'm a big guy… concrete floors take a real toll" (walking in boots; man on sofa with red foot) → 14.8 "felt like landing on a nail" (bare foot over a **bed of nails**) → 19.4–28.9 "calmed down… but after a long shift it always came back… tried every trick… nothing" (walking in snow, rubbing foot, hallway, walking away) → 26.3–36.5 "planned a day at Six Flags… had to back out… my kids… their faces" (TH; girl on suitcase; boy sad) → 36.7–46.8 "Is this really my life now? Always hurting… slowing everyone down" (TH eyes closed; **B&W re-enactment** in blue plaid; man on stairs gripping rail) → 46.8–60 "went to the foot doctor… plantar fasciitis… feet collapse inwards… unnatural tension" (doctor in white coat; X-ray with gloved pointer; 3D foot red ligament; 3D foot on insole; skeleton model; weight-line leg with red heel; glowing X-ray shoe).
**Rest by section:** 60–92 advice + failed fixes (ice, stretch, better shoes, night brace, cortisone, custom insoles; On Running "those thick cushioned shoes for one day"; Amazon screenshot "I ordered a bunch"; soft ones ✗, too stiff ✗; splint) → 92–139 desperate research → "everyone was talking about Xstance Insoles 2.0" → 139–176 product: "made by [lab scientist at a scan screen] and built for folks who stand all day" (split screen workers) → "you just drop them in and go" → **6-face UGC grid** "Everyone said…" → Triple Support System (green numbered "2" overlays per feature) → website PDP screenshot ($49.95 → $29.95) → 90-day (cash, tape gun "send them back") → 176–257 results + "bought five more pairs… in all of my shoes" → mechanism recap (support holds, cushioning "takes the hit", 3D heel heal) → "So don't wait… If the Xstance insoles are still in stock, get a few pairs now" (PDP, green insoles on grass) → **257–391 UGC tail** (134 s) with mid-frame green "UP TO 55% OFF / Tap below to try them risk-free for 90 days" box.
**B-roll inventory:** talking-head (customer) ×~35 · B&W/alt-wardrobe re-enactment ×5 · problem visualisation (bed of nails, red glows) ×~15 · stock emotional ×4 · anatomy/X-ray ×~8 · failed fixes + Amazon screenshot ×~12 · lab/scientist stock ×1 · UGC 6-face grid ×1 · PDP/website screenshots ×3 · product demo ×~15 · testimonial clips ×5 (tail)
**Transitions & motion:** hard cuts, black text card, tracked red circle (hand-drawn style) in the hook, green numbers per feature, split screens, 6-up grid.
**Caption system:** Oswald Bold white with black stroke, 1–3 words, glyph ≈ 60–75 px, lower third (~78–85%). Karaoke colour on the active word in the hook (red / yellow / green).
**Pacing:** hook 1.9 + 1.0 + 2.9 s, body median 1.7 s, TH holds up to 5.2 s on emotional lines.
**Offer & CTA:** guarantee ~170 s, multi-pair ~227 s, CTA ~253 s, 55% in the tail box.
**Steal this:**
- Use a "[CONDITION] HEALING JOURNEY" two-tone title bar + "This is [Name]'s foot 4 weeks ago / And this is now" + a red circle tracking the foot.
- Use a black "Here's what he/she did." card as the hinge between proof and story (also used in 06).
- Show a 6-face UGC grid on "everyone was talking about…".

### the_xstance_08 — "Don't stretch your calves if you have PLANTAR FASCIITIS" → Body A (01 minus the myth list)
**Data:** 366 days · active · rank **8 / 352** · stable · 4 dupes · 301.4s · 144 shots · avg 2.09s / median 1.46s · VO 211 wpm in first 60 s · EN · 4:5
**Format / angle / persona:** **hook-swap of 01**. A single "don't do X" myth (3.7 s) replaces 01's 11 s three-myth list. Body = 01 from "Most people don't realize this…" (01's 11.2 s maps to 08's 3.7 s).
**Hook (0–3 s):**
- Visual: a woman (long hair, denim shorts, dark tee) doing a calf stretch against a white door in a home hallway, static camera (0–3.7 s).
- Text hook: "Don't stretch your calves / if you have / **PLANTAR FASCIITIS**". Black bold + red heavy caps on a white rounded box, **mid-frame (~38–57% from top)** over her torso, glyph ≈ 35 px black / ≈ 55 px red. "Do this instead!" sub-pill at 3.0 s.
- Verbal hook: "Don't stretch your calves if you have plantar fasciitis, do this instead." (0.00)
- Audio: presenter VO · Hook archetype(s): "don't do X" warning on a common remedy
- First hard cut at 3.74 s.
**First 60 s:** identical to 01's 11.2–67.5 s (symptoms → NOT aging → truth → mechanism → rubber band → re-agitate → "Not because they're getting older…"), shifted −7.5 s.
**Rest by section:** as 01 (−7.5 s): product reveal ~82 s, Triple Support, guarantee, multi-pair, 42% off ~187 s, CTA, UGC tail 219–301 s.
**B-roll / Transitions / Captions / Pacing / Offer:** as 01.
**Steal this:**
- One myth beats three? Here no: 01 (3 myths, 11 s) is rank 1 and 08 (1 myth, 3.7 s) is rank 8. With an older audience, a **numbered myth list can out-perform a faster single warning**. Test both.
- Put the headline box mid-frame over the action (not the top 15%) for a 4:5 placement.
- Freeze a winning body and test 3–4 s "don't do [remedy]" hooks on it.

### the_xstance_09 — "HOW TO: HEAL PLANTAR FASCIITIS (WORKS EVERY TIME)" infographic → woman's story (Body B)
**Data:** **561 days** (longest-running Xstance in set) · active · rank **9 / 352** · stable · **36 dupes** · 373.1s · 155 shots · avg 2.41s / median 1.81s · VO 174 wpm in first 60 s · EN · 4:5
**Format / angle / persona:** Pinterest-style "how-to" infographic thumb-stop, then 06's woman's story without the recovery montage.
**Hook (0–3 s):**
- Visual: a static pastel-pink graphic. "HOW TO:" / "HEAL **PLANTAR FASCIITIS**" / "(WORKS EVERY TIME)" in condensed caps (Bebas Neue/Oswald-like, the key words bold black), with a **2×3 icon grid** of flat illustrations: Rest And Avoid Overuse, Wear Supportive Footwear, Stretch Your Calves, Apply Ice To Affected Area, Support Your Arches, Educate Yourself. Glyph lines ≈ 50 / 79 / 50 px, 3–23% from top. At 2.25 s a **zoom-blur push into the "Wear Supportive Footwear" icon** transitions to the woman talking head (2.3 s). Product not until ~133 s.
- Verbal hook: "If you have plantar fasciitis, watch this." (0.00) → "I've been dealing with heel pain from my work shoes for nearly a year now." (2.4)
- Audio: female VO · Hook archetype(s): educational infographic / save-able checklist, "watch this" call-out
- First hard cut at 2.3 s (zoom-blur).
**First 60 s:** 06's backstory from "I've been dealing with heel pain…" (06's 8.2 s → 09's 2.3 s): work shoes, plus-size, concrete floors, first attack (lightning), "tried EVERYTHING" collage, Disneyland CANCELED, kids, "Is this what my life is going to be like?", podiatrist, fascia anatomy, standard advice list (rest, icing, stretching, orthopedic shoes, braces, cortisone, custom orthotics) at 55–66 s.
**Rest by section:** as 06 (−5.9 s): failed fixes → discovery → features → 90-day → results → "bought 3 more pairs" → CTA ~278 s → UGC tail 282–373 s.
**B-roll / Transitions / Captions / Pacing / Offer:** as 06 (Oswald 2-line captions ≈ 55–65 px at 77–87%).
**Steal this:**
- An **infographic hook that looks like a saved Pinterest/Facebook post** ("HOW TO: HEAL [X] (WORKS EVERY TIME)" + 6 icons). It reads as content, not an ad, and older audiences save and share these. One icon ("Wear Supportive Footwear") is the bridge to the product.
- A zoom-blur push into the relevant icon gives a clean pattern-break transition into the story.
- 36 dupes and 561 days: the most-iterated Xstance hook. Keep the format and rotate the icons and colours.

### the_xstance_10 — Black Friday "Our craziest 24-hour sale is here" 28 s promo
**Data:** 322 days · active · rank **10 / 352** · stable · 8 dupes · 27.8s · 20 shots · avg 1.39s / median 1.13s · VO 170 wpm · EN · 9:16
**Format / angle / persona:** short sale-urgency promo: product insertion B-roll + multi-pair social proof + condition list + "price goes back up". Ad copy: Black Friday 55% off, "sold out in 6 hours last year", "most customers order 3–4 pairs".
**Hook (0–3 s):**
- Visual: 0–0.77 a hand lifts an Xstance green insole out of a blue/yellow Hoka. 0.77 top-down on two Hokas with Xstance insoles inside. 1.4 macro of a hand flexing the black/green insole. 2.5 a man's hands sliding the insole into a grey sneaker on a window ledge (city view). Product in frame 1.
- Text hook: "OUR CRAZIEST 24-HOUR / SALE IS HERE AND THINGS / ARE FLYING OFF SHELVES". Black bold caps on white rounded box (TikTok-native), 3 lines, glyph ≈ 35 px, ~27–36% from top. Persists 0–4.7 s.
- Verbal hook: "Black Friday savings are live. Xstance insoles are up to 55% off." (0.00)
- Audio: female VO over a music bed · Hook archetype(s): sale announcement, scarcity ("flying off shelves"), product-in-hand
- First hard cut at 0.77 s; 3 cuts in first 3 s.
**Beat map:**
| t | beat | VO (short) | visuals/B-roll | on-screen text |
|---|---|---|---|---|
| 0–4.7 | hook / offer | "Black Friday savings are live… up to 55% off" | 4 insertion/handling shots incl. **nurse in blue scrubs inserting insole** (3.5 s) | sale box |
| 4.7–9.2 | social proof | "People are grabbing multiple pairs because this is our biggest discount ever" | woman in kitchen holding insoles; older man with insole; grey-haired woman fanning 3 pairs | "People are grabbing multiple pairs" / "because this is our BIGGEST discount ever." |
| 9.2–17.1 | conditions | "plantar fasciitis, heel pain, Achilles tightness, overpronation… travels into knees or hips" | red-tinted soles; hand on heel (red glow); red target on Achilles; heel with red tilt line; 3D blue body with red knees/hips | small white-box captions |
| 17.1–21.1 | mechanism | "Xstance can make a REAL difference with its Triple Support System" | woman with 3 pairs; split product/foot | |
| 21.1–24.5 | urgency | "Don't wait. Once the sale ends, the price goes back up." | woman "Don't wait!"; insoles on wood; insoles on road with flying cash | |
| 24.5–27.8 | end card | "Take advantage of your 55% off now." | mint-green end card: XSTANCE wordmark, insole pair packshot, red "55% off" burst badge, footprint pattern | — |
**B-roll inventory:** product handling/insert ×5 · testimonial-style holders ×4 · problem visualisation ×4 · anatomy ×1 · offer/price card ×1 · stock (cash) ×1
**Transitions & motion:** 100% hard cuts at ~1.1 s. Red overlays. Packshot end card with badge.
**Caption system:** small TikTok-native white rounded boxes with black sentence-case text (≈ 28–32 px), 1–2 lines, placed near the subject (35–75%). CAPS emphasis ("BIGGEST", "REAL").
**Pacing:** 0.7–2.5 s shots, end card 3.4 s.
**Offer & CTA:** 55% in the first VO line (0–4.6 s), multi-pair at 4.8 s, "price goes back up" at 22 s, end card.
**Steal this:**
- The **sale-announcement hook** box ("Our craziest 24-hour sale is here and things are flying off shelves") over product insertion B-roll, with the offer in the first VO line.
- "People are grabbing multiple pairs" is a social-proof framing for the bundle.
- Include a nurse-in-scrubs insertion shot even in a generic promo. Persona cues can be single 1 s shots.

---

## Batch patterns

### Stepprs (10 ads, 28–56 s, mean 41.6 s, all 9:16)
- **There are 4 creative families, heavily recycled.** Egg-drop test (01, 05, 06, 07 = 4/10, plus egg clips reused inside 08 → 5/10 use the egg footage). POV-caption + founder sale montage (02, 09 share an identical 46 s body). Step-in meme + show-and-tell (03 is a 1.9 s-tighter re-cut of 10). Single creator review (04). AI-anatomy timeline (08).
- **Why they last 384–472 days (01, 04, 05, 10).** (1) The hook is a **language-free physical demo** (eggs breaking, foam squashing) that needs no claim and can't go stale. (2) Everything verbal is a **modular ~20 s VO block** added late, so it can be re-voiced per persona (07 = steel-toe / concrete floors on 01's identical take) and pointed at persona landing pages (03 long-shift, 07 steel-toe, 08 neuropathy). (3) The concept is **reshot in new locations** (3 different kitchens/flats for the egg test) instead of being replaced. (4) The offer is evergreen ("up to 60%", "90-day money back", never a date). (5) Each entry collapses **13–25 near-duplicate variants**, so the brand is constantly refreshing delivery under the same idea. (6) Everything is shot on a phone in real homes, so it looks native, not like an ad.
- **Delayed VO is the norm:** 8/10 have no VO for the first ≥2 s and 6/10 for ≥7 s (01/07 12.6 s, 05 23.1 s). Only 04 and 08 open with a spoken line. The egg ads also have **no on-screen text until the VO starts**.
- **Product in frame by 3 s in 8/10** (03, 04, 10 at frame 1; 01, 06, 07 at 1.75 s edge-of-frame; 02, 08 at 2.5 s). The exceptions are 05 (~8 s) and 09 (10.3 s). 09 is the lower-ranked twin of 02 (rank 23 vs 3).
- **Cut rate is bimodal:** long single takes (01, 05, 06, 07 avg 4–6 s, with a first cut at 24–40 s) or 1.0–1.5 s median montages (02, 04, 08, 09). 6/10 have zero hard cuts in the first 3 s. Motion inside the frame does the work.
- **Captions:** 5/10 use **karaoke Montserrat ExtraBold ALL CAPS, white, active word on a solid brand-orange box**, glyph ≈ 40–46 px, centred 49–58% from top. 2/10 use white caps with black outline at 62–64%. 2/10 use lowercase TikTok-classic 1–2-word captions ≈ 41 px at 61–64%. 1/10 uses lowercase + CAPS keywords at 66–70%.
- **Hook text, where present (5/10), is TikTok-native:** white rounded boxes with black text (03, 04, 10) or TikTok-classic white-with-outline (02, 09), placed 16–31% from top, with emoji in 4/5.
- **Comparison vs a named competitor in 6/10:** Nike insoles in the egg test (4) and Amazon screenshots of Dr. Scholl's with prices (02, 09).
- **Offer:** "up to 60% off" in 9/10 (04 uses "~$20 vs hundreds on shoes"). 90-day money-back spoken in 6/10. An animated **"SHOP NOW!" pill + cursor tap** CTA card in 4/10 (the egg family). Fake urgency ("only two days left until we have to sell everything") on 02/09 has run for 132 days.
- **Brand-colour discipline:** orange insole, orange caption box, orange pouches, orange CTA backdrop. The product is recognisable in a 0.5 s glance even on a cluttered counter.
- **End buttons:** 2/10 add a post-CTA payoff shot (06 dog eating the egg, 07 egg-smeared insoles). 01 ends on 3.2 s of black, which is wasted.

### The Xstance (9 long-forms 245–391 s, mean 325 s ≈ 5.4 min; 1 × 28 s promo)
- **3 script bodies × many hooks:** Body A presenter explainer (01, 03, 08), Body B first-person customer odyssey (02, 06, 07, 09), Body C doctor at podcast mic (04, 05). Hook-only swaps: 08 vs 01, 09 vs 06, 05 vs 04. Body re-skins: 03 = Body A for hips. Re-casts: 05 = Body C with a second doctor, 07 = Body B with a different man.
- **10/10 have a text hook in frame 1. In 7/10 (01–06, 08) it is spoken verbatim as the first VO line.** 07, 09 and 10 pair a title or graphic with a different spoken line. Style: white rounded box/pill with black bold sans, plus a **red keyword line in 6/10** ("making the pain worse", "HIPS HURT", "PLANTAR FASCIITIS", "WORSE"). Position: top 4–16% in 7/10, mid-frame in 08, 10 and 05.
- **Hook archetypes:** "don't do X / stop X → do this instead" in 6/10 (01, 02, 03, 04, 05, 08). Before/after transformation in 2/10 (06 split screen + Day 1/7/14, 07 "James's foot 4 weeks ago / now"). Educational infographic in 1/10 (09, the oldest at 561 days with 36 dupes). Sale announcement in 1/10 (10).
- **First hard cut at 1.9–3.9 s in all 10.** 31–41 shots in the first 60 s (~1.7 s average). Body median 1.4–1.8 s. Talking-head shots are capped at ~2–5 s and immediately covered with illustrative B-roll.
- **The product is hidden for 78–139 s in 8/9 long-forms** (only 04 shows it at 5 s in a split screen). They sell the mechanism and the failed alternatives first, which is the advertorial/VSL logic. The landing page is an article (`/article/5-reasons`).
- **Every long-form uses the same skeleton:** symptom call-out → "it's NOT aging" → mechanism (overpronation / "fascia collapse") with 3D anatomy (10/10 use anatomy/X-ray) → **failed-fixes montage with red ✗ stickers** (9/9) → product + "Triple Support System" (3 named parts) → skeptic/objection → 90-day guarantee (10/10) → **multi-pair logic** (10/10: "one pair per shoe" / "I bought 3–5 more pairs" / "people are grabbing multiple pairs") → offer + scarcity → CTA.
- **Authority layering:** suited presenter (3), white-coat doctor at mic (2), a named "foot & ankle surgeon Dr. Gregory Pomeroy" (4 story ads), a Cleveland Clinic page screenshot (04/05), the "Xstance Insoles 2.0" name.
- **Emotional-cost beat** in 4/10 (story family): cancelled Disneyland/Six Flags trip with red "CANCELED" stamps, sad-kid stock, "Is this my life now?" with floating "?" or B&W re-enactment.
- **Caption systems by family:** grey translucent rounded box + white geometric sans, ≈ 45–50 px at 75–87% (Body A). Oswald Bold white with black stroke, ≈ 55–90 px, lower third, with **colour-coded keywords** (red pain / yellow emphasis / green relief) (Body B + every UGC tail). Small centred TikTok-style white shadow text ≈ 30 px at ~45–50% (Body C).
- **UGC review tail after the CTA in 9/9 long-forms**, 80–90 s (7) or 134 s (05, 07): 4–6 phone-selfie testimonials held 9–39 s each, under a **persistent green offer banner** ("Click Below ↓ UP TO 42% OFF FOR 24H" bottom 85–97%, or a mid-frame "UP TO 55% OFF / Tap below to try them risk-free for 90 days").
- **Offer timing:** the discount is spoken late (42% at 177–194 s in Body A) or **never spoken** (Body B/C: only "if they're still available" + the tail banner). The short promo (10) puts 55% in the first line.
- **Graphics kit (reused across all):** red heel-pain circle icon, red/orange glow on joints, yellow lightning, red ✗ circles, red→green alignment line on the heel, 42% yellow badge, checkout/PDP screenshots, Amazon competitor screenshots (4/10), 2–3 panel split screens, 6-face UGC grid, black text cards ("Here's how I did it…", "Avoid those traps…").

---

## What WearOrtho should take

1. **Delayed-hero torture test** (stepprs_01, 05, 06): one handheld POV take where a generic flat shoe and a named competitor (e.g. Skechers) "fail" first, with OrthoStretch placed in frame from ~2 s but tested last (egg-under-the-heel stomp, heavy book drop, or palm press showing rebound). Use no text and no VO for the first 8–12 s, only natural sound. Then add karaoke captions (Montserrat ExtraBold caps, ≈ 40–46 px, mid-frame, active word on a ComfortWear brand-colour box) and a 20 s VO. End with a "button" shot (pet, grandchild, blooper) after the CTA (stepprs_06).
2. **One demo, many voices** (stepprs_07, plus persona LPs on 03/08): keep the winning footage frozen and re-record only the use-case line ("perfect for 12-hour hospital shifts" / "for teachers on their feet all day" / "for airport walking"). Insert one persona B-roll shot exactly on that phrase and send each version to a persona landing page.
3. **POV result-caption hook with the shoe reveal by 2.5 s** (stepprs_02 beats its own hook-swap stepprs_09, rank 3 vs 23): a nurse at her front door slips off her shoe and shows the footbed. TikTok-classic white text with outline, ≈ 46 px, 20–28% from top: "my 12 hour shift really just felt like 2 😮‍💨🙏 / Money well spent 👏". Keep the POV hold ≤ 7 s.
4. **Meme labels over a step-in squish** (stepprs_03/10, and stepprs_04's headline): shin-height shot of two feet, with TikTok white boxes over each leg: "You after a 12-hr shift 🤮" / "Your feet in OrthoStretch 😮‍💨". Add an audible "oh my…", then "I was doing it in *this*" (old flat shoe reveal) at ~2.6 s.
5. **Myth / "don't do X → do this instead" pill headline** (the_xstance_01, 02, 03, 08): white rounded pill, black bold line + red second line, glyph ≈ 55–60 px, top 4–15% (mid-frame for 4:5). Stack numbered myths as smaller sub-pills, and speak the headline verbatim as the first VO line. WearOrtho versions: "3 BUNION MYTHS making the pain worse", "Don't ice your plantar fasciitis. Do this instead!", "Stop resting if your HEELS HURT".
6. **Make cushioning the enemy and position "support + comfort"** (the_xstance_04): a white letterbox title bar in Arial Black caps, "STOP BUYING SOFT SHOES FOR YOUR / PLANTAR FASCIITIS" (red, underlined). At ~5 s, a split screen "INSTEAD, TRY THIS": foam sneaker sinking vs OrthoStretch heel cup. Follow with an "If I wanted to fix morning heel pain starting today, here's what I'd do… I wouldn't…" anti-list from a credentialed speaker (podiatrist or nurse), one 3 s B-roll per "I wouldn't".
7. **Side-by-side before/after walk + day labels** (the_xstance_06, 07; timeline logic from stepprs_08): the same woman limping (left) vs striding (right) with "Watch my PLANTAR FASCIITIS recovery". Then "Day 1: struggling to walk / Day 7: walked three blocks / Day 14: …" labels with white-flash transitions, and a black "Here's how I did it…" card before the story. Optional: an orange→green glow overlay on the foot to show pain becoming relief. (Keep the results language within claims we can substantiate.)
8. **Colour-coded word captions for the story section** (the_xstance_02, 06): Oswald Bold white with black stroke, lower third (~80–88%), with **red for pain words, green for relief/product words, yellow for emphasis**. For a 45–75 audience prefer the 2-line phrase version (06, ≈ 55–65 px glyph) over 1-word karaoke.
9. **"HOW TO: RELIEVE PLANTAR FASCIITIS (WORKS EVERY TIME)" infographic hook** (the_xstance_09, 561 days, 36 variants): a pastel save-able card with a 2×3 icon grid (rest, ice, stretch, *wear supportive shoes*, arch support, educate yourself). Zoom-blur into the "supportive shoes" icon at ~2.3 s, then cut to the testimonial or demo. It reads as content and earns saves and shares from older viewers.
10. **Failed-fixes montage + price anchor** (the_xstance_02/06 and stepprs_02): ice packs, night splints, cortisone, "five brands from Amazon" (screenshot with narrator picture-in-picture), "$600 custom orthotics" (cash pile with a big yellow "600"), each with a red ✗ sticker at 0.8–1.5 s per shot. Then OrthoStretch as the answer at a fraction of the price.
11. **Post-CTA UGC review reel under a persistent offer banner** (the_xstance_01, 04, 05): after the main CTA, run 3–5 real customer selfies (9–30 s each) with Oswald captions and a fixed green bottom band, "Click Below ↓ / UP TO X% OFF – 90-DAY TRIAL" (85–97% from top), or a mid-frame rounded box "Tap below to try them risk-free for 90 days". This is cheap to add to any long-form and extends watch time into a second CTA zone.
12. **Multi-pair framing as logic, not just a discount** (the_xstance_01, stepprs_03, the_xstance_10): "If you only have one comfortable pair, your feet are unsupported the rest of the day: work, home, errands. That's why we made the 2-pair bundle." Seed it earlier with "I got one for every pair I own" and use "People are grabbing multiple pairs" over 3 quick "customer holding 2–3 pairs" shots.

Compliance note: several competitor lines would be risky for WearOrtho to copy literally ("100% healed", "feel your toes again", neuropathy "without pills or surgery", "fixes plantar fasciitis for good"). Copy the structures, not the medical claims.
