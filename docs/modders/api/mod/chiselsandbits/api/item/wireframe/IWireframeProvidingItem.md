--- 
title: IWireframeProvidingItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.wireframe](index.md)  
# Interface IWireframeProvidingItem  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWireframeProvidingItem</span></div>  

  

<div class="block">Represents an item which can provide a wireframe for different purposes,
 including rendering a preview.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Returns the position the wire frame should be rendered at.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrame</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;rayTraceResult)</code></td><td><div class="block">Provides access to the wire frame of the item.</div><br></td></tr>
  <tr><td><code>org.joml.Vector4f</code></td><td><code><a href="#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrameColor</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">The color to render the wireframe in.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepth(net.minecraft.world.item.ItemStack)" class="member-name-link">ignoreDepth</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Returns the position the wire frame should be rendered at.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrame</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;rayTraceResult)</code></td><td><div class="block">Provides access to the wire frame of the item.</div><br></td></tr>
  <tr><td><code>org.joml.Vector4f</code></td><td><code><a href="#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrameColor</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">The color to render the wireframe in.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepth(net.minecraft.world.item.ItemStack)" class="member-name-link">ignoreDepth</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Returns the position the wire frame should be rendered at.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrame</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;rayTraceResult)</code></td><td><div class="block">Provides access to the wire frame of the item.</div><br></td></tr>
  <tr><td><code>org.joml.Vector4f</code></td><td><code><a href="#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getWireFrameColor</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">The color to render the wireframe in.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#ignoreDepth(net.minecraft.world.item.ItemStack)" class="member-name-link">ignoreDepth</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">

:::tabs
== getWireFrame
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">getWireFrame</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack,
 net.minecraft.world.entity.player.Player&nbsp;player,
 net.minecraft.world.phys.BlockHitResult&nbsp;rayTraceResult)</span></div>
<div class="block">Provides access to the wire frame of the item.</div>
<dl class="notes">
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
<div class="member-signature"><span class="return-type">org.joml.Vector4f</span>&nbsp;<span class="element-name">getWireFrameColor</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack,
 net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</span></div>
<div class="block">The color to render the wireframe in.</div>
<dl class="notes">
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
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getTargetedPosition</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack,
 net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</span></div>
<div class="block">Returns the position the wire frame should be rendered at.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>heldStack</code> - The stack to get the position for.</dd>
<dd><code>playerEntity</code> - The entity that is rendering the wire frame.</dd>
<dd><code>blockRayTraceResult</code> - The block ray trace result for the current context.</dd>
<dt>Returns:</dt>
<dd>The position to render the wire frame.</dd>
</dl>
:::


</section>

<section id="ignoreDepth(net.minecraft.world.item.ItemStack)">

:::tabs
== ignoreDepth
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">ignoreDepth</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack)</span></div>
<div class="block">Returns whether to effectively ignore the depth buffer and render in front of everything</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>heldStack</code> - The stack to get depth logic for.</dd>
<dt>Returns:</dt>
<dd>Whether depth is effectively ignored.</dd>
</dl>
:::


</section>

:::::
  

