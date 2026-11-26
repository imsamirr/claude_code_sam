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
