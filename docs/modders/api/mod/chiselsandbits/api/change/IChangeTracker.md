--- 
title: IChangeTracker
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.change](index.md)  
# Interface IChangeTracker  
**All Extended Interfaces:**  
[IChangeHandler](changes/IChangeHandler.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChangeTracker</span><span class="extends-implements"><br/>  
extends <a href="changes/IChangeHandler.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeHandler</a></span></div>  

  

The change tracker for tracking changes to bit blocks.
Currently still work in progress.  

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
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears the tracker from all currently stored changes.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Deque.html" title="class or interface in java.util" class="external-link">Deque</a><wbr>&lt;<a href="changes/IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#getChanges()" class="member-name-link">getChanges</a>()</code></td><td><div class="block">Gets a readonly-copy of the changes in the queue.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onBlocksUpdated(java.util.Map,java.util.Map)" class="member-name-link">onBlocksUpdated</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;net.minecraft.core.BlockPos, <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;&nbsp;beforeStates,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;net.minecraft.core.BlockPos, <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;&nbsp;afterState)</code></td><td><div class="block">Invoked when several chiseled blocks are updated from one state to the next.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onBlockUpdated(net.minecraft.core.BlockPos,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">onBlockUpdated</a><wbr>(net.minecraft.core.BlockPos&nbsp;blockPos,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;before,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;after)</code></td><td><div class="block">Invoked when a chiseled block is updated from one state to the next.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setChanges(java.util.Deque)" class="member-name-link">setChanges</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Deque.html" title="class or interface in java.util" class="external-link">Deque</a>&lt;<a href="changes/IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;&nbsp;changes)</code></td><td><div class="block">Sets the changes in the tracker.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears the tracker from all currently stored changes.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Deque.html" title="class or interface in java.util" class="external-link">Deque</a><wbr>&lt;<a href="changes/IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#getChanges()" class="member-name-link">getChanges</a>()</code></td><td><div class="block">Gets a readonly-copy of the changes in the queue.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onBlocksUpdated(java.util.Map,java.util.Map)" class="member-name-link">onBlocksUpdated</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;net.minecraft.core.BlockPos, <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;&nbsp;beforeStates,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;net.minecraft.core.BlockPos, <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;&nbsp;afterState)</code></td><td><div class="block">Invoked when several chiseled blocks are updated from one state to the next.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onBlockUpdated(net.minecraft.core.BlockPos,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">onBlockUpdated</a><wbr>(net.minecraft.core.BlockPos&nbsp;blockPos,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;before,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;after)</code></td><td><div class="block">Invoked when a chiseled block is updated from one state to the next.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setChanges(java.util.Deque)" class="member-name-link">setChanges</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Deque.html" title="class or interface in java.util" class="external-link">Deque</a>&lt;<a href="changes/IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;&nbsp;changes)</code></td><td><div class="block">Sets the changes in the tracker.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears the tracker from all currently stored changes.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Deque.html" title="class or interface in java.util" class="external-link">Deque</a><wbr>&lt;<a href="changes/IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#getChanges()" class="member-name-link">getChanges</a>()</code></td><td><div class="block">Gets a readonly-copy of the changes in the queue.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onBlocksUpdated(java.util.Map,java.util.Map)" class="member-name-link">onBlocksUpdated</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;net.minecraft.core.BlockPos, <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;&nbsp;beforeStates,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;net.minecraft.core.BlockPos, <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;&nbsp;afterState)</code></td><td><div class="block">Invoked when several chiseled blocks are updated from one state to the next.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setChanges(java.util.Deque)" class="member-name-link">setChanges</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Deque.html" title="class or interface in java.util" class="external-link">Deque</a>&lt;<a href="changes/IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;&nbsp;changes)</code></td><td><div class="block">Sets the changes in the tracker.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#onBlockUpdated(net.minecraft.core.BlockPos,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">onBlockUpdated</a><wbr>(net.minecraft.core.BlockPos&nbsp;blockPos,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;before,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;after)</code></td><td><div class="block">Invoked when a chiseled block is updated from one state to the next.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;mod.chiselsandbits.api.change.changes.<a href="changes/IChangeHandler.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeHandler</a><a href="changes/IChangeHandler.html#canRedo(net.minecraft.world.entity.player.Player)" title="canRedo(Player)">canRedo</a>, <a href="changes/IChangeHandler.html#canUndo(net.minecraft.world.entity.player.Player)" title="canUndo(Player)">canUndo</a>, <a href="changes/IChangeHandler.html#redo(net.minecraft.world.entity.player.Player)" title="redo(Player)">redo</a>, <a href="changes/IChangeHandler.html#undo(net.minecraft.world.entity.player.Player)" title="undo(Player)">undo</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="onBlockUpdated(net.minecraft.core.BlockPos,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)">

:::tabs
== onBlockUpdated
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">onBlockUpdated</span><wbr><span class="parameters">(net.minecraft.core.BlockPos&nbsp;blockPos,
 <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;before,
 <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;after)</span></div>
<div class="block">Invoked when a chiseled block is updated from one state to the next.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockPos</code> - The position of the block updated.</dd>
<dd><code>before</code> - The before state.</dd>
<dd><code>after</code> - The after state.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="onBlocksUpdated(java.util.Map,java.util.Map)">

:::tabs
== onBlocksUpdated
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">onBlocksUpdated</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;net.minecraft.core.BlockPos, <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;&nbsp;beforeStates,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;net.minecraft.core.BlockPos, <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;&nbsp;afterState)</span></div>
<div class="block">Invoked when several chiseled blocks are updated from one state to the next.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>beforeStates</code> - The states before the update.</dd>
<dd><code>afterState</code> - The states after the update.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getChanges()">

:::tabs
== getChanges
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Deque.html" title="class or interface in java.util" class="external-link">Deque</a>&lt;<a href="changes/IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</span>&nbsp;<span class="element-name">getChanges</span>()</div>
<div class="block">Gets a readonly-copy of the changes in the queue.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The changes last performed and recorded by this tracker.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="setChanges(java.util.Deque)">

:::tabs
== setChanges
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setChanges</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Deque.html" title="class or interface in java.util" class="external-link">Deque</a>&lt;<a href="changes/IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;&nbsp;changes)</span></div>
<div class="block">Sets the changes in the tracker.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changes</code> - The changes to set.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="clear()">

:::tabs
== clear
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clear</span>()</div>
<div class="block">Clears the tracker from all currently stored changes.</div>
</div>
:::


</section>

</li>
</ul>
:::::
  

