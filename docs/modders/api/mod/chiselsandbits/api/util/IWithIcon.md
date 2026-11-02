--- 
title: IWithIcon
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Interface IWithIcon  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWithIcon</span></div>  

  

An object with an icon to render.  

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
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getIcon()" class="member-name-link">getIcon</a>()</code></td><td><div class="block">The icon to render.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderOnHotBar()" class="member-name-link">shouldRenderOnHotBar</a>()</code></td><td><div class="block">Indicates whether this group should render as a mode icon on the player hotbar.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getIcon()" class="member-name-link">getIcon</a>()</code></td><td><div class="block">The icon to render.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderOnHotBar()" class="member-name-link">shouldRenderOnHotBar</a>()</code></td><td><div class="block">Indicates whether this group should render as a mode icon on the player hotbar.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getIcon()" class="member-name-link">getIcon</a>()</code></td><td><div class="block">The icon to render.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderOnHotBar()" class="member-name-link">shouldRenderOnHotBar</a>()</code></td><td><div class="block">Indicates whether this group should render as a mode icon on the player hotbar.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getIcon()">

:::tabs
== getIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.resources.Identifier</span>&nbsp;<span class="element-name">getIcon</span>()</div>
The icon to render.
<dl class="notes">
<dt>Returns:</dt>
<dd>The icon.</dd>
</dl>
</div>
:::


</section>

<section id="shouldRenderOnHotBar()">

:::tabs
== shouldRenderOnHotBar
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">shouldRenderOnHotBar</span>()</div>
Indicates whether this group should render as a mode icon on the player hotbar.
<p>
By default, this is disabled.
Only specific gameplay aspects which have icons turn this on to aid the player.
</p>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> when we should render it on the hotbar.</dd>
</dl>
</div>
:::


</section>

:::::
  

