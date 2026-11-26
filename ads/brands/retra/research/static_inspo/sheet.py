"""Download ad previews for a brand candidate list and make a numbered contact sheet.
    python3 sheet.py <brand>   reads candidates/<brand>.txt  (lines: ad_id url days)"""
import sys, urllib.request, os
from PIL import Image, ImageDraw, ImageFont
from concurrent.futures import ThreadPoolExecutor
b = sys.argv[1]
rows = [l.split() for l in open(f"candidates/{b}.txt") if l.strip()]
os.makedirs(f"img/{b}", exist_ok=True)
def get(r):
    p = f"img/{b}/{r[0]}.jpg"
    if not os.path.exists(p):
        urllib.request.urlretrieve(r[1], p)
    return p
with ThreadPoolExecutor(10) as ex: paths = list(ex.map(get, rows))
T, cols = 300, 8
n = len(rows); rws = (n + cols - 1) // cols
sh = Image.new("RGB", (cols * (T + 6), rws * (T + 30)), "white")
f = ImageFont.load_default()
for i, (r, p) in enumerate(zip(rows, paths)):
    try: im = Image.open(p).convert("RGB")
    except Exception: continue
    im.thumbnail((T, T)); x, y = (i % cols) * (T + 6), (i // cols) * (T + 30)
    sh.paste(im, (x, y)); ImageDraw.Draw(sh).text((x + 2, y + T + 4), f"#{i} {r[2]}d", fill="red", font=f)
sh.save(f"sheet_{b}.jpg", quality=80); print(n, "->", f"sheet_{b}.jpg", sh.size)
