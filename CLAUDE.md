# Ad copy rule: StefanBrain writes every word

**User rule (2026-11-18): whenever copy needs to be written, it ALWAYS goes through StefanBrain.** StefanBrain
(Stefan Georgi's copywriting AI) is the copywriter for both brands. This covers ad headlines, on-image text,
Meta primary text and headlines, video captions and scripts, long-form stories, scroll-video scripts, hooks,
emails, landing-page copy, and copy asked for in chat. Claude researches, plans, briefs, checks rules and
facts, lays out and renders; Claude does not write or rewrite the copy itself. If a line breaks a rule, send
it back to StefanBrain in the same chat with the reason.

## How to reach StefanBrain

- **In chat (interactive sessions):** the `stefanbrain` MCP server (`.mcp.json`) gives the tools; use
  `ask_stefanbrain` with the brand's project so it works from that brand's files:
  - Comfort Wear: project `proj_59a994cdb82b45a4b43afb8ba51c357a` ("Comfortorthowear Launch")
  - DentalPULSE: project `proj_9ba354c8bfc94079b53e4c1347b0bd1e` ("Dentalpulsepro Launch")
  Long turns return a `run_id`: poll `get_job_result` (family `mcp_ask`, same project/session). Follow-ups go in
  the same chat. Send the facts StefanBrain can't see (product, offer and dates, audience/persona, placement
  and character limits, the user's requirements); don't dictate a framework, tone or sample lines.
- **In scripts and routines:** `ads/stefanbrain.py` (on the routine branches): `copy` (static batches),
  `shortform` (short-form video batches), `write --kind longform|text` (long-form stories, scroll scripts,
  anything else), `followup`, `upload`.
- The API key is a network secret on the "Sam's Default C-environment" cloud environment (locally:
  `STEFANBRAIN_API_KEY`). Never print or commit it.
- If StefanBrain is unreachable (401/403 or a run past 50 min): retry once; only then write a stopgap, label it
  "not StefanBrain copy" at the top of the deliverable, and send it to StefanBrain for a rewrite next time.

## What StefanBrain knows (and what to read before briefing it)

Each brand's StefanBrain product holds its research files; the same files live in the repo under
`ads/brands/<brand>/research/` on the routine branches:
- Comfort Wear: `avatar_personas.md` (start here: avatar + 10 personas), `customer_survey_digest.md`
  (18,521 post-purchase answers), `voc_synthesis.md` + `voc/` (Reddit, Amazon, YouTube, Trustpilot, Facebook
  ad comments: objections, competitor likes, features, benefits), ad-account digest, scripts library,
  competitors.
- DentalPULSE: feedback deep dive, customer voice, Notion brief, scripts library, competitors.
Name the persona every piece of copy is written for.

## Claims (Comfort Wear, current)

Approved: 30-day money-back guarantee, 500,000+, HSA/FSA eligible, doctor-recommended, podiatrist-recommended
(doctor and podiatrist characters allowed). Never: "orthopedic approved", cure/treatment claims, named real
doctors or invented doctor counts, extra-wide or fits-everyone promises, instant relief, shipping speed.
Unconfirmed (don't state): B-width last, EU tooling, no half sizes.
