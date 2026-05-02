---
title: Extrude 2
order: 26
summary:
  icon: /icons/chiselmodes/connected_material.png
---

# Extrude 2

![Extrude icon](/icons/chiselmodes/connected_material.png)

Selects connected same-material bits and extrudes/intrudes by 2 bits along the hit face.

## Details

| Property | Value                  |
|----------|------------------------|
| Mode id  | `connected_material_2` |
| Group    | Extrude (Connected Material) |
| Depth    | 2 bits                 |

## Usage

- **Left-click (chisel):** Removes connected same-material bits reachable within 2 bits of the face.
- **Right-click (place):** Fills connected air bits reachable within 2 bits of the face with the held material.

## Tips

> [!TIP]
> Good for removing slightly thicker connected surface coatings while staying material-aware.
