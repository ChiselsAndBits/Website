--- 
title: IAreaMutator
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.mutator](index.md)  
# Interface IAreaMutator  
**All Extended Interfaces:**  
[IAABBOwner](../../aabb/IAABBOwner.md), [IAreaAccessor](../accessor/IAreaAccessor.md), [IStateAccessor](../accessor/IStateAccessor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IAreaMutator</span><span class="extends-implements"><br/>  
extends <a href="../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></span></div>  

  

A mutator for a given area.  

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
  <tr><td><code>void</code></td><td><code><a href="#clearInAreaTarget(net.minecraft.world.phys.Vec3)" class="member-name-link">clearInAreaTarget</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Clears the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clearInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">clearInBlockTarget</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Clears the current area, using the in area block position offset as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IMutableStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutableStateEntryInfo</a>&gt;</code></td><td><code><a href="#mutableStream()" class="member-name-link">mutableStream</a>()</code></td><td><div class="block">Returns all entries in the current area in a mutable fashion.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">overrideInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Overrides the target block information in the current area, using the in area block position offset as well<br>as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">overrideInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Overrides the target block information in the current area, using the offset from the<br>area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">setInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Sets the target block information in the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setInBlockTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">setInBlockTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Sets the target block information in the current area, using the in area block position offset<br>as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clearInAreaTarget(net.minecraft.world.phys.Vec3)" class="member-name-link">clearInAreaTarget</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Clears the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clearInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">clearInBlockTarget</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Clears the current area, using the in area block position offset as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IMutableStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutableStateEntryInfo</a>&gt;</code></td><td><code><a href="#mutableStream()" class="member-name-link">mutableStream</a>()</code></td><td><div class="block">Returns all entries in the current area in a mutable fashion.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">overrideInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Overrides the target block information in the current area, using the in area block position offset as well<br>as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">overrideInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Overrides the target block information in the current area, using the offset from the<br>area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">setInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Sets the target block information in the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setInBlockTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">setInBlockTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Sets the target block information in the current area, using the in area block position offset<br>as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clearInAreaTarget(net.minecraft.world.phys.Vec3)" class="member-name-link">clearInAreaTarget</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Clears the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clearInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">clearInBlockTarget</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Clears the current area, using the in area block position offset as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IMutableStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutableStateEntryInfo</a>&gt;</code></td><td><code><a href="#mutableStream()" class="member-name-link">mutableStream</a>()</code></td><td><div class="block">Returns all entries in the current area in a mutable fashion.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">setInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Sets the target block information in the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setInBlockTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">setInBlockTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Sets the target block information in the current area, using the in area block position offset<br>as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">overrideInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Overrides the target block information in the current area, using the in area block position offset as well<br>as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">overrideInAreaTarget</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Overrides the target block information in the current area, using the offset from the<br>area as well as the in area target offset.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a>
<a href="../../aabb/IAABBOwner.html#getBoundingBox()" title="getBoundingBox()">getBoundingBox</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>
<a href="../accessor/IAreaAccessor.html#createNewShapeIdentifier()" title="createNewShapeIdentifier()">createNewShapeIdentifier</a>, <a href="../accessor/IAreaAccessor.html#createSnapshot()" title="createSnapshot()">createSnapshot</a>, <a href="../accessor/IAreaAccessor.html#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)" title="forEachWithPositionMutator(IPositionMutator, Consumer)">forEachWithPositionMutator</a>, <a href="../accessor/IAreaAccessor.html#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="isInside(BlockPos, Vec3)">isInside</a>, <a href="../accessor/IAreaAccessor.html#isInside(net.minecraft.world.phys.Vec3)" title="isInside(Vec3)">isInside</a>, <a href="../accessor/IAreaAccessor.html#stream()" title="stream()">stream</a>, <a href="../accessor/IAreaAccessor.html#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" title="streamWithPositionMutator(IPositionMutator)">streamWithPositionMutator</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>
<a href="../accessor/IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)" title="getInAreaTarget(Vec3)">getInAreaTarget</a>, <a href="../accessor/IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="getInBlockTarget(BlockPos, Vec3)">getInBlockTarget</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="mutableStream()">

:::tabs
== mutableStream
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;<a href="IMutableStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutableStateEntryInfo</a>&gt;</span>&nbsp;<span class="element-name">mutableStream</span>()</div>
Returns all entries in the current area in a mutable fashion.
Includes all empty areas as areas containing an air state.
<dl class="notes">
<dt>Returns:</dt>
<dd>A stream with a mutable state entry info for each mutable section in the area.</dd>
</dl>
</div>
:::


</section>

<section id="setInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)">

:::tabs
== setInAreaTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setInAreaTarget</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</span>
              throws <span class="exceptions"><a href="../../exceptions/SpaceOccupiedException.html" title="class in mod.chiselsandbits.api.exceptions">SpaceOccupiedException</a></span></div>
Sets the target block information in the current area, using the offset from the area as well as the in area target offset.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>inAreaTarget</code> - The in area offset.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../exceptions/SpaceOccupiedException.html" title="class in mod.chiselsandbits.api.exceptions">SpaceOccupiedException</a></code> - When the space is not clear and as such the bit can not be set.</dd>
</dl>
</div>
:::


</section>

<section id="setInBlockTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">

:::tabs
== setInBlockTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setInBlockTarget</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,
 net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</span>
               throws <span class="exceptions"><a href="../../exceptions/SpaceOccupiedException.html" title="class in mod.chiselsandbits.api.exceptions">SpaceOccupiedException</a></span></div>
Sets the target block information in the current area, using the in area block position offset
as well as the in block target offset to calculate the in area offset for setting.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>inAreaBlockPosOffset</code> - The offset of blocks in the current area.</dd>
<dd><code>inBlockTarget</code> - The offset in the targeted block.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../exceptions/SpaceOccupiedException.html" title="class in mod.chiselsandbits.api.exceptions">SpaceOccupiedException</a></code> - When the space is not clear and as such the bit can not be set.</dd>
</dl>
</div>
:::


</section>

<section id="clearInAreaTarget(net.minecraft.world.phys.Vec3)">

:::tabs
== clearInAreaTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clearInAreaTarget</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</span></div>
Clears the current area, using the offset from the area as well as the in area target offset.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inAreaTarget</code> - The in area offset.</dd>
</dl>
</div>
:::


</section>

<section id="clearInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">

:::tabs
== clearInBlockTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clearInBlockTarget</span><wbr><span class="parameters">(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,
 net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</span></div>
Clears the current area, using the in area block position offset as well as the in block target offset to calculate the in area offset for setting.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inAreaBlockPosOffset</code> - The offset of blocks in the current area.</dd>
<dd><code>inBlockTarget</code> - The offset in the targeted block.</dd>
</dl>
</div>
:::


</section>

<section id="overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)">

:::tabs
== overrideInAreaTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">overrideInAreaTarget</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</span></div>
Overrides the target block information in the current area, using the offset from the
area as well as the in area target offset.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>inAreaTarget</code> - The in area offset.</dd>
</dl>
</div>
:::


</section>

<section id="overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">

:::tabs
== overrideInAreaTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">overrideInAreaTarget</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,
 net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</span></div>
Overrides the target block information in the current area, using the in area block position offset as well
as the in block target offset to calculate the in area offset for setting.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>inAreaBlockPosOffset</code> - The offset of blocks in the current area.</dd>
<dd><code>inBlockTarget</code> - The offset in the targeted block.</dd>
</dl>
</div>
:::


</section>

:::::
  

