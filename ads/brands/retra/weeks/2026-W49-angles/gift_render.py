"""4K Kie shots for the bundle gifts (Sam 2026-11-27: B2G1 + free woven strap, B3G2 + strap + leather bag).
Strap reference: the store's product photo (assets/retra/product/gifts/gift_strap.jpg). The store's bag photo 502s on
the CDN, so the bag is rendered from a description.  python3 gift_render.py [ids...]"""
import sys
from concurrent.futures import ThreadPoolExecutor
import render, batch2
from render import kie, REPO

WHITE = batch2.WHITE
STRAP = ("a cream woven cotton camera wrist strap with tan leather end tabs and a small silver clip, exactly as in the"
         " strap reference photo")
BAG = ("a compact tan-brown leather camera case shaped to the camera, with a fold-over flap, fine stitching and a small"
       " press stud, no logo")
SIX = ["blossom", "sol", "pine", "chalk", "dune"]
FEST = ("Real overhead photo on a deep red linen party table with scattered gold sequin confetti and warm string-light"
        " bokeh at the edges, soft festive light, natural shadows.")
J = {
    "gift_strap": dict(refs=[], ar="1:1", style=WHITE, prompt=(
        f"Product photo: {STRAP}, loosely coiled, alone on pure white, centred, nothing else in frame.")),
    "gift_bag": dict(refs=[], ar="1:1", style=WHITE, prompt=(
        f"Studio product photo: {BAG}, brand new and spotless, closed, standing upright, three-quarter view, alone on a"
        " seamless pure white sweep, centred. No hands, no people, no other objects, no wear or scratches.")),
    "flat_b2g1": dict(refs=["blossom", "sol", "pine"], ar="4:5", style=FEST, prompt=(
        "Top-down flat lay: three Retra cameras (raspberry pink, mustard yellow, olive green) lying face up in a"
        f" relaxed diagonal row across the middle of the frame, and {STRAP} coiled beside them on the right. Generous"
        " space between items; top 25% of the frame is plain table.")),
    "flat_b3g2": dict(refs=SIX, ar="4:5", style=FEST, prompt=(
        "Top-down flat lay: five Retra cameras (raspberry pink, mustard yellow, olive green, off-white, caramel brown)"
        f" lying face up in two neat rows in the middle of the frame, with {STRAP} coiled and {BAG} beside them at the"
        " lower right. The same red linen table and confetti continue evenly to every edge of the frame (one continuous"
        " surface, no plain band or seam); keep the upper quarter sparse so text can sit there.")),
}
orig = render.build_prompt


def bp(job, fix=""):
    p = orig(job, fix)
    if not job["refs"]:
        p = p.replace(", except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference.",
                      ". No cameras, brand names, wordmarks, logos or lettering anywhere.")
    return p


render.build_prompt = bp
render.COLOURS["dune"] = "caramel brown"
render.JOBS.update(J)
_strap = None


def strap_url():
    global _strap
    if _strap is None:
        _strap = kie.upload(REPO / "assets/retra/product/gifts/gift_strap.jpg", "retra")
    return _strap


STRAP_JOBS = {"gift_strap", "flat_b2g1", "flat_b3g2"}


def run(k, n=1):
    import json
    job = render.JOBS[k]
    prompt = render.build_prompt(job)
    imgs = [render.ref_url(c) for c in job["refs"]] + ([strap_url()] if k in STRAP_JOBS else [])
    if k in STRAP_JOBS:
        prompt += " The last reference image shows the strap only (ignore its camera and background)."
    inp = {"prompt": prompt, "image_input": imgs, "aspect_ratio": job["ar"], "resolution": "4K", "output_format": "png"}
    tid = kie.create("nano-banana-pro", inp)
    path = kie.download(kie.wait(tid)[0], render.OUT / f"{k}_t{n}.png")
    with open(render.OUT / "_usage.jsonl", "a") as f:
        f.write(json.dumps({"ad": k, "try": n, "task_id": tid, "model": "nano-banana-pro", "prompt": prompt}) + "\n")
    print("done", path.name, flush=True)


if __name__ == "__main__":
    ids = sys.argv[1:] or list(J)
    strap_url()
    for i in ids:
        for c in J[i]["refs"]:
            render.ref_url(c)
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(lambda k: run(k, render.next_try(k)), ids))
