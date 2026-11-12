# Scrolling long-form video ads

**The format:** one looping background clip of the narrator's world. The full story scrolls up from the bottom in big bold outlined text, and a voice-over reads it word for word over a soft music bed. The video runs 4–5 minutes, and the Facebook caption is short.

## Studied examples (Atria, saved 2026-11)

| Ad | Length | Background | Text | Audio |
|---|---|---|---|---|
| Cat Care Corner (m1845460936626768), vet "pulled 40 senior cats", #1 of 122 in-account | 5:22 | vet in a clinic room | yellow, black outline | music/VO |
| FluffCo (m926031156988423), hotel front desk "What if I just steal one?" | 4:51 | hotel hallway, someone carrying a pillow | white, black outline | music only |
| Albert H. Benton (m1476614284352616), physical therapist on sciatica | 4:24 | PT treating a patient | white, black outline | voice-over reading the text |

**What they share:**
- **Frame:** 720×1280 at 30fps.
- **Opening:** the hook sits in the lower half at second 0, then scrolls at reading pace (about 2.3–2.5 words per second, about 650–750 words in total).
- **Text:** paragraphs of 1–3 short sentences, centered, about 86% of the frame width.
- **Caption:** 1–3 sentences (the hook plus curiosity).

## Pipeline: `ads/scroll_video.py`

```bash
python ads/scroll_video.py --brand <brand> --spec <variations.json> --only assets --tts openai [IDs]  # voices + Veo clips + tile sheets
# review every <ID>/bg_*_tiles.jpg; delete + re-run bad clips
python ads/scroll_video.py --brand <brand> --spec <variations.json> --music <bed.mp3> --only render [IDs]
```

### The spec (one object per variation)

| Field | What it holds |
|---|---|
| `id` | LV<nn> |
| `script` | Paragraphs separated by blank lines, 600–720 words |
| `voice` | Gender, age and accent notes for the narrator |
| `background` | Veo prompt for the narrator's world |
| `caption`, `headline`, `landing_page` | The ad's caption, headline and landing page |
| `offer_swaps`, `alt_hooks` | Dated offer replacements and alternate openings |
| `text_color` | Optional: white or yellow |

### Spec fields for still-image and music-only videos (from DentalPULSE, 2026-11; both brands)
- **Background photo:** `background_image_prompt` (preferred) or `background_image` (older DentalPULSE specs put the prompt here; a path to an existing file is used as-is). It's rendered with Kie `nano-banana-pro` at 2K, then the HQ render below (no Veo). Keep the middle of the frame calm and mid-to-dark, because white text sits on it.
- **`"audio": "music"`** (or `--no-voice`): no voice-over. It renders with the HQ still-image mode below (1 px per frame at 50 fps, about 2.2 words a second). Write these scripts with shorter paragraphs and more one-line cliffhangers.
- **Scroll speed (user feedback 2026-11-12, both brands):** the text must rise slowly from the first frame, like the references, never jump. In HQ mode the hook starts at 60% height and rises at a steady 50 px/s. Voice videos stay at a steady speed until they reach the voice's place, then follow the voice.
- **Music beds:** without `--music`, one Suno bed is generated per spec file (`<stem>_music.mp3` next to it) and shared by its variations. Set `music_prompt` on the first variation to change the mood.
- **Voice availability (2026-11-12):** Kie's ElevenLabs models (turbo-2-5 and multilingual-v2) returned "Internal Error", and the OpenAI fallback needs account credits. Check both before a voice batch.

### What each stage does

- **Voice:**
  - ElevenLabs via Kie (`elevenlabs/text-to-speech-turbo-2-5`) is the first choice. Both Kie ElevenLabs models returned "Internal Error" on 2026-11-11.
  - The fallback is OpenAI `gpt-4o-mini-tts` (voice `sage`, read as a real woman telling her own story) with `--tts openai`. Report which one was used (`<ID>/voice_engine.txt`).
  - The voice is generated in sections of about 110 words. Paragraph start times come from section durations split by word count. The text layer's y-position is piecewise linear, so each paragraph reaches the reading line (30% down) when the voice starts it.
- **Background:**
  - Kie `veo3_fast` makes 2 clips of 8 seconds from the **same prompt**, so they're two moments of one place. They're crossfaded, looped, darkened slightly, and Veo's own audio is dropped.
  - Never write "iPhone video" in the prompt, because Veo then draws a phone frame. Say "raw handheld footage… the camera itself is never visible". "A different angle" drifts to a different town.
- **Music:** one Suno V4_5 instrumental bed per angle (a soft piano or acoustic mood, no drums), mixed at −24 dB under the voice and faded out at the end.
- **Text:** Montserrat ExtraBold (`ads/assets/fonts`, OFL) at 46px with a 5px black stroke, white by default.

### QA, in this order

1. Tile sheets of every clip: no phone frame, no logos, no characters, the right setting. Also check:
   - **Letterbox bars:** Veo sometimes returns 9:16 with black bars baked in. Run `cropdetect` on every clip; when it isn't `720:1280:0:0`, crop to 9:16 inside the bars and scale back to 720×1280.
   - **Folded or bent geometry:** wide river and landscape scenes at 9:16 come back with the far bank bent up into a wall (LV01 failed this twice). Use an interior or close scene instead, or switch that video to a cheap-mode image.
   - **The background matches the final script:** when a story detail is changed (for example frozen peas to a foot tub), update the `background` prompt too and regenerate the clips.
2. Frames at 0.5s, 30s and 2 minutes, plus the last 10 seconds: the hook is visible at the start, the text is legible, and the CTA rests on screen at the end.
3. Duration matches the voice.
4. Spot-check that the voice is in sync with the text.

## Writing

Use the writer spec in `ads/brands/comfortwear/output/scroll_videos/scripts/WRITER_SPEC.md`. It's the long-form rules adapted for the ear:
- no symbols, and numbers written as they're spoken
- 600–720 words
- the hook is on screen at second 0
- the source ad's DNA is kept
- 3 variations per angle, each a different story and background
- the brand's dated close

**Names:** dedupe them across the batch (narrators, messengers and towns) and against existing LF files. Never reuse a competitor's signature detail (for example Orthora's frozen peas).

## Delivery
- **Notion:** one card per angle on the brand's board (Comfort Wear's is the "ComfortWear Video Board" database, data source `fc6096bb-…`), titled `LV01–03 | Scroll Video | <Angle>`. List the 3 variations on it, each with: story, headline, caption, the video, the full on-screen script, offer swaps and alternate hooks. Escape `$` as `\$` in the content, or Notion may read prices as math.
- **Video files (superseded, see HQ mode below):** do NOT put an 18MB re-compressed full-length video on a card. The user rejected that quality. The command below is kept only for short clips:
  ```bash
  ffmpeg -i LVxx.mp4 -c:v libx264 -preset veryfast -b:v 380k -maxrate 420k -bufsize 840k -c:a aac -b:a 64k -movflags +faststart notion/LVxx.mp4
  ```
  Call `notion-create-file-upload` with `content_type: "video/mp4"`, because the default `application/mp4` rejects a `video/mp4` POST. POST the file right away, and create the card within the hour. Embed it with `<video source="file-upload://<id>">LVxx video</video>`. For anything over 20MB, use Drive (`create_file` with a `sha256:<hash>:<path>` reference) and link to it.
- **Before the final render, fact-check the on-screen text:** city and state pairs, spacing inside quotes, prices that add up. A mistake means re-rendering the video.
- **Sample:** send one video with SendUserFile.


## Still-image HQ mode (the default, user decision 2026-11-11: "the main purpose of the video is the text")

The user rejected the first renders as poor quality. Those were 720p Veo backgrounds compressed to 380 kbps to fit Notion. Every video now uses the following.

**Background.** One dedicated still photo per video from the spec's `background_image_prompt`, made with Kie nano-banana-pro at **2K, 9:16**. It's a moment from that story, in the iPhone-snapshot style. Never share one across videos. Check every photo for readable text (shirts, signs) and logos.

**Render** (`build_still` in `scroll_video.py`):
- 1080×1920, text at 1.5× the 720p sizes (69px Montserrat ExtraBold, 8px stroke)
- **exactly 1 px per frame at 50 fps** (50 px/s, about 2.2 words a second). Whole-pixel steps don't shimmer; fractional speeds are rounded and judder.
- the hook starts at 60% height and rises slowly; the CTA rests mid-screen for 3 seconds at the end
- a light `gblur=sigma=2` on the photo. Detailed textures behind moving text otherwise double the file size (390MB vs 155MB on cobblestones), and the text is the ad.
- x264 `-preset fast -crf 27 -maxrate 4500k`: crisp text at about 3–4.5 Mbps, so 5.5 minutes is about 120–180MB
- the text layer is padded by one screen above and below, and the visible 1080×1920 window is cropped from it each frame. Overlaying the full 16k-pixel layer is 2–3× slower. Each video takes about 4 minutes to render.

**Delivery.** Full files are 90–180MB, which is over Notion's 20MB limit and the Drive connector's 10MB limit, so they go up through the Drive API:
- **Full files go to Google Drive (user setup 2026-11-12):** `python ads/drive_upload.py --folder <brand.json longform_program.scroll_video_drive_folder> <files>` uploads each full-quality video with the Drive API: resumable, about 10–20 s per 100–180MB file. Credentials are env `GDRIVE_CLIENT_ID`, `GDRIVE_CLIENT_SECRET` and `GDRIVE_REFRESH_TOKEN` (the user's own OAuth app). It prints JSON lines with `id` and `link`. Name each file like its Notion concept: `<ID>.mp4::<ID> - <Concept title> - <Angle>.mp4` (the user asked for this on 2026-11-12). Re-uploading the same name updates that file in place, so links stay valid. On each Notion card, write `[Download <ID> from Google Drive](https://drive.google.com/file/d/<id>/view) · <size, length> · full quality`. Don't write the bare file name: Notion turns "LV01.mp4" into a broken link. If the Drive variables are missing or the upload fails, fall back to SendUserFile download cards in the chat and say so.
- on Notion, attach a **30-second full-quality hook preview** (`-t 30 -c:v copy`, about 15MB), plus that "Full video" note
- never put a re-compressed under-20MB full-length video on a card. That's what looked bad.
- existing video blocks can't be matched by `update_content`. To swap videos, rewrite the card with `replace_content`.

## Cheap mode (superseded by the HQ mode above)

- **Background:** one **dedicated** still image per video, made with Kie nano-banana-pro (about 15 credits) from the spec's `background_image_prompt`, then a slow zoom in and out on a 40-second seamless loop. This costs about 10× less than 2 Veo clips (about 130 credits, or about $0.70 per video).
- **Never reuse images.** Never share one image across concepts, and never reuse the concept's static images A–D. Every video gets its own scene, in the same iPhone-realism style.
- **Music:** the angle's bed from `ads/brands/<brand>/assets/music/<angle>.mp3` (Suno, made once). Mapping: europe, disney, plussize, nurse, over50.
- **Voice:** none while Kie ElevenLabs is failing (Internal Error on 2026-11-11). The scroll runs at reading pace, about 2.4 words per second (`--no-voice`).
- **File size:** rendered at 400 kbps, so a 5-minute video is about 19MB and can be attached directly to its Notion card.

```bash
python ads/scroll_video.py --brand <brand> --spec <scroll_specs.json> --music ads/brands/<brand>/assets/music/<angle>.mp3 --only render --no-voice <IDs>
```

**Kie balance:** check it first (`GET /api/v1/chat/credit`). A negative balance means every generation fails.

## Voice-over with ElevenLabs (user rules 2026-11-12: at most 5,000 credits per run, 1–2 voiced concepts)

- **Key:** env `ElevenLabKey` (direct ElevenLabs API, not Kie). It can't read the account or list voices, so the voice IDs are fixed in `EL_VOICES` (US voices: Rachel, Matilda, Aria, Jessica, Laura).
- **Opt in per video** with `"voiceover": true` in the spec. Pick the **1–2 concepts with the strongest hooks** for voice. Every other video stays music-only.
- **Voice choice:** `"el_voice": "<name>"`, or by default from the narrator's age in `"voice"`: 55+ gets Matilda, under 42 gets Jessica, everyone else Rachel.
- **Cost:** the model is `eleven_turbo_v2_5`, at 0.5 credit per character, so a 700-word script is about 2,000 credits.
- **Hard caps in the script:** 5,000 credits and 2 voiced videos per UTC day, tracked in `output/scroll_videos/_elevenlabs_ledger.json` across separate invocations. Override with `ELEVENLABS_RUN_BUDGET` / `ELEVENLABS_MAX_VOICED` only if the user raises the limit.
- **Over the cap:** the video falls back to music-only and the log says so. Report the credits used in the run summary.
- **Render:** the whole script is read in one request, so the narration flows naturally. Symbols are spoken naturally (HSA and FSA, percent). The text still moves exactly 1 px per frame, with the frame rate (24–60) chosen so the scroll lasts as long as the narration. The music bed plays at about −18 dB under the voice.
