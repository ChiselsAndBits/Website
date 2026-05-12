--- 
title: IPatternPlacementType
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.pattern.placement](index.md)  
# Interface IPatternPlacementType  
**All Extended Interfaces:**  
ICustomRegistryEntry, [IRenderableMode](../../item/withmode/IRenderableMode.md), [IToolMode\<IToolModeGroup\>](../../item/withmode/IToolMode.md), [IPlacementProperties](../../placement/IPlacementProperties.md), [IWithColor](../../util/IWithColor.md), [IWithDisplayName](../../util/IWithDisplayName.md), [IWithIcon](../../util/IWithIcon.md), [IWithIconAndColor](../../util/IWithIconAndColor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPatternPlacementType</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry, <a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>&lt;<a href="../../item/withmode/group/IToolModeGroup.html" title="interface in mod.chiselsandbits.api.item.withmode.group">IToolModeGroup</a>&gt;, <a href="../../placement/IPlacementProperties.html" title="interface in mod.chiselsandbits.api.placement">IPlacementProperties</a></span></div>  

  

Presents a way placing a pattern in the world.  

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
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#buildVoxelShapeForWireframe(mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">buildVoxelShapeForWireframe</a><wbr>(<a href="../../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;sourceSnapshot,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.Vec3&nbsp;targetedPoint,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Used to build a voxelshape for rendering in the preview.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked to determine where the targeted position of the placement type is.</div><br></td></tr>
  <tr><td><code><a href="../../placement/PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#performPlacement(mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,net.minecraft.world.item.context.BlockPlaceContext,boolean)" class="member-name-link">performPlacement</a><wbr>(<a href="../../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;source,<br> net.minecraft.world.item.context.BlockPlaceContext&nbsp;context,<br> boolean&nbsp;simulate)</code></td><td><div class="block">Invoked to perform the actual placement of the pattern in the world.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#buildVoxelShapeForWireframe(mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">buildVoxelShapeForWireframe</a><wbr>(<a href="../../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;sourceSnapshot,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.Vec3&nbsp;targetedPoint,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Used to build a voxelshape for rendering in the preview.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked to determine where the targeted position of the placement type is.</div><br></td></tr>
  <tr><td><code><a href="../../placement/PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#performPlacement(mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,net.minecraft.world.item.context.BlockPlaceContext,boolean)" class="member-name-link">performPlacement</a><wbr>(<a href="../../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;source,<br> net.minecraft.world.item.context.BlockPlaceContext&nbsp;context,<br> boolean&nbsp;simulate)</code></td><td><div class="block">Invoked to perform the actual placement of the pattern in the world.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#buildVoxelShapeForWireframe(mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">buildVoxelShapeForWireframe</a><wbr>(<a href="../../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;sourceSnapshot,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.Vec3&nbsp;targetedPoint,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Used to build a voxelshape for rendering in the preview.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)" class="member-name-link">getTargetedPosition</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;heldStack,<br> net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</code></td><td><div class="block">Invoked to determine where the targeted position of the placement type is.</div><br></td></tr>
  <tr><td><code><a href="../../placement/PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#performPlacement(mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,net.minecraft.world.item.context.BlockPlaceContext,boolean)" class="member-name-link">performPlacement</a><wbr>(<a href="../../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;source,<br> net.minecraft.world.item.context.BlockPlaceContext&nbsp;context,<br> boolean&nbsp;simulate)</code></td><td><div class="block">Invoked to perform the actual placement of the pattern in the world.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;com.communi.suggestu.scena.core.registries.ICustomRegistryEntrygetRegistryNameMethods inherited from interface&nbsp;mod.chiselsandbits.api.placement.<a href="../../placement/IPlacementProperties.html" title="interface in mod.chiselsandbits.api.placement">IPlacementProperties</a><a href="../../placement/IPlacementProperties.html#overridesOccupiedBits(net.minecraft.world.item.ItemStack)" title="overridesOccupiedBits(ItemStack)">overridesOccupiedBits</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../../item/withmode/IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a><a href="../../item/withmode/IRenderableMode.html#getColorVector()" title="getColorVector()">getColorVector</a>, <a href="../../item/withmode/IRenderableMode.html#getPositionVector()" title="getPositionVector()">getPositionVector</a>, <a href="../../item/withmode/IRenderableMode.html#getScaleVector()" title="getScaleVector()">getScaleVector</a>, <a href="../../item/withmode/IRenderableMode.html#isActive()" title="isActive()">isActive</a>, <a href="../../item/withmode/IRenderableMode.html#shouldRenderDisplayNameInMenu()" title="shouldRenderDisplayNameInMenu()">shouldRenderDisplayNameInMenu</a>, <a href="../../item/withmode/IRenderableMode.html#shouldRenderName()" title="shouldRenderName()">shouldRenderName</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a><a href="../../item/withmode/IToolMode.html#getGroup()" title="getGroup()">getGroup</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a><a href="../../util/IWithColor.html#getAlphaChannel()" title="getAlphaChannel()">getAlphaChannel</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a><a href="../../util/IWithDisplayName.html#getDisplayName()" title="getDisplayName()">getDisplayName</a>, <a href="../../util/IWithDisplayName.html#getMultiLineDisplayName()" title="getMultiLineDisplayName()">getMultiLineDisplayName</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a><a href="../../util/IWithIcon.html#getIcon()" title="getIcon()">getIcon</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="buildVoxelShapeForWireframe(mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)">

:::tabs
== buildVoxelShapeForWireframe
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">buildVoxelShapeForWireframe</span><wbr><span class="parameters">(<a href="../../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;sourceSnapshot,
 net.minecraft.world.entity.player.Player&nbsp;player,
 net.minecraft.world.phys.Vec3&nbsp;targetedPoint,
 net.minecraft.core.Direction&nbsp;hitFace)</span></div>
<div class="block">Used to build a voxelshape for rendering in the preview.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceSnapshot</code> - The snapshot stored in the pattern for placement.</dd>
<dd><code>player</code> - The player performing the action.</dd>
<dd><code>targetedPoint</code> - The point targeted by the player.</dd>
<dd><code>hitFace</code> - The face hit by the player.</dd>
<dt>Returns:</dt>
<dd>The VoxelShape used to render the wireframe.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="performPlacement(mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,net.minecraft.world.item.context.BlockPlaceContext,boolean)">

:::tabs
== performPlacement
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../../placement/PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">performPlacement</span><wbr><span class="parameters">(<a href="../../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;source,
 net.minecraft.world.item.context.BlockPlaceContext&nbsp;context,
 boolean&nbsp;simulate)</span></div>
<div class="block">Invoked to perform the actual placement of the pattern in the world.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - The snapshot stored in the pattern for placement.</dd>
<dd><code>context</code> - The use context of the pattern item on a block.</dd>
<dd><code>simulate</code> - Indicates if the placement operation is a simulation or not.</dd>
<dt>Returns:</dt>
<dd>The action result which influences the further processing of the click interaction.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">

:::tabs
== getTargetedPosition
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getTargetedPosition</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;heldStack,
 net.minecraft.world.entity.player.Player&nbsp;player,
 net.minecraft.world.phys.BlockHitResult&nbsp;blockRayTraceResult)</span></div>
<div class="block">Invoked to determine where the targeted position of the placement type is.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>heldStack</code> - The stack that the player is holding.</dd>
<dd><code>player</code> - The player which is holding the itemstack.</dd>
<dd><code>blockRayTraceResult</code> - The block ray trace result in the current context.</dd>
<dt>Returns:</dt>
<dd>The position of the potential placement.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

