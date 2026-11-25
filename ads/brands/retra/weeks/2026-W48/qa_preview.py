"""Side-by-side QA preview of renders: python3 qa_preview.py OUT.jpg 01_t1 03_t1 ..."""
import sys
from PIL import Image, ImageDraw
out, names = sys.argv[1], sys.argv[2:]
ims = []
for n in names:
    im = Image.open(f"renders/{n}.png").convert("RGB"); im.thumbnail((620, 775))
    ImageDraw.Draw(im).text((8, 8), n, fill="red")
    ims.append(im)
W = sum(i.width for i in ims) + 10 * (len(ims) - 1)
sheet = Image.new("RGB", (W, max(i.height for i in ims)), "white"); x = 0
for i in ims: sheet.paste(i, (x, 0)); x += i.width + 10
sheet.save(out, quality=88)
print(Image.open(f"renders/{names[0]}.png").size)
