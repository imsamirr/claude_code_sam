---
name: winner-video-batch
description: Weekly batch of 10 organic-style short-form video ads that iterate a brand's current top-spending and top-performing ads (Atria ad account), with every scene unique across all batches, uploaded to the brand's Drive video folder, logged as a Notion card on the brand's creative board, and summarized for the user. Works for any brand in ads/brands/<brand>/ that has a video block in brand.json. Use for "run the weekly video batch", "Thursday videos", "iterate our top ads into short-form", "set up the weekly video batch for <brand>", or the scheduled weekly routine.
---

# Weekly winner video batch

Builds on the `video-ads` skill (engine, footage, QA): read it too. Everything brand-specific is in
`ads/brands/<brand>/brand.json` → `video` (rules, `weekly`, `drive_folder_id`, `notion`, end cards).

## Rules (Comfort Wear user rules, Nov 2026; other brands copy them unless told otherwise)

- **Only iterate winners** from `python ads/video/select_winners.py --brand <brand>`:
  - top: ≥ **$1,000** spend in the last 7 days and ROAS ≥ **1.6**
  - new: launched in the last 7 days (no spend in the 60 days before), ≥ **$200** spend, ROAS ≥ **1.6**
  (thresholds in `video.weekly.winners`; all accounts in `video.weekly.atria_accounts`).
- **10 videos per batch** (`video.weekly.videos_per_batch`), every one a **different concept**
  (format + hook + story). Several may share an angle/audience if that's what's winning (nurse,
  Disney, plus-size, travel, teacher…): split the 10 across winners roughly by spend × ROAS, every
  winner gets at least one.
- **Scenes never repeat**: no source clip in two ads, ever, across all batches
  (`python ads/video/check_batch.py <week dir>` checks this week against every earlier folder; it
  must exit 0 before rendering). A Drive file named `snaptik_<id>…` is the same clip as `tiktok:<id>`.
- **The format** is the organic-post style in `video-ads` §3 and `ads/video/playbook.md`: one static
  first-person caption, 2–4 real shots, music only, no voiceover, 10–16 s + end card, 9:16 with all
  content inside the 4:5 area, captions never on faces/eyes/product/action.
- **Caption looks rotate (user rule, Nov 13)**: the references use several caption styles, not only the
  white box. Use **at least 5 different looks per batch** (no look on more than 2 videos), each matched to
  its format's reference: box, narrow box column, translucent box, plain text + shadow, bold Helvetica +
  shadow, TikTok Classic thin outline, IG serif, meme stroke, lowercase (`ads/video/playbook.md` §7, engine
  options `style`/`font`/`weight`/`x`/`lower`). Record the look in each edit.json `caption_style`.
- **Discover new looks every week (user rule, Nov 14)**: each run finds **≥ 2 caption looks not used
  before** (fresh Atria UGC ads, preview grid of ~30 thumbnails; TikTok), builds them into
  `ads/video/build.py` if needed, uses them in the batch and logs them in the playbook §7 style log.
- **Script captions (user rule, Nov 14)**: the text doesn't have to stay the same all video. In 3–5 of the
  10 videos give each scene its own line so the lines read as a running script (problem → mechanism →
  turn → payoff), one caption per scene with `"clip": i`, key phrase in `*asterisks*` (playbook §8,
  example `V46_21_nurse_trash_script`).
- Each concept keeps its winner's angle, audience and proof points; it changes the format, hook and
  story. Use `claims_to_avoid` from brand.json.

## Run (Thursday, or when asked)

1. **Setup**: `git fetch && git checkout <branch>`; `pip install -q requests python-dotenv pillow
   opencv-python-headless==4.10.0.84 yt-dlp curl_cffi` (OpenCV 5 lacks the Haar fallback; YuNet model
   is in `ads/video/models/`). Folder: `ads/brands/<brand>/video/<YYYY>-W<ww>/` (ISO week of the run),
   ids `V<ww>_01_<slug>` … `V<ww>_10_<slug>`.
2. **Winners**: `python ads/video/select_winners.py --brand <brand> --out <week dir>/_winners` → read
   `winners.md` (copy, headline, landing page, transcript). If none qualify, say so, stop, and still
   post the Notion card noting "no qualifying winners". If `ATRIA_API_KEY` is missing, use the Atria
   MCP (`list_ad_account_ads period=last_7d`) with the same thresholds.
3. **Fresh research (short, every run; includes ≥ 2 new caption looks, see Rules)**: re-read `ads/video/playbook.md`; check what's new on TikTok
   (WebSearch: trending formats/sounds this week, the winners' niches, e.g. "#nursesoftiktok trend
   this week") and 3–5 fresh organic-style ads in Atria (`search_library_ads`, `order: best_match`,
   `active_since` last 30 days, `min_days_running` 7, video 0–30 s). Append anything new and useful
   to the playbook under a dated heading.
4. **Concepts**: write 10 concepts (winner → format → caption → 2–4 shots). Different format for
   each, no caption reused from earlier batches (grep earlier `edit.json`s).
5. **Footage** (new clips only; list what's taken with `check_batch.py --used ads/brands/<brand>/video`):
   - the brand's Drive: `video/footage.csv` (tagged) and `video/drive_inventory.tsv` (every file;
     search names), triage with `ads/video/triage.py`, sheet with `build.py --sheet`;
   - **TikTok creators** (allowed: individual creators' posts, never other brands' own content): find
     post URLs with WebSearch (`site:tiktok.com <niche> <moment>`), use them as `tiktok:<video id>`
     sources (the engine downloads them with yt-dlp, no watermark). YouTube blocks this server
     ("sign in to confirm you're not a bot"); skip it unless a cookies file is provided.
   - Add every clip you review to `footage.csv` with tags and best in/out ranges.
6. **Edits**: one `edit.json` per video (`video-ads` schema): `created` = today, `end_card: auto`,
   `music` from `video/music/` (or a new royalty-free bed via Atria `ad_maker_generate_music`,
   ~$0.60, saved into `video/music/`), `based_on` = winner ad name + 7-day spend/ROAS,
   `primary_text`/`headline`/`link` from the winner. Run `check_batch.py`; fix any reuse.
7. **Render + QA**: `build.py` each (≈1 min per video), then `qa.py` each: PASS, no faces outside 4:5,
   then Read the strips **and** a 1-frame-per-second strip of every video
   (`ffmpeg -t <content s> -i v.mp4 -vf "fps=1,scale=150:-2,tile=16x1"`) to catch text on eyes,
   product or action between samples. Fix and re-render failures.
8. **Deliver**:
   - Commit `<week dir>` (edits + mp4s + sheets), `footage.csv`, playbook changes; push.
   - Drive: `python ads/video/drive_upload.py <video.drive_folder_id> <week dir>/*/V*.mp4` (straight into
     the folder, no subfolders; needs GDRIVE_* env vars).
   - Notion: one card on the brand's board (`video.notion`): title `SF W<ww> | Short-Form Organic
     Batch (10) | <angles>`, Stage `In Review`, Strategist from config, Frame Link = the Drive folder;
     body: winners table (ad, spend, ROAS, tier), then one row per video (id, winner, format, caption,
     Drive link), music used, anything skipped.
   - Final message: counts, winners, concepts, Drive + Notion links, cost, issues.

## Setting up a new brand

Add to its `brand.json` → `video`: `drive_folder_id` (create "<Brand> – Short-Form Video Ads"),
`end_cards` (+ `lang`), `weekly` (`atria_accounts`, `winners`, `videos_per_batch`, `weekday`),
`notion` (`data_source`, `title_prefix`, `stage`, `strategist`), `rules`; build its footage library
(`video-ads` §2) and a music bed or two. Then create the routine (below) with a different minute.

## Routine (one per brand)

create_trigger, `create_new_session_on_fire: true`, cron like
`CRON_TZ=America/New_York 23 5 * * 4`, connectors Notion (+ Atria if no ATRIA_API_KEY). Prompt:
"Run the `winner-video-batch` skill for brand `<brand>` on repo <owner>/<repo> branch <branch>
(clone if missing; push there, no PR). Produce this week's 10 videos, upload to Drive, create the
Notion card, and end with the summary. If a step fails (no winners, connector missing), say so at the
top and still post what you can."
