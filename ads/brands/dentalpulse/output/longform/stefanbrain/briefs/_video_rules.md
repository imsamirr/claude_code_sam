## Format: scrolling long-form video (Mode A), the writer spec's limits
A vertical 9:16 video, about 4–5 minutes. One calm still photo of the narrator's world sits in the background; the whole story scrolls up from the bottom as big bold white text with a black outline. Most videos are MUSIC ONLY (the text alone has to hold the reader); the one marked VOICE also gets a voice-over reading the text word for word.
- Length: 620–720 words per script (count them). Paragraphs of 1–3 short sentences, at most 35 words each, a blank line between paragraphs.
- No emojis, symbols (%, $, #, &) or hashtags in the script. Numbers as people say them ("ninety-nine ninety-five", "forty-two thousand times a second", "ninety-nine point nine percent" spelled as words, "in 2015" is fine).
- The first 2–3 paragraphs are on screen at second 0 and must stop the scroll; open a loop the story only closes near the end. MUSIC-ONLY scripts: shorter paragraphs, more one-line punches and cliffhangers. VOICE script: written for the ear, natural spoken rhythm.
- The story runs: hook, "let me back up" + identity, failed fixes with prices (soak, brush, tablets, the cheap pod), rock bottom, a messenger from the narrator's world giving the mechanism in plain words with one household analogy, a free self-test, a 3–5 point criteria list, DentalPULSE named about 55–65% of the way through, the first cycle (cloudy, brown water), results with each loss paid off, a payoff that reverses the opening image, then the close.
- Close, in this order: one line restating the enemy; "The DentalPULSE Pod. Ultrasonic cleaning and medical-grade UV-C light. Tap water. Five minutes. It eliminates 99.9% of bacteria." (you may spell the number out); "Right now it's 40% off, ninety-nine ninety-five, with a free travel bag and a free dental case."; "Try it for 120 days. If you don't see the difference, send it back for your money back."; "Tap below to see it." Evergreen: no deadline words.
- The 3 stories in this angle are different stories: different narrator (age, job, gender mix), town, season, family situation, hook type.

## What to return (JSON schema fields, one concept per DV id)
- id: DV<nn>
- primary_text: the FULL on-screen scroll script (620–720 words, rules above)
- headline: short Meta headline
- cta: "Learn More"
- alternate_hooks: 3 alternative opening paragraph(s) for the script
- scroll_script: the 1–3 sentence Facebook caption (hook + curiosity) for this video
- persona: the persona plus narrator name, age, job, town
- why: the hook type, open-loop type, lead type, and the word count of primary_text
