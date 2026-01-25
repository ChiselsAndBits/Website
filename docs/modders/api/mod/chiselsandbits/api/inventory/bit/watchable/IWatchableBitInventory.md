--- 
title: IWatchableBitInventory
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.inventory.bit.watchable](index.md)  
# Interface IWatchableBitInventory  
**All Extended Interfaces:**  
[IBitInventory](../IBitInventory.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWatchableBitInventory</span><span class="extends-implements"><br/>  
extends <a href="../IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a></span></div>  

  

Bit inventory variant which can be watched for changes.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IWatch.html" title="interface in mod.chiselsandbits.api.inventory.bit.watchable">IWatch</a></code></td><td><code><a href="#startWatching(java.lang.Runnable)" class="member-name-link">startWatching</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onChangeCallback)</code></td><td><div class="block">Invoke to start receiving change callbacks on this given callback.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IWatch.html" title="interface in mod.chiselsandbits.api.inventory.bit.watchable">IWatch</a></code></td><td><code><a href="#startWatching(java.lang.Runnable)" class="member-name-link">startWatching</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onChangeCallback)</code></td><td><div class="block">Invoke to start receiving change callbacks on this given callback.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IWatch.html" title="interface in mod.chiselsandbits.api.inventory.bit.watchable">IWatch</a></code></td><td><code><a href="#startWatching(java.lang.Runnable)" class="member-name-link">startWatching</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onChangeCallback)</code></td><td><div class="block">Invoke to start receiving change callbacks on this given callback.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.inventory.bit.<a href="../IBitInventory.html" title="interface in mod.chiselsandbits.api.inventory.bit">IBitInventory</a>
<a href="../IBitInventory.html#canExtract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">canExtract</a>, <a href="../IBitInventory.html#canExtractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)">canExtractOne</a>, <a href="../IBitInventory.html#canInsert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">canInsert</a>, <a href="../IBitInventory.html#canInsertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)">canInsertOne</a>, <a href="../IBitInventory.html#contains(mod.chiselsandbits.api.blockinformation.BlockInformation)">contains</a>, <a href="../IBitInventory.html#extract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">extract</a>, <a href="../IBitInventory.html#extractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)">extractOne</a>, <a href="../IBitInventory.html#getContainedStates()">getContainedStates</a>, <a href="../IBitInventory.html#getMaxExtractAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)">getMaxExtractAmount</a>, <a href="../IBitInventory.html#getMaxInsertAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)">getMaxInsertAmount</a>, <a href="../IBitInventory.html#insert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">insert</a>, <a href="../IBitInventory.html#insert(net.minecraft.world.item.ItemStack)">insert</a>, <a href="../IBitInventory.html#insertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)">insertOne</a>, <a href="../IBitInventory.html#insertOrDiscard(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">insertOrDiscard</a>, <a href="../IBitInventory.html#isEmpty()">isEmpty</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="startWatching(java.lang.Runnable)">

:::tabs
== startWatching
<div class="member-signature"><span class="return-type"><a href="IWatch.html" title="interface in mod.chiselsandbits.api.inventory.bit.watchable">IWatch</a></span>&nbsp;<span class="element-name">startWatching</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onChangeCallback)</span></div>
Invoke to start receiving change callbacks on this given callback.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>onChangeCallback</code> - Triggered when the inventory changes.</dd>
<dt>Returns:</dt>
<dd>The watch object that can be closed to stop listening.</dd>
</dl>
:::


</section>

:::::
  

