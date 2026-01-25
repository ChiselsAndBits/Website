--- 
title: IModificationOperation
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.modification.operation](index.md)  
# Interface IModificationOperation  
**All Extended Interfaces:**  
ICustomRegistryEntry, [IRenderableMode](../withmode/IRenderableMode.md), [IToolMode\<IModificationOperationGroup\>](../withmode/IToolMode.md), [IWithColor](../util/IWithColor.md), [IWithDisplayName](../util/IWithDisplayName.md), [IWithIcon](../util/IWithIcon.md), [IWithIconAndColor](../util/IWithIconAndColor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IModificationOperation</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry, <a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>&lt;<a href="IModificationOperationGroup.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperationGroup</a>&gt;</span></div>  

  

<div class="block">A modification operation that can be performed in the modification table.</div>
  

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
  <tr><td><code>void</code></td><td><code><a href="#apply(mod.chiselsandbits.api.multistate.mutator.IGenerallyModifiableAreaMutator)" class="member-name-link">apply</a><wbr>(<a href="../../multistate/mutator/IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a>&nbsp;source)</code></td><td><div class="block">Performs a modification on the snapshot.</div><br></td></tr>
  <tr><td><code>static <a href="IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a></code></td><td><code><a href="#getDefaultMode()" class="member-name-link">getDefaultMode</a>()</code></td><td><div class="block">The default modification operation.</div><br></td></tr>
  <tr><td><code>static com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a>&gt;</code></td><td><code><a href="#getRegistry()" class="member-name-link">getRegistry</a>()</code></td><td><div class="block">The underlying registry that contains the different modification modes that can be performed.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a></code></td><td><code><a href="#getDefaultMode()" class="member-name-link">getDefaultMode</a>()</code></td><td><div class="block">The default modification operation.</div><br></td></tr>
  <tr><td><code>static com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a>&gt;</code></td><td><code><a href="#getRegistry()" class="member-name-link">getRegistry</a>()</code></td><td><div class="block">The underlying registry that contains the different modification modes that can be performed.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#apply(mod.chiselsandbits.api.multistate.mutator.IGenerallyModifiableAreaMutator)" class="member-name-link">apply</a><wbr>(<a href="../../multistate/mutator/IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a>&nbsp;source)</code></td><td><div class="block">Performs a modification on the snapshot.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#apply(mod.chiselsandbits.api.multistate.mutator.IGenerallyModifiableAreaMutator)" class="member-name-link">apply</a><wbr>(<a href="../../multistate/mutator/IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a>&nbsp;source)</code></td><td><div class="block">Performs a modification on the snapshot.</div><br></td></tr>
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
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a></span>&nbsp;<span class="element-name">getDefaultMode</span>()</div>
<div class="block">The default modification operation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The default operation.</dd>
</dl>
:::


</section>

<section id="getRegistry()">

:::tabs
== getRegistry
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type">com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a>&gt;</span>&nbsp;<span class="element-name">getRegistry</span>()</div>
<div class="block">The underlying registry that contains the different modification modes that can be performed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The underlying forge registry.</dd>
</dl>
:::


</section>

<section id="apply(mod.chiselsandbits.api.multistate.mutator.IGenerallyModifiableAreaMutator)">

:::tabs
== apply
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">apply</span><wbr><span class="parameters">(<a href="../../multistate/mutator/IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a>&nbsp;source)</span></div>
<div class="block">Performs a modification on the snapshot.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - The mutator to modify.</dd>
</dl>
:::


</section>

:::::
  

