# Retra — Static Ad Brief for Claude Code (Kie.ai)

Batch: 10 static image ads · 7 top of funnel (TOF) · 3 bottom of funnel (BOF)
Prepared: 2026-11-25 · Market: Canada (Quebec + Ontario first), then US
Renderer: Kie.ai (use the existing Kie setup from the ComfortWear / DentalPULSE pipeline)

---

> **Repo notes (read first):**
> - Per `CLAUDE.md`, StefanBrain writes all final copy. Treat every headline, subhead, primary text and FR line below as the angle and the facts to brief StefanBrain with, not as final copy. Retra doesn't have a StefanBrain project yet, so ask Sam which project to use or whether to create one.
> - The camera images under `landing-pages/retra/` (`g0-*`, `gallery-src/base/*.jpg`) were generated on Kie to match Klik's body. They are **not** real product photos and must not be used as references.
> - Colour names seen in the landing-page handoff: Dune, Pine, Aegean, Sol, Blossom, Obsidian, Chalk. Not yet confirmed by Sam or the supplier.
> - The gold serif "Retra" logo is only in renders so far. Don't show a logo on the camera unless Sam confirms it's printed on real units.
> - Don't use Klik's or Camp Snap's product photos as references (their copyright).

## 0. Before you render anything

1. **Product reference photos are required.** Put them in `assets/retra/product/` (front, back, top, 3/4 angle, every colour, on a plain background). Every render must be **image-to-image / reference-guided** from these photos. Never let the model invent the camera.
2. **Confirm product facts with Sam before final copy:** colour names, whether "Retra" is printed on the body, sensor MP, shots per charge, what's in the box.
3. **Real sample photos (optional, strongly preferred):** put 1–2 real photos per filter in `assets/retra/samples/{vintage,bw,natural,film}/`. Ad #8 uses them. If none exist, render illustrative samples and mark the file `_ILLUSTRATIVE` so it isn't used without review.

---

## 1. Product

- **Name:** Retra screen-free digital camera
- **What it is:** a reusable "modern disposable." Point, shoot, no screen. See your photos later.
- **Filters (4):** Vintage, Black & White, Natural, Film
- **Export:** USB-C to phone or computer
- **Rechargeable, reusable**
- **Do NOT claim:** "EMF-free" or "radiation-free" (not accurate for any battery device; Competition Act risk). Allowed only once the supplier confirms there's no wireless chip: "No Wi-Fi. No Bluetooth. No app."
- **Avoid:** health claims, "safe for kids' brains," any Disney name, castle, characters or logo, any real celebrity.

## 2. Offer (BOF ads only)

- **Buy 2, get 1 free**
- **Low stock** ("Selling fast", "Almost gone", sold-out stamps on some colours)
- **$99 CAD, compare at $165: 40% off**

## 3. Who we're talking to

| Persona | What they want | Core emotion |
| --- | --- | --- |
| Digicam girl (Gen Z / young millennial woman, 18–30) | The flash-lit, grainy 2000s look; nights out, trips | Nostalgia, fun, authenticity |
| Present parent (30–45) | Photos of the kids without picking up the phone | Less guilt, pride |
| Traveller / theme-park fan | Stay present on the trip, candid shots | Freedom, joy |
| Wedding / event host | Guest candids without phones out | Belonging, anticipation |
| Concertgoer | Watch the show, still keep a memory | Presence, rebellion against the phone wall |
| Gift buyer for grandparents | A simple, novel gift | Warmth, relief ("finally something easy") |

**One dominant pain (all TOF ads):** you pull out your phone for one photo, and 20 minutes later you're in your email and Instagram. You were there, but not really there.

**Peak emotion to show:** anticipation, the surprise of seeing the photos later.

## 4. What the research says wins (Atria, Meta image ads, 7+ days running)

- Klik #1 (214 days, 1.78M reach): "SELLING FAST." Eight colours in a row, two stamped "Sold out," price on image. Cream background, handwritten font.
- Klik #2 (149 days, 1.9M reach): "No more disposables." One camera, three plain benefits.
- Flashback #1 (92 days, 3.09M reach): camera shrink-wrapped like a supermarket meat tray, "+1 free gift," "Sells out fast!"
- Camp Snap: new colours treated as news ("Gone twice. Back again.").
- **Gap nobody fills:** people, parents, the phone problem, real sample photos, the reveal moment, French copy. Our TOF ads go into that gap. Our BOF ads borrow the proven scarcity + colour-lineup layout.

## 5. "Must not look like AI" rules

Apply to every prompt:

- **Shot on a real camera:** "candid 35mm-style photo, shot on a compact camera with on-camera flash" or "iPhone photo, natural window light." Never "8K, ultra-detailed, hyperrealistic, cinematic."
- **Imperfections on purpose:** slight motion blur, flash hotspot, mild grain, off-centre framing, a stray object in frame, uneven light, a bit of lens flare.
- **Real people:** natural skin texture, pores, flyaway hair, ordinary clothes, no model poses, mid-laugh or mid-movement. No perfect symmetrical faces.
- **Hands:** max one hand holding the camera; fingers fully visible and correct. Re-render if fingers are wrong.
- **Product fidelity:** the camera must match the reference exactly: shape, button layout, viewfinder, flash window, colour, logo. If the model changes any detail, re-render.
- **Text:** render the scene **without text**, then composite headline/subhead in code (Pillow) for crisp, correctly spelled type. Leave clean space where text goes.
- **Negative prompt (where supported):** `glossy CGI, plastic skin, airbrushed, oversaturated, extra fingers, warped text, fake logo, studio-perfect lighting, symmetrical face, 3D render, illustration`

## 6. Specs

- **Size:** 1080×1350 (4:5) master. Optional 1080×1920 (9:16) crop for Stories with text inside the middle 1080×1420 safe zone.
- **Render resolution:** 2K on Kie, then downscale.
- **Text layout:** headline max 7 words; subhead max 12 words; one CTA line on BOF only. Text covers no more than about 20% of the image.
- **Fonts:** TOF headlines use a clean handwritten or marker font (e.g. Caveat Bold / Permanent Marker) or a simple grotesk (Inter / Helvetica Neue Bold). BOF uses a bold grotesk for price and stamps.
- **Colours:** cream `#F3EEE4` or warm white backgrounds for product-only ads; black or deep-red stamp for "Sold out."
- **File naming:** `RET_W48_{##}_{tof|bof}_{angle}_v{n}.png`, e.g. `RET_W48_01_tof_phone-fatigue_v1.png`.
- **French versions (phase 2):** make every headline a variable so FR copy can be swapped in. FR lines are suggested below.

---

## 7. The 10 ads

Each ad below has: angle, persona, headline/subhead (EN + FR), Kie prompt, text placement, and the primary text for Meta.

### TOF (7 ads)

#### 01 — Phone fatigue (all personas)
- **Headline:** Your camera shouldn't have notifications.
- **Subhead:** No screen. No apps. Just the moment.
- **FR:** Ton appareil photo ne devrait pas avoir de notifications.
- **Prompt:** Using the reference product photo exactly, a hand holding the Retra camera in the foreground on a small café table, in focus. Behind it, slightly out of focus, a smartphone lies face up, its screen lit with a stack of notification banners. Afternoon window light, a half-finished latte and a crumpled napkin on the table. Candid iPhone photo, natural light, mild grain, slightly off-centre framing. Top 30% of the frame is calm and uncluttered for text.
- **Text placement:** top, dark text on light area.
- **Primary text:** You took your phone out for one photo. 20 minutes later you were in your inbox. Retra is a screen-free camera: point, shoot, and see your photos later. No notifications, ever.

#### 02 — Kids see you, not your phone
- **Headline:** They'll remember you looking at them.
- **Subhead:** Not at your phone.
- **FR:** Ils se souviendront de ton regard. Pas de ton téléphone.
- **Prompt:** Using the reference product photo exactly, a mother in her mid-30s in a sweater, seen from behind her shoulder, raising the Retra camera to photograph two kids (around 5 and 8) laughing at a kitchen table covered in craft paper and crayons. Her phone sits face down in a fruit bowl on the counter. Warm evening kitchen light, slight flash bounce, real home clutter (a mug, a lunchbox). Candid, documentary feel, natural skin, slight motion blur on the kids.
- **Text placement:** bottom third over a soft gradient.
- **Primary text:** Kids notice when you're on your phone. Retra lets you capture the moments without picking it up. No screen, no scrolling, just photos you'll see later.

#### 03 — Theme-park travel (no Disney IP)
- **Headline:** No screen between you and the magic.
- **Subhead:** Candid park-day photos. Zero scrolling.
- **FR:** Aucun écran entre toi et la magie.
- **Prompt:** Using the reference product photo exactly, the Retra camera hangs from a wrist strap on a dad's wrist while he carries a laughing young daughter on his shoulders on a busy theme-park street. Generic colourful park buildings, balloons and string lights in the background, no recognizable castles, characters, logos or trademarks. Bright midday sun, slight overexposure, mild grain, candid snapshot taken by a family member.
- **Text placement:** top, white text with a subtle shadow.
- **Primary text:** You flew all this way, so don't watch it through a screen. Retra takes up to 500 candid photos per charge, and you see them all when you get home.
- **Targeting note:** reach Disney fans through interests, not the creative.

#### 04 — Europe travel
- **Headline:** See Europe. Not your feed.
- **Subhead:** 500 candid shots per charge. See them when you're home.
- **FR:** Vois l'Europe. Pas ton fil d'actualité.
- **Prompt:** Using the reference product photo exactly, two women in their late 20s walking arm in arm and laughing on a narrow cobblestone street with pastel buildings and flower boxes (Lisbon or Rome style, no landmarks with logos). One holds the Retra camera up mid-shot toward her friend. Golden hour, warm low sun, lens flare, slight motion blur, shot from a few steps ahead like a candid snapshot. Ordinary travel clothes, a tote bag.
- **Text placement:** top-left.
- **Primary text:** The best trip photos are the ones you didn't pose for. Retra has no screen to check, so you keep walking, keep laughing, and find the photos later.

#### 05 — Wedding
- **Headline:** Phones away. Cameras out.
- **Subhead:** The modern disposable for every guest table.
- **FR:** Téléphones rangés. Appareils sortis.
- **Prompt:** Using the reference product photo exactly, a wedding reception table at night: white linen, candles, eucalyptus, half-full wine glasses, place cards. A Retra camera sits at two place settings next to a small handwritten card (leave the card blank for text compositing). In the background, out of focus, guests dancing under warm string lights. On-camera flash look, warm tones, slight grain, a crumpled napkin and a lipstick-marked glass for realism.
- **Text placement:** top; composite "Take a photo, leave your phone" onto the blank card.
- **Primary text:** The candids you'll love most are the ones your guests take. Put a Retra on every table: no film, no developing, hundreds of shots each.

#### 06 — Concert
- **Headline:** Be the one actually watching.
- **Subhead:** Snap the moment. Put it away. Feel the show.
- **FR:** Sois celui qui regarde vraiment le show.
- **Prompt:** Using the reference product photo exactly, a crowd at an indoor concert seen from behind, dozens of raised glowing phone screens blocking the stage lights. In the foreground, one young woman holds the Retra camera at chest height, looking up at the stage instead of a screen. Purple and blue stage lights, haze, high grain, flash-lit foreground, slight blur. No band logos, no real artists.
- **Text placement:** top over the dark haze, white text.
- **Primary text:** A wall of phones and nobody watching. Retra lets you grab a few shots and get back to the show. No screen, no recording, no distraction.
- **Note:** don't position it for phone-free (Yondr) shows; those usually ban all cameras.

#### 07 — Grandparents gift
- **Headline:** One button. No menus. Grandma approved.
- **Subhead:** The easiest camera they'll ever own.
- **FR:** Un bouton. Aucun menu. Approuvé par grand-maman.
- **Prompt:** Using the reference product photo exactly, close-up of a woman in her 70s with silver hair and reading glasses, smiling as she holds the Retra camera with both hands, thumb on the shutter button. Behind her, softly blurred, a grandchild opening a gift and a Christmas tree with warm lights. Living-room lamp light, natural wrinkles and skin texture, slight grain, candid family photo feel.
- **Text placement:** top-left.
- **Primary text:** No passwords, no apps, no tiny settings. Retra is point and shoot: one button, a viewfinder, and photos they can see on the computer later. A gift they'll actually use.

### BOF (3 ads)

#### 08 — The 4 filters + 40% off
- **Headline:** 4 film looks. Zero apps.
- **Subhead:** Vintage · Black & White · Natural · Film
- **Offer line:** $99 ~~$165~~ · 40% off
- **FR:** 4 looks argentiques. Aucune application.
- **Build:** 2×2 grid of the SAME candid scene in each filter (use real samples from `assets/retra/samples/` if available), with the product photo (from reference, cutout) overlapping the centre and a small label under each tile.
- **Prompt (only if no real samples):** A candid photo of friends laughing around a picnic blanket in a park at golden hour, shot on a compact camera with flash. Render 4 versions: (a) warm faded vintage tones with soft halation, (b) high-contrast black and white with grain, (c) natural true-to-life colour, (d) Kodak-style film colour with green shadows and warm highlights. Identical composition in all 4. Mark output `_ILLUSTRATIVE`.
- **Primary text:** Four film looks built in: Vintage, Black & White, Natural and Film. No editing and no apps. Now $99 (was $165).

#### 09 — Buy 2, get 1 free (colour lineup)
- **Headline:** Buy 2, get 1 free.
- **Subhead:** One for you, one for them, one for the trip.
- **FR:** Achète-en 2, obtiens le 3e gratuit.
- **Prompt:** Using the reference product photos exactly, every Retra colourway lined up in a slightly diagonal row on a warm cream seamless background (#F3EEE4), soft natural shadow, product photography style but with real-world softness (slight grain, not glossy CGI). Three cameras in the centre tied together with a thin black ribbon. Empty space top 30% for text.
- **Text placement:** headline top centre in bold grotesk; small "Limited time" pill below.
- **Primary text:** Holiday gifting, sorted. Buy 2 Retra cameras and get the third free. Reusable, rechargeable, and screen-free.

#### 10 — Low stock + price
- **Headline:** SELLING FAST.
- **Subhead:** Screen-free camera. $99 (was $165). Pick your colour before it's gone.
- **FR:** ÇA PART VITE.
- **Prompt:** Using the reference product photos exactly, all Retra colours in a straight horizontal row on a cream background, evenly spaced, soft shadows, real product photo feel with mild grain. Leave room above two of the cameras for a stamp.
- **Composite:** red or black rubber-stamp "SOLD OUT" over 2 colours (use colours Sam confirms are actually low); small "In stock" tags under the others. Price line under the row.
- **Primary text:** Our last restock is almost gone. Retra is $99 (was $165) while stock lasts. Pick your colour.
- **Rule:** only stamp colours that are really low or sold out. Fake scarcity is a Competition Act risk.

---

## 8. QA checklist (run on every output)

- [ ] Camera matches the reference exactly (shape, buttons, viewfinder, flash, colour, logo)
- [ ] Hands and fingers look correct
- [ ] No warped or AI-garbled text in the scene (all text composited in code)
- [ ] Faces look like real people (skin texture, not airbrushed)
- [ ] No Disney, band, landmark or brand logos
- [ ] No "EMF-free" or health claims; scarcity and prices are true
- [ ] 1080×1350, headline readable on a phone at thumbnail size
- [ ] File named `RET_W48_{##}_{tof|bof}_{angle}_v{n}.png`

## 9. Hand-back

Deliver a contact sheet (all 10 in one image) plus a CSV with: ID, funnel, angle, persona, headline, subhead, primary text, FR headline, file path, render cost, notes.
