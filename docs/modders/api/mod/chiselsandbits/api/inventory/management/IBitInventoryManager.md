--- 
title: IBitInventoryManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.inventory.management](index)  
# Interface IBitInventoryManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBitInventoryManager</span></div>  

  

Manager which deals with bit inventories.  

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
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(java.lang.Object)" class="member-name-link">create</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;target)</code></td><td><div class="block">Creates a new bit inventory wrapping the given <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(net.minecraft.world.Container)" class="member-name-link">create</a><wbr>(net.minecraft.world.Container&nbsp;inventory)</code></td><td><div class="block">Creates a new bit inventory wrapping the given inventory.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(net.minecraft.world.entity.player.Player)" class="member-name-link">create</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Creates a new bit inventory wrapping the inventory of the player.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventoryItemStack.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack</a></code></td><td><code><a href="#create(net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates a new bit inventory wrapping the given itemstack.</div><br></td></tr>
  <tr><td><code>static <a href="IBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.management">IBitInventoryManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the bit inventory manager.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.management">IBitInventoryManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the bit inventory manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(java.lang.Object)" class="member-name-link">create</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;target)</code></td><td><div class="block">Creates a new bit inventory wrapping the given <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(net.minecraft.world.Container)" class="member-name-link">create</a><wbr>(net.minecraft.world.Container&nbsp;inventory)</code></td><td><div class="block">Creates a new bit inventory wrapping the given inventory.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(net.minecraft.world.entity.player.Player)" class="member-name-link">create</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Creates a new bit inventory wrapping the inventory of the player.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventoryItemStack.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack</a></code></td><td><code><a href="#create(net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates a new bit inventory wrapping the given itemstack.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(java.lang.Object)" class="member-name-link">create</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;target)</code></td><td><div class="block">Creates a new bit inventory wrapping the given <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(net.minecraft.world.Container)" class="member-name-link">create</a><wbr>(net.minecraft.world.Container&nbsp;inventory)</code></td><td><div class="block">Creates a new bit inventory wrapping the given inventory.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></code></td><td><code><a href="#create(net.minecraft.world.entity.player.Player)" class="member-name-link">create</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Creates a new bit inventory wrapping the inventory of the player.</div><br></td></tr>
  <tr><td><code><a href="../bit/IBitInventoryItemStack.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack</a></code></td><td><code><a href="#create(net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates a new bit inventory wrapping the given itemstack.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.management">IBitInventoryManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
Gives access to the bit inventory manager.
<dl class="notes">
<dt>Returns:</dt>
<dd>The bit inventory manager.</dd>
</dl>
</div>
:::


</section>

<section id="create(net.minecraft.world.entity.player.Player)">

:::tabs
== create
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</span></div>
Creates a new bit inventory wrapping the inventory of the player.
This player inventory is aware of items which themselves can act
as a bit inventory.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player inventory.</dd>
<dt>Returns:</dt>
<dd>The bit inventory which represents the players inventory.</dd>
</dl>
</div>
:::


</section>

<section id="create(java.lang.Object)">

:::tabs
== create
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;target)</span></div>
Creates a new bit inventory wrapping the given <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.
This inventory is aware of items which themselves can act
as a bit inventory.
This endpoint is platform specific and might or might not be able to convert the object given.
Importantly on forge this endpoint is able to accept IItemHandlers, while on Fabric it will only support
IInventory.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - The <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.</dd>
<dt>Returns:</dt>
<dd>The bit inventory which represents the inventory.</dd>
</dl>
</div>
:::


</section>

<section id="create(net.minecraft.world.Container)">

:::tabs
== create
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../bit/IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(net.minecraft.world.Container&nbsp;inventory)</span></div>
Creates a new bit inventory wrapping the given inventory.
This inventory is aware of items which themselves can act
as a bit inventory.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inventory</code> - The inventory.</dd>
<dt>Returns:</dt>
<dd>The bit inventory which represents the inventory.</dd>
</dl>
</div>
:::


</section>

<section id="create(net.minecraft.world.item.ItemStack)">

:::tabs
== create
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../bit/IBitInventoryItemStack.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack</a></span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Creates a new bit inventory wrapping the given itemstack.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The itemstack to wrap.</dd>
<dt>Returns:</dt>
<dd>The bit inventory which represents the inventory.</dd>
</dl>
</div>
:::


</section>

:::::
  

