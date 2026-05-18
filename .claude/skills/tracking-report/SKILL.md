---
name: tracking-report
description: Post the daily shipping-status report to Slack. Two flows are supported. **Stage 2 (post-only, the daily trigger's path)**: a GitHub Action already refreshed the sheet at 13:00 UTC and committed today's pre-built message + CSV to `tracking-updates/daily-reports/<DATE>.{txt,csv}`. Pull the latest, read those files, post to #team-order-tracking-updates via the Slack MCP, upload the CSV to Drive, and reply in-thread with the link. **Ad-hoc / on-demand**: full lookup + post, used when the user types something like "run the tracking report now" outside the cron window. Trigger on: a scheduled invocation that names this skill, or user phrases like "post today's shipping update", "run the tracking report", "refresh the stuck-orders list".
---

# Tracking Report

You're being asked to surface the daily shipping-status update. Pick a
flow based on context.

## Stage 2 — post-only (the daily trigger's path)

This is what runs every day. The GitHub Action
`.github/workflows/daily-tracking.yml` already did the work at 13:00 UTC:
re-looked up every non-Delivered order on yuntrack, wrote status
updates back to the 2026 ORDERS sheet, and committed two artifacts to
the `claude/shipping-status-tracker-OCqtX` branch:

- `tracking-updates/daily-reports/<DATE>.txt` — the Slack message body
- `tracking-updates/daily-reports/<DATE>.csv` — the action-lists CSV

Your job at 14:00 UTC is to read those two files and post them.

### Steps

1. **Pull the latest commit** so today's artifacts are present:
   ```
   git pull --ff-only origin claude/shipping-status-tracker-OCqtX
   ```

2. **Find today's report files**:
   ```
   today=$(date -u +%Y-%m-%d)
   msg=tracking-updates/daily-reports/$today.txt
   csv=tracking-updates/daily-reports/$today.csv
   ```
   If either file is missing, the workflow either hasn't finished or
   failed. Check the latest commit (`git log --oneline -3`) and the
   workflow run on GitHub before doing anything else — do **not** fall
   back to ad-hoc lookups in this flow, that's expensive and the user
   explicitly chose option B to avoid it. Report the gap and stop.

3. **Read the message** via the Read tool.

4. **Post the main message** to `#team-order-tracking-updates`
   (channel id `C04PZVBS9GA`) using `mcp__3b0fa9c8-…__slack_send_message`.
   Capture the returned `message_ts` — you need it for the thread reply.

5. **Upload the CSV to Drive** via
   `mcp__9ceb8d52-…__create_file` with:
   - `title`: `tracking-action-lists-<DATE>.csv`
   - `contentMimeType`: `text/csv`
   - `disableConversionToGoogleType`: `true` (keep it as a real CSV, not
     a Google Sheet)
   - `parentId`: `1Q_gTAz6ViJt_IETPKqOw2JK80xG0mhQn` (the sheet's parent
     folder — inherits the same team-share permissions)

   Encode the file content as base64 before passing it as
   `base64Content`.

6. **Reply in-thread** with the Drive link via a second
   `slack_send_message`, this time with `thread_ts` set to the
   `message_ts` from step 4. Body template:
   ```
   Action lists as CSV: https://drive.google.com/file/d/<FILE_ID>/view

   Columns: `category, row_in_sheet, order, date, tracking, days_in_transit, status`. Categories: Stuck > 10 days, Stuck in Customs, Returned to sender, Fulfilled But Not Shipped, No Tracking.
   ```

7. **Stop.** Don't commit anything, don't push, don't follow up. The
   trigger session ends naturally.

### Things to watch for

- **Message body is counts-only, no order lists.** The user explicitly
  asked for the Slack post to stay short and the per-order detail to
  live only in the CSV thread reply. `build_message()` in
  `scripts/daily_tracking_job.py` already produces a ~500-char summary
  with one count per category. **Never paste order numbers, tracking
  numbers, row IDs, or bulleted lists into the main message** — even
  if a category only has 1-2 entries. Consistency every run, every
  category. If the user wants to see who's in a category, they open
  the CSV.
- **Don't re-look up parcels in this flow.** The whole point of Stage 2
  is that the Action did the lookup; your job is purely to deliver the
  pre-built artifacts. A 25-min yuntrack loop would burn Claude usage
  budget the user is explicitly trying to avoid.
- **The bot's identity.** Posts come from the Slack MCP's authenticated
  user (currently `U04PZNV9FV0`), not from a separate bot account. If
  the user wants posts to come from a `tracking-bot` instead, that's a
  separate setup task (see `.github/SLACK_SETUP.md`).

## Ad-hoc — full lookup + post

Use when the user wants a fresh report outside the cron window
(e.g. "run the tracking report now" at 4 PM). Three sub-paths in
descending preference:

1. **Workflow dispatch** — Trigger the daily workflow on GitHub
   (`mcp__github__` tooling or guide the user to the Actions page,
   `.github/workflows/daily-tracking.yml`). Same data flow as the cron,
   but kicked off now. Then wait for the commit on the branch and run
   Stage 2 above.

2. **Local lookup, no sheet write** — When the user wants you to
   draft the message for review before it goes out:
   - Download the sheet via `mcp__9ceb8d52-…__download_file_content`
     for `fileId=1D-FIUSN5BsLL7JIMSnvcjNWREPm3qxkbj6BfjPud4Rk` with
     `exportMimeType=text/csv`. Save as `/tmp/sheet.csv`.
   - **Use `csv.reader` for row numbering, never `awk`.** The sheet
     has ~700 multi-line quoted cells (notes / item descriptions);
     `awk`'s `NR` over-counts and you will write status updates to the
     wrong sheet rows. This is a bug that already bit us once.
   - Build the lookup input from the CSV (filter by status in
     LOOKUP_STATUSES, see `scripts/daily_tracking_job.py`).
   - Run `scripts/lookup_tracking.py` in the background; it flushes
     its queue file every 100 rows so partial results survive a kill.
     ~3,000 rows × 0.4 s/req ≈ 20 min.
   - Run `scripts/build_daily_report.py --csv /tmp/sheet.csv --queue
     <queue.json> --out-file /tmp/msg.txt --csv-out /tmp/lists.csv`.
   - Show the user the message, post via Slack MCP + Drive CSV as
     above.

3. **From-sheet fallback** — If the user just wants to see the current
   action lists from the sheet without any fresh lookup:
   - Download the sheet (same as path 2).
   - `python scripts/build_daily_report.py --csv /tmp/sheet.csv
     --from-sheet --out-file /tmp/msg.txt --csv-out /tmp/lists.csv`.
   - This skips the "Newly Delivered" metric (there's no diff signal
     in --from-sheet mode) but produces the four actionable lists
     accurately.

## Sheet / Slack reference

- Sheet ID: `1D-FIUSN5BsLL7JIMSnvcjNWREPm3qxkbj6BfjPud4Rk`
- Sheet tab: `2026 ORDERS`
- Sheet columns: A=Date, B=Order, C=Tracking, D=Shipping Update,
  E=Days in Transit, F=Notes
- Drive parent folder for CSV uploads:
  `1Q_gTAz6ViJt_IETPKqOw2JK80xG0mhQn`
- Slack channel: `#team-order-tracking-updates` →
  `C04PZVBS9GA`
- Branch: `claude/shipping-status-tracker-OCqtX`
- yuntrack rate-limit floor: 0.4 s between requests (don't lower)

## Don't

- Don't run a fresh yuntrack lookup in Stage 2 — that defeats the
  whole point of the split architecture and burns usage budget.
- Don't reclassify Canceled / Returned / Unable to Deliver rows; those
  are terminal and may be human-curated. `LOOKUP_STATUSES` already
  excludes them.
- Don't write to sheet column F — that's the user's Notes column.
  Only D (Shipping Update) and E (Days in Transit) are safe to update.
