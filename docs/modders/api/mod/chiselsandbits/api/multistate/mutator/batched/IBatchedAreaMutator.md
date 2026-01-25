--- 
title: IBatchedAreaMutator
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.mutator.batched](index.md)  
# Interface IBatchedAreaMutator  
**All Extended Interfaces:**  
[IAABBOwner](../aabb/IAABBOwner.md), [IAreaAccessor](../accessor/IAreaAccessor.md), [IStateAccessor](../accessor/IStateAccessor.md), [IAreaMutator](../mutator/IAreaMutator.md), [IWithBatchableMutationSupport](../util/IWithBatchableMutationSupport.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBatchedAreaMutator</span><span class="extends-implements"><br/>  
extends <a href="../IAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IAreaMutator</a>, <a href="../../../util/IWithBatchableMutationSupport.html" title="interface in mod.chiselsandbits.api.util">IWithBatchableMutationSupport</a></span></div>  

  

<div class="block">A mutator which supports making mutations in batches.</div>
  

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
  <tr><td><code><a href="../../../util/IBatchMutation.html" title="interface in mod.chiselsandbits.api.util">IBatchMutation</a></code></td><td><code><a href="#batch(mod.chiselsandbits.api.change.IChangeTracker)" class="member-name-link">batch</a><wbr>(<a href="../../../change/IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a>&nbsp;changeTracker)</code></td><td><div class="block">Triggers a batch mutation start for block placement.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../../util/IBatchMutation.html" title="interface in mod.chiselsandbits.api.util">IBatchMutation</a></code></td><td><code><a href="#batch(mod.chiselsandbits.api.change.IChangeTracker)" class="member-name-link">batch</a><wbr>(<a href="../../../change/IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a>&nbsp;changeTracker)</code></td><td><div class="block">Triggers a batch mutation start for block placement.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../../util/IBatchMutation.html" title="interface in mod.chiselsandbits.api.util">IBatchMutation</a></code></td><td><code><a href="#batch(mod.chiselsandbits.api.change.IChangeTracker)" class="member-name-link">batch</a><wbr>(<a href="../../../change/IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a>&nbsp;changeTracker)</code></td><td><div class="block">Triggers a batch mutation start for block placement.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a>
<a href="../../../aabb/IAABBOwner.html#getBoundingBox()">getBoundingBox</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>
<a href="../../accessor/IAreaAccessor.html#createNewShapeIdentifier()">createNewShapeIdentifier</a>, <a href="../../accessor/IAreaAccessor.html#createSnapshot()">createSnapshot</a>, <a href="../../accessor/IAreaAccessor.html#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)">forEachWithPositionMutator</a>, <a href="../../accessor/IAreaAccessor.html#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">isInside</a>, <a href="../../accessor/IAreaAccessor.html#isInside(net.minecraft.world.phys.Vec3)">isInside</a>, <a href="../../accessor/IAreaAccessor.html#stream()">stream</a>, <a href="../../accessor/IAreaAccessor.html#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)">streamWithPositionMutator</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="../IAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IAreaMutator</a>
<a href="../IAreaMutator.html#clearInAreaTarget(net.minecraft.world.phys.Vec3)">clearInAreaTarget</a>, <a href="../IAreaMutator.html#clearInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">clearInBlockTarget</a>, <a href="../IAreaMutator.html#mutableStream()">mutableStream</a>, <a href="../IAreaMutator.html#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">overrideInAreaTarget</a>, <a href="../IAreaMutator.html#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)">overrideInAreaTarget</a>, <a href="../IAreaMutator.html#setInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)">setInAreaTarget</a>, <a href="../IAreaMutator.html#setInBlockTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">setInBlockTarget</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>
<a href="../../accessor/IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)">getInAreaTarget</a>, <a href="../../accessor/IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">getInBlockTarget</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../../util/IWithBatchableMutationSupport.html" title="interface in mod.chiselsandbits.api.util">IWithBatchableMutationSupport</a>
<a href="../../../util/IWithBatchableMutationSupport.html#batch()">batch</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="batch(mod.chiselsandbits.api.change.IChangeTracker)">

:::tabs
== batch
<div class="member-signature"><span class="return-type"><a href="../../../util/IBatchMutation.html" title="interface in mod.chiselsandbits.api.util">IBatchMutation</a></span>&nbsp;<span class="element-name">batch</span><wbr><span class="parameters">(<a href="../../../change/IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a>&nbsp;changeTracker)</span></div>
<div class="block">Triggers a batch mutation start for block placement.
 Enables tracking of the changes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changeTracker</code> - The change tracker to apply the changes to.</dd>
<dt>Returns:</dt>
<dd>The batch mutation, which will record the changes automatically.</dd>
</dl>
:::


</section>

:::::
  

