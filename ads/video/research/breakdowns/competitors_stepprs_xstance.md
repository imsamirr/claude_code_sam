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
- Audio: VO (male, steady) over a soft bed · Hook archetype(s): condition call-out + gross-out anatomy + "this is what would happen" open loop + time-bound promise
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

