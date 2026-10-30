---
name: video-ads
description: Make a brand's video ads (story/dialogue dramas, UGC edits, b-roll + voiceover) from a reference video, Drive footage, AI-generated clips (kie.ai, Sora) or organic inspo clips. Covers the required order of work (brief → frame-by-frame samples → full edit), matching a reference frame by frame, direct-response research on Atria, and where footage lives. Use for "edit a video ad", "make it look like this video", "video brief", "b-roll edit", "story ad", or any video creative request.
---

# Video ads

## Order of work (the user's standing rule — never skip a gate)

1. **Brief first.** Write the brief (or take the one the user provides) and stop. Get approval before anything else.
2. **Frame-by-frame samples next.** Show key frames, one per beat, each side by side with the matching
   reference frame, plus one short clip. The user leaves revisions. Stop again.
3. **Full edit only after samples are approved**, then a rough cut for notes, then the final.

Quote generation costs before any paid step (kie.ai, Sora, image models) and wait for a go-ahead.

## Match the reference frame by frame

Before writing the brief, measure the reference itself — do not eyeball it. The output must match on:

- **Structure and pacing:** beats, shot count, average shot length (scene-cut detection with ffmpeg), transitions.
- **Color and look:** lighting, grade, depth of field, framing (shot/reverse-shot, foreground shoulder).
- **Animation:** any zooms, punch-ins, text or logo animation, and their timing.
- **Text:** caption font, size as % of frame width, position as % of frame height, color, shadow or box,
  words per line, case, whether captions animate. Title cards and their hold time.
- **Voice:** dialogue vs narrator, voice age and tone. Transcribe with timestamps (faster-whisper).
- **Background music:** check with a spectrogram whether there is a music bed or only room tone; match it.
- **Loudness:** integrated LUFS (ffmpeg ebur128).
- **End card:** layout, animation order, CTA, length.

Put every measurement in the brief as a spec table ("reference, as measured" vs "our version"), and check each
sample frame against it before showing the user.

## Direct-response standard

Study winners on Atria before writing a script (top video ads by impressions per advertiser). Reference brands:
Happy Mammoth, HIKE Footwear, Orthora Footwear, BioRoot Labs, Hollow (Alpaca) Socks, Viasox. Look for: a
specific failed solution, a new mechanism that blames the old product rather than the buyer, a specific
symptom or job-based pain, a stacked offer and guarantee said out loud, objections answered before the CTA, and
repeated CTAs. Keep claims compliant: comfort, room and support — never that a product replaces treatment.

## Footage and tools

- **Comfort Wear / Ortho Stretch footage (Google Drive):** Ortho Stretch Cushion Shoe → Video →
  `CATEGORIZED LIBRARY` (01_Cushion and Arch Support … 13_Voice Over) and Video Assets → `New Content` →
  2026 (creator folders) — the newer footage. Drive downloads work through the Google Drive connector.
- **YouTube / TikTok:** downloads are blocked from cloud sessions. For internal-only organic mockups, the user
  downloads clips and drops them in a Drive folder. Never run organic creators' footage as ads.
- **AI clips:** kie.ai needs `KIE_API_KEY` in the environment; OpenAI (Sora, TTS) uses `OPENAI_API_KEY`.
- **Brand rules:** read `ads/brands/<brand>/brand.json` (e.g. Ortho Stretch is a women's shoe — only women wear it).

## First brief made this way

Ortho Stretch "Padding Isn't Room" story ad, matching the HIKE toddler-drama reference:
https://claude.ai/artifact/R3tNFoAvfH82dQnsMZEMoZ
