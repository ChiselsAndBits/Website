--- 
title: ISingleBlockAxisAlignedAreaAccessor
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor](index.md)  
# Interface ISingleBlockAxisAlignedAreaAccessor  
**All Extended Interfaces:**  
[IAABBOwner](../aabb/IAABBOwner.md), [IAreaAccessor](IAreaAccessor.md), [IStateAccessor](IStateAccessor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ISingleBlockAxisAlignedAreaAccessor</span><span class="extends-implements"><br/>  
extends <a href="IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></span></div>  

  

<div class="block">Represents a single block axis aligned area accessor</div>
  

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
  <tr><td><code><a href="../../item/multistate/IStatistics.html" title="interface in mod.chiselsandbits.api.item.multistate">IStatistics</a></code></td><td><code><a href="#getStatistics()" class="member-name-link">getStatistics</a>()</code></td><td><div class="block">The statistics of the itemstack.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../item/multistate/IStatistics.html" title="interface in mod.chiselsandbits.api.item.multistate">IStatistics</a></code></td><td><code><a href="#getStatistics()" class="member-name-link">getStatistics</a>()</code></td><td><div class="block">The statistics of the itemstack.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../item/multistate/IStatistics.html" title="interface in mod.chiselsandbits.api.item.multistate">IStatistics</a></code></td><td><code><a href="#getStatistics()" class="member-name-link">getStatistics</a>()</code></td><td><div class="block">The statistics of the itemstack.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a>
<a href="../../aabb/IAABBOwner.html#getBoundingBox()">getBoundingBox</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>
<a href="IAreaAccessor.html#createNewShapeIdentifier()">createNewShapeIdentifier</a>, <a href="IAreaAccessor.html#createSnapshot()">createSnapshot</a>, <a href="IAreaAccessor.html#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)">forEachWithPositionMutator</a>, <a href="IAreaAccessor.html#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">isInside</a>, <a href="IAreaAccessor.html#isInside(net.minecraft.world.phys.Vec3)">isInside</a>, <a href="IAreaAccessor.html#stream()">stream</a>, <a href="IAreaAccessor.html#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)">streamWithPositionMutator</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>
<a href="IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)">getInAreaTarget</a>, <a href="IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">getInBlockTarget</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getStatistics()">

:::tabs
== getStatistics
<div class="member-signature"><span class="return-type"><a href="../../item/multistate/IStatistics.html" title="interface in mod.chiselsandbits.api.item.multistate">IStatistics</a></span>&nbsp;<span class="element-name">getStatistics</span>()</div>
<div class="block">The statistics of the itemstack.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The statistics.</dd>
</dl>
:::


</section>

:::::
  

