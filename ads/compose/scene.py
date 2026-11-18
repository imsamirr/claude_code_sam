"""Generate a TEXT-FREE photo scene with Kie (gpt-image-2) for a composed ad; layout and text are added in HTML.
usage: python ads/compose/scene.py <out.png> "<scene prompt>" [reference.png ...]"""
import sys, types
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate  # noqa: E402

NO_TEXT = (" Photorealistic, natural light, real camera photo. Absolutely NO text, letters, numbers, logos, "
           "signs, watermarks or UI anywhere in the image. Leave the described empty areas clean for a designer to "
           "add text later. Any shoe shown is EXACTLY the product in the reference photo at true proportions.")

if __name__ == "__main__":
    out, prompt, refs = sys.argv[1], sys.argv[2], sys.argv[3:]
    args = types.SimpleNamespace(kie_resolution="2K", usage_log=str(Path(out).parent / "_usage.jsonl"))
    images = [(Path(r).name, Path(r).read_bytes()) for r in refs]
    generate.call_kie(prompt + NO_TEXT, images, args, (1080, 1350), "scene").save(out)
    print("saved", out)
