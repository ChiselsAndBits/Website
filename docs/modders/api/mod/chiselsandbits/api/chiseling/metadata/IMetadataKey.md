--- 
title: IMetadataKey
aside: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling.metadata](index.md)  
# Interface IMetadataKey\<T\>  
**Type Parameters:**  
T - The internal type.  

**All Extended Interfaces:**  
ICustomRegistryEntry  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMetadataKey&lt;T&gt;</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry</span></div>  

  

<div class="block">Represents a key passed to an instance of <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling"><code>IChiselingContext</code></a> so that additional data can be stored
 on the context.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMetadataKey.html" title="type parameter in IMetadataKey">T</a></code></td><td><code><a href="#snapshot(T)" class="member-name-link">snapshot</a><wbr>(<a href="IMetadataKey.html" title="type parameter in IMetadataKey">T</a>&nbsp;value)</code></td><td><div class="block">Creates a snapshot of the value that is passed to it.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMetadataKey.html" title="type parameter in IMetadataKey">T</a></code></td><td><code><a href="#snapshot(T)" class="member-name-link">snapshot</a><wbr>(<a href="IMetadataKey.html" title="type parameter in IMetadataKey">T</a>&nbsp;value)</code></td><td><div class="block">Creates a snapshot of the value that is passed to it.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMetadataKey.html" title="type parameter in IMetadataKey">T</a></code></td><td><code><a href="#snapshot(T)" class="member-name-link">snapshot</a><wbr>(<a href="IMetadataKey.html" title="type parameter in IMetadataKey">T</a>&nbsp;value)</code></td><td><div class="block">Creates a snapshot of the value that is passed to it.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.communi.suggestu.scena.core.registries.ICustomRegistryEntry
getRegistryName
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="snapshot(T)">

:::tabs
== snapshot
<div class="member-signature"><span class="return-type"><a href="IMetadataKey.html" title="type parameter in IMetadataKey">T</a></span>&nbsp;<span class="element-name">snapshot</span><wbr><span class="parameters">(<a href="IMetadataKey.html" title="type parameter in IMetadataKey">T</a>&nbsp;value)</span></div>
<div class="block">Creates a snapshot of the value that is passed to it.
 The primary task of this method is to create a deep copy of the given value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - The value.</dd>
<dt>Returns:</dt>
<dd>The deep copied value.</dd>
</dl>
:::


</section>

:::::
  

