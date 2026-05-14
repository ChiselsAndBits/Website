--- 
title: IWorldObject
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Interface IWorldObject  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWorldObject</span></div>  

  

Represents a 3D object in world.  

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
  <tr><td><code>default net.minecraft.world.phys.AABB</code></td><td><code><a href="#getInWorldBoundingBox()" class="member-name-link">getInWorldBoundingBox</a>()</code></td><td><div class="block">Gives access to the in world axis aligned bounding box of the object.</div><br></td></tr>
  <tr><td><code>default net.minecraft.core.BlockPos</code></td><td><code><a href="#getInWorldEndBlockPoint()" class="member-name-link">getInWorldEndBlockPoint</a>()</code></td><td><div class="block">The end block point of the object in the world.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldEndPoint()" class="member-name-link">getInWorldEndPoint</a>()</code></td><td><div class="block">The end point of the object in the world.</div><br></td></tr>
  <tr><td><code>default net.minecraft.core.BlockPos</code></td><td><code><a href="#getInWorldStartBlockPoint()" class="member-name-link">getInWorldStartBlockPoint</a>()</code></td><td><div class="block">The start block point of the object in the world.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldStartPoint()" class="member-name-link">getInWorldStartPoint</a>()</code></td><td><div class="block">The start point of the object in the world.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.level.LevelAccessor</code></td><td><code><a href="#getWorld()" class="member-name-link">getWorld</a>()</code></td><td><div class="block">The world the object is in.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.AABB</code></td><td><code><a href="#getInWorldBoundingBox()" class="member-name-link">getInWorldBoundingBox</a>()</code></td><td><div class="block">Gives access to the in world axis aligned bounding box of the object.</div><br></td></tr>
  <tr><td><code>default net.minecraft.core.BlockPos</code></td><td><code><a href="#getInWorldEndBlockPoint()" class="member-name-link">getInWorldEndBlockPoint</a>()</code></td><td><div class="block">The end block point of the object in the world.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldEndPoint()" class="member-name-link">getInWorldEndPoint</a>()</code></td><td><div class="block">The end point of the object in the world.</div><br></td></tr>
  <tr><td><code>default net.minecraft.core.BlockPos</code></td><td><code><a href="#getInWorldStartBlockPoint()" class="member-name-link">getInWorldStartBlockPoint</a>()</code></td><td><div class="block">The start block point of the object in the world.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldStartPoint()" class="member-name-link">getInWorldStartPoint</a>()</code></td><td><div class="block">The start point of the object in the world.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.level.LevelAccessor</code></td><td><code><a href="#getWorld()" class="member-name-link">getWorld</a>()</code></td><td><div class="block">The world the object is in.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldEndPoint()" class="member-name-link">getInWorldEndPoint</a>()</code></td><td><div class="block">The end point of the object in the world.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getInWorldStartPoint()" class="member-name-link">getInWorldStartPoint</a>()</code></td><td><div class="block">The start point of the object in the world.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.level.LevelAccessor</code></td><td><code><a href="#getWorld()" class="member-name-link">getWorld</a>()</code></td><td><div class="block">The world the object is in.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.AABB</code></td><td><code><a href="#getInWorldBoundingBox()" class="member-name-link">getInWorldBoundingBox</a>()</code></td><td><div class="block">Gives access to the in world axis aligned bounding box of the object.</div><br></td></tr>
  <tr><td><code>default net.minecraft.core.BlockPos</code></td><td><code><a href="#getInWorldEndBlockPoint()" class="member-name-link">getInWorldEndBlockPoint</a>()</code></td><td><div class="block">The end block point of the object in the world.</div><br></td></tr>
  <tr><td><code>default net.minecraft.core.BlockPos</code></td><td><code><a href="#getInWorldStartBlockPoint()" class="member-name-link">getInWorldStartBlockPoint</a>()</code></td><td><div class="block">The start block point of the object in the world.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getWorld()">
:::tabs
== getWorld
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.level.LevelAccessor</span>&nbsp;<span class="element-name">getWorld</span>()</div>
The world the object is in.
<dl class="notes">
<dt>Returns:</dt>
<dd>The world.</dd>
</dl>
</div>
:::
</section>
<section id="getInWorldStartPoint()">
:::tabs
== getInWorldStartPoint
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getInWorldStartPoint</span>()</div>
The start point of the object in the world.
<dl class="notes">
<dt>Returns:</dt>
<dd>The start point.</dd>
</dl>
</div>
:::
</section>
<section id="getInWorldEndPoint()">
:::tabs
== getInWorldEndPoint
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getInWorldEndPoint</span>()</div>
The end point of the object in the world.
<dl class="notes">
<dt>Returns:</dt>
<dd>The end point.</dd>
</dl>
</div>
:::
</section>
<section id="getInWorldStartBlockPoint()">
:::tabs
== getInWorldStartBlockPoint
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">getInWorldStartBlockPoint</span>()</div>
The start block point of the object in the world.
<dl class="notes">
<dt>Returns:</dt>
<dd>The start point.</dd>
</dl>
</div>
:::
</section>
<section id="getInWorldEndBlockPoint()">
:::tabs
== getInWorldEndBlockPoint
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">getInWorldEndBlockPoint</span>()</div>
The end block point of the object in the world.
<dl class="notes">
<dt>Returns:</dt>
<dd>The end point.</dd>
</dl>
</div>
:::
</section>
<section id="getInWorldBoundingBox()">
:::tabs
== getInWorldBoundingBox
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.AABB</span>&nbsp;<span class="element-name">getInWorldBoundingBox</span>()</div>
Gives access to the in world axis aligned bounding box of the object.
<dl class="notes">
<dt>Returns:</dt>
<dd>The axis aligned bounding box.</dd>
</dl>
</div>
:::
</section>
:::::
  

