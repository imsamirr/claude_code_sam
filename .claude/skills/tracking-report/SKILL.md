---
name: tracking-report
description: Post the daily shipping-status report. The daily GitHub workflow already committed today's pre-built message + CSV under tracking-updates/daily-reports/. Read those, post to #team-order-tracking-updates via Slack MCP, upload CSV to Drive, thread the link. Use for the daily trigger, "run the tracking report", "post today's shipping update", or "refresh the stuck-orders list".
---

# Tracking Report

## Stage 2 — post-only (daily trigger path)

You're posting today's report. The artifacts are already on disk in
the freshly-cloned repo; do not re-run yuntrack lookups.

1. `today=$(date -u +%Y-%m-%d)`. The artifacts are
   `tracking-updates/daily-reports/$today.txt` and `.csv`.
   If either file is missing the GitHub workflow either hasn't
   finished or crashed — check `git log --oneline -5` and the
   workflow run. Don't fall back to a fresh lookup; report the gap
   and stop.

2. Read the `.txt` body via Read.

3. Post it to `#team-order-tracking-updates` (`C04PZVBS9GA`) using
   `mcp__3b0fa9c8-...__slack_send_message`. Capture `message_ts`.

4. Upload the CSV to Drive with
   `mcp__9ceb8d52-...__create_file`:
   - `title`: `tracking-action-lists-<DATE>.csv`
   - `contentMimeType`: `text/csv`
   - `disableConversionToGoogleType`: `true`
   - `parentId`: `1Q_gTAz6ViJt_IETPKqOw2JK80xG0mhQn`
   - `base64Content`: base64 of the `.csv` bytes

5. Reply in-thread (`slack_send_message` again, `thread_ts =
   message_ts` from step 3):

   ```
   Action lists as CSV: https://drive.google.com/file/d/<FILE_ID>/view

   Columns: `category, row_in_sheet, order, date, tracking, days_in_transit, status`. Categories: Stuck > 10 days, Stuck in Customs, Returned to sender, Fulfilled But Not Shipped, No Tracking.
   ```

6. Stop. Don't commit, don't push, don't follow up.

### Hard rules

- **Counts-only message body.** `build_message()` produces the ~500-char
  summary already. Never paste order numbers, tracking numbers, or
  bulleted lists into the Slack message body — even for tiny
  categories. Detail lives only in the CSV.
- **No yuntrack lookups in this flow.** The Action did the work; you
  just deliver it. A 25-min lookup loop in a Claude session would
  burn the user's plan budget for zero added value.
- **Don't touch sheet column F.** That's the user's Notes column.
  `daily_tracking_job.py` already writes only D and E (Status, Days).

## Ad-hoc — manual lookup + post

Use only when the user explicitly wants a fresh lookup outside the
cron, or the daily artifacts are missing and they want a recovery.
Order of preference:

1. **Workflow dispatch** (`.github/workflows/daily-tracking.yml` →
   *Run workflow*). Same code path as the cron. Wait for the
   `Daily tracking report — <DATE>` commit on the branch, then run
   Stage 2 above.

2. **Local lookup + post** (~25 min, expensive in a Claude session):
   - Download the sheet via
     `mcp__9ceb8d52-...__download_file_content`
     `fileId=1D-FIUSN5BsLL7JIMSnvcjNWREPm3qxkbj6BfjPud4Rk`
     `exportMimeType=text/csv`, save as `/tmp/sheet.csv`.
   - **Use `csv.reader` for row numbering, never `awk`** — the sheet
     has multi-line quoted cells and `awk NR` over-counts. Real bug
     this project already hit.
   - Build the lookup input by filtering `LOOKUP_STATUSES` (see
     `scripts/daily_tracking_job.py`), run
     `scripts/lookup_tracking.py` in the background (~17-25 min,
     flushes every 100 rows), then
     `scripts/build_daily_report.py --csv /tmp/sheet.csv --queue
     <queue.json> --out-file /tmp/msg.txt --csv-out /tmp/lists.csv`.
   - Post via Slack MCP + Drive CSV as in Stage 2.
   - Commit the queue file (apply workflow updates the sheet).

3. **From-sheet preview** (`build_daily_report.py --csv ...
   --from-sheet`) — instant, no Newly-Delivered metric. Use when the
   user just wants to see the action lists from current sheet state.

## Reference

- Sheet: `1D-FIUSN5BsLL7JIMSnvcjNWREPm3qxkbj6BfjPud4Rk` tab `2026 ORDERS`
- Sheet columns: A=Date, B=Order, C=Tracking, D=Shipping Update,
  E=Days in Transit, F=Notes
- Drive parent: `1Q_gTAz6ViJt_IETPKqOw2JK80xG0mhQn`
- Slack channel: `C04PZVBS9GA`
- Branch: `claude/shipping-status-tracker-OCqtX` (until merged)
- yuntrack rate floor: 0.4 s between requests
