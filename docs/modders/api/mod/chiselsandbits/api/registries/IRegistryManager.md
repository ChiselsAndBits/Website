--- 
title: IRegistryManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.registries](index)  
# Interface IRegistryManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IRegistryManager</span></div>  

  

Manages all registries which are used by Chisels and Bits.  

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
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../change/changes/IChangeType.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeType</a>&gt;</code></td><td><code><a href="#getChangeTypeRegistry()" class="member-name-link">getChangeTypeRegistry</a>()</code></td><td><div class="block">The registry used for change types.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;</code></td><td><code><a href="#getChiselModeRegistry()" class="member-name-link">getChiselModeRegistry</a>()</code></td><td><div class="block">The registry which controls all available chiseling modes.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../cutting/operation/ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a>&gt;</code></td><td><code><a href="#getCuttingOperationRegistry()" class="member-name-link">getCuttingOperationRegistry</a>()</code></td><td><div class="block">The registry used for cutting of single use patterns.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../glueing/operation/IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a>&gt;</code></td><td><code><a href="#getGlueingOperationRegistry()" class="member-name-link">getGlueingOperationRegistry</a>()</code></td><td><div class="block">The registry used for glueing of single use patterns.</div><br></td></tr>
  <tr><td><code>static <a href="IRegistryManager.html" title="interface in mod.chiselsandbits.api.registries">IRegistryManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a>&gt;</code></td><td><code><a href="#getModificationOperationRegistry()" class="member-name-link">getModificationOperationRegistry</a>()</code></td><td><div class="block">The registry used for modifications of single use patterns.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../multistate/snapshot/IMultiStateSnapshotType.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshotType</a>&gt;</code></td><td><code><a href="#getMultiStateSnapshotTypeRegistry()" class="member-name-link">getMultiStateSnapshotTypeRegistry</a>()</code></td><td><div class="block">The registry used for multi state snapshot types.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../pattern/placement/IPatternPlacementType.html" title="interface in mod.chiselsandbits.api.pattern.placement">IPatternPlacementType</a>&gt;</code></td><td><code><a href="#getPatternPlacementTypeRegistry()" class="member-name-link">getPatternPlacementTypeRegistry</a>()</code></td><td><div class="block">The registry used for pattern placement types.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IRegistryManager.html" title="interface in mod.chiselsandbits.api.registries">IRegistryManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../change/changes/IChangeType.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeType</a>&gt;</code></td><td><code><a href="#getChangeTypeRegistry()" class="member-name-link">getChangeTypeRegistry</a>()</code></td><td><div class="block">The registry used for change types.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;</code></td><td><code><a href="#getChiselModeRegistry()" class="member-name-link">getChiselModeRegistry</a>()</code></td><td><div class="block">The registry which controls all available chiseling modes.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../cutting/operation/ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a>&gt;</code></td><td><code><a href="#getCuttingOperationRegistry()" class="member-name-link">getCuttingOperationRegistry</a>()</code></td><td><div class="block">The registry used for cutting of single use patterns.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../glueing/operation/IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a>&gt;</code></td><td><code><a href="#getGlueingOperationRegistry()" class="member-name-link">getGlueingOperationRegistry</a>()</code></td><td><div class="block">The registry used for glueing of single use patterns.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a>&gt;</code></td><td><code><a href="#getModificationOperationRegistry()" class="member-name-link">getModificationOperationRegistry</a>()</code></td><td><div class="block">The registry used for modifications of single use patterns.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../multistate/snapshot/IMultiStateSnapshotType.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshotType</a>&gt;</code></td><td><code><a href="#getMultiStateSnapshotTypeRegistry()" class="member-name-link">getMultiStateSnapshotTypeRegistry</a>()</code></td><td><div class="block">The registry used for multi state snapshot types.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../pattern/placement/IPatternPlacementType.html" title="interface in mod.chiselsandbits.api.pattern.placement">IPatternPlacementType</a>&gt;</code></td><td><code><a href="#getPatternPlacementTypeRegistry()" class="member-name-link">getPatternPlacementTypeRegistry</a>()</code></td><td><div class="block">The registry used for pattern placement types.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../change/changes/IChangeType.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeType</a>&gt;</code></td><td><code><a href="#getChangeTypeRegistry()" class="member-name-link">getChangeTypeRegistry</a>()</code></td><td><div class="block">The registry used for change types.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;</code></td><td><code><a href="#getChiselModeRegistry()" class="member-name-link">getChiselModeRegistry</a>()</code></td><td><div class="block">The registry which controls all available chiseling modes.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../cutting/operation/ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a>&gt;</code></td><td><code><a href="#getCuttingOperationRegistry()" class="member-name-link">getCuttingOperationRegistry</a>()</code></td><td><div class="block">The registry used for cutting of single use patterns.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../glueing/operation/IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a>&gt;</code></td><td><code><a href="#getGlueingOperationRegistry()" class="member-name-link">getGlueingOperationRegistry</a>()</code></td><td><div class="block">The registry used for glueing of single use patterns.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a>&gt;</code></td><td><code><a href="#getModificationOperationRegistry()" class="member-name-link">getModificationOperationRegistry</a>()</code></td><td><div class="block">The registry used for modifications of single use patterns.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../multistate/snapshot/IMultiStateSnapshotType.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshotType</a>&gt;</code></td><td><code><a href="#getMultiStateSnapshotTypeRegistry()" class="member-name-link">getMultiStateSnapshotTypeRegistry</a>()</code></td><td><div class="block">The registry used for multi state snapshot types.</div><br></td></tr>
  <tr><td><code>@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="../pattern/placement/IPatternPlacementType.html" title="interface in mod.chiselsandbits.api.pattern.placement">IPatternPlacementType</a>&gt;</code></td><td><code><a href="#getPatternPlacementTypeRegistry()" class="member-name-link">getPatternPlacementTypeRegistry</a>()</code></td><td><div class="block">The registry used for pattern placement types.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IRegistryManager.html" title="interface in mod.chiselsandbits.api.registries">IRegistryManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
</div>
:::


</section>

<section id="getChiselModeRegistry()">

:::tabs
== getChiselModeRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="../chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;</span>&nbsp;<span class="element-name">getChiselModeRegistry</span>()</div>
The registry which controls all available chiseling modes.
<dl class="notes">
<dt>Returns:</dt>
<dd>The registry.</dd>
</dl>
</div>
:::


</section>

<section id="getModificationOperationRegistry()">

:::tabs
== getModificationOperationRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="../modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a>&gt;</span>&nbsp;<span class="element-name">getModificationOperationRegistry</span>()</div>
The registry used for modifications of single use patterns.
<dl class="notes">
<dt>Returns:</dt>
<dd>The modification operation registry.</dd>
</dl>
</div>
:::


</section>

<section id="getCuttingOperationRegistry()">

:::tabs
== getCuttingOperationRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="../cutting/operation/ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a>&gt;</span>&nbsp;<span class="element-name">getCuttingOperationRegistry</span>()</div>
The registry used for cutting of single use patterns.
<dl class="notes">
<dt>Returns:</dt>
<dd>The cutting operation registry.</dd>
</dl>
</div>
:::


</section>

<section id="getGlueingOperationRegistry()">

:::tabs
== getGlueingOperationRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="../glueing/operation/IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a>&gt;</span>&nbsp;<span class="element-name">getGlueingOperationRegistry</span>()</div>
The registry used for glueing of single use patterns.
<dl class="notes">
<dt>Returns:</dt>
<dd>The glueing operation registry.</dd>
</dl>
</div>
:::


</section>

<section id="getChangeTypeRegistry()">

:::tabs
== getChangeTypeRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="../change/changes/IChangeType.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeType</a>&gt;</span>&nbsp;<span class="element-name">getChangeTypeRegistry</span>()</div>
The registry used for change types.
<dl class="notes">
<dt>Returns:</dt>
<dd>The change type registry.</dd>
</dl>
</div>
:::


</section>

<section id="getMultiStateSnapshotTypeRegistry()">

:::tabs
== getMultiStateSnapshotTypeRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="../multistate/snapshot/IMultiStateSnapshotType.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshotType</a>&gt;</span>&nbsp;<span class="element-name">getMultiStateSnapshotTypeRegistry</span>()</div>
The registry used for multi state snapshot types.
<dl class="notes">
<dt>Returns:</dt>
<dd>The multi state snapshot type registry.</dd>
</dl>
</div>
:::


</section>

<section id="getPatternPlacementTypeRegistry()">

:::tabs
== getPatternPlacementTypeRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="../pattern/placement/IPatternPlacementType.html" title="interface in mod.chiselsandbits.api.pattern.placement">IPatternPlacementType</a>&gt;</span>&nbsp;<span class="element-name">getPatternPlacementTypeRegistry</span>()</div>
The registry used for pattern placement types.
<dl class="notes">
<dt>Returns:</dt>
<dd>The pattern placement type registry.</dd>
</dl>
</div>
:::


</section>

:::::
  

