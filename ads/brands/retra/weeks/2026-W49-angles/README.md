# Retra W49 angles batch: 59 statics from Sam's 61 picked formats × his angles

19 concepts, 1 static each, 9:16 master (`_9x16.png`, content inside the centred 4:5 band) + 4:5 crop (`_4x5.png`).
Funnel: 13 TOF · 3 MOF · 3 BOF.

## Files
- `copy.json`: StefanBrain copy (project "Retra Launch", chat `chat_e2881d64bb4e43c687b42831eb31dff3`), v2 after claim fixes; `copy_v1.json` is the first draft.
- `layouts.py`: product-only layouts (02 04 07 08 09 10 11 14 15 16 17 18 19) from clean cut-outs
  (`assets/retra/product/cutout_clean/`, made by `clean_cutouts.py`) and the 4K gallery fronts.
- `render.py`: 4K Kie scenes (Nano Banana Pro, reference-guided from `assets/retra/product/retra_<colour>_34.jpg`) for 01 03 05 06 12 13; 2 takes each, picks in `scenes.py` (PICKS). Raw renders kept as JPEG archives; 4K PNGs stay local.
- `scenes.py`: layouts on the scene renders.
- `output/`: 19 statics × (9:16 + 4:5), `_sheet_4x5.jpg`, `_sheet_9x16.jpg`, `RET_A49_concepts.csv` (on-image text, Meta headline, primary text, persona, notes).
- `lib.py`: type system matched to the live store theme (reclaimnutra.com, theme "Retra-Shots", `assets/retra.css`): display Tinos (site stack "Times New Roman", Tinos) weight 400, -0.04em, line-height 1.1, navy #022B49; body Inter 400 in #416077; kicker/hand Shantell Sans italic; CTA pill gradient #2C4D63 / #4B6B80 / #8EA6B4; dark label pill #0E1C27; heading emphasis two-tone navy / navy-50. Plus 9:16 + 4:5 export.
- `sheet.py`: contact sheets.

## Backgrounds
Plain backgrounds are pure white (Sam, 2026-11-26). Deliberate colour blocks stay: 02 dark collage, 07 navy, 14 black, 16 yellow frame.

## Cost
Kie: 354 credits for 14 scene renders + 18 for the disposable cut-out, about $1.86.

## Flags
- `_ILLUSTRATIVE` (02, 10, 18, 19): the sample photos are Kie renders with Retra's filter curves applied, not real Retra photos. Swap in real samples before launch.
- 01 uses the handle "@retra": confirm Retra's real handle.
- Several primary texts mention looking "through the viewfinder" (the camera has a viewfinder window; confirm it's usable).

## Batch 2 (ids 20-59, added 2026-11-26)
Sam's remaining picked formats (Manta's review card skipped: no real reviews yet), copy in `copy_b2.json` (StefanBrain v2 after claim fixes),
layouts in `b2.py`, scenes from `batch2.py` (4K Kie). Funnel across all 59: 37 TOF · 13 MOF · 9 BOF.

## Realism + grip pass (2026-11-26)
- Product layouts now use real 4K Kie product photos (`products.py`: each colour on a white sweep, fronts, Sol on navy,
  six-colour lineup on black) placed with a multiply blend (`lib.product` / `lib.multiply`), replacing pasted cut-outs.
- Every hands-on-camera scene was re-rendered with a grip spec (hands on the ends, finger on the shutter, nothing over the
  lens/flash/viewfinder/wordmark); picks in `scenes.py`.
- No-camera scenes are rendered without the wordmark allowance (`rerender_noref.py`) so nothing else carries "Retra".
- Comparison charts label our column "Ours" (09, 30, 45, 54). 08 headline is Sam's own line.

## KLIK-inspired (ids 60-67, 2026-11-26)
Six classic KLIK formats not used before (stair-step lineup, gift flat lay, icon checklist + hands with a stack, colour tower,
27 -> 500 number swap, $0 receipt) and two of KLIK's current Black Friday formats (huge % off with a ribbon-tied stack,
"On Santa's list"). Copy: `copy_klik.json` (StefanBrain v2). Scenes: `klik_render.py`; layouts: `klik.py`.
60's lineup is built from the verified product photos (Kie's group shot changed the button shape).
Skipped: KLIK's iMessage-chat formats (need invented customers) and its 30-day guarantee (not confirmed for Retra).

## Pain-point batch (ids 68-77, 2026-11-27)
One specific pain per under-covered angle, aggressive pain-first copy (StefanBrain v3: v1 draft, v2 rule fixes + harder
pain, v3 "up to 500" and no viewfinder). Formats from Sam's picks plus two native-UI mocks (iOS battery banner, stacked
permission dialogs). Copy: `copy_pain.json` (`copy_pain_v1.json` = first draft). Scenes: `pain_render.py` (takes chosen
in `pain.py`: p68_t2, p70_t2, p77_t2, others t1); layouts: `pain.py`. Sheet: `output/_sheet_pain_4x5.jpg`.
68 theme park: phone dead by afternoon · 69 wedding: guest photos trapped in camera rolls · 70 grandparents: grandkid
photos locked on someone else's phone · 71 detox: one photo turns into 40 minutes · 72 solo travel: $1,500 phone held up
in a pickpocket crowd · 73 sensory: buzz/glow/ping · 74 wireless: pair/update/sign-in popups · 75 parents: kid wants a
phone · 76 honeymoon: flew across the world to stare at phones · 77 one-click: hours tweaking presets (BOF, 40% off).

## Magic Kingdom (ids D1-D4, 2026-11-27)
Sam asked for 4 Disney-trip concepts outside the inspiration picks, with Magic Kingdom in the background, on being in the
moment. Sam chose to show the real Cinderella Castle and name Disney / Magic Kingdom (accepting the IP and Meta-review
risk); still no characters and nothing implying Disney endorses Retra. Formats: D1 annotated fireworks photo, D2 snapshot
board (ILLUSTRATIVE prints), D3 postcard to future you, D4 Main Street hero + colour swatches. Copy: `copy_disney.json`
(StefanBrain v2; `copy_disney_v1.json` first draft). Scenes: `disney_render.py` (patches render.REAL to allow the castle);
layouts: `disney.py`. Sheet: `output/_sheet_disney_4x5.jpg`.
Revision (Sam, same day): D1 re-rendered with the camera at true palm size (`d1b`); D4 now a film-look 4x6 print with the
camera beside it (`d4p`; plain lab print, not instant film, since Retra doesn't print); D3 postcard replaced by "your
parents' Disney photos vs your camera roll" (`d3v1`, `d3v2` faded 90s prints; `d3p` tiled as a camera roll).
Fireworks split (D1V Vintage, D1F Film): one clean castle-fireworks render (`d5`), left half as shot, right half through
the landing-page filter curve (`compose_gallery.retra_filter`), slider divider. ILLUSTRATIVE. Sheet: `output/_sheet_disney_split_4x5.jpg`.

## Colour rename (2026-11-27, from the Shopify store)
Chalk->White, Obsidian->Midnight, Sol->Yellow, Dune->Brown, Pine->Green Forest, Blossom->Red, plus a 7th colour Blue
(alt text "Aegean"). `colour_rename.py` swapped names and "six"->"seven" colours in all copy files and the CSV; lib.py
has STORE_NAME / STORE_ORDER and the Blue swatch. Re-rendered statics with colours on the image: 11, 15, 34, 50, D4.
Open: the store's compare-at price is now $200 (statics still say $165 / 40% off); 11 shows six tiles under "All 7".

## D5 + wedding memories (W1-W5), 2026-11-27
D5: golden-hour Main Street (`d6_t2`) through the Vintage curve with lens frame marks, labelled "Simulated" (ILLUSTRATIVE).
W1-W5 follow Sam's wedding refs: W1 RTR flash photo + text bubbles, W2 The Knot card + arrow CTA, W3 The Knot dark
first-dance headline + link CTA, W4 The Knot iOS reminder, W5 Olive & Piper bridal product hero (Tinos Italic added to
fonts/). Copy: `copy_wedding.json` (StefanBrain v2; v1 in `copy_wedding_v1.json`). Scenes: `wedding_render.py`;
layouts: `wedding.py`. Sam wants 4:5 deliverables from here on. Sheet: `output/_sheet_wedding_4x5.jpg`.
