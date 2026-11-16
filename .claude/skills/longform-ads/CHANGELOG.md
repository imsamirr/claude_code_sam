# longform-ads skill changelog

## 2026-11-12
- Scroll videos: HQ still-image mode is the default (1080x1920, 50 fps, 1 px/frame, light background blur, CRF 27). Notion gets 30 s full-quality hook previews; the user uploads full files to the Drive folder. Reason: the user rejected the 720p/19MB renders as poor quality.
- Added the weekly Monday market study plus skill-update loop (scheduled task trig_011ZJquwEETg3Es2LQseZ9jj).
- **Merged the ComfortWear and DentalPULSE copies of this skill into one** (branch claude/awesome-ride-mnjwdt, merged from claude/blissful-ptolemy-3oupr1). Both brands' scheduled tasks and the Monday market study now use this one skill.
  - From DentalPULSE: product reference photos for images (`"ref"`), per-concept `specs_*.json`, parallel image renders with retries, `"audio": "music"` specs, and an auto-generated Suno music bed when `--music` is omitted.
  - From ComfortWear: HQ still-image scroll videos (now also used for `"audio": "music"` and `background_image` prompt specs), Veo QA checks, and the Notion hook-preview delivery.
- Delivery: full scroll videos now go as download cards in the Claude chat (the user's choice). Notion cards carry the 30 s hook preview plus a note pointing to the chat; no Drive step.
- ElevenLabs voice-over (env ElevenLabKey) for 1–2 concepts per run, hard-capped at 5,000 credits per run in scroll_video.py (Turbo v2.5, about 2,000 credits per video). Everything else stays music-only.
- Full scroll videos now upload to Google Drive with `ads/drive_upload.py` (Drive API with the user's OAuth app; env GDRIVE_*), and each Notion card gets a per-video Drive download link. Chat download cards are the fallback.
- Merged the DentalPULSE chat's parallel scroll-video work into the shared branch: 60 fps whole-pixel render, ease-in, ElevenLabs sections with a 5k cap and ledger, and the Drive uploader with --folder-id/--names/--replace. Added ComfortWear compatibility (background_image_prompt, voiceover, el_voice, --no-voice, --folder <id>, path::name) and fixed the default Rachel voice ID.
- Added references/direct_response.md: awareness and sophistication, one belief, mechanisms, 6 lead types, proof, objections, offer value equation, DR tags, and the copy scorecard (ship at 16/20 or above). SKILL.md now requires DR tags and a scorecard grade for every concept, plus a results loop by DR tag.

## 2026-11-16: first weekly market study
Evidence: `ads/brands/comfortwear/research/learning/market_study_2026-11-16.md` (39 ads, 22 brands, all in `hook_loop_bank.csv`). The Meta Ad Library returned 403, so the study is Atria only.

**SKILL.md**
- New non-negotiable 11: re-hook a proven body before replacing it, and re-cut it as a music-only scroll video. Evidence: Jessica Whitney 132–140 days with 3 openers; Volosso 284–306 days with 3+ openers, and its RV body relaunched after 294 days; Naturva 197-day static and 188-day video; Estella #1 of 551 at 106 days.
- Length: allow one 18–22k long cut against a 9k cut per batch. Evidence: Julia Bennett 31.6k active at 268 days; EverWell 22.8k and PhotoStick 16.3k at rank 1.

**playbook.md**
- Hooks 15–19: sunk-cost object, insider voyeur, hard deadline + found object, professional irony, historical secret + heirloom, plus 3 video-only hook types. Added "hook iteration on a fixed body".
- Open loops 11–12: the silent-spouse loop (Volosso) and the failed-fix refrain (Sculptara 21k, rank 2).
- Results: "week one, nothing" softened for products you feel at once. Use a reframed first result instead (Orthora relaunch, rising; Koprez, rank 1).
- Bridges: feature-as-reveal (Koprez), tag read aloud (Volosso), and criteria → late EDIT (Orthora blog). The measured median brand position is 59%; footwear tends to name the brand late or never.
- Length: the "past ~18k, returns diminish" rule is softened to a warning (31.6k at 268 days, 17.1k at 197 days, 16.4k at 172 days).
- Long-runner rule 8: the problem is the anti-doctor stance, not profanity (Naturva profane static 204 days; Julia Bennett 238 days).
- New long-runner rules 11–13: winners recycle the body; footwear long-copy statics are fragile (Stepprs ≤2 days, Hike ≤38 days, Orthora none over 2k); a list of ads that died fast.
- Mechanism: the self-test is both the discovery and the CTA (use our own test, never Orthora's thumb press), and measurement and logs work as proof.

**scroll_videos.md**
- New section on how the long-running scroll videos are built. Mode B is a full-static re-cut: about 4–4.5 words a second, music only, the full story in the primary text, and a calm on-topic still. Mode A is our 700-word, 2.5 words-a-second script. The 1–3 sentence caption rule now applies to Mode A only.

**scroll_video.py** (ads/ and skill scripts/)
- New `--px-per-frame` flag. The default is 1 (Mode A); 2 gives Mode B at 120 px/s with whole-pixel steps.
