---
title: Drawn Wall (Thin)
order: 10
summary:
  icon: /icons/chiselmodes/drawn_wall_1.png
---

# Drawn Wall (Thin)

![Drawn Wall Thin icon](/icons/chiselmodes/drawn_wall_1.png)

Drag to draw a wall along your path. The wall follows the drag path in the horizontal plane and extends vertically to match the drag height. This variant has a **1-bit** half-width (3 bits total across).

## Details

| Property      | Value              |
|---------------|--------------------|
| Mode id       | `drawn_wall_thin`  |
| Group         | Draw               |
| Extension width | 1 bit each side (3 bits total) |

## Usage

- **Hold Left-click + drag (chisel):** Draws the wall outline while held; releases to chisel the wall shape.
- **Hold Right-click + drag (place):** Draws the wall outline while held; releases to place bits in the wall shape.

> [!NOTE]
> The wall axis is determined by the face you first click — hitting a horizontal face produces a vertical wall, hitting a vertical face produces a horizontal one.

## Tips

> [!TIP]
> Ideal for thin dividers, fences, or narrow raised edges on your build.
