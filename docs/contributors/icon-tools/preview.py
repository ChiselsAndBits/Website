"""Review helpers for the Chisels & Bits icon set.

    python preview.py sheet  <svg-dir> <out.png> [--bg "#1B1B1F"] [--size 32] [--names a,b,c]
    python preview.py cvd    <svg-dir> <out.png> --names a,b,c
    python preview.py stress <svg-dir> <out-dir>

sheet   Contact sheet of icons on one background colour at one size.
cvd     For each icon on website light and dark: normal, protanopia,
        deuteranopia, tritanopia (Machado et al. 2009, severity 1.0) and grayscale.
stress  Every icon on the background stress-test colours at 128 and 32 px
        (writes stress_128.png and stress_32.png).
"""
import argparse
import glob
import io
import os

import cairosvg
import numpy as np
from PIL import Image

CVD = {
    "normal": np.eye(3),
    "protan": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216],
                        [-0.003882, -0.048116, 1.051998]]),
    "deutan": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413],
                        [-0.011820, 0.042940, 0.968881]]),
    "tritan": np.array([[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602],
                        [0.004733, 0.691367, 0.303900]]),
    "gray": None,
}
STRESS = ["#FFFFFF", "#F6F6F7", "#202127", "#1B1B1F", "#C6C6C6", "#000000", "#3C8527", "#A2834F"]


def files(src, names):
    out = sorted(glob.glob(os.path.join(src, "*.svg")))
    if names:
        wanted = names.split(",")
        out = [f for f in out if os.path.splitext(os.path.basename(f))[0] in wanted]
    return out


def rast(path, size):
    png = cairosvg.svg2png(url=path, output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def sheet(a):
    fs = files(a.src, a.names)
    cols, cell = 6, a.size + 12
    img = Image.new("RGBA", (cols * cell, ((len(fs) + cols - 1) // cols) * cell), a.bg)
    for i, f in enumerate(fs):
        img.alpha_composite(rast(f, a.size), ((i % cols) * cell + 6, (i // cols) * cell + 6))
    img.save(a.out)


def _lin(c):
    c = c / 255
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _srgb(c):
    c = np.clip(c, 0, 1)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055) * 255


def cvd(a):
    fs = files(a.src, a.names)
    size, cell = 96, 104
    img = Image.new("RGB", (cell * len(CVD), cell * len(fs) * 2), "white")
    for r, f in enumerate(fs):
        icon = rast(f, size)
        for b, bg in enumerate(("#F6F6F7", "#202127")):
            base = Image.new("RGBA", (size, size), bg)
            base.alpha_composite(icon)
            lin = _lin(np.asarray(base.convert("RGB")).astype(float))
            for c, m in enumerate(CVD.values()):
                if m is None:
                    y = lin @ np.array([0.2126, 0.7152, 0.0722])
                    o = np.repeat(y[..., None], 3, 2)
                else:
                    o = lin @ m.T
                img.paste(Image.fromarray(_srgb(o).astype("uint8")), (c * cell + 4, (r * 2 + b) * cell + 4))
    img.save(a.out)


def stress(a):
    fs = files(a.src, a.names)
    os.makedirs(a.out, exist_ok=True)
    for size in (128, 32):
        cell = max(size, 40) + 8
        img = Image.new("RGBA", (cell * len(STRESS), cell * len(fs)), "white")
        for r, f in enumerate(fs):
            icon = rast(f, size)
            for c, bg in enumerate(STRESS):
                tile = Image.new("RGBA", (cell, cell), bg)
                tile.alpha_composite(icon, ((cell - size) // 2, (cell - size) // 2))
                img.paste(tile, (c * cell, r * cell))
        img.save(os.path.join(a.out, f"stress_{size}.png"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (("sheet", sheet), ("cvd", cvd), ("stress", stress)):
        p = sub.add_parser(name)
        p.add_argument("src", help="directory with SVG sources")
        p.add_argument("out", help="output PNG (or directory for stress)")
        p.add_argument("--names", help="comma-separated icon names (default: all)")
        if name == "sheet":
            p.add_argument("--bg", default="#FFFFFF")
            p.add_argument("--size", type=int, default=128)
        p.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
