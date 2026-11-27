"""4K Kie scenes for the Magic Kingdom statics (D1-D4). python3 disney_render.py [ids...]
Sam chose to show the real Cinderella Castle (2026-11-27, accepting the IP / ad-review risk), so these jobs drop the
"no castles / landmarks" clause from render.REAL. Characters stay out."""
import sys
from concurrent.futures import ThreadPoolExecutor
import render, batch2

G = batch2.GRIP
FLASH, PHONE = render.FLASH, render.PHONE
CASTLE = (" The castle is the real Cinderella Castle at Magic Kingdom, Walt Disney World, Florida, exactly as it really"
          " looks: white and grey stone walls, blue and gold conical spires.")
NOCHAR = " No costumed characters, mascots, cartoon characters or character merchandise anywhere."
J = {
    "d1": dict(refs=["blossom"], ar="9:16", style=FLASH + " Night, fireworks light, warm glow, grain.", prompt=(
        "Night at Magic Kingdom: fireworks burst over the castle in the upper half of the frame. A dense crowd in the"
        " middle ground all hold up glowing phones (plain, no logos, no readable screens) filming the show. In the"
        " lower-left foreground a mum in her late 30s and her daughter about 7 stand close, faces lit by the"
        " fireworks, looking up in wonder, NOT holding phones; the raspberry-pink Retra camera hangs from the mum's"
        " wrist on its strap, front facing the viewer." + CASTLE + NOCHAR)),
    "d2a": dict(refs=[], ar="4:5", style="Candid film-look snapshot, warm vintage colour, grain, slight vignette.", prompt=(
        "Early morning on Main Street, U.S.A. at Magic Kingdom, two kids (about 6 and 9) running ahead down the"
        " street toward the castle at the end, seen from behind, soft morning light, few people." + CASTLE + NOCHAR)),
    "d2b": dict(refs=[], ar="4:5", style="Candid film-look snapshot, warm vintage colour, grain, slight vignette.", prompt=(
        "Close candid of a girl about 6 with sugar on her face biting a long cinnamon churro, laughing, sunny park"
        " street behind her out of focus with the castle spires softly visible." + CASTLE + NOCHAR)),
    "d2c": dict(refs=[], ar="4:5", style="Candid black-and-white film-look snapshot, grain.", prompt=(
        "A dad carrying his son about 5 on his shoulders in a crowd on a park plaza, the boy pointing ahead with both"
        " arms up, both laughing, the castle behind them." + CASTLE + NOCHAR)),
    "d2d": dict(refs=[], ar="4:5", style="Candid film-look snapshot at night, warm, grain, slight motion blur.", prompt=(
        "Fireworks bursting over the castle at night, silhouettes of a family of four in the foreground, arms around"
        " each other, watching." + CASTLE + NOCHAR)),
    "d3": dict(refs=["sol"], ar="3:2", style=FLASH + " Bright afternoon sun.", prompt=(
        "A candid, slightly off-centre family photo in front of the castle at Magic Kingdom: mum, dad and two kids"
        " (about 5 and 8) squeezed together laughing, one kid mid-blink; the dad holds the mustard-yellow Retra camera"
        " at chest height, front facing the viewer." + CASTLE + NOCHAR + G)),
    "d4": dict(refs=["chalk"], ar="4:5", style=PHONE + " Bright morning sun, blue sky.", prompt=(
        "Main Street, U.S.A. at Magic Kingdom with the castle at the end of the street in the upper middle of the"
        " frame. In the middle ground a dad carries his daughter about 4 on his shoulders, both laughing. In the"
        " lower-right foreground the mum, seen from the side, raises the off-white Retra camera to photograph them,"
        " front of the camera facing the viewer." + CASTLE + NOCHAR + G)),
}
orig = render.build_prompt


def bp(job, fix=""):
    p = orig(job, fix)
    p = p.replace("brand logos, landmarks with logos, castles, cartoon characters or trademarks anywhere",
                  "brand logos, cartoon characters or trademarks anywhere (the castle architecture itself is wanted)")
    if not job["refs"]:
        p = p.replace(", except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference.",
                      ". No cameras, brand names, wordmarks, logos or lettering anywhere.")
    return p


render.build_prompt = bp
render.JOBS.update(J)
if __name__ == "__main__":
    ids = sys.argv[1:] or list(J)
    for i in ids:
        for c in J[i]["refs"]:
            render.ref_url(c)
    with ThreadPoolExecutor(10) as ex:
        list(ex.map(render.render, ids))
