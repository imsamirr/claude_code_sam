"""4K Kie scenes for the holiday / New Year / offer statics. Reads copy_holiday.json; renders the photo templates
(T1 hero, T4 gift tag, T5 alert, T7 text bubbles) from StefanBrain's scene line, with a camera colour per concept.
python3 holiday_render.py [ids...]   (writes holiday_colours.json for every concept)"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import render, batch2

HERE = Path(__file__).resolve().parent
CON = json.load(open(HERE / "copy_holiday.json"))["concepts"]
CYCLE = ["blossom", "sol", "pine", "chalk", "dune", "obsidian"]
COLOURS = {c["id"]: CYCLE[i % 6] for i, c in enumerate(CON)}
# a colour named in the scene (store names) wins over the cycle
NAMED = {"white": "chalk", "midnight": "obsidian", "yellow": "sol", "brown": "dune", "green forest": "pine", "pine": "pine",
         "red": "blossom", "sol": "sol"}
for c in CON:
    for name, key in NAMED.items():
        if f" {name} camera" in " " + c["scene"].lower() or f"in {name}" in c["scene"].lower():
            COLOURS[c["id"]] = key
            break
json.dump(COLOURS, open(HERE / "holiday_colours.json", "w"), indent=1)
G = batch2.GRIP
STYLE = {
    "T1": render.FLASH + " Warm, festive, mild grain.",
    "T4": "Real product photo, warm cosy window light, shallow depth of field, festive but natural.",
    "T5": render.FLASH + " Warm, festive, mild grain.",
    "T7": "Direct on-camera flash party photo, hard flash, dark falloff, warm skin, mild grain.",
}
EXTRA = {
    "T1": " Leave the top 30% of the frame calm and uncluttered for a headline.",
    "T4": (" The camera is wrapped with a satin ribbon and bow that does NOT cover the gold 'Retra' wordmark or lens,"
           " in the middle of the frame; leave the lower-right quarter calm for a gift tag. No people."),
    "T5": " Keep the main subject in the upper two thirds of the frame.",
    "T7": " Faces in the upper half; the lower 45% is calmer (clothes, background).",
}
J = {}
for c in CON:
    t = c["template"].split()[0].upper()
    if t not in STYLE:
        continue
    col = COLOURS[c["id"]]
    p = c["scene"].strip().rstrip(".") + "." + EXTRA[t]
    for name in ("White", "Midnight", "Yellow", "Brown", "Green Forest", "Red"):
        p = p.replace(f"camera in {name}", "camera").replace(f"{name} camera", "camera")
    p += f" The {render.COLOURS[col]} Retra camera is clearly visible, front facing the viewer."
    if t != "T4":
        p += G
    J[f"h_{c['id']}"] = dict(refs=[col], ar="9:16", style=STYLE[t], prompt=p)
# G2: the tag is drawn in layout, so the photo must not carry one
if "h_G2" in J:
    J["h_G2"]["prompt"] = J["h_G2"]["prompt"].replace("A wrapped gift box on dark green paper with a handwritten kraft paper tag.",
        "The Retra camera tied with a red satin ribbon, beside a small wrapped gift box and pine sprigs, on dark green"
        " paper. No gift tag, no labels, no writing.")
# concepts whose scene shows several cameras
MULTI = {"h_O5": ["blossom", "sol", "pine", "chalk", "dune", "obsidian"], "h_O6": ["dune", "pine", "sol"]}
for k, refs in MULTI.items():
    if k in J:
        J[k]["refs"] = refs
        J[k]["prompt"] = J[k]["prompt"].split(" The ")[0] + (" Several Retra cameras in different colours, each identical"
                         " in shape to its reference, fronts facing the viewer.") + (G if k == "h_O6" else "")
render.COLOURS["dune"] = "caramel brown"
render.JOBS.update(J)

if __name__ == "__main__":
    ids = [f"h_{i}" for i in sys.argv[1:]] or list(J)
    ids = [i for i in ids if i in J]
    for i in ids:
        for col in J[i]["refs"]:
            render.ref_url(col)
    with ThreadPoolExecutor(10) as ex:
        list(ex.map(render.render, ids))
