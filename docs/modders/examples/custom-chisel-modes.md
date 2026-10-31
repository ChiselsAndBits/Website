---
title: Custom chisel modes
order: 4
---

# Register a vertical-bore chisel mode

This mode removes a **one-bit-wide vertical column inside one block**. It is
useful for carving channels through decorative builds. Unlike a raw world edit,
it uses C&B's selection context, permission checks, change tracker, tool damage,
and bit inventory. It is deliberately **removal-only**: right-click reports an
error instead of placing free material.

The code uses API and Scena types only, not C&B's internal mode builders.

## 1. Register a mode, not a new registry

`ExampleModes.java`:

```java
package com.example.cbcompat;

import com.communi.suggestu.scena.core.registries.deferred.ICustomRegistrar;
import com.communi.suggestu.scena.core.registries.deferred.IRegistryObject;
import mod.chiselsandbits.api.chiseling.mode.IChiselMode;

public final class ExampleModes {
    private static final ICustomRegistrar<IChiselMode> MODES =
            ICustomRegistrar.create(IChiselMode.class, "examplemod");

    public static final IRegistryObject<IChiselMode> VERTICAL_BORE =
            MODES.register("vertical_bore", VerticalBoreMode::new);

    private ExampleModes() {}

    public static void register() {
        // Loading this class declares the deferred entries.
    }
}
```

Call `ExampleModes.register()` from your plugin's `onConstruction()`. Scena's
registrar is the same deferred mechanism used by C&B's built-in modes; it handles
assigning `examplemod:vertical_bore` to the entry. **Do not call `makeRegistry()`**:
C&B already owns the `IChiselMode` registry.

Do not call `VERTICAL_BORE.get()` in an early static initializer. Resolve it only
after registration has completed. Registered modes appear in the existing mode
menus; a new item or menu screen is not necessary.

## 2. Implement selection and harvesting

`VerticalBoreMode.java`:

```java
package com.example.cbcompat;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import com.communi.suggestu.scena.core.registries.AbstractCustomRegistryEntry;
import mod.chiselsandbits.api.axissize.CollisionType;
import mod.chiselsandbits.api.blockinformation.BlockInformation;
import mod.chiselsandbits.api.change.IChangeTrackerManager;
import mod.chiselsandbits.api.chiseling.IChiselingContext;
import mod.chiselsandbits.api.chiseling.mode.IChiselMode;
import mod.chiselsandbits.api.inventory.bit.IBitInventory;
import mod.chiselsandbits.api.inventory.management.IBitInventoryManager;
import mod.chiselsandbits.api.item.bit.IBitItemManager;
import mod.chiselsandbits.api.item.click.ClickProcessingState;
import mod.chiselsandbits.api.item.withmode.group.IToolModeGroup;
import mod.chiselsandbits.api.multistate.StateEntrySize;
import mod.chiselsandbits.api.multistate.accessor.IAreaAccessor;
import mod.chiselsandbits.api.multistate.mutator.world.IInWorldMutableStateEntryInfo;
import mod.chiselsandbits.api.multistate.mutator.world.IWorldAreaMutator;
import mod.chiselsandbits.api.util.IBatchMutation;
import mod.chiselsandbits.api.util.RayTracingUtils;
import mod.chiselsandbits.api.voxelshape.IVoxelShapeManager;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.HitResult;
import net.minecraft.world.phys.Vec3;
import net.minecraft.world.phys.shapes.Shapes;
import net.minecraft.world.phys.shapes.VoxelShape;

public final class VerticalBoreMode extends AbstractCustomRegistryEntry implements IChiselMode {
    @Override
    public ClickProcessingState onLeftClickBy(Player player, IChiselingContext context) {
        if (!selectColumn(player, context)) {
            return ClickProcessingState.DENIED;
        }
        if (context.isSimulation()) {
            return ClickProcessingState.DEFAULT;
        }
        context.setComplete();
        if (!(player instanceof ServerPlayer serverPlayer)) {
            return ClickProcessingState.ALLOW;
        }

        Optional<IWorldAreaMutator> selection = context.getMutator();
        if (selection.isEmpty()) {
            context.setError(Component.translatable("examplemod.bore.denied"));
            return ClickProcessingState.DENIED;
        }
        IWorldAreaMutator mutator = selection.get();
        Map<BlockInformation, Integer> harvested = new HashMap<>();
        try (IBatchMutation batch = mutator.batch(
                IChangeTrackerManager.getInstance().getChangeTracker(player))) {
            for (IInWorldMutableStateEntryInfo entry : mutator.inWorldMutableStream()
                    .filter(state -> !state.getBlockInformation().isAir()).toList()) {
                BlockInformation material = entry.getBlockInformation();
                int damage = context.tryDamageItemAndDoOrSetBrokenError(() -> {
                    entry.clear();
                    harvested.merge(material, 1, Integer::sum);
                });
                if (damage == 0) {
                    break;
                }
            }
        }

        if (harvested.isEmpty()) {
            context.setError(Component.translatable("examplemod.bore.empty"));
            return ClickProcessingState.DENIED;
        }
        if (!player.hasInfiniteMaterials()) {
            harvested.forEach((material, count) -> giveBits(serverPlayer, material, count));
        }
        return ClickProcessingState.ALLOW;
    }

    private static boolean selectColumn(Player player, IChiselingContext context) {
        context.resetMutator();
        context.clearStateFilter();
        HitResult result = RayTracingUtils.rayTracePlayer(player);
        if (!(result instanceof BlockHitResult hit) || result.getType() != HitResult.Type.BLOCK) {
            context.setError(Component.translatable("examplemod.bore.no_block"));
            return false;
        }

        StateEntrySize size = StateEntrySize.current();
        Vec3 inward = Vec3.atLowerCornerOf(hit.getDirection().getOpposite().getUnitVec3i())
                .scale(size.getSizePerHalfBit());
        Vec3 target = hit.getLocation().add(inward);
        BlockPos block = BlockPos.containing(target);
        if (context.getWorld().isOutsideBuildHeight(block)) {
            context.setError(Component.translatable("examplemod.bore.height"));
            return false;
        }

        Vec3 origin = Vec3.atLowerCornerOf(block);
        Vec3 local = size.roundDownToNearest(target.subtract(origin));
        double half = size.getSizePerHalfBit();
        double x = local.x() + half;
        double z = local.z() + half;
        context.include(block, new Vec3(x, half, z));
        context.include(block, new Vec3(x, 1.0 - half, z));
        if (context.getMutator().isEmpty()) {
            context.setError(Component.translatable("examplemod.bore.denied"));
            return false;
        }
        return true;
    }

    private static void giveBits(ServerPlayer player, BlockInformation material, int count) {
        IBitInventory inventory = IBitInventoryManager.getInstance().create(player);
        int inserted = Math.min(count, inventory.getMaxInsertAmount(material));
        if (inserted > 0) {
            inventory.insert(material, inserted);
        }
        int remaining = count - inserted;
        while (remaining > 0) {
            ItemStack stack = IBitItemManager.getInstance().create(material);
            if (stack.isEmpty()) {
                throw new IllegalStateException("Cannot create harvested bits for " + material);
            }
            int amount = Math.min(remaining, stack.getMaxStackSize());
            stack.setCount(amount);
            player.drop(stack, false);
            remaining -= amount;
        }
    }

    @Override
    public ClickProcessingState onRightClickBy(Player player, IChiselingContext context) {
        context.setError(Component.translatable("examplemod.bore.removal_only"));
        if (!context.isSimulation()) {
            context.setComplete();
        }
        return ClickProcessingState.DENIED;
    }

    @Override
    public void onStoppedLeftClicking(Player player, IChiselingContext context) {}

    @Override
    public void onStoppedRightClicking(Player player, IChiselingContext context) {}

    @Override
    public Optional<IAreaAccessor> getCurrentAccessor(IChiselingContext context) {
        return context.getMutator().map(mutator -> mutator);
    }

    @Override
    public VoxelShape getShape(IChiselingContext context) {
        return context.getMutator()
                .map(mutator -> IVoxelShapeManager.getInstance().get(mutator, CollisionType.ALL))
                .orElseGet(Shapes::empty);
    }

    @Override
    public Identifier getIcon() {
        return Identifier.fromNamespaceAndPath("chiselsandbits", "line");
    }

    @Override
    public Component getDisplayName() {
        return Component.translatable("examplemod.mode.vertical_bore");
    }

    @Override
    public Optional<IToolModeGroup> getGroup() {
        return Optional.empty();
    }
}
```

The example reuses C&B's line icon so it works without an additional texture.
Return your own icon identifier when providing your own icon assets.

Add these entries to `assets/examplemod/lang/en_us.json`:

```json
{
  "examplemod.mode.vertical_bore": "Vertical bore",
  "examplemod.bore.denied": "You cannot chisel this area.",
  "examplemod.bore.empty": "No chiselable material in this column.",
  "examplemod.bore.no_block": "Aim at a block.",
  "examplemod.bore.height": "The target is outside the build height.",
  "examplemod.bore.removal_only": "Vertical bore only removes bits."
}
```

## Why these details matter

Selection runs **before** the simulation check, so previews and validity checks
describe the same column as real use. The face offset moves the hit half a bit
inside the block; using the exact face coordinate can select the neighboring
block. Grid rounding happens relative to the containing block, including at
negative world coordinates. No fixed `16` or `4096` is needed.

Only the server mutates the world or inventory. `getMutator()` is checked after
selection because the context can reject it through the permission handler.
The mutator exposes only supported material entries; air is excluded before
damaging tools or counting drops.

The batch records the edit in the player's change tracker and is closed even
on failure. It is **not a transaction** that rolls back inventory or arbitrary
side effects. Harvest counts are accumulated only inside the successful
damage callback. If the tool breaks mid-column, only removed bits are returned.
Survival overflow becomes dropped stacks rather than disappearing; creative
use removes material without generating drops.

The mode is a registry singleton: never store a player's selection on its
fields. Multi-click modes should use `IChiselingContext` metadata with registered
`IMetadataKey` entries and a suitable snapshot implementation. The stop-click
callbacks are documented as currently unused, so do not depend on them to
finish an operation.

`getShape()` uses C&B's cached voxel-shape manager. For this rectangular
selection, `CollisionType.ALL` describes the selected volume, including holes.
Do not rebuild large voxel shapes every rendered frame.

::: warning Filters are not automatically enforced everywhere
The current context stores `setStateFilter(...)` but does not wrap every
mutator operation in that filter. If your mode uses a non-rectangular selection,
apply the same predicate to preview/accessor behavior, extraction counts, and
every modification stream yourself. In particular, do not assume delegating to
an arbitrary built-in mode will enforce your filter on both click paths.
:::

## Adding placement

A placement mode must obtain the held bit's **whole `BlockInformation`**, count
only empty eligible target entries, check `IBitInventory.canExtract`, and extract
exactly the amount placed (except with infinite materials). Check permissions
and build height before charging the inventory. Keep simulation side-effect
free and never overwrite occupied material merely to avoid handling
`SpaceOccupiedException`.

If a mode requires a held bit for all its operations, override
`requiresPlaceableEditStack()` to return `true`; that excludes it from ordinary
chisel mode menus. This removal-only example leaves the default `false`.

## Verify the behavior

On a solid block, a click removes `StateEntrySize.current().getBitsPerBlockSide()`
bits, all at the targeted X/Z grid location and all inside that block. Repeating
the click on an empty column must not yield bits or spend durability.

Test top and side faces, negative X/Z coordinates, the lowest and highest legal
blocks, a mixed-variant block, a nearly broken chisel, full bit bags and inventory,
creative mode, undo/redo, and a denied claim. The world edit should be one tracked
operation. C&B's world change tracking is not a general inventory transaction;
check the target release's undo semantics separately from survival accounting.
