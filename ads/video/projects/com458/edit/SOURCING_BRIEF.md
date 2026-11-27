# COM458 clip sourcing brief (for sourcing agents)

Project root: `/home/user/claude_code_sam/ads/video/projects/com458`
Shot list (directed by StefanBrain): `edit/STEFANBRAIN_DIRECTION_COM458.md` — every shot has VO words, visual, source type, TikTok query.
Winner being iterated: COM376 (Disney). Its frames are in `reference/d_01.jpg`…`d_06.jpg` (1 fps) — look at 2–3 of them so you know the look: organic phone UGC of the exact place named, cut on every noun, ~1.3 s per shot.

## Your job
For each shot in your assigned range whose source is **NYC_UGC**, **COMPETITOR_UGC** or **UGC**, find a real organic TikTok clip that literally shows what the VO says (NYC means real New York UGC: subway stairs, Manhattan sidewalks, bagel lines, Central Park, Brooklyn Bridge, Broadway, slush, grates, yellow cabs…). Skip PRODUCT / ANIMATION / GRAPHICS / AI shots (the editor handles those) — just list them as `skip`.

## How
1. Discovery: `WebSearch` with `allowed_domains: ["tiktok.com"]`, mode standard. Use the shot's query, then variants (e.g. "nyc subway stairs pov", "nyc winter slush walking"). Collect `tiktok.com/@user/video/<id>` URLs (discover/tag pages are useless for downloading).
2. Download with the existing helper (plain public downloads only):
   `printf "<category>\t<url>\n" >> /tmp/claude-0/<you>_urls.txt` then
   `/home/user/claude_code_sam/ads/video/scripts/tt_pull.sh /tmp/claude-0/<you>_urls.txt /home/user/claude_code_sam/ads/video/projects/com458/tiktok`
   It saves to `tiktok/<category>/<uploader>_<id>.mp4` and appends creator/url to `tiktok/sources.tsv`. Use short categories like `nyc_subway`, `nyc_lines`, `hoka`, `oncloud`, `nyc_winter`, `nyc_payoff`.
   - **Never** download from YouTube or use any workaround for blocked downloads; if a TikTok says "IP blocked", skip it.
   - Download at most ~45 clips total; check each one before downloading more for the same shot.
3. Check footage: make a 1 fps contact sheet and look at it (Read the jpg):
   `python3 -I /tmp/claude-0/dense.py <video.mp4> /tmp/claude-0/<you>_<name> 1 160` (writes `<prefix>_01.jpg` …).
   Pick the exact in-point (seconds) where the needed action is visible for ≥1.5 s. Prefer: vertical 9:16, real phone UGC, no burned-in captions in the middle (top/bottom text is OK, the editor can crop/zoom), no competitor logos in giant macro, no faces talking to camera unless the shot calls for it. Burned-in text you can't avoid → note its y-band so it can be inpainted.
4. If nothing usable exists after 3–4 searches for a shot, say so and suggest the best fallback (another shot's clip, or a generic UGC alternative).

## Output (required)
Write `edit/sourcing_<GROUP>.json` — a list of objects:
`{"shot": "18", "vo": "Number one, that soft foam feeling", "file": "tiktok/hoka/<file>.mp4", "in": 3.2, "usable_s": 2.5, "crop_hint": "zoom on feet, lower 60%", "text_band": null, "creator": "@user", "url": "...", "note": "thumb pressing Hoka midsole"}`
(`file` relative to project root; use `"file": null, "status": "skip"` for PRODUCT/ANIMATION/AI/GRAPHICS shots and `"status": "missing"` when not found.)
Your final message: ≤15 lines — how many shots filled / missing, and the 3 best finds.
