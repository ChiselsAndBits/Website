--- 
title: IPlaceable
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.placement](index)  
# Interface IPlaceable  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPlaceable</span></div>  

  

  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#getPlacementResult(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getPlacementResult</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked to determine the result of attempting actual placement in the world.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#getPlacementResult(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getPlacementResult</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked to determine the result of attempting actual placement in the world.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#getPlacementResult(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getPlacementResult</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked to determine the result of attempting actual placement in the world.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getPlacementResult(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">

:::tabs
== getPlacementResult
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">getPlacementResult</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack,
 net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</span></div>
Invoked to determine the result of attempting actual placement in the world.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>heldStack</code> - The stack to get the color for.</dd>
<dd><code>playerEntity</code> - The entity that is rendering with the color.</dd>
<dd><code>blockRayTraceResult</code> - The block ray trace result for the current context.</dd>
<dt>Returns:</dt>
<dd>The simulated action result of placement</dd>
</dl>
</div>
:::


</section>

:::::
  

