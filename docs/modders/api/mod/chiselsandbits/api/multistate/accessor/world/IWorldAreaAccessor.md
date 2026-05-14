--- 
title: IWorldAreaAccessor
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor.world](index)  
# Interface IWorldAreaAccessor  
**All Extended Interfaces:**  
[IAABBOwner](../../../aabb/IAABBOwner), [IAreaAccessor](../IAreaAccessor), [IStateAccessor](../IStateAccessor), [IWorldObject](../../../util/IWorldObject)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWorldAreaAccessor</span><span class="extends-implements"><br/>  
extends <a href="../IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="../../../util/IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a></span></div>  

  

Represents an area accessor which actually exists in the world.  

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
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#coveredAreaStream()" class="member-name-link">coveredAreaStream</a>()</code></td><td><div class="block">Gives access to a stream which represents all the blocks touched by the accessor.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IInWorldStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IInWorldStateEntryInfo</a>&gt;</code></td><td><code><a href="#inWorldStream()" class="member-name-link">inWorldStream</a>()</code></td><td><div class="block">Gives access to a stream of in world state entries.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#coveredAreaStream()" class="member-name-link">coveredAreaStream</a>()</code></td><td><div class="block">Gives access to a stream which represents all the blocks touched by the accessor.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IInWorldStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IInWorldStateEntryInfo</a>&gt;</code></td><td><code><a href="#inWorldStream()" class="member-name-link">inWorldStream</a>()</code></td><td><div class="block">Gives access to a stream of in world state entries.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#coveredAreaStream()" class="member-name-link">coveredAreaStream</a>()</code></td><td><div class="block">Gives access to a stream which represents all the blocks touched by the accessor.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IInWorldStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IInWorldStateEntryInfo</a>&gt;</code></td><td><code><a href="#inWorldStream()" class="member-name-link">inWorldStream</a>()</code></td><td><div class="block">Gives access to a stream of in world state entries.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a>
<a href="../../../aabb/IAABBOwner.html#getBoundingBox()" title="getBoundingBox()">getBoundingBox</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>
<a href="../IAreaAccessor.html#createNewShapeIdentifier()" title="createNewShapeIdentifier()">createNewShapeIdentifier</a>, <a href="../IAreaAccessor.html#createSnapshot()" title="createSnapshot()">createSnapshot</a>, <a href="../IAreaAccessor.html#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)" title="forEachWithPositionMutator(IPositionMutator, Consumer)">forEachWithPositionMutator</a>, <a href="../IAreaAccessor.html#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="isInside(BlockPos, Vec3)">isInside</a>, <a href="../IAreaAccessor.html#isInside(net.minecraft.world.phys.Vec3)" title="isInside(Vec3)">isInside</a>, <a href="../IAreaAccessor.html#stream()" title="stream()">stream</a>, <a href="../IAreaAccessor.html#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" title="streamWithPositionMutator(IPositionMutator)">streamWithPositionMutator</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>
<a href="../IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)" title="getInAreaTarget(Vec3)">getInAreaTarget</a>, <a href="../IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="getInBlockTarget(BlockPos, Vec3)">getInBlockTarget</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../../util/IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>
<a href="../../../util/IWorldObject.html#getInWorldBoundingBox()" title="getInWorldBoundingBox()">getInWorldBoundingBox</a>, <a href="../../../util/IWorldObject.html#getInWorldEndBlockPoint()" title="getInWorldEndBlockPoint()">getInWorldEndBlockPoint</a>, <a href="../../../util/IWorldObject.html#getInWorldEndPoint()" title="getInWorldEndPoint()">getInWorldEndPoint</a>, <a href="../../../util/IWorldObject.html#getInWorldStartBlockPoint()" title="getInWorldStartBlockPoint()">getInWorldStartBlockPoint</a>, <a href="../../../util/IWorldObject.html#getInWorldStartPoint()" title="getInWorldStartPoint()">getInWorldStartPoint</a>, <a href="../../../util/IWorldObject.html#getWorld()" title="getWorld()">getWorld</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="inWorldStream()">

:::tabs
== inWorldStream
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;<a href="IInWorldStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IInWorldStateEntryInfo</a>&gt;</span>&nbsp;<span class="element-name">inWorldStream</span>()</div>
Gives access to a stream of in world state entries.
Filters out all "virtual"-none-in-world state entries that might or might not be included
in <a href="../IAreaAccessor.html#stream()"><code>IAreaAccessor.stream()</code></a>.
<dl class="notes">
<dt>Returns:</dt>
<dd>A stream with only state entries which actually exist in world.</dd>
</dl>
</div>
:::


</section>

<section id="coveredAreaStream()">

:::tabs
== coveredAreaStream
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">coveredAreaStream</span>()</div>
Gives access to a stream which represents all the blocks touched by the accessor.
<dl class="notes">
<dt>Returns:</dt>
<dd>The blocks touched by the accessor.</dd>
</dl>
</div>
:::


</section>

:::::
  

