--- 
title: IWithColor
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Interface IWithColor  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWithColor</span></div>  

  

An object with a color associated with it.  

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
  <tr><td><code>default double</code></td><td><code><a href="#getAlphaChannel()" class="member-name-link">getAlphaChannel</a>()</code></td><td><div class="block">The alpha channel intensity to render with.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getColorVector()" class="member-name-link">getColorVector</a>()</code></td><td><div class="block">The color used to render.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default double</code></td><td><code><a href="#getAlphaChannel()" class="member-name-link">getAlphaChannel</a>()</code></td><td><div class="block">The alpha channel intensity to render with.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getColorVector()" class="member-name-link">getColorVector</a>()</code></td><td><div class="block">The color used to render.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getColorVector()" class="member-name-link">getColorVector</a>()</code></td><td><div class="block">The color used to render.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default double</code></td><td><code><a href="#getAlphaChannel()" class="member-name-link">getAlphaChannel</a>()</code></td><td><div class="block">The alpha channel intensity to render with.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getColorVector()">

:::tabs
== getColorVector
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getColorVector</span>()</div>
<div class="block">The color used to render.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The color in a 3d double vector as RGB.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getAlphaChannel()">

:::tabs
== getAlphaChannel
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">getAlphaChannel</span>()</div>
<div class="block">The alpha channel intensity to render with.
By default, this is 1.0.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The alpha channel intensity.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

