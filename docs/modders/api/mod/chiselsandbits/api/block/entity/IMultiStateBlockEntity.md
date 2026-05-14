--- 
title: IMultiStateBlockEntity
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.entity](index)  
# Interface IMultiStateBlockEntity  
**All Extended Interfaces:**  
[IAABBOwner](../../aabb/IAABBOwner), [IAreaAccessor](../../multistate/accessor/IAreaAccessor), [IAreaAccessorWithVoxelShape](../../multistate/accessor/IAreaAccessorWithVoxelShape), [ISingleBlockAxisAlignedAreaAccessor](../../multistate/accessor/ISingleBlockAxisAlignedAreaAccessor), [IStateAccessor](../../multistate/accessor/IStateAccessor), [IWorldAreaAccessor](../../multistate/accessor/world/IWorldAreaAccessor), [IBatchedAreaMutator](../../multistate/mutator/batched/IBatchedAreaMutator), [IAreaMutator](../../multistate/mutator/IAreaMutator), [IGenerallyModifiableAreaMutator](../../multistate/mutator/IGenerallyModifiableAreaMutator), [IMirrorAndRotateble](../../multistate/mutator/IMirrorAndRotateble), [IWorldAreaMutator](../../multistate/mutator/world/IWorldAreaMutator), [IWithBatchableMutationSupport](../../util/IWithBatchableMutationSupport), [IWorldObject](../../util/IWorldObject)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiStateBlockEntity</span><span class="extends-implements"><br/>  
extends <a href="../../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>, <a href="../../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a>, <a href="../../multistate/mutator/batched/IBatchedAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.batched">IBatchedAreaMutator</a>, <a href="../../multistate/mutator/IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a>, <a href="../../multistate/accessor/IAreaAccessorWithVoxelShape.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessorWithVoxelShape</a>, <a href="../../multistate/accessor/ISingleBlockAxisAlignedAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">ISingleBlockAxisAlignedAreaAccessor</a></span></div>  

  

Represents the block entity with the state data, which under-ly the information
provided by the <a href="../IMultiStateBlock.html" title="interface in mod.chiselsandbits.api.block"><code>IMultiStateBlock</code></a> blocks.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Interface</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="IMultiStateBlockEntity.BlockStack.html" class="type-name-link" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateBlockEntity.BlockStack.html" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></code></td><td><code><a href="#getBlockStack()" class="member-name-link">getBlockStack</a>()</code></td><td><div class="block">Creates an <code>ItemStack</code> for placement as a block.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getShape(mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">getShape</a><wbr>(<a href="../../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;type)</code></td><td><div class="block">Returns the current blocks shape for the given collision type.</div><br></td></tr>
  <tr><td><code><a href="../../multistate/statistics/IMultiStateObjectStatistics.html" title="interface in mod.chiselsandbits.api.multistate.statistics">IMultiStateObjectStatistics</a></code></td><td><code><a href="#getStatistics()" class="member-name-link">getStatistics</a>()</code></td><td><div class="block">The statistics of this block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#initializeWith(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">initializeWith</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;initialInformation)</code></td><td><div class="block">Initializes the block entity so that all its state entries<br>have the given block information as their block information.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isCanBeFlooded()" class="member-name-link">isCanBeFlooded</a>()</code></td><td><div class="block">Indicates whether the current block entity can be flooded with water.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmitsLightBasedOnFullBlock()" class="member-name-link">isEmitsLightBasedOnFullBlock</a>()</code></td><td><div class="block">Indicates whether the lighting conditions of the block are based on the amount of bits in the block or the full block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setCanBeFlooded(boolean)" class="member-name-link">setCanBeFlooded</a><wbr>(boolean&nbsp;canBeFlooded)</code></td><td><div class="block">Sets the flooding indicator.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setEmitsLightBasedOnFullBlock(boolean)" class="member-name-link">setEmitsLightBasedOnFullBlock</a><wbr>(boolean&nbsp;emitsLightBasedOnFullBlock)</code></td><td><div class="block">Sets the lighting conditions indicator.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateBlockEntity.BlockStack.html" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></code></td><td><code><a href="#getBlockStack()" class="member-name-link">getBlockStack</a>()</code></td><td><div class="block">Creates an <code>ItemStack</code> for placement as a block.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getShape(mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">getShape</a><wbr>(<a href="../../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;type)</code></td><td><div class="block">Returns the current blocks shape for the given collision type.</div><br></td></tr>
  <tr><td><code><a href="../../multistate/statistics/IMultiStateObjectStatistics.html" title="interface in mod.chiselsandbits.api.multistate.statistics">IMultiStateObjectStatistics</a></code></td><td><code><a href="#getStatistics()" class="member-name-link">getStatistics</a>()</code></td><td><div class="block">The statistics of this block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#initializeWith(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">initializeWith</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;initialInformation)</code></td><td><div class="block">Initializes the block entity so that all its state entries<br>have the given block information as their block information.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isCanBeFlooded()" class="member-name-link">isCanBeFlooded</a>()</code></td><td><div class="block">Indicates whether the current block entity can be flooded with water.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmitsLightBasedOnFullBlock()" class="member-name-link">isEmitsLightBasedOnFullBlock</a>()</code></td><td><div class="block">Indicates whether the lighting conditions of the block are based on the amount of bits in the block or the full block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setCanBeFlooded(boolean)" class="member-name-link">setCanBeFlooded</a><wbr>(boolean&nbsp;canBeFlooded)</code></td><td><div class="block">Sets the flooding indicator.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setEmitsLightBasedOnFullBlock(boolean)" class="member-name-link">setEmitsLightBasedOnFullBlock</a><wbr>(boolean&nbsp;emitsLightBasedOnFullBlock)</code></td><td><div class="block">Sets the lighting conditions indicator.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateBlockEntity.BlockStack.html" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></code></td><td><code><a href="#getBlockStack()" class="member-name-link">getBlockStack</a>()</code></td><td><div class="block">Creates an <code>ItemStack</code> for placement as a block.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getShape(mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">getShape</a><wbr>(<a href="../../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;type)</code></td><td><div class="block">Returns the current blocks shape for the given collision type.</div><br></td></tr>
  <tr><td><code><a href="../../multistate/statistics/IMultiStateObjectStatistics.html" title="interface in mod.chiselsandbits.api.multistate.statistics">IMultiStateObjectStatistics</a></code></td><td><code><a href="#getStatistics()" class="member-name-link">getStatistics</a>()</code></td><td><div class="block">The statistics of this block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#initializeWith(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">initializeWith</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;initialInformation)</code></td><td><div class="block">Initializes the block entity so that all its state entries<br>have the given block information as their block information.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isCanBeFlooded()" class="member-name-link">isCanBeFlooded</a>()</code></td><td><div class="block">Indicates whether the current block entity can be flooded with water.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmitsLightBasedOnFullBlock()" class="member-name-link">isEmitsLightBasedOnFullBlock</a>()</code></td><td><div class="block">Indicates whether the lighting conditions of the block are based on the amount of bits in the block or the full block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setCanBeFlooded(boolean)" class="member-name-link">setCanBeFlooded</a><wbr>(boolean&nbsp;canBeFlooded)</code></td><td><div class="block">Sets the flooding indicator.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setEmitsLightBasedOnFullBlock(boolean)" class="member-name-link">setEmitsLightBasedOnFullBlock</a><wbr>(boolean&nbsp;emitsLightBasedOnFullBlock)</code></td><td><div class="block">Sets the lighting conditions indicator.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a>
<a href="../../aabb/IAABBOwner.html#getBoundingBox()" title="getBoundingBox()">getBoundingBox</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>
<a href="../../multistate/accessor/IAreaAccessor.html#createNewShapeIdentifier()" title="createNewShapeIdentifier()">createNewShapeIdentifier</a>, <a href="../../multistate/accessor/IAreaAccessor.html#createSnapshot()" title="createSnapshot()">createSnapshot</a>, <a href="../../multistate/accessor/IAreaAccessor.html#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)" title="forEachWithPositionMutator(IPositionMutator, Consumer)">forEachWithPositionMutator</a>, <a href="../../multistate/accessor/IAreaAccessor.html#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="isInside(BlockPos, Vec3)">isInside</a>, <a href="../../multistate/accessor/IAreaAccessor.html#isInside(net.minecraft.world.phys.Vec3)" title="isInside(Vec3)">isInside</a>, <a href="../../multistate/accessor/IAreaAccessor.html#stream()" title="stream()">stream</a>, <a href="../../multistate/accessor/IAreaAccessor.html#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" title="streamWithPositionMutator(IPositionMutator)">streamWithPositionMutator</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../multistate/accessor/IAreaAccessorWithVoxelShape.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessorWithVoxelShape</a>
<a href="../../multistate/accessor/IAreaAccessorWithVoxelShape.html#provideShape(mod.chiselsandbits.api.axissize.CollisionType,net.minecraft.core.BlockPos,boolean)" title="provideShape(CollisionType, BlockPos, boolean)">provideShape</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="../../multistate/mutator/IAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IAreaMutator</a>
<a href="../../multistate/mutator/IAreaMutator.html#clearInAreaTarget(net.minecraft.world.phys.Vec3)" title="clearInAreaTarget(Vec3)">clearInAreaTarget</a>, <a href="../../multistate/mutator/IAreaMutator.html#clearInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="clearInBlockTarget(BlockPos, Vec3)">clearInBlockTarget</a>, <a href="../../multistate/mutator/IAreaMutator.html#mutableStream()" title="mutableStream()">mutableStream</a>, <a href="../../multistate/mutator/IAreaMutator.html#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="overrideInAreaTarget(BlockInformation, BlockPos, Vec3)">overrideInAreaTarget</a>, <a href="../../multistate/mutator/IAreaMutator.html#overrideInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" title="overrideInAreaTarget(BlockInformation, Vec3)">overrideInAreaTarget</a>, <a href="../../multistate/mutator/IAreaMutator.html#setInAreaTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" title="setInAreaTarget(BlockInformation, Vec3)">setInAreaTarget</a>, <a href="../../multistate/mutator/IAreaMutator.html#setInBlockTarget(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="setInBlockTarget(BlockInformation, BlockPos, Vec3)">setInBlockTarget</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.batched.<a href="../../multistate/mutator/batched/IBatchedAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.batched">IBatchedAreaMutator</a>
<a href="../../multistate/mutator/batched/IBatchedAreaMutator.html#batch(mod.chiselsandbits.api.change.IChangeTracker)" title="batch(IChangeTracker)">batch</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="../../multistate/mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a>
<a href="../../multistate/mutator/IMirrorAndRotateble.html#mirror(net.minecraft.core.Direction.Axis)" title="mirror(Direction.Axis)">mirror</a>, <a href="../../multistate/mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis)" title="rotate(Direction.Axis)">rotate</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../multistate/accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>
<a href="../../multistate/accessor/IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)" title="getInAreaTarget(Vec3)">getInAreaTarget</a>, <a href="../../multistate/accessor/IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="getInBlockTarget(BlockPos, Vec3)">getInBlockTarget</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithBatchableMutationSupport.html" title="interface in mod.chiselsandbits.api.util">IWithBatchableMutationSupport</a>
<a href="../../util/IWithBatchableMutationSupport.html#batch()" title="batch()">batch</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.world.<a href="../../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>
<a href="../../multistate/accessor/world/IWorldAreaAccessor.html#coveredAreaStream()" title="coveredAreaStream()">coveredAreaStream</a>, <a href="../../multistate/accessor/world/IWorldAreaAccessor.html#inWorldStream()" title="inWorldStream()">inWorldStream</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.world.<a href="../../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a>
<a href="../../multistate/mutator/world/IWorldAreaMutator.html#inWorldMutableStream()" title="inWorldMutableStream()">inWorldMutableStream</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>
<a href="../../util/IWorldObject.html#getInWorldBoundingBox()" title="getInWorldBoundingBox()">getInWorldBoundingBox</a>, <a href="../../util/IWorldObject.html#getInWorldEndBlockPoint()" title="getInWorldEndBlockPoint()">getInWorldEndBlockPoint</a>, <a href="../../util/IWorldObject.html#getInWorldEndPoint()" title="getInWorldEndPoint()">getInWorldEndPoint</a>, <a href="../../util/IWorldObject.html#getInWorldStartBlockPoint()" title="getInWorldStartBlockPoint()">getInWorldStartBlockPoint</a>, <a href="../../util/IWorldObject.html#getInWorldStartPoint()" title="getInWorldStartPoint()">getInWorldStartPoint</a>, <a href="../../util/IWorldObject.html#getWorld()" title="getWorld()">getWorld</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="isCanBeFlooded()">

:::tabs
== isCanBeFlooded
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isCanBeFlooded</span>()</div>
Indicates whether the current block entity can be flooded with water.
<dl class="notes">
<dt>Returns:</dt>
<dd>True to allow flooding, false when not.</dd>
</dl>
</div>
:::


</section>

<section id="setCanBeFlooded(boolean)">

:::tabs
== setCanBeFlooded
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setCanBeFlooded</span><wbr><span class="parameters">(boolean&nbsp;canBeFlooded)</span></div>
Sets the flooding indicator.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canBeFlooded</code> - True to allow flooding, false when not.</dd>
</dl>
</div>
:::


</section>

<section id="isEmitsLightBasedOnFullBlock()">

:::tabs
== isEmitsLightBasedOnFullBlock
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isEmitsLightBasedOnFullBlock</span>()</div>
Indicates whether the lighting conditions of the block are based on the amount of bits in the block or the full block.
<dl class="notes">
<dt>Returns:</dt>
<dd>True to use full block size calculation, false when not.</dd>
</dl>
</div>
:::


</section>

<section id="setEmitsLightBasedOnFullBlock(boolean)">

:::tabs
== setEmitsLightBasedOnFullBlock
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setEmitsLightBasedOnFullBlock</span><wbr><span class="parameters">(boolean&nbsp;emitsLightBasedOnFullBlock)</span></div>
Sets the lighting conditions indicator.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>emitsLightBasedOnFullBlock</code> - True to calculate lighting conditions over the full block, false only over the set bits.</dd>
</dl>
</div>
:::


</section>

<section id="getStatistics()">

:::tabs
== getStatistics
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../../multistate/statistics/IMultiStateObjectStatistics.html" title="interface in mod.chiselsandbits.api.multistate.statistics">IMultiStateObjectStatistics</a></span>&nbsp;<span class="element-name">getStatistics</span>()</div>
The statistics of this block.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../multistate/accessor/ISingleBlockAxisAlignedAreaAccessor.html#getStatistics()">getStatistics</a></code>&nbsp;in interface&nbsp;<code><a href="../../multistate/accessor/ISingleBlockAxisAlignedAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">ISingleBlockAxisAlignedAreaAccessor</a></code></dd>
<dt>Returns:</dt>
<dd>The statistics.</dd>
</dl>
</div>
:::


</section>

<section id="rotate(net.minecraft.core.Direction.Axis,int)">

:::tabs
== rotate
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">rotate</span><wbr><span class="parameters">(net.minecraft.core.Direction.Axis&nbsp;axis,
 int&nbsp;rotationCount)</span></div>
Rotates the current multistate block 90 degrees around the given axis with the given rotation count.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../multistate/mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis,int)">rotate</a></code>&nbsp;in interface&nbsp;<code><a href="../../multistate/mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a></code></dd>
<dt>Parameters:</dt>
<dd><code>axis</code> - The axis to rotate around.</dd>
<dd><code>rotationCount</code> - The amount of times to rotate the</dd>
</dl>
</div>
:::


</section>

<section id="initializeWith(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== initializeWith
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">initializeWith</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;initialInformation)</span></div>
Initializes the block entity so that all its state entries
have the given block information as their block information.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initialInformation</code> - The new initial block information.</dd>
</dl>
</div>
:::


</section>

<section id="getShape(mod.chiselsandbits.api.axissize.CollisionType)">

:::tabs
== getShape
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">getShape</span><wbr><span class="parameters">(<a href="../../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;type)</span></div>
Returns the current blocks shape for the given collision type.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - The collision type to get the shape for.</dd>
<dt>Returns:</dt>
<dd>The shape.</dd>
</dl>
</div>
:::


</section>

<section id="getBlockStack()">

:::tabs
== getBlockStack
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IMultiStateBlockEntity.BlockStack.html" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></span>&nbsp;<span class="element-name">getBlockStack</span>()</div>
Creates an <code>ItemStack</code> for placement as a block.
<dl class="notes">
<dt>Returns:</dt>
<dd>The block stack.</dd>
</dl>
</div>
:::


</section>

:::::
  

