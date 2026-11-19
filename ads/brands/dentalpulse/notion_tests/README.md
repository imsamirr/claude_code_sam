# DentalPULSE: what has been tested (Notion inventory)

Snapshot taken 2026-11-19 of every brief on the DentalPULSE Notion creative hub:
- Monthly script boards, Apr–Nov 2026 (DEN codes)
- The old DentalPULSE Creative Tracker, Nov 2025–Apr 2026 (D codes)
- The Native Ads advertorial tracker (long-form statics, D codes; Mar–Jul 2026)

Each brief was read in full. `primary_angle`, `format` and `appliance` come from the script itself, not the
Notion properties. `written` is true only when the task page holds real script/brief copy (title-only, template,
link-only or inspo-only pages are false). Advertorials were classified from the tracker's concept, hook and
image-prompt fields; their full copy sits in ZIP attachments that were not opened.

Use `tested_briefs.json` (or the CSV) to answer "have I already tested this?": search `title`, `hooks`,
`angle_summary`, `primary_angle`, `secondary_angles`, `format`, `appliance`, `competitors_named`.
Live matrix page: https://claude.ai/artifact/QZ2Pb6B7eFztL4vpx6VNM5

Known data issues on the board:
- 60 ad codes are used for two different concepts (e.g. DEN215–226 in both Aug and Sep, DEN314–319 in both
  Oct and Nov, D73–D89 in both the Creative Tracker and the advertorial tracker). Rows carry `code_reused: true`.
- Month = the board a brief sits on (monthly scripts) or its created month (trackers). Some rows were created
  in a different month than the board they live on.
