--- 
title: IAreaAccessorWithVoxelShape
aside: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor](index.md)  
# Interface IAreaAccessorWithVoxelShape  
**All Extended Interfaces:**  
[IAABBOwner](../aabb/IAABBOwner.md), [IAreaAccessor](IAreaAccessor.md), [IStateAccessor](IStateAccessor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IAreaAccessorWithVoxelShape</span><span class="extends-implements"><br/>  
extends <a href="IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></span></div>  

  

<div class="block">A special <a href="IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IAreaAccessor</code></a> that is capable of determining its own voxelshape.</div>
  

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
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#provideShape(mod.chiselsandbits.api.axissize.CollisionType,net.minecraft.core.BlockPos,boolean)" class="member-name-link">provideShape</a><wbr>(<a href="../../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;type,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Determines the voxelshape of the <a href="IAreaAccessorWithVoxelShape.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IAreaAccessorWithVoxelShape</code></a> at the given position.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#provideShape(mod.chiselsandbits.api.axissize.CollisionType,net.minecraft.core.BlockPos,boolean)" class="member-name-link">provideShape</a><wbr>(<a href="../../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;type,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Determines the voxelshape of the <a href="IAreaAccessorWithVoxelShape.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IAreaAccessorWithVoxelShape</code></a> at the given position.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#provideShape(mod.chiselsandbits.api.axissize.CollisionType,net.minecraft.core.BlockPos,boolean)" class="member-name-link">provideShape</a><wbr>(<a href="../../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;type,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Determines the voxelshape of the <a href="IAreaAccessorWithVoxelShape.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IAreaAccessorWithVoxelShape</code></a> at the given position.</div><br></td></tr>
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
<section id="provideShape(mod.chiselsandbits.api.axissize.CollisionType,net.minecraft.core.BlockPos,boolean)">

:::tabs
== provideShape
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">provideShape</span><wbr><span class="parameters">(<a href="../../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;type,
 net.minecraft.core.BlockPos&nbsp;offset,
 boolean&nbsp;simplify)</span></div>
<div class="block">Determines the voxelshape of the <a href="IAreaAccessorWithVoxelShape.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IAreaAccessorWithVoxelShape</code></a> at the given position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - The type of the voxel shape that is needed.</dd>
<dd><code>offset</code> - The offset of the <a href="IAreaAccessorWithVoxelShape.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IAreaAccessorWithVoxelShape</code></a> from the given position.</dd>
<dd><code>simplify</code> - Whether to simplify the voxelshape.</dd>
<dt>Returns:</dt>
<dd>The voxelshape of the <a href="IAreaAccessorWithVoxelShape.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IAreaAccessorWithVoxelShape</code></a> at the given position.</dd>
</dl>
:::


</section>

:::::
  

