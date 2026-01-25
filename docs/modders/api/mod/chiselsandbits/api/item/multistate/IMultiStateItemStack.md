--- 
title: IMultiStateItemStack
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.multistate](index.md)  
# Interface IMultiStateItemStack  
**All Extended Interfaces:**  
[IAABBOwner](../aabb/IAABBOwner.md), [IAreaAccessor](../accessor/IAreaAccessor.md), [ISingleBlockAxisAlignedAreaAccessor](../accessor/ISingleBlockAxisAlignedAreaAccessor.md), [IStateAccessor](../accessor/IStateAccessor.md), [IMirrorAndRotateble](../mutator/IMirrorAndRotateble.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiStateItemStack</span><span class="extends-implements"><br/>  
extends <a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="../../multistate/mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a>, <a href="../../multistate/accessor/ISingleBlockAxisAlignedAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">ISingleBlockAxisAlignedAreaAccessor</a></span></div>  

  

<div class="block">The itemstack sensitive version of the multistate item.</div>
  

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
  <tr><td><code><a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#copy()" class="member-name-link">copy</a>()</code></td><td><div class="block">Copies the current stack.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toBlockStack()" class="member-name-link">toBlockStack</a>()</code></td><td><div class="block">Converts this multistate itemstack data to an actual use able itemstack.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toPatternStack()" class="member-name-link">toPatternStack</a>()</code></td><td><div class="block">Converts this multistate itemstack data into a pattern that can be reused.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#writeDataTo(net.minecraft.world.item.ItemStack)" class="member-name-link">writeDataTo</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Writes the state data to the itemstack.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#copy()" class="member-name-link">copy</a>()</code></td><td><div class="block">Copies the current stack.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toBlockStack()" class="member-name-link">toBlockStack</a>()</code></td><td><div class="block">Converts this multistate itemstack data to an actual use able itemstack.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toPatternStack()" class="member-name-link">toPatternStack</a>()</code></td><td><div class="block">Converts this multistate itemstack data into a pattern that can be reused.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#writeDataTo(net.minecraft.world.item.ItemStack)" class="member-name-link">writeDataTo</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Writes the state data to the itemstack.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#copy()" class="member-name-link">copy</a>()</code></td><td><div class="block">Copies the current stack.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toBlockStack()" class="member-name-link">toBlockStack</a>()</code></td><td><div class="block">Converts this multistate itemstack data to an actual use able itemstack.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#toPatternStack()" class="member-name-link">toPatternStack</a>()</code></td><td><div class="block">Converts this multistate itemstack data into a pattern that can be reused.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#writeDataTo(net.minecraft.world.item.ItemStack)" class="member-name-link">writeDataTo</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Writes the state data to the itemstack.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.aabb.<a href="../../aabb/IAABBOwner.html" title="interface in mod.chiselsandbits.api.aabb">IAABBOwner</a>
<a href="../../aabb/IAABBOwner.html#getBoundingBox()">getBoundingBox</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>
<a href="../../multistate/accessor/IAreaAccessor.html#createNewShapeIdentifier()">createNewShapeIdentifier</a>, <a href="../../multistate/accessor/IAreaAccessor.html#createSnapshot()">createSnapshot</a>, <a href="../../multistate/accessor/IAreaAccessor.html#forEachWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator,java.util.function.Consumer)">forEachWithPositionMutator</a>, <a href="../../multistate/accessor/IAreaAccessor.html#isInside(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">isInside</a>, <a href="../../multistate/accessor/IAreaAccessor.html#isInside(net.minecraft.world.phys.Vec3)">isInside</a>, <a href="../../multistate/accessor/IAreaAccessor.html#stream()">stream</a>, <a href="../../multistate/accessor/IAreaAccessor.html#streamWithPositionMutator(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)">streamWithPositionMutator</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="../../multistate/mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a>
<a href="../../multistate/mutator/IMirrorAndRotateble.html#mirror(net.minecraft.core.Direction.Axis)">mirror</a>, <a href="../../multistate/mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis)">rotate</a>, <a href="../../multistate/mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis,int)">rotate</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../multistate/accessor/ISingleBlockAxisAlignedAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">ISingleBlockAxisAlignedAreaAccessor</a>
<a href="../../multistate/accessor/ISingleBlockAxisAlignedAreaAccessor.html#getStatistics()">getStatistics</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../../multistate/accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a>
<a href="../../multistate/accessor/IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)">getInAreaTarget</a>, <a href="../../multistate/accessor/IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">getInBlockTarget</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="toBlockStack()">

:::tabs
== toBlockStack
<div class="member-signature"><span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">toBlockStack</span>()</div>
<div class="block">Converts this multistate itemstack data to an actual use able itemstack.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The itemstack with the data of this multistate itemstack.</dd>
</dl>
:::


</section>

<section id="toPatternStack()">

:::tabs
== toPatternStack
<div class="member-signature"><span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">toPatternStack</span>()</div>
<div class="block">Converts this multistate itemstack data into a pattern that can be reused.
 By default converts this into a single use pattern.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The single use patter from this multi state itemstack.</dd>
</dl>
:::


</section>

<section id="writeDataTo(net.minecraft.world.item.ItemStack)">

:::tabs
== writeDataTo
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">writeDataTo</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Writes the state data to the itemstack.</div>
<dl class="notes"></dl>
:::


</section>

<section id="copy()">

:::tabs
== copy
<div class="member-signature"><span class="return-type"><a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></span>&nbsp;<span class="element-name">copy</span>()</div>
<div class="block">Copies the current stack.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The stack copied.</dd>
</dl>
:::


</section>

:::::
  

