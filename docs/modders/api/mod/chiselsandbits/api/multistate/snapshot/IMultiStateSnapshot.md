--- 
title: IMultiStateSnapshot
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.snapshot](index.md)  
# Interface IMultiStateSnapshot  
**All Extended Interfaces:**  
Cloneable, [IAABBOwner](../../aabb/IAABBOwner.md), [IAreaAccessor](../accessor/IAreaAccessor.md), [IStateAccessor](../accessor/IStateAccessor.md), [IAreaMutator](../mutator/IAreaMutator.md), [IGenerallyModifiableAreaMutator](../mutator/IGenerallyModifiableAreaMutator.md), [IMirrorAndRotateble](../mutator/IMirrorAndRotateble.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiStateSnapshot</span><span class="extends-implements"><br/>  
extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang" class="external-link">Cloneable</a>, <a href="../mutator/IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</code></td><td><code><a href="#STREAM_CODEC" class="member-name-link">STREAM_CODEC</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#clone()" class="member-name-link">clone</a>()</code></td><td><div class="block">Creates a clone of the snapshot.</div><br></td></tr>
  <tr><td><code><a href="../statistics/IMultiStateObjectStatistics.html" title="interface in mod.chiselsandbits.api.multistate.statistics">IMultiStateObjectStatistics</a></code></td><td><code><a href="#getStatics()" class="member-name-link">getStatics</a>()</code></td><td><div class="block">Returns the statistics of the current snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshotType.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshotType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Gets the type of the snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#limitedToProgression(float)" class="member-name-link">limitedToProgression</a><wbr>(float&nbsp;progress)</code></td><td><div class="block">Creates a new snapshot which limits the currents snapshots contents to the given progression.</div><br></td></tr>
  <tr><td><code><a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#toItemStack()" class="member-name-link">toItemStack</a>()</code></td><td><div class="block">Converts the current snapshot to a variant which is itemstack capable.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#clone()" class="member-name-link">clone</a>()</code></td><td><div class="block">Creates a clone of the snapshot.</div><br></td></tr>
  <tr><td><code><a href="../statistics/IMultiStateObjectStatistics.html" title="interface in mod.chiselsandbits.api.multistate.statistics">IMultiStateObjectStatistics</a></code></td><td><code><a href="#getStatics()" class="member-name-link">getStatics</a>()</code></td><td><div class="block">Returns the statistics of the current snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshotType.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshotType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Gets the type of the snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#limitedToProgression(float)" class="member-name-link">limitedToProgression</a><wbr>(float&nbsp;progress)</code></td><td><div class="block">Creates a new snapshot which limits the currents snapshots contents to the given progression.</div><br></td></tr>
  <tr><td><code><a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#toItemStack()" class="member-name-link">toItemStack</a>()</code></td><td><div class="block">Converts the current snapshot to a variant which is itemstack capable.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#clone()" class="member-name-link">clone</a>()</code></td><td><div class="block">Creates a clone of the snapshot.</div><br></td></tr>
  <tr><td><code><a href="../statistics/IMultiStateObjectStatistics.html" title="interface in mod.chiselsandbits.api.multistate.statistics">IMultiStateObjectStatistics</a></code></td><td><code><a href="#getStatics()" class="member-name-link">getStatics</a>()</code></td><td><div class="block">Returns the statistics of the current snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshotType.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshotType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Gets the type of the snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#limitedToProgression(float)" class="member-name-link">limitedToProgression</a><wbr>(float&nbsp;progress)</code></td><td><div class="block">Creates a new snapshot which limits the currents snapshots contents to the given progression.</div><br></td></tr>
  <tr><td><code><a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#toItemStack()" class="member-name-link">toItemStack</a>()</code></td><td><div class="block">Converts the current snapshot to a variant which is itemstack capable.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a><a href="../../aabb/IAABBOwner.html#getBoundingBox()" title="getBoundingBox()">getBoundingBox</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a><a href="../accessor/IAreaAccessor.html#createNewShapeIdentifier()" title="createNewShapeIdentifier()">createNewShapeIdentifier</a>, <a href="../accessor/IAreaAccessor.html#createSnapshot()" title="createSnapshot()">createSnapshot</a>, <a href="../accessor/IAreaAccessor.html#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)" title="forEachWithPositionMutator(IPositionMutator, Consumer)">forEachWithPositionMutator</a>, <a href="../accessor/IAreaAccessor.html#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="isInside(BlockPos, Vec3)">isInside</a>, <a href="../accessor/IAreaAccessor.html#isInside(net.minecraft.world.phys.Vec3)" title="isInside(Vec3)">isInside</a>, <a href="../accessor/IAreaAccessor.html#stream()" title="stream()">stream</a>, <a href="../accessor/IAreaAccessor.html#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" title="streamWithPositionMutator(IPositionMutator)">streamWithPositionMutator</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="../mutator/IAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IAreaMutator</a><a href="../mutator/IAreaMutator.html#clearInAreaTarget(net.minecraft.world.phys.Vec3)" title="clearInAreaTarget(Vec3)">clearInAreaTarget</a>, <a href="../mutator/IAreaMutator.html#clearInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="clearInBlockTarget(BlockPos, Vec3)">clearInBlockTarget</a>, <a href="../mutator/IAreaMutator.html#mutableStream()" title="mutableStream()">mutableStream</a>, <a href="../mutator/IAreaMutator.html#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="overrideInAreaTarget(BlockInformation, BlockPos, Vec3)">overrideInAreaTarget</a>, <a href="../mutator/IAreaMutator.html#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" title="overrideInAreaTarget(BlockInformation, Vec3)">overrideInAreaTarget</a>, <a href="../mutator/IAreaMutator.html#setInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" title="setInAreaTarget(BlockInformation, Vec3)">setInAreaTarget</a>, <a href="../mutator/IAreaMutator.html#setInBlockTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="setInBlockTarget(BlockInformation, BlockPos, Vec3)">setInBlockTarget</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="../mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a><a href="../mutator/IMirrorAndRotateble.html#mirror(net.minecraft.core.Direction.Axis)" title="mirror(Direction.Axis)">mirror</a>, <a href="../mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis)" title="rotate(Direction.Axis)">rotate</a>, <a href="../mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis,int)" title="rotate(Direction.Axis, int)">rotate</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a><a href="../accessor/IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)" title="getInAreaTarget(Vec3)">getInAreaTarget</a>, <a href="../accessor/IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="getInBlockTarget(BlockPos, Vec3)">getInBlockTarget</a>
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="CODEC">

:::tabs
== CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
</div>
:::


</section>

<section id="STREAM_CODEC">

:::tabs
== STREAM_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</span>&nbsp;<span class="element-name">STREAM_CODEC</span></div>
</div>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getType()">

:::tabs
== getType
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IMultiStateSnapshotType.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshotType</a></span>&nbsp;<span class="element-name">getType</span>()</div>
Gets the type of the snapshot.
<dl class="notes">
<dt>Returns:</dt>
<dd>The type of the snapshot.</dd>
</dl>
</div>
:::


</section>

<section id="toItemStack()">

:::tabs
== toItemStack
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></span>&nbsp;<span class="element-name">toItemStack</span>()</div>
Converts the current snapshot to a variant which is itemstack capable.
<dl class="notes">
<dt>Returns:</dt>
<dd>The multistate itemstack which is the itemstack nbt representation of the current snapshot.</dd>
</dl>
</div>
:::


</section>

<section id="getStatics()">

:::tabs
== getStatics
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../statistics/IMultiStateObjectStatistics.html" title="interface in mod.chiselsandbits.api.multistate.statistics">IMultiStateObjectStatistics</a></span>&nbsp;<span class="element-name">getStatics</span>()</div>
Returns the statistics of the current snapshot.
<dl class="notes">
<dt>Returns:</dt>
<dd>The statistics</dd>
</dl>
</div>
:::


</section>

<section id="clone()">

:::tabs
== clone
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></span>&nbsp;<span class="element-name">clone</span>()</div>
Creates a clone of the snapshot.
<dl class="notes">
<dt>Returns:</dt>
<dd>The clone.</dd>
</dl>
</div>
:::


</section>

<section id="limitedToProgression(float)">

:::tabs
== limitedToProgression
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></span>&nbsp;<span class="element-name">limitedToProgression</span><wbr><span class="parameters">(float&nbsp;progress)</span></div>
Creates a new snapshot which limits the currents snapshots contents to the given progression.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>progress</code> - The current progress in procent</dd>
<dt>Returns:</dt>
<dd>The progress</dd>
</dl>
</div>
:::


</section>

:::::
  

