--- 
title: IChangeTrackerManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.change](index.md)  
# Interface IChangeTrackerManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChangeTrackerManager</span></div>  

  

The central change tracker manager which gives access to each players individual change tracker if applicable.
This data is not synced.
On the client generally this data is only available for the current player, all other players return an empty change tracker.

All change trackers are reset upon server restart or datapack reload.  

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
  <tr><td><code>@NotNull <a href="IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a></code></td><td><code><a href="#getChangeTracker(net.minecraft.world.entity.player.Player)" class="member-name-link">getChangeTracker</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Gives access to the change tracker of the given player.</div><br></td></tr>
  <tr><td><code>static @NotNull <a href="IChangeTrackerManager.html" title="interface in mod.chiselsandbits.api.change">IChangeTrackerManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Short circuit method to get the manager instance from the api.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static @NotNull <a href="IChangeTrackerManager.html" title="interface in mod.chiselsandbits.api.change">IChangeTrackerManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Short circuit method to get the manager instance from the api.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a></code></td><td><code><a href="#getChangeTracker(net.minecraft.world.entity.player.Player)" class="member-name-link">getChangeTracker</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Gives access to the change tracker of the given player.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a></code></td><td><code><a href="#getChangeTracker(net.minecraft.world.entity.player.Player)" class="member-name-link">getChangeTracker</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Gives access to the change tracker of the given player.</div><br></td></tr>
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
</span><span class="modifiers">static</span>&nbsp;<span class="return-type">@NotNull <a href="IChangeTrackerManager.html" title="interface in mod.chiselsandbits.api.change">IChangeTrackerManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">Short circuit method to get the manager instance from the api.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The change tracker manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getChangeTracker(net.minecraft.world.entity.player.Player)">

:::tabs
== getChangeTracker
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a></span>&nbsp;<span class="element-name">getChangeTracker</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player)</span></div>
<div class="block">Gives access to the change tracker of the given player.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The player in question.</dd>
<dt>Returns:</dt>
<dd>The change tracker for the given player.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

