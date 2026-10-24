"""Generate RECLAIM PDP and section images with OpenAI's image model, in Blume SuperBelly's style.

Usage: python landing/reclaim/generate_images.py [name ...]   (no names = all missing images)
Needs OPENAI_API_KEY. Writes landing/reclaim/img/<name>.webp.
"""
import base64, io, os, sys, json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE / "img"
API = "https://api.openai.com/v1/images/edits"

STYLE = ("Premium DTC wellness e-commerce photography in the exact style of Blume SuperBelly product page images: "
         "bright seamless colored studio backdrop, crisp soft daylight with gentle shadows, saturated juicy colors, "
         "fresh real fruit props, clear glasses of vivid pink drink with big ice cubes. Any on-image text is set in a bold "
         "rounded geometric sans-serif (like Poppins Bold) or an elegant high-contrast serif for accents, colored deep plum #5C1C4F "
         "unless stated, perfectly spelled, generous margins. No watermarks, no extra brand names, no logos other than the product's own.")
PACK = ("The product is the RECLAIM pouch in the reference photo: a hot magenta-to-red stand-up pouch with the white "
        "lowercase wordmark 'reclaim', 'Cortisol Balance + Hydration', 'Dragonfruit Lemonade'. Reproduce the pouch exactly "
        "(shape, colors, wordmark, layout). Single-serve sachet sticks are slim magenta-to-red sticks with the white "
        "wordmark 'reclaim' printed vertically.")
LIFE = ("Editorial lifestyle photograph, natural candid moment, real skin texture, warm natural light, shot on 35mm, "
        "shallow depth of field, color palette of blush pink, cream, plum and warm sunlight. No on-image text.")

IMAGES = {
 # ---- PDP gallery, 1:1 ----
 "pdp-1-hero": ("1024x1024", "high", True,
   "Square product hero. Soft blush-pink seamless backdrop. Center: the RECLAIM pouch standing upright, slightly angled, "
   "with two sachet sticks leaning against it, a clear tumbler of pink dragonfruit lemonade with ice and a lemon wheel to "
   "the right, a frosted translucent pink shaker bottle behind on the left, a halved dragonfruit (white flesh, black seeds) "
   "and lemon halves in front. Top-left: a white rounded pill-shaped badge with a small pink shaker icon and the text "
   "'FREE' (large, bold) then 'Shaker Cup' then 'with Subscription' (small, magenta)."),
 "pdp-2-what-is-it": ("1024x1024", "high", True,
   "Square infographic. Background split vertically: left half pale lilac #F2DCEA, right half soft pink #F8C6D8. "
   "Center: a hand tipping a RECLAIM sachet stick, pink powder streaming into a tall clear glass of vivid pink drink with ice, "
   "strawberries-free; a dragonfruit half and lemon slice at the base. Left column text: headline 'Daily Calm' then small lines "
   "'Stress Support', 'L-Theanine', 'Magnesium'. Right column text: headline '+ Hydration' then small lines 'Electrolytes', "
   "'No Sugar', 'Dragonfruit Lemonade'. A small plum circle badge near the glass reading 'Mix with Water' in white."),
 "pdp-3-inside": ("1024x1024", "high", True,
   "Square ingredient callout infographic on a butter-yellow #FBE3A0 background. Headline at top: 'Calm + Hydration in Every Stick'. "
   "Center: one large vertical RECLAIM sachet stick. Thin plum callout lines connect to four small circular photo icons with labels: "
   "top-left 'L-Theanine' (green tea leaves icon) with small caption 'From green tea'; bottom-left 'Magnesium' (pink mineral crystals icon) "
   "with caption 'The calming mineral'; top-right 'Electrolytes' (water droplet icon) with caption 'For daily hydration'; bottom-right "
   "'Dragonfruit + Lemon' (fruit icon) with caption 'Bright, tropical taste'. Small footer text: 'Every amount listed on the label'."),
 "pdp-4-flavor": ("1024x1024", "high", True,
   "Square flavor shot on a soft lilac #E9D2F0 backdrop. Two clear glasses of vivid pink dragonfruit lemonade with ice, one with a curly "
   "pink straw, one with a lemon wheel; halved dragonfruit, lemons and three RECLAIM sachet sticks scattered at the base, hard sunlight shadows. "
   "Headline at the top: 'Dragonfruit Lemonade'. A white rounded label pill near the glass reading 'Bright lemon · Delicate dragonfruit'."),
 "pdp-5-made-for-her": ("1024x1024", "high", False,
   "Square infographic on butter-yellow #FBE3A0. Left side headline 'Made for Her Day' in plum. Below it, four horizontal rounded pill "
   "bars with plum outline, filled mostly with lime green #E4EB9C, each containing bold plum text: 'Stress support', 'Hydration support', "
   "'No sugar', 'Every dose listed'. Right side: a handheld milk frother whisking vivid pink drink inside a tall clear glass, splash. "
   "No percentages or numbers anywhere."),
 "pdp-6-bonus": ("1024x1024", "high", False,
   "Square promo graphic with a hot pink to coral red gradient background. Headline in white elegant italic serif: 'Your Subscriber Bonus'. "
   "Subline in white sans: 'Start a RECLAIM subscription & you'll get:'. Below, two pale pink arch-shaped frames side by side: left frame "
   "holds a frosted translucent pink shaker bottle with the word 'reclaim' on it; right frame holds a phone showing a simple subscription "
   "screen with 'Skip', 'Pause', 'Cancel' buttons. Captions under the arches in white: 'FREE Shaker Cup' and 'Skip, pause or cancel online'."),
 "pdp-7-compare": ("1024x1024", "high", False,
   "Square comparison chart on a warm orange-to-amber gradient background. Headline in white: small sans 'Combining' then large serif "
   "'Calm & Hydration'. Below, a cream rounded table with 3 data columns: first column highlighted butter-yellow headed by the magenta "
   "wordmark 'reclaim', second 'Leading Electrolyte Drink', third 'Leading Calm Capsule'. Rows (labels in left column): 'L-Theanine' "
   "(check, cross, check), 'Magnesium' (check, cross, check), 'Electrolytes' (check, check, cross), 'Tastes like a treat' (check, check, cross), "
   "'Made for' ('Her stress + hydration', 'Hydration', 'Stress'). Plum checkmarks and crosses."),
 "pdp-8-on-the-go": ("1024x1024", "high", True,
   "Square lifestyle-meets-graphic image. Bright outdoor scene with blue sky and soft clouds. A woman in her mid-40s in a sunny yellow "
   "fleece holds a clear water bottle filled with pink drink and pours a RECLAIM sachet stick into it, smiling. Large headline on the left "
   "sky in plum: 'Daily Calm' then 'On the go', and smaller 'Just add water. 30 sachets in each pouch.'"),
 "pdp-9-badges": ("1024x1024", "high", False,
   "Square brand-facts graphic on a hot magenta-pink #E0177A background. White thin-line icons arranged in a 3x2 grid with white "
   "labels under each: a big number '30' with label 'Servings'; crossed sugar cubes 'No Sugar'; lotus flower 'With L-Theanine'; "
   "mineral crystal 'With Magnesium'; check shield 'Third-Party Tested'; shaker bottle 'Just Add Water'. Clean, symmetrical, lots of space."),
 # ---- page sections ----
 "sec-modern-life": ("1024x1024", "high", False, LIFE +
   " A woman in her late 40s with shoulder-length dark hair, cream linen shirt, standing by a sunlit kitchen window, eyes closed, "
   "sipping a glass of vivid pink drink with ice, a moment of quiet. Soft hazy sky outside."),
 "sec-ing-theanine": ("1536x1024", "medium", False,
   "Abstract macro background for a website banner, no text, no product: fresh green tea leaves with dew drops, washed in soft pink and "
   "magenta light, dreamy bokeh, the left half darker and calmer for overlaid white text."),
 "sec-ing-magnesium": ("1536x1024", "medium", False,
   "Abstract macro background for a website banner, no text, no product: glowing pale pink and lilac mineral crystals and fine powder, "
   "soft plum shadows, dreamy, the left half darker and calmer for overlaid white text."),
 "sec-ing-electrolytes": ("1536x1024", "medium", False,
   "Abstract macro background for a website banner, no text, no product: vivid pink water splash with droplets frozen mid-air against a "
   "soft blue sky, the left half calmer for overlaid white text."),
 "sec-ing-dragonfruit": ("1536x1024", "medium", False,
   "Abstract macro background for a website banner, no text, no product: halved dragonfruit with magenta skin and white seeded flesh next "
   "to sliced lemons, overhead on a soft coral surface, juicy, the left half less busy for overlaid white text."),
 "sec-benefits": ("1024x1024", "high", True,
   "Two women's hands raising and clinking clear glasses of vivid pink drink with big ice cubes against a bright blue sky with fluffy white "
   "clouds, pink liquid splashing upward; one hand also holds a RECLAIM sachet stick. Photographic, playful, saturated. No text."),
 "sec-meet": ("1536x1024", "high", True,
   "Wide styled tabletop scene on a blush-pink set: several RECLAIM pouches, sachet sticks, a frosted pink shaker bottle, clear glasses and a "
   "coupe of pink dragonfruit lemonade with ice, dragonfruit halves and lemons, hard sunlight shadows. Leave the center calm (it will be "
   "covered by a translucent overlay and text). No text."),
 "sec-season-work": ("1024x1024", "medium", False, LIFE +
   " A woman around 48 at a home desk in late afternoon, laptop open, rubbing her temple then pausing with a glass of pink drink with ice, "
   "sticky notes on the monitor."),
 "sec-season-mom": ("1024x1024", "medium", False, LIFE +
   " A mother around 38 in a busy morning kitchen, lunchboxes and a child's backpack on the counter, taking a calm sip of a pink drink "
   "with ice, a small smile."),
 "sec-season-evening": ("1024x1024", "medium", False, LIFE +
   " A woman around 52 curled on a sofa in the early evening, warm lamp light, phone face down, holding a glass of pink drink with ice, "
   "relaxed."),
 "sec-shaker": ("1024x1024", "medium", True,
   "A woman's hand holding a frosted translucent pink shaker bottle with a lilac lid, filled with vivid pink drink, the word 'reclaim' "
   "printed vertically on the bottle in plum, on a plain soft lilac #F2DCEA background."),
}


def ref_png():
    im = Image.open(HERE / "reclaim-pouch.webp").convert("RGB")
    b = io.BytesIO(); im.save(b, "PNG"); return b.getvalue()


def gen(name):
    size, quality, with_pack, desc = IMAGES[name]
    prompt = "\n\n".join([STYLE, PACK if with_pack else "Do not show any product packaging.", desc])
    files = [("image[]", ("ref.png", REF, "image/png"))]
    r = requests.post(API, headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"}, files=files, timeout=900,
                      data={"model": "gpt-image-2", "prompt": prompt, "quality": quality, "n": "1", "size": size})
    if r.status_code != 200:
        return name, f"ERROR {r.status_code}: {r.text[:300]}"
    img = Image.open(io.BytesIO(base64.b64decode(r.json()["data"][0]["b64_json"]))).convert("RGB")
    img.save(OUT / f"{name}.webp", quality=86)
    return name, f"ok {img.size}"


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    REF = ref_png()
    names = sys.argv[1:] or [n for n in IMAGES if not (OUT / f"{n}.webp").exists()]
    with ThreadPoolExecutor(6) as ex:
        for name, status in ex.map(gen, names):
            print(name, status, flush=True)
