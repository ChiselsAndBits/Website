---
title: Extrude 1
order: 25
summary:
  icon: /icons/chiselmodes/connected_material.png
---

# Extrude 1

![Extrude icon](/icons/chiselmodes/connected_material.png)

Selects the connected region of the same material as the targeted bit and extrudes or intrudes it by 1 bit along the hit face direction. Air bits within the connected region are also included during placement.

## Details

| Property | Value                   |
|----------|-------------------------|
| Mode id  | `connected_material_1`  |
| Group    | Extrude (Connected Material) |
| Depth    | 1 bit                   |

## Usage

- **Left-click (chisel):** Removes all connected same-material bits reachable within 1 bit of the face.
- **Right-click (place):** Fills connected air bits reachable within 1 bit of the face with the held material.

## Tips

> [!TIP]
> Unlike Connected Plane, this mode also traverses air gaps within the region, making it behave more like flood-fill with material awareness.
