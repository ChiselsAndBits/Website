--- 
title: IAccessorFactory
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor](index)  
# Interface IAccessorFactory  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IAccessorFactory</span></div>  

  

Allows for the creation of new accessors used to access chiselable areas.  

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
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;from,<br> net.minecraft.core.BlockPos&nbsp;to)</code></td><td><div class="block">Creates an accessor which mutates a given area.</div><br></td></tr>
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to)</code></td><td><div class="block">Creates an accessor which mutates a given area.</div><br></td></tr>
  <tr><td><code>static <a href="IAccessorFactory.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAccessorFactory</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the accessor factory.</div><br></td></tr>
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#in(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos)" class="member-name-link">in</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Creates a accessor which mutates a particular block only.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IAccessorFactory.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAccessorFactory</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the accessor factory.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;from,<br> net.minecraft.core.BlockPos&nbsp;to)</code></td><td><div class="block">Creates an accessor which mutates a given area.</div><br></td></tr>
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to)</code></td><td><div class="block">Creates an accessor which mutates a given area.</div><br></td></tr>
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#in(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos)" class="member-name-link">in</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Creates a accessor which mutates a particular block only.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;from,<br> net.minecraft.core.BlockPos&nbsp;to)</code></td><td><div class="block">Creates an accessor which mutates a given area.</div><br></td></tr>
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to)</code></td><td><div class="block">Creates an accessor which mutates a given area.</div><br></td></tr>
  <tr><td><code><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></code></td><td><code><a href="#in(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos)" class="member-name-link">in</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Creates a accessor which mutates a particular block only.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IAccessorFactory.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAccessorFactory</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
Gives access to the accessor factory.
<dl class="notes">
<dt>Returns:</dt>
<dd>The accessor factory.</dd>
</dl>
</div>
:::


</section>

<section id="in(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos)">

:::tabs
== in
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></span>&nbsp;<span class="element-name">in</span><wbr><span class="parameters">(net.minecraft.world.level.LevelAccessor&nbsp;world,
 net.minecraft.core.BlockPos&nbsp;pos)</span></div>
Creates a accessor which mutates a particular block only.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world to mutate in.</dd>
<dd><code>pos</code> - The position to mutate.</dd>
<dt>Returns:</dt>
<dd>The accessor.</dd>
</dl>
</div>
:::


</section>

<section id="covering(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)">

:::tabs
== covering
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></span>&nbsp;<span class="element-name">covering</span><wbr><span class="parameters">(net.minecraft.world.level.LevelAccessor&nbsp;world,
 net.minecraft.core.BlockPos&nbsp;from,
 net.minecraft.core.BlockPos&nbsp;to)</span></div>
Creates an accessor which mutates a given area.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world to mutate in.</dd>
<dd><code>from</code> - The block to function as a start point.</dd>
<dd><code>to</code> - The block to function as an end point.</dd>
<dt>Returns:</dt>
<dd>The accessor.</dd>
</dl>
</div>
:::


</section>

<section id="covering(net.minecraft.world.level.LevelAccessor,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== covering
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a></span>&nbsp;<span class="element-name">covering</span><wbr><span class="parameters">(net.minecraft.world.level.LevelAccessor&nbsp;world,
 net.minecraft.world.phys.Vec3&nbsp;from,
 net.minecraft.world.phys.Vec3&nbsp;to)</span></div>
Creates an accessor which mutates a given area.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world to mutate in.</dd>
<dd><code>from</code> - The start point.</dd>
<dd><code>to</code> - The end point.</dd>
<dt>Returns:</dt>
<dd>The accessor.</dd>
</dl>
</div>
:::


</section>

:::::
  

