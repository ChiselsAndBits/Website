--- 
title: IGlueingOperation
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.glueing.operation](index.md)  
# Interface IGlueingOperation  
**All Extended Interfaces:**  
ICustomRegistryEntry, [IRenderableMode](../../item/withmode/IRenderableMode.md), [IToolMode\<IGlueingOperationGroup\>](../../item/withmode/IToolMode.md), [IWithColor](../../util/IWithColor.md), [IWithDisplayName](../../util/IWithDisplayName.md), [IWithIcon](../../util/IWithIcon.md), [IWithIconAndColor](../../util/IWithIconAndColor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IGlueingOperation</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry, <a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>&lt;<a href="IGlueingOperationGroup.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperationGroup</a>&gt;</span></div>  

  

A Glueing operation that can be performed in the Glueing table.  

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
  <tr><td><code><a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#apply(java.util.Collection)" class="member-name-link">apply</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;&nbsp;sources)</code></td><td><div class="block">Performs a glueing on the given snapshots.</div><br></td></tr>
  <tr><td><code>static <a href="IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a></code></td><td><code><a href="#getDefaultMode()" class="member-name-link">getDefaultMode</a>()</code></td><td><div class="block">The default Glueing operation.</div><br></td></tr>
  <tr><td><code>static com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a>&gt;</code></td><td><code><a href="#getRegistry()" class="member-name-link">getRegistry</a>()</code></td><td><div class="block">The underlying registry that contains the different Glueing modes that can be performed.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a></code></td><td><code><a href="#getDefaultMode()" class="member-name-link">getDefaultMode</a>()</code></td><td><div class="block">The default Glueing operation.</div><br></td></tr>
  <tr><td><code>static com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a>&gt;</code></td><td><code><a href="#getRegistry()" class="member-name-link">getRegistry</a>()</code></td><td><div class="block">The underlying registry that contains the different Glueing modes that can be performed.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#apply(java.util.Collection)" class="member-name-link">apply</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;&nbsp;sources)</code></td><td><div class="block">Performs a glueing on the given snapshots.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#apply(java.util.Collection)" class="member-name-link">apply</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;&nbsp;sources)</code></td><td><div class="block">Performs a glueing on the given snapshots.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.communi.suggestu.scena.core.registries.ICustomRegistryEntry
getRegistryName
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../../item/withmode/IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a>
<a href="../../item/withmode/IRenderableMode.html#getColorVector()" title="getColorVector()">getColorVector</a>, <a href="../../item/withmode/IRenderableMode.html#getPositionVector()" title="getPositionVector()">getPositionVector</a>, <a href="../../item/withmode/IRenderableMode.html#getScaleVector()" title="getScaleVector()">getScaleVector</a>, <a href="../../item/withmode/IRenderableMode.html#isActive()" title="isActive()">isActive</a>, <a href="../../item/withmode/IRenderableMode.html#shouldRenderDisplayNameInMenu()" title="shouldRenderDisplayNameInMenu()">shouldRenderDisplayNameInMenu</a>, <a href="../../item/withmode/IRenderableMode.html#shouldRenderName()" title="shouldRenderName()">shouldRenderName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>
<a href="../../item/withmode/IToolMode.html#getGroup()" title="getGroup()">getGroup</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a>
<a href="../../util/IWithColor.html#getAlphaChannel()" title="getAlphaChannel()">getAlphaChannel</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a>
<a href="../../util/IWithDisplayName.html#getDisplayName()" title="getDisplayName()">getDisplayName</a>, <a href="../../util/IWithDisplayName.html#getMultiLineDisplayName()" title="getMultiLineDisplayName()">getMultiLineDisplayName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a>
<a href="../../util/IWithIcon.html#getIcon()" title="getIcon()">getIcon</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getDefaultMode()">

:::tabs
== getDefaultMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a></span>&nbsp;<span class="element-name">getDefaultMode</span>()</div>
The default Glueing operation.
<dl class="notes">
<dt>Returns:</dt>
<dd>The default operation.</dd>
</dl>
</div>
:::


</section>

<section id="getRegistry()">

:::tabs
== getRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type">com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a>&gt;</span>&nbsp;<span class="element-name">getRegistry</span>()</div>
The underlying registry that contains the different Glueing modes that can be performed.
<dl class="notes">
<dt>Returns:</dt>
<dd>The underlying forge registry.</dd>
</dl>
</div>
:::


</section>

<section id="apply(java.util.Collection)">

:::tabs
== apply
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></span>&nbsp;<span class="element-name">apply</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;&nbsp;sources)</span></div>
Performs a glueing on the given snapshots.
The given collection contains the individual pieces that are needed to be glued together.
<p>
In total a maximum 64 pieces can be given.</p>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sources</code> - The accessors to glue.</dd>
<dt>Returns:</dt>
<dd>An accessor which was created by the operation.</dd>
</dl>
</div>
:::


</section>

:::::
  

