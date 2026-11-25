"""Render the W48 Retra scenes on Kie (Nano Banana Pro, 2K, 4:5), reference-guided from the product shots.

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

COLOURS = {"chalk": "off-white", "obsidian": "black", "blossom": "raspberry pink", "sol": "mustard yellow", "pine": "olive green"}

JOBS = {
    "01": dict(refs=["obsidian"], style=PHONE, prompt=(
        "A hand holding the Retra camera in the foreground just above a small round café table, in sharp focus, front"
        " of the camera facing the viewer. Behind it, slightly out of focus, a smartphone lies face up on the table, its"
        " screen lit with a stack of blurred notification banners (no readable words). Afternoon window light, a"
        " half-finished latte and a crumpled paper napkin on the table. Slightly off-centre framing. The top 30% of the"
        " frame is a calm, plain, light café wall with nothing in it, left empty for a headline.")),
    "02": dict(refs=["blossom"], style=FLASH, prompt=(
        "Warm evening family kitchen. Across the kitchen table, a mother in her mid-30s in a knit sweater lifts the"
        " Retra camera to her eye to photograph her two kids (about 5 and 8), front of the camera facing the viewer;"
        " half of her face is hidden behind the camera and she is smiling. In the soft foreground, the backs of the two"
        " kids' heads and shoulders, laughing, slight motion blur, the table covered in craft paper and crayons. Behind"
        " her on the counter, her phone lies face down in a fruit bowl. Real home clutter: a mug, a lunchbox. Warm"
        " evening light with a slight flash bounce, documentary feel. Keep the bottom third of the frame darker and"
        " simple (table surface) for text.")),
    "03": dict(refs=["sol"], style=FLASH + " Bright midday sun, slight overexposure.", prompt=(
        "A dad in his late 30s carries his laughing young daughter (about 5) on his shoulders along a busy, generic"
        " modern amusement-park midway: plain colourful kiosks and food stands with no signs, a generic steel roller"
        " coaster and a Ferris wheel far in the background, plain round single-colour balloons, string lights, a crowd."
        " NOT a Victorian main street, no towers, no spires, no castle, no shaped balloons, no tram tracks. The Retra camera hangs from a short black wrist strap on his wrist near the bottom of the frame,"
        " front of the camera facing the viewer. Candid snapshot taken by a family member a few steps ahead. No"
        " castles, no characters, no mascots, no ears headbands, no logos, no readable signs. The top 30% of the frame"
        " is mostly bright sky for a headline.")),
    "04": dict(refs=["chalk"], style=FLASH + " Golden hour, warm low sun, lens flare.", prompt=(
        "Two women in their late 20s walk arm in arm, laughing, down a narrow cobblestone street with pastel buildings"
        " and flower boxes (Lisbon style, no landmarks, no shop signs). The woman on the right raises the Retra camera"
        " toward the viewer mid-shot, front of the camera facing the viewer. Shot from a few steps ahead like a candid"
        " snapshot, slight motion blur. Ordinary travel clothes, a canvas tote bag. The top-left 30% of the frame is"
        " soft out-of-focus building wall and sky, left plain for a headline.")),
    "05": dict(refs=["chalk", "obsidian"], style=FLASH + " Warm tones.", prompt=(
        "A wedding reception table at night, seen from just above the table edge: white linen, candles, eucalyptus"
        " garland, half-full wine glasses, a crumpled napkin and a glass with a lipstick mark. Two Retra cameras sit at"
        " two place settings, one off-white (Chalk) and one black (Obsidian), as in the two references, fronts facing"
        " the viewer. Between them stands one small folded tent card in plain white card stock, completely blank, facing"
        " the viewer squarely, large enough to write a short line on. In the background, out of focus, guests dancing"
        " under warm string lights. The top 30% of the frame is dark, out-of-focus background for a headline.")),
    "06": dict(refs=["chalk"], style=FLASH + " High grain, purple and blue stage light, haze.", prompt=(
        "Indoor concert, seen from slightly in front of and beside a young woman (early 20s) in the crowd: behind and"
        " around her, dozens of raised glowing phone screens (no readable content) block the stage lights. She is NOT"
        " filming: she looks up toward the stage, smiling, holding the Retra camera casually at chest height with the"
        " front of the camera turned toward the viewer, lit by on-camera flash. No band, no artist, no logos, no"
        " readable screens. The top 30% of the frame is dark haze with stage light beams, left clear for a headline.")),
    "07": dict(refs=["pine"], style="Candid family photo, living-room lamp light, slight grain.", prompt=(
        "Close-up of a grandmother in her 70s with silver hair and reading glasses, smiling, holding the Retra camera in"
        " both hands in front of her chest as if she just unwrapped it, front of the camera facing the viewer, thumb"
        " resting on top of the camera. Behind her, softly blurred, a grandchild opening a gift and a Christmas tree"
        " with warm lights, wrapping paper on the floor. Natural wrinkles and skin texture. The top-left 30% of the"
        " frame is soft, plain, out-of-focus wall for a headline.")),
    "08": dict(refs=[], style=FLASH + " Golden hour.", prompt=(
        "Four friends in their 20s laughing around a picnic blanket in a city park at golden hour, a bottle of"
        " lemonade, a paper bag of cherries, a tote bag; one friend mid-laugh leaning back, another pointing off-frame."
        " Shot on a compact camera with flash, slightly off-centre, real and unposed. No cameras or phones in the"
        " scene.")),
    "09": dict(refs=["chalk", "obsidian", "blossom", "sol", "pine"],
               style="Real product photo, soft daylight, slight grain, not glossy CGI.", prompt=(
        "All five Retra cameras from the five references (off-white Chalk, black Obsidian, raspberry pink Blossom,"
        " mustard yellow Sol, olive green Pine), each identical in shape to its reference, standing upright in a slightly"
        " diagonal row on a warm cream seamless paper background (#F3EEE4) with soft natural shadows, fronts facing the"
        " viewer. The three cameras in the centre are tied together with one thin black ribbon bow. Every camera keeps"
        " its gold 'Retra' wordmark exactly as in the reference. The top 30% of the frame is empty cream background for"
        " a headline.")),
    "10": dict(refs=["chalk", "obsidian", "blossom", "sol", "pine"],
               style="Real product photo, soft daylight, mild grain, not glossy CGI.", prompt=(
        "All five Retra cameras from the five references (off-white Chalk, black Obsidian, raspberry pink Blossom,"
        " mustard yellow Sol, olive green Pine), each identical in shape to its reference, standing upright in one"
        " straight, evenly spaced horizontal row across the middle of a warm cream seamless background (#F3EEE4), fronts"
        " facing the viewer, soft natural shadows. Every camera keeps its gold 'Retra' wordmark exactly as in the"
        " reference. Leave the top 30% and the bottom 25% of the frame as empty cream background for text.")),
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
           "aspect_ratio": "4:5", "resolution": "2K", "output_format": "png"}
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
        f.write(json.dumps({"ad": ad, "try": n, "task_id": tid, "model": "nano-banana-pro", "resolution": "2K",
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
