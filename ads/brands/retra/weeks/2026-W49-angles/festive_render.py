"""4K holiday-party backdrops for the G/N/O statics (Sam: 'more unique and holiday party theme').
python3 festive_render.py [ids...] -> renders/bg_<name>_t1.png"""
import sys
from concurrent.futures import ThreadPoolExecutor
import render

orig = render.build_prompt


def bp(job, fix=""):
    p = orig(job, fix)
    return p.replace(", except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference.",
                     ". No cameras, people, brand names, wordmarks, logos or lettering anywhere.")


render.build_prompt = bp
BASE = (" Shot from directly above or straight on as a flat backdrop that fills the whole frame; the centre 75% of the"
        " frame is the plain surface with only a few scattered details, the richer party details sit around the edges.")
J = {
    "bg_xmas_green": dict(refs=[], ar="9:16", style="Real photo, warm festive light, soft bokeh, rich colour.", prompt=(
        "A deep emerald-green velvet tablecloth at a holiday party, warm golden fairy-light bokeh, gold and red glass"
        " baubles, pine sprigs, red satin ribbon curls and small gold confetti around the edges." + BASE)),
    "bg_xmas_red": dict(refs=[], ar="9:16", style="Real photo, warm festive light, soft bokeh, rich colour.", prompt=(
        "A rich cranberry-red satin backdrop at a holiday party with gold tinsel garland, gold star confetti, cinnamon"
        " sticks, small wrapped presents in kraft paper and white ribbon around the edges." + BASE)),
    "bg_nye_gold": dict(refs=[], ar="9:16", style="Real photo, glamorous party light, sparkle, rich contrast.", prompt=(
        "A black glitter tablecloth at a New Year's Eve party scattered with gold metallic confetti, gold streamers,"
        " champagne coupes catching the light and sparkler trails around the edges." + BASE)),
    "bg_nye_midnight": dict(refs=[], ar="9:16", style="Real photo, glamorous party light, sparkle, rich contrast.", prompt=(
        "A deep midnight-blue sequin backdrop at a New Year's party with silver and gold star confetti, curled metallic"
        " streamers and a few silver party horns around the edges." + BASE)),
    "bg_party_redgold": dict(refs=[], ar="9:16", style="Real photo, warm festive light, soft bokeh, rich colour.", prompt=(
        "A festive party table with a deep red linen surface, gold sequin confetti, red and gold crackers, gold"
        " ribbon and warm string-light bokeh around the edges." + BASE)),
}
render.JOBS.update(J)
if __name__ == "__main__":
    ids = sys.argv[1:] or list(J)
    with ThreadPoolExecutor(6) as ex:
        list(ex.map(render.render, ids))
