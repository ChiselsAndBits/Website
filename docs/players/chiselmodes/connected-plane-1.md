---
title: Connected Plane 1
order: 21
summary:
  icon: /icons/chiselmodes/connected_plane.png
---

# Connected Plane 1

![Connected Plane icon](/icons/chiselmodes/connected_plane.png)

Like the Plane mode, but only affects bits that are connected to the targeted bit on the face — non-contiguous regions are left untouched. Depth is 1 bit.

## Details

| Property | Value              |
|----------|--------------------|
| Mode id  | `connected_plane_1` |
| Group    | Connected Plane    |
| Depth    | 1 bit              |

## Usage

- **Left-click (chisel):** Flood-fills across the face from the targeted bit, removing all same-state connected bits at depth 1.
- **Right-click (place):** Flood-fills across the face, placing bits in all connected air slots at depth 1.

## Tips

> [!TIP]
> Ideal for removing a specific face region without affecting neighbouring areas of a different material.
