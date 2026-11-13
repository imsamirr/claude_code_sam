"""Contact pages for a batch of raw clips, so footage can be reviewed by eye before cutting.

Each clip becomes a numbered tile with 3 frames (15% / 50% / 85% through) and its duration;
24 tiles per page. Use it on a whole Drive folder, then make dense sheets of the shortlist with
`python ads/video/build.py --sheet drive:<id> --every 0.5`.

Usage:
    python ads/video/triage.py clips.tsv out_dir/
    clips.tsv: one clip per line, "<source>\t<label>" where source is drive:<fileId> or a path.
    Writes out_dir/page0.jpg, page1.jpg, ... and out_dir/index.tsv (n, source, label, seconds).
"""

import io
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import FONTS, probe, resolve_source  # noqa: E402

TW, TH, PER = 306, 210, 24


def frame(path, t):
    out = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(path), "-frames:v", "1",
                          "-vf", "scale=100:178:force_original_aspect_ratio=increase,crop=100:178",
                          "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(out)) if out else Image.new("RGB", (100, 178))


def tile(item):
    src, label = item
    try:
        path = resolve_source(src)
        dur = probe(path)["dur"]
        frames = [frame(path, dur * f) for f in (0.15, 0.5, 0.85)]
    except SystemExit as e:
        print(f"skip {src}: {e}", file=sys.stderr)
        return src, label, 0.0, None
    return src, label, dur, frames


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    items = []
    for line in Path(sys.argv[1]).read_text().splitlines():
        if line.strip():
            parts = line.split("\t")
            items.append((parts[0], parts[1] if len(parts) > 1 else parts[0]))
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(8) as ex:
        tiles = list(ex.map(tile, items))
    font = ImageFont.truetype(str(FONTS / "Inter-Bold.otf"), 22)
    rows = []
    for p in range(0, len(tiles), PER):
        sheet = Image.new("RGB", (TW * 6, TH * 4), "black")
        d = ImageDraw.Draw(sheet)
        for k, (src, label, dur, frames) in enumerate(tiles[p:p + PER]):
            n, x, y = p + k, (k % 6) * TW, (k // 6) * TH
            for j, im in enumerate(frames or []):
                sheet.paste(im, (x + 2 + j * 101, y + 28))
            d.text((x + 4, y + 2), f"#{n} {dur:.0f}s", font=font, fill="yellow")
            rows.append(f"{n}\t{src}\t{label}\t{dur:.1f}")
        sheet.save(out / f"page{p // PER}.jpg", quality=85)
    (out / "index.tsv").write_text("\n".join(rows) + "\n")
    print(f"{len(tiles)} clips -> {out}/page*.jpg + index.tsv")


if __name__ == "__main__":
    main()
