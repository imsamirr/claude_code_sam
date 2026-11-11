# Story images (Kie.ai): style, prompt recipe, QA

## The style (from long-form winners saved in Atria)

Almost every winning long-form static uses an **amateur phone snapshot of one moment or object from the story**:
- foamy toilet water, swollen feet on a rug, dentures on a sidewalk, a flashlight in a washer drum, a couple on a couch

**What they don't have:** studio polish, ad layout or overlaid text. The product rarely appears.

**Native ad image types that work:**
- the domestic-shame moment, which doubles as the hook (Orthora: "The Peas Were Supposed to Be Dinner.")
- photo misdirection ("Nobody punched me")
- a hand-drawn split diagram

## Tooling

**Script:** `python ads/longform_images.py --brand <brand> <IDs>`

**Model:** Kie.ai `nano-banana-pro`, called with `aspect_ratio` "3:4" and `resolution` "1K". It was chosen in a side-by-side test:
- `google/nano-banana` looked too polished.
- `seedream/4.5` added Polaroid borders and theme-park castles.

**Finish:** a 3:4 render is centre-cropped to 4:5, sized 1080×1350, and saved as a JPEG at quality 84, like a phone photo uploaded to Facebook.

**Specs** go in `<output_dir>/images/specs.json`:

```json
{"LF05_A": {"copy": "what moment this is", "prompt": "...", "size": "3:4",
            "overlay": {"type": "imessage", "time": "Today 7:42 PM",
                        "bubbles": [{"text": "Wish you were here.", "me": false},
                                    {"text": "I'm 200 feet below you. In my socks.", "me": true}]}}}
```

Use `overlay` for any text the story depends on. Never ask the model to write it, and avoid emoji in overlays (the font may not render them).

**Credits:** check the balance with `GET https://api.kie.ai/api/v1/chat/credit`.

## Prompt recipe

The script prepends the iPhone style automatically: camera roll, edge to edge, no UI, deep focus, flat HDR, noise, crooked framing, no logos. Each spec prompt adds:
1. **Who took it, from where, and when.** For example "taken by her daughter from about 10 feet away with the flash", or "from the driver's seat".
2. **The scene in concrete nouns.** Name the people (age, build, clothes matching the season), the objects, and the light.
3. **The story detail that must be right,** marked IMPORTANT. For example "her feet are only in socks; her sneakers sit empty on the pavement".
4. **Shoes or products:** "plain smooth side panels in a single solid color, no stripes, swooshes, letters or logos".
5. **Places:** "no castle, no characters, no recognizable landmarks", when relevant.

**A set of 4:** A is the hook moment. B, C and D are other moments: a failed fix, the mechanism prop or self-test, and the payoff (opening image reversed). Vary indoor and outdoor, day and night, people and objects.

## QA: failures seen and their fixes

| Failure | Fix |
|---|---|
| Fake Instagram or app UI, captions, "iPhone 13 · 3:26 AM" bar | Don't write "posted to Facebook" or "taken on an iPhone 13". The style already says "no captions, timestamps, camera labels, borders or interface". Re-render. |
| Competitor logo on shoes (N, S, swoosh) | Add the "plain smooth side panels…" line. Name a generic type ("nurse clogs", "mesh work sneakers"). |
| Car or brand emblem | "Steering wheel centre pad smooth and blank", or reframe so the wheel is mostly out of frame. A blur patch looks fake; re-render instead. |
| Cartoon character on a backpack or toy | "plain solid-pink backpack with no characters or prints". |
| Shoes still on feet that should be bare | Put the empty shoes in the foreground, or remove the person (an empty café table, kicked-off sneakers, untouched wine). |
| Open-toe socks | Avoid "compression socks"; use "thick white crew socks covering every toe". |
| Wrong season or clothing (winter coats at a spring-break park) | State the weather and clothing explicitly. |
| Narrator doesn't read as the persona (plus-size, age) | Be explicit: "clearly US size 22, round face, heavy arms". |
| Too cinematic, golden glow, bokeh | Remove "golden hour", "warm glow" and "sunset light" wording; add "ordinary light, slightly overexposed sky". |

**Always:**
- **Contact sheet:** build one with PIL and Read it before uploading.
- **Re-render:** a failure gets at most 2 retries, after which reframe the scene.
- **Report:** the number of renders.
