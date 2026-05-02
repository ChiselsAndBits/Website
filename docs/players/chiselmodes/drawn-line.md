---
title: Drawn Line
order: 9
summary:
  icon: /icons/chiselmodes/drawn_line.png
---

# Drawn Line

![Drawn Line icon](/icons/chiselmodes/drawn_line.png)

Click and drag between two points to edit a 1-bit-wide line following the shortest path between them using a 3D line-drawing algorithm.

## Details

| Property  | Value        |
|-----------|--------------|
| Mode id   | `drawn_line` |
| Group     | Draw         |
| Selection | Drag-defined line (1 bit thick) |

## Usage

- **Hold Left-click + drag (chisel):** Sets the start anchor, then removes all bits along the traced line on release.
- **Hold Right-click + drag (place):** Sets the start anchor, then fills air bits along the traced line on release.

> [!NOTE]
> This is a multi-click mode — hold the mouse button while dragging, then release to apply.

## Tips

> [!TIP]
> Great for drawing diagonal grooves, pipes, or wire-like details through a block.
