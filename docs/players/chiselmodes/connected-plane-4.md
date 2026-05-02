---
title: Connected Plane 4
order: 23
summary:
  icon: /icons/chiselmodes/connected_plane.png
---

# Connected Plane 4

![Connected Plane icon](/icons/chiselmodes/connected_plane.png)

Connected Plane flood-fill extended to 4 bits of depth from the hit surface.

## Details

| Property | Value               |
|----------|---------------------|
| Mode id  | `connected_plane_4` |
| Group    | Connected Plane     |
| Depth    | 4 bits              |

## Usage

- **Left-click (chisel):** Removes all connected same-state bits on the face up to 4 bits deep.
- **Right-click (place):** Fills connected air bits on the face up to 4 bits deep with the held material.

## Tips

> [!TIP]
> Quarter-block depth — useful for removing thicker surface layers of a connected material region.
