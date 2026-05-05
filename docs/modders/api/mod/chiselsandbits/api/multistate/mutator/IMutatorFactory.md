--- 
title: IMutatorFactory
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.mutator](index.md)  
# Interface IMutatorFactory  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMutatorFactory</span></div>  

  

Allows for the creation of new mutators used to modify chiselable areas.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a></code></td><td><code><a href="#clonedFromAccessor(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">clonedFromAccessor</a><wbr>(<a href="../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;source)</code></td><td><div class="block">Creates a clone of the accessor and returns a mutator of it.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;from,<br> net.minecraft.core.BlockPos&nbsp;to)</code></td><td><div class="block">Creates a mutator which mutates a given area.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to)</code></td><td><div class="block">Creates a mutator which mutates a given area.</div><br></td></tr>
  <tr><td><code>static @NotNull <a href="IMutatorFactory.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutatorFactory</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the the mutator factory.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#in(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos)" class="member-name-link">in</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Creates a mutator which mutates a particular block only.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static @NotNull <a href="IMutatorFactory.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutatorFactory</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the the mutator factory.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a></code></td><td><code><a href="#clonedFromAccessor(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">clonedFromAccessor</a><wbr>(<a href="../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;source)</code></td><td><div class="block">Creates a clone of the accessor and returns a mutator of it.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;from,<br> net.minecraft.core.BlockPos&nbsp;to)</code></td><td><div class="block">Creates a mutator which mutates a given area.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to)</code></td><td><div class="block">Creates a mutator which mutates a given area.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#in(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos)" class="member-name-link">in</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Creates a mutator which mutates a particular block only.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a></code></td><td><code><a href="#clonedFromAccessor(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">clonedFromAccessor</a><wbr>(<a href="../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;source)</code></td><td><div class="block">Creates a clone of the accessor and returns a mutator of it.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;from,<br> net.minecraft.core.BlockPos&nbsp;to)</code></td><td><div class="block">Creates a mutator which mutates a given area.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#covering(net.minecraft.world.level.LevelAccessor,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">covering</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to)</code></td><td><div class="block">Creates a mutator which mutates a given area.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></code></td><td><code><a href="#in(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos)" class="member-name-link">in</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;world,<br> net.minecraft.core.BlockPos&nbsp;pos)</code></td><td><div class="block">Creates a mutator which mutates a particular block only.</div><br></td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">static</span>&nbsp;<span class="return-type">@NotNull <a href="IMutatorFactory.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutatorFactory</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">Gives access to the the mutator factory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The mutator factory.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="in(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos)">

:::tabs
== in
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></span>&nbsp;<span class="element-name">in</span><wbr><span class="parameters">(net.minecraft.world.level.LevelAccessor&nbsp;world,
 net.minecraft.core.BlockPos&nbsp;pos)</span></div>
<div class="block">Creates a mutator which mutates a particular block only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world to mutate in.</dd>
<dd><code>pos</code> - The position to mutate.</dd>
<dt>Returns:</dt>
<dd>The mutator.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="covering(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)">

:::tabs
== covering
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></span>&nbsp;<span class="element-name">covering</span><wbr><span class="parameters">(net.minecraft.world.level.LevelAccessor&nbsp;world,
 net.minecraft.core.BlockPos&nbsp;from,
 net.minecraft.core.BlockPos&nbsp;to)</span></div>
<div class="block">Creates a mutator which mutates a given area.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world to mutate in.</dd>
<dd><code>from</code> - The block to function as a start point.</dd>
<dd><code>to</code> - The block to function as an end point.</dd>
<dt>Returns:</dt>
<dd>The mutator.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="covering(net.minecraft.world.level.LevelAccessor,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== covering
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a></span>&nbsp;<span class="element-name">covering</span><wbr><span class="parameters">(net.minecraft.world.level.LevelAccessor&nbsp;world,
 net.minecraft.world.phys.Vec3&nbsp;from,
 net.minecraft.world.phys.Vec3&nbsp;to)</span></div>
<div class="block">Creates a mutator which mutates a given area.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world to mutate in.</dd>
<dd><code>from</code> - The start point.</dd>
<dd><code>to</code> - The end point.</dd>
<dt>Returns:</dt>
<dd>The mutator.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="clonedFromAccessor(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)">

:::tabs
== clonedFromAccessor
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="IGenerallyModifiableAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IGenerallyModifiableAreaMutator</a></span>&nbsp;<span class="element-name">clonedFromAccessor</span><wbr><span class="parameters">(<a href="../accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;source)</span></div>
<div class="block">Creates a clone of the accessor and returns a mutator of it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - The source accessor.</dd>
<dt>Returns:</dt>
<dd>The mutator.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

