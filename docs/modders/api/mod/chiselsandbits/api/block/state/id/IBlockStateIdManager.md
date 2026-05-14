--- 
title: IBlockStateIdManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.state.id](index.md)  
# Interface IBlockStateIdManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBlockStateIdManager</span></div>  

  

The blockstate id manager which manages the blockstate ids for the current session.

Generally this manager is comparable to the relevant methods in the game registry.  

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
  <tr><td><code>default net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#getBlockStateFrom(int)" class="member-name-link">getBlockStateFrom</a><wbr>(int&nbsp;id)</code></td><td><div class="block">Calculates the blockstate from the given id.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#getIdFrom(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getIdFrom</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td><div class="block">Calculates the the integer id representation of the blockstate.</div><br></td></tr>
  <tr><td><code>static <a href="IBlockStateIdManager.html" title="interface in mod.chiselsandbits.api.block.state.id">IBlockStateIdManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IBlockStateIdManager.html" title="interface in mod.chiselsandbits.api.block.state.id">IBlockStateIdManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#getBlockStateFrom(int)" class="member-name-link">getBlockStateFrom</a><wbr>(int&nbsp;id)</code></td><td><div class="block">Calculates the blockstate from the given id.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#getIdFrom(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getIdFrom</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td><div class="block">Calculates the the integer id representation of the blockstate.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#getBlockStateFrom(int)" class="member-name-link">getBlockStateFrom</a><wbr>(int&nbsp;id)</code></td><td><div class="block">Calculates the blockstate from the given id.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#getIdFrom(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getIdFrom</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td><div class="block">Calculates the the integer id representation of the blockstate.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">
:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IBlockStateIdManager.html" title="interface in mod.chiselsandbits.api.block.state.id">IBlockStateIdManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
</div>
:::
</section>
<section id="getIdFrom(net.minecraft.world.level.block.state.BlockState)">
:::tabs
== getIdFrom
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getIdFrom</span><wbr><span class="parameters">(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</span></div>
Calculates the the integer id representation of the blockstate.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockState</code> - The blockstate for which the id is requested.</dd>
<dt>Returns:</dt>
<dd>The id of the given blockstate.</dd>
</dl>
</div>
:::
</section>
<section id="getBlockStateFrom(int)">
:::tabs
== getBlockStateFrom
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.level.block.state.BlockState</span>&nbsp;<span class="element-name">getBlockStateFrom</span><wbr><span class="parameters">(int&nbsp;id)</span></div>
Calculates the blockstate from the given id.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - The integer id representation of the requested blockstate.</dd>
<dt>Returns:</dt>
<dd>The blockstate which is represented by the given id.</dd>
</dl>
</div>
:::
</section>
:::::
  

