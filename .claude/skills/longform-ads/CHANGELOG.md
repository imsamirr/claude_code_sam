# longform-ads skill changelog

## 2026-11-12
- Scroll videos: HQ still-image mode is the default (1080x1920, 50 fps, 1 px/frame, light background blur, CRF 27). Notion gets 30 s full-quality hook previews; the user uploads full files to the Drive folder. Reason: the user rejected the 720p/19MB renders as poor quality.
- Added the weekly Monday market study plus skill-update loop (scheduled task trig_011ZJquwEETg3Es2LQseZ9jj).
- **Merged the ComfortWear and DentalPULSE copies of this skill into one** (branch claude/awesome-ride-mnjwdt, merged from claude/blissful-ptolemy-3oupr1). Both brands' scheduled tasks and the Monday market study now use this one skill.
  - From DentalPULSE: product reference photos for images (`"ref"`), per-concept `specs_*.json`, parallel image renders with retries, `"audio": "music"` specs, and an auto-generated Suno music bed when `--music` is omitted.
  - From ComfortWear: HQ still-image scroll videos (now also used for `"audio": "music"` and `background_image` prompt specs), Veo QA checks, and the Notion hook-preview delivery.
- Delivery: full scroll videos now go as download cards in the Claude chat (the user's choice). Notion cards carry the 30 s hook preview plus a note pointing to the chat; no Drive step.
