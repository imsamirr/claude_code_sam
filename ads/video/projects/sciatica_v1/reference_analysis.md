# Reference study: "Best Pain Relief Shoe 2026!" (HIKE / HF Flow, Atria m1130233342912462)

- **Specs:** 208.98 s · 720×1280 · 101 hard cuts (avg 2.07 s, median 1.63 s) · first cut 1.53 s · VO 647 words ≈ 186 wpm, one female "clinician" voice.
- **Running:** live 31 days; rank 3 of 308 for this advertiser.
- **Method:** I viewed every second (1 fps sheets), checked key frames at full resolution and transcribed the VO. Folder: `reference/` (`dense/`, `full/`, `ref/cuts.json`, `ref/transcript.txt`).

## 1. Structure (what plays when)

| Time | Beat | VO (short) | Picture |
|---|---|---|---|
| 0.0–1.5 | Symptom hook | "If you have sciatica…" | Real gym clip of a man bending to a barbell, with an **AI anatomy layer** (glute and hamstring muscles in red, a glowing yellow-to-blue nerve running down the leg). **Red box, white caps "IF YOU HAVE SCIATICA"**, mid-frame (~45 %). |
| 1.5–4.1 | Pattern interrupt | "…shoes you should never wear" | AI "monster shoe" with teeth held up over grass. Serif white "TOP 3 SHOES / YOU SHOULD / NEVER" (red) builds line by line. |
| 4.1–6.1 | Escalate | "They just make the problem worse" | Man grimacing with a **red glow on his foot**, then a red X-ray foot close-up. White box at the top: "They just make the problem / WORSE" (red box). |
| 6.1–14.4 | Authority + audience | "3 shoes I'd never recommend… women over 60" | Clinician in a lab coat in a lab (name embroidered). Older woman in pyjamas struggling to stand by stairs. Walker and new sneakers walking. 85-year-old with a walker in a shoe shop. |
| 14.4–16.0 | Chapter card 1 | "Number one, New Balance" | Burgundy **#743D3C** full-frame card, red slab-serif "NUMBER 1" with black outline (~22 % from top), product cut-out mid-frame popping in ~0.5 s later. |
| 16–23 | Concession | "patients bring these in… look supportive" | Exam room (patient in NB shoes, clinician's back), clinician, woman walking outdoors in NB. |
| 22–32 | **Mechanism montage (aggressive)** | "elevated heel tipping weight… pelvis… discs… sciatic nerve every step" | X-ray leg in shoe with a **red-hot heel** and a red dashed sole line. Muscled torso with **red lightning down the leg**. X-ray skeleton with a **lumbar spark explosion**. Close-up vertebrae with a **glowing red disc** and yellow nerves. Pelvis-to-leg nerve in red. |
| 32–47 | Consequence | "muscles never engage… weaken… hips and back… clamping" | Woman in pyjamas holding her back. **Red muscle glow inside a shoe** (X-ray through the upper). Hands massaging a foot with red/blue veins. Translucent walking body. **Hunched muscle-man** (aging). Presenter. Woman's back with a **glowing spine and red lumbar**. Woman walking with a **blue X-ray pelvis overlay**. |
| 47.6–50.7 | Chapter card 2 | "Brooks Ghost or Adrenaline" | Same card; two cut-outs with a "VS" disc and model labels. |
| 50–76 | Brooks section | "graduate to… max cushioning… numb… lower back overtime… compression" | Older woman by a sofa with a dog. Brooks on feet (B-roll). Another "clinician" in an exam room. Glittering **numb foot** (fairy-light nerves). Long red **sciatic-nerve-through-pelvis** render (3 s+). Presenter. **Screaming old woman in a gown, red glowing lumbar spine** (73–76 s). |
| 76–77.5 | Chapter card 3 | "Hokas" | Same card. |
| 77–110 | Hoka section | "break my heart… $180… shooting pain… inch thick… shut down muscles… spine aligned… ruining your foundation" | Presenter. Senior man with clinician. Finger pressing a shoe. Senior woman bracing on a sofa. Presenter with a **warm light-leak flash**. Woman in Hokas walking. **Orange glowing nerves in the calves**. Thick sole 3D. **Foot muscles turning from red to grey inside the shoe**. Skeleton with the spine lighting red. Disc glow. Muscle back with red spine. **Red lightning down the glutes/hamstrings** (107–110 s). |
| 110–121 | Recommendation | "So what do I recommend… HF Flow… stop sciatica at the root" | Presenter holds (the longest talking-head stretch). The product reveal at 116 s is the shoe on a dust bag, then on feet. Caption becomes a **bold black-caps product box**. |
| 121–158 | **Solution mechanism (green)** | "thin sole… muscles fire… hips release… toe box… zero drop… pelvis settles" | Mirror of the problem montage in **green**: X-ray leg with green muscles, glowing ground rings, green-vs-red leg comparison, green spine, anatomy chart with green arrows, toe-box arrows, "EXTRA-ROOM TOE BOX" diagram, level/plumb lines, "ZERO-DROP SOLE" spaced caps, real walking. |
| 158–168 | Convenience | "hands-free… no bending… slide in" | Shoe step-in. **B&W bending-over shots with a big red X** (3 cuts). Slide-in. Women at home. Happy dance. |
| 168–193 | Testimony montage | "patients tell me… shooting pain quieting… stop bracing… grocery store… slept" | 1–2 s lifestyle clips: walking outdoors, holding shoes, snow walk, arms-out joy, standing from a chair, elderly woman helped then walking, grocery cart, waking up in bed. |
| 193–206 | Re-agitate + close | "If your sciatica has been getting worse… shoe may be a big part… let your feet do their job" | Woman struggling up from a sofa (real, slow). Woman pulling shoes off on stairs. Feet walking in a car park, with a kid. |
| 206–209 | CTA | "Get HF Flow at the link below" | Shoes placed onto a branded dust bag, top-down. No end card. |

## 2. How the aggressive scenes are built (and how we'll rebuild them without AI)

| Device | In the reference | Our version |
|---|---|---|
| **Anatomy layer on a real body** | AI video-to-video: muscles and a glowing nerve painted onto the person, tracking the motion. | Composite on real footage: red radial heat glow at the lumbar spine and buttock, plus an **animated branching lightning nerve** running from L5 down the back of the thigh to the calf. It is procedurally generated per frame (flicker, re-branching every 2–3 frames), blurred and additively blended. Add a subtle red grade and edge vignette, plus a 2-frame white "zap" flash on the first strike. |
| **Glowing disc / spine** | AI 3D vertebrae with a hot red disc. | Reuse the **X-ray skeleton / spine / 3D foot assets** from our own winning ads, and from the Drive `12_Animations` folder if present. Then add the same red lightning and heat-glow layer at the lumbar point. |
| **Red pain glow on a foot or back** | Red bloom on the area being held. | Radial gradient (#FF2A00 → transparent), pulsing at 2–3 Hz, with screen blend. Our past winners already use this (W04, W07, W09, W11). |
| **Screaming / grimacing woman** | AI senior in a hospital gown. | Real creator clips of women holding their back or leg, struggling up from a chair (TikTok and Drive `06_Pain Points`), plus the lightning layer. No faked screaming. |
| **Muscle shutting down (red → grey)** | AI foot muscles. | **Not used.** The brief bans implying competitor shoes damage muscles. |
| **Green healing mirror** | Green spine and muscles after the product. | **Not used** (brief: no cure imagery). Product explanation uses **blue (#1E6FD9) feature callouts** on real ComfortWear footage. |
| **Monster shoe** | AI shoe with teeth. | Replaced per the brief with 3 hard-cut packshots on the spoken brand names. The interrupt comes from rhythm plus a whoosh and white flash. |
| **B&W + giant red X** | Bending-over shots. | Available for the "loosening laces" line, used on generic, unbranded footage only. |

**Compliance stance:** the aggressive nerve and lightning visuals are used only on **symptom-recognition lines** (rows 01, 07, 21, 40: "if you have sciatica", "shooting pain down your leg", "back and leg pain", "already managing sciatica"). They are never placed on or next to a competitor shoe, and never after the ComfortWear reveal. This keeps the reference's intensity without the brief's banned causal claims.

## 3. Text system (measured)

- **Running captions:** white rounded box, black bold sans (TikTok Sans / Proxima Semibold look), lowercase sentence fragments of 2–6 words over 1–2 lines. Glyph ≈ 38–42 px at 1080 width, box padding ≈ 14 px, radius ≈ 14 px. Centred at **~45–67 % from top**: it sits mid-frame, moves to avoid faces and hands, and changes on every phrase.
- **Hook banner:** red box (#E8141B), white heavy caps (Montserrat Black / Poppins ExtraBold), ≈ 46 px glyph, mid-frame.
- **Chapter card:** background #743D3C, "NUMBER N" in red (#FF0000) heavy slab serif with a black outline and drop shadow, ≈ 85 px tall at ~22 % from top. The product cut-out is centred at ~55–70 %.
- **Product name:** black bold caps on a white box, 2 lines ("HF FLOW / BAREFOOT SHOES").
- **Diagram labels:** spaced thin caps ("Z E R O - D R O P   S O L E"), dashed lines and arrows in black/white or green.

## 4. Rhythm lessons

1. **Hook stacking:** 3 different visual worlds in 6 s (anatomy-on-human → surreal shoe → grimace), with each text beat building the sentence.
2. Cut **on the noun**: every anatomical word gets its own render ("pelvis", "discs", "nerve", "muscles", "hips").
3. **Chapter cards** are 1.5–3 s with a sound hit; they reset attention every ~30 s.
4. The **presenter returns** every 10–20 s as a "breather" between montage runs. Holds run 1–3 s, except the recommendation block (110–121 s), which is the one long hold.
5. **Concession first**, then the mechanism ("I understand they look supportive, but…").
6. The **product arrives at 53 %** of runtime (116 s / 209 s), consistent with our own winners.
7. The close **re-agitates** (struggling off the sofa) right before the CTA.
8. The CTA is plain: a top-down shoes-on-bag placement with no end card or discount.
