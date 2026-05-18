# Slack bot setup for the daily tracking workflow

The workflow at `.github/workflows/daily-tracking.yml` needs one secret —
`SLACK_BOT_TOKEN` — before it can post to `#team-order-tracking-updates`.
The other secret it uses (`GOOGLE_SA_JSON`) is already in place.

Total time: ~3 minutes.

---

## 1. Create the Slack app (2 min)

1. Open <https://api.slack.com/apps?new_app=1>.
2. Pick **From a manifest**, then choose the **ComfortWear** workspace.
3. Paste this YAML and click **Next** → **Create**:

   ```yaml
   display_information:
     name: Tracking Bot
     description: Posts the daily shipping status report
   features:
     bot_user:
       display_name: tracking-bot
       always_online: false
   oauth_config:
     scopes:
       bot:
         - chat:write
         - files:write
   settings:
     org_deploy_enabled: false
     socket_mode_enabled: false
     token_rotation_enabled: false
   ```

4. On the app page, click **Install to ComfortWear** → **Allow**.
5. Go to **OAuth & Permissions** in the left sidebar.
6. Copy the **Bot User OAuth Token** — it starts with `xoxb-…`.
7. In Slack, open `#team-order-tracking-updates` and run:
   ```
   /invite @tracking-bot
   ```
   This is required because the channel is private; without it you'll
   see a `not_in_channel` error in the workflow log.

## 2. Add the token to GitHub (30 sec)

Open this URL:

> <https://github.com/imsamirr/claude_code_sam/settings/secrets/actions/new>

Fill in:

- **Name**: `SLACK_BOT_TOKEN`
- **Secret**: paste the `xoxb-…` value from step 1.6
- Click **Add secret**

## 3. Verify the schedule

The workflow runs automatically every day at **13:00 UTC** (≈ 08:00 ET
winter / 09:00 ET summer). Next run is the next 13:00 UTC after the
secret lands.

To verify without waiting for the cron:

1. Open <https://github.com/imsamirr/claude_code_sam/actions/workflows/daily-tracking.yml>
2. Click **Run workflow** → leave **dry-run** checked → **Run workflow**.
3. Watch the run. Dry-run skips the sheet write but still posts to
   Slack, so a green check + a Slack message means everything is wired.

## What gets posted

A message to `#team-order-tracking-updates` (channel id `C04PZVBS9GA`)
with these sections, followed by a CSV attachment as a thread reply:

- In Transit total + Newly Delivered + avg delivery days
- **🚨 In Transit > 10 days** — generic stuck parcels
- **⚠️ Stuck in Customs** — latest event is "In clearance processing"
  or similar customs-hold wording
- **Returned to sender**
- **Fulfilled But Not Shipped** — label created but carrier never
  picked up
- **No Tracking Numbers** — open orders without a tracking number

CSV columns: `category, row_in_sheet, order, date, tracking,
days_in_transit, status`.

## Troubleshooting

| Workflow error | Fix |
| --- | --- |
| `not_in_channel` | `/invite @tracking-bot` in `#team-order-tracking-updates` |
| `missing_scope` on file upload | Re-open the app at api.slack.com → OAuth & Permissions → Add `files:write` → Reinstall |
| `invalid_auth` | Token was rotated or revoked — regenerate at OAuth & Permissions and update the GitHub secret |
| Workflow doesn't fire on the cron | GitHub disables scheduled workflows on repos with no activity for 60 days; push any commit to wake it up |
