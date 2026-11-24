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

## 2026-11-19 (DentalPULSE Thursday run)
- `scroll_video.py`: still background and text layer decoded once and cached with the `loop` filter (pixel-identical output, ~40× cheaper filter; renders were running at ~1 fps). New `SCROLL_X264_PRESET` env override (default medium).
- `scroll_video.py`: logs ElevenLabs `character-cost` per voice section to `<ID>/el_costs.txt`, because the key can't read `/v1/user/subscription`.

## 2026-11-23: second weekly market study
Evidence: `ads/brands/comfortwear/research/learning/market_study_2026-11-23.md` (27 new ads from 19 brands, plus a 7-day re-check of all 57 earlier rows in `hook_loop_bank.csv`). The Meta Ad Library returned 403 again, so the study is Atria only (MCP plus the Open API).

**SKILL.md**
- **Non-negotiable 4:** a market ad's first-week rank is not evidence. Count an ad as evidence only after 14+ days, or when the advertiser's earlier ads ran 60+ days in that format. Why: 7 of the 11-16 study's rank-1 launches died within 10 days (EverWell 3 days, PhotoStick 5, Koprez 10, Volosso RV relaunch 5, Whisp 6, Inflammation Fix 6, Sculptara Airbnb 3).
- **Non-negotiable 11:** if a concept with a proven back half dies fast, keep the back half and rewrite the trigger and the front 30%. Why: PhotoStick m1521996796617216 (dead at 5 days) was relaunched as m1127648890268432 with the same back half and a universal trigger.
- **§2.3 length:** the 15–20k long cut beside the current cut is now a standard test in every batch, no longer an optional one. Why: the Auniva page network's 15.4–24k bodies ran 120–145 days, and Elvera's 12.5k and 16.7k cuts of one hook each ran 145–180 days.

**playbook.md**
- **Sources:** a "how to weigh market evidence" rule (14+ days); rules that rest only on launch rank are marked *unproven*.
- **§1:** the prophesied timeline. The messenger predicts the quiet start and the guarantee reuses it (Elvera m28161283220215359, urologist m1618765572775417; launches).
- **§2:**
  - **Hook type 20, dated domestic incident / someone else's moment.** This one has long-runner proof: Auniva pages, 124–144 days; Pet Organica 24.3k, active at 107 days; with the 0-day "mother's pickles" counter-example.
  - **Types 21–24 (launches):** point-of-no-return near-miss, rule-break stress test in a static, anonymous benefactor, sale spotted in the wild.
- **§3:**
  - **Loops 14–16:** prophesied timeline, concealment → confession, public record → new record.
  - **Silent-spouse loop marked unproven:** Volosso m2196690051278068 died after 1 day.
- **§4:** on-off-on proof (Miracle Sheets m1914741186628481) and disaster confirmed after the rescue (PhotoStick).
- **§5:** 4 new bridges (second-hand expert chain, two-messenger split, a tradesman whose trade is the analogy, the villain's playbook as scorecard). Measured brand position: median 56% across 21 statics.
- **§9:** long-runner evidence for 15–24k bodies. The long cut is a standard test for proven bodies.
- **§10:**
  - **Rule 14:** a dead ad is not a dead body (PhotoStick; the Nerve Support relaunch).
  - **Rule 15:** the footwear update. Orthora's 4 blog stories are active at 12 days, its tier lists died again (7 cuts at 0–1 days), and ComfoFeet's insider ranking video has run 42+ days.
- **§11:** the Auniva pattern. One mechanism block runs across many conditions and pages, and one body ran on 2 pages for 139–144 days each.

**scroll_videos.md**
- **New 2026-11-23 section:**
  - The Mode B pace band is 2.5–4.5 words a second. Two new music-only scrolls run at 2.5–2.8 (Susan Miller m1662443618619314, rank 1/34; Ageless Beauty m1543429487624419, rank 7/310), and Estella's 4 words a second is still #1/549 at 113 days.
  - 1:1 square scroll via a center crop.
  - Mode C, "chapter one": a voice-over of the opening 20–25% with the full story in the caption (New World Publications, 5 duplicates in its top 10).
- **Older 4–4.5 words-a-second rule:** softened to match.

**Mirrored:** playbook changes into `ads/research/long-form-copy/PLAYBOOK.md`. Rebuilt `ads/research/long-form-copy/longform-ads-skill.zip`.
- Playbook: added the Cuurt November-wave case study (witness-buyer narrator, behavior-first mystery, evidence device as results log, free at-home test, 3 hand-checks, kill the cheap copy, mirror story). Backlog: 5 test ideas for Comfort Wear.
- Witness format added to SKILL.md §2.3, with LF15 (Prague step counter) as the model; the 2026-11-26 batch has been reworked to 7 witness concepts plus 3 first-person controls.
