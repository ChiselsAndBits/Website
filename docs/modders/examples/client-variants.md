---
title: Client-side variants
order: 3
---

# Render and describe a variant

The [paint variant](./state-variants.md) preserves RGB values on both sides.
Rendering and tooltips are separate client concerns. Keep these classes in your
mod's client source set, or otherwise behind its physical-client classloading
boundary.

## Expose a tooltip and model data

`PaintClientProvider.java` (client-only):

```java
package com.example.cbcompat;

import java.util.List;
import java.util.Locale;
import com.communi.suggestu.scena.core.client.models.data.IBlockModelData;
import com.communi.suggestu.scena.core.client.models.data.IModelDataBuilder;
import com.communi.suggestu.scena.core.client.models.data.IModelDataKey;
import mod.chiselsandbits.api.client.variant.state.IClientStateVariantProvider;
import mod.chiselsandbits.api.variant.state.IStateVariant;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.TooltipFlag;

public final class PaintClientProvider implements IClientStateVariantProvider {
    public static final IModelDataKey<Integer> RGB = IModelDataKey.create();

    @Override
    public IBlockModelData getBlockModelData(IStateVariant variant) {
        PaintVariant paint = requirePaint(variant);
        return IModelDataBuilder.create().withInitial(RGB, paint.rgb()).build();
    }

    @Override
    public void appendHoverText(
            IStateVariant variant, Item.TooltipContext context,
            List<Component> tooltip, TooltipFlag flags) {
        PaintVariant paint = requirePaint(variant);
        tooltip.add(Component.translatable(
                "examplemod.tooltip.paint",
                String.format(Locale.ROOT, "#%06X", paint.rgb())));
    }

    private static PaintVariant requirePaint(IStateVariant variant) {
        if (!(variant instanceof PaintVariant paint)) {
            throw new IllegalArgumentException("Expected paint variant");
        }
        return paint;
    }
}
```

In a separate client-only setup class, register it for the **same block** as the
common provider:

```java
IClientStateVariantManager.getInstance().registerStateVariantProvider(
        () -> ModBlocks.PAINTED_STONE.get(),
        new PaintClientProvider());
```

Import
`mod.chiselsandbits.api.client.variant.state.IClientStateVariantManager`.
Call that setup class from your plugin's `onClientConstruction()`. As in the
common registration, `ModBlocks` belongs to your mod. Register before the first
client variant query; this manager also resolves block suppliers lazily.

Add to `assets/examplemod/lang/en_us.json`:

```json
{
  "examplemod.tooltip.paint": "Pigment: %s"
}
```

The provider's tooltip method takes a `List<Component>`, even though the manager
has a newer consumer-based tooltip entrypoint. Implement the provider contract
shown above, not the manager's signature.

## Connect the color to your actual rendering path

**Model data is not a tint registration.** A custom model must explicitly read
the same `PaintClientProvider.RGB` key for that data to affect its output.
`IClientStateVariantManager.getBlockModelData(information)` exposes the data to
consumers, but registering a key alone does not ensure every C&B rendering path
will consume it.

In the current renderer, C&B also extracts the original block's model using a
fresh block entity created through `BlockInformation.newBlockEntity(...)`.
That method calls `PaintVariant.updateBlockEntity(...)`, which restores the
RGB value before model extraction. Make your original block's model/tint
integration able to read `PaintAccess` from this temporary entity, without
needing a live ticking world or casting the supplied block getter to `Level`.

For item rendering, the provider's `getItemStack()` returns an original block
item carrying `DYED_COLOR`. Your original block item's model and tint sources
must read that component too. A component on the stack does not change the
appearance of an arbitrary item model by itself.

Choose the approach supported by your actual model implementation and loader:

| Model input | Integration responsibility |
| --- | --- |
| Temporary block entity | Implement `updateBlockEntity`; make extraction and world tint queries work with the reconstructed entity. |
| Scena model data | Return the data through the client provider and ensure the consuming custom model requests and reads it. |
| Original block item | Return the correct component-bearing item from `getItemStack`; make its item model/tint sources use that component. |

Use the common `getName()` callback for a material's display name, the client
provider for extra tooltip lines, and the rendering inputs for appearance.
These are independent contracts.

## Rendering checks

Check a red and blue bit in the inventory, in-hand, as dropped items, and placed
in the **same** chiseled block. Check an exported chiseled block item too.
Reload resources and reconnect to a dedicated server. If only one presentation
is white, trace that presentation's input instead of changing the serialized
variant or registering the common provider on the client only.

Model extraction can run on worker threads. Keep providers stateless, use
immutable variant values, and never query or mutate a live world from
`getBlockModelData()`. Do not cache baked models or sprites forever across
resource reloads.
