---
title: State variants
order: 2
---

# Preserve a painted block as bits

Suppose your mod has a full-cube decorative block whose block entity holds a
24-bit RGB color. A `BlockState` alone cannot distinguish a red instance from a
blue instance. A state variant preserves that extra material identity through
chiseling, bit inventories, saves, networking, and full-block reconstruction.

This example deliberately stores **only appearance**, not an inventory, owner,
energy buffer, running machine, or reference to a live block entity.

::: warning A provider opts a material into chiseling
In the current implementation, a `BlockInformation` with a variant is accepted by
the eligibility manager before the normal block-behavior checks. Register only for
blocks that are safe to turn into passive micro-materials. A variant does not make
each bit a functioning instance of your original block entity.
:::

## 1. Define your block's integration boundary

`PaintAccess.java`:

```java
package com.example.cbcompat;

public interface PaintAccess {
    int getRgb();

    void setRgb(int rgb);
}
```

Your decorative block entity implements this interface. `setRgb` updates its
stored color and marks it dirty. If attached to a real world, it also performs
your mod's normal client synchronization/model refresh. It must also work on a
newly constructed block entity **without a level**: C&B can construct temporary
entities for model extraction and color queries.

The block's normal item uses Minecraft's `DataComponents.DYED_COLOR` with a
`DyedItemColor` value. Your block-item placement code must read that component
into the block entity; your normal block drops/pick-block code must write it back.
Missing color means white (`0xFFFFFF`). Those are host-mod responsibilities, not
behavior automatically added by C&B.

## 2. Make an immutable value

`PaintVariant.java`:

```java
package com.example.cbcompat;

import com.mojang.serialization.Codec;
import com.mojang.serialization.MapCodec;
import mod.chiselsandbits.api.variant.state.IStateVariant;
import mod.chiselsandbits.api.variant.state.IStateVariantProvider;
import net.minecraft.network.RegistryFriendlyByteBuf;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.world.level.block.entity.BlockEntity;

public record PaintVariant(int rgb) implements IStateVariant {
    public static final int DEFAULT_RGB = 0xFFFFFF;

    public static final MapCodec<PaintVariant> MAP_CODEC =
            Codec.intRange(0, 0xFFFFFF).fieldOf("rgb")
                    .xmap(PaintVariant::new, PaintVariant::rgb);

    public static final StreamCodec<RegistryFriendlyByteBuf, PaintVariant> STREAM_CODEC =
            new StreamCodec<>() {
                @Override
                public PaintVariant decode(RegistryFriendlyByteBuf buffer) {
                    return new PaintVariant(buffer.readInt());
                }

                @Override
                public void encode(RegistryFriendlyByteBuf buffer, PaintVariant value) {
                    buffer.writeInt(value.rgb());
                }
            };

    public PaintVariant {
        if (rgb < 0 || rgb > 0xFFFFFF) {
            throw new IllegalArgumentException("Expected 24-bit RGB, got " + rgb);
        }
    }

    @Override
    public IStateVariantProvider provider() {
        return PaintProvider.INSTANCE;
    }

    @Override
    public PaintVariant createSnapshot() {
        return this;
    }

    @Override
    public int compareTo(IStateVariant other) {
        if (!(other instanceof PaintVariant paint)) {
            throw new IllegalArgumentException("Cannot compare different variant types");
        }
        return Integer.compare(rgb, paint.rgb);
    }

    @Override
    public void updateBlockEntity(BlockEntity blockEntity) {
        if (!(blockEntity instanceof PaintAccess paint)) {
            throw new IllegalArgumentException("Paint variant needs a PaintAccess block entity");
        }
        paint.setRgb(rgb);
    }
}
```

A record gives value-based `equals` and `hashCode`, so identical colors stack and
different colors remain separate. `compareTo` agrees with equality within this
variant type; `BlockInformation` orders different variant classes separately.
Returning `this` from `createSnapshot()` is safe because this value is immutable.
Do not keep mutable tags, item stacks, arrays, worlds, or entities in a variant.

The map codec stores only the payload. C&B's `IStateVariant.CODEC` dispatches using
`provider()` and the provider's registered name; its stream codec does the same
for networking. Both codecs must reconstruct the same value. The constructor
also rejects invalid values received over the network.

## 3. Implement all provider paths

`PaintProvider.java`:

```java
package com.example.cbcompat;

import java.util.Collection;
import java.util.List;
import java.util.Optional;
import com.communi.suggestu.scena.core.fluid.FluidInformation;
import com.mojang.serialization.MapCodec;
import mod.chiselsandbits.api.blockinformation.BlockInformation;
import mod.chiselsandbits.api.variant.state.IStateVariant;
import mod.chiselsandbits.api.variant.state.IStateVariantProvider;
import net.minecraft.core.BlockPos;
import net.minecraft.core.component.DataComponents;
import net.minecraft.network.RegistryFriendlyByteBuf;
import net.minecraft.network.chat.Component;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.resources.Identifier;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.component.DyedItemColor;
import net.minecraft.world.level.LevelAccessor;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.material.FluidState;

public final class PaintProvider implements IStateVariantProvider {
    public static final PaintProvider INSTANCE = new PaintProvider();
    private static final Identifier ID =
            Identifier.fromNamespaceAndPath("examplemod", "paint");

    private PaintProvider() {}

    @Override
    public Identifier getRegistryName() {
        return ID;
    }

    @Override
    public Optional<IStateVariant> getStateVariant(
            BlockState state, Optional<BlockEntity> blockEntity) {
        if (blockEntity.isEmpty()) {
            return Optional.of(new PaintVariant(PaintVariant.DEFAULT_RGB));
        }
        if (!(blockEntity.get() instanceof PaintAccess paint)) {
            throw new IllegalArgumentException("Registered paint block lacks PaintAccess");
        }
        return Optional.of(new PaintVariant(paint.getRgb()));
    }

    @Override
    public Optional<IStateVariant> getStateVariant(BlockState state, ItemStack stack) {
        DyedItemColor color = stack.getOrDefault(
                DataComponents.DYED_COLOR, new DyedItemColor(PaintVariant.DEFAULT_RGB));
        return Optional.of(new PaintVariant(color.rgb()));
    }

    @Override
    public Optional<IStateVariant> getStateVariant(FluidState state) {
        return Optional.empty();
    }

    @Override
    public Optional<IStateVariant> getStateVariant(FluidInformation fluid) {
        return Optional.empty();
    }

    @Override
    public Collection<? extends IStateVariant> getAllDefaultVariants(BlockState state) {
        return List.of(
                new PaintVariant(PaintVariant.DEFAULT_RGB),
                new PaintVariant(0xCC3333),
                new PaintVariant(0x3366CC));
    }

    @Override
    public Optional<ItemStack> getItemStack(BlockInformation information) {
        PaintVariant paint = requirePaint(information);
        ItemStack stack = new ItemStack(information.blockState().getBlock());
        stack.set(DataComponents.DYED_COLOR, new DyedItemColor(paint.rgb()));
        return Optional.of(stack);
    }

    @Override
    public Optional<FluidInformation> getFluidInformation(IStateVariant variant, long amount) {
        return Optional.empty();
    }

    @Override
    public Optional<Component> getName(BlockInformation information) {
        PaintVariant paint = requirePaint(information);
        return Optional.of(Component.translatable(
                "examplemod.material.painted",
                information.blockState().getBlock().getName(),
                String.format(java.util.Locale.ROOT, "#%06X", paint.rgb())));
    }

    @Override
    public MapCodec<PaintVariant> mapCodec() {
        return PaintVariant.MAP_CODEC;
    }

    @Override
    public StreamCodec<RegistryFriendlyByteBuf, PaintVariant> streamCodec() {
        return PaintVariant.STREAM_CODEC;
    }

    @Override
    public void setFullBlock(LevelAccessor level, BlockPos pos, BlockInformation information) {
        PaintVariant paint = requirePaint(information);
        BlockState state = information.blockState();
        level.setBlock(pos, state, Block.UPDATE_ALL);
        BlockEntity blockEntity = level.getBlockEntity(pos);
        if (!(blockEntity instanceof PaintAccess target)) {
            throw new IllegalStateException("Paint block entity missing at " + pos);
        }
        target.setRgb(paint.rgb());
    }

    @Override
    public Optional<Integer> getBeaconColorMultiplier(
            BlockInformation information, LevelReader level, BlockPos pos, BlockPos beaconPos) {
        return Optional.empty();
    }

    private static PaintVariant requirePaint(BlockInformation information) {
        IStateVariant variant = information.variant().orElseThrow(
                () -> new IllegalArgumentException("Missing paint variant"));
        if (!(variant instanceof PaintVariant paint)) {
            throw new IllegalArgumentException("Expected paint variant");
        }
        return paint;
    }
}
```

The manager routes calls by block, so register this provider only for your
paint-compatible blocks. The overload without a live block entity intentionally
returns the default white variant. It is used by callers that enumerate ordinary
block states; returning no variant there can leave the block ineligible.

The three default colors are a **curated palette**, not every possible RGB value.
Avoid enumerating millions of variants for creative lists. Unsupported fluid
paths and the opaque block's beacon-tint query return `Optional.empty()` because
there is deliberately no such representation/effect. For transparent colored
materials, implement the beacon callback using the color format expected by
your target Minecraft version.

`getItemStack()` returns the **original full-block item**, not a C&B bit. To make
bits, use `IBitItemManager` as shown in [the design examples](./designs.md).

## 4. Register early, on both physical sides

In the [plugin's](./plugin-setup.md) `onConstruction()`:

```java
IStateVariantManager.getInstance().registerProvider(
        PaintProvider.INSTANCE,
        () -> ModBlocks.PAINTED_STONE.get());
```

Import `mod.chiselsandbits.api.variant.state.IStateVariantManager`.
`ModBlocks.PAINTED_STONE` is **your mod's deferred block registration**, not a
C&B class. The supplier must return a block whose block entity implements
`PaintAccess` and whose normal item carries the color component.

Register before any variant queries, on client and dedicated server alike. The
current manager resolves pending block suppliers on first use; it is not a
late-registration or hot-reload registry. Provider names must be unique.
There is one effective provider per block, so coordinate integrations rather than
registering competing providers for the same block.

`assets/examplemod/lang/en_us.json`:

```json
{
  "examplemod.material.painted": "%s (%s)"
}
```

## 5. Exercise the complete round trip

Place red and blue blocks, chisel both, and confirm their bits do not merge.
Place enough red bits to fill an entire block and verify its original block type
and red block entity return. Save/reload, reconnect to a dedicated server, and
repeat with the color absent from the item (white).

Also test the value contracts in your mod's test harness:

```java
PaintVariant red = new PaintVariant(0xCC3333);
PaintVariant sameRed = new PaintVariant(0xCC3333);
PaintVariant blue = new PaintVariant(0x3366CC);
assert red.equals(sameRed);
assert red.hashCode() == sameRed.hashCode();
assert red.compareTo(sameRed) == 0;
assert !red.equals(blue);
assert red.createSnapshot().equals(red);
```

Round-trip both `PaintVariant.MAP_CODEC.codec()` and
`PaintVariant.STREAM_CODEC`, then the dispatched `BlockInformation` codecs with
the provider registered. Test invalid RGB values, missing providers, and a
temporary block entity without a level. Enable Java assertions if using the
assertions above outside your normal test framework.

Continue with [client-side variants](./client-variants.md) to expose the color to
models and tooltips; serializing a color does not automatically tint a mesh.
