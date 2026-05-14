--- 
title: IBlockNeighborhood
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.neighborhood](index.md)  
# Interface IBlockNeighborhood  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBlockNeighborhood</span></div>  

  

Marker interface used to detect block neighborhoods in cache keys.  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final <a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></code></td><td><code><a href="#EMPTY" class="member-name-link">EMPTY</a></code></td><td><div class="block">Empty neighborhood.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></code></td><td><code><a href="#around(net.minecraft.world.level.block.entity.BlockEntity)" class="member-name-link">around</a><wbr>(net.minecraft.world.level.block.entity.BlockEntity&nbsp;blockEntity)</code></td><td><div class="block">Creates a block neighborhood around the given block entity.</div><br></td></tr>
  <tr><td><code>@Nullable <a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#getAreaAccessor(net.minecraft.core.Direction)" class="member-name-link">getAreaAccessor</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks potential area accessor neighbor in the given direction.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.core.Direction)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks neighbor in the given direction.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></code></td><td><code><a href="#around(net.minecraft.world.level.block.entity.BlockEntity)" class="member-name-link">around</a><wbr>(net.minecraft.world.level.block.entity.BlockEntity&nbsp;blockEntity)</code></td><td><div class="block">Creates a block neighborhood around the given block entity.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@Nullable <a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#getAreaAccessor(net.minecraft.core.Direction)" class="member-name-link">getAreaAccessor</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks potential area accessor neighbor in the given direction.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.core.Direction)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks neighbor in the given direction.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@Nullable <a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#getAreaAccessor(net.minecraft.core.Direction)" class="member-name-link">getAreaAccessor</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks potential area accessor neighbor in the given direction.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.core.Direction)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks neighbor in the given direction.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="EMPTY">

:::tabs
== EMPTY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type"><a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></span>&nbsp;<span class="element-name">EMPTY</span></div>
Empty neighborhood.</div>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="around(net.minecraft.world.level.block.entity.BlockEntity)">

:::tabs
== around
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></span>&nbsp;<span class="element-name">around</span><wbr><span class="parameters">(net.minecraft.world.level.block.entity.BlockEntity&nbsp;blockEntity)</span></div>
Creates a block neighborhood around the given block entity.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockEntity</code> - the entity to get the neighborhood for.</dd>
<dt>Returns:</dt>
<dd>The neighborhood.</dd>
</dl>
</div>
:::


</section>

<section id="getBlockInformation(net.minecraft.core.Direction)">

:::tabs
== getBlockInformation
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getBlockInformation</span><wbr><span class="parameters">(net.minecraft.core.Direction&nbsp;direction)</span></div>
Returns the blocks neighbor in the given direction.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - The direction.</dd>
<dt>Returns:</dt>
<dd>The blockstate</dd>
</dl>
</div>
:::


</section>

<section id="getAreaAccessor(net.minecraft.core.Direction)">

:::tabs
== getAreaAccessor
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type">@Nullable <a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></span>&nbsp;<span class="element-name">getAreaAccessor</span><wbr><span class="parameters">(net.minecraft.core.Direction&nbsp;direction)</span></div>
Returns the blocks potential area accessor neighbor in the given direction.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - The direction.</dd>
<dt>Returns:</dt>
<dd>The area accessor.</dd>
</dl>
</div>
:::


</section>

:::::
  

