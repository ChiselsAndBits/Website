--- 
title: IGenerallyModifiableAreaMutator
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.mutator](index.md)  
# Interface IGenerallyModifiableAreaMutator  
**All Extended Interfaces:**  
[IAABBOwner](../../aabb/IAABBOwner.md), [IAreaAccessor](../accessor/IAreaAccessor.md), [IStateAccessor](../accessor/IStateAccessor.md), [IAreaMutator](IAreaMutator.md), [IMirrorAndRotateble](IMirrorAndRotateble.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IGenerallyModifiableAreaMutator</span><span class="extends-implements"><br/>  
extends <a href="IAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IAreaMutator</a>, <a href="IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a>
<a href="../../aabb/IAABBOwner.html#getBoundingBox()" title="getBoundingBox()">getBoundingBox</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>
<a href="../accessor/IAreaAccessor.html#createNewShapeIdentifier()" title="createNewShapeIdentifier()">createNewShapeIdentifier</a>, <a href="../accessor/IAreaAccessor.html#createSnapshot()" title="createSnapshot()">createSnapshot</a>, <a href="../accessor/IAreaAccessor.html#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)" title="forEachWithPositionMutator(IPositionMutator, Consumer)">forEachWithPositionMutator</a>, <a href="../accessor/IAreaAccessor.html#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="isInside(BlockPos, Vec3)">isInside</a>, <a href="../accessor/IAreaAccessor.html#isInside(net.minecraft.world.phys.Vec3)" title="isInside(Vec3)">isInside</a>, <a href="../accessor/IAreaAccessor.html#stream()" title="stream()">stream</a>, <a href="../accessor/IAreaAccessor.html#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" title="streamWithPositionMutator(IPositionMutator)">streamWithPositionMutator</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="IAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IAreaMutator</a>
<a href="IAreaMutator.html#clearInAreaTarget(net.minecraft.world.phys.Vec3)" title="clearInAreaTarget(Vec3)">clearInAreaTarget</a>, <a href="IAreaMutator.html#clearInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="clearInBlockTarget(BlockPos, Vec3)">clearInBlockTarget</a>, <a href="IAreaMutator.html#mutableStream()" title="mutableStream()">mutableStream</a>, <a href="IAreaMutator.html#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="overrideInAreaTarget(BlockInformation, BlockPos, Vec3)">overrideInAreaTarget</a>, <a href="IAreaMutator.html#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" title="overrideInAreaTarget(BlockInformation, Vec3)">overrideInAreaTarget</a>, <a href="IAreaMutator.html#setInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" title="setInAreaTarget(BlockInformation, Vec3)">setInAreaTarget</a>, <a href="IAreaMutator.html#setInBlockTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="setInBlockTarget(BlockInformation, BlockPos, Vec3)">setInBlockTarget</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a>
<a href="IMirrorAndRotateble.html#mirror(net.minecraft.core.Direction.Axis)" title="mirror(Direction.Axis)">mirror</a>, <a href="IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis)" title="rotate(Direction.Axis)">rotate</a>, <a href="IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis,int)" title="rotate(Direction.Axis, int)">rotate</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>
<a href="../accessor/IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)" title="getInAreaTarget(Vec3)">getInAreaTarget</a>, <a href="../accessor/IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="getInBlockTarget(BlockPos, Vec3)">getInBlockTarget</a>
:::::
  
  
  

  

  

  

  

  

  

