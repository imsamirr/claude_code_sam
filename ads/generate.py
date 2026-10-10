"""Generate static ad images from ads/concepts.json with OpenAI's image model
(the model behind ChatGPT image generation).

Each concept's product reference photo is sent with the prompt so the shoe
stays accurate. Output PNGs land in ads/output/<concept_id>_v<n>.png.

Usage:
    export OPENAI_API_KEY=sk-...
    python ads/generate.py                    # all concepts, 1 variant each
    python ads/generate.py C01 C04 -n 3       # selected concepts, 3 variants
    python ads/generate.py --size 1024x1536   # 2:3 portrait instead of square
    python ads/generate.py C03 --extra "make the headline bigger"
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

ADS_DIR = Path(__file__).resolve().parent
API_URL = "https://api.openai.com/v1/images/edits"


def learned_preferences(concept_id):
    """Turn approve/reject notes from ads/feedback.json into prompt guidance."""
    path = ADS_DIR / "feedback.json"
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


def build_prompt(spec, concept, extra):
    rules = " ".join(spec["global_prompt_rules"])
    brand = spec["brand"]
    parts = [
        concept["prompt"],
        f"Brand styling: {brand['palette']}; {brand['font_style']}.",
        rules,
    ]
    prefs = learned_preferences(concept["id"])
    if prefs:
        parts.append(prefs)
    if extra:
        parts.append(extra)
    return "\n\n".join(parts)


def generate(concept, prompt, args, api_key):
    ref = ADS_DIR / concept["reference_image"]
    with open(ref, "rb") as f:
        resp = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {api_key}"} if api_key else {},
            files=[("image[]", (ref.name, f, "image/png"))],
            data={
                "model": args.model,
                "prompt": prompt,
                "size": args.size,
                "quality": args.quality,
                "n": str(args.n),
                "input_fidelity": args.fidelity,
            },
            timeout=600,
        )
    if resp.status_code != 200:
        raise RuntimeError(f"{resp.status_code}: {resp.text[:500]}")
    return [base64.b64decode(d["b64_json"]) for d in resp.json()["data"]]


def main():
    load_dotenv()
    p = argparse.ArgumentParser()
    p.add_argument("ids", nargs="*", help="concept id prefixes, e.g. C01 C04 (default: all)")
    p.add_argument("-n", type=int, default=1, help="variants per concept")
    p.add_argument("--size", default="1024x1024", help="1024x1024 | 1024x1536 | 1536x1024")
    p.add_argument("--quality", default="high", help="low | medium | high")
    p.add_argument("--model", default=os.getenv("OPENAI_IMAGE_MODEL", "gpt-image-1"))
    p.add_argument("--fidelity", default="high", help="high | low: how closely to keep the reference shoe")
    p.add_argument("--extra", default="", help="extra instruction appended to every prompt")
    args = p.parse_args()

    # Without OPENAI_API_KEY the request goes out unauthenticated, which works
    # when the key is configured as a network secret the proxy attaches.
    api_key = os.getenv("OPENAI_API_KEY")

    spec = json.loads((ADS_DIR / "concepts.json").read_text())
    concepts = [c for c in spec["concepts"] if not args.ids or any(c["id"].startswith(i) for i in args.ids)]
    out_dir = ADS_DIR / "output"
    out_dir.mkdir(exist_ok=True)

    for c in concepts:
        print(f"Generating {c['id']} ...", flush=True)
        try:
            images = generate(c, build_prompt(spec, c, args.extra), args, api_key)
        except Exception as e:
            print(f"  failed: {e}")
            continue
        existing = len(list(out_dir.glob(f"{c['id']}_v*.png")))
        for i, img in enumerate(images, start=existing + 1):
            path = out_dir / f"{c['id']}_v{i}.png"
            path.write_bytes(img)
            print(f"  saved {path.relative_to(ADS_DIR.parent)}")


if __name__ == "__main__":
    main()
