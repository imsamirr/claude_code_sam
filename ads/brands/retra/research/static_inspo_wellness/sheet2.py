"""Two 4x5 contact sheets per brand (bigger thumbnails): sheet_<brand>_a.jpg (#0-19), _b.jpg (#20-39)."""
import sys
from PIL import Image, ImageDraw, ImageFont
b = sys.argv[1]
rows = [l.split() for l in open(f"candidates/{b}.txt") if l.strip()]
T, cols = 320, 4
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22) if __import__("os").path.exists("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") else ImageFont.load_default()
for part, lo in (("a", 0), ("b", 20)):
    chunk = rows[lo:lo + 20]
    sh = Image.new("RGB", (cols * (T + 8), 5 * (T + 30)), "white")
    for i, r in enumerate(chunk):
        try: im = Image.open(f"img/{b}/{r[0]}.jpg").convert("RGB")
        except Exception: continue
        im.thumbnail((T, T)); x, y = (i % cols) * (T + 8), (i // cols) * (T + 30)
        sh.paste(im, (x + (T - im.width) // 2, y))
        ImageDraw.Draw(sh).text((x + 4, y + T + 2), f"#{lo + i}  {r[2]}d", fill="red", font=f)
    sh.save(f"sheet_{b}_{part}.jpg", quality=82)
