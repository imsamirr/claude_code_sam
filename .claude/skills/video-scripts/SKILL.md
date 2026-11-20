---
name: video-scripts
description: Write Meta video ad scripts for DentalPULSE from a Notion brief (the "November Scripts"-style monthly boards, DEN### pages) or an inspiration script. StefanBrain writes every word. Claude reads the brief, gathers facts and data, briefs StefanBrain, checks claims and the house style, sends bad lines back, then pastes the script into the Notion page and sets its properties. Use for "work on this brief", "write DEN###", "adapt this inspiration script", "make hooks for…".
---

# DentalPULSE video scripts

The copy rule in CLAUDE.md applies: StefanBrain writes every spoken line, SUPER and hook. Claude never writes or rewrites copy. Paste StefanBrain's lines verbatim. If a line breaks a rule, send it back in the same chat with the reason.

## Sources to read first

- `ads/brands/dentalpulse/video_script_style.md`: the owner's house style (plain words, less technical, hook checklist). It is also on the StefanBrain product.
- `ads/brands/dentalpulse/masterclass_lessons.md`: lessons from the copywriting masterclass the owner shared (9 beats, bridges, accommodation, proof ladder, offer framing) and its checklist. Use this checklist too in step 4. Also on the StefanBrain product.
- `ads/brands/dentalpulse/brand.json`: approved claims, claims to avoid, offers.
- `ads/brands/dentalpulse/research/voc/`: survey refresh, Reddit, Amazon and YouTube voice of customer, and the 60-day Atria video performance digest.
- StefanBrain project `proj_9ba354c8bfc94079b53e4c1347b0bd1e` (product "Dentalpulsepro" holds all the files). Use the session label `dentalpulse-video-scripts`, so every script stays in one chat.

## Steps

1. **Read the brief.** Fetch the Notion page (and its properties). Most briefs are a concept title only. Look at 1–2 sibling briefs on the same board with the same angle for the team's format and current offer.
2. **Fill the facts StefanBrain can't see:**
   - appliance/persona
   - execution style (default "AI + Existing Footage" unless the brief or user says otherwise)
   - offer (currently "Black Friday" = 40% OFF the Pod at $99.95; Ultimate Cleaning Bundle $169.95; 120-day money-back guarantee; 1-year warranty)
   - the user's requirements
   - relevant data points (e.g. night guard buyers who expected set-in yellow to vanish rate about 2.8★; comparison/test formats drive our ROAS)

   Don't dictate angle, tone or sample lines. Point StefanBrain at `video_script_style.md` for voice and hooks.
3. **Format the team uses:** HOOK 1/2/3 (each with [visual direction], a short SUPER and a spoken line), then one SHARED BODY with [visual notes] for the editor. Name the persona each hook is for.
4. **Check before pasting:**
   - **Claims:** brand.json only.
     - No "free shipping", "sitewide", "medical-grade", or stock or scarcity lines.
     - No invented counts or studies, and no competitor names (unbranded only).
     - No cure or prevention claims.
     - 99.9% = "the Pod … in one 5-minute cycle". Always 5 minutes.
   - **Style:** the checklist in video_script_style.md. Plain words ("smell", not "odor"), no warm-up lines, hooks open on the appliance/person plus one concrete problem, and the three hooks differ in angle.
   - **Rule from the owner's DEN336 edits:** fewer specs. Don't stack Hz, cavitation and UV-C in one paragraph.
   - Send any failing line back to StefanBrain in the same chat with the reason, and paste only after the fixes return.
5. **Paste into Notion** with `insert_content` on the blank page, using the board format: escaped brackets `\[ \]`, escaped `\$`, `<b>` labels. Start with one italic line: "Script written by StefanBrain…" plus the offer. End with short strategy notes. Set properties: Angle, Creator Type, Offer, Execution Style, NN/IT, Status "Ready to Review". Don't touch Strategist or V-Editor unless asked.
6. **Report** to the user: the link, the hooks (one line each), the claims sent back, and any assumptions (offer, execution style) to confirm.

## Learning loop

When the owner edits a script in Notion, fetch it, diff it against what was pasted, and add the pattern to `video_script_style.md`. Then re-upload that file to the StefanBrain product: POST to /api/developers/v1/files via curl (the proxy adds auth), then `manage_products` update `files.add`, and `files.remove` the old copy.
