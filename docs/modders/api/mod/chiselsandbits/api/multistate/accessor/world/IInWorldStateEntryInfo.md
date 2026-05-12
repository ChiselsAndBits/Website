--- 
title: IInWorldStateEntryInfo
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor.world](index.md)  
# Interface IInWorldStateEntryInfo  
**All Extended Interfaces:**  
[IAABBOwner](../../../aabb/IAABBOwner.md), [IStateEntryInfo](../IStateEntryInfo.md), [IWorldObject](../../../util/IWorldObject.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IInWorldStateEntryInfo</span><span class="extends-implements"><br/>  
extends <a href="../IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>, <a href="../../../util/IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a></span></div>  

  

Represents a single state entry that actually exists in a physical world.  

<dl class="notes"><br/>  
<dt>See Also:</dt><br/>  
<dd><br/>  
<ul class="tag-list"><br/>  
<li><a href="../IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IStateEntryInfo</code></a></li><br/>  
<li><a href="IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world"><code>IWorldAreaAccessor</code></a></li><br/>  
</ul><br/>  
</dd><br/>  
</dl>  

<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#getBlockPos()" class="member-name-link">getBlockPos</a>()</code></td><td><div class="block">The position of the block that this state entry is part of.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldCenterPoint()" class="member-name-link">getInWorldCenterPoint</a>()</code></td><td><div class="block">The center position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldEndPoint()" class="member-name-link">getInWorldEndPoint</a>()</code></td><td><div class="block">The end (highest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldStartPoint()" class="member-name-link">getInWorldStartPoint</a>()</code></td><td><div class="block">The start (lowest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#getBlockPos()" class="member-name-link">getBlockPos</a>()</code></td><td><div class="block">The position of the block that this state entry is part of.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldCenterPoint()" class="member-name-link">getInWorldCenterPoint</a>()</code></td><td><div class="block">The center position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldEndPoint()" class="member-name-link">getInWorldEndPoint</a>()</code></td><td><div class="block">The end (highest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldStartPoint()" class="member-name-link">getInWorldStartPoint</a>()</code></td><td><div class="block">The start (lowest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#getBlockPos()" class="member-name-link">getBlockPos</a>()</code></td><td><div class="block">The position of the block that this state entry is part of.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldCenterPoint()" class="member-name-link">getInWorldCenterPoint</a>()</code></td><td><div class="block">The center position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldEndPoint()" class="member-name-link">getInWorldEndPoint</a>()</code></td><td><div class="block">The end (highest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldStartPoint()" class="member-name-link">getInWorldStartPoint</a>()</code></td><td><div class="block">The start (lowest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a><a href="../IStateEntryInfo.html#getBlockInformation()" title="getBlockInformation()">getBlockInformation</a>, <a href="../IStateEntryInfo.html#getBoundingBox()" title="getBoundingBox()">getBoundingBox</a>, <a href="../IStateEntryInfo.html#getCenterPoint()" title="getCenterPoint()">getCenterPoint</a>, <a href="../IStateEntryInfo.html#getEndPoint()" title="getEndPoint()">getEndPoint</a>, <a href="../IStateEntryInfo.html#getStartPoint()" title="getStartPoint()">getStartPoint</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../../util/IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a><a href="../../../util/IWorldObject.html#getInWorldBoundingBox()" title="getInWorldBoundingBox()">getInWorldBoundingBox</a>, <a href="../../../util/IWorldObject.html#getInWorldEndBlockPoint()" title="getInWorldEndBlockPoint()">getInWorldEndBlockPoint</a>, <a href="../../../util/IWorldObject.html#getInWorldStartBlockPoint()" title="getInWorldStartBlockPoint()">getInWorldStartBlockPoint</a>, <a href="../../../util/IWorldObject.html#getWorld()" title="getWorld()">getWorld</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getBlockPos()">

:::tabs
== getBlockPos
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">getBlockPos</span>()</div>
<div class="block">The position of the block that this state entry is part of.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The in world block position.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getInWorldStartPoint()">

:::tabs
== getInWorldStartPoint
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getInWorldStartPoint</span>()</div>
<div class="block">The start (lowest on all three axi) position of the state that this entry occupies.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../util/IWorldObject.html#getInWorldStartPoint()">getInWorldStartPoint</a></code>&nbsp;in interface&nbsp;<code><a href="../../../util/IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a></code></dd>
<dt>Returns:</dt>
<dd>The start position of this entry in the given world.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getInWorldEndPoint()">

:::tabs
== getInWorldEndPoint
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getInWorldEndPoint</span>()</div>
<div class="block">The end (highest on all three axi) position of the state that this entry occupies.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../util/IWorldObject.html#getInWorldEndPoint()">getInWorldEndPoint</a></code>&nbsp;in interface&nbsp;<code><a href="../../../util/IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a></code></dd>
<dt>Returns:</dt>
<dd>The end position of this entry in the given world.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getInWorldCenterPoint()">

:::tabs
== getInWorldCenterPoint
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getInWorldCenterPoint</span>()</div>
<div class="block">The center position of the state that this entry occupies.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The center position of this entry in the given world.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

