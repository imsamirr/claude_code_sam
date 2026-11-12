---
name: video-ad-deep-dive
description: Weekly creative deep dive on any brand's Meta ad account through the Atria MCP. Pulls the top spenders (default over $5K in the last 7 or 14 days) and new launches from the last 7 days (default over $100 spend and 1.6+ ROAS). Reads every script word for word and reviews the videos frame by frame. Reports what's working, patterns in scenes/b-roll/mentions across winners, what's missing or leaking (landing page, ad text, offer, reveal timing, proof, hooks, fatigue), and iteration ideas named by full Atria ad name and concept code. Delivers in chat or as a Slack DM, and can set up a weekly scheduled task per brand. Use for "deep dive on <brand>'s ad account", "analyze our top ads", "what are the winners doing", "weekly creative report", "set up the Monday deep dive for <brand>", or a scheduled deep-dive run.
---

# Video ad deep dive

One brand per run. Per-brand settings live in `ads/brands/<brand>/brand.json` under `video_deep_dive`
(see §0). Read that block first. If it's missing, run §0 before anything else.

Helpers in this skill's `scripts/` folder:
- `contact_sheets.sh <video.mp4> <out_dir> [label]`: writes a hook sheet (0–6s at 2 fps, timestamped)
  and a body sheet (1 frame every 4s).
- `transcribe.py <lang|auto> <video.mp4>…`: free local transcription. Use it only when Atria has no
  cached transcript.

Put all downloads in the scratchpad, never in the repo. The scheduled-task version of this skill runs
without the repo, so `references/routine-prompt-template.md` inlines everything it needs.

## 0. Onboarding a brand (first run, or when `video_deep_dive` is missing)

1. `list_ad_accounts` (Atria MCP). Pick the account by name and check it actually spends:
   `get_ad_account_summary` for last_14d. Some brands have a dead duplicate account (e.g. "WearOrtho V2"
   has no spend). Record the Atria `id`, the Meta `ad_account_id`, currency and timezone.
2. Ask the user, in one AskUserQuestion call or one short message, for anything not already given:
   - **Top-spender threshold.** Default: over $5,000 in the last 7 or 14 days. Scale it to the
     account's spend: about 5–8% of 14-day spend is a sensible default if the user has no number.
   - **New-launch rule.** Default: launched in the last 7 days, spend over $100, ROAS 1.6+ (inclusive).
   - **Expert or authority figure, and product name**, to track in frames (e.g. "podiatrist" and
     "ComfortWear shoe"; "dentist" and "DentalPULSE pod").
   - **Delivery**: chat only, or Slack. For Slack, take names and resolve them with `slack_search_users`.
     Never guess an ID. If a name isn't found, say so and ask; don't substitute a lookalike.
   - **Schedule** (optional): weekday and time, with timezone. Default Monday 7:43 AM in the account's
     timezone.
3. Save the answers in `brand.json` → `video_deep_dive` (same shape as `ads/brands/comfortwear`), then
   commit and push.

## 1. Pick the ads

Use the Atria MCP. Windows are UTC days; presets end yesterday. Ask for these metrics:
`spend,roas,purchases,cost_per_purchase,aov,ctr_link,cpm,thumbstop_ratio,hold_rate,video_play_avg_time,frequency`.

1. `get_ad_account_summary` for last_7d and last_14d: spend, ROAS, CPA.
2. **Top spenders.** Run `list_ad_account_ads` with `sort_by=spend` for last_7d and last_14d (limit 25).
   Keep every ad over the threshold in either window.
3. **New launches.** Atria has no launch date, so infer it:
   - List last_7d by spend (offset 0, then 25, until spend falls below the minimum).
   - List the prior 7 days: `period=custom`, days 8–14 back.
   - An ad is **new** if it had no spend, or a trivial amount, in the prior week. Meta ad IDs from the
     same upload batch share a prefix, which helps date a batch.
   - Also check a custom window ending today. Recent days settle late, so an ad may only cross the bar
     once today's data is in. Report both numbers.
   - Keep new ads with spend > min and ROAS ≥ the bar (inclusive).
   - If none qualify, say so plainly, then analyze the 2–3 closest near-misses, labelled as near-misses.
4. **Comparison ads (1–2).** Add the most efficient video ad at meaningful spend (about 3–4% of 14-day
   spend), and any sharp fader (big week-over-week ROAS drop). They sharpen the patterns.
5. **Week-over-week ROAS** for each winner: prior 7d vs last 7d.
6. Static/image ads have no frames or script. Analyze them briefly (image, headline, ad text) and note
   how retargeting statics compare.

Rate limits: `get_ad_account_ad` can return "Too Many Requests". Batch about 5 calls, and retry the
failures once.

## 2. Pull creative and scripts

For each video ad:
1. **Creative.** `get_ad_account_ad` with the same metric list plus
   `video_play_rate_p25,video_play_rate_p50,video_play_rate_p75,video_play_rate_p95`. Record:
   - ad text (`body`), `title`, CTA, `link_url`
   - video `url`, `duration`, `video_id`
2. **Script.**
   - First, `get_ad_account_video_transcript` (cache only, free).
   - If it isn't cached, **don't** call `transcribe_ad_account_video`: it spends Atria credits. The
     exception is when the user has explicitly authorized credits.
   - Otherwise, download the mp4 (`curl -sS -o <scratch>/vids/<label>.mp4 <url>`) and run
     `python3 -I scripts/transcribe.py auto <file>`.
   - Gaps in Atria transcripts are usually transcription artifacts, not cut audio. Before calling
     something an audio problem, check it by re-transcribing that span locally.
3. **Frames.** `scripts/contact_sheets.sh <mp4> <scratch>/vids <label>`, then Read both sheets.
   Body frame k is at second 4×(k−1).

## 3. Analyze

Read `references/analysis-checklist.md` and work through it for every ad. It covers:
- the hook (first 3s)
- when the expert first appears and when the product first appears, against p25/p95 retention
- teardown and mechanism structure, mentions and numbers
- b-roll types, captions, end card
- message match across video, ad text, headline, landing page and offer

Then compare winners against the weaker ads in the same set. A pattern counts only if it separates
them. Name the exception when one breaks a pattern, and say the sample is small.

## 4. Report

Sections, in this order:
1. **Ads analyzed**: a table with the **full Atria ad name** (never only a short code like "HF7"), Meta
   ad ID, why it's included, spend, ROAS, CPA, hook and hold rates. State plainly when thresholds were
   missed.
2. **What's working**: patterns among the winners, each backed by specific ads and numbers.
3. **Scenes, b-roll and mentions**:
   - opening-shot table (expert in first 3s? → ROAS)
   - recurring b-roll
   - recurring spoken and on-screen mentions
   - caption and end-card style
   - what the winners never show
4. **What's missing or leaking**:
   - landing page and ad text vs the video's occasion and audience
   - offer and guarantee consistency
   - reveal timing vs p95
   - missing proof
   - weak hooks
   - credibility slips
   - fatigue
5. **Iteration ideas, prioritized.** For each idea give the exact full ad name(s) and concept code it
   builds on (the `COM###` / `OCTWK#_VID#` / `Kyro###` style part of the name), and what to keep vs
   change.
6. **What changed vs last time** (scheduled runs): find the previous report in the Slack DM and say
   what's new, what faded, and which leaks are fixed or still open.

**Delivery**
- **Chat:** markdown as above. Offer to write briefs for the top ideas.
- **Slack:** `slack_send_message` to each recipient ID in `video_deep_dive.slack_recipients`.
  - The first message starts with `<Brand> weekly creative deep dive – week ending <date>` and gives a
    short summary.
  - Post each section as a threaded reply (`thread_ts`). Messages cap at about 5,000 characters.
  - Send only to the configured recipients.

Never create, pause or edit ads, and never spend Atria credits without explicit approval.

## 5. Scheduling it weekly

1. Build the prompt from `references/routine-prompt-template.md`. Fill in:
   - the account IDs and thresholds from `brand.json`
   - the expert and product names
   - the recipients
   - a baseline summary of the latest report, used only when no Slack report exists yet
2. Call `create_trigger` with:
   - `create_new_session_on_fire: true`
   - `cron_expression: "CRON_TZ=<tz> <min> <hour> * * <dow>"`, staggering brands about 15 minutes apart
   - `initiation: human_request`
   - `notifications: {"push": true}`
3. If the result warns that the task stores no connectors, tell the user plainly. They must attach the
   **Atria MCP** and **Slack** connectors to the scheduled task in claude.ai, or the run can't read data
   or post. Once they've done that, confirm with `get_trigger` that `mcp_connections` lists both.
4. Record the schedule and trigger ID in `video_deep_dive.schedule`, then commit and push.
5. To change a live task's prompt later, use `update_trigger` with the full new prompt. Connectors
   survive prompt updates; check with `get_trigger`.
