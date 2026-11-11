# brand.json fields used by longform-ads

The skill reads `ads/brands/<brand>/brand.json`. The skeleton is in `ads/brands/_template/brand.json`, and the full worked example is `ads/brands/comfortwear/brand.json`.

## Shared brand fields

| Field | What it holds | Example (Comfort Wear) |
|---|---|---|
| `name`, `product`, `price`, `website` | Product facts used in the copy | "Ortho Stretch Cushion Shoe", "$59.95 (was $120)" |
| `audience`, `personas` | Who wears it and who the narrators can be | women only; nurse, CNA, teacher, traveler, retiree… |
| `prompt_rules` | Image rules for the product (when the product appears) | exact shoe from the reference photo, women wear it |
| `claims_to_avoid` | Never say these | podiatrist recommended, cure/treatment, star ratings |
| `confirmed_claims` | The only claims the close can make, with the confirmation date | 30-day money-back guarantee; 500,000+; HSA/FSA eligible |
| `offers` | Dated sale calendar: `name`, `start`, `end`, `line` (exact wording), `note` (combination rules) | Black Friday: 60% off sitewide OR buy-2-get-2-gifts (never combined), to Dec 5; Christmas: 60% off + 2 free gifts with 2 pairs, to Dec 31; New Year: 40% off + free shipping, Jan 1–15 |

## `longform_program`

| Field | Purpose |
|---|---|
| `atria_account` | Exact ad-account name in Atria, used by `atria_pull.py longform` |
| `schedule`, `schedule_trigger_id` | When the batch runs and which scheduled task runs it |
| `weekly_output`, `split`, `images_per_concept` | Batch size and mix (default: 10 = 6 iterations + 4 net-new), and 4 images per concept |
| `ids` | ID scheme. LF<nn> goes into ad names so results tie back to each copy |
| `category_terms` | Ad-library search terms for the category |
| `competitors_longform` | Direct competitors whose long-form must be read every run (page names included; competitors often post from "blog"-style pages) |
| `feedback_sheet` | Name and Drive file ID of the customer feedback or survey sheet |
| `reddit.subreddits`, `reddit.access_note` | Where the buyer talks, and what access works from the cloud |
| `notion.data_source`, `board_name`, `title_format`, `properties` | Where the cards go and how they're filed |
| `landing_pages` | Landing page per angle (reuse the source winner's page) |
| `image_rules` | Brand-specific image guardrails (who may wear the product, logos to avoid, settings to avoid) |
| `output_dir` | Usually `output/longform` |
| `research_sources`, `learning` | Notes on the research inputs and the transcription authorization |

## Onboarding questions to ask (only what you can't find)

1. Which Atria ad account? Which competitors run long-form in your category?
2. What exact offers are running, with dates, and which ones can't be combined? Is there a guarantee, and how many days? A customer count? Any eligibility claims (HSA/FSA, made in…)?
3. Which Notion board and properties should the cards use? Who's the strategist?
4. Where is customer feedback (survey sheet, reviews)?
5. What schedule, batch size and iteration/net-new split? How many images per concept?
6. Are Atria credits authorized for transcribing competitors' and the library's videos?
