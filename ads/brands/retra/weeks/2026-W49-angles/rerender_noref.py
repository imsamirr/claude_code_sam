"""Re-render no-camera scenes without the wordmark allowance in render.REAL."""
import sys
from concurrent.futures import ThreadPoolExecutor
import render, batch2
orig = render.build_prompt
def bp(job, fix=""):
    p = orig(job, fix)
    if not job["refs"]:
        p = p.replace(", except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference.",
                      ". No brand names, wordmarks, logos or lettering anywhere, including on phones and cameras.")
    return p
render.build_prompt = bp
extra = {"s32": " No people, no hands, no phones, no other objects in front of the board.",
         "s36": " No hands or people.", "s42a": " The phone is plain with no logo or text.",
         "s30a": " Plain phone with no logo or text."}
for k, v in extra.items():
    batch2.J[k]["prompt"] += v
render.JOBS.update(batch2.J)
ids = sys.argv[1:]
with ThreadPoolExecutor(6) as ex:
    list(ex.map(render.render, ids))
