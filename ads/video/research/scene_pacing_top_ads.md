# Scene pacing: $20k+ WearOrtho video ads vs COM458 (Nov 2026)

Client feedback on COM458: "sometimes it looks like it's changing scenes really fast".
Measured with `scripts/pacing.py` (frame-difference + colour-histogram cut detection on the *rendered* video, so it counts every
visible scene change, including cuts that live inside source clips). 30 WearOrtho ads with >= $20k spend vs the COM458 H1 final.

| metric | winners (median) | COM458 H1 |
|---|---|---|
| visible scene changes | 74 per ~2 min ad | 173 in 3:42 |
| median shot (s) | 1.54 | 1.03 |
| 25th pct shot (s) | 0.90 | 0.53 |
| share of shots < 1.0 s | 0.29 | 0.50 |
| share of shots < 1.5 s | 0.48 | 0.65 |
| longest run of < 1.5 s shots | 8.00 | 12.00 |
| VO words per shot | 5.08 | 3.83 |
| soft/dissolve transitions | 0.08 | 0.06 |
| cuts within same scene | 0.03 | 0.08 |
| in-shot motion | 3.81 | 3.94 |
| cuts landing mid-word | 0.39 | 0.41 |

## What it means
1. **The edit decision list was fine, the footage wasn't.** COM458's EDL had 112 shots (≈5.9 VO words per shot, in line with winners),
   but the viewer saw ~170 scene changes: 61 extra cuts came from *inside* the TikTok clips (creator jump-cuts / montage edits;
   one Lonely Planet travel montage alone added 15). That is what read as "changing scenes really fast".
2. Winners hold a scene for ~5 words of VO (median 1.5 s on screen, 25th percentile 0.9 s) and use almost only hard cuts (8% soft).
3. Winners do have fast moments, but in short bursts; most shots are one continuous take.

## Rules for COM459 onwards
- Every shot is one continuous take: source clips are scanned for internal cuts and the in-point is moved to a clean window
  that covers the whole shot (+0.3 s). No clean window -> pick another clip.
- ~5-6 VO words per shot; minimum shot 1.2 s unless it's a deliberate burst; group adjacent nouns < 1.2 s apart into one shot.
- Hard cuts placed in the breath before the word (soft 4-frame blend kept, it reads as a clean cut).
- Re-measure every render with `pacing.py`; target visible-shot median >= 1.5 s and < 1.0 s share <= winners (0.29).
