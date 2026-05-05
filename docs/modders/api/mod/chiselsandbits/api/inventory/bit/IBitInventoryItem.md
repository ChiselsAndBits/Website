--- 
title: IBitInventoryItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.inventory.bit](index.md)  
# Interface IBitInventoryItem  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBitInventoryItem</span></div>  

  

Represents an item which is a bit inventory.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IBitInventoryItemStack.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack</a></code></td><td><code><a href="#create(net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates a bit inventory which is represented by the<br>given itemstack which contains this item.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isFilteredPickupInventory(net.minecraft.world.item.ItemStack)" class="member-name-link">isFilteredPickupInventory</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if this items inventory is an inventory which is filtered, so that only bits which are already in the inventory are added when the player picks them up.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isPreferredPickupInventory(net.minecraft.world.item.ItemStack)" class="member-name-link">isPreferredPickupInventory</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if this items inventory is an inventory which should be preferred when bits are being picked up by the player.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IBitInventoryItemStack.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack</a></code></td><td><code><a href="#create(net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates a bit inventory which is represented by the<br>given itemstack which contains this item.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isFilteredPickupInventory(net.minecraft.world.item.ItemStack)" class="member-name-link">isFilteredPickupInventory</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if this items inventory is an inventory which is filtered, so that only bits which are already in the inventory are added when the player picks them up.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isPreferredPickupInventory(net.minecraft.world.item.ItemStack)" class="member-name-link">isPreferredPickupInventory</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if this items inventory is an inventory which should be preferred when bits are being picked up by the player.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IBitInventoryItemStack.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack</a></code></td><td><code><a href="#create(net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates a bit inventory which is represented by the<br>given itemstack which contains this item.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isFilteredPickupInventory(net.minecraft.world.item.ItemStack)" class="member-name-link">isFilteredPickupInventory</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if this items inventory is an inventory which is filtered, so that only bits which are already in the inventory are added when the player picks them up.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isPreferredPickupInventory(net.minecraft.world.item.ItemStack)" class="member-name-link">isPreferredPickupInventory</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if this items inventory is an inventory which should be preferred when bits are being picked up by the player.</div><br></td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="create(net.minecraft.world.item.ItemStack)">

:::tabs
== create
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IBitInventoryItemStack.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack</a></span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Creates a bit inventory which is represented by the
given itemstack which contains this item.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to create an inventory of.</dd>
<dt>Returns:</dt>
<dd>The bit inventory.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="isPreferredPickupInventory(net.minecraft.world.item.ItemStack)">

:::tabs
== isPreferredPickupInventory
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isPreferredPickupInventory</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Indicates if this items inventory is an inventory which should be preferred when bits are being picked up by the player.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to check for.</dd>
<dt>Returns:</dt>
<dd>True when preferred, false when not.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="isFilteredPickupInventory(net.minecraft.world.item.ItemStack)">

:::tabs
== isFilteredPickupInventory
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isFilteredPickupInventory</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Indicates if this items inventory is an inventory which is filtered, so that only bits which are already in the inventory are added when the player picks them up.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to check for.</dd>
<dt>Returns:</dt>
<dd>True when filtered, false when not.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

