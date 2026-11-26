"""Render the Retra product-gallery scenes on Kie (Nano Banana Pro, 2K, 1:1), per colour.

    python3 render_gallery.py                  # everything missing
    python3 render_gallery.py hand_sol         # one job (new try)
    python3 render_gallery.py --fix hand_sol "correction"

Scenes have no text; compose_gallery.py adds StefanBrain's words.
Back/bottom views have no real-photo reference: they follow the landing page's existing Kie renders
(landing-pages/retra/gallery-src/base/back.jpg, bottom.jpg, usbc.jpg), so outputs that show them are
suffixed _RENDERED-BACK.
"""
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / "ads"))
import kie  # noqa: E402

PRODUCT = REPO / "assets/retra/product"
BASE = HERE / "base"  # landing-page base renders (back/bottom/usbc), copied from the landing-page branch
OUT = HERE / "renders"
OUT.mkdir(exist_ok=True)
COLOURS = {"chalk": "off-white (Chalk)", "obsidian": "black (Obsidian)", "sol": "mustard yellow (Sol)"}
EXTRA = {"dune": "warm tan-brown (Dune)"}  # extra colours rendered only on request
BG = "a plain warm cream seamless background (#F1ECE2)"

REAL = (" Real product photography: soft diffused daylight, gentle natural shadow, slight grain, true colours."
        " No text, captions, logos or watermarks anywhere except the gold serif 'Retra' wordmark printed on the"
        " camera exactly as in the reference. Avoid: glossy CGI, 3D render, plastic look, oversaturated, warped"
        " wordmark, extra buttons, extra fingers.")
CAM = (" The camera is exactly the product in the reference photo: black top band with the gold serif 'Retra'"
       " wordmark on the left, square viewfinder window and ribbed flash window at top right, {col} pebbled"
       " leatherette front panel, black ribbed lens ring with a small lens, black pill-shaped button right of the"
       " lens, small strap lugs on both sides. Keep shape, proportions, layout, colour and wordmark identical.")


def jobs():
    j = {}
    for c, col in {**COLOURS, **EXTRA}.items():
        j[f"hand_{c}"] = dict(refs=[PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            f"Square product photo on {BG}. A woman's right hand comes in from the right edge and holds the Retra"
            " camera from below, the camera shown straight-on from the front, centred, filling about half the frame"
            " width. Relaxed natural hand: five fingers, short natural nails, realistic skin texture; fingertips"
            " rest on the lower front of the camera without covering the lens, wordmark or viewfinder. Nothing else"
            " in frame." + CAM.format(col=col) + REAL))
        j[f"front_{c}"] = dict(refs=[PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            f"Square product photo on {BG}: the Retra camera standing upright, shown perfectly straight-on from the"
            " front (orthographic, no tilt), centred, filling about 70% of the frame width, small soft contact"
            " shadow underneath. Nothing else in frame." + CAM.format(col=col) + REAL))
        j[f"bottom_{c}"] = dict(refs=[BASE / "bottom.jpg", PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            "Recreate the first image (the same camera seen from below at the same angle, showing its bottom edge"
            " with the USB-C port, slot and small buttons) with two changes only: the leatherette front panel is"
            f" {col} exactly as in the second reference photo, and the background is {BG}. Keep the camera's shape,"
            " pose, bottom ports and buttons identical to the first image. The camera floats slightly with a soft"
            " shadow below." + REAL))
        j[f"usbc_{c}"] = dict(refs=[BASE / "usbc.jpg", PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            "Recreate the first image (top-down flat lay: the camera in the centre with a USB-C cable from its"
            " bottom edge, a laptop at the left and a phone at the right, both cabled, their screens showing a grid"
            " of travel photos) with these changes only: the camera's leatherette front panel is"
            f" {col} exactly as in the second reference photo, and the background surface is {BG}. The laptop has"
            " no logo and the keyboard keys have no readable legends; the screens show photos only, no text or app"
            " UI. Keep the layout, cables and framing." + REAL))
        j[f"gift_{c}"] = dict(refs=[BASE / "gift.jpg", PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            f"Top-down flat lay on {BG}, following the layout of the first image: at left a closed white retail gift box"
            " tied with a wide navy-blue satin ribbon and a neat bow (the ribbon is plain, with no printed words or"
            " pattern); the box lid shows only a small gold serif 'Retra' wordmark, no other printing. At right, the"
            " Retra camera from the second reference lying flat, front facing up, with a black braided wrist strap"
            " attached to its side lug and loosely looped. Leave the top 30% of the frame empty cream for a headline."
            + CAM.format(col=col) + REAL))
        j[f"box_{c}"] = dict(refs=[PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            f"Overhead three-quarter product flat lay on {BG}, unboxing layout: top right, an open-flap white retail box"
            " standing at a slight angle whose front shows only a small gold serif 'Retra' wordmark (no other printing,"
            " no icons, no text); centre, the Retra camera from the reference; left, a black braided wrist strap with"
            " a small black clip, loosely coiled; bottom left, a coiled black USB-C cable; bottom right, one small"
            " micro SD memory card with a plain black label (no readable text, no brand, no capacity). Items spaced"
            " apart with clear empty cream space around each for small labels." + CAM.format(col=col) + REAL))
        j[f"boxblank_{c}"] = dict(refs=[PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            f"Overhead three-quarter product flat lay on {BG}, unboxing layout. Top right: a closed white rectangular"
            " retail box standing upright on its long edge, its large front panel (about 1.6 times wider than tall)"
            " turned toward the viewer at a slight angle, so the whole front panel is clearly visible and large in"
            " frame (about 45% of the image width). The front panel is completely plain matte white with NO printing,"
            " text, logo or graphics at all. Centre: the Retra camera from the reference lying flat. Left: a short"
            " black braided wrist strap loop (about 15 cm) with a small black clip. Bottom left: a coiled black USB-C"
            " cable. Bottom right: one small micro SD memory card with a plain black label (no readable text). Items"
            " spaced apart with clear cream space around each." + CAM.format(col=col) + REAL))
        j[f"macro_{c}"] = dict(refs=[PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            "Extreme close-up macro product photo of the Retra camera from the reference, seen at a steep diagonal angle"
            " from the lower left: the ribbed lens ring and the small glass lens fill the lower-left half of the frame,"
            " part of the black top band with the gold serif 'Retra' wordmark and the viewfinder window visible, the"
            f" {col} leatherette texture sharp and tactile. Shallow depth of field. Plain warm cream backdrop (#F2EEE3)"
            " filling the upper-right 45% of the frame, completely empty for a headline. Soft, slightly faded film"
            " colour grade, fine grain." + CAM.format(col=col).replace(" Show the FRONT", " Show the front") + REAL))
        j[f"float_{c}"] = dict(refs=[PRODUCT / f"retra_{c}_34.jpg"], prompt=(
            "Clean studio product render-photo: the Retra camera from the reference floating in mid-air, tilted about 20"
            " degrees, three-quarter front view, centred and filling about 45% of the frame width, soft shadow far"
            " below. Background: a pale warm grey-beige seamless studio cyclorama (#E9E4D6) with faint thin grid lines"
            " that curve gently where the wall meets the floor. Generous empty space left and right of the camera for"
            " callout labels." + CAM.format(col=col) + REAL))
    j["disposable"] = dict(refs=[], prompt=(
        "Product photo on a plain warm cream backdrop (#F2EEE3): a generic single-use disposable film camera made of"
        " black plastic with a plain unprinted kraft-paper cardboard wrap, small flash window, thumb film-advance wheel"
        " on top, standing upright at a slight three-quarter angle, and next to it one plain unbranded 35mm film"
        " canister. No text, no brand names, no logos, no labels anywhere. Soft daylight, gentle shadow, slight grain."
        + REAL.replace(" except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference", "")))
    j["scene_split"] = dict(refs=[], prompt=(
        "Wide travel photo, golden hour, of a Mediterranean harbour town: pastel houses stacked up a hillside, small"
        " fishing boats moored in calm water in the foreground, a few people on the quay, low sun from the upper left"
        " with a soft flare. Ordinary modern smartphone photo: sharp, true-to-life colour, no film grain. No signs with"
        " readable text, no logos. Leave the lower-left corner slightly calmer for a caption." + REAL.replace(
            " except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference", "")))
    j["portrait"] = dict(refs=[], prompt=(
        "Candid golden-hour portrait of a woman in her late 20s in a wide-brimmed straw hat and a simple black top,"
        " looking up and away from the camera, one hand resting on the hat brim, warm low sun on her face, palm trees"
        " and green shrubs behind against a clear blue sky. Snapshot feel, slightly tilted framing, natural skin"
        " texture, flyaway hair. No text, no logos, no signs." + REAL.replace(
            " except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference", "")))
    nt = REAL.replace(" except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference", "")
    snap = " Candid 35mm-style snapshot, slightly imperfect framing, natural skin texture. No cameras or phones visible."
    j["sample_party"] = dict(refs=[], prompt=(
        "Indoor house party at night: three friends in their late 20s crowd around a turntable on a wooden sideboard,"
        " one flipping a vinyl record, the others laughing and mid-dance, string lights and plants behind, a few"
        " drinks on the sideboard. Direct on-camera flash, hard shadows on the wall, slight motion blur on the dancer."
        " No readable text, no album art, no logos." + snap + nt))
    j["sample_dj"] = dict(refs=[], prompt=(
        "Nightclub at night, seen from just in front of the DJ booth: a DJ in his late 20s with curly hair and a dark"
        " t-shirt leans over the decks, both hands on the mixer, head down and grinning; two friends dance right behind"
        " the booth, one mid-laugh with an arm up. Behind them a dark packed dance floor, haze, magenta and amber stage"
        " lights and a few light beams. Direct on-camera flash lights the DJ and the front of the booth, the background"
        " falls into darkness, slight motion blur on the dancers. DJ gear is generic and unbranded: no logos, no"
        " readable labels or screens, no neon signs, no text anywhere." + snap + nt))
    j["sample_rave"] = dict(refs=[], prompt=(
        "Underground rave in a low-ceilinged concrete basement or old warehouse at night, seen from inside the crowd:"
        " a dense crowd of silhouetted heads and shoulders from behind, a few arms raised, thick haze lit deep red,"
        " exposed pipes and a bare concrete ceiling, a row of blinding white strobe and wash lights at the far end"
        " behind a small makeshift DJ table, light beams cutting through the smoke. Grainy, high-ISO, slightly blurred,"
        " the lower half falling into near-black. No text, no signs, no logos." + snap + nt))
    j["sample_ferry"] = dict(refs=[], prompt=(
        "A young woman seen from behind on the open deck of a small ferry, leaning on the white railing, hair blowing"
        " in the wind, linen shirt, looking out at a rocky green coastline and turquoise sea, late afternoon sun, wake"
        " foam below. Horizon slightly tilted." + snap + nt))
    j["sample_sand"] = dict(refs=[], prompt=(
        "Point-of-view photo looking straight down at a person's bare feet in warm sand at the edge of a striped beach"
        " towel; on the towel a pair of sunglasses and a well-worn paperback with a plain blank cover; a little seawater"
        " foam reaching the bottom corner. Bright midday sun, crisp shadows." + snap + nt))
    j["sample_rain"] = dict(refs=[], prompt=(
        "Rainy city street at night seen from a sidewalk: people with umbrellas crossing, wet asphalt reflecting car"
        " tail lights and shop light, light streaks from a passing car, a cyclist in a raincoat. Shop windows glow but"
        " carry no readable signs, letters or logos." + snap + nt))
    j["sample_bike"] = dict(refs=[], prompt=(
        "An old city bicycle with a wicker front basket leaning against a pale pink plaster wall beside a weathered"
        " green wooden door, terracotta pots of geraniums on the cobbled pavement, soft morning light, a cat asleep on"
        " the doorstep. No signs, no house numbers, no text." + snap + nt))
    return j


JOBS = jobs()
_urls = {}
RES = os.environ.get("KIE_RES", "2K")
HQ = (" Studio product photography quality: crisp edges, accurate true-to-life colours with neutral blacks and no colour"
      " casts, even and clean pebbled leather grain with no smudges, stains or blotches, sharp gold wordmark, clean glass"
      " in the viewfinder and flash windows.") if RES == "4K" else ""


def url(p):
    p = str(p)
    if p not in _urls:
        _urls[p] = kie.upload(p, "retra-gallery")
    return _urls[p]


def next_try(name):
    n = 1
    while (OUT / f"{name}_t{n}.png").exists() or (OUT / f"{name}_t{n}.jpg").exists():
        n += 1
    return n


def render(name, fix=""):
    job = JOBS[name]
    prompt = job["prompt"] + (HQ if job["refs"] else "") + (" Correction from the last attempt: " + fix if fix else "")
    inp = {"prompt": prompt, "image_input": [url(r) for r in job["refs"]], "aspect_ratio": "1:1",
           "resolution": RES, "output_format": "png"}
    for _ in range(3):
        try:
            tid = kie.create("nano-banana-pro", inp)
            res = kie.wait(tid)
            break
        except Exception as e:  # noqa: BLE001
            print(name, "kie error", e, flush=True)
            time.sleep(5)
    else:
        return
    n = next_try(name)
    kie.download(res[0], OUT / f"{name}_t{n}.png")
    with open(OUT / "_usage.jsonl", "a") as f:
        f.write(json.dumps({"job": name, "try": n, "task_id": tid, "model": "nano-banana-pro", "resolution": RES,
                            "refs": [Path(r).name for r in job["refs"]], "fix": fix, "prompt": prompt}) + "\n")
    print("done", name, n, flush=True)


def main():
    a = sys.argv[1:]
    fix = ""
    if a[:1] == ["--fix"]:
        fix, a = a[2], [a[1]]
    names = a or [n for n in JOBS if not list(OUT.glob(f"{n}_t*"))]
    before = kie.credits()
    for n in names:
        for r in JOBS[n]["refs"]:
            url(r)
    with ThreadPoolExecutor(12) as ex:
        list(ex.map(lambda n: render(n, fix), names))
    spent = round(before - kie.credits(), 2)
    with open(OUT / "_credits.jsonl", "a") as f:
        f.write(json.dumps({"jobs": names, "fix": fix, "credits_spent": spent, "usd": round(spent * 0.005, 3)}) + "\n")
    print("credits spent", spent, flush=True)


if __name__ == "__main__":
    main()
