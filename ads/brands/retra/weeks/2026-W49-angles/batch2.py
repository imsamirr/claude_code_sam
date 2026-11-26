"""Scenes for the W49 batch-2 statics (ids 20-59). python3 batch2.py [ids...]"""
import sys
from concurrent.futures import ThreadPoolExecutor
import render

GRIP = (" Hold the camera the way a photographer really does: hands only on the camera's two short ends and underside,"
        " thumbs on the back, the right index finger on the small shutter button on the top plate; no finger covers the"
        " lens, lens ring, flash window, viewfinder window or gold Retra wordmark. Exactly five natural fingers per hand.")
FLASH, PHONE = render.FLASH, render.PHONE
WHITE = ("Real product photograph, not CGI: seamless pure white paper sweep, soft window light from the upper left,"
         " natural soft contact shadows, true-to-life textures, accurate colours.")
J = {
    "s20": dict(refs=["blossom"], ar="9:16", style="Real photo, bright even daylight, mild grain.", prompt=(
        "A hand holds the raspberry-pink Retra camera out toward the viewer against a seamless bold coral-pink paper"
        " backdrop, front of the camera facing the viewer, camera in the lower-middle of the frame. Top 40% is plain"
        " backdrop." + GRIP)),
    "s23": dict(refs=["chalk"], ar="9:16", style=FLASH + " Warm evening lamp light.", prompt=(
        "A candid family moment on a living-room sofa: a dad in his late 30s and two kids (about 6 and 9) laughing and"
        " tumbling over each other; the off-white Retra camera sits on the coffee table in the foreground, front facing"
        " the viewer. Real home clutter. The top 30% of the frame is a calm, plain wall for a headline.")),
    "s24": dict(refs=["chalk"], ar="1:1", style=WHITE, prompt=(
        "Top-down knolling flat lay on white, evenly spaced in a neat grid: the off-white Retra camera (front facing up),"
        " a coiled white USB-C cable, a black woven wrist strap, one small microSD memory card, and a plain white gift"
        " box with its lid set beside it. No text or logos except the camera's own wordmark.")),
    "s25": dict(refs=["sol"], ar="9:16", style="Real product photo, bright studio light, crisp, slight motion blur.", prompt=(
        "The mustard-yellow Retra camera caught mid-air at a playful tilt, falling toward a soft butter-yellow paper"
        " floor with its shadow below, front facing the viewer, in the lower-middle of the frame. Top 40% plain"
        " butter-yellow backdrop.")),
    "s26": dict(refs=["obsidian"], ar="9:16", style=PHONE + " Bright midday sun.", prompt=(
        "Low angle: a traveller's hand holds the black Retra camera up high against a clear deep-blue sky, front facing"
        " the viewer, old terracotta rooftops just visible at the bottom edge. Camera in the middle of the frame with"
        " open sky all around it." + GRIP)),
    "s29": dict(refs=["obsidian"], ar="9:16", style="Moody low-key studio photo, drifting smoke, warm rim light, grain.",
        prompt=("The black Retra camera standing on a dark surface surrounded by drifting smoke, warm rim light on its"
        " edges, front facing the viewer, in the lower half of the frame. Top 45% dark smoky haze.")),
    "s30a": dict(refs=[], ar="2:3", style=PHONE + " Golden hour.", prompt=(
        "A young woman at a scenic coastal viewpoint at sunset looks down at her phone, its screen glowing (no readable"
        " content), ignoring the view behind her; slightly bored expression. Candid.")),
    "s30b": dict(refs=["dune"], ar="2:3", style=FLASH + " Golden hour.", prompt=(
        "The same kind of young woman at a scenic coastal viewpoint at sunset, laughing, raising the caramel-brown Retra"
        " camera to photograph the view, front of the camera facing the viewer." + GRIP)),
    "s31": dict(refs=["sol"], ar="1:1", style=WHITE, prompt=(
        "The mustard-yellow Retra camera standing upright on white, wearing a tiny black graduation mortarboard cap with"
        " a gold tassel perched on its top plate (the cap does not cover the wordmark or lens), three-quarter view.")),
    "s32": dict(refs=[], ar="9:16", style=PHONE, prompt=(
        "An empty clean office whiteboard on a wall, photographed straight-on, filling the frame, with a marker tray at"
        " the bottom holding two black markers and an eraser. The board is completely blank, slight reflections.")),
    "s33": dict(refs=[], ar="16:9", style="Minimal black continuous-line illustration on pure white, no text.", prompt=(
        "Three separate small line drawings side by side of the same young woman: left, hunched over looking at a"
        " phone; middle, holding a small compact camera up to her eye; right, laughing with two friends. Simple,"
        " elegant single-weight black lines, lots of white space, no words, no colours.")),
    "s34": dict(refs=["pine"], ar="1:1", style=WHITE, prompt=(
        "The olive-green Retra camera on white, wrapped with one glossy red satin ribbon tied in a big bow on top (ribbon"
        " does not cover the lens or wordmark), three-quarter view.")),
    "s36": dict(refs=[], ar="4:5", style="Real photo on white, soft daylight.", prompt=(
        "A messy heap of about twelve generic, unbranded single-use disposable film cameras in plain kraft-paper and"
        " black plastic (no logos, no text), with a few loose film canisters, piled on a white table.")),
    "s37": dict(refs=["chalk"], ar="4:5", style=WHITE, prompt=(
        "The off-white Retra camera lying on a white foam supermarket meat tray on an absorbent pad, tightly shrink-wrapped"
        " in clear plastic film with real wrinkles and glare, a plain blank white price label stuck on the film"
        " (no text on it), on white.")),
    "s41": dict(refs=[], ar="9:16", style=FLASH + " Haze, purple and blue stage light, high grain.", prompt=(
        "A packed concert crowd seen from behind, dozens of raised glowing phone screens (no readable content) blocking"
        " the stage lights, no band, no logos. Top 35% stage haze and beams.")),
    "s42a": dict(refs=[], ar="2:3", style="Over-processed smartphone selfie look, heavy beauty filter, oversharpened.",
        prompt=("A posed smartphone selfie of two young women pouting at arm's length at a generic seaside viewpoint,"
                " stiff, over-edited, no landmarks.")),
    "s42b": dict(refs=[], ar="2:3", style=FLASH, prompt=(
        "Two young women laughing mid-movement at a generic seaside viewpoint, hair blowing, candid, unposed, no camera"
        " or phone visible.")),
    "s43": dict(refs=["blossom"], ar="4:5", style="Real top-down photo, soft daylight, mild grain.", prompt=(
        "Holiday flat lay from directly above on white linen: the raspberry-pink Retra camera (front facing up) with"
        " glass ornaments, red ribbon curls, pine sprigs and a blank kraft gift tag. The top 30% is mostly plain linen.")),
    "s46": dict(refs=["chalk", "sol", "blossom"], ar="9:16", style=FLASH + " Garden party, late afternoon.", prompt=(
        "A woman's hand holds three Retra cameras fanned out like playing cards (off-white Chalk, mustard Sol, raspberry"
        " Blossom, each identical to its reference), fronts facing the viewer, in front of a blurred outdoor wedding"
        " party with string lights. Cameras in the middle of the frame. Fingers only on the cameras' edges, none over"
        " lenses or wordmarks; five natural fingers.")),
    "s47": dict(refs=["pine"], ar="9:16", style=PHONE, prompt=(
        "A young woman at a café table by a big window, looking out at the street, the olive-green Retra camera on the"
        " table beside a flat white coffee, front facing the viewer. Candid. Top 35% bright window.")),
    "s48": dict(refs=["sol"], ar="9:16", style="Front-facing phone selfie in a car, natural daylight, slight grain.",
        prompt=("A smiling young woman in a car's passenger seat, sunglasses on her head, road and hills through the"
        " window, holding the mustard-yellow Retra camera up next to her face, front of the camera facing the viewer."
        + GRIP)),
    "s49": dict(refs=["sol"], ar="9:16", style=FLASH + " Bright sun.", prompt=(
        "At a generic county-fair style amusement park, a dad carries his laughing daughter (about 5) on his shoulders;"
        " the mustard-yellow Retra camera hangs from a short wrist strap on his wrist, front facing the viewer. A generic"
        " carousel and Ferris wheel behind, no castles, no characters, no logos, no readable signs. Top 30% sky.")),
    "s51a": dict(refs=[], ar="3:2", style=PHONE + " Warm evening light.", prompt=(
        "A family of four at a dinner table, every person staring down at their own glowing phone (no readable screens),"
        " food untouched, nobody talking.")),
    "s51b": dict(refs=["chalk"], ar="3:2", style=FLASH + " Warm evening light.", prompt=(
        "The same kind of family of four at a dinner table, laughing together, phones nowhere; the off-white Retra camera"
        " sits on the table, front facing the viewer.")),
    "s53": dict(refs=["pine"], ar="9:16", style=FLASH + " Dusk, warm lantern light.", prompt=(
        "The olive-green Retra camera on a mossy granite rock beside a small tent and a glowing lantern at dusk in a pine"
        " forest, front facing the viewer, in the lower half of the frame. Top 35% dusk sky through the pines.")),
    "s56a": dict(refs=[], ar="1:1", style="Over-processed smartphone photo, heavy filter, oversaturated, oversharpened.",
        prompt=("A stiff, posed smartphone selfie of a young woman with a duck face at a café, heavy beauty filter.")),
    "s57": dict(refs=["blossom"], ar="9:16", style=PHONE, prompt=(
        "Seen from above at a slight angle: two hands lifting the raspberry-pink Retra camera out of a white gift box"
        " lined with tissue paper on a wooden table, front of the camera facing the viewer." + GRIP)),
    "s58": dict(refs=["chalk"], ar="9:16", style="Bright summer photo, hard sun, water caustics.", prompt=(
        "The off-white Retra camera lying on a blue-and-white striped towel at the tiled edge of a sunny swimming pool,"
        " front facing up toward the viewer, in the lower third of the frame. Top 55% sparkling turquoise pool water.")),
    "s59": dict(refs=[], ar="9:16", style="Thermal-imaging camera picture, iron colour palette (purple, red, orange, yellow, white-hot).",
        prompt=("A thermal image of a concert crowd seen from behind with many raised phones: the phones glow brightest"
                " white-hot, people in warm orange and red, background cool purple. No text, no numbers, no overlay.")),
}
render.COLOURS["dune"] = "caramel brown"
render.JOBS.update(J)
if __name__ == "__main__":
    ids = sys.argv[1:] or list(J)
    for i in ids:
        for c in J[i]["refs"]:
            render.ref_url(c)
    with ThreadPoolExecutor(10) as ex:
        list(ex.map(render.render, ids))
