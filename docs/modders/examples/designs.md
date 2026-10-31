---
title: Reading and creating designs
order: 5
---

# Inspect, export, and generate designs

These are useful building blocks for an inspection tool, creative design
generator, recipe display, or server-admin command. They do not require access
to C&B's internal block entity or data component classes.

## Count materials without changing the world

`DesignExamples.java`:

```java
package com.example.cbcompat;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import mod.chiselsandbits.api.blockinformation.BlockInformation;
import mod.chiselsandbits.api.chiseling.eligibility.IEligibilityAnalysisResult;
import mod.chiselsandbits.api.chiseling.eligibility.IEligibilityManager;
import mod.chiselsandbits.api.item.bit.IBitItemManager;
import mod.chiselsandbits.api.multistate.accessor.IAccessorFactory;
import mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot;
import mod.chiselsandbits.api.variant.state.IStateVariantManager;
import net.minecraft.core.BlockPos;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.LevelAccessor;
import net.minecraft.world.level.block.state.BlockState;

public final class DesignExamples {
    private DesignExamples() {}

    public static Map<BlockInformation, Integer> countMaterials(LevelAccessor level, BlockPos pos) {
        Map<BlockInformation, Integer> counts = new HashMap<>();
        IAccessorFactory.getInstance().in(level, pos).stream()
                .filter(entry -> !entry.getBlockInformation().isAir())
                .forEach(entry -> counts.merge(entry.getBlockInformation(), 1, Integer::sum));
        return Map.copyOf(counts);
    }

    public static ItemStack exportBlock(LevelAccessor level, BlockPos pos) {
        IMultiStateSnapshot snapshot = IAccessorFactory.getInstance()
                .in(level, pos).createSnapshot();
        return snapshot.toItemStack().toBlockStack();
    }

    public static BlockInformation materialFromItem(BlockState state, ItemStack originalBlockItem) {
        return new BlockInformation(state, IStateVariantManager.getInstance()
                .getStateVariant(state, originalBlockItem));
    }

    public static ItemStack sampleBit(BlockInformation material) {
        requireMaterial(material);
        ItemStack result = IBitItemManager.getInstance().create(material, 1);
        if (result.isEmpty()) {
            throw new IllegalStateException("C&B did not create a bit for " + material);
        }
        return result;
    }

    public static ItemStack makeLowerSlab(
            LevelAccessor level, BlockPos source, BlockInformation material) {
        requireMaterial(material);
        IMultiStateSnapshot design = IAccessorFactory.getInstance()
                .in(level, source).createSnapshot();
        design.mutableStream().forEach(entry -> entry.clear());
        design.mutableStream()
                .filter(entry -> entry.getEndPoint().y() <= 0.5)
                .forEach(entry -> entry.overrideState(material));
        return design.toItemStack().toBlockStack();
    }

    public static BlockInformation plainMaterial(BlockState state) {
        return new BlockInformation(state, Optional.empty());
    }

    private static void requireMaterial(BlockInformation material) {
        IEligibilityAnalysisResult analysis = IEligibilityManager.getInstance().analyse(material);
        if (material.isAir() || !analysis.canBeChiseled() || analysis.isAlreadyChiseled()) {
            throw new IllegalArgumentException("Not a source material: "
                    + analysis.getReason().getString());
        }
    }
}
```

Run world-backed reads on the logical world's owning thread and only for loaded,
in-bounds positions that your caller is allowed to inspect. Validate packet or
command inputs before calling these helpers; do not let an untrusted client
select arbitrary distant chunks.

`in(level, pos)` covers one block. The current accessor adapts a supported solid
block into bit-sized entries; a non-chiselable block can produce no entries.
For a chiseled block the counts describe its material cells, not the number of
distinct Minecraft blocks. The map deliberately uses `BlockInformation` keys,
so different paint colors remain separate.

## Export is not harvesting

`exportBlock()` copies geometry to a chiseled item; it does not remove the source
or pay for its materials. Use it for privileged creative/admin features or
display-only previews, not an unrestricted survival duplication command.
Check for an empty/unsupported source in your caller and report that to the user.

For a pattern item instead, use
`snapshot.toItemStack().toPatternStack()`. The default conversion produces a
single-use pattern, not an automatically reusable one.

## Generate an item without editing a world

`makeLowerSlab()` uses a **single-block** source only to obtain a correctly sized
detached snapshot, clears it, and fills its bottom half. The source position is
not modified. Pass a known supported block as the source, not a machine or other
unsupported block whose accessor may be empty.

Despite the snapshot interface's name, its inherited mutator methods allow
editing this detached data. Do not assume it is a deeply read-only object.
Call `clone()` before editing a snapshot shared with another consumer.

Coordinates here are local block units: `0` to `1`, with `0.5` at half height.
Using each entry's end point ensures only cells wholly below that plane are
filled. The current normal resolution yields a slab with half a block's bits.
At the one-cell test resolution there are no whole cells below the plane.

`plainMaterial()` is appropriate for a genuinely ordinary block state such as
stone. For a painted block item, call `materialFromItem()` with the matching
block state and original block item so the provider can recover its variant.
For a live block, use the overload taking `Optional.ofNullable(blockEntity)`;
do not substitute an empty variant and silently lose its color.

## Persist a design using the API codecs

Use `BlockInformation.CODEC` / `STREAM_CODEC` for individual materials and
`IMultiStateSnapshot.CODEC` / `STREAM_CODEC` for complete designs. The snapshot
codec dispatches by registered snapshot type; the material codec dispatches
variants by provider. Decode only after those registrations exist.

In a registry-aware persistence context, supply registry-aware serialization
operations as required by the value's codec. Surface the `DataResult` error
instead of substituting an empty design. Avoid depending on the internal
layout of C&B's item components or manually writing its palette data.

## If you need a world-editing machine

Use `IMutatorFactory` for live world edits and a `try`-with-resources
`mutator.batch(changeTracker)` when the edit belongs to a player. That does not
automatically enforce your machine's claim checks, recipes, material payment,
chunk limits, or rollback. Call `IPermissionHandler.canManipulate` for the
**entire** target area before editing and implement the missing policies.

For player tool behavior, the
[custom mode example](./custom-chisel-modes.md) shows a complete removal path
through a chiseling context, including durability and overflow handling.
