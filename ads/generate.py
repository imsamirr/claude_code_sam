"""Generate static (and optional GIF) ads for a brand with OpenAI's image model.

Every ad is rendered as a 4:5 image (1088x1360), then its background is
extended to a 9:16 vertical (1088x1920) and the original 4:5 pixels are put
back on top. So all text and product are guaranteed to sit in the 4:5 safe
area, the 9:16 runs in Stories/Reels, and the _4x5.png runs in feed.

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
FEATHER = 48                  # px blended where the 4:5 content meets the extended edges
FORMAT_RULE = (
    "Vertical 4:5 canvas (even if the description below says square or 9:16). Keep text at least "
    "4% away from the edges."
)
EXTEND_PROMPT = (
    "Fill only the transparent top and bottom areas by naturally continuing the image's background "
    "(same scene, colors, lighting and perspective). Do not add any text, logos, people, products "
    "or new objects there."
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
    liked = [f["notes"] for f in fb if f["verdict"] == "approve"][:8]
    disliked = [f["notes"] for f in fb if f["verdict"] == "reject"][:8]
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
    colorway = concept["colorway"]
    persona = brand.get("personas", {}).get(concept.get("persona"), {})
    allowed = persona.get("colorways", "any")
    allowed = allowed + persona.get("test_colorways", []) if allowed != "any" else allowed
    if allowed != "any" and colorway not in allowed:
        print(f"  note: {colorway} is outside the {concept['persona']} palette {allowed}")
    return bdir / brand["colorways"][colorway]["file"]


def build_prompt(bdir, brand, concept, extra):
    parts = [FORMAT_RULE, concept["prompt"]]
    if concept.get("colorway"):
        parts.append(f"The shoe is the {brand['colorways'][concept['colorway']]['label']} colorway shown in the reference photo.")
    parts.append(f"Brand styling: {brand['palette']}; {brand['font_style']}.")
    guide = brand.get("format_guides", {}).get(concept.get("format", ""))
    if guide:
        parts.append(guide)
    parts += brand["prompt_rules"]
    lang = concept.get("lang", "en")
    if lang != "en":
        parts.append(brand["language_rules"][lang])
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
    return img if img.size == size else img.resize(size, Image.LANCZOS)


def extend_to_9x16(content, args, api_key):
    """Outpaint the background above and below the 4:5 ad, then put the original pixels back.

    The model redraws the whole canvas, so only its top and bottom bands are kept; the 4:5
    content is pasted over them unchanged, with a short vertical feather to hide the seam.
    """
    canvas = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    canvas.paste(content.convert("RGBA"), (0, TOP))
    blob = png_bytes(canvas)
    edges = call_api(EXTEND_PROMPT, [("canvas.png", blob)], args, api_key, size=SIZE, mask=blob,
                     kind="extend", quality=args.extend_quality)
    return composite(content, edges)


def composite(content, edges):
    alpha = Image.new("L", CONTENT, 255)
    for i in range(FEATHER):
        v = int(255 * (i + 1) / FEATHER)
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
    frames, durations = [content], [gif.get("first_ms", 1400)]
    for i, step in enumerate(gif["frames"], start=2):
        print(f"  gif frame {i}/{len(gif['frames']) + 1}", flush=True)
        prompt = (
            "Edit this ad. Keep everything identical (layout, background, every word of text, the shoe, "
            f"lighting, framing) except this change: {step['edit']} "
            "The product must still match the second image exactly. " + FORMAT_RULE
        )
        frame = call_api(prompt, [("frame.png", png_bytes(frames[-1])), ("product.png", ref_bytes)], args, api_key,
                         kind="gif", quality=args.gif_quality)
        frames.append(frame)
        composite(frame, full).save(out_dir / f"{stem}_f{i}.png")
        durations.append(step.get("ms", 1400))
    if gif.get("build"):
        # frames were made by removing elements from the finished ad; play them back so it builds up
        frames, durations = frames[::-1], durations[1:][::-1] + durations[:1]
    # every frame reuses the static's extended top and bottom, so only the 4:5 area changes
    frames = [composite(f, full) for f in frames]
    small = [f.resize((544, 960), Image.LANCZOS).quantize(colors=200, method=Image.Quantize.MEDIANCUT) for f in frames]
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
    p.add_argument("--quality", default="medium", help="main 4:5 render: low | medium | high (high for product close-ups)")
    p.add_argument("--extend-quality", default="low", help="9:16 background extension (outside the safe area)")
    p.add_argument("--gif-quality", default="medium", help="GIF frames (shown at 544x960, 200 colors)")
    p.add_argument("--model", default=os.getenv("OPENAI_IMAGE_MODEL", "gpt-image-2"))
    p.add_argument("--extra", default="", help="extra instruction appended to every prompt")
    args = p.parse_args()

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
            if args.gif_only:
                stem = f"{c['id']}_v{versions(out_dir, c['id'])[-1]}"
                content = Image.open(out_dir / f"{stem}_4x5.png").convert("RGB")
                full = Image.open(out_dir / f"{stem}.png").convert("RGB")
            else:
                stem = f"{c['id']}_v{(versions(out_dir, c['id']) or [0])[-1] + 1}"
                content = call_api(build_prompt(bdir, brand, c, args.extra), [(ref.name, ref_bytes)], args, api_key)
                full = extend_to_9x16(content, args, api_key)
                save_static(content, full, out_dir, stem)
                print(f"  saved {(out_dir / stem).relative_to(ADS_DIR.parent)}.png (+ _4x5)")
            if (args.gif or args.gif_only) and c.get("gif"):
                render_gif(content, full, ref_bytes, c, out_dir, stem, args, api_key)
        except Exception as e:
            print(f"  failed: {e}")


if __name__ == "__main__":
    main()
