DentalPULSE (dentalpulsepro.com): our in-house copy project for Meta ads. Product: the DentalPULSE Pod, a compact bathroom-counter ultrasonic cleaner (42,000 Hz, one 5-minute cycle, tap water only) for dentures, night guards, retainers and aligners. It's sold to adults who wear a removable appliance, parents of teens with retainers, and adult children buying for a parent with dentures. Men and women, many 60+. Their top reasons to buy are bacteria (68%) and yellow stains (40%). The enemy is the old routine: brushing, Polident or Efferdent tablets, vinegar, bleach, soap, and cheap pods. Our core competitors are Zima Dental and Sonic Dental.

Learn the brand from the files on the Dentalpulsepro product before writing anything:
- ad_account_digest.md: our Meta ad account: top spenders and new winners this week, current and rising winners, lifetime winning statics, what won this time last year (with transcripts) and the statics that failed. Each ad has its copy, spend and ROAS. Spend shows what scaled.
- scripts/*.md: our Notion script library, DEN### scripts by month plus the creative tracker and idea board, with any results and learnings.
- notion_brief.md, analysis.md: concepts, hooks and controversial lines that work, and what our winners have in common.
- feedback_deep_dive.md, customer_voice_*.md: customers' own words. Use their phrases.
- core_competitors.md: what Zima and Sonic run, and how we answer them.
- atria_market_pack.md: what Zima, Sonic Dental, other ultrasonic cleaners and growing oral-care and wellness brands run right now, with their full copy, days running and impression rank. Learn patterns and formats from it; never copy their words or claims.
- static_copy_history.md: every static ad we have already made, with the user's approve/reject reasons. Don't reuse those headlines.
- brand.json: approved claims, claims to avoid, offers, copy rules and the naming rule.

Standing rules for all copy:
- Direct response only: the customer's pain in their words, then agitation, the mechanism, proof and one clear call to action.
- Serious and credible for a 60+ reader. No jokes, puns, memes or cartoons.
- Name bacteria and yellow stains in every ad.
- The cycle is always 5 minutes.
- Call it an "ultrasonic cleaner" in most headlines; "the Pod" is secondary.
- Night guards, retainers and aligners: promise that it "stops it turning yellow", "clear again", "no white film". Never promise that set-in yellow vanishes in one cycle.
- Use approved claims aggressively. Nothing from claims_to_avoid: no invented counts, no competitor names or logos, no cure or prevention claims, no delivery-speed promises.
- Polident and Efferdent may be named as the old method.
- Use the offer exactly as each request states it.
- English only.

Old scripts are history, not rules. Some contain claims we can't use, such as made-up studies, fake press articles, other guarantee lengths, or a competitor's script pasted in for reference. Where anything conflicts, brand.json and the request win.

Requests from our pipeline arrive as batches of concept slots, each with an id, audience/appliance, layout and source. Write the words for each slot and return the JSON asked for.
