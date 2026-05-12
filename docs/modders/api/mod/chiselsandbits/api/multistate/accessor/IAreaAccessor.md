--- 
title: IAreaAccessor
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor](index.md)  
# Interface IAreaAccessor  
**All Extended Interfaces:**  
[IAABBOwner](../../aabb/IAABBOwner.md), [IStateAccessor](IStateAccessor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IAreaAccessor</span><span class="extends-implements"><br/>  
extends <a href="IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>, <a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a></span></div>  

  

Gives access to all states in a given area.
Might be larger than a single block.  

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
  <tr><td><code><a href="identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a></code></td><td><code><a href="#createNewShapeIdentifier()" class="member-name-link">createNewShapeIdentifier</a>()</code></td><td><div class="block">Creates a new area shape identifier.</div><br></td></tr>
  <tr><td><code><a href="../snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td><div class="block">Creates a snapshot of the current state.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)" class="member-name-link">forEachWithPositionMutator</a><wbr>(<a href="sortable/IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;positionMutator,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&nbsp;consumer)</code></td><td><div class="block">Runs a for each-loop over the states inside the accessor, with the ability to specify the loop order.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">isInside</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Indicates if the given target (with the given block position offset) is inside of the current accessor.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInside(net.minecraft.world.phys.Vec3)" class="member-name-link">isInside</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Indicates if the given target is inside of the current accessor.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#stream()" class="member-name-link">stream</a>()</code></td><td><div class="block">Gives access to a stream with the entry state info inside the accessors range.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" class="member-name-link">streamWithPositionMutator</a><wbr>(<a href="sortable/IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;positionMutator)</code></td><td><div class="block">Gives access to a stream with the entry state info inside the accessors range.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a></code></td><td><code><a href="#createNewShapeIdentifier()" class="member-name-link">createNewShapeIdentifier</a>()</code></td><td><div class="block">Creates a new area shape identifier.</div><br></td></tr>
  <tr><td><code><a href="../snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td><div class="block">Creates a snapshot of the current state.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)" class="member-name-link">forEachWithPositionMutator</a><wbr>(<a href="sortable/IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;positionMutator,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&nbsp;consumer)</code></td><td><div class="block">Runs a for each-loop over the states inside the accessor, with the ability to specify the loop order.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">isInside</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Indicates if the given target (with the given block position offset) is inside of the current accessor.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInside(net.minecraft.world.phys.Vec3)" class="member-name-link">isInside</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Indicates if the given target is inside of the current accessor.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#stream()" class="member-name-link">stream</a>()</code></td><td><div class="block">Gives access to a stream with the entry state info inside the accessors range.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" class="member-name-link">streamWithPositionMutator</a><wbr>(<a href="sortable/IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;positionMutator)</code></td><td><div class="block">Gives access to a stream with the entry state info inside the accessors range.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a></code></td><td><code><a href="#createNewShapeIdentifier()" class="member-name-link">createNewShapeIdentifier</a>()</code></td><td><div class="block">Creates a new area shape identifier.</div><br></td></tr>
  <tr><td><code><a href="../snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td><div class="block">Creates a snapshot of the current state.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)" class="member-name-link">forEachWithPositionMutator</a><wbr>(<a href="sortable/IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;positionMutator,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&nbsp;consumer)</code></td><td><div class="block">Runs a for each-loop over the states inside the accessor, with the ability to specify the loop order.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">isInside</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Indicates if the given target (with the given block position offset) is inside of the current accessor.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInside(net.minecraft.world.phys.Vec3)" class="member-name-link">isInside</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Indicates if the given target is inside of the current accessor.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#stream()" class="member-name-link">stream</a>()</code></td><td><div class="block">Gives access to a stream with the entry state info inside the accessors range.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" class="member-name-link">streamWithPositionMutator</a><wbr>(<a href="sortable/IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;positionMutator)</code></td><td><div class="block">Gives access to a stream with the entry state info inside the accessors range.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a><a href="../../aabb/IAABBOwner.html#getBoundingBox()" title="getBoundingBox()">getBoundingBox</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a><a href="IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)" title="getInAreaTarget(Vec3)">getInAreaTarget</a>, <a href="IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="getInBlockTarget(BlockPos, Vec3)">getInBlockTarget</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="createNewShapeIdentifier()">

:::tabs
== createNewShapeIdentifier
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a></span>&nbsp;<span class="element-name">createNewShapeIdentifier</span>()</div>
<div class="block">Creates a new area shape identifier.

Note: This method always returns a new instance.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The new identifier.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="stream()">

:::tabs
== stream
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</span>&nbsp;<span class="element-name">stream</span>()</div>
<div class="block">Gives access to a stream with the entry state info inside the accessors range.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The stream with the inner states.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="isInside(net.minecraft.world.phys.Vec3)">

:::tabs
== isInside
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isInside</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</span></div>
<div class="block">Indicates if the given target is inside of the current accessor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inAreaTarget</code> - The area target to check.</dd>
<dt>Returns:</dt>
<dd>True when inside, false when not.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">

:::tabs
== isInside
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isInside</span><wbr><span class="parameters">(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,
 net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</span></div>
<div class="block">Indicates if the given target (with the given block position offset) is inside of the current accessor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inAreaBlockPosOffset</code> - The offset of blocks in the current area.</dd>
<dd><code>inBlockTarget</code> - The offset in the targeted block.</dd>
<dt>Returns:</dt>
<dd>True when inside, false when not.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="createSnapshot()">

:::tabs
== createSnapshot
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></span>&nbsp;<span class="element-name">createSnapshot</span>()</div>
<div class="block">Creates a snapshot of the current state.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The snapshot.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)">

:::tabs
== streamWithPositionMutator
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</span>&nbsp;<span class="element-name">streamWithPositionMutator</span><wbr><span class="parameters">(<a href="sortable/IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;positionMutator)</span></div>
<div class="block">Gives access to a stream with the entry state info inside the accessors range.
Allows for the entry state order to be mutated using a position mutator.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>positionMutator</code> - The mutator for the positional order.</dd>
<dt>Returns:</dt>
<dd>The stream with the inner states.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)">

:::tabs
== forEachWithPositionMutator
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">forEachWithPositionMutator</span><wbr><span class="parameters">(<a href="sortable/IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;positionMutator,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&nbsp;consumer)</span></div>
<div class="block">Runs a for each-loop over the states inside the accessor, with the ability to specify the loop order.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>positionMutator</code> - The position mutator to use.</dd>
<dd><code>consumer</code> - The consumer to pass the states to.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

