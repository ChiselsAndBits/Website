--- 
title: IPlacementProperties
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.placement](index)  
# Interface IPlacementProperties  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPlacementProperties</span></div>  

  

Provides placement behavior options for an item.  

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
  <tr><td><code>default boolean</code></td><td><code><a href="#overridesOccupiedBits(net.minecraft.world.item.ItemStack)" class="member-name-link">overridesOccupiedBits</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Invoked to determine whether this replaces non-air bits of blocks, or only replaces air bits.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#overridesOccupiedBits(net.minecraft.world.item.ItemStack)" class="member-name-link">overridesOccupiedBits</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Invoked to determine whether this replaces non-air bits of blocks, or only replaces air bits.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#overridesOccupiedBits(net.minecraft.world.item.ItemStack)" class="member-name-link">overridesOccupiedBits</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack)</code></td><td><div class="block">Invoked to determine whether this replaces non-air bits of blocks, or only replaces air bits.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="overridesOccupiedBits(net.minecraft.world.item.ItemStack)">

:::tabs
== overridesOccupiedBits
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">overridesOccupiedBits</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack)</span></div>
Invoked to determine whether this replaces non-air bits of blocks, or only replaces air bits.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>heldStack</code> - item stack whose placement behavior is being checked</dd>
<dt>Returns:</dt>
<dd><code>true</code> when placement may replace occupied bits</dd>
</dl>
</div>
:::


</section>

:::::
  

