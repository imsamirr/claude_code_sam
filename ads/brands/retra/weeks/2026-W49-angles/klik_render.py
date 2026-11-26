"""4K Kie scenes for the KLIK-inspired statics (60-67). python3 klik_render.py [ids...]"""
import sys
from concurrent.futures import ThreadPoolExecutor
import render, batch2
SIX = ["chalk", "sol", "blossom", "obsidian", "dune", "pine"]
NAMES6 = ("off-white Chalk, mustard-yellow Sol, raspberry-pink Blossom, black Obsidian, caramel-brown Dune, olive-green Pine,"
          " each identical in shape to its reference")
WHITE = batch2.WHITE
G = batch2.GRIP
J = {
    "k60": dict(refs=SIX, ar="9:16", style=WHITE, prompt=(
        "Six Retra cameras (" + NAMES6 + ") standing upright in a diagonal stair-step line running from the upper-left"
        " to the lower-right of the frame, each slightly lower and further right than the last, all angled the same way,"
        " fronts facing the viewer, on pure white. Top-right and bottom-left corners are empty white.")),
    "k61": dict(refs=["pine"], ar="4:5", style="Real top-down product photo, soft daylight, mild grain.", prompt=(
        "Directly from above on deep olive-green paper: the olive-green Retra camera lying face up inside an open plain"
        " olive-green gift box, beside it a coiled black USB-C cable, a small microSD memory card and the lid with a"
        " wide olive satin ribbon tied in a bow. Elegant, tonal, minimal. Bottom-left 25% is plain paper.")),
    "k62": dict(refs=["chalk", "sol", "blossom"], ar="4:5", style=WHITE, prompt=(
        "Two hands hold a neat stack of three Retra cameras (off-white Chalk on top, mustard Sol in the middle, raspberry"
        " Blossom at the bottom), fronts facing the viewer, one hand on top of the stack and one underneath, entering"
        " from the right; the stack sits in the right 60% of the frame on pure white; the left 40% is empty white."
        " Fingers only on the cameras' top and bottom edges; five natural fingers per hand.")),
    "k63": dict(refs=SIX, ar="9:16", style=WHITE, prompt=(
        "Two hands hold a tall, perfectly vertical tower of six stacked Retra cameras (" + NAMES6 + "), one hand on top"
        " and one underneath, fronts facing the viewer, the tower in the right half of the frame from top to bottom, on"
        " pure white. Left half empty white. Fingers only on the top and bottom cameras' edges; five natural fingers.")),
    "k64": dict(refs=["dune"], ar="4:5", style=WHITE, prompt=(
        "A hand holds the caramel-brown Retra camera out toward the viewer from the lower right, front facing the"
        " viewer, camera in the lower-middle of the frame on pure white. Top 40% empty white." + G)),
    "k66": dict(refs=SIX, ar="9:16", style="Real product photo on soft blush-pink paper, soft daylight, natural shadows.",
        prompt=("A neat stack of six Retra cameras (" + NAMES6 + ") in two columns of three, fronts facing the viewer,"
        " tied together with one wide black satin ribbon and a big black bow on top, on blush-pink paper, in the lower"
        " half of the frame. Top 45% plain pink.")),
    "k67": dict(refs=["sol"], ar="4:5", style=WHITE, prompt=(
        "The mustard-yellow Retra camera standing upright on white, front facing the viewer, in the lower half of the"
        " frame; a small cute generic Santa Claus figurine (classic red suit, white beard, no brand) peeks over the top"
        " of the camera from behind, hands resting on the top plate, not covering the wordmark or lens. Top 40% white.")),
}
render.COLOURS["dune"] = "caramel brown"
render.JOBS.update(J)
if __name__ == "__main__":
    ids = sys.argv[1:] or list(J)
    for i in ids:
        for c in J[i]["refs"]:
            render.ref_url(c)
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(render.render, ids))
