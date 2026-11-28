# COM459 (Japan) clip sourcing brief — for sourcing agents

Project root: `/home/user/claude_code_sam/ads/video/projects/com459`
Shot list (directed by StefanBrain): `edit/STEFANBRAIN_DIRECTION_COM459.md`. Every shot has: shot id (H1.1, P2.7 …), the VO words it covers, a visual description, a source tier and a TikTok query.
Sister ad COM458 (NYC) is already cut. Its look = organic phone UGC of the exact place named. See `../com458/reference/d_02.jpg` and `d_03.jpg` (1 fps frames of the winner it copies).

## Your job
For each shot in your range whose tier is **JAPAN_UGC** or **COMPETITOR_UGC** (or PRODUCT / JAPAN_UGC mixes, for the Japan half only), find a real organic TikTok clip that literally shows what the shot description says. JAPAN means real Japan footage: Tokyo/Kyoto/Osaka stations and subway stairs, Shinjuku/Shibuya crowds, packed trains, ramen lines, Fushimi Inari, Kiyomizu-dera, shrines, wet station tiles, Japan snow, Omoide Yokocho / Golden Gai, last train …
Skip PRODUCT / ANIMATION / AI shots. List them as `skip`; the editor handles those.

### Competitor shots: check what we already have first
COM458 already downloaded Hoka / On Cloud / toe-box clips. Look at those first and reuse a file when it fits (use its path as-is, e.g. `../com458/tiktok/hoka/<file>.mp4`):
`ls /home/user/claude_code_sam/ads/video/projects/com458/tiktok/{hoka,oncloud,toebox}`. Also see `../com458/edit/sourcing_*.json` for notes on those files and their in-points.
Download new competitor clips only for shots those can't cover (e.g. wet-floor slip test, price tag in a store).

## NEW HARD RULE: one continuous take per shot
The client said our last edit "changed scenes too fast". We measured it: most of the extra cuts came from INSIDE the TikTok clips (creator jump-cuts, travel montages). So:
- The window you pick (`in` → `in + usable_s`) must be ONE continuous camera take, with no cut inside it. `usable_s` must be ≥ 2.0 s (≥ 2.5 s preferred).
- Avoid fast-cut montage edits ("Japan in 30 seconds" style) unless one of their takes is long enough on its own.
- When you check a clip, look at the 0.5 s contact sheet and confirm that consecutive frames in your window are the same scene.

## How
1. Discovery: `WebSearch` with `allowed_domains: ["tiktok.com"]`, mode standard. Use the shot's query, then variants (e.g. "tokyo station stairs pov", "kyoto snow temple steps"). Collect `tiktok.com/@user/video/<id>` URLs (discover/tag pages are useless for downloading).
2. Download with the helper (plain public downloads only):
   `printf "<category>\t<url>\n" >> /tmp/claude-0/<you>_urls.txt` then
   `/home/user/claude_code_sam/ads/video/scripts/tt_pull.sh /tmp/claude-0/<you>_urls.txt /home/user/claude_code_sam/ads/video/projects/com459/tiktok`
   (it skips nothing; give it a fresh urls file each time so you don't re-download). Files land in `tiktok/<category>/<uploader>_<id>.mp4` and creator/url go to `tiktok/sources.tsv`. Use short categories: `jp_station`, `jp_stairs`, `jp_train`, `jp_lines`, `jp_kyoto`, `jp_shrine`, `jp_winter`, `jp_night`, `jp_pain`, `jp_hotel`, `jp_steps`, `jp_travel`, `hoka`, `oncloud`.
   - **Never** download from YouTube or use any workaround for blocked downloads. If a TikTok says "IP blocked", skip it.
   - Download at most ~40 clips. Check each one before downloading more for the same shot. Disk is tight; delete any clip you won't use (`rm`) and remove its line from sources.tsv.
3. Check footage: `python3 -I /tmp/claude-0/dense.py <video.mp4> /tmp/claude-0/<you>_<name> 0.5 160` writes `<prefix>_01.jpg` …; Read them.
   Prefer: vertical 9:16, real phone UGC, no big burned-in captions mid-frame (top/bottom text is OK, the editor crops/erases it), no talking heads unless the shot calls for one, no giant competitor logo macros.
4. If nothing usable exists after 3–4 searches for a shot, say so and suggest the best fallback (another shot's clip, or a generic Japan UGC alternative).

## Output (required)
Write `edit/sourcing_<GROUP>.json`, a list of objects:
`{"shot": "P1.7", "vo": "You are climbing five flights", "file": "tiktok/jp_stairs/<file>.mp4", "in": 3.2, "usable_s": 2.6, "continuous": true, "crop_hint": "...", "text_band": null, "creator": "@user", "url": "...", "note": "looking up long Tokyo Metro staircase"}`
(`file` is relative to the com459 project root; reused COM458 files start with `../com458/`. Use `"file": null, "status": "skip"` for PRODUCT/ANIMATION/AI shots and `"status": "missing"` when not found.)
Your final message is ≤15 lines: how many shots filled / missing, and the 3 best finds.
