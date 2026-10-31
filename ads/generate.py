"""Generate static (and optional GIF) ads for a brand through the Kie.ai API (GPT Image 2).

Every ad is one 4:5 image (1088x1360) for feed placements; there is no 9:16 version.
The product reference photo is uploaded to Kie's file store, a gpt-image-2-image-to-image
task is created with aspect_ratio 4:5, and the result is polled and downloaded.

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

Key: KIE_AI (or KIE_API_KEY) in the environment or .env.
"""

import argparse
import hashlib
import io
import json
import os
import re
import time
from pathlib import Path

import requests
from dotenv import load_dotenv
from PIL import Image

ADS_DIR = Path(__file__).resolve().parent
KIE_API = "https://api.kie.ai/api/v1/jobs"
KIE_UPLOAD = "https://kieai.redpandaai.co/api/file-stream-upload"
MODEL = "gpt-image-2-image-to-image"
CONTENT = (1088, 1360)        # 4:5, the only deliverable
USD_PER_CREDIT = float(os.getenv("KIE_USD_PER_CREDIT", "0.005"))
FORMAT_RULE = (
    "Vertical 4:5 canvas (even if the description below says square or 9:16). Keep text at least "
    "4% away from the edges."
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


ILLUSTRATED = {"cartoon_3d", "comic_strip", "flat_illustration", "claymation", "retro_cartoon", "anime_soft"}
ILLUSTRATED_RULE = ("This ad is an illustration, not a photo: render the whole scene in the art style described, at "
                    "polished professional quality, with no watermarks or extra logos. Draw the product in the same style "
                    "but keep its exact shape, colors, proportions, texture pattern and wordmark so it is instantly "
                    "recognizable as the product in the reference photo. Do not give the product a face unless asked.")


def build_prompt(bdir, brand, concept, extra):
    parts = [FORMAT_RULE, concept["prompt"]]
    if concept.get("colorway"):
        template = brand.get("colorway_template", "The product is the {label} shown in the reference photo.")
        parts.append(template.format(label=brand['colorways'][concept['colorway']]['label']))
    parts.append(f"Brand styling: {brand['palette']}; {brand['font_style']}.")
    guide = brand.get("format_guides", {}).get(concept.get("format", ""))
    if guide:
        parts.append(guide)
    rules = brand["prompt_rules"]
    if concept.get("format") in ILLUSTRATED:
        # Cartoon/animation formats: drop the photo-quality rule, keep the product recognizable.
        rules = [r for r in rules if "photography" not in r.lower()] + [ILLUSTRATED_RULE]
    parts += rules
    lang = concept.get("lang", "en")
    if lang != "en":
        parts.append(brand["language_rules"][lang])
    prefs = learned_preferences(bdir, concept["id"])
    if prefs:
        parts.append(prefs)
    if extra:
        parts.append(extra)
    return "\n\n".join(parts)


def log_usage(args, kind, task):
    credits = task.get("creditsConsumed") or 0
    with open(args.usage_log, "a") as f:
        f.write(json.dumps({"kind": kind, "quality": args.resolution, "credits": credits,
                            "cost_usd": round(credits * USD_PER_CREDIT, 4), "task_id": task.get("taskId"),
                            "seconds": task.get("costTime")}) + "\n")


_uploaded = {}


def upload(name, blob, api_key):
    """Kie takes input images as URLs: upload once per run (files expire after 24h)."""
    key = hashlib.sha1(blob).hexdigest()
    if key not in _uploaded:
        r = requests.post(KIE_UPLOAD, headers={"Authorization": f"Bearer {api_key}"}, timeout=300,
                          files={"file": (f"{key[:12]}_{Path(name).stem}.png", blob, "image/png")},
                          data={"uploadPath": "ads-inputs"})
        body = r.json()
        if body.get("code") != 200:
            raise RuntimeError(f"upload failed: {body.get('msg')}")
        _uploaded[key] = body["data"]["downloadUrl"]
    return _uploaded[key]


def call_api(prompt, images, args, api_key, kind="static"):
    headers = {"Authorization": f"Bearer {api_key}"}
    urls = [upload(name, blob, api_key) for name, blob in images]
    r = requests.post(f"{KIE_API}/createTask", headers=headers, timeout=120, json={
        "model": MODEL, "input": {"prompt": prompt, "input_urls": urls,
                                  "aspect_ratio": "4:5", "resolution": args.resolution}}).json()
    if r.get("code") != 200:
        raise RuntimeError(f"createTask {r.get('code')}: {r.get('msg')}")
    task = r["data"]["taskId"]
    deadline, wait = time.time() + 900, 5
    while time.time() < deadline:
        time.sleep(wait)
        wait = min(wait + 2, 15)
        d = requests.get(f"{KIE_API}/recordInfo", headers=headers, params={"taskId": task}, timeout=60).json()["data"]
        if d["state"] == "fail":
            raise RuntimeError(f"task {task} failed: {d.get('failCode')} {d.get('failMsg')}")
        if d["state"] == "success":
            log_usage(args, kind, d)
            url = json.loads(d["resultJson"])["resultUrls"][0]
            img = Image.open(io.BytesIO(requests.get(url, timeout=120).content)).convert("RGB")
            return img if img.size == CONTENT else img.resize(CONTENT, Image.LANCZOS)
    raise RuntimeError(f"task {task} timed out")


def png_bytes(img):
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return buf.getvalue()


def render_gif(content, ref_bytes, concept, out_dir, stem, args, api_key):
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
            "Edit this ad. Keep everything identical (layout, background, every word of text, the product, "
            f"lighting, framing) except this change: {step['edit']} "
            "The product must still match the second image exactly. " + FORMAT_RULE
        )
        frame = call_api(prompt, [("frame.png", png_bytes(frames[-1])), ("product.png", ref_bytes)], args, api_key,
                         kind="gif")
        frames.append(frame)
        frame.save(out_dir / f"{stem}_f{i}.png")
        durations.append(step.get("ms", 1400))
    if gif.get("build"):
        # frames were made by removing elements from the finished ad; play them back so it builds up
        frames, durations = frames[::-1], durations[1:][::-1] + durations[:1]
    small = [f.resize((544, 680), Image.LANCZOS).quantize(colors=200, method=Image.Quantize.MEDIANCUT) for f in frames]
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
    p.add_argument("--resolution", default="1K", choices=["1K", "4K"],
                   help="Kie output resolution (2K does not support 4:5); saved at 1088x1360 either way")
    p.add_argument("--extra", default="", help="extra instruction appended to every prompt")
    args = p.parse_args()

    api_key = os.getenv("KIE_AI") or os.getenv("KIE_API_KEY")
    if not api_key:
        raise SystemExit("Set KIE_AI (or KIE_API_KEY) to your Kie.ai API key.")

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
                content = Image.open(out_dir / f"{stem}.png").convert("RGB")
                if content.size != CONTENT:  # older batches: stem.png was 9:16, the 4:5 lived in _4x5.png
                    content = Image.open(out_dir / f"{stem}_4x5.png").convert("RGB")
            else:
                stem = f"{c['id']}_v{(versions(out_dir, c['id']) or [0])[-1] + 1}"
                content = call_api(build_prompt(bdir, brand, c, args.extra), [(ref.name, ref_bytes)], args, api_key)
                content.save(out_dir / f"{stem}.png")
                print(f"  saved {(out_dir / stem).relative_to(ADS_DIR.parent)}.png")
            if (args.gif or args.gif_only) and c.get("gif"):
                render_gif(content, ref_bytes, c, out_dir, stem, args, api_key)
        except Exception as e:
            print(f"  failed: {e}")


if __name__ == "__main__":
    main()
