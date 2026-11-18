# ComfortWear past-script library: index

Exported from Notion (read-only) on 2026-11-18. **This is a partial export.** Most script bodies have not been exported yet. See "Coverage" below.

## Files

| File | Source (Notion) | Rows in source | Scripts with full text in file | Notes |
|---|---|---|---|---|
| `scripts_2026.md` | 📅 Scripts 2026 > Creative Strategy Tracker | 435 (COM1–COM4xx, created 2026-04-23 → 2026-11-18) | 1 (COM104) | Only COM104 was fetched. |
| `scripts_2026_catalog.md` | same | 42 listed | 0 | Property-level rows for the 42 rows visible in the September view only. |
| `tracker_old_version.md` | ComfortWear Creative Tracker \| Old Version > Creative Brainstorming | 698 (COM01–COM698, created 2025-09-27 → 2026-04-30; launch dates 2026-03-11 → 2026-05-13) | 6 (COM643, 638, 637, 635, 634, 624) | 4 more were fetched but the page body is empty because the script lives in the "Shot List" sub-database (COM628, 625, 620, 619). |
| `tracker_old_version_catalog.md` | same | 692 listed | 0 | One row per unexported row: concept name, type, format, angle, product, status, launch date, Analysis, Learnings, Hypothesis, Idea. |
| `angle_databank.md` | ComfortWear Ad Angle Databank | 167 | n/a (one table) | Complete. Report dates 2026-03-26 → 2026-06-15. All rows are "Not started" and none has Performance Notes. |
| `master_tracker.md` | Master Creative Tracker > Creative Brainstorming (older hub) | 180 (created 2025-09-25 → 2025-09-28) | not written | It looks like the original copy of COM01–COM~180, which was duplicated into the Old Version tracker on 2025-09-27. I have not checked this row by row. |

Rows with no script/brief text: 4 confirmed (the Shot-List-only rows above). The rest are unknown until their pages are fetched.

## Where results and learnings live

- **Scripts 2026:** the `Learnings` text property. `Status` = "🏆 Winner" or "Launched" shows the outcome. There is no separate metrics field.
- **Old Version tracker:** two places.
  - `Analysis` is a select with the verdict: Kill / almost there / Winner! / iteration - new hook/body/creator/spanish / Landing Page Issue / Low Spend.
  - `Learnings` is free text, filled on 56 rows (mostly COM490–COM643, launched Mar–May 2026). A legacy `Learnings:` field is filled on 9 rows.
  - `Claude Score` / `Claude Feedback` hold AI brief-quality grades, not ad results, so I did not export them.
- **Angle Databank:** `Performance Notes` exists but is empty on all 167 rows.
- **Master tracker:** a `Learnings:` property. I did not query it.

## Themes

- **Personas:** nurses and 12-hour shifts dominate (Nurse is the top angle in both trackers). Then teachers, retail and restaurant workers, seniors and fall prevention, travel/Disney, overweight/plus-size women, plantar fasciitis, neuropathy/diabetic, and Spanish-language versions.
- **Formats:** Prob/Sol (68), UGC testimonial (35), comparison/ranking ("we rated 5 nurse shoes", podiatrist rates shoes), "3 reasons why" (incl. reverse-psychology "3 downsides"), AI doctor/podiatrist avatar and podcast style, AI + existing-footage mash-ups, statics, AI songs and cartoons.
- **Recurring claims:**
  - competitor call-outs (Hoka, Brooks, Skechers, Crocs, Asics, OrthoFeet)
  - arch support that "holds its shape through hour 12"
  - wide toe box for swelling and bunions, wet-floor grip
  - under $60 / 40% off, HSA/FSA eligible, 45-day guarantee, 500K+ customers
- **Products:** Ortho Stretch shoe (~88% of rows), Flow Hands-Free, Daily Slip-On.

## Coverage, and what blocked a full export

- Each row's script has to be fetched one page at a time with the Notion MCP. That is about 1,300 pages across the three trackers.
- Many older briefs (Iterations especially) keep the per-shot script in an inline "Shot List" sub-database. That needs 2 more calls per row.
- The Notion SQL/rows query allowance ran out early in the run, and it is shared with a parallel export. Because of that, the full Scripts 2026 row list could not be pulled. Only its single saved view, filtered to September, was readable.
