--- 
title: IAdaptingBitInventoryManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.inventory.bit](index.md)  
# Interface IAdaptingBitInventoryManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IAdaptingBitInventoryManager</span></div>  

  

  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&gt;</code></td><td><code><a href="#create(java.lang.Object)" class="member-name-link">create</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;target)</code></td><td><div class="block">Creates a new bit inventory wrapping the given <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.</div><br></td></tr>
  <tr><td><code>static <a href="IAdaptingBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.bit">IAdaptingBitInventoryManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IAdaptingBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.bit">IAdaptingBitInventoryManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&gt;</code></td><td><code><a href="#create(java.lang.Object)" class="member-name-link">create</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;target)</code></td><td><div class="block">Creates a new bit inventory wrapping the given <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&gt;</code></td><td><code><a href="#create(java.lang.Object)" class="member-name-link">create</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;target)</code></td><td><div class="block">Creates a new bit inventory wrapping the given <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IAdaptingBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.bit">IAdaptingBitInventoryManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="create(java.lang.Object)">

:::tabs
== create
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&gt;</span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;target)</span></div>
Creates a new bit inventory wrapping the given <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.

 This inventory is aware of items which themselves can act
 as a bit inventory.

 This endpoint is platform specific and might or might not be able to convert the object given.
 Importantly on forge this endpoint is able to accept IItemHandlers, while on Fabric it will only support
 IInventory.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - The <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link"><code>Object</code></a>.</dd>
<dt>Returns:</dt>
<dd>The bit inventory which represents the inventory.</dd>
</dl>
:::


</section>

:::::
  

