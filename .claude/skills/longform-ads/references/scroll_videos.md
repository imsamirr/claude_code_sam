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

### Still-image backgrounds and music-only videos (added for DentalPULSE, 2026-11)
- **`background_image`** (instead of `background`): a prompt for one calm, mid-to-dark 9:16 phone photo of the narrator's world. It's rendered with Kie `nano-banana-pro` at 2K, then given a slow breathing zoom over the whole video (no Veo). Keep the middle of the frame quiet, because white text sits on it.
- **`"audio": "music"`**: no voice-over. The text scrolls at a fixed reading pace (`MUSIC_WPS` = 2.5 words a second, with the hook held for 2.5 seconds) and the music bed plays at −6 dB. Write these scripts with shorter paragraphs and more one-line cliffhangers.
- **Scroll speed (user feedback 2026-11-12):** the text must rise slowly from the first frame, like the references, never jump. Music-only videos scroll at one steady speed (story length ÷ runtime, about 35–40 px/s) after an ease-in at a third of that speed for the first 6 seconds. Voice videos stay at that steady speed until it reaches the voice's place, then follow the voice.
- **Music beds:** without `--music`, one Suno bed is generated per spec file (`<stem>_music.mp3` next to it) and shared by its variations. Set `music_prompt` on the first variation to change the mood.
- **ElevenLabs direct (2026-11-12):** the user added an ElevenLabs API key as the environment variable `ElevenLabKey`. Whenever it is set, `scroll_video.py` uses the ElevenLabs API directly first (`eleven_multilingual_v2`, Rachel for women and Brian for men, or `el_voice_id` in the spec), then falls back to Kie, then OpenAI. Use `--tts elevenlabs` to force it.
- **ElevenLabs credit cap (user rule 2026-11-12):** at most 5,000 ElevenLabs credits per run. The default model is `eleven_turbo_v2_5` at 0.5 credit per character, so a ~700-word script costs about 2,000 credits and at most 2 voice videos fit per run; every other video is music-only. `scroll_video.py` enforces this: each voice video reserves its credits in a per-day ledger (`elevenlabs_credit_ledger.json`, shared by parallel processes), and one that would go over `--voice-budget` (default 5000) is rendered music-only with an `audio_note`. Check the real usage with `GET https://api.elevenlabs.io/v1/user/subscription` (`character_count`) before and after.
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

1. Tile sheets of every clip: no phone frame, no logos, no characters, the right setting.
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
- **Drive API uploader (2026-11-12):** `python ads/drive_upload.py --brand <brand> --folder-id <id> --names <map.json> <files>` uploads files of any size (resumable) and prints each Drive link. It needs `GDRIVE_CLIENT_ID`, `GDRIVE_CLIENT_SECRET` and `GDRIVE_REFRESH_TOKEN`, an OAuth refresh token for the Drive owner with the `drive` scope, set up through Google Cloud and the OAuth Playground. Use it instead of the Drive connector, which caps files at about 3 MB. The folder id and naming rule live in `brand.json → longform_program.scroll_videos`.

- **Notion:** one card per angle, listing its 3 variations: script, caption, headline, landing page, Drive link.
- **Video files:** 5-minute videos are 50–90MB, over Notion's 20MB single-part limit and too big for git. Upload them to the brand's Drive folder with `create_file` and a `sha256:<hash>:<path>` file reference (each needs the user's approval), and link them from the cards.
- **Sample:** send one video with SendUserFile.
