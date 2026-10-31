---
title: Examples
order: 1
---

# API examples

These guides turn common mod integrations into small, reusable examples. Start with
[plugin setup](./plugin-setup.md), then pick the scenario that matches your mod.

| Scenario | Guide |
| --- | --- |
| Keep a decorative block's per-instance color when it becomes bits | [State variants](./state-variants.md) |
| Give variant bits names, tooltips, and the correct model inputs | [Client-side variants](./client-variants.md) |
| Add a tool mode with its own selection, preview, harvesting, and undo | [Custom chisel modes](./custom-chisel-modes.md) |
| Read materials, export a design, or generate a chiseled item | [Reading and creating designs](./designs.md) |
| Integrate a claim system without bypassing other protection mods | [Area permissions](./permissions.md) |

## Version and scope

The examples target the **Minecraft 26.1.2 / Java 25** API in the current C&B source.
Names such as `Identifier`, registry-friendly stream codecs, and item data components
are intentional; older releases may use different names or contracts. Match the API,
C&B runtime, Scena dependency, and Minecraft version in your development environment.

Java examples use the package `com.example.cbcompat`. Each labeled Java file is a
separate source file. Resource paths are relative to `src/main/resources` unless
stated otherwise. The decorative block and its normal Minecraft registration,
persistence, item placement, and networking belong to your mod; the variant guide
spells out the small interface that block must implement.

::: tip Keep the entire material identity
Use `BlockInformation`, not just `BlockState`, whenever you count, compare, serialize,
or move materials. Two bits can have the same block state but different variants.
:::

## Before shipping an integration

Try a dedicated server as well as an integrated client. For variants, test harvesting,
inventory separation, item rendering, reconnecting, saving/reloading, and rebuilding
a completely solid block. For modes, test previews, survival inventory accounting,
tool breakage, creative use, undo/redo, and permission denial.
