"""Render the W49 lifestyle scenes on Kie (Nano Banana Pro, 4K), reference-guided from the product shots.

    python3 render.py                 # render every job that has no file yet
    python3 render.py 03 06           # (re-)render these ad ids as a new try
    python3 render.py --fix 03 "..."  # new try with an extra correction line appended to the prompt

Scenes are rendered WITHOUT text; copy is composited later by compose.py.
Writes renders/{id}_t{n}.png and appends one line per task to renders/_usage.jsonl.
"""
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "ads"))
import kie  # noqa: E402

PRODUCT = REPO / "assets/retra/product"
OUT = HERE / "renders"
OUT.mkdir(exist_ok=True)
CREDIT_USD = 0.005  # Kie list price per credit

REAL = (
    " Photographic realism: this must read as a real, slightly imperfect photo, never as AI. {style}"
    " Deliberate imperfections: mild grain, slight motion blur on moving subjects, uneven light, off-centre framing,"
    " a stray everyday object in frame. Real people: natural skin texture with pores, flyaway hair, ordinary clothes,"
    " candid mid-movement, no model poses, no perfectly symmetrical faces. Hands must be anatomically correct with"
    " five fingers each, fully visible where they touch the camera."
    " No text, letters, captions, signs, screens with readable words, watermarks, brand logos, landmarks with logos,"
    " castles, cartoon characters or trademarks anywhere, except the gold serif 'Retra' wordmark printed on the camera"
    " exactly as in the reference."
    " Avoid: glossy CGI, plastic skin, airbrushed, oversaturated, extra fingers, warped text, fake logo,"
    " studio-perfect lighting, symmetrical face, 3D render, illustration, 8K hyperrealistic cinematic look."
)
CAM = (
    " The camera is the exact product in the reference image: a palm-sized compact camera about 11 cm wide, black"
    " top band with the gold serif 'Retra' wordmark on the left, a square viewfinder window and a ribbed flash window"
    " at top right, a {colour} pebbled leatherette front panel, a black ribbed lens ring with a small lens, a black"
    " pill-shaped button to the right of the lens, small strap lugs on both sides. Keep its shape, proportions,"
    " button layout, colours and wordmark identical to the reference. Show the FRONT of the camera (lens and"
    " wordmark side) to the viewer."
)
FLASH = "Candid 35mm-style photo shot on a compact camera with on-camera flash."
PHONE = "Casual iPhone photo in natural window light."

COLOURS = {"chalk": "off-white", "obsidian": "black", "blossom": "raspberry pink", "sol": "mustard yellow", "pine": "olive green", "dune": "caramel brown"}

JOBS = {
    "01": dict(refs=["chalk", "obsidian"], ar="4:5", style=FLASH + " Warm tones, night reception.", prompt=(
        "A wedding reception at night, guests' table in the foreground: white linen, candles, eucalyptus, half-full"
        " wine glasses. A woman guest in her late 20s in a satin dress leans across the table laughing and holds the"
        " off-white (Chalk) Retra camera up with both hands, photographing friends; front of the camera faces the viewer."
        " A black (Obsidian) Retra camera sits on the table by a place setting, front facing the viewer. Behind, out of"
        " focus, guests dancing under warm string lights. Real party mess: a crumpled napkin, a lipstick-marked glass.")),
    "03": dict(refs=["pine"], ar="9:16", style="Moody low-key photo, single warm lamp, soft shadows, mild grain.", prompt=(
        "Close-up of two relaxed hands holding the olive-green (Pine) Retra camera at chest height in a dim, calm room"
        " lit by one warm table lamp from the side; front of the camera faces the viewer and is sharp. A soft knit"
        " sleeve, a mug and a closed notebook blurred in the background. Very calm, quiet mood, deep shadows. The camera"
        " sits in the middle of the frame; the top 35% of the frame is dark, plain, out-of-focus wall for a headline, and"
        " there is dark negative space left and right of the camera for small labels.")),
    "05a": dict(refs=[], ar="3:2", style=PHONE + " Busy, slightly chaotic.", prompt=(
        "Close-up from slightly above of a traveller's black cross-body bag with its zip closed, worn at the hip, in a"
        " crowded outdoor night market: blurred shoppers, food-stall lights, motion blur. A smartphone shape is"
        " visible as a faint rectangular outline through the bag's thin fabric pocket, zipped away. No camera in the"
        " frame. No readable signs.")),
    "05b": dict(refs=["obsidian"], ar="3:2", style=FLASH + " Late-afternoon sun.", prompt=(
        "A solo traveller woman in her late 20s on a narrow old-town street with laundry lines and a scooter, raising"
        " the black (Obsidian) Retra camera to her eye to take a photo; front of the camera faces the viewer and is"
        " sharp and large in frame. A small backpack, a linen shirt. Shot from a few steps away, candid.")),
    "06": dict(refs=["sol"], ar="9:16", style=FLASH + " Bright afternoon sun, slight overexposure.", prompt=(
        "A mum in her late 30s in a generic modern amusement park, laughing, holding the mustard-yellow (Sol) Retra"
        " camera at chest height, front of the camera facing the viewer, while her son (about 7) beside her points up"
        " excitedly at a generic steel roller coaster loop in the background. Plain colourful food kiosks with no signs,"
        " a Ferris wheel far away, plain round balloons. NOT a castle, no towers, no spires, no characters, no mascots,"
        " no ears headbands, no logos, no readable signs. Faces and the camera sit in the middle third of the frame; the"
        " bottom 25% is pavement and legs, left simple for a caption bar.")),
    "12": dict(refs=["chalk"], ar="9:16", style=PHONE + " Golden hour, warm light, slight lens flare.", prompt=(
        "A honeymoon couple in their early 30s on a whitewashed terrace above a deep blue sea (Greek-island style, no"
        " landmarks, no signs). He holds the off-white (Chalk) Retra camera up at chest height toward the viewer as if"
        " photographing her; front of the camera faces the viewer. She is laughing, leaning into him, wind in her hair."
        " A straw hat on a chair, linen clothes. Candid hand-held photo by a friend. Faces and the camera sit in the"
        " middle of the frame; the top 25% is open sky.")),
    "13": dict(refs=["sol"], ar="9:16", style="Real product photo, warm soft window light, mild grain, not glossy CGI.", prompt=(
        "The mustard-yellow (Sol) Retra camera standing on a wooden kitchen table, front facing the viewer, wrapped"
        " with one oversized, glossy red satin ribbon tied in a big bow on top of the camera (the ribbon crosses the"
        " camera's top band but does NOT cover the lens or the gold 'Retra' wordmark). Behind, softly blurred, a"
        " decorated tree with warm lights and a child's mittens on the table. The camera sits in the lower-middle of"
        " the frame; the top 35% is soft, plain out-of-focus background for a headline.")),
}


def build_prompt(job, fix=""):
    p = "Using the reference product photo exactly. " if job["refs"] else ""
    p += job["prompt"]
    if job["refs"]:
        cols = ", ".join(COLOURS[c] for c in job["refs"])
        p += CAM.format(colour=cols)
    p += REAL.format(style=job["style"])
    if fix:
        p += " Correction from the last attempt: " + fix
    return p


_ref_urls = {}


def ref_url(colour):
    if colour not in _ref_urls:
        _ref_urls[colour] = kie.upload(PRODUCT / f"retra_{colour}_34.jpg", "retra")
    return _ref_urls[colour]


def next_try(ad):
    n = 1
    while (OUT / f"{ad}_t{n}.png").exists():
        n += 1
    return n


def render(ad, fix=""):
    job = JOBS[ad]
    n = next_try(ad)
    prompt = build_prompt(job, fix)
    inp = {"prompt": prompt, "image_input": [ref_url(c) for c in job["refs"]],
           "aspect_ratio": job["ar"], "resolution": "4K", "output_format": "png"}
    for attempt in range(3):  # Kie sometimes returns "Internal Error"; retry the submit, not a new try
        try:
            tid = kie.create("nano-banana-pro", inp)
            urls = kie.wait(tid)
            break
        except Exception as e:  # noqa: BLE001
            print(ad, "kie error", e, flush=True)
            time.sleep(5)
    else:
        return ad, None
    path = kie.download(urls[0], OUT / f"{ad}_t{n}.png")
    with open(OUT / "_usage.jsonl", "a") as f:
        f.write(json.dumps({"ad": ad, "try": n, "task_id": tid, "model": "nano-banana-pro", "resolution": "4K",
                            "refs": job["refs"], "fix": fix, "prompt": prompt}) + "\n")
    print("done", path.name, flush=True)
    return ad, path


def main():
    args = sys.argv[1:]
    fix = ""
    if args[:1] == ["--fix"]:
        fix = args[2]
        args = [args[1]]
    ads = args or [a for a in JOBS if not any(OUT.glob(f"{a}_t*.png"))]
    before = kie.credits()
    for ad in ads:
        for c in JOBS[ad]["refs"]:
            ref_url(c)
    with ThreadPoolExecutor(10) as ex:
        list(ex.map(lambda a: render(a, fix), ads))
    after = kie.credits()
    spent = round(before - after, 2)
    with open(OUT / "_credits.jsonl", "a") as f:
        f.write(json.dumps({"ads": ads, "fix": fix, "credits_before": before, "credits_after": after,
                            "credits_spent": spent, "usd": round(spent * CREDIT_USD, 3)}) + "\n")
    print(f"credits spent {spent} (~${spent * CREDIT_USD:.2f}) for {len(ads)} renders", flush=True)


if __name__ == "__main__":
    main()
