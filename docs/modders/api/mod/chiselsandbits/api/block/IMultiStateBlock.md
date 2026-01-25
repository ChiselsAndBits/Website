--- 
title: IMultiStateBlock
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block](index.md)  
# Interface IMultiStateBlock  
**All Extended Interfaces:**  
IBlockWithWorldlyProperties, BeaconBeamBlock, EntityBlock, ItemLike  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiStateBlock</span><span class="extends-implements"><br/>  
extends net.minecraft.world.level.block.EntityBlock, com.communi.suggestu.saecularia.caudices.core.block.IBlockWithWorldlyProperties</span></div>  

  

Implemented by Chisels and Bits Blocks, can be used to request a material that represents
 the largest quantity of a Chisels and Bits block.  

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
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState(net.minecraft.world.level.BlockGetter,net.minecraft.core.BlockPos)" class="member-name-link">getPrimaryState</a><wbr>(@NotNull net.minecraft.world.level.BlockGetter&nbsp;world,<br> @NotNull net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Returns the primary state of the block.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState(net.minecraft.world.level.BlockGetter,net.minecraft.core.BlockPos)" class="member-name-link">getPrimaryState</a><wbr>(@NotNull net.minecraft.world.level.BlockGetter&nbsp;world,<br> @NotNull net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Returns the primary state of the block.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState(net.minecraft.world.level.BlockGetter,net.minecraft.core.BlockPos)" class="member-name-link">getPrimaryState</a><wbr>(@NotNull net.minecraft.world.level.BlockGetter&nbsp;world,<br> @NotNull net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Returns the primary state of the block.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.world.level.block.EntityBlock
getListener, getTicker, newBlockEntity
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.communi.suggestu.saecularia.caudices.core.block.IBlockWithWorldlyProperties
canBeGrass, canHarvestBlock, getBeaconColorMultiplier, getCloneItemStack, getColor, getExplosionResistance, getFriction, getSoundType, mirror, rotate, shouldCheckWeakPower, shouldDisplayFluidOverlay
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.world.level.ItemLike
asItem
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getPrimaryState(net.minecraft.world.level.BlockGetter,net.minecraft.core.BlockPos)">

:::tabs
== getPrimaryState
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getPrimaryState</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.level.BlockGetter&nbsp;world,
 @NotNull
 @NotNull net.minecraft.core.BlockPos&nbsp;pos)</span></div>
Returns the primary state of the block.
 In terms of Chisels and Bits this is the blockstate that is represented the most inside the block.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world to read the data from. Required to get access to the tile entity with the backing data.</dd>
<dd><code>pos</code> - The pos in the given world to get the primary blockstate from. Required to get access to the tile entity with the backing data.</dd>
<dt>Returns:</dt>
<dd>The primary blockstate, or when not found the default state from the air block. <code>Block.defaultBlockState()</code></dd>
</dl>
:::


</section>

:::::
  

