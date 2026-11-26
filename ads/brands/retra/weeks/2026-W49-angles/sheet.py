"""Contact sheet of output/*_4x5.png (or 9x16 with --tall). python3 sheet.py [out.jpg] [--tall] [ids...]"""
import sys, glob
from PIL import Image, ImageDraw
args = [a for a in sys.argv[1:] if not a.startswith("--")]
tall = "--tall" in sys.argv
out = args[0] if args and args[0].endswith(".jpg") else "output/_sheet.jpg"
ids = [a for a in args if not a.endswith(".jpg")]
fs = sorted(glob.glob(f"output/*_{'9x16' if tall else '4x5'}.png"))
if ids: fs = [f for f in fs if any(f"_A49_{i}_" in f for i in ids)]
tw = 420; th = int(tw * (1920 / 1080 if tall else 1350 / 1080)); cols = 5
rows = (len(fs) + cols - 1) // cols
sh = Image.new("RGB", (cols * (tw + 10), rows * (th + 34)), "white")
for i, f in enumerate(fs):
    im = Image.open(f).convert("RGB").resize((tw, th))
    x, y = (i % cols) * (tw + 10), (i // cols) * (th + 34)
    sh.paste(im, (x, y)); ImageDraw.Draw(sh).text((x + 4, y + th + 8), f.split("/")[-1][8:60], fill="black")
sh.save(out, quality=85); print(out, len(fs))
