# Video breakdown brief (shared by every breakdown agent)

Goal: study proven DR video ads frame by frame so we can replicate *how* they are built: hooks, B-roll, scene changes, transitions, on-screen text (font, size, color, position), pacing. Be concrete and measurable. Do not summarise vaguely ("engaging hook"); write what is literally on screen and when.

## Inputs per video (folder = `<analysis_root>/<key>[_<id>]/`)
- `cuts.json` — duration, every shot (start/end/len), avg/median shot length, cuts in first 3 s / 10 s. Scene detection catches hard cuts; it misses cuts *inside* split-screen panels and soft punch-ins, so verify visually.
- `hook_sheet.jpg` — frames every 0.25 s from 0.00 to 3.50 s (5 per row).
- `shots_sheet_N.jpg` — one frame per detected shot, labelled `#shot start (length)`.
- `transcript.txt` / `transcript.json` — VO with segment timings (json also has word timings and `wpm`). Auto-transcribed locally: brand names can be misspelled (e.g. "comfort wear" = ComfortWear, WearOrtho's shoe brand; "sketchers" = Skechers).
- Some WearOrtho entries have only `thumbnail.jpg` (video no longer downloadable): analyse the thumbnail + ad copy only and say so.
- The mp4 itself (path in the index JSON) — use it for anything the sheets can't answer.

## Tools
- Full-res frame to look at: `ffmpeg -v quiet -ss <t> -i <video> -frames:v 1 -vf scale=540:-2 /tmp/claude-0/<name>.png` then Read it. Keep extracts ≤540 px wide unless reading small text.
- Text size in px at 1080×1920: `python3 ads/video/scripts/measure_text.py <video> <t> --y0 <top> --y1 <bottom> --color white|black|yellow|red` → prints text bands (y range, height px, width px, % from top) and saves a crop at /tmp/claude-0/measure_crop.png you can Read. If captions are black text on a white box, measure the box with `--color white` and the glyph lines with `--color black`. A band height ≈ one line of text incl. ascenders/descenders; report it as "line height ≈ N px", plus box height if boxed. Measure the hook headline and the running captions in each video (2–3 measurements per video is enough).
- Fonts: identify by eye from a full-res crop (e.g. TikTok Sans/Proxima Nova Semibold for the native TikTok white-box caption, Montserrat ExtraBold/Black, Poppins Bold, Arial Black/Helvetica Bold, Bebas Neue, Anton, Futura, serif fonts…). Give your best guess plus the visual tells (geometric round "o", double-story "a", tall x-height, condensed, etc.).
- Work from the repo root `/home/user/claude_code_sam`. Write only your own output file(s). Don't download anything from YouTube.

## Output per video (markdown, this exact skeleton)
```
### <key> — <one-line concept name>
**Data:** <WearOrtho: spend CAD, ROAS, #ads, run months | Competitor: days running, status, impression rank/pool, trend> · <duration>s · <n> shots · avg <x>s / median <y>s · VO <wpm> wpm · lang
**Format / angle / persona:** e.g. listicle "Top 5 shoes for nurses" · comparison vs. named competitors · nurse persona
**Hook (0–3 s):**
- Visual: exactly what's on screen frame by frame (layout: full-frame / split / 3-panel stack / green-screen / TikTok UI…), motion, product visible at what second
- Text hook: "exact words" — font guess, weight, case, color(s)/highlight, box/stroke/shadow, line height ≈ px, position (% from top)
- Verbal hook: "first sentence of VO" (start time)
- Audio: music/SFX/none · Hook archetype(s): …
- First hard cut at Xs; # visual changes in first 3 s
**Beat map:** table | t | beat (hook/problem/agitate/mechanism/demo/proof/offer/CTA…) | VO (short) | visuals/B-roll | on-screen text |
**B-roll inventory:** bullet list of shot types with rough counts (use the taxonomy below)
**Transitions & motion:** hard cut share, punch-ins/zooms, whip/glitch, speed ramps, split-screen, graphics (arrows, circles, ratings, emojis, stickers, product cut-outs), SFX if audible from transcript gaps
**Caption system:** style (TikTok white-box / outlined white / word-by-word highlight / phrase 1–2 lines), font guess, size (line px), words per caption, position band, colors, consistency; plus headline/title-bar spec if present
**Pacing:** shot length in hook vs body vs CTA; where holds happen and why
**Offer & CTA:** when it lands, words, visuals (price strike-through, % off badge, guarantee…)
**Steal this:** 3 bullets of concrete, reusable techniques
```
After all videos in your batch, add `## Batch patterns` — 10–15 bullets on what recurs (hook types, avg cut rate, caption spec that dominates, B-roll mix, length, CTA timing), with counts ("7/10 use…").

## B-roll taxonomy (tag shots with these)
talking-head (creator selfie), talking-head (pro/doctor/podiatrist), POV walking/feet close-up, product hero/packshot, product handling/unboxing, product demo (flex/twist/stretch/press insole), comparison vs. competitor product, problem visualisation (pain, rubbing feet, limping, swollen), anatomy/3D/medical animation, lifestyle (work/nurse shift/travel/walking dog), testimonial clip (other customer), review/UGC screenshot, press/social-proof graphic, text-only/kinetic type card, stock footage, green-screen over article/website, offer/price card, reaction shot, ASMR/texture macro, before/after.
