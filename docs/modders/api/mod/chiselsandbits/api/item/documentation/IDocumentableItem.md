--- 
title: IDocumentableItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.documentation](index.md)  
# Interface IDocumentableItem  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IDocumentableItem</span></div>  

  

Represents an item that is documented via the Chisels and Bits documentation export system.  

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
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>, net.minecraft.world.item.ItemStack&gt;</code></td><td><code><a href="#getDocumentableInstances(net.minecraft.world.item.Item)" class="member-name-link">getDocumentableInstances</a><wbr>(net.minecraft.world.item.Item&nbsp;item)</code></td><td><div class="block">Gives access to the variants of the item that are exportable.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>, net.minecraft.world.item.ItemStack&gt;</code></td><td><code><a href="#getDocumentableInstances(net.minecraft.world.item.Item)" class="member-name-link">getDocumentableInstances</a><wbr>(net.minecraft.world.item.Item&nbsp;item)</code></td><td><div class="block">Gives access to the variants of the item that are exportable.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>, net.minecraft.world.item.ItemStack&gt;</code></td><td><code><a href="#getDocumentableInstances(net.minecraft.world.item.Item)" class="member-name-link">getDocumentableInstances</a><wbr>(net.minecraft.world.item.Item&nbsp;item)</code></td><td><div class="block">Gives access to the variants of the item that are exportable.</div><br></td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getDocumentableInstances(net.minecraft.world.item.Item)">

:::tabs
== getDocumentableInstances
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>, net.minecraft.world.item.ItemStack&gt;</span>&nbsp;<span class="element-name">getDocumentableInstances</span><wbr><span class="parameters">(net.minecraft.world.item.Item&nbsp;item)</span></div>
<div class="block">Gives access to the variants of the item that are exportable.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>item</code> - The item instance in question.</dd>
<dt>Returns:</dt>
<dd>The variants with their names as key.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

