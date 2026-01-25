--- 
title: IBitBagAcceptingBlock
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.bitbag](index.md)  
# Interface IBitBagAcceptingBlock  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBitBagAcceptingBlock</span></div>  

  

<div class="block">Represents a block which can accept a bit bags interaction.</div>
  

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
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#onBitBagInteraction(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">onBitBagInteraction</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;bitBagStack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked when a bit bag interaction is performed against a given block.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#onBitBagInteraction(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">onBitBagInteraction</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;bitBagStack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked when a bit bag interaction is performed against a given block.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#onBitBagInteraction(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">onBitBagInteraction</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;bitBagStack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked when a bit bag interaction is performed against a given block.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="onBitBagInteraction(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">

:::tabs
== onBitBagInteraction
<div class="member-signature"><span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">onBitBagInteraction</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;bitBagStack,
 net.minecraft.world.entity.player.Player&nbsp;player,
 net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</span></div>
<div class="block">Invoked when a bit bag interaction is performed against a given block.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bitBagStack</code> - The bit bag stack.</dd>
<dd><code>player</code> - The player performing the action.</dd>
<dd><code>blockRayTraceResult</code> - The ray trace result.</dd>
</dl>
:::


</section>

:::::
  

