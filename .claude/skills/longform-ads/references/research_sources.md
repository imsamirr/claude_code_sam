# Research sources: exact calls, filters and fallbacks

## 1. Our own winners (Atria Open API, `ATRIA_API_KEY`)

```bash
python ads/atria_pull.py longform --brand <brand> --transcribe
```

**What the command does:**
- **Window and audience:** prospecting only, 90 days (`--days`). Retargeting is detected from the ad, campaign or adset name: RTG, RETARGET, REMARKET, WARM, BOF.
- **Script families:** videos are grouped by transcript similarity of 0.6 or more on the body after the hook. Statics are grouped by headline plus copy. Videos without a transcript stay as their own family.
- **Qualifying bar:** family spend of at least `--lf-min-spend` ($3k), and ROAS of at least 0.95 × the account's prospecting ROAS.
- **Ranking:** `spend × ROAS / baseline`.
- **Paid transcription:** `--transcribe` pays only for uncached videos with at least `--lf-transcribe-floor` ($2k) spend. A "video not found" response means Meta deleted the video; use a sibling iteration's transcript instead.
- **Output:** `research/data/longform_winners.md` and `.csv`.

**Lifetime winners:** `research/data/video_transcripts.md` (top videos ever) and `atria_pull.py winners`. Check these, because a 90-day window can hide the biggest historical angle.

**Open API endpoints:**
- `GET ad-accounts/{acc}/ads` (top 50 per window)
- `GET ad-accounts/{acc}/ads/{id}`
- `GET|POST ad-accounts/{acc}/videos/{video_id}/transcript`
- `GET ad-library/search`
- `GET ad-library/{id}`

Library transcripts are **not** on the Open API. Use the MCP for those.

## 2. Market long-form (Atria MCP)

- **Saved ads:** `search_library_ads` with `scope=saved`, `media_format=["image"]`, `min_body_length=2000`, `order=saved_newest`, paged with `cursor`.
- **New long-form statics:** `search_library_ads` with `launched_after=<7 days ago>`, `media_format=["image"]`, `min_body_length=2000`, `language=["en"]`, plus `query` from `category_terms`.
- **New long videos:** `media_format=["video"]` with `video_length=["60-120","120-"]`. Get the transcript with `get_library_ad_transcript` (free). Use `transcribe_library_ad` (credits) only when there is none, and only with the user's authorization.
- **Competitors:** search each `competitors_longform` name and read their ads in full with `get_library_ad`. Note `days_running`, `status` and `impression_rank`.
- **Run days are the signal.** Re-check logged ads at 7, 14 and 30 days. Ads running 100+ days are long runners. Ads that ran under 10 days were usually killed: aggressive scam framing, medication-avoidance copy, continuity errors.

## 3. Customer voice (Google Drive MCP)

- **Finding the file:** `search_files` with `title contains '<word>'`, then `read_file_content`. The file is big (18k+ rows for Comfort Wear), so give it to a subagent.
- **What the subagent returns:** the columns and date range; counts of jobs, ages, problems, previous products and life moments; 25+ verbatim quotes; 8–10 unused angles with frequencies; objections and complaints (these become "don't promise" rules).

## 4. Reddit

- **Access:** reddit.com and old.reddit.com are blocked from the cloud. Use WebSearch with `site:reddit.com …` for snippets, and the archive mirror reddit.sentinel-team.org for full threads. Mumsnet works for the 45+ women's audience. Many alternative viewers, allnurses, Cruise Critic and the QVC forums are blocked.
- **Delegate it:** give the research to a subagent with the brand's subreddits and the angles already used. Ask for 25+ verbatim snippets with links, 8–10 new angles, and a list of what users distrust in ads.
- **Verify quotes** before using them verbatim in copy.

## 5. Swipe files

`ads/research/long-form-copy/breakdowns/` holds per-ad breakdowns of about 95 saved long-form ads and a 30-variation swipe doc.
