---
title: Extrude 8
order: 28
summary:
  icon: /icons/chiselmodes/connected_material.png
---

# Extrude 8

![Extrude icon](/icons/chiselmodes/connected_material.png)

Selects connected same-material bits and extrudes/intrudes by up to 8 bits along the hit face — the deepest extrude option.

## Details

| Property | Value                  |
|----------|------------------------|
| Mode id  | `connected_material_8` |
| Group    | Extrude (Connected Material) |
| Depth    | 8 bits                 |

## Usage

- **Left-click (chisel):** Removes connected same-material bits reachable within 8 bits of the face.
- **Right-click (place):** Fills connected air bits reachable within 8 bits of the face with the held material.

## Tips

> [!TIP]
> Half-block extrusion depth — perfect for deeply connected material regions that span much of the block's interior.
