---
title: Chisel Mode Icon Design
order: 4
---

<script setup>
import { withBase } from 'vitepress'

const icon = (id) => withBase(`/icons/chiselmodes/design/${id}.svg`)

const showcase = [
  'single_bit', 'medium_bit_aligned', 'drawn_wall_medium', 'line_4', 'plane_2',
  'connected_plane_4', 'connected_material_4', 'medium_sphere', 'replace'
]

const backgrounds = [
  { name: 'Website light', color: '#F6F6F7' },
  { name: 'Website dark', color: '#202127' },
  { name: 'Minecraft GUI', color: '#C6C6C6' },
  { name: 'Black overlay', color: '#000000' },
  { name: 'Grass', color: '#3C8527' },
  { name: 'Oak planks', color: '#A2834F' }
]
</script>

<style module>
.gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 12px;
  border-radius: 8px;
  margin: 8px 0 4px 0;
  align-items: center;
}
.gallery img {
  display: block;
}
.caption {
  font-size: 12px;
  color: var(--vp-c-text-2);
  margin: 0 0 12px 0;
}
.cell {
  width: 48px;
  height: 48px;
  max-width: none;
}
</style>

# Chisel mode icon design language

This page defines the visual language for the chisel mode icons shown in the
radial menu in game and on the [chisel mode pages](../players/chiselmodes/index.md)
of this website. It applies to every new or redrawn chisel mode icon.

The production icons in `public/icons/chiselmodes/` are 128 × 128 PNGs, one
per mode, named after the mode id. They are rendered from the SVG sources in
[`public/icons/chiselmodes/design/`](https://github.com/ChiselsAndBits/Website/tree/main/public/icons/chiselmodes/design),
which follow this page exactly. They replace the earlier 16 × 16 pixel art,
which was mostly white and disappeared on light backgrounds, drew spheres as
flat discs, relied on red against blue alone, and shared one icon between
several size variants.

To change an icon, edit its SVG source and re-export it to a 128 × 128 PNG
with the same name in `public/icons/chiselmodes/`.

<div :class="$style.gallery" style="background: var(--vp-c-bg-soft)">
  <img v-for="id in showcase" :key="id" :src="icon(id)" :alt="id" :title="id" width="64" height="64" />
</div>
<p :class="$style.caption">Specimens on the current website theme. Toggle light and dark mode to compare.</p>

## Requirements

Every icon must meet these four requirements. The rest of this page explains how.

| # | Requirement | How the language meets it |
| --- | --- | --- |
| 1 | Always exactly **128 × 128** pixels | A fixed [canvas and construction grid](#canvas-and-export) with one shared reference block |
| 2 | Show that every operation is **3D** | One fixed [isometric projection](#projection-and-3d), three-tone face lighting, and a reference block for scale |
| 3 | Readable with **colour vision deficiencies** | Colour is never the only cue. Every meaning also has a [shape, pattern, or luminance](#colour-and-accessibility) difference |
| 4 | Readable on **light and dark** backgrounds, both on the website and in game | A [double keyline](#the-double-keyline) of dark Ink and light Halo around every element, and transparent backgrounds only |

## Canvas and export

| Property | Rule |
| --- | --- |
| Size | 128 × 128 px. Do not use other sizes, and never upscale lower-resolution art. |
| Source format | SVG, built on the [construction template](#construction-template) |
| Delivered format | PNG, 8-bit RGBA, sRGB, transparent background |
| Clear edge | Keep 2 px clear on all sides. Nothing, including the Halo, may touch the outer 2 px. |
| Background | Fully transparent. Do not add a backing plate, glow, or drop shadow. |
| Text | Do not use font text. Draw numerals with the [pixel numerals](#size-badge) as shapes. |
| File name | The mode id, for example `connected_plane_4.png`. Each mode gets its own icon, so variants no longer share files. |
| Anti-aliasing | Allowed and expected at 128 px. Keep every structural edge on the projection grid so edges stay crisp when scaled down. |

Icons are scaled down at runtime. The website shows them at 64 px, and the
radial menu typically shows them at about 32 px, depending on GUI scale.
Design at 128 px, but **judge legibility at 32 px**: every
[minimum size](#line-weights-and-minimum-sizes) on this page exists so a
feature stays at least one screen pixel wide at 32 px. The game should sample
these textures with linear filtering or mipmaps. Nearest-neighbour
downsampling from 128 px drops thin lines.

## Projection and 3D

Every icon uses the **same 2:1 isometric projection** and the **same
reference block**. That way, size and position mean the same thing in every
icon.

### Coordinates

Work in *bit coordinates*. A Minecraft block is 16 × 16 × 16 bits, so `x`,
`y`, and `z` run from 0 to 16:

- `x` points toward the viewer's right-front.
- `y` points toward the viewer's left-front.
- `z` points up.

A bit coordinate maps to canvas pixels as follows:

```text
px = 64 + 3 · (x − y)
py = 68 + 1.5 · (x + y) − 3.5 · z
```

| One bit along | Moves on canvas |
| --- | --- |
| `x` | 3 px right, 1.5 px down |
| `y` | 3 px left, 1.5 px down |
| `z` | 3.5 px up |

The **reference block** (0,0,0)–(16,16,16) therefore covers x 16–112 and
y 12–116, and its centre (8,8,8) lands exactly on the canvas centre (64, 64).
Place geometry on whole or half bits so edges land on clean pixel positions.
Do not rotate the camera, use perspective, or mirror the view for individual
icons.

### Lighting

Light always comes from the top-left. Every solid has three visible faces,
and each face always uses the same tone of its colour ramp:

| Face | Faces toward | Tone |
| --- | --- | --- |
| Top | +z | Light |
| Left | +y | Mid |
| Right | +x | Dark |

This fixed light-mid-dark order is what makes a shape read as a volume. It
works in grayscale and for every type of colour vision. Spheres use the same
three tones as banded shading: the dark base, a mid disc offset toward the
top-left, and a light highlight. Add an Ink equator arc on the front half
to show the curvature. Do not use soft gradients, because they turn to mud
at 32 px.

### Drawing order

Paint back to front. Each solid element is drawn as follows:

1. Halo: the silhouette filled and stroked in Halo, which [knocks out](#the-double-keyline) whatever lies behind it.
2. Face fills: top, left, and right.
3. Inner edges: the three edges meeting at the front-top corner, in Ink.
4. Silhouette outline in Ink.

## Line weights and minimum sizes

All sizes are in pixels on the 128 px canvas.

| Element | Size | At 32 px |
| --- | --- | --- |
| Silhouette outline (Ink) | 4 px, round joins | 1 px |
| Inner face edges (Ink) | 2 px | 0.5 px, which shows as a tone change |
| Halo outside the outline | 3 px (stroke width 10 behind the 4 px outline) | about 1 px |
| Ghost block edges | 3 px visible, 2 px dashed `4 4` hidden | about 1 px |
| Smallest solid feature | 8 px across | 2 px |
| Arrow shaft and head | 6 px shaft, 18 px head, 14 px head length | readable |

## Colour and accessibility

### Palette

Colours have **roles**, not decorative meaning. Do not add new hues. If a
new mode needs a new meaning, express it with a new shape motif first.

| Role | Light (top) | Mid (left) | Dark (right) | Used for |
| --- | --- | --- | --- | --- |
| **Ink** | `#1A1C22` | | | Outlines, edges, arrows, badge, markers |
| **Halo** | `#F5F3EE` | | | Outer keyline, marker and badge highlights |
| **Ghost** | `#8C9099` | | | The transparent reference block |
| **Selection** (cobalt) | `#86A2FF` | `#3F66F5` | `#2541A8` | The volume the mode affects |
| **Material** (stone) | `#D3D6DB` | `#A0A6AF` | `#6E747D` | Existing bits that are not selected |
| **Second material** (amber, hatched) | `#FFD08A` | `#F39A2E` | `#B4650C` | A different material, used only by Replace |

The Ghost block's faces use Ghost at 10% (top), 18% (left), and 26% (right)
opacity. This tinted glass reads on both light and dark backgrounds and keeps
the lighting order.

### Never rely on hue alone

Cobalt and amber are the most distinguishable pair under protanopia,
deuteranopia, and tritanopia. Still, every meaning must survive with **no
colour at all**:

- **Luminance**: each ramp step differs from its neighbour by about 1.9:1
  contrast. Selection and Material differ by 1.7:1 to 1.9:1 on the same face.
- **Pattern**: the second material is always hatched with 45° stripes, 3 px
  wide every 8 px, drawn in the next darker tone. A hatched cube is "the
  other material" even in grayscale.
- **Shape**: modifiers such as aligned, connected, drawn, or extrude are always
  shown with a [motif](#motif-vocabulary), never only with a colour change.

The old icons distinguished Connected Material from Connected Plane only by a
red top face. In this language, Extrude shows a solid stone block with a
raised region and an up arrow, while Connected Plane shows a region cut into
the glass reference block next to an unselected island.

## The double keyline

The icons are shown on the website in light and dark mode, and in game over
GUI panels and over arbitrary world terrain. No single colour contrasts with
all of these backgrounds. The language solves this with two keylines around
every element:

- An inner **Ink** outline (4 px, dark) that carries the shape on light backgrounds.
- An outer **Halo** band (3 px, light) that carries the shape on dark backgrounds.

Ink against Halo is **15.4:1**. Contrast ratios multiply, so for *any*
background colour at least one of the two keylines reaches √15.4 ≈ **3.9:1**,
which is above the WCAG 3:1 minimum for graphical objects. On the test
backgrounds this works out as follows:

| Background | Ink | Halo | Best keyline |
| --- | --- | --- | --- |
| Website light `#F6F6F7` | 15.8:1 | 1.0:1 | Ink |
| Website dark `#202127` | 1.1:1 | 14.5:1 | Halo |
| Minecraft GUI `#C6C6C6` | 10.0:1 | 1.5:1 | Ink |
| Black `#000000` | 1.2:1 | 18.9:1 | Halo |

The Halo also **knocks out** what lies behind an element. Where the
selection overlaps the Ghost block or a marker overlaps the selection, the
Halo cuts a clean gap, so overlapping layers stay separate.

The face fills are mid-luminance. Cobalt mid is 4.4:1 on website light and
3.4:1 on website dark, so filled areas stay visible on both themes even
before the keylines are considered.

## Size encoding

Many modes come in sizes (1, 2, 4, 8 bits and so on). Drawn at true scale, a
single bit would be 6 px wide, which is invisible at 32 px. Sizes are
therefore drawn on a fixed **legibility scale** and stated exactly with a
**size badge**.

### Legibility scale

| Nominal size (bits) | 1 | 2 | 4 | 8 | 16 |
| --- | --- | --- | --- | --- | --- |
| Drawn size (bits) | 3 | 5 | 8 | 12 | 16 |

Use this table for cube edges, line thickness, plane and extrusion depth, and
sphere diameter. A given nominal size is always drawn the same way, so
Plane 4, Line 4, and Medium Bit share one visual size. Quantities that are
already 3 bits or more and outside this series, such as drawn wall widths of
3, 5, and 7, are drawn at true scale.

### Size badge

Every mode that has size variants carries a badge in the bottom-right
corner. Single-variant modes (Full Cube, Drawn Cube, Drawn Line, Replace) do
not have one.

- The badge is an Ink rounded rectangle (corner radius 6 px) with a 3 px Halo stroke, anchored to the bottom-right at (124, 124).
- One digit is 32 × 40 px. Each extra digit adds 24 px of width toward the left.
- Numerals are drawn in Halo on a **5 × 7 pixel grid of 4 px cells**, with 6 px padding and a 4 px gap between digits. At 32 px, each cell is exactly one screen pixel, in the spirit of the Minecraft font.
- The badge sits on top of everything else and may overlap the reference block.

The badge number is the value players see in the mode name. It is the
selection edge for cubes, the thickness for lines, the depth for planes,
connected planes, and extrusions, the diameter for spheres, and the total
width for drawn walls.

## Motif vocabulary

Every icon is composed only from these parts. Use each motif for one meaning
only.

| Motif | Looks like | Means |
| --- | --- | --- |
| **Ghost block** | The reference block as tinted glass, with dashed hidden edges | One block of space, for scale and position. Used by geometry modes. |
| **Selection** | A cobalt solid | The bits the mode affects |
| **Material block** | A stone solid | Existing bits. Shown by modes that depend on material. |
| **Second material** | An amber, hatched solid | A different material (Replace) |
| **Snap lattice** | Ghost-coloured lines on the glass faces, spaced at the selection size and starting at the selection | The selection snaps to a grid |
| **Snap ticks** | Short Ink ticks with a Halo outline, pointing outward where lattice lines meet the block outline | Snapping. Stays visible when the selection covers the lattice. |
| **Seed marker** | An Ink ring with a Halo centre and an Ink dot (r 9 / 6 / 2.5 px) | The bit you clicked, which matters for flood-fill and material matching |
| **Drag path** | A dashed Ink line (`6 5`) on a Halo underlay, from a seed marker to a diamond handle | Click-and-drag definition |
| **Direction arrow** | A solid Ink arrow with a Halo outline | The direction of the operation |
| **Size badge** | An Ink plate with Halo pixel numerals | The exact size variant |

**Geometry modes** show the Ghost block. **Material-aware modes** (Extrude
and Replace) show solid stone material instead. Players can see at a glance
whether a mode cares about material.

## Mode catalogue

The specimen column renders on this page's current theme. Toggle between
light and dark mode to check both.

| Specimen | Mode id | Composition | Badge |
| --- | --- | --- | --- |
| <img :src="icon('single_bit')" :class="$style.cell" alt="single_bit" /> | `single_bit` | Selection cube centred in the Ghost block | 1 |
| <img :src="icon('small_bit')" :class="$style.cell" alt="small_bit" /> | `small_bit` | As above, drawn edge 5 | 2 |
| <img :src="icon('medium_bit')" :class="$style.cell" alt="medium_bit" /> | `medium_bit` | As above, drawn edge 8 | 4 |
| <img :src="icon('large_bit')" :class="$style.cell" alt="large_bit" /> | `large_bit` | As above, drawn edge 12 | 8 |
| <img :src="icon('small_bit_aligned')" :class="$style.cell" alt="small_bit_aligned" /> | `small_bit_aligned` | Selection cube in the front-top corner, snap lattice and snap ticks | 2 |
| <img :src="icon('medium_bit_aligned')" :class="$style.cell" alt="medium_bit_aligned" /> | `medium_bit_aligned` | As above, drawn edge 8 | 4 |
| <img :src="icon('large_bit_aligned')" :class="$style.cell" alt="large_bit_aligned" /> | `large_bit_aligned` | As above, drawn edge 12. The ticks carry the meaning. | 8 |
| <img :src="icon('full_cube')" :class="$style.cell" alt="full_cube" /> | `full_cube` | The whole reference block as a Selection solid | none |
| <img :src="icon('drawn_cube')" :class="$style.cell" alt="drawn_cube" /> | `drawn_cube` | Selection cuboid with a drag path between opposite corners | none |
| <img :src="icon('drawn_line')" :class="$style.cell" alt="drawn_line" /> | `drawn_line` | Thin Selection rod with a drag path along it | none |
| <img :src="icon('drawn_wall_thin')" :class="$style.cell" alt="drawn_wall_thin" /> | `drawn_wall_thin` | Upright Selection wall, 3 bits thick, with a drag path along its base | 3 |
| <img :src="icon('drawn_wall_medium')" :class="$style.cell" alt="drawn_wall_medium" /> | `drawn_wall_medium` | As above, 5 bits thick | 5 |
| <img :src="icon('drawn_wall_fat')" :class="$style.cell" alt="drawn_wall_fat" /> | `drawn_wall_fat` | As above, 7 bits thick | 7 |
| <img :src="icon('line_1')" :class="$style.cell" alt="line_1" /> | `line_1` | Selection column through the full block height, with a down arrow onto the hit face | 1 |
| <img :src="icon('line_2')" :class="$style.cell" alt="line_2" /> | `line_2` | As above, drawn thickness 5 | 2 |
| <img :src="icon('line_4')" :class="$style.cell" alt="line_4" /> | `line_4` | As above, drawn thickness 8 | 4 |
| <img :src="icon('line_8')" :class="$style.cell" alt="line_8" /> | `line_8` | As above, drawn thickness 12 | 8 |
| <img :src="icon('plane_1')" :class="$style.cell" alt="plane_1" /> | `plane_1` | Full-face Selection slab at the top of the Ghost block | 1 |
| <img :src="icon('plane_2')" :class="$style.cell" alt="plane_2" /> | `plane_2` | As above, drawn depth 5 | 2 |
| <img :src="icon('plane_4')" :class="$style.cell" alt="plane_4" /> | `plane_4` | As above, drawn depth 8 | 4 |
| <img :src="icon('plane_8')" :class="$style.cell" alt="plane_8" /> | `plane_8` | As above, drawn depth 12 | 8 |
| <img :src="icon('connected_plane_1')" :class="$style.cell" alt="connected_plane_1" /> | `connected_plane_1` | L-shaped Selection slab with a seed marker, next to a separate stone island that is not selected | 1 |
| <img :src="icon('connected_plane_2')" :class="$style.cell" alt="connected_plane_2" /> | `connected_plane_2` | As above, drawn depth 5 | 2 |
| <img :src="icon('connected_plane_4')" :class="$style.cell" alt="connected_plane_4" /> | `connected_plane_4` | As above, drawn depth 8 | 4 |
| <img :src="icon('connected_plane_8')" :class="$style.cell" alt="connected_plane_8" /> | `connected_plane_8` | As above, drawn depth 12 | 8 |
| <img :src="icon('connected_material_1')" :class="$style.cell" alt="connected_material_1" /> | `connected_material_1` | Solid stone block with an L-shaped Selection region raised from it and an up arrow | 1 |
| <img :src="icon('connected_material_2')" :class="$style.cell" alt="connected_material_2" /> | `connected_material_2` | As above, drawn height 5 | 2 |
| <img :src="icon('connected_material_4')" :class="$style.cell" alt="connected_material_4" /> | `connected_material_4` | As above, drawn height 8 | 4 |
| <img :src="icon('connected_material_8')" :class="$style.cell" alt="connected_material_8" /> | `connected_material_8` | As above, drawn height 12 | 8 |
| <img :src="icon('small_sphere')" :class="$style.cell" alt="small_sphere" /> | `small_sphere` | Shaded Selection sphere centred in the Ghost block, with an equator arc | 4 |
| <img :src="icon('medium_sphere')" :class="$style.cell" alt="medium_sphere" /> | `medium_sphere` | As above, drawn diameter 12 | 8 |
| <img :src="icon('large_sphere')" :class="$style.cell" alt="large_sphere" /> | `large_sphere` | As above, drawn diameter 16 | 16 |
| <img :src="icon('replace')" :class="$style.cell" alt="replace" /> | `replace` | Stone cube with a seed marker, an arrow, and a hatched amber cube | none |

## Background stress test

Every icon must stay legible on all of these backgrounds at both 64 px and
32 px. The last three stand in for what the radial menu can sit on in game.

<template v-for="bg in backgrounds" :key="bg.name">
  <div :class="$style.gallery" :style="{ background: bg.color }">
    <img v-for="id in showcase" :key="id" :src="icon(id)" :alt="id" width="64" height="64" />
    <img v-for="id in showcase" :key="id + '-32'" :src="icon(id)" :alt="id" width="32" height="32" />
  </div>
  <p :class="$style.caption">{{ bg.name }} <code>{{ bg.color }}</code></p>
</template>

## Construction template

[`construction_template.svg`](https://github.com/ChiselsAndBits/Website/blob/main/public/icons/chiselmodes/design/construction_template.svg)
contains the canvas, the 2 px clear edge, the reference block with its
bit grid on all three visible faces, the canvas centre, and the single-digit
badge zone. Start every new icon from it, and delete the construction layers
before export.

<div :class="$style.gallery" style="background: #FFFFFF; width: fit-content">
  <img :src="icon('construction_template')" alt="Construction template" width="256" height="256" />
</div>

## Review checklist

Before you submit an icon, check all of the following and include the
evidence in your pull request:

- [ ] The PNG is exactly 128 × 128, RGBA, with a transparent background, and named after the mode id.
- [ ] All geometry uses the shared projection and reference block. Nothing is rotated, mirrored, or drawn in perspective.
- [ ] Faces follow the light (top), mid (left), dark (right) order.
- [ ] Every element has the 4 px Ink outline and the 3 px Halo, and nothing touches the 2 px clear edge.
- [ ] Only palette colours are used, and each colour is used in its role.
- [ ] Sizes follow the legibility scale, and the badge matches the mode name.
- [ ] The icon is distinguishable from every other icon in its family **at 32 px**.
- [ ] Screenshots are attached on website light, website dark, Minecraft GUI gray, and a dark in-game background.
- [ ] The icon passes a grayscale check and a protanopia, deuteranopia, and tritanopia simulation (for example the
      [Coblis simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/) or browser
      DevTools' *Emulate vision deficiencies*). Every icon in the family still reads differently.
- [ ] The SVG source in `design/` and the exported PNG are both updated.
- [ ] The `summary.icon` frontmatter of the matching page in `docs/players/chiselmodes/` points to the PNG.
