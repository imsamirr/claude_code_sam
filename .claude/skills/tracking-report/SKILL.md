---
name: tracking-report
description: Run the shipping-status tracking refresh job ad-hoc — re-look up every non-Delivered order on yuntrack, write status updates back to the 2026 ORDERS sheet, and post a daily summary plus action-lists CSV to #team-order-tracking-updates. Use when the user wants to trigger an off-schedule run (e.g. "run the tracking report now", "post today's shipping update", "refresh the stuck-orders list"). The scheduled cron at .github/workflows/daily-tracking.yml already fires Mon/Wed/Fri 13:00 UTC, so prefer that for routine reporting; this skill is for one-offs.
---

# Tracking Report — Ad-Hoc Run

You are being asked to run the order-tracking refresh outside of its
scheduled Mon/Wed/Fri 13:00 UTC cron. There are two paths; pick based on
what the user actually wants.

## Decide first: production or sandbox?

Ask the user (briefly) if it isn't already obvious:

- **Production** — *update the real sheet and post to the real channel.*
  Trigger the GitHub Action via `workflow_dispatch`. This is the right
  path 95% of the time — same secrets, same Python, same data flow as
  the cron job, with no chance of writing the wrong values from a local
  CSV that's already gone stale.
- **Preview only** — *don't touch the sheet, just see what the report
  would look like.* Either trigger `workflow_dispatch` with the
  `dry_run` input checked (it will skip sheet writes but still post to
  Slack), or run locally with the steps below if Slack must also be
  suppressed.

## Path A — production / preview via GitHub Actions

Find the workflow and dispatch it (requires the GitHub MCP tools):

1. The workflow file is `.github/workflows/daily-tracking.yml` on the
   `claude/shipping-status-tracker-OCqtX` branch (or whatever branch is
   current; check `git branch --show-current`).
2. Use `mcp__github__` tooling to dispatch the workflow — there is no
   direct workflow-run dispatch tool exposed by default, so guide the
   user to click *Run workflow* on the Actions page, OR use the GitHub
   REST API via curl with a PAT.
3. Watch for the workflow's commit on the branch (`Mark tracking
   updates as applied`) the same way the apply workflow's runs are
   tracked. Use a Monitor that polls `git fetch` + `git log` on the
   branch. Do **not** poll via Bash `sleep` loops.
4. When it lands, fetch and share the Slack permalink — the workflow
   logs print it after `chat.postMessage` returns.

Required secrets (must already be configured):

- `GOOGLE_SA_JSON` — service account with Editor on the sheet
- `SLACK_BOT_TOKEN` — `xoxb-…` token; bot must be in
  `#team-order-tracking-updates` (`C04PZVBS9GA`) and hold `chat:write`
  plus `files:write` scopes.

## Path B — local lookup (no sheet write, custom Slack send)

Use this only if the user wants you to control the post yourself
(e.g. "draft the message, let me review before sending") or the
service account is unavailable. The lookup itself works fine without
any Google credentials.

1. Refresh the sheet snapshot:
   ```
   mcp__9ceb8d52-...__download_file_content fileId=1D-FIUSN5BsLL7JIMSnvcjNWREPm3qxkbj6BfjPud4Rk exportMimeType=text/csv
   ```
   The result is too large for the chat — it gets persisted to disk; jq
   the `.content` field and base64 -d to recover the CSV. Save as
   `/tmp/sheet.csv`.

2. **Use `csv.reader` for row numbering, never `awk`.** The sheet has
   ~700 multi-line quoted cells; `awk`'s `NR` over-counts and you will
   write status updates to the wrong sheet rows. This is a real bug
   that already happened once on this project — don't repeat it.

3. Build the lookup input:
   ```python
   import csv, json
   LOOKUP_STATUSES = {"", "In transit", "Stuck In Transit",
                      "Stuck in Customs", "Out For Delivery",
                      "Ready for Pick Up", "Fulfilled But Not Shipped"}
   with open('/tmp/sheet.csv', newline='') as f:
       reader = csv.reader(f); next(reader)
       targets = [
           {"row": i, "tracking": r[2].strip()}
           for i, r in enumerate(reader, start=2)
           if len(r) >= 6 and r[2].strip() and r[3].strip() in LOOKUP_STATUSES
       ]
   json.dump(targets, open('/tmp/in.json', 'w'))
   ```

4. Run the lookup. ~3,000 rows takes ~25 min — kick it off with
   `Bash run_in_background=true` so the foreground stays responsive,
   and arm an `until ! kill -0 <pid>` watcher for completion:
   ```
   nohup python -u scripts/lookup_tracking.py /tmp/in.json --delay 0.4 \
     --out daily-$(date -u +%Y%m%dT%H%M%S).json \
     > /tmp/lookup.log 2>&1 &
   ```
   The script flushes its queue file every 100 rows, so if anything
   gets killed mid-run the partial results survive.

5. Generate the message + CSV from the queue file:
   ```
   python scripts/build_daily_report.py \
     --csv /tmp/sheet.csv \
     --queue tracking-updates/queue/daily-*.json \
     --out-file /tmp/slack_msg.txt \
     --csv-out /tmp/action_lists.csv
   ```

6. Show the user the message preview, then post via Slack MCP:
   - Main message: `mcp__3b0fa9c8-...__slack_send_message` to channel
     `C04PZVBS9GA`. Capture the returned `message_ts`.
   - CSV: there is no Slack file-upload MCP tool — upload the CSV to
     Drive via `mcp__9ceb8d52-...__create_file` (contentMimeType
     `text/csv`, `disableConversionToGoogleType: true`, parent
     `1Q_gTAz6ViJt_IETPKqOw2JK80xG0mhQn`), then `slack_send_message`
     a thread reply with the Drive view URL using the captured
     `thread_ts`.

7. Commit and push the queue file so the apply workflow updates the
   sheet:
   ```
   git add tracking-updates/queue/daily-*.json
   git commit -m "Ad-hoc tracking refresh queue"
   git push -u origin <current-branch>
   ```

## Reading the report

The Slack message has these sections — same in either path:

- **In Transit** count, **Newly Delivered** count + avg delivery days
- **🚨 In Transit > 10 days** — generic stuck (any non-customs facility)
- **⚠️ Stuck in Customs** — latest event is "In clearance processing"
  or similar customs-hold wording
- **Returned to sender**, **Fulfilled But Not Shipped** (label created
  but carrier never picked up), **No Tracking Numbers** (open orders
  without a tracking number)

The CSV attached in the thread has every actionable row across those
four categories, columns `category, row_in_sheet, order, date,
tracking, days_in_transit, status`.

## Don't

- Don't ask the user to set up the Slack bot or service account from
  inside this skill. If a secret is missing, surface the error from the
  workflow log and point at the workflow header, which lists the
  required scopes.
- Don't run more than one lookup batch concurrently against
  yuntrack — they share a request quota and you'll start getting WAF
  blocks. The 0.4 s inter-request delay is the floor.
- Don't reclassify Canceled / Returned to sender / Unable to Deliver
  rows — those are terminal and may be human-curated. The
  `LOOKUP_STATUSES` set already excludes them.
