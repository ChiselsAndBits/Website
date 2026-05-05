--- 
title: IMultiStateItemFactory
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.multistate](index.md)  
# Interface IMultiStateItemFactory  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiStateItemFactory</span></div>  

  

Can create multistate items from a given source.  

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
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#createBlockFrom(mod.chiselsandbits.api.multistate.accessor.IStateEntryInfo)" class="member-name-link">createBlockFrom</a><wbr>(<a href="../../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&nbsp;stateEntryInfo)</code></td><td><div class="block">Creates a new multistate itemstack with a single state internally.</div><br></td></tr>
  <tr><td><code>static <a href="IMultiStateItemFactory.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemFactory</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The instance of the manager.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IMultiStateItemFactory.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemFactory</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The instance of the manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#createBlockFrom(mod.chiselsandbits.api.multistate.accessor.IStateEntryInfo)" class="member-name-link">createBlockFrom</a><wbr>(<a href="../../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&nbsp;stateEntryInfo)</code></td><td><div class="block">Creates a new multistate itemstack with a single state internally.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#createBlockFrom(mod.chiselsandbits.api.multistate.accessor.IStateEntryInfo)" class="member-name-link">createBlockFrom</a><wbr>(<a href="../../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&nbsp;stateEntryInfo)</code></td><td><div class="block">Creates a new multistate itemstack with a single state internally.</div><br></td></tr>
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
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IMultiStateItemFactory.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemFactory</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">The instance of the manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The instance.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="createBlockFrom(mod.chiselsandbits.api.multistate.accessor.IStateEntryInfo)">

:::tabs
== createBlockFrom
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">createBlockFrom</span><wbr><span class="parameters">(<a href="../../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&nbsp;stateEntryInfo)</span></div>
<div class="block">Creates a new multistate itemstack with a single state internally.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateEntryInfo</code> - The state entry info to create an itemstack for.</dd>
<dt>Returns:</dt>
<dd>The itemstack containing only the given single state entry.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

