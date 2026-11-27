"""4K Kie scenes for the pain-point statics (68-77). python3 pain_render.py [ids...]
No-camera jobs (refs=[]) get the no-wordmark rule from rerender_noref."""
import sys
from concurrent.futures import ThreadPoolExecutor
import render, batch2
ARGS = sys.argv[1:]
sys.argv = sys.argv[:1]  # rerender_noref renders its argv ids on import
import rerender_noref  # noqa: F401  (patches render.build_prompt; runs nothing without argv ids)

G = batch2.GRIP
FLASH, PHONE = render.FLASH, render.PHONE
J = {
    "p68": dict(refs=["sol"], ar="9:16", style=PHONE + " Hot bright early-afternoon sun, slightly washed out.", prompt=(
        "Candid at a busy generic amusement park (no recognisable rides, no castle, no characters): a mum in her mid 30s"
        " with sunglasses on her head, a backpack strap on one shoulder, raises the mustard-yellow Retra camera to"
        " photograph her two kids (about 5 and 8) who are laughing in the queue for a teacup-style ride behind her."
        " Camera in the lower-middle of the frame, front facing the viewer. The top 35% of the frame is pale sky and"
        " out-of-focus ride lights." + G)),
    "p70": dict(refs=["chalk"], ar="9:16", style=FLASH + " Warm afternoon window light, cosy kitchen.", prompt=(
        "Candid in a lived-in family kitchen: a grandmother in her late 60s with short silver hair and reading glasses"
        " pushed up, laughing, holds the off-white Retra camera up with both hands and photographs her two grandkids"
        " (about 4 and 7) who are covered in flour decorating cookies at the table. Grandma in the lower half,"
        " camera front facing the viewer. The top 35% is a calm plain kitchen wall." + G)),
    "p72a": dict(refs=[], ar="3:4", style=PHONE + " Midday, harsh light.", prompt=(
        "A crowded old-town street market abroad, dense crowd jostling: a young solo female traveller holds a large"
        " plain smartphone high above her head at arm's length to film, totally absorbed, her open tote bag hanging"
        " behind her; a stranger's hand in the crowd is close behind her. The phone is plain, no logo or text.")),
    "p72b": dict(refs=["obsidian"], ar="3:4", style=FLASH + " Midday, harsh light.", prompt=(
        "The same kind of crowded old-town street market abroad: a young solo female traveller with a zipped cross-body"
        " bag worn in front of her, holds the black Retra camera at chest height on its wrist strap and shoots, smiling,"
        " relaxed. Camera front facing the viewer, in the middle of the frame. No phone visible." + G)),
    "p75": dict(refs=["blossom"], ar="9:16", style=FLASH + " Christmas morning, warm tree lights, mild mess.", prompt=(
        "Christmas morning on a living-room floor full of torn wrapping paper: a girl about 9 in pyjamas, mouth open in"
        " delight, lifts the raspberry-pink Retra camera out of an open plain white gift box with both hands, front of"
        " the camera facing the viewer, in the lower-middle of the frame. Out-of-focus tree lights behind. The top 35%"
        " of the frame is soft blurred lights and wall." + G)),
    "p76": dict(refs=["dune"], ar="9:16", style=FLASH + " Golden hour on a tropical beach, warm, sun flare.", prompt=(
        "Candid honeymoon couple in their early 30s on a quiet tropical beach at golden hour, sitting close on a towel,"
        " laughing; she holds the caramel-brown Retra camera at arm's length turned toward them for a selfie, front of"
        " the camera facing the viewer and them, his chin on her shoulder. No phones anywhere. Couple in the lower 60%"
        " of the frame; top 35% warm sky and sea." + G)),
    "p77": dict(refs=["pine"], ar="9:16", style=PHONE + " Late afternoon sun, warm.", prompt=(
        "A woman traveller in her late 20s in a linen shirt stands on a sunlit hillside terrace above a generic"
        " Mediterranean town of white houses and terracotta roofs by the sea, raising the olive-green Retra camera to"
        " shoot the view, three-quarter view of her from the front, camera front facing the viewer in the middle of"
        " the frame. Top 30% open sky." + G)),
}
render.COLOURS["dune"] = "caramel brown"
render.JOBS.update(J)
if __name__ == "__main__":
    ids = ARGS or list(J)
    for i in ids:
        for c in J[i]["refs"]:
            render.ref_url(c)
    for _ in range(2):  # two takes; sequential passes so next_try() numbering doesn't race
        with ThreadPoolExecutor(10) as ex:
            list(ex.map(render.render, ids))
