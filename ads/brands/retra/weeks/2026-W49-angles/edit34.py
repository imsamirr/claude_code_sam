"""34 v2: same gift-bow scene, plus a few printed candid photos on the table (Sam, 2026-11-27); ribbon off the wordmark.
python3 edit34.py  -> renders/s34b_t<n>.png (two takes)"""
import json
from concurrent.futures import ThreadPoolExecutor
import render
from render import kie, OUT

base = kie.upload(OUT / "s34_t1.png", "retra")
P = ("Edit the first image, keeping it a real, natural product photo with the same light, hands, mug, white table and"
     " olive-green Retra camera (the second image shows the exact camera). Changes: (1) move the red satin ribbon and"
     " bow so it wraps the camera's left end and does NOT cover the gold serif 'Retra' wordmark on the black top band"
     " - the full wordmark must be clearly readable; (2) add three small 4x6 photo prints with thin white borders"
     " lying casually on the table in the foreground and to the left of the camera, slightly overlapping, showing"
     " warm candid moments: friends laughing at a dinner table, a child in a snowy garden, a couple hugging on a beach."
     " Keep everything else identical. No text, captions or logos on the prints.")


def go(_):
    n = render.next_try("s34b")
    inp = {"prompt": P, "image_input": [base, render.ref_url("pine")], "aspect_ratio": "1:1", "resolution": "4K",
           "output_format": "png"}
    tid = kie.create("nano-banana-pro", inp)
    path = kie.download(kie.wait(tid)[0], OUT / f"s34b_t{n}.png")
    with open(OUT / "_usage.jsonl", "a") as f:
        f.write(json.dumps({"ad": "s34b", "try": n, "task_id": tid, "model": "nano-banana-pro", "edit_of": "s34_t1",
                            "prompt": P}) + "\n")
    print("done", path.name, flush=True)


for i in range(2):  # sequential so take numbers don't collide
    go(i)
