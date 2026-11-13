---
name: video-ads
description: Make short-form video ads (Reels/TikTok/Stories, 9:16 + 4:5 feed crop) for a brand in ads/brands/<brand>/ by editing existing footage from the brand's Google Drive asset folder. Studies inspiration ads from Atria (downloads and watches them), pulls the brand's own winning angles from its Atria ad account, inventories and triages Drive footage, writes a native-style script (text-on-screen story captions, POV/meme formats, no voiceover by default), cuts it with ffmpeg via an edit.json, QAs frames, and delivers. Use for "make me a video ad", "short-form ad from our footage", "<angle> video", "UGC edit", "iterate this video winner into short form", "TikTok/Reels ad", or when the user sends Atria inspiration ad links for video.
---

# Video ads (short form, from existing footage)

Engine: `ads/video/build.py` (edit.json → finished MP4s + QA sheet), `ads/video/triage.py` (contact
pages for a batch of raw clips). Brand facts, claims and personas come from the brand's
`brand.json`: read it first, same rules as the `static-ads` skill (claims_to_avoid, women-only, etc.).

Per brand, video work lives in `ads/brands/<brand>/video/`:
- `footage.csv`: the tagged footage library (drive id, folder, seconds, **rights**, tags, best
  in/out ranges, burned-in text, notes). Read it first; add every clip you review.
- `<YYYY>-W<ww>/<ID>_<slug>/edit.json`: one folder per ad, ids `V<ww>_nn_slug`, with its renders
  next to it (`<id>.mp4`, `<id>_4x5.mp4`, `<id>_sheet.jpg`).

Downloads cache in `ads/.cache/footage/` (gitignored). Drive files shared by link download with
`drive:<fileId>` straight from the engine; no connector call needed.

## 1. Research (every new angle)

**Inspiration ads the user sends** (`app.tryatria.com/ad/<id>`): `get_library_ad` → video URL;
`curl` the mp4 into the scratchpad, then *watch it*:
`python ads/video/build.py --sheet <mp4> --every 1` (0.5 for ads under 10s) and Read the sheet.
`get_library_ad_transcript` is free; many native ads have none (music only). Write down per ad:
length, number of cuts, caption style and position, hook in the first 1.5s, structure, CTA.

What the Oct–Nov 2026 inspo set has in common (Dr. Woof ×4, Harmonia, BitePal, LuxeLight):
- 6–20s, real phone footage, 1–2.5s per cut, product shown *in use*.
- **Text on screen carries the story; no voiceover.** TikTok-classic captions: white rounded box
  with black text, or white text with a thin outline; centered; upper-middle of frame.
- Formats: **persistent callout header + changing story captions** ("Flight compression socks for
  men" / "POV: he won't board without…" → "So I got him these" → "Maybe one for you");
  **meme flip** ("Vets wearing scrubs made for human med 💀" → "us: … FOR VETS 💅"); **single
  caption over a try-on** ("Wearing … for the first time and loving it >>>"); one-line self-aware
  joke ("I may never be an airport fashion icon…but no varicose veins babe 💋").
- The CTA is soft (last caption or a brand pill); the button does the selling.

**The brand's own winners for the angle** (Atria ad account, `list_ad_accounts` → id):
`list_ad_account_ads period=last_30d limit=50` (sorted by spend), find the angle's ads by name,
`get_ad_account_ad` for copy + video URL, `get_ad_account_video_transcript` (free). The script you
write keeps the winner's *angle and proof points* and moves it into the short native format.

## 2. Footage

1. **Inventory** (first time per brand, then refresh new folders only): crawl the asset folder
   with Drive `search_files` (`parentId = '<id>'`, `excludeContentSnippets: true`, `pageSize: 100`,
   follow `nextPageToken`, recurse into folders). A subagent does this well; have it write a TSV
   (path, id, title, mimeType, size, created, owner).
2. **Triage**: write `drive:<id>\t<label>` lines for candidate folders, run
   `python ads/video/triage.py clips.tsv <scratch>/triage/`, Read every page, shortlist.
3. **Shortlist sheets**: `python ads/video/build.py --sheet drive:<id> --every 0.5` per clip; note
   usable in/out ranges, framing, and **burned-in creator text** (crop it out with `zoom` +
   `focus_y`, or skip the clip). Record each in `footage.csv`.
4. **Rights**: tag every clip `owned_creator`, `owned_agency`, `ai_generated` or
   `third_party_tiktok`. Snaptik/TikTok downloads are other people's videos: tell the user in the
   delivery message which shots are third-party so they can confirm permission/whitelisting
   before spend. Prefer owned footage for the product shots, always.

## 3. Script → edit.json

- **Angle** from the winner + persona from brand.json. **Format** from the inspo list above.
- 15–20s, 6–9 cuts. **Hook in the first frame** (strongest visual + caption visible at t=0).
  Order: problem (1–2 cuts) → turn ("so I switched…") → product proof on the body (2–3 cuts, one
  feature each) → payoff in the setting → brand pill.
- Captions: one idea each, ≤ 8 words, audience's voice (casual, a little self-aware, emoji at the
  end). Product facts and claims only from brand.json; nothing from `claims_to_avoid` (Comfort
  Wear: no guarantees, review counts or star ratings, no medical/podiatrist claims on screen).
- Respect the audience: celebrate, don't mock (plus-size: no "struggling to fit" punchlines).
- Caption timings must match the cumulative clip boundaries (sum of `(out-in)/speed`). Set the
  last captions' `end` to 99 (clamped to the video length).
- Keep caption `y` between 0.18 and 0.72 (inside the 4:5 feed crop, clear of the TikTok/Reels UI),
  and off faces and the product. Persistent header at y≈0.2 in `dark` style; story captions in
  `box`; brand name as a `brand` pill on the last shot.
- Also write `primary_text`, `headline`, `cta`, `link` in edit.json (reuse the winner's landing
  page).
- Schema and options (`zoom`, `focus`, `focus_y`, `push`, `speed`, `gain`, `eq`, `music`): see the
  docstring at the top of `ads/video/build.py`.

## 4. Render

```bash
python ads/video/build.py ads/brands/<brand>/video/<week>/<id>/edit.json --sheet-every 0.5
```
~80s for an 18s ad. Outputs 1080×1920 H.264 30fps (-14 LUFS), the 1080×1350 feed crop, and a sheet.

**Audio**: TikTok downloads carry their creators' music; don't cut it together (choppy, and not
licensed). Default: `gain: 0` on every clip and the music added at upload from Meta Sound
Collection / TikTok Commercial Music Library. If the user wants a bed baked in, generate a
royalty-free track (Atria `ad_maker_generate_music`, ~$0.60 for 20s; **ask first, it spends
credits**), save it next to edit.json and set `"music": {"file": "<path>", "gain": 0.5}`.

## 5. QA (always, before showing anything)

Read `<id>_sheet.jpg`, then pull full-size frames at the middle of every cut from both the 9:16 and
the 4:5 file (`ffmpeg -ss <t> -i <file> -frames:v 1 -vf scale=360:-2 f.png`, `hstack` 4 per row)
and Read them. Fix and re-render anything with:
- burned-in creator text, watermarks, other brands' logos as the hero;
- captions on faces or on the product, orphan words/emoji on a line, text outside y 0.18–0.72;
- a caption that changes mid-shot or outlives its shot; an empty last half-second;
- the wrong product/colorway, a product shot that doesn't show the feature its caption names;
- dark or soft shots (`eq` brightness/contrast; avoid sub-720p sources for product shots);
- claims outside brand.json; a tone that mocks the audience.

## 6. Deliver

1. Commit the ad folder (edit.json + renders) and `footage.csv`; push to the working branch.
2. `SendUserFile` the 9:16 MP4 (`display: render`) and the sheet; in the message give: the
   script (shot → caption table), source winner + inspo it borrows from, primary text/headline,
   which shots are third-party footage, audio status, and what to test next (hook variants).
3. If the brand has Drive/Slack delivery set up (`drive_folder_id`, `slack`) and the user wants
   it, mirror the static-ads delivery (Drive folder for the week, Slack DM with links).

## Iterating

Hook tests are cheap: copy the folder to `V<ww>_nn_<slug>_h2`, change only the first clip and
caption, re-render. Log what the user approves/rejects in `ads/brands/<brand>/video/feedback.md`
and read it before the next script.
