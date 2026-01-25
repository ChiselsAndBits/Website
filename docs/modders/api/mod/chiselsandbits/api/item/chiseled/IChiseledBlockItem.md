--- 
title: IChiseledBlockItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.chiseled](index.md)  
# Interface IChiseledBlockItem  
**All Extended Interfaces:**  
[IMultiStateItem](../multistate/IMultiStateItem.md), [IWireframeProvidingItem](../wireframe/IWireframeProvidingItem.md), [IWithModeItem\<IModificationOperation\>](../withmode/IWithModeItem.md), [IPlaceable](../placement/IPlaceable.md), [IPlacementPreviewProvidingItem](../placement/IPlacementPreviewProvidingItem.md), [IPlacementProperties](../placement/IPlacementProperties.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiseledBlockItem</span><span class="extends-implements"><br/>  
extends <a href="../multistate/IMultiStateItem.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItem</a>, <a href="../../placement/IPlacementPreviewProvidingItem.html" title="interface in mod.chiselsandbits.api.placement">IPlacementPreviewProvidingItem</a>, <a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a>&lt;<a href="../../modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a>&gt;</span></div>  

  

<div class="block">Represents items which represent a broken chiseled block.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Returns the position the wire frame should be rendered at.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrame</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;rayTraceResult)</code></td><td><div class="block">Provides access to the wire frame of the item.</div><br></td></tr>
  <tr><td><code>default org.joml.Vector4f</code></td><td><code><a href="#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrameColor</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">The color to render the wireframe in.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#overridesOccupiedBits(net.minecraft.world.item.ItemStack)" class="member-name-link">overridesOccupiedBits</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Invoked to determine whether this replaces non-air bits of blocks, or only replaces air bits.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Returns the position the wire frame should be rendered at.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrame</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;rayTraceResult)</code></td><td><div class="block">Provides access to the wire frame of the item.</div><br></td></tr>
  <tr><td><code>default org.joml.Vector4f</code></td><td><code><a href="#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrameColor</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">The color to render the wireframe in.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#overridesOccupiedBits(net.minecraft.world.item.ItemStack)" class="member-name-link">overridesOccupiedBits</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Invoked to determine whether this replaces non-air bits of blocks, or only replaces air bits.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Returns the position the wire frame should be rendered at.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrame</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;rayTraceResult)</code></td><td><div class="block">Provides access to the wire frame of the item.</div><br></td></tr>
  <tr><td><code>default org.joml.Vector4f</code></td><td><code><a href="#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrameColor</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">The color to render the wireframe in.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#overridesOccupiedBits(net.minecraft.world.item.ItemStack)" class="member-name-link">overridesOccupiedBits</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Invoked to determine whether this replaces non-air bits of blocks, or only replaces air bits.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.multistate.<a href="../multistate/IMultiStateItem.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItem</a>
<a href="../multistate/IMultiStateItem.html#createItemStack(net.minecraft.world.item.ItemStack)">createItemStack</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.placement.<a href="../../placement/IPlaceable.html" title="interface in mod.chiselsandbits.api.placement">IPlaceable</a>
<a href="../../placement/IPlaceable.html#getPlacementResult(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getPlacementResult</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.placement.<a href="../../placement/IPlacementPreviewProvidingItem.html" title="interface in mod.chiselsandbits.api.placement">IPlacementPreviewProvidingItem</a>
<a href="../../placement/IPlacementPreviewProvidingItem.html#ignoreDepth(net.minecraft.world.item.ItemStack)">ignoreDepth</a>, <a href="../../placement/IPlacementPreviewProvidingItem.html#ignoreDepthForPlacement(net.minecraft.world.item.ItemStack,mod.chiselsandbits.api.placement.PlacementResult)">ignoreDepthForPlacement</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a>
<a href="../withmode/IWithModeItem.html#getMode(net.minecraft.world.item.ItemStack)">getMode</a>, <a href="../withmode/IWithModeItem.html#getPossibleModes()">getPossibleModes</a>, <a href="../withmode/IWithModeItem.html#requiresUpdateOnClosure()">requiresUpdateOnClosure</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,int)">setMode</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,M)">setMode</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">

:::tabs
== getWireFrame
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">getWireFrame</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack,
 net.minecraft.world.entity.player.Player&nbsp;player,
 net.minecraft.world.phys.BlockHitResult&nbsp;rayTraceResult)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../wireframe/IWireframeProvidingItem.html#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">IWireframeProvidingItem</a></code></span></div>
<div class="block">Provides access to the wire frame of the item.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../wireframe/IWireframeProvidingItem.html#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getWireFrame</a></code>&nbsp;in interface&nbsp;<code><a href="../wireframe/IWireframeProvidingItem.html" title="interface in mod.chiselsandbits.api.item.wireframe">IWireframeProvidingItem</a></code></dd>
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to get the wire frame from.</dd>
<dd><code>player</code> - The player to get the wire frame for.</dd>
<dd><code>rayTraceResult</code> - The ray trace result of the current context.</dd>
<dt>Returns:</dt>
<dd>The VoxelShape for the wire frame.</dd>
</dl>
:::


</section>

<section id="getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">

:::tabs
== getWireFrameColor
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">org.joml.Vector4f</span>&nbsp;<span class="element-name">getWireFrameColor</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack,
 net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../wireframe/IWireframeProvidingItem.html#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">IWireframeProvidingItem</a></code></span></div>
<div class="block">The color to render the wireframe in.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../wireframe/IWireframeProvidingItem.html#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getWireFrameColor</a></code>&nbsp;in interface&nbsp;<code><a href="../wireframe/IWireframeProvidingItem.html" title="interface in mod.chiselsandbits.api.item.wireframe">IWireframeProvidingItem</a></code></dd>
<dt>Parameters:</dt>
<dd><code>heldStack</code> - The stack to get the wire frame color for.</dd>
<dd><code>playerEntity</code> - The entity that is rendering the wire frame color.</dd>
<dd><code>blockRayTraceResult</code> - The block ray trace result for the current context.</dd>
<dt>Returns:</dt>
<dd>An RGB (XYZ) Vector with the color.</dd>
</dl>
:::


</section>

<section id="getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">

:::tabs
== getTargetedPosition
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getTargetedPosition</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack,
 net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../wireframe/IWireframeProvidingItem.html#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">IWireframeProvidingItem</a></code></span></div>
<div class="block">Returns the position the wire frame should be rendered at.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../wireframe/IWireframeProvidingItem.html#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getTargetedPosition</a></code>&nbsp;in interface&nbsp;<code><a href="../wireframe/IWireframeProvidingItem.html" title="interface in mod.chiselsandbits.api.item.wireframe">IWireframeProvidingItem</a></code></dd>
<dt>Parameters:</dt>
<dd><code>heldStack</code> - The stack to get the position for.</dd>
<dd><code>playerEntity</code> - The entity that is rendering the wire frame.</dd>
<dd><code>blockRayTraceResult</code> - The block ray trace result for the current context.</dd>
<dt>Returns:</dt>
<dd>The position to render the wire frame.</dd>
</dl>
:::


</section>

<section id="overridesOccupiedBits(net.minecraft.world.item.ItemStack)">

:::tabs
== overridesOccupiedBits
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">overridesOccupiedBits</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../placement/IPlacementProperties.html#overridesOccupiedBits(net.minecraft.world.item.ItemStack)">IPlacementProperties</a></code></span></div>
<div class="block">Invoked to determine whether this replaces non-air bits of blocks, or only replaces air bits.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../placement/IPlacementProperties.html#overridesOccupiedBits(net.minecraft.world.item.ItemStack)">overridesOccupiedBits</a></code>&nbsp;in interface&nbsp;<code><a href="../../placement/IPlacementProperties.html" title="interface in mod.chiselsandbits.api.placement">IPlacementProperties</a></code></dd>
</dl>
:::


</section>

:::::
  

