--- 
title: ICuttingOperation
aside: false 
---
_Package:_ [mod.chiselsandbits.api.cutting.operation](index.md)  
# Interface ICuttingOperation  
**All Extended Interfaces:**  
ICustomRegistryEntry, [IRenderableMode](../withmode/IRenderableMode.md), [IToolMode\<ICuttingOperationGroup\>](../withmode/IToolMode.md), [IWithColor](../util/IWithColor.md), [IWithDisplayName](../util/IWithDisplayName.md), [IWithIcon](../util/IWithIcon.md), [IWithIconAndColor](../util/IWithIconAndColor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ICuttingOperation</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry, <a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>&lt;<a href="ICuttingOperationGroup.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperationGroup</a>&gt;</span></div>  

  

<div class="block">A Cutting operation that can be performed in the Cutting table.</div>
  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;</code></td><td><code><a href="#apply(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">apply</a><wbr>(<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;source)</code></td><td><div class="block">Performs a Cutting on the snapshot.</div><br></td></tr>
  <tr><td><code>static <a href="ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a></code></td><td><code><a href="#getDefaultMode()" class="member-name-link">getDefaultMode</a>()</code></td><td><div class="block">The default Cutting operation.</div><br></td></tr>
  <tr><td><code>static com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a>&gt;</code></td><td><code><a href="#getRegistry()" class="member-name-link">getRegistry</a>()</code></td><td><div class="block">The underlying registry that contains the different Cutting modes that can be performed.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a></code></td><td><code><a href="#getDefaultMode()" class="member-name-link">getDefaultMode</a>()</code></td><td><div class="block">The default Cutting operation.</div><br></td></tr>
  <tr><td><code>static com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a>&gt;</code></td><td><code><a href="#getRegistry()" class="member-name-link">getRegistry</a>()</code></td><td><div class="block">The underlying registry that contains the different Cutting modes that can be performed.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;</code></td><td><code><a href="#apply(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">apply</a><wbr>(<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;source)</code></td><td><div class="block">Performs a Cutting on the snapshot.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;</code></td><td><code><a href="#apply(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">apply</a><wbr>(<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;source)</code></td><td><div class="block">Performs a Cutting on the snapshot.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.communi.suggestu.scena.core.registries.ICustomRegistryEntry
getRegistryName
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../../item/withmode/IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a>
<a href="../../item/withmode/IRenderableMode.html#getColorVector()">getColorVector</a>, <a href="../../item/withmode/IRenderableMode.html#getPositionVector()">getPositionVector</a>, <a href="../../item/withmode/IRenderableMode.html#getScaleVector()">getScaleVector</a>, <a href="../../item/withmode/IRenderableMode.html#isActive()">isActive</a>, <a href="../../item/withmode/IRenderableMode.html#shouldRenderDisplayNameInMenu()">shouldRenderDisplayNameInMenu</a>, <a href="../../item/withmode/IRenderableMode.html#shouldRenderName()">shouldRenderName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>
<a href="../../item/withmode/IToolMode.html#getGroup()">getGroup</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a>
<a href="../../util/IWithColor.html#getAlphaChannel()">getAlphaChannel</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a>
<a href="../../util/IWithDisplayName.html#getDisplayName()">getDisplayName</a>, <a href="../../util/IWithDisplayName.html#getMultiLineDisplayName()">getMultiLineDisplayName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a>
<a href="../../util/IWithIcon.html#getIcon()">getIcon</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getDefaultMode()">

:::tabs
== getDefaultMode
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a></span>&nbsp;<span class="element-name">getDefaultMode</span>()</div>
<div class="block">The default Cutting operation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The default operation.</dd>
</dl>
:::


</section>

<section id="getRegistry()">

:::tabs
== getRegistry
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type">com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a>&gt;</span>&nbsp;<span class="element-name">getRegistry</span>()</div>
<div class="block">The underlying registry that contains the different Cutting modes that can be performed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The underlying forge registry.</dd>
</dl>
:::


</section>

<section id="apply(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)">

:::tabs
== apply
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;</span>&nbsp;<span class="element-name">apply</span><wbr><span class="parameters">(<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;source)</span></div>
<div class="block">Performs a Cutting on the snapshot.
 The returned collection contains the individual pieces that result of this cut.

 In total a maximum 64 pieces can be returned.

 Note: The cutter generates a bundle if more than one unique piece is cut.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - The mutator to modify.</dd>
<dt>Returns:</dt>
<dd>A collection of accessors that were created by the operation.</dd>
</dl>
:::


</section>

:::::
  

