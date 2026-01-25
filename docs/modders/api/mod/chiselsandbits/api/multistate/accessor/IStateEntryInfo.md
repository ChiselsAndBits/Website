--- 
title: IStateEntryInfo
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor](index.md)  
# Interface IStateEntryInfo  
**All Extended Interfaces:**  
[IAABBOwner](../../aabb/IAABBOwner.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IStateEntryInfo</span><span class="extends-implements"><br/>  
extends <a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a></span></div>  

  

Represents a single entry inside an area which can have multiple states.  

<dl class="notes"><br/>  
<dt>See Also:</dt><br/>  
<dd><br/>  
<ul class="tag-list"><br/>  
<li><a href="IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IAreaAccessor</code></a></li><br/>  
<li><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world"><code>IWorldAreaAccessor</code></a></li><br/>  
<li><a href="world/IInWorldStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world"><code>IInWorldStateEntryInfo</code></a></li><br/>  
</ul><br/>  
</dd><br/>  
</dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation()" class="member-name-link">getBlockInformation</a>()</code></td><td><div class="block">The state that this entry represents.</div><br></td></tr>
  <tr><td><code>default @NotNull net.minecraft.world.phys.AABB</code></td><td><code><a href="#getBoundingBox()" class="member-name-link">getBoundingBox</a>()</code></td><td><div class="block">Gives access to the bounding box of this object.</div><br></td></tr>
  <tr><td><code>default @NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getCenterPoint()" class="member-name-link">getCenterPoint</a>()</code></td><td><div class="block">The center point of the entry in the current block.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getEndPoint()" class="member-name-link">getEndPoint</a>()</code></td><td><div class="block">The end (highest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getStartPoint()" class="member-name-link">getStartPoint</a>()</code></td><td><div class="block">The start (lowest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation()" class="member-name-link">getBlockInformation</a>()</code></td><td><div class="block">The state that this entry represents.</div><br></td></tr>
  <tr><td><code>default @NotNull net.minecraft.world.phys.AABB</code></td><td><code><a href="#getBoundingBox()" class="member-name-link">getBoundingBox</a>()</code></td><td><div class="block">Gives access to the bounding box of this object.</div><br></td></tr>
  <tr><td><code>default @NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getCenterPoint()" class="member-name-link">getCenterPoint</a>()</code></td><td><div class="block">The center point of the entry in the current block.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getEndPoint()" class="member-name-link">getEndPoint</a>()</code></td><td><div class="block">The end (highest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getStartPoint()" class="member-name-link">getStartPoint</a>()</code></td><td><div class="block">The start (lowest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation()" class="member-name-link">getBlockInformation</a>()</code></td><td><div class="block">The state that this entry represents.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getEndPoint()" class="member-name-link">getEndPoint</a>()</code></td><td><div class="block">The end (highest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getStartPoint()" class="member-name-link">getStartPoint</a>()</code></td><td><div class="block">The start (lowest on all three axi) position of the state that this entry occupies.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default @NotNull net.minecraft.world.phys.AABB</code></td><td><code><a href="#getBoundingBox()" class="member-name-link">getBoundingBox</a>()</code></td><td><div class="block">Gives access to the bounding box of this object.</div><br></td></tr>
  <tr><td><code>default @NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getCenterPoint()" class="member-name-link">getCenterPoint</a>()</code></td><td><div class="block">The center point of the entry in the current block.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getBlockInformation()">

:::tabs
== getBlockInformation
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getBlockInformation</span>()</div>
The state that this entry represents.
<dl class="notes">
<dt>Returns:</dt>
<dd>The state.</dd>
</dl>
:::


</section>

<section id="getStartPoint()">

:::tabs
== getStartPoint
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getStartPoint</span>()</div>
The start (lowest on all three axi) position of the state that this entry occupies.
<dl class="notes">
<dt>Returns:</dt>
<dd>The start position of this entry in the given block.</dd>
</dl>
:::


</section>

<section id="getEndPoint()">

:::tabs
== getEndPoint
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getEndPoint</span>()</div>
The end (highest on all three axi) position of the state that this entry occupies.
<dl class="notes">
<dt>Returns:</dt>
<dd>The start position of this entry in the given block.</dd>
</dl>
:::


</section>

<section id="getCenterPoint()">

:::tabs
== getCenterPoint
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">default</span>&nbsp;<span class="return-type">@NotNull net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getCenterPoint</span>()</div>
The center point of the entry in the current block.
<dl class="notes">
<dt>Returns:</dt>
<dd>The center position of this entry in the given block.</dd>
</dl>
:::


</section>

<section id="getBoundingBox()">

:::tabs
== getBoundingBox
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">default</span>&nbsp;<span class="return-type">@NotNull net.minecraft.world.phys.AABB</span>&nbsp;<span class="element-name">getBoundingBox</span>()</div>
Gives access to the bounding box of this object.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../aabb/IAABBOwner.html#getBoundingBox()">getBoundingBox</a></code>&nbsp;in interface&nbsp;<code><a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a></code></dd>
<dt>Returns:</dt>
<dd>The axis aligned bounding box.</dd>
</dl>
:::


</section>

:::::
  

