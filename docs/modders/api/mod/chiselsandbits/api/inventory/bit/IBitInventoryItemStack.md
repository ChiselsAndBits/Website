--- 
title: IBitInventoryItemStack
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.inventory.bit](index.md)  
# Interface IBitInventoryItemStack  
**All Extended Interfaces:**  
Iterable\<ItemStack\>, [IBitInventory](IBitInventory.md), Clearable, Container, SlotProvider  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBitInventoryItemStack</span><span class="extends-implements"><br/>  
extends <a href="IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a>, net.minecraft.world.Container</span></div>  

  

A bit inventory which can be converted to an itemstack.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Interface</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="IBitInventoryItemStack.DisplayContents.html" class="type-name-link" title="class in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack.DisplayContents</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
Nested classes/interfaces inherited from interface&nbsp;net.minecraft.world.Containernet.minecraft.world.Container.ContainerIterator
:::::
  
  
<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
Fields inherited from interface&nbsp;net.minecraft.world.ContainerDEFAULT_DISTANCE_BUFFER
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">clear</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state)</code></td><td><div class="block">Clears the bit inventory of the current state.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#convert(net.minecraft.world.entity.player.Player)" class="member-name-link">convert</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Converts the inventory into blocks</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#getFilledRatio()" class="member-name-link">getFilledRatio</a>()</code></td><td><div class="block">Calculates the fullness ratio of the itemstack inventory.</div><br></td></tr>
  <tr><td><code><a href="IBitInventoryItemStack.DisplayContents.html" title="class in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack.DisplayContents</a></code></td><td><code><a href="#listContents()" class="member-name-link">listContents</a>()</code></td><td><div class="block">This lists the contents of the itemstacks bit inventory.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#sort()" class="member-name-link">sort</a>()</code></td><td><div class="block">Sorts the bit inventory.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toItemStack()" class="member-name-link">toItemStack</a>()</code></td><td><div class="block">Converts this bit inventory into an itemstack.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">clear</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state)</code></td><td><div class="block">Clears the bit inventory of the current state.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#convert(net.minecraft.world.entity.player.Player)" class="member-name-link">convert</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Converts the inventory into blocks</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#getFilledRatio()" class="member-name-link">getFilledRatio</a>()</code></td><td><div class="block">Calculates the fullness ratio of the itemstack inventory.</div><br></td></tr>
  <tr><td><code><a href="IBitInventoryItemStack.DisplayContents.html" title="class in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack.DisplayContents</a></code></td><td><code><a href="#listContents()" class="member-name-link">listContents</a>()</code></td><td><div class="block">This lists the contents of the itemstacks bit inventory.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#sort()" class="member-name-link">sort</a>()</code></td><td><div class="block">Sorts the bit inventory.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toItemStack()" class="member-name-link">toItemStack</a>()</code></td><td><div class="block">Converts this bit inventory into an itemstack.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">clear</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state)</code></td><td><div class="block">Clears the bit inventory of the current state.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#convert(net.minecraft.world.entity.player.Player)" class="member-name-link">convert</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Converts the inventory into blocks</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#getFilledRatio()" class="member-name-link">getFilledRatio</a>()</code></td><td><div class="block">Calculates the fullness ratio of the itemstack inventory.</div><br></td></tr>
  <tr><td><code><a href="IBitInventoryItemStack.DisplayContents.html" title="class in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack.DisplayContents</a></code></td><td><code><a href="#listContents()" class="member-name-link">listContents</a>()</code></td><td><div class="block">This lists the contents of the itemstacks bit inventory.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#sort()" class="member-name-link">sort</a>()</code></td><td><div class="block">Sorts the bit inventory.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toItemStack()" class="member-name-link">toItemStack</a>()</code></td><td><div class="block">Converts this bit inventory into an itemstack.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;net.minecraft.world.ClearableclearContentMethods inherited from interface&nbsp;net.minecraft.world.ContainercanPlaceItem, canTakeItem, countItem, getContainerSize, getEntitiesWithContainerOpen, getItem, getMaxStackSize, getMaxStackSize, getSlot, hasAnyMatching, hasAnyOf, isEmpty, iterator, removeItem, removeItemNoUpdate, setChanged, setItem, startOpen, stillValid, stopOpenMethods inherited from interface&nbsp;mod.chiselsandbits.api.inventory.bit.<a href="IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a><a href="IBitInventory.html#canExtract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" title="canExtract(BlockInformation, int)">canExtract</a>, <a href="IBitInventory.html#canExtractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" title="canExtractOne(BlockInformation)">canExtractOne</a>, <a href="IBitInventory.html#canInsert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" title="canInsert(BlockInformation, int)">canInsert</a>, <a href="IBitInventory.html#canInsertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" title="canInsertOne(BlockInformation)">canInsertOne</a>, <a href="IBitInventory.html#contains(mod.chiselsandbits.api.blockinformation.BlockInformation)" title="contains(BlockInformation)">contains</a>, <a href="IBitInventory.html#extract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" title="extract(BlockInformation, int)">extract</a>, <a href="IBitInventory.html#extractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" title="extractOne(BlockInformation)">extractOne</a>, <a href="IBitInventory.html#getContainedStates()" title="getContainedStates()">getContainedStates</a>, <a href="IBitInventory.html#getMaxExtractAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)" title="getMaxExtractAmount(BlockInformation)">getMaxExtractAmount</a>, <a href="IBitInventory.html#getMaxInsertAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)" title="getMaxInsertAmount(BlockInformation)">getMaxInsertAmount</a>, <a href="IBitInventory.html#insert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" title="insert(BlockInformation, int)">insert</a>, <a href="IBitInventory.html#insert(net.minecraft.world.item.ItemStack)" title="insert(ItemStack)">insert</a>, <a href="IBitInventory.html#insertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" title="insertOne(BlockInformation)">insertOne</a>, <a href="IBitInventory.html#insertOrDiscard(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" title="insertOrDiscard(BlockInformation, int)">insertOrDiscard</a>, <a href="IBitInventory.html#isEmpty()" title="isEmpty()">isEmpty</a>Methods inherited from interface&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang" class="external-link">forEach</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html#spliterator()" title="class or interface in java.lang" class="external-link">spliterator</a>Methods inherited from interface&nbsp;net.minecraft.world.entity.SlotProvidergetSlotsFromRange
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="toItemStack()">

:::tabs
== toItemStack
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">toItemStack</span>()</div>
Converts this bit inventory into an itemstack.
<dl class="notes">
<dt>Returns:</dt>
<dd>The itemstack which represents this inventory.</dd>
</dl>
</div>
:::


</section>

<section id="listContents()">

:::tabs
== listContents
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IBitInventoryItemStack.DisplayContents.html" title="class in mod.chiselsandbits.api.inventory.bit">IBitInventoryItemStack.DisplayContents</a></span>&nbsp;<span class="element-name">listContents</span>()</div>
This lists the contents of the itemstacks bit inventory.
<dl class="notes">
<dt>Returns:</dt>
<dd>The contents.</dd>
</dl>
</div>
:::


</section>

<section id="getFilledRatio()">

:::tabs
== getFilledRatio
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">double</span>&nbsp;<span class="element-name">getFilledRatio</span>()</div>
Calculates the fullness ratio of the itemstack inventory.
Useful to render the fullness ration as durability bar on the item.
<dl class="notes">
<dt>Returns:</dt>
<dd>The filled ratio.</dd>
</dl>
</div>
:::


</section>

<section id="clear(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== clear
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clear</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state)</span></div>
Clears the bit inventory of the current state.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - The blockstate to remove from the bit inventory.</dd>
</dl>
</div>
:::


</section>

<section id="sort()">

:::tabs
== sort
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">sort</span>()</div>
Sorts the bit inventory.</div>
:::


</section>

<section id="convert(net.minecraft.world.entity.player.Player)">

:::tabs
== convert
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">convert</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player)</span></div>
Converts the inventory into blocks</div>
:::


</section>

:::::
  

