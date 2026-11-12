# Scheduled-task prompt template

Scheduled runs start fresh, without this repo, so the prompt must be self-contained. Fill every
`<…>` from the brand's `video_deep_dive` block and the latest report, then pass it to `create_trigger`
(or `update_trigger`).

The live ComfortWear task (`trig_01UpF6xwkG3g2yKYVtQ4LznX`) is a filled-in example. Read it with
`get_trigger`.

---

<Brand> weekly creative deep dive for the <Atria account name> Meta ad account, delivered to Slack.

## Data source
Use the Atria MCP tools (load them with ToolSearch). The ad account is "<Atria account name>" (Atria account id <atria_account_id>, Meta <meta_ad_account_id>, currency <currency>).<Optional: Do NOT use "<dead duplicate account>" (no spend).> Windows are UTC days; presets end yesterday.

## Which ads to analyze
1. Account summary for last_7d and last_14d (spend, ROAS, CPA).
2. Top spenders: list_ad_account_ads sorted by spend for last_7d and last_14d, with metrics spend,roas,purchases,cost_per_purchase,aov,ctr_link,cpm,thumbstop_ratio,hold_rate,video_play_avg_time,frequency. Include every ad with more than $<top_spend_min> spend in either window.
3. New launches: ads launched in the last 7 days with spend over $<new_launch_min_spend> and a ROAS of <new_launch_min_roas> or higher (inclusive).
   - Identify launches by comparing last_7d against the prior 7 days (custom window, days 8–14 back). An ad is new if it had no spend, or only a trivial amount, in the prior week.
   - Also check a custom window that includes today.
   - If none qualify, say so plainly and analyze the closest near-misses, labelled as near-misses.
4. Add 1–2 comparison ads: the most efficient video ad at meaningful spend (over about $<comparison_min_spend> in 14d) and any notable fader (big week-over-week ROAS drop).
5. Show week-over-week ROAS trend for winners (prior 7d vs last 7d).

## How to analyze each video
- get_ad_account_ad for creative: ad text, headline, CTA, landing URL, video URL, video_id. Also pull retention metrics: video_play_rate_p25,p50,p75,p95, hold_rate, thumbstop_ratio.
- Script word for word: try get_ad_account_video_transcript (free cache lookup) first. If it isn't cached, do NOT spend Atria credits. Instead download the mp4 and transcribe locally with faster-whisper ("small", int8, CPU; pip install faster-whisper if missing), piping audio via ffmpeg to a numpy float32 array (PyAV file opening is broken in this environment). Use language auto-detect for non-English ads.
- Frames: download each mp4 to the scratchpad. Use ffmpeg to extract the hook at 2 fps for 0–6s (with timestamp overlay) and the body at 1 frame per 4s. Tile into contact sheets and view them with Read.
- Note:
  - hook visuals and text
  - when the <expert> first appears
  - when the <product> first appears
  - b-roll types
  - <how-it-works / medical> graphics
  - pain-acting and payoff shots
  - on-screen captions
  - end card

## Report content
1. Ad table using the FULL Atria ad names (never short codes alone), with spend, ROAS, CPA, hook and hold rates.
2. What's working: patterns among winners.
3. Patterns in scenes, b-roll and things said, across the frames.
4. What's missing or leaking:
   - landing page and ad-text mismatch with the video's occasion/audience
   - offer and guarantee inconsistencies
   - late product reveal versus p95 retention
   - missing proof/reviews
   - weak hooks
   - fatigue
5. Prioritized iteration ideas, each naming the exact full Atria ad name and concept code it builds on.
6. "What changed vs last week": new winners, faded winners, and leaks fixed or still open.

## Baseline
Before writing the report, read the previous weekly report from the Slack DM with <first recipient name> (<first recipient id>): the most recent message starting with "<Brand> weekly creative deep dive" and its thread. Use it as the baseline for section 6.

If there is no previous report, use this baseline (<date>):
<3–6 bullets: winners with full ad names, top spender + ROAS, winning pattern, main leaks>

## Delivery
- Send the report as a Slack DM to <each recipient: name (ID)> using slack_send_message with channel_id = the recipient ID. Write it in Slack markdown.
- The first message must start with "<Brand> weekly creative deep dive – week ending <date>" and give a short summary.
- Each message is limited to about 5,000 characters, so post each section as a threaded reply (thread_ts) to that first message.
- Do not send to anyone else.
- Do not create, pause or edit any ads, and do not spend Atria credits.
