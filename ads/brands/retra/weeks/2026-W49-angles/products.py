"""Real-looking 4K product photos on Kie (replace pasted cut-outs). python3 products.py [ids...]
Uses render.py's prompt builder (camera description + realism rules) and writes renders/<id>_t<n>.png."""
import sys
from concurrent.futures import ThreadPoolExecutor
import render

STUDIO = ("Real product photograph, not CGI: seamless {bg} paper sweep, soft large window light from the upper left,"
          " a natural soft contact shadow directly under and slightly behind the camera, true-to-life pebbled"
          " leatherette texture with tiny real-world imperfections, subtle dust-free sheen on the black parts, shot on a"
          " 90 mm lens at f/8, accurate colours.")
P = {}
for c in ["chalk", "obsidian", "sol", "dune", "pine", "blossom"]:
    P[f"p34_{c}"] = dict(refs=[c], ar="1:1", style=STUDIO.format(bg="pure white"), prompt=(
        "One Retra camera standing upright on the white surface in a three-quarter front view (turned about 20 degrees"
        " to the left), centred, filling about 60% of the frame width, the rest of the frame plain white."))
for c in ["obsidian", "chalk"]:
    P[f"pfront_{c}"] = dict(refs=[c], ar="4:3", style=STUDIO.format(bg="pure white"), prompt=(
        "One Retra camera standing upright, seen exactly straight-on from the front (lens pointing directly at the"
        " viewer, top plate edge level, no perspective tilt), centred, filling about 70% of the frame width."))
P["p07_sol_navy"] = dict(refs=["sol"], ar="9:16", style=STUDIO.format(bg="deep navy blue (#022B49)"), prompt=(
    "One mustard-yellow Retra camera standing upright in a three-quarter front view on the navy paper, placed in the"
    " lower half of the frame, filling about 75% of the frame width. The top 45% of the frame is empty navy paper."))
P["p02_dune_dark"] = dict(refs=["dune"], ar="1:1", style=STUDIO.format(bg="dark chocolate-brown"), prompt=(
    "One caramel-brown Retra camera standing upright in a three-quarter front view on the dark brown paper, centred,"
    " filling about 65% of the frame width, warm low-key light."))
P["p14_lineup_black"] = dict(refs=["chalk", "sol", "blossom", "obsidian", "dune", "pine"], ar="9:16",
    style="Real product photograph, not CGI: glossy black acrylic floor and black background, one soft spotlight from"
          " above, gentle real reflections of each camera on the glossy floor, accurate colours.", prompt=(
    "Six Retra cameras, one of each colour exactly as in the six references (off-white Chalk, mustard-yellow Sol,"
    " raspberry-pink Blossom, black Obsidian, caramel-brown Dune, olive-green Pine), standing upright, fronts facing the"
    " viewer, arranged in two neat rows of three (back row: Chalk, Sol, Blossom; front row: Obsidian, Dune, Pine), evenly"
    " spaced, all identical in shape. The group sits in the lower 60% of the frame; the top 40% is empty black."))
P["pdisp_white"] = dict(refs=[], ar="1:1", style=STUDIO.format(bg="pure white"), prompt=(
    "A generic, unbranded single-use disposable film camera in a plain kraft-paper wrap (no logos, no text) standing"
    " upright next to a small black 35 mm film canister, centred on the white surface."))
render.COLOURS["dune"] = "caramel brown"
render.JOBS.update(P)
if __name__ == "__main__":
    ids = sys.argv[1:] or list(P)
    for i in ids:
        for c in P[i]["refs"]:
            render.ref_url(c)
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(render.render, ids))
