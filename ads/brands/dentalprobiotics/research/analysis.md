# DentalPULSE Advanced Dental Probiotics: research

Sources: Sam's master brief "Everything we know about the oral probiotic opportunity" (Oct 12, 2026;
585 Amazon reviews, 347 TikToks, ~16k comments), Sam's Atria scan of oral-care advertisers (Oct 12),
and our own Atria pulls (`data/competitor_ads.csv`, 971 ads from 18 brands; `data/inspiration_raw.csv`,
376 rising image ads). Contact sheets are in `sheets/`. No ad-account history yet (new product), so no
winners, losers or ROAS.

## 1. Product and guardrails

- One blue jar of daily capsules: BLIS K12 2B CFU, zinc gluconate, sodium copper chlorophyllin,
  berberine HCl, artichoke leaf (2.5% cynarin), bromelain, papain. Same formula as NOURI's
  "Three-Source Breath Formula"; the formula alone doesn't set it apart.
- The ads show the "ADVANCED DENTAL PROBIOTICS" label (user, Oct 12), not "Advanced Breath Support".
- Approved claims: Doctor Recommended, 3rd Party Lab Tested in USA, 90-day money-back guarantee,
  strain + CFU + ingredients. No price on ads.
- Structure/function wording only: "supports fresher breath / healthy gums / oral microbiome". Never
  "cures", "dissolves stones", "reverses cavities", "treats gum disease/SIBO". No liver breath,
  no fluoride conspiracy.
- Meta personal attributes: no "Do you have bad breath?" or "Are you on Ozempic?". Use first person,
  third person or product framing.
- Illustrated tonsils/tongues, not real stone close-ups.
- Berberine caution on GLP-1 / diabetes ads.
- Open issue in the brief: the label's "Supports Gum Disease" reads as a disease claim (fix on the
  pack). Testimonials must come from real customers before spend.

## 2. Scale angles (brief)

1. Core bad breath: "You brush, floss and rinse. Here's what your routine misses."
2. Mouth + gut, reframed: "Bad breath has two sources: mouth and gut." (80–90% starts in the mouth.)
3. Tonsil stones: "The smell isn't coming from your teeth. It's behind your tongue." (98M plays.)
4. Social signals: "The coworker who offered you gum wasn't being polite."
5. White tongue coating: "Scraping removes it. This changes why it comes back."
6. Mouthwash dependence: "Your mouth isn't supposed to be sterile."

Tests: GLP-1 breath (open lane, only Wellnesse), after antibiotics, aligners/retainers (Dental Pod
cross-sell). Gums: support role only.

## 3. Competitors: what's running

| Brand | Longest-running image formats and hooks |
|---|---|
| NOURI (171d) | Benefit-icon pack shot "Bad breath, not anymore"; copy "Why every mouthwash & mint fails"; 3-source (gut, mouth, liver) story; advertorial funnel |
| Deos (40d) | Tongue-out selfie with handwritten sticky note "10 years of bad breath. Gone in one week."; microbiome split (unbalanced vs balanced); "F*ck morning breath"; "Stop f*cking masking your breath, it starts in your gut"; "Your dentist said your teeth are fine" |
| Riverwell (11–13d, scaling) | Two cartoon faces "Clean the sulfur gas off your tongue"; X-ray "40% have these. Most never see them."; 4-panel tonsil comic; "We have made too much" warehouse; "Your teeth are clean. Your throat isn't." |
| Breath Lab (106d) | Office scene + myth caption "Most people think bad breath comes from poor hygiene"; wrist lick test; old vs new formula |
| Breevelle (173d) | Romance narratives: "He started leaning in again", "The kiss he will not stop replaying" |
| Cool Breath (388d) | "Kiss-ready breath in 3 sec", "Stop using gum" |
| NOBS | Protest sign on a city street; "Now at Target" hand-held jar; product + review card |
| SuperTeeth | Quote-card testimonial; "Dentists keep recommending this one"; benefit pills |
| Wellnesse | "92%" big-number study tile; GLP-1 angle; day 1 vs day 60 |
| LIVFRESH | Offers (Buy 2 Get 1), "Yes, it's pricier", review card + bundle |

Rising inspiration (all categories): "Official Apology Statement" letter, "What 30 days does"
day-grid (tongues), big-number tiles, celebrity/UGC holding jar, foreign-language advertorial cards.

## 4. Formats to take

1. Name the old routine (gum, mints, mouthwash, scraper) and show it failing.
2. Native UI: X post, Facebook comments, Trustpilot card, iMessage thread, Notes checklist.
3. Shock stat + medical visual (X-ray, illustrated throat cross-section).
4. Sticky-note / ugly UGC selfie with jar.
5. Protest sign / street photo.
6. Romance payoff lines (partner leans in again).
7. Mechanism cartoons (comic strip, claymation bacteria moving out, 1930s old way vs new way).
8. Big-number type ("15 MINUTES").
9. Starter-pack flat-lay of everything they've tried.
10. Trust tile: lab tested, doctor recommended, 90-day guarantee, strain + CFU.
11. Apology letter and day-by-day grid from the inspiration pull.

## 5. Personas and mix

Personas live in `brand.json`. Launch mix (`weeks/2026-W42-launch`, 30 statics): 12 core bad breath,
6 mouth + gut, 6 tonsil/throat, 6 tests (GLP-1, aligners, gums, skeptic, after antibiotics, romance).

## 6. Perio breath (research Oct 12, batch `weeks/2026-W42-perio`)

- About 4 in 10 US adults over 30 have gum disease (42–47%; 70% of 65+). People with it are ~3.6x more
  likely to have measurable bad breath. Most don't know they have it: the clues are blood on the
  brush or floss, floss that smells, and breath that's back by lunch.
- The fear is closeness, not hygiene: 85% of UK singles call bad breath the biggest turn-off, 80%
  wouldn't go on a second date; one 10-second kiss passes ~80 million bacteria.
- Gap: romance ads sell sprays that mask; gum ads sell devices/softgels. Nobody links bleeding gums
  to breath failing up close.
- Audiences: long-term partner (biggest), dater (urgent), late-night crowd, partner who can't say
  it (gift / routine for two), 40+ women with gum changes.
- Copy rules (user Oct 13): plain words, no technical terms (no strain names, "periodontitis",
  "sulfur compounds"), aggressive. Safe: "supports fresher breath and healthy gums", "daily support
  between cleanings", "bleeding gums are a sign to see your dentist". Never: treats/reverses gum
  disease, replaces cleanings, "contagious", "Are you hiding gum disease?", sexual language.
