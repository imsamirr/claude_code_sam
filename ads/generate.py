"""Generate static (and optional GIF) ads for a brand with OpenAI's image model.

Default (--layout feed, user rule Oct 18): ONE size, 4:5 (1088x1360), one high-quality render per
ad, saved as <id>_vN.png. Older layouts: --layout native composes a 9:16 (1088x1920) for Stories/Reels
then re-lays it out as a 4:5; --layout extend renders 4:5 then outpaints above and below it.

Layout:
    ads/brands/<brand>/brand.json         brand, colorways, personas, language rules
    ads/brands/<brand>/reference/         product photos, one per colorway
    ads/brands/<brand>/concepts.json      concept library / backlog
    ads/brands/<brand>/weeks/<week>/concepts.json   a weekly batch
    ...and output/ next to whichever concepts.json was used.

Usage:
    python ads/generate.py --brand comfortwear --week 2026-W41          # whole weekly batch
    python ads/generate.py --brand comfortwear --week 2026-W41 W41_03   # one concept
    python ads/generate.py --brand comfortwear --week 2026-W41 --gif    # also render GIFs
    python ads/generate.py --brand comfortwear C17                      # from the library
    python ads/generate.py ... --extra "make the headline bigger"
"""

import argparse
import base64
import io
import json
import os
import re
from pathlib import Path

import requests
from dotenv import load_dotenv
from PIL import Image

ADS_DIR = Path(__file__).resolve().parent
API_URL = "https://api.openai.com/v1/images/edits"
SIZE = (1088, 1920)           # 9:16 deliverable
CONTENT = (1088, 1360)        # 4:5 safe area, centered in SIZE
TOP = (SIZE[1] - CONTENT[1]) // 2
OVERLAP = 120                 # px of the 4:5 edge the outpaint may redraw, so the scene flows across the seam
FEATHER = 40                  # only the outermost px blend into the outpaint (wider blends ghost nearby text)
FORMAT_RULE = (
    "Vertical 4:5 canvas (even if the description below says square or 9:16). Keep all text, faces, "
    "products, badges and UI cards at least 12% away from the top and bottom edges (those bands hold only "
    "background). The scene or background "
    "must run all the way to every edge: no borders, frames, white bands, solid header/footer strips or "
    "panels touching the top or bottom edge, so the image can be extended upward and downward seamlessly."
)
VERTICAL_RULE = (
    "Tall vertical 9:16 canvas (even if the description below says square or 4:5), designed for Instagram "
    "and Facebook Stories/Reels. Compose for the full height so the ad flows top to bottom with no empty, "
    "blurred or filler bands: spread the layout over the whole frame (for example headline in the upper "
    "third, the product or scene large in the middle, supporting copy or offer in the lower-middle). "
    "Background and scene run edge to edge. Keep text, faces and the product out of the top 12% and the "
    "bottom 18% of the frame (app UI covers them), but fill those areas with real scene or background, "
    "never blur or blank them."
)
FEED_RULE = (
    "Vertical 4:5 canvas for the Facebook and Instagram feed (even if the description below says square or "
    "9:16). Compose natively for 4:5 and use the full frame: headline in the upper third, the product or "
    "scene large in the middle, supporting copy or offer in the lower part. Keep at least 6% margin around "
    "all text and nothing cut off. Background and scene run edge to edge, with no blurred, empty or filler bands."
)
FEED_PROMPT = (
    "Re-lay out the first image (a 9:16 ad) as the same ad on a 4:5 vertical canvas for the Facebook and "
    "Instagram feed. Keep the identical headline and every word of copy (spelled exactly the same), the "
    "same colors, fonts, scene, people and product, but rearrange spacing and sizes so everything fits "
    "comfortably inside 4:5 with nothing cut off and nothing squeezed. Do not crop text, do not add "
    "anything new. Keep at least 6% margin around all text. The product must still match the second "
    "image exactly, at natural proportions."
)
EXTEND_PROMPT = (
    "Extend this image to a taller 9:16 frame. Fill the transparent top and bottom areas by continuing "
    "the existing scene exactly: same surfaces, walls, sky, gradients, textures, lighting, grain and "
    "perspective, so it reads as one continuous photo or illustration with no visible seam, band, "
    "line, color shift or change in sharpness where old and new meet. Objects cut off at the edge "
    "continue naturally. Do not add any text, logos, people, products or new objects."
)


def load_brand(brand):
    bdir = ADS_DIR / "brands" / brand
    return bdir, json.loads((bdir / "brand.json").read_text())


def concepts_path(bdir, week):
    return bdir / "weeks" / week / "concepts.json" if week else bdir / "concepts.json"


def learned_preferences(bdir, concept_id):
    """Turn approve/reject notes from the brand's feedback.json into prompt guidance."""
    path = bdir / "feedback.json"
    if not path.exists():
        return ""
    fb = [f for f in json.loads(path.read_text()) if f.get("notes")]
    # this concept's own feedback first, then the most recent general feedback
    fb.sort(key=lambda f: f["date"], reverse=True)
    fb.sort(key=lambda f: f["concept"] != concept_id)
    # dict.fromkeys drops repeated notes (e.g. one verdict logged on a whole batch) but keeps the order
    liked = list(dict.fromkeys(f["notes"] for f in fb if f["verdict"] == "approve"))[:8]
    disliked = list(dict.fromkeys(f["notes"] for f in fb if f["verdict"] == "reject"))[:8]
    lines = []
    if liked:
        lines.append("The creative director approved past ads for: " + "; ".join(liked) + ".")
    if disliked:
        lines.append("The creative director rejected past ads for: " + "; ".join(disliked) + ". Avoid these.")
    return " ".join(lines)


def reference_for(bdir, brand, concept):
    """Resolve the product photo: explicit reference_image, else the concept's colorway."""
    if concept.get("reference_image"):
        return bdir / concept["reference_image"]
    if concept.get("no_product") and not concept.get("colorway"):
        # text-only ads still send a product photo for brand context (the prompt says not to show it)
        return bdir / next(iter(brand["colorways"].values()))["file"]
    colorway = concept["colorway"]
    persona = brand.get("personas", {}).get(concept.get("persona"), {})
    allowed = persona.get("colorways", "any")
    allowed = allowed + persona.get("test_colorways", []) if allowed != "any" else allowed
    if allowed != "any" and colorway not in allowed:
        print(f"  note: {colorway} is outside the {concept['persona']} palette {allowed}")
    return bdir / brand["colorways"][colorway]["file"]


ILLUSTRATED = {"cartoon_3d", "comic_strip", "flat_illustration", "claymation", "retro_cartoon", "anime_soft"}
ILLUSTRATED_RULE = ("This ad is an illustration, not a photo: render the whole scene in the art style described, at "
                    "polished professional quality, with no watermarks or extra logos. Draw the product in the same style "
                    "but keep its exact shape, colors, proportions, texture pattern and wordmark so it is instantly "
                    "recognizable as the product in the reference photo. Do not give the product a face unless asked.")


BENCHMARK_RULE = (
    "The FIRST attached image is the product reference. The SECOND attached image is one of this brand's own "
    "top-performing ads: match its production quality, photo realism, product size and sharpness, typography "
    "weight and scale, and layout cleanliness. Do not copy its words, and only follow its layout as far as the "
    "description above asks."
)


UGC_RULE = ("This must look like a real, unedited phone photo or a real screenshot taken by an ordinary person, "
            "not an ad render: natural uneven daylight or indoor light, slightly imperfect framing and focus falloff, "
            "real everyday surroundings, real middle-aged and older women with natural skin, visible creases and "
            "ordinary hands, real clothing, ordinary clutter. No studio lighting, no glossy or airbrushed look, no "
            "perfect stock-photo faces, no dramatic color grading, no 3D render look. Text overlays are simple "
            "and flat like a phone editing app, handwritten notes or stickers look hand-made. The shoe stays the exact "
            "product from the reference at true proportions.")
LETTER_RULE = ("This is a text-first native ad: a plain typed letter, email, founder note or announcement, like the "
               "attached format reference. It must read as a real note, not a designed ad: plain background, simple "
               "system-style sans or serif type, left-aligned short paragraphs with blank lines between them, bold or "
               "underline only on the key phrases the description names. Render every quoted word exactly, in order, "
               "with nothing added. Body text is large for readers aged 60+: each line at least about 1/32 of the canvas "
               "height, dark text on a light background (or white on dark), generous margins, never small or light grey. "
               "If the description shows the product, it is the exact shoe from the product reference at true natural "
               "proportions, placed where the description says.")
LETTER_BENCH_RULE = ("The SECOND attached image is the FORMAT reference (another brand's ad): recreate its layout, structure, "
                     "type treatment, emphasis style and overall feel closely, but use only the words in the description. "
                     "Never show that brand's product, name, logo or signature.")
LOGO_RULE = ("The LAST attached image is the brand's own logo. Wherever the description says to show the logo, reproduce "
             "it exactly (same wordmark, letter shapes, icon and color), clean and fully legible, printed naturally on "
             "that surface; nowhere else. This overrides the no-logos rule for this logo only.")
COPY_BENCH_RULE = ("The SECOND attached image is this brand's own approved ad: reproduce it as exactly as possible (layout, "
                   "every word, type, sizes, colors, signature, stickers), changing only what the description says. "
                   "The shoe still matches the FIRST attached product reference exactly.")
UGC_BENCH_RULE = ("The SECOND attached image is a past ad of this brand: use it only as a loose reference for how big and "
                  "bold the headline and labels are; do NOT match its glossy studio look.")


def benchmark_for(bdir, brand, concept):
    """The brand ad attached as a quality/style reference: concept['benchmark'] names a key in brand.json."""
    key = concept.get("benchmark")
    if not key:
        return None
    entry = brand.get("benchmarks", {}).get(key)
    if not entry:
        print(f"  note: unknown benchmark '{key}'")
        return None
    return bdir / entry["file"]


def input_images(bdir, brand, concept, ref, ref_bytes):
    images = [(ref.name, ref_bytes)]
    bench = benchmark_for(bdir, brand, concept)
    if bench:
        images.append((f"benchmark{bench.suffix}", bench.read_bytes()))
    if concept.get("logo") and brand.get("logo_file"):
        logo = bdir / brand["logo_file"]
        images.append((f"logo{logo.suffix}", logo.read_bytes()))
    return images


def build_prompt(bdir, brand, concept, extra, layout_rule=FORMAT_RULE):
    if concept.get("format") in brand.get("banned_formats", []):
        raise SystemExit(f"{concept['id']}: format '{concept['format']}' is banned for this brand "
                         f"({brand.get('banned_style_note', 'see brand.json banned_formats')}). Rewrite the concept.")
    parts = [layout_rule, concept["prompt"]]
    if concept.get("colorway") and not concept.get("no_product"):
        template = brand.get("colorway_template", "The product is the {label} shown in the reference photo.")
        parts.append(template.format(label=brand['colorways'][concept['colorway']]['label']))
    parts.append(f"Brand styling: {brand['palette']}; {brand['font_style']}.")
    guide = brand.get("format_guides", {}).get(concept.get("format", ""))
    if guide:
        parts.append(guide)
    rules = brand["prompt_rules"]
    if concept.get("no_product"):
        # Native/lo-fi images without the product: drop the product-fidelity rule (always the first rule).
        rules = rules[1:] + ["The attached product reference photo is for brand context only: do NOT show that "
                             "product (or anything resembling it) anywhere in this image."]
    if concept.get("format") in ILLUSTRATED:
        # Cartoon/animation formats: drop the photo-quality rule, keep the product recognizable.
        rules = [r for r in rules if "photography" not in r.lower()] + [ILLUSTRATED_RULE]
    ugc = concept.get("style") == "ugc"
    letter = concept.get("style") == "letter"
    if ugc:
        rules = [r for r in rules if "photography" not in r.lower()] + [brand.get("ugc_rule", UGC_RULE)]
    if letter:
        rules = [r for r in rules if "photography" not in r.lower()] + [LETTER_RULE]
    parts += rules
    lang = concept.get("lang", "en")
    if lang != "en":
        parts.append(brand["language_rules"][lang])
    if not letter:  # the letter style replaces the shoe-hero/headline quality bar with LETTER_RULE
        parts += brand.get("quality_bar_ugc", []) if ugc and brand.get("quality_bar_ugc") else brand.get("quality_bar", [])
    if benchmark_for(bdir, brand, concept):
        # format_ref: the benchmark is another brand's ad the user supplied as a layout to recreate
        # copy_of: the benchmark is one of our own approved renders, re-made with a change (e.g. another colorway)
        parts.append(COPY_BENCH_RULE if concept.get("copy_of") else
                     LETTER_BENCH_RULE if letter or concept.get("format_ref") else UGC_BENCH_RULE if ugc else BENCHMARK_RULE)
    if concept.get("logo") and brand.get("logo_file"):
        parts.append(LOGO_RULE)
    prefs = learned_preferences(bdir, concept["id"])
    if prefs:
        parts.append(prefs)
    if extra:
        parts.append(extra)
    return "\n\n".join(parts)


# USD per 1M tokens for gpt-image-2 (text in, image in, image out); check OpenAI's pricing page
PRICES = {"text": 5.0, "image": 8.0, "output": 30.0}


def log_usage(args, kind, quality, usage):
    d = usage.get("input_tokens_details", {})
    cost = (d.get("text_tokens", 0) * PRICES["text"] + d.get("image_tokens", 0) * PRICES["image"]
            + usage.get("output_tokens", 0) * PRICES["output"]) / 1e6
    with open(args.usage_log, "a") as f:
        f.write(json.dumps({"kind": kind, "quality": quality, "cost_usd": round(cost, 4), **usage}) + "\n")


def call_api(prompt, images, args, api_key, size=CONTENT, mask=None, kind="static", quality=None):
    files = [("image[]", (name, blob, "image/png")) for name, blob in images]
    if mask:
        files.append(("mask", ("mask.png", mask, "image/png")))
    resp = requests.post(API_URL, headers={"Authorization": f"Bearer {api_key}"} if api_key else {},
                         files=files, timeout=600,
                         data={"model": args.model, "prompt": prompt, "quality": quality or args.quality,
                               "n": "1", "size": f"{size[0]}x{size[1]}"})
    if resp.status_code != 200:
        raise RuntimeError(f"{resp.status_code}: {resp.text[:500]}")
    body = resp.json()
    log_usage(args, kind, quality or args.quality, body.get("usage", {}))
    img = Image.open(io.BytesIO(base64.b64decode(body["data"][0]["b64_json"]))).convert("RGB")
    return fit(img, size)


def fit(img, size):
    """Scale to `size` without distortion: center-crop to the target aspect first.

    A plain resize between different aspect ratios squashes the product (e.g. a
    2:3 return forced into 4:5 makes the shoe look compressed).
    """
    if img.size == size:
        return img
    tw, th = size
    w, h = img.size
    if w * th > h * tw:                      # too wide: trim the sides
        nw = round(h * tw / th)
        img = img.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    elif w * th < h * tw:                    # too tall: trim top and bottom
        nh = round(w * th / tw)
        img = img.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    if img.size != size:
        print(f"  note: API returned {w}x{h}; center-cropped to {tw}:{th} instead of stretching")
    return img.resize(size, Image.LANCZOS)


def render_native(bdir, brand, concept, ref, ref_bytes, args, api_key):
    """Compose the 9:16 for its full height, then re-lay it out as the 4:5 feed version."""
    full = call_api(build_prompt(bdir, brand, concept, args.extra, VERTICAL_RULE),
                    input_images(bdir, brand, concept, ref, ref_bytes), args, api_key, size=SIZE)
    # a half-size copy of the 9:16 is enough to re-lay it out and halves the input image tokens
    small = full.resize((SIZE[0] // 2, SIZE[1] // 2), Image.LANCZOS)
    content = call_api(FEED_PROMPT, [("ad_9x16.png", png_bytes(small)), (ref.name, ref_bytes)], args, api_key,
                       size=CONTENT, kind="feed", quality=args.feed_quality)
    return content, full


def render_feed(bdir, brand, concept, ref, ref_bytes, args, api_key):
    """One 4:5 render, composed natively (user rule, Oct 18: single size, 4:5 only)."""
    return call_api(build_prompt(bdir, brand, concept, args.extra, FEED_RULE),
                    input_images(bdir, brand, concept, ref, ref_bytes), args, api_key, size=CONTENT, kind="feed")


def extend_to_9x16(content, args, api_key):
    """Outpaint the background above and below the 4:5 ad, then put the original pixels back.

    The model redraws the whole canvas, so only its top and bottom bands are kept; the 4:5
    content is pasted over them unchanged, with a short vertical feather to hide the seam.
    """
    canvas = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    canvas.paste(content.convert("RGBA"), (0, TOP))
    image = png_bytes(canvas)
    # The mask also opens OVERLAP px inside the 4:5 edges, so the model redraws across the seam.
    mask = canvas.copy()
    clear = Image.new("RGBA", (SIZE[0], OVERLAP), (0, 0, 0, 0))
    mask.paste(clear, (0, TOP))
    mask.paste(clear, (0, TOP + CONTENT[1] - OVERLAP))
    edges = call_api(EXTEND_PROMPT, [("canvas.png", image)], args, api_key, size=SIZE, mask=png_bytes(mask),
                     kind="extend", quality=args.extend_quality)
    return composite(content, edges)


def composite(content, edges):
    alpha = Image.new("L", CONTENT, 255)
    for i in range(FEATHER):
        t = (i + 1) / FEATHER
        v = int(255 * t * t * (3 - 2 * t))  # smoothstep: no visible ramp edge
        alpha.paste(v, (0, i, CONTENT[0], i + 1))
        alpha.paste(v, (0, CONTENT[1] - 1 - i, CONTENT[0], CONTENT[1] - i))
    out = edges.copy()
    out.paste(content, (0, TOP), alpha)
    return out


def png_bytes(img):
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return buf.getvalue()


def save_static(content, full, out_dir, stem):
    if full is None:                          # feed layout: the single 4:5 static is <stem>.png
        content.save(out_dir / f"{stem}.png")
        return
    full.save(out_dir / f"{stem}.png")
    content.save(out_dir / f"{stem}_4x5.png")


def render_gif(content, full, ref_bytes, concept, out_dir, stem, args, api_key):
    """Each later frame is an edit of the previous one, so layout and copy stay put.

    concept["gif"] = {"first_ms": 2200, "build": true,
                      "frames": [{"edit": "remove the third chat bubble", "ms": 900}, ...]}
    With build=true the edits strip elements from the finished static and the GIF
    plays them in reverse, so it builds up and ends (and holds) on the full ad.
    """
    gif = concept["gif"]
    feed = args.layout == "feed"
    native = args.layout in ("native", "feed")
    # feed: frames are edits of the 4:5; native: edits of the full 9:16; extend: edits of the 4:5, reusing the static's extended bands
    base, size, rule = ((content, CONTENT, FEED_RULE) if feed else (full, SIZE, VERTICAL_RULE) if native
                        else (content, CONTENT, FORMAT_RULE))
    frames, durations = [base], [gif.get("first_ms", 1400)]
    for i, step in enumerate(gif["frames"], start=2):
        print(f"  gif frame {i}/{len(gif['frames']) + 1}", flush=True)
        prompt = (
            "Edit this ad. Keep everything identical (layout, background, every word of text, the shoe, "
            f"lighting, framing) except this change: {step['edit']} "
            "The product must still match the second image exactly. " + rule
        )
        frame = call_api(prompt, [("frame.png", png_bytes(frames[-1])), ("product.png", ref_bytes)], args, api_key,
                         size=size, kind="gif", quality=args.gif_quality)
        frames.append(frame)
        (frame if native else composite(frame, full)).save(out_dir / f"{stem}_f{i}.png")
        durations.append(step.get("ms", 1400))
    if gif.get("build"):
        # frames were made by removing elements from the finished ad; play them back so it builds up
        frames, durations = frames[::-1], durations[1:][::-1] + durations[:1]
    if not native:
        frames = [composite(f, full) for f in frames]
    small = [f.resize((544, 680) if feed else (544, 960), Image.LANCZOS).quantize(colors=200, method=Image.Quantize.MEDIANCUT) for f in frames]
    small[0].save(out_dir / f"{stem}.gif", save_all=True, append_images=small[1:],
                  duration=durations, loop=0, optimize=True)
    print(f"  saved {stem}.gif ({len(frames)} frames)")


def versions(out_dir, cid):
    """Version numbers of a concept's statics (C01_v2.png -> 2), ignoring crops and GIF frames."""
    return sorted(int(m.group(1)) for q in out_dir.glob(f"{cid}_v*.png")
                  if (m := re.fullmatch(rf"{re.escape(cid)}_v(\d+)", q.stem)))


def main():
    load_dotenv()
    p = argparse.ArgumentParser()
    p.add_argument("ids", nargs="*", help="concept id prefixes, e.g. W41_03 or C01 (default: all)")
    p.add_argument("--brand", default=os.getenv("ADS_BRAND", "comfortwear"))
    p.add_argument("--week", help="weekly batch folder, e.g. 2026-W41 (default: the brand's concept library)")
    p.add_argument("--gif", action="store_true", help="also render GIFs for concepts that define them")
    p.add_argument("--gif-only", action="store_true", help="render GIFs from existing statics without regenerating them")
    p.add_argument("--quality", default=os.getenv("ADS_QUALITY", "high"), help="main render: low | medium | high (default high: a single 4:5 render per ad, user rule Oct 18)")
    p.add_argument("--layout", choices=["feed", "native", "extend"], default=os.getenv("ADS_LAYOUT", "feed"),
                   help="feed: ONE 4:5 render, composed natively (default, user rule Oct 18); native: compose the 9:16 for its full height, then re-lay out a 4:5 (default); "
                        "extend: render 4:5 and outpaint background above/below (older method)")
    p.add_argument("--feed-quality", default=None, help="native layout: the 4:5 re-layout render (default: same as --quality)")
    p.add_argument("--reextend", action="store_true", help="extend layout only: rebuild the 9:16 from the existing 4:5")
    p.add_argument("--extend-quality", default="medium", help="9:16 background extension (outside the safe area)")
    p.add_argument("--gif-quality", default="medium", help="GIF frames (shown at 544x960, 200 colors)")
    p.add_argument("--model", default=os.getenv("OPENAI_IMAGE_MODEL", "gpt-image-2"))
    p.add_argument("--extra", default="", help="extra instruction appended to every prompt")
    args = p.parse_args()
    args.feed_quality = args.feed_quality or args.quality

    # Without OPENAI_API_KEY the request goes out unauthenticated, which works
    # when the key is configured as a network secret the proxy attaches.
    api_key = os.getenv("OPENAI_API_KEY")

    bdir, brand = load_brand(args.brand)
    cpath = concepts_path(bdir, args.week)
    concepts = [c for c in json.loads(cpath.read_text())["concepts"]
                if not args.ids or any(c["id"].startswith(i) for i in args.ids)]
    out_dir = cpath.parent / "output"
    out_dir.mkdir(exist_ok=True)
    args.usage_log = out_dir / "_usage.jsonl"

    for c in concepts:
        print(f"Generating {c['id']} ...", flush=True)
        ref = reference_for(bdir, brand, c)
        ref_bytes = ref.read_bytes()
        try:
            if args.reextend:
                stem = f"{c['id']}_v{versions(out_dir, c['id'])[-1]}"
                content = Image.open(out_dir / f"{stem}_4x5.png").convert("RGB")
                extend_to_9x16(content, args, api_key).save(out_dir / f"{stem}.png")
                print(f"  re-extended {stem}.png")
                continue
            if args.gif_only:
                stem = f"{c['id']}_v{versions(out_dir, c['id'])[-1]}"
                if (out_dir / f"{stem}_4x5.png").exists():
                    content = Image.open(out_dir / f"{stem}_4x5.png").convert("RGB")
                    full = Image.open(out_dir / f"{stem}.png").convert("RGB")
                else:                         # feed layout: single 4:5 static
                    content, full = Image.open(out_dir / f"{stem}.png").convert("RGB"), None
            else:
                stem = f"{c['id']}_v{(versions(out_dir, c['id']) or [0])[-1] + 1}"
                if args.layout == "feed":
                    content, full = render_feed(bdir, brand, c, ref, ref_bytes, args, api_key), None
                elif args.layout == "native":
                    content, full = render_native(bdir, brand, c, ref, ref_bytes, args, api_key)
                else:
                    content = call_api(build_prompt(bdir, brand, c, args.extra),
                                       input_images(bdir, brand, c, ref, ref_bytes), args, api_key)
                    full = extend_to_9x16(content, args, api_key)
                save_static(content, full, out_dir, stem)
                print(f"  saved {(out_dir / stem).relative_to(ADS_DIR.parent)}.png" + ("" if full is None else " (+ _4x5)"))
            if (args.gif or args.gif_only) and c.get("gif"):
                render_gif(content, full, ref_bytes, c, out_dir, stem, args, api_key)
        except Exception as e:
            print(f"  failed: {e}")


if __name__ == "__main__":
    main()
