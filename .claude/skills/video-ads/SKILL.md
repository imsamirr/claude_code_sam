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
4. **Rights (user rule, Comfort Wear)**: third-party TikToks from individual creators are OK;
   never use other brands' own content (their ads, promos, product videos). Tag every clip `owned_creator`, `owned_agency`, `ai_generated` or
   `third_party_tiktok`. Snaptik/TikTok downloads are other people's videos: tell the user in the
   delivery message which shots are third-party so they can confirm permission/whitelisting
   before spend. Prefer owned footage for the product shots, always.

## 3. Script → edit.json

**Direct-response copy (user rule: aggressive DR).** Study the references (user's Atria links +
`search_library_ads` with `order=best_match`, `active_since` last ~75 days, `min_days_running`
14+, the category's pains as query) and read their transcripts. The structure that wins
(Orthora nurse shoes, WideStep, Koprez, Stepprs, Wooten):
1. **Callout hook** that names the audience and a command or warning: "If you're plus-size and going
   to Disney, do not wear your gym sneakers." / "Nurses: don't make my mistake." / objection reply
   ("I'd try them but they're too expensive" → "Well, it's your lucky day").
2. **Agitate** with a specific, felt moment: "by hour five", "sit on the stairs just to get my shoes off".
3. **Name the enemy**: running shoes, narrow toe boxes, memory foam that goes flat, $150 brand shoes.
4. **Mechanism**: one feature per beat, each tied to the pain (wide toe box → room to swell).
5. **Proof**: personal numbers (22,000 steps, 10,000 steps, 3 nurses on my floor), no unconfirmed counts.
6. **Offer + urgency + hard CTA**: the current offer (Black Friday 60% off + 2 free gifts), "ends soon",
   "stop scrolling and grab a pair", "tap the link before it's gone".
Visual style: a hook header in the first second, VO-synced word-chunk subtitles (2–4 words) low in the
frame, a cut every 1.5–3 s, a big callout (score, offer, "ENDS SOON") on key beats.

**Subtitles from the voiceover**: in `voiceover` add `"lines": [...]` (one string per scene, the exact
words, numbers as digits) and `"sub": {"style": "box", "size": 58, "y": 0.68, "max_words": 4}`; the
engine times chunks to the speech of each line. Pass `"segments"` explicitly when short beats
("Hokas, four out of ten.") would confuse automatic sentence detection.

**Scenes (user rules)**: no source clip appears in more than one ad of the batch; run
`python ads/video/check_batch.py ads/brands/<brand>/video/<week>/` before rendering. Build a big
enough pool first (triage the brand's B-roll folders: creators with full scene sets — pain, shoes
off, putting on, car, at work — make the strongest testimonials).
**Text never covers the main elements (user rule)**: captions are moved off faces automatically (OpenCV
face detection, `pip install opencv-python-headless==4.10.0.84`; OpenCV 5 lacks the detector), off
other captions, and off a clip's `"keep_clear": [[y0, y1]]` bands (use for the product). Still read
the QA strip for eyes, product and action.
**Blur competitor branding (user rule: always blur Skechers logos/markings)**: per clip
`"blur": [{"box": [x0, y0, x1, y1], "t": [a, b], "strength": 28}]` (fractions of the 1080×1920
frame, optional seconds within the clip). Find the logo on gridded frames
(`drawgrid=w=108:h=192`) over the chosen window, prefer windows where the logo stays put, and check
the render frame by frame.

- **Angle** from the winner + persona from brand.json. **Format** from the inspo list above.
- 15–20s, 6–9 cuts. **Hook in the first frame** (strongest visual + caption visible at t=0).
  Order: problem (1–2 cuts) → turn ("so I switched…") → product proof on the body (2–3 cuts, one
  feature each) → payoff in the setting → brand pill.
- Captions: one idea each, ≤ 8 words, audience's voice (casual, a little self-aware, emoji at the
  end). Product facts and claims only from brand.json; nothing from `claims_to_avoid` (Comfort
  Wear: no guarantees, review counts or star ratings, no medical/podiatrist claims on screen).
- Respect the audience: celebrate, don't mock (plus-size: no "struggling to fit" punchlines).
- **Scene = caption (user rule)**: every scene must show what its caption/VO line names. "Nike
  Air Max: 5/10" plays over Nike Air Max footage, "Hokas" over Hokas, "slip-resistant" over the
  outsole, "3 nurses on my floor" over a nurse at work. If the only clip of a competitor has
  burned-in text, put the caption exactly over it (measure its y on a frame) with `"delay": -0.25`
  so it's covered from the first visible frame. Competitor shoes may appear when named (this
  overrides the statics' "no other brands' products" rule).
- **Unique concepts (user rule)**: every video in a batch has its own concept (angle + format +
  hook). Don't make two videos for the same angle in one batch, and spread footage so the same
  clip isn't the hook or hero of more than one video.
- **Congruence (user rule)**: every scene must fit the concept's audience and setting. A
  "plus-size Disney" ad shows only plus-size women and/or Disney, including the product shots
  (use a plus-size creator such as Larissa for those). No generic feet, car or home b-roll that
  breaks the world of the ad.
- **Spanish ads**: `"lang": "es"` picks the Spanish end card automatically (`video.end_cards[].lang`).
  New Spanish cards are rebuilt from the English one with `ads/video/make_end_card_es.py`
  (inpaints the English elements, redraws them in Spanish, animates the build).
- **End card (user rule)**: set `"end_card": "auto"` and `"created": "<YYYY-MM-DD>"`. The engine
  appends the brand's card from `brand.json` → `video.end_cards`: Comfort Wear uses the Black
  Friday card for creatives made **on or before 2026-11-23**, the regular card after. The last
  scene's captions end where the card starts (don't put text over the card).
- **Time captions by scene**, not by seconds: `"clip": 3` (one scene) or `"clips": [0, 7]` (a
  header across scenes). The engine works out the times, including crossfades, so captions switch
  exactly with the picture. Captions fade in/out over 0.12s (the first one is on screen at t=0).
- **Caption size (user rule)**: story captions `size` 64, `width` 0.88; header `size` 60.
- **Transitions (user rule)**: scenes join with a 0.25s crossfade (`"transition": "fade"`,
  `"transition_duration": 0.25` at the top level; per clip `"transition": "cut"` for a hard cut
  or any ffmpeg xfade name). The end card fades in over 0.35s.
- **No glitches (user rule)**: never use `push` (per-frame rescaling jitters; it is ignored now);
  use a static `zoom`. Every clip is converted to a constant 30 fps before scaling.
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

**Voiceover** (when the user asks for one; ~1 Atria credit per take):
1. Voice from `brand.json` → `video.voiceover` (Comfort Wear: **Harper**, chosen for "a high-quality
   woman in her 30s"). Speech needs an Atria project id (`ad_maker_create_video_project` once,
   saved in brand.json); `ad_maker_generate_speech` then `ad_maker_get_task` for the mp3 URL.
2. **Sound human (user rule)**: write it the way a person talks to a friend: contractions, small
   connectors ("Okay, so…", "Turns out,", "And yes,"), commas where she'd breathe, one sentence
   per scene, normal punctuation. **Never** put ` ... ` between lines (it makes ~1s robotic gaps).
   Generate the whole script as **one take** and save it as `vo/<voice>_natural.mp3`.
3. Add `"voiceover": {"file": "vo/<voice>_natural.mp3", "mode": "continuous", "tempo": 1.05,
   "lead": 0.15, "tail": 0.35}`. Continuous mode plays the take unbroken and **cuts the picture in
   the breath between sentences** (the n-1 longest pauses = sentence ends; commas stay inside a
   line). It rewrites each clip's `out`, so give enough source footage after `in`. `tempo` (pitch
   kept) trims a long read; keep it at 1.0–1.08. `"mode": "lines"` places each line at its scene
   start instead (more robotic; only for very short scenes). The end card's own line
   (`video.end_cards[].vo`, recorded once per card in the same voice) plays over the card, so the
   spoken offer always matches the card on screen.
   **Music bed (user rule: low volume, so the VO isn't monotone)**: generate an instrumental with
   Atria `ad_maker_generate_music` (elevenlabs/music, ~$0.60, 30–35s, prompt: genre/instruments
   matching the ad's world, "sits under a voiceover, no vocals, no drops, steady energy") into
   `vo/music_<slug>.mp3`, then `"music": {"file": "vo/music_<slug>.mp3", "gain": 0.15, "duck": true}`
   → the bed sits ~16 dB under the voice and ducks further while she talks. Trending TikTok songs
   are not cleared for paid ads: those get added at upload from TikTok's Commercial Music Library
   / Meta Sound Collection, on a music-free export (`"music"` removed).
4. Make captions say the same words as the voice (shortened is fine).
5. QA the sync: `ffmpeg -i <id>.mp4 -af silencedetect=noise=-38dB:d=0.25 -f null -` and check
   every spoken stretch sits inside its scene window (printed by the build); loudness about -14
   LUFS with peaks under -1 dBFS (`-af ebur128=peak=true`). Can't hear it? Compare voices by
   measurement (median pitch, pitch movement, pace) and say so.

## 5. QA (always, before showing anything)

`python ads/video/qa.py <id>.mp4` runs all of the checks below and writes `<id>_qa.png`: one frame
from the middle of every scene, 9:16 on top and 4:5 below. Read it. It must print PASS.

The same checks by hand:
```bash
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames,avg_frame_rate -of csv=p=0 <id>.mp4   # frames == 30 x duration
ffprobe -v error -select_streams v:0 -show_entries packet=pts_time -of csv=p=0 <id>.mp4 | sort -n | awk 'NR>1{d=$1-p; if (d>0.0345||d<0.032) print "gap",p,$1} {p=$1}'   # no output
ffmpeg -i <id>.mp4 -vf freezedetect=n=0.002:d=0.3 -map 0:v -f null - 2>&1 | grep freeze_start   # no output (except a static end card)
```
Then read `<id>_sheet.jpg`, then pull full-size frames at the middle of every cut from both the 9:16 and
the 4:5 file (`ffmpeg -ss <t> -i <file> -frames:v 1 -vf scale=360:-2 f.png`, `hstack` 4 per row)
and Read them. Fix and re-render anything with:
- burned-in creator text, watermarks, other brands' logos as the hero;
- captions on faces or on the product, orphan words/emoji on a line, text outside y 0.18–0.72;
- a caption that changes mid-shot or outlives its shot; an empty last half-second;
- the wrong product/colorway, a product shot that doesn't show the feature its caption names;
- dark or soft shots (`eq` brightness/contrast; avoid sub-720p sources for product shots);
- claims outside brand.json; a tone that mocks the audience.

## 6. Deliver

**Drive upload (user rule: finished videos go to the brand's Drive video folder,
`brand.json` → `video.drive_folder_id`).** The Drive connector caps each call at ~3 MB, so upload
with the Drive API instead (uses `GDRIVE_CLIENT_ID/SECRET/REFRESH_TOKEN` from the environment,
resumable, shared drives OK, re-run safe):
```bash
W=$(python ads/video/drive_upload.py <drive_folder_id> --mkdir "<YYYY>-W<ww>")
python ads/video/drive_upload.py $W ads/brands/<brand>/video/<week>/*/V*.mp4      # 9:16 + 4:5
```

1. Commit the ad folder (edit.json + renders) and `footage.csv`; push to the working branch.
2. `SendUserFile` the 9:16 MP4 (`display: render`) and the sheet; in the message give: the
   script (shot → caption table), source winner + inspo it borrows from, primary text/headline,
   which shots are third-party footage, audio status, and what to test next (hook variants).
3. If the brand has Drive/Slack delivery set up (`drive_folder_id`, `slack`) and the user wants
   it, mirror the static-ads delivery (Drive folder for the week, Slack DM with links).

## Iterating on the account's winners ("iterate our top ads")

1. Pull winners from Atria: `list_ad_accounts` → `list_ad_account_ads period=last_14d
   metrics=spend,roas,purchases,cost_per_purchase,ctr_all` (sorted by spend), keep the user's
   threshold (Comfort Wear Nov 2026: **$1,000+ spend and ROAS > 1.7 over 14 days**, top 5 by
   spend). Check every connected account for the brand (WearOrtho, WearOrtho V2).
2. Study each: `get_ad_account_ad` (copy, headline, landing page, video URL),
   `get_ad_account_video_transcript` (free), download and watch the video as a sheet. Statics
   count too: their headline + proof points become a product-demo video.
3. One iteration per winner: keep its **angle, audience and proof points**, move it into a
   different short-form inspo format, and keep its landing page and language. Match formats to
   winners: rating/ranking → "Brand: x/10" captions; testimonial UGC → header + story captions
   with first-person VO; doctor/expert ratings in Spanish → Spanish meme flip (text only); a winner
   already iterated → a second, different format (one-liner over montage); a static → product demo
   with the static's feature icons as pills, offer left to the end card.
4. Record `based_on` (ad name, spend, ROAS) in every edit.json, and drop claims from the source
   that are in `claims_to_avoid` (guarantees, podiatrist, review counts).

## Iterating on our own ads

Hook tests are cheap: copy the folder to `V<ww>_nn_<slug>_h2`, change only the first clip and
caption, re-render. Log what the user approves/rejects in `ads/brands/<brand>/video/feedback.md`
and read it before the next script.
