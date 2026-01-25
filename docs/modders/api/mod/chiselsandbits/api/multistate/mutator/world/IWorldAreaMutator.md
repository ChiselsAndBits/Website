--- 
title: IWorldAreaMutator
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.mutator.world](index.md)  
# Interface IWorldAreaMutator  
**All Extended Interfaces:**  
[IAABBOwner](../../../aabb/IAABBOwner.md), [IAreaAccessor](../../accessor/IAreaAccessor.md), [IStateAccessor](../../accessor/IStateAccessor.md), [IWorldAreaAccessor](../../accessor/world/IWorldAreaAccessor.md), [IBatchedAreaMutator](../batched/IBatchedAreaMutator.md), [IAreaMutator](../IAreaMutator.md), [IWithBatchableMutationSupport](../../../util/IWithBatchableMutationSupport.md), [IWorldObject](../../../util/IWorldObject.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWorldAreaMutator</span><span class="extends-implements"><br/>  
extends <a href="../../accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>, <a href="../IAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IAreaMutator</a>, <a href="../batched/IBatchedAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.batched">IBatchedAreaMutator</a></span></div>  

  

Allows for a given area in the world to be mutated.  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IInWorldMutableStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IInWorldMutableStateEntryInfo</a>&gt;</code></td><td><code><a href="#inWorldMutableStream()" class="member-name-link">inWorldMutableStream</a>()</code></td><td><div class="block">Returns all entries in the current area in a mutable fashion.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IInWorldMutableStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IInWorldMutableStateEntryInfo</a>&gt;</code></td><td><code><a href="#inWorldMutableStream()" class="member-name-link">inWorldMutableStream</a>()</code></td><td><div class="block">Returns all entries in the current area in a mutable fashion.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IInWorldMutableStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IInWorldMutableStateEntryInfo</a>&gt;</code></td><td><code><a href="#inWorldMutableStream()" class="member-name-link">inWorldMutableStream</a>()</code></td><td><div class="block">Returns all entries in the current area in a mutable fashion.</div><br></td></tr>
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
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.batched.<a href="../batched/IBatchedAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.batched">IBatchedAreaMutator</a>
<a href="../batched/IBatchedAreaMutator.html#batch(mod.chiselsandbits.api.change.IChangeTracker)">batch</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>
<a href="../../accessor/IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)">getInAreaTarget</a>, <a href="../../accessor/IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">getInBlockTarget</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../../util/IWithBatchableMutationSupport.html" title="interface in mod.chiselsandbits.api.util">IWithBatchableMutationSupport</a>
<a href="../../../util/IWithBatchableMutationSupport.html#batch()">batch</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.world.<a href="../../accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>
<a href="../../accessor/world/IWorldAreaAccessor.html#coveredAreaStream()">coveredAreaStream</a>, <a href="../../accessor/world/IWorldAreaAccessor.html#inWorldStream()">inWorldStream</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../../util/IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>
<a href="../../../util/IWorldObject.html#getInWorldBoundingBox()">getInWorldBoundingBox</a>, <a href="../../../util/IWorldObject.html#getInWorldEndBlockPoint()">getInWorldEndBlockPoint</a>, <a href="../../../util/IWorldObject.html#getInWorldEndPoint()">getInWorldEndPoint</a>, <a href="../../../util/IWorldObject.html#getInWorldStartBlockPoint()">getInWorldStartBlockPoint</a>, <a href="../../../util/IWorldObject.html#getInWorldStartPoint()">getInWorldStartPoint</a>, <a href="../../../util/IWorldObject.html#getWorld()">getWorld</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="inWorldMutableStream()">

:::tabs
== inWorldMutableStream
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;<a href="IInWorldMutableStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IInWorldMutableStateEntryInfo</a>&gt;</span>&nbsp;<span class="element-name">inWorldMutableStream</span>()</div>
Returns all entries in the current area in a mutable fashion.
 Includes all empty areas as areas containing an air state.
<dl class="notes">
<dt>Returns:</dt>
<dd>A stream with a mutable state entry info for each mutable section in the area.</dd>
</dl>
:::


</section>

:::::
  

