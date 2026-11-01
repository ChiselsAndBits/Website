"""Generates the Chisels & Bits icon set from code.

Every icon described in docs/contributors/chisel-mode-icons.md is defined in
this file: the chisel mode icons, the radial menu group icons, and the UI and
tool icons. Edit the geometry here, re-run the script, and commit the
regenerated SVG and PNG files.

Usage (from the website repository root):

    pip install -r docs/contributors/icon-tools/requirements.txt
    python docs/contributors/icon-tools/generate_icons.py
    python docs/contributors/icon-tools/generate_icons.py \\
        --mod-icons ../Chisels-and-Bits/core/src/main/resources/assets/chiselsandbits/textures/icons

Output:
    public/icons/chiselmodes/design/<id>.svg  chisel mode and group sources
    public/icons/chiselmodes/<id>.png         128 x 128 renders
    public/icons/ui/design/<id>.svg           UI and tool icon sources
    public/icons/ui/<id>.png                  128 x 128 renders
"""
import argparse
import math as _m
import os
import shutil

INK = "#1A1C22"
HALO = "#F5F3EE"
GHOST = "#8C9099"
STONE = ("#D3D6DB", "#A0A6AF", "#6E747D")      # top, left, right
COBALT = ("#86A2FF", "#3F66F5", "#2541A8")
AMBER = ("#FFD08A", "#F39A2E", "#B4650C")

INK_W = 4
INNER_W = 2
HALO_W = INK_W + 2 * 3

SCALE = {1: 3, 2: 5, 3: 6, 4: 8, 5: 9, 7: 11, 8: 12, 16: 16}

DIGITS = {
    "1": ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "2": [".###.", "#...#", "....#", "..##.", ".#...", "#....", "#####"],
    "3": [".###.", "#...#", "....#", "..##.", "....#", "#...#", ".###."],
    "4": ["...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."],
    "5": ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."],
    "6": ["..##.", ".#...", "#....", "####.", "#...#", "#...#", ".###."],
    "7": ["#####", "....#", "...#.", "..#..", ".#...", ".#...", ".#..."],
    "8": [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "Z": ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"],
    "F": ["#####", "#####", ".###.", "..#..", "..#..", "..#..", "..##."],
}


def P(x, y, z):
    return (64 + 3 * (x - y), 68 + 1.5 * (x + y) - 3.5 * z)


def pts(points):
    return " ".join(f"{x:g},{y:g}" for x, y in points)


def poly(points, **attrs):
    a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<polygon points="{pts(points)}" {a}/>'


def line(p0, p1, **attrs):
    a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<line x1="{p0[0]:g}" y1="{p0[1]:g}" x2="{p1[0]:g}" y2="{p1[1]:g}" {a}/>'


class Icon:
    def __init__(self, title):
        self.title = title
        self.defs = []
        self.body = []
        self._pid = 0

    def add(self, s):
        self.body.append(s)

    def hatch(self, tone, stripe):
        self._pid += 1
        pid = f"h{self._pid}"
        self.defs.append(
            f'<pattern id="{pid}" width="8" height="8" patternUnits="userSpaceOnUse" '
            f'patternTransform="rotate(45)"><rect width="8" height="8" fill="{tone}"/>'
            f'<rect width="3" height="8" fill="{stripe}"/></pattern>')
        return f"url(#{pid})"

    def ghost(self, lattice=None):
        b = [(0, 0, 16), (16, 0, 16), (16, 0, 0), (16, 16, 0), (0, 16, 0), (0, 16, 16)]
        top = [P(0, 0, 16), P(16, 0, 16), P(16, 16, 16), P(0, 16, 16)]
        left = [P(0, 16, 16), P(16, 16, 16), P(16, 16, 0), P(0, 16, 0)]
        right = [P(16, 0, 16), P(16, 16, 16), P(16, 16, 0), P(16, 0, 0)]
        for face, op in ((top, 0.10), (left, 0.18), (right, 0.26)):
            self.add(poly(face, fill=GHOST, fill_opacity=op))
        back = P(0, 0, 0)
        for e in (P(0, 0, 16), P(16, 0, 0), P(0, 16, 0)):
            self.add(line(back, e, stroke=GHOST, stroke_width=2, stroke_dasharray="4 4"))
        if lattice:
            n = lattice
            for i in [16 - k * n for k in range(1, 8) if 16 - k * n > 0]:
                self.add(line(P(i, 0, 16), P(i, 16, 16), stroke=GHOST, stroke_width=2))
                self.add(line(P(0, i, 16), P(16, i, 16), stroke=GHOST, stroke_width=2))
                self.add(line(P(16, i, 16), P(16, i, 0), stroke=GHOST, stroke_width=2))
                self.add(line(P(16, 0, i), P(16, 16, i), stroke=GHOST, stroke_width=2))
                self.add(line(P(i, 16, 16), P(i, 16, 0), stroke=GHOST, stroke_width=2))
                self.add(line(P(0, 16, i), P(16, 16, i), stroke=GHOST, stroke_width=2))
        mid = P(16, 16, 16)
        for e in (P(16, 0, 16), P(0, 16, 16), P(16, 16, 0)):
            self.add(line(mid, e, stroke=GHOST, stroke_width=3, stroke_linecap="round"))
        self.add(poly([P(*c) for c in b], fill="none", stroke=GHOST, stroke_width=3,
                      stroke_linejoin="round"))

    def ticks(self, n):
        import math
        def tick(p, d):
            L = math.hypot(*d)
            q = (p[0] + d[0] / L * 9, p[1] + d[1] / L * 9)
            self.ticks_buf.append((p, q))
        self.ticks_buf = []
        for v in [16 - k * n for k in range(1, 8) if 16 - k * n > 0]:
            tick(P(v, 0, 16), (3, -1.5))
            tick(P(0, v, 16), (-3, -1.5))
            tick(P(16, 0, v), (3, -1.5))
            tick(P(0, 16, v), (-3, -1.5))
            tick(P(16, v, 0), (0, 1))
            tick(P(v, 16, 0), (0, 1))
        for p, q in self.ticks_buf:
            self.add(line(p, q, stroke=HALO, stroke_width=8, stroke_linecap="round"))
        for p, q in self.ticks_buf:
            self.add(line(p, q, stroke=INK, stroke_width=3, stroke_linecap="round"))

    def box(self, x0, y0, z0, x1, y1, z1, tones, hatch=False, halo=True):
        sil = [P(x0, y0, z1), P(x1, y0, z1), P(x1, y0, z0), P(x1, y1, z0), P(x0, y1, z0), P(x0, y1, z1)]
        if halo:
            self.add(poly(sil, fill=HALO, stroke=HALO, stroke_width=HALO_W, stroke_linejoin="round"))
        top = [P(x0, y0, z1), P(x1, y0, z1), P(x1, y1, z1), P(x0, y1, z1)]
        left = [P(x0, y1, z1), P(x1, y1, z1), P(x1, y1, z0), P(x0, y1, z0)]
        right = [P(x1, y0, z1), P(x1, y1, z1), P(x1, y1, z0), P(x1, y0, z0)]
        fills = list(tones)
        if hatch:
            fills = [self.hatch(tones[0], tones[1]), self.hatch(tones[1], tones[2]),
                     self.hatch(tones[2], INK)]
        self.add(poly(top, fill=fills[0]))
        self.add(poly(left, fill=fills[1]))
        self.add(poly(right, fill=fills[2]))
        c = P(x1, y1, z1)
        for e in (P(x1, y0, z1), P(x0, y1, z1), P(x1, y1, z0)):
            self.add(line(c, e, stroke=INK, stroke_width=INNER_W, stroke_linecap="round"))
        self.add(poly(sil, fill="none", stroke=INK, stroke_width=INK_W, stroke_linejoin="round"))

    def prism(self, cells, z0, z1, tones, halo=True):
        """Extrudes a union of square cells (x, y, size) between z0 and z1 as one solid."""
        from shapely.geometry import Polygon
        from shapely.ops import unary_union
        occ = set()
        for (x, y, sz) in cells:
            for a in range(sz):
                for b in range(sz):
                    occ.add((x + a, y + b))
        hexes = [Polygon([P(x, y, z1), P(x + 1, y, z1), P(x + 1, y, z0), P(x + 1, y + 1, z0),
                          P(x, y + 1, z0), P(x, y + 1, z1)]) for (x, y) in occ]
        sil = unary_union(hexes).buffer(0.01).simplify(0.05)
        sil_pts = list(sil.exterior.coords)
        if halo:
            self.add(poly(sil_pts, fill=HALO, stroke=HALO, stroke_width=HALO_W, stroke_linejoin="round"))
        order = sorted(occ, key=lambda c: (c[0] + c[1], c[0]))
        edges = []
        for (x, y) in order:
            if (x, y + 1) not in occ:
                self.add(poly([P(x, y + 1, z1), P(x + 1, y + 1, z1), P(x + 1, y + 1, z0), P(x, y + 1, z0)],
                              fill=tones[1], stroke=tones[1], stroke_width=2))
            if (x + 1, y) not in occ:
                self.add(poly([P(x + 1, y, z1), P(x + 1, y + 1, z1), P(x + 1, y + 1, z0), P(x + 1, y, z0)],
                              fill=tones[2], stroke=tones[2], stroke_width=2))
        tops = unary_union([Polygon([P(x, y, z1), P(x + 1, y, z1), P(x + 1, y + 1, z1), P(x, y + 1, z1)])
                            for (x, y) in occ]).buffer(0.01).simplify(0.05)
        self.add(poly(list(tops.exterior.coords), fill=tones[0]))
        for (x, y) in occ:
            if (x, y - 1) not in occ:
                edges.append((P(x, y, z1), P(x + 1, y, z1)))
            if (x - 1, y) not in occ:
                edges.append((P(x, y, z1), P(x, y + 1, z1)))
            if (x, y + 1) not in occ:
                edges.append((P(x, y + 1, z1), P(x + 1, y + 1, z1)))
                if (x - 1, y + 1) in occ or (x - 1, y) not in occ:
                    edges.append((P(x, y + 1, z1), P(x, y + 1, z0)))
            if (x + 1, y) not in occ:
                edges.append((P(x + 1, y, z1), P(x + 1, y + 1, z1)))
                if (x + 1, y + 1) in occ or (x, y + 1) not in occ:
                    edges.append((P(x + 1, y + 1, z1), P(x + 1, y + 1, z0)))
                if (x + 1, y - 1) in occ:
                    edges.append((P(x + 1, y, z1), P(x + 1, y, z0)))
            if (x, y + 1) not in occ and (x - 1, y + 1) in occ:
                pass
        for a, b in edges:
            self.add(line(a, b, stroke=INK, stroke_width=INNER_W, stroke_linecap="round"))
        self.add(poly(sil_pts, fill="none", stroke=INK, stroke_width=INK_W, stroke_linejoin="round"))

    def sphere(self, d, tones):
        cx, cy = P(8, 8, 8)
        r = d * 1.7
        self._pid += 1
        cid = f"c{self._pid}"
        self.defs.append(f'<clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r:g}"/></clipPath>')
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r:g}" fill="{HALO}" stroke="{HALO}" stroke-width="{HALO_W}"/>')
        self.add(f'<g clip-path="url(#{cid})">'
                 f'<rect width="128" height="128" fill="{tones[2]}"/>'
                 f'<circle cx="{cx - r * 0.18:g}" cy="{cy - r * 0.18:g}" r="{r * 0.92:g}" fill="{tones[1]}"/>'
                 f'<circle cx="{cx - r * 0.38:g}" cy="{cy - r * 0.38:g}" r="{r * 0.42:g}" fill="{tones[0]}"/>'
                 f'</g>')
        self.add(f'<path d="M {cx - r:g} {cy} A {r:g} {r / 2:g} 0 0 0 {cx + r:g} {cy}" fill="none" '
                 f'stroke="{INK}" stroke-width="{INNER_W}"/>')
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r:g}" fill="none" stroke="{INK}" stroke-width="{INK_W}"/>')

    def arrow(self, p0, p1, shaft=6, head=18, head_len=14):
        import math
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        nx, ny = -uy, ux
        b = (p1[0] - ux * head_len, p1[1] - uy * head_len)
        s = shaft / 2
        h = head / 2
        shape = [
            (p0[0] + nx * s, p0[1] + ny * s), (b[0] + nx * s, b[1] + ny * s),
            (b[0] + nx * h, b[1] + ny * h), p1,
            (b[0] - nx * h, b[1] - ny * h), (b[0] - nx * s, b[1] - ny * s),
            (p0[0] - nx * s, p0[1] - ny * s)]
        self.add(poly(shape, fill=HALO, stroke=HALO, stroke_width=6, stroke_linejoin="round"))
        self.add(poly(shape, fill=INK, stroke=INK, stroke_width=1, stroke_linejoin="round"))

    def seed(self, p):
        self.add(f'<circle cx="{p[0]:g}" cy="{p[1]:g}" r="9" fill="{INK}"/>')
        self.add(f'<circle cx="{p[0]:g}" cy="{p[1]:g}" r="6" fill="{HALO}"/>')
        self.add(f'<circle cx="{p[0]:g}" cy="{p[1]:g}" r="2.5" fill="{INK}"/>')

    def drag(self, p0, p1):
        self.add(line(p0, p1, stroke=HALO, stroke_width=8, stroke_linecap="round"))
        self.add(line(p0, p1, stroke=INK, stroke_width=3, stroke_dasharray="6 5", stroke_linecap="round"))
        self.seed(p0)
        self.add(f'<rect x="{p1[0] - 7:g}" y="{p1[1] - 7:g}" width="14" height="14" fill="{INK}" '
                 f'stroke="{HALO}" stroke-width="3" transform="rotate(45 {p1[0]:g} {p1[1]:g})"/>')

    def badge(self, text):
        self.badge_start = len(self.body)
        cell = 4
        gap = 4
        w = len(text) * 5 * cell + (len(text) - 1) * gap + 12
        h = 7 * cell + 12
        x0, y0 = 124 - w, 124 - h
        self.add(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="6" fill="{INK}" '
                 f'stroke="{HALO}" stroke-width="3"/>')
        cx = x0 + 6
        for ch in text:
            for r, row in enumerate(DIGITS[ch]):
                for c, v in enumerate(row):
                    if v == "#":
                        self.add(f'<rect x="{cx + c * cell}" y="{y0 + 6 + r * cell}" '
                                 f'width="{cell}" height="{cell}" fill="{HALO}"/>')
            cx += 5 * cell + gap

    def svg(self):
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">'
                f'<title>{self.title}</title><defs>{"".join(self.defs)}</defs>'
                + "".join(self.body) + "</svg>\n")


def centered(n):
    d = SCALE[n]
    a = 8 - d / 2
    return a, a + d


icons = {}
ui = {}


def cubed(name, n):
    i = Icon(name)
    i.ghost()
    a, b = centered(n)
    i.box(a, a, a, b, b, b, COBALT)
    i.badge(str(n))
    icons[name] = i


def aligned(name, n):
    i = Icon(name)
    d = SCALE[n] if n < 16 else 16
    i.ghost(lattice=None if n == 16 else d)
    i.box(16 - d, 16 - d, 16 - d, 16, 16, 16, COBALT)
    if n < 16:
        i.ticks(d)
        i.badge(str(n))
    icons[name] = i


for n, nm in ((1, "single-bit"), (2, "small-bit"), (4, "medium-bit"), (8, "large-bit")):
    cubed(nm, n)
for n, nm in ((2, "small-bit-aligned"), (4, "medium-bit-aligned"), (8, "large-bit-aligned"),
              (16, "full-cube")):
    aligned(nm, n)

for n in (1, 2, 4, 8):
    i = Icon(f"line-{n}")
    i.ghost()
    a, b = centered(n)
    i.box(a, a, 0, b, b, 16, COBALT)
    top = P(8, 8, 16)
    i.arrow((top[0], top[1] - 30), (top[0], top[1] - 6))
    i.badge(str(n))
    icons[f"line-{n}"] = i

    i = Icon(f"plane-{n}")
    i.ghost()
    i.box(0, 0, 16 - SCALE[n], 16, 16, 16, COBALT)
    i.badge(str(n))
    icons[f"plane-{n}"] = i

L_REGION = [(x, y, 4) for x in range(0, 16, 4) for y in range(0, 16, 4)
            if x >= 8 or y >= 12]
ISLAND = [(0, 0, 4)]

for n in (1, 2, 4, 8):
    d = SCALE[n]
    i = Icon(f"connected-plane-{n}")
    i.ghost()
    i.prism(ISLAND, 16 - d, 16, STONE)
    i.prism(L_REGION, 16 - d, 16, COBALT)
    i.seed(P(12, 12, 16))
    i.badge(str(n))
    icons[f"connected-plane-{n}"] = i

    i = Icon(f"connected-material-{n}")
    i.box(0, 0, 0, 16, 16, 8, STONE)
    i.prism(L_REGION, 8, 8 + d, COBALT)
    i.arrow(P(4, 6, 8), P(4, 6, 8 + 8))
    i.badge(str(n))
    icons[f"connected-material-{n}"] = i

for d, nm in ((4, "small-sphere"), (8, "medium-sphere"), (16, "large-sphere")):
    i = Icon(nm)
    i.ghost()
    i.sphere(SCALE[d], COBALT)
    i.badge(str(d))
    icons[nm] = i

i = Icon("drawn-cube")
i.ghost()
i.box(2, 2, 3, 14, 14, 11, COBALT)
i.drag(P(2, 14, 3), P(14, 2, 11))
icons["drawn-cube"] = i

i = Icon("drawn-line")
i.ghost()
i.box(0, 6.5, 6.5, 16, 9.5, 9.5, COBALT)
i.drag(P(0, 9.5, 8), P(16, 9.5, 8))
icons["drawn-line"] = i

for w, nm in ((3, "drawn-wall-thin"), (5, "drawn-wall-medium"), (7, "drawn-wall-fat")):
    i = Icon(nm)
    i.ghost()
    t = w
    i.box(0, 8 - t / 2, 0, 16, 8 + t / 2, 10, COBALT)
    i.drag(P(0, 8 + t / 2, 0), P(16, 8 + t / 2, 0))
    i.badge(str(w))
    icons[nm] = i

i = Icon("replace")
i.box(-2, 3, 6, 6, 11, 14, STONE)
i.box(10, 5, 0, 18, 13, 8, AMBER, hatch=True)
i.seed(P(2, 7, 14))
i.arrow(P(8, 3, 15), P(15, 7, 10.5))
icons["replace"] = i

# ---------------------------------------------------------------------------
# UI / tool icons (bit bag, change tracker, patterns, measuring tape, ...)
# ---------------------------------------------------------------------------


def glyph(icon, d, w=8, cap="round", join="round", extra=""):
    """A 2D Ink stroke with a Halo underlay."""
    icon.add(f'<path d="{d}" fill="none" stroke="{HALO}" stroke-width="{w + 6}" '
             f'stroke-linecap="{cap}" stroke-linejoin="{join}" {extra}/>')
    icon.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" '
             f'stroke-linecap="{cap}" stroke-linejoin="{join}" {extra}/>')


def head(icon, tip, direction, size=22, length=18):
    """Filled Ink arrowhead with Halo, pointing along `direction` and ending at `tip`."""
    L = _m.hypot(*direction)
    ux, uy = direction[0] / L, direction[1] / L
    nx, ny = -uy, ux
    b = (tip[0] - ux * length, tip[1] - uy * length)
    tri = [tip, (b[0] + nx * size / 2, b[1] + ny * size / 2), (b[0] - nx * size / 2, b[1] - ny * size / 2)]
    icon.add(poly(tri, fill=HALO, stroke=HALO, stroke_width=6, stroke_linejoin="round"))
    icon.add(poly(tri, fill=INK, stroke=INK, stroke_width=2, stroke_linejoin="round"))


def curve(icon, points, w=7, arrow_end=True, halo=True):
    d = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in points)
    if halo:
        icon.add(f'<path d="{d}" fill="none" stroke="{HALO}" stroke-width="{w + 6}" '
                 f'stroke-linecap="round" stroke-linejoin="round"/>')
    icon.add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" '
             f'stroke-linecap="round" stroke-linejoin="round"/>')
    if arrow_end:
        a, b = points[-2], points[-1]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = _m.hypot(dx, dy)
        head(icon, (b[0] + dx / L * 16, b[1] + dy / L * 16), (dx, dy), size=22, length=20)


def ring_points(axis, r, t0, t1, c=(8, 8, 8), n=90):
    out = []
    for k in range(n + 1):
        t = _m.radians(t0 + (t1 - t0) * k / n)
        u, v = r * _m.cos(t), r * _m.sin(t)
        if axis == "z":
            p = (c[0] + u, c[1] + v, c[2])
        elif axis == "x":
            p = (c[0], c[1] + u, c[2] + v)
        else:
            p = (c[0] + u, c[1], c[2] + v)
        out.append(p)
    return out


def spin(icon, axis, solid, r=10.5, t0=0, t1=300, c=(8, 8, 8)):
    """Rotation ring around an axis, correctly occluded by the solid drawn by `solid()`."""
    pts3 = ring_points(axis, r, t0, t1, c)
    depth0 = sum(c)
    segs, cur, front = [], [], None
    for p in pts3:
        f = (p[0] + p[1] + p[2]) > depth0
        if front is None or f == front:
            cur.append(p)
        else:
            segs.append((front, cur))
            cur = [cur[-1], p]
        front = f
    segs.append((front, cur))
    last = len(segs) - 1
    for i, (f, s) in enumerate(segs):
        if not f:
            curve(icon, [P(*p) for p in s], arrow_end=(i == last))
    solid()
    for i, (f, s) in enumerate(segs):
        if f:
            curve(icon, [P(*p) for p in s], arrow_end=(i == last))


def dim(icon, p0, p1, cap=9):
    """Dimension line with perpendicular end caps (the measuring motif)."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    L = _m.hypot(dx, dy)
    nx, ny = -dy / L * cap, dx / L * cap
    segs = [(p0, p1), ((p0[0] - nx, p0[1] - ny), (p0[0] + nx, p0[1] + ny)),
            ((p1[0] - nx, p1[1] - ny), (p1[0] + nx, p1[1] + ny))]
    for a, b in segs:
        icon.add(line(a, b, stroke=HALO, stroke_width=10, stroke_linecap="round"))
    for a, b in segs:
        icon.add(line(a, b, stroke=INK, stroke_width=4, stroke_linecap="round"))


def solid_halo(icon, boxes):
    """One merged Halo behind several touching boxes so internal seams stay crisp."""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    polys = []
    for (x0, y0, z0, x1, y1, z1) in boxes:
        polys.append(Polygon([P(x0, y0, z1), P(x1, y0, z1), P(x1, y0, z0), P(x1, y1, z0),
                              P(x0, y1, z0), P(x0, y1, z1)]))
    u = unary_union(polys).buffer(0.01)
    geoms = getattr(u, "geoms", [u])
    for g in geoms:
        icon.add(poly(list(g.exterior.coords), fill=HALO, stroke=HALO, stroke_width=HALO_W,
                      stroke_linejoin="round"))


def boxes(icon, items):
    """items: list of (box, tones, hatch). Drawn back-to-front in given order with one halo."""
    solid_halo(icon, [b for b, _, _ in items])
    for b, tones, h in items:
        icon.box(*b, tones, hatch=h, halo=False)


def outline_box(icon, x0, y0, z0, x1, y1, z1):
    """Dashed Ink wireframe for bits that are removed / not present."""
    v = lambda x, y, z: P(x, y, z)
    edges = [((x0, y0, z1), (x1, y0, z1)), ((x1, y0, z1), (x1, y1, z1)), ((x1, y1, z1), (x0, y1, z1)),
             ((x0, y1, z1), (x0, y0, z1)), ((x1, y0, z1), (x1, y0, z0)), ((x1, y1, z1), (x1, y1, z0)),
             ((x0, y1, z1), (x0, y1, z0)), ((x1, y0, z0), (x1, y1, z0)), ((x1, y1, z0), (x0, y1, z0))]
    for a, b in edges:
        icon.add(line(v(*a), v(*b), stroke=HALO, stroke_width=10, stroke_linecap="round"))
    for a, b in edges:
        icon.add(line(v(*a), v(*b), stroke=INK, stroke_width=5, stroke_linecap="round"))
    for a, b in edges:
        icon.add(line(v(*a), v(*b), stroke=COBALT[0], stroke_width=3, stroke_dasharray="6 5",
                      stroke_linecap="butt"))


# --- Measuring tape types --------------------------------------------------
i = Icon("bit")
i.ghost()
i.box(4, 4, 4, 12, 12, 12, COBALT)
a, b = P(4, 12, 4), P(12, 12, 4)
dim(i, (a[0] - 7, a[1] + 14), (b[0] - 7, b[1] + 14), cap=8)
ui["bit"] = i

i = Icon("block")
i.box(2, 2, 2, 14, 14, 14, COBALT)
a, b = P(2, 14, 2), P(14, 14, 2)
dim(i, (a[0] - 8, a[1] + 16), (b[0] - 8, b[1] + 16))
ui["block"] = i

i = Icon("line")
i.ghost()
p0, p1 = P(2, 14, 2), P(14, 2, 14)
dim(i, p0, p1, cap=8)
i.seed(p0)
i.seed(p1)
ui["line"] = i

# --- Pattern modification groups -------------------------------------------
MIRROR_L = [((-1, 10, 0, 7, 18, 7), STONE, False), ((-1, 14, 7, 7, 18, 15), STONE, False)]

MIRROR_R = [((y0, x0, z0, y1, x1, z1), t, h) for ((x0, y0, z0, x1, y1, z1), t, h) in MIRROR_L]
i = Icon("mirror")
boxes(i, MIRROR_L)
boxes(i, MIRROR_R)
top, bot = P(-1, -1, 18), P(17, 17, -2)
i.add(f'<rect x="{top[0] - 7:g}" y="{top[1]:g}" width="14" height="{bot[1] - top[1]:g}" rx="4" '
      f'fill="{HALO}" stroke="{HALO}" stroke-width="6"/>')
i.add(f'<rect x="{top[0] - 5:g}" y="{top[1] + 2:g}" width="10" height="{bot[1] - top[1] - 4:g}" rx="3" '
      f'fill="{COBALT[1]}" stroke="{INK}" stroke-width="{INK_W}"/>')
ui["mirror"] = i

i = Icon("rotate")
spin(i, "z", lambda: boxes(i, [((3.5, 3.5, 0, 12.5, 12.5, 9), STONE, False)]), r=11.5, t0=150, t1=410,
     c=(8, 8, 4.5))
ui["rotate"] = i

for ax, nm in (("x", "roll_x"), ("y", "roll_z")):
    i = Icon(nm)
    i.ghost()
    spin(i, ax, lambda: boxes(i, [((4, 4, 4, 12, 12, 12), STONE, False)]), r=9.5, t0=120, t1=380)
    i.badge("X" if ax == "x" else "Z")
    ui[nm] = i

# --- Pattern placement types -----------------------------------------------
NOTCH = (8, 8, 8, 16, 16, 16)
NOTCHED = [((0, 0, 0, 16, 16, 8), STONE, False), ((0, 0, 8, 8, 16, 16), STONE, False),
           ((8, 0, 8, 16, 8, 16), STONE, False)]

i = Icon("pattern_place")
i.ghost()
boxes(i, [((8, 8, 0, 16, 16, 8), COBALT, False), ((8, 8, 8, 16, 16, 16), COBALT, False)])
t = P(12, 12, 16)
i.arrow((t[0], t[1] - 34), (t[0], t[1] - 8))
ui["pattern_place"] = i

i = Icon("pattern_merge")
boxes(i, NOTCHED)
boxes(i, [((8, 8, 8, 16, 16, 16), COBALT, False)])
i.add(poly([P(8, 8, 16), P(16, 8, 16), P(16, 16, 16), P(8, 16, 16)], fill="none"))
ui["pattern_merge"] = i

i = Icon("pattern_impose")
boxes(i, [((0, 0, 0, 16, 16, 16), STONE, False)])
boxes(i, [((6, 6, 6, 17, 17, 17), COBALT, False)])
t = P(11.5, 11.5, 17)
i.arrow((t[0], t[1] - 26), (t[0], t[1] - 4), shaft=8, head=22, head_len=16)
ui["pattern_impose"] = i

i = Icon("pattern_remove")
boxes(i, NOTCHED)
outline_box(i, 8, 8, 8, 16, 16, 16)
t = P(12, 12, 16)
i.arrow((t[0] + 6, t[1] - 4), (t[0] + 26, t[1] - 36))
ui["pattern_remove"] = i

CARVED = [((0, 0, 0, 8, 16, 16), STONE, False), ((8, 0, 0, 16, 8, 16), STONE, False)]
i = Icon("pattern_carve")
boxes(i, CARVED)
i.add(poly([P(8, 8, 0), P(16, 8, 0), P(16, 16, 0), P(8, 16, 0)], fill=STONE[0]))
outline_box(i, 8, 8, 0, 16, 16, 16)
ui["pattern_carve"] = i

# --- Change tracker / generic actions ---------------------------------------
i = Icon("undo")
glyph(i, "M 98 104 V 70 A 26 26 0 0 0 72 44 H 40", w=12)
head(i, (14, 44), (-1, 0), size=40, length=30)
ui["undo"] = i

i = Icon("redo")
i.add('<g transform="translate(128 0) scale(-1 1)">')
glyph(i, "M 98 104 V 70 A 26 26 0 0 0 72 44 H 40", w=12)
head(i, (14, 44), (-1, 0), size=40, length=30)
i.add("</g>")
ui["redo"] = i

i = Icon("trash")
boxes(i, [((3, 3, 0, 13, 13, 12), STONE, False), ((1.5, 1.5, 12, 14.5, 14.5, 14.5), STONE, False),
          ((6, 6.5, 14.5, 10, 9.5, 16.5), STONE, False)])
for k in (5.5, 8, 10.5):
    i.add(line(P(k, 13, 10), P(k, 13, 2), stroke=INK, stroke_width=3, stroke_linecap="round"))
    i.add(line(P(13, k, 10), P(13, k, 2), stroke=INK, stroke_width=3, stroke_linecap="round"))
ui["trash"] = i

i = Icon("sort")
boxes(i, [((-1, 4, 0, 17, 10, 5), COBALT, False), ((-1, 4, 5, 11, 10, 10), COBALT, False),
          ((-1, 4, 10, 5, 10, 15), COBALT, False)])
a, b = P(14, 7, 20), P(14, 7, 8)
i.arrow(a, b, shaft=8, head=22, head_len=16)
ui["sort"] = i

i = Icon("place")
boxes(i, [((0, 0, 0, 16, 16, 5), STONE, False), ((4, 4, 5, 12, 12, 13), COBALT, False)])
t = P(8, 8, 13)
i.arrow((t[0], t[1] - 46), (t[0], t[1] - 6), shaft=8, head=24, head_len=18)
ui["place"] = i

i = Icon("swap")
i.box(-1, 5, 3, 7, 13, 11, STONE)
i.box(9, 3, 5, 17, 11, 13, AMBER, hatch=True)
glyph(i, "M 30 40 Q 52 10 82 26", w=7)
head(i, (98, 40), (1, 0.9), size=22, length=18)
glyph(i, "M 98 92 Q 76 122 46 106", w=7)
head(i, (30, 92), (-1, -0.9), size=22, length=18)
ui["swap"] = i


# --- Bit bag modes -------------------------------------------------------------
def bag(title, badge_text=None):
    ic = Icon(title)
    body = ("M 52 40 C 30 52 18 72 20 92 C 22 110 36 118 64 118 "
            "C 92 118 106 110 108 92 C 110 72 98 52 76 40 Z")
    flaps = "M 46 14 L 82 14 L 74 32 L 54 32 Z"
    band = "M 48 30 H 80 V 42 H 48 Z"
    for d in (body, flaps, band):
        ic.add(f'<path d="{d}" fill="{HALO}" stroke="{HALO}" stroke-width="{HALO_W}" stroke-linejoin="round"/>')
    ic._pid += 1
    cid = f"bag{ic._pid}"
    ic.defs.append(f'<clipPath id="{cid}"><path d="{body}"/></clipPath>')
    ic.add(f'<path d="{body}" fill="{STONE[1]}"/>')
    ic.add(f'<g clip-path="url(#{cid})"><path d="M 72 30 C 98 50 100 96 80 128 H 128 V 30 Z" '
           f'fill="{STONE[2]}"/><ellipse cx="44" cy="70" rx="14" ry="20" fill="{STONE[0]}"/></g>')
    ic.add(f'<path d="{body}" fill="none" stroke="{INK}" stroke-width="{INK_W}" stroke-linejoin="round"/>')
    ic.add(f'<path d="{flaps}" fill="{STONE[0]}" stroke="{INK}" stroke-width="{INK_W}" stroke-linejoin="round"/>')
    ic.add(f'<path d="{band}" fill="{INK}" stroke="{INK}" stroke-width="{INK_W}" stroke-linejoin="round"/>')
    if badge_text:
        ic.badge(badge_text)
    ui[title] = ic


bag("bag_mode_normal")
bag("bag_mode_filter")
_b = ui["bag_mode_filter"]
_b.badge_start = len(_b.body)
_b.add(f'<rect x="88" y="84" width="36" height="40" rx="6" fill="{INK}" stroke="{HALO}" stroke-width="3"/>')
_b.add(f'<path d="M 95 92 H 117 L 109 104 V 116 L 103 119 V 104 Z" fill="{HALO}"/>')
bag("bag_mode_first", "1")
bag("bag_mode_second", "2")

GROUPS = {
    "group_cubed": "medium-bit",
    "group_cubed_aligned": "medium-bit-aligned",
    "group_line": "line-4",
    "group_plane": "plane-4",
    "group_sphere": "medium-sphere",
    "group_connected_plane": "connected-plane-4",
    "group_connected_material": "connected-material-4",
    "group_draw": "drawn-cube",
}
for gname, src in GROUPS.items():
    s_icon = icons[src]
    g = Icon(gname)
    g.defs = list(s_icon.defs)
    g.body = s_icon.body[:getattr(s_icon, "badge_start", len(s_icon.body))]
    icons[gname] = g

# Construction template (not an icon): canvas, clear edge, block keylines, badge zone.
t = Icon("construction-template")
t.add('<rect x="0" y="0" width="128" height="128" fill="none" stroke="#E5484D" stroke-width="1"/>')
t.add('<rect x="2" y="2" width="124" height="124" fill="none" stroke="#E5484D" stroke-width="0.75" stroke-dasharray="3 2"/>')
for k in range(0, 17):
    t.add(line(P(k, 0, 16), P(k, 16, 16), stroke="#8C9099", stroke_width=0.5))
    t.add(line(P(0, k, 16), P(16, k, 16), stroke="#8C9099", stroke_width=0.5))
    t.add(line(P(16, k, 16), P(16, k, 0), stroke="#8C9099", stroke_width=0.5))
    t.add(line(P(16, 0, k), P(16, 16, k), stroke="#8C9099", stroke_width=0.5))
    t.add(line(P(k, 16, 16), P(k, 16, 0), stroke="#8C9099", stroke_width=0.5))
    t.add(line(P(0, 16, k), P(16, 16, k), stroke="#8C9099", stroke_width=0.5))
t.ghost()
t.add('<rect x="92" y="84" width="32" height="40" rx="6" fill="#1A1C22" fill-opacity="0.15" stroke="#1A1C22" stroke-dasharray="3 2"/>')
t.add(f'<circle cx="64" cy="64" r="1.5" fill="#E5484D"/>')
icons["construction-template"] = t


def write(svg_dir, png_dir, mod_dir, name, icon, png=True):
    svg_path = os.path.join(svg_dir, f"{name}.svg")
    with open(svg_path, "w") as f:
        f.write(icon.svg())
    if not png:
        return
    import cairosvg
    png_path = os.path.join(png_dir, f"{name}.png")
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=128, output_height=128)
    if mod_dir:
        shutil.copyfile(png_path, os.path.join(mod_dir, f"{name}.png"))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Generates the Chisels & Bits icon set.")
    ap.add_argument("--site", default=os.path.normpath(os.path.join(here, "..", "..", "..")),
                    help="website repository root (default: inferred from this file)")
    ap.add_argument("--mod-icons", help="also copy every PNG into this folder "
                    "(the mod's assets/chiselsandbits/textures/icons)")
    ap.add_argument("--svg-only", action="store_true", help="skip PNG rendering")
    args = ap.parse_args()

    cm = os.path.join(args.site, "public", "icons", "chiselmodes")
    uid = os.path.join(args.site, "public", "icons", "ui")
    for d in (cm, os.path.join(cm, "design"), uid, os.path.join(uid, "design")):
        os.makedirs(d, exist_ok=True)
    if args.mod_icons and not os.path.isdir(args.mod_icons):
        ap.error(f"{args.mod_icons} is not a directory")

    for name, icon in icons.items():
        fname = name.replace("-", "_")
        template = fname == "construction_template"
        write(os.path.join(cm, "design"), cm, None if template else args.mod_icons,
              fname, icon, png=not (args.svg_only or template))
    for name, icon in ui.items():
        write(os.path.join(uid, "design"), uid, args.mod_icons, name, icon, png=not args.svg_only)
    print(f"{len(icons) - 1} chisel mode and group icons, {len(ui)} UI icons written")


if __name__ == "__main__":
    main()
