--- 
title: IPlacementPreviewProvidingItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.placement](index.md)  
# Interface IPlacementPreviewProvidingItem  
**All Extended Interfaces:**  
[IWireframeProvidingItem](../item/wireframe/IWireframeProvidingItem.md), [IPlaceable](IPlaceable.md), [IPlacementProperties](IPlacementProperties.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPlacementPreviewProvidingItem</span><span class="extends-implements"><br/>  
extends <a href="../item/wireframe/IWireframeProvidingItem.html" title="interface in mod.chiselsandbits.api.item.wireframe">IWireframeProvidingItem</a>, <a href="IPlaceable.html" title="interface in mod.chiselsandbits.api.placement">IPlaceable</a>, <a href="IPlacementProperties.html" title="interface in mod.chiselsandbits.api.placement">IPlacementProperties</a></span></div>  

  

  

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
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepth(net.minecraft.world.item.ItemStack)" class="member-name-link">ignoreDepth</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepthForPlacement(net.minecraft.world.item.ItemStack,mod.chiselsandbits.api.placement.PlacementResult)" class="member-name-link">ignoreDepthForPlacement</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a>&nbsp;placementResult)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything for a given placement result.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepth(net.minecraft.world.item.ItemStack)" class="member-name-link">ignoreDepth</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepthForPlacement(net.minecraft.world.item.ItemStack,mod.chiselsandbits.api.placement.PlacementResult)" class="member-name-link">ignoreDepthForPlacement</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a>&nbsp;placementResult)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything for a given placement result.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepth(net.minecraft.world.item.ItemStack)" class="member-name-link">ignoreDepth</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepthForPlacement(net.minecraft.world.item.ItemStack,mod.chiselsandbits.api.placement.PlacementResult)" class="member-name-link">ignoreDepthForPlacement</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a>&nbsp;placementResult)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything for a given placement result.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.placement.<a href="IPlaceable.html" title="interface in mod.chiselsandbits.api.placement">IPlaceable</a>
<a href="IPlaceable.html#getPlacementResult(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getPlacementResult</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.placement.<a href="IPlacementProperties.html" title="interface in mod.chiselsandbits.api.placement">IPlacementProperties</a>
<a href="IPlacementProperties.html#overridesOccupiedBits(net.minecraft.world.item.ItemStack)">overridesOccupiedBits</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.wireframe.<a href="../item/wireframe/IWireframeProvidingItem.html" title="interface in mod.chiselsandbits.api.item.wireframe">IWireframeProvidingItem</a>
<a href="../item/wireframe/IWireframeProvidingItem.html#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getTargetedPosition</a>, <a href="../item/wireframe/IWireframeProvidingItem.html#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getWireFrame</a>, <a href="../item/wireframe/IWireframeProvidingItem.html#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getWireFrameColor</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="ignoreDepthForPlacement(net.minecraft.world.item.ItemStack,mod.chiselsandbits.api.placement.PlacementResult)">

:::tabs
== ignoreDepthForPlacement
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">ignoreDepthForPlacement</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack,
 <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a>&nbsp;placementResult)</span></div>
Returns whether to effectively ignore the depth buffer and render in front of everything for a given placement result.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>heldStack</code> - The stack to get depth logic for.</dd>
<dd><code>placementResult</code> - The placement result to get depth logic for.</dd>
<dt>Returns:</dt>
<dd>Whether depth is effectively ignored.</dd>
</dl>
:::


</section>

<section id="ignoreDepth(net.minecraft.world.item.ItemStack)">

:::tabs
== ignoreDepth
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">ignoreDepth</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack)</span></div>
Returns whether to effectively ignore the depth buffer and render in front of everything
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../item/wireframe/IWireframeProvidingItem.html#ignoreDepth(net.minecraft.world.item.ItemStack)">ignoreDepth</a></code>&nbsp;in interface&nbsp;<code><a href="../item/wireframe/IWireframeProvidingItem.html" title="interface in mod.chiselsandbits.api.item.wireframe">IWireframeProvidingItem</a></code></dd>
<dt>Parameters:</dt>
<dd><code>heldStack</code> - The stack to get depth logic for.</dd>
<dt>Returns:</dt>
<dd>Whether depth is effectively ignored.</dd>
</dl>
:::


</section>

:::::
  

