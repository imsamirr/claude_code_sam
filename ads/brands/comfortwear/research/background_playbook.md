# Background playbook (started 2026-11-18)

Why this exists: in 2026-W47-fri and 2026-W47-tue about half the ads sat on a plain white / light-grey / pastel
studio field. The cause was our own prompt prefix ("white or very light backgrounds") plus inspiration taken only
from the `atria_pull.py wellness` growth list, which is dominated by flat product tiles. "Never a dark shoe on a dark
background" means the area AROUND THE SHOE must be light or mid-tone; it does not mean the whole ad must be white.

## Where backgrounds come from (every run)
1. **Atria MCP `search_library_ads`** (not only the API pulls), image, active, US, en, `collapse_variants`,
   `order=most_impressions`, industries Apparel / Health & Medical / Beauty / Fitness:
   - proven: `min_days_running=60`;
   - rising: `launched_after=<today-45d>`, `min_days_running=10`, `impression_trend=rising`;
   - seasonal: `theme=[holiday_festival, seasonal, post_it_notes, UGC]`, `min_days_running=7`.
2. **Atria MCP `search_ad_templates`** (hand-picked set), industry Apparel, themes lifestyle / seasonal_holiday /
   ugc_testimonial / problem_solution.
3. Contact-sheet all results, read every page, add new families below with the source ad (advertiser, days, rank).

## Families (source in Atria, how we use it, colorway pairing)
| # | Family | Atria evidence (2026-11-18) | Our use | Shoe colors that work |
|---|---|---|---|---|
| 1 | Real place that carries the mood (no product focus in the scene) | Sara Garret misty river path 136d #1/179; Deb Rustad cornfield sunset 46d; Flawless After 40 lake 21d | grey fall morning path, Lisbon street at dusk, park bench after a shift, hospital parking lot at sunrise | light/mid shoes; all-black only on pale stone |
| 2 | Real storefront / landmark context | NOBS at Target 70d | hand holding the shoe in front of a hospital entrance or an airport gate (no logos, no castles) | any |
| 3 | Seasonal: fall leaves, warm amber | Ledisa fall 50% #1/246; smileactives "Fall Event" 14d rising | shoe on porch steps / wood table with maple leaves, warm bokeh | black/purple, black/white, red, navy on light wood |
| 4 | Seasonal: holiday | Summary red ornaments 11d rising; Tatcha / Josie Maran holiday sets | shoe under a tree, shoes as ornaments, gift box with tissue, first-frost window | light shoes on deep red; dark shoes on white snow/tissue |
| 5 | Textured prop surface + handwriting | Dr. Clarke wood table + price stickers 19d; Avalaine warehouse box + sticky note 166d | oak table with sticky notes, cork board with pins, cardboard box in a warehouse, locker shelf | any (light props) |
| 6 | The "graveyard" of what she tried | Nancy Anderson trash can 149d #1/106 | trash can / donation bag full of insoles, creams, ice packs, worn sneakers, our shoe in hand | any |
| 7 | Saturated color field + photo/polaroid | Medtronic cobalt polaroid 19d rising; OKOA cobalt text 42d; Sourse plum 20d; FEM+ pink | cobalt / plum / tomato / butter-yellow field with a tilted real photo and the shoe | red, light grey, grey/pink, white-blue on cobalt or plum; NEVER navy/all-black on dark fields |
| 8 | Grayscale photo + one color | Atria template New Balance (seasonal/urgency) | black-and-white photo of scrubs or a park day where only our shoe is in full color | purple, turquoise, red (color pops) |
| 9 | Elements / action | Atria template boots in water; Vitaclean shower 30d | shoe stepping through a puddle on a wet path, rain on cobblestones, wet hospital floor sign | light/mid shoes; all-black only with bright wet reflections |
| 10 | Real interior at a time of day | Flawless/UGC sets | 5am bedroom floor in first light, hotel bathroom tile, break-room table at 3am | any |
| 11 | Bold illustrated / hand-drawn frame | Primal Storm hand-drawn 10d | marker doodles around a real shoe photo on kraft paper | any |
| 12 | Plain studio field (white/grey/pastel) | many | ONLY for our proven layouts (dear_nurses_callouts, sale three colors) | any |

## Rule (brand.json `program.background_rule_2026_11_18`)
Every concept sets `"background"` (family number + one-line description) and `"background_source"` (Atria ad).
Per batch: family 12 (plain studio) on at most 15% of concepts; no family on more than 20%; at least 3 seasonal
(families 3-4) from November to December; QA rejects a render whose background turned into a plain studio wall
when the concept asked for a scene.

## 2026-11-20 Atria MCP backgrounds (W48-fri)
Source: Atria MCP `search_library_ads` (proven 60d+, rising since 2026-10-06, seasonal/holiday/post-it/UGC, Black Friday,
Thanksgiving) + `search_ad_templates`; 238 candidates contact-sheeted (`research/sheets/atria_mcp_w48fri_*.jpg`); 34 picks saved
as `reference/benchmarks/rv420_*.jpg`. New families:

| # | Family | Atria evidence (2026-11-20) | Our use | Shoe colors that work |
|---|---|---|---|---|
| 13 | Printed paper on a real table (newspaper, shopping list, coupon) | Konjoun newspaper "Early Black Friday" 12d rising; Anabar checked grocery list 22d | BF offer as a newspaper headline next to coffee; Thanksgiving / packing list with our shoe ticked | any (light wood or kitchen table) |
| 14 | Natural woven texture (burlap, linen, folded knit stack) | ShopRite Thanksgiving burlap 10d; We are Amma folded knit stack 78d | burlap Thanksgiving offer; stack of fall-colored knits behind the shoe (knit = our material) | black/purple, red, navy on light burlap; light shoes on the darker knit rows |
| 16 | Boutique display riser / shop shelf | Bella Belts BF tiered riser 14d | all colorways on a 4-tier riser, BF ribbon bands | light and mid shoes on black tiers; no all-black |
| 17 | Holographic / iridescent foil | Noobru Black Friday foil 17d | BF early-access / announcement with the shoe on foil | white, grey, black/purple (foil is light) |
| 18 | Outdoor signage in a real place (yard sign) | Dr. Richard Calloway lawn sign 84d proven | a contrarian statement on a yard sign; the shoe on the porch step | any |
| 19 | Clinical room (exam room, PT gym, nurses' station) | Carol Bennett podiatrist exam room 31d; Kirsty Phillips nurses' station 61d; David Parker PT clinic 11d | unnamed podiatrist character examining a foot (bunions); nurse station at 3am | black/white, white/blue, black/purple (nurse colors) |
| 20 | Travel gear flatlay (open bag, suitcase) | Basic Jane weekender bag 10d rising | open carry-on with sweater, passport, our pair packed | any light/mid |
| 21 | Dynamic splash / exploding materials | Q Collection golden splash 35d rising | the shoe center with knit fibers, cushioning and leaves flying around it | light/mid shoes on warm gold |

Also refreshed with new sources: family 3 (My Derma Dream maple-leaf border 29d; Proper Wild harvest basket 8d rising),
family 4 (Plant Therapy string lights on orange 22d; TULA snow drift 9d rising; Rumpl gift handoff 7d; MacKenzie-Childs
plaid gift box UGC 9d), family 1 (Judy Callihan suburban street 73d; Earthing sunlit lawn 19d), family 11 (vintage oil
painting, Tiffany Mccomb 62d; pop-art comic, Mane Strong 16d).
