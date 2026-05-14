--- 
title: IArrayBackedAreaShapeIdentifier
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor.identifier](index.md)  
# Interface IArrayBackedAreaShapeIdentifier  
**All Extended Interfaces:**  
[IAreaShapeIdentifier](IAreaShapeIdentifier.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IArrayBackedAreaShapeIdentifier</span><span class="extends-implements"><br/>  
extends <a href="IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a></span></div>  

  

Indicates that the <a href="IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier"><code>IAreaShapeIdentifier</code></a> is backed by a long array and as such its core data can directly be used to
compare the identifiers.  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Fields inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.identifier.<a href="IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>
<a href="IAreaShapeIdentifier.html#DUMMY">DUMMY</a>
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>long[]</code></td><td><code><a href="#getBackingData()" class="member-name-link">getBackingData</a>()</code></td><td><div class="block">Gives access to the backing long array.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getPalette()" class="member-name-link">getPalette</a>()</code></td><td><div class="block">The palette that is in use for this identifier.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>long[]</code></td><td><code><a href="#getBackingData()" class="member-name-link">getBackingData</a>()</code></td><td><div class="block">Gives access to the backing long array.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getPalette()" class="member-name-link">getPalette</a>()</code></td><td><div class="block">The palette that is in use for this identifier.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>long[]</code></td><td><code><a href="#getBackingData()" class="member-name-link">getBackingData</a>()</code></td><td><div class="block">Gives access to the backing long array.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getPalette()" class="member-name-link">getPalette</a>()</code></td><td><div class="block">The palette that is in use for this identifier.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getBackingData()">

:::tabs
== getBackingData
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">long[]</span>&nbsp;<span class="element-name">getBackingData</span>()</div>
Gives access to the backing long array.
<dl class="notes">
<dt>Returns:</dt>
<dd>The backing long array.</dd>
</dl>
</div>
:::


</section>

<section id="getPalette()">

:::tabs
== getPalette
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">getPalette</span>()</div>
The palette that is in use for this identifier.
<dl class="notes">
<dt>Returns:</dt>
<dd>The palette list.</dd>
</dl>
</div>
:::


</section>

:::::
  

