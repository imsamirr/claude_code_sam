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
- **Video files:** a 5-minute Veo render is 50–110MB. Compress a copy for Notion to about 18MB, under its 20MB single-part limit. Text stays sharp at this setting:
  ```bash
  ffmpeg -i LVxx.mp4 -c:v libx264 -preset veryfast -b:v 380k -maxrate 420k -bufsize 840k -c:a aac -b:a 64k -movflags +faststart notion/LVxx.mp4
  ```
  Call `notion-create-file-upload` with `content_type: "video/mp4"`, because the default `application/mp4` rejects a `video/mp4` POST. POST the file right away, and create the card within the hour. Embed it with `<video source="file-upload://<id>">LVxx video</video>`. For anything over 20MB, use Drive (`create_file` with a `sha256:<hash>:<path>` reference) and link to it.
- **Before the final render, fact-check the on-screen text:** city and state pairs, spacing inside quotes, prices that add up. A mistake means re-rendering the video.
- **Sample:** send one video with SendUserFile.


## Cheap mode (default for the weekly batch, user decision 2026-11-11)

- **Background:** one **dedicated** still image per video, made with Kie nano-banana-pro (about 15 credits) from the spec's `background_image_prompt`, then a slow zoom in and out on a 40-second seamless loop. This costs about 10× less than 2 Veo clips (about 130 credits, or about $0.70 per video).
- **Never reuse images.** Never share one image across concepts, and never reuse the concept's static images A–D. Every video gets its own scene, in the same iPhone-realism style.
- **Music:** the angle's bed from `ads/brands/<brand>/assets/music/<angle>.mp3` (Suno, made once). Mapping: europe, disney, plussize, nurse, over50.
- **Voice:** none while Kie ElevenLabs is failing (Internal Error on 2026-11-11). The scroll runs at reading pace, about 2.4 words per second (`--no-voice`).
- **File size:** rendered at 400 kbps, so a 5-minute video is about 19MB and can be attached directly to its Notion card.

```bash
python ads/scroll_video.py --brand <brand> --spec <scroll_specs.json> --music ads/brands/<brand>/assets/music/<angle>.mp3 --only render --no-voice <IDs>
```

**Kie balance:** check it first (`GET /api/v1/chat/credit`). A negative balance means every generation fails.
