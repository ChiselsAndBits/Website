--- 
title: RawSerializable
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.serialization](index.md)  
# Interface RawSerializable  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">RawSerializable</span></div>  

  

Defines objects which can be serialized into a raw format.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;?&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;?&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;?,<wbr>?&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;?&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;?&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;?,<wbr>?&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;?&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;?&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;?,<wbr>?&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="codec()">

:::tabs
== codec
<div class="member-signature"><span class="return-type">com.mojang.serialization.Codec&lt;?&gt;</span>&nbsp;<span class="element-name">codec</span>()</div>
Returns The codec used for direct serialization..
<dl class="notes">
<dt>Returns:</dt>
<dd>The codec used for direct serialization.</dd>
</dl>
:::


</section>

<section id="mapCodec()">

:::tabs
== mapCodec
<div class="member-signature"><span class="return-type">com.mojang.serialization.MapCodec&lt;?&gt;</span>&nbsp;<span class="element-name">mapCodec</span>()</div>
Returns The codec used for complex serialization..
<dl class="notes">
<dt>Returns:</dt>
<dd>The codec used for complex serialization.</dd>
</dl>
:::


</section>

<section id="streamCodec()">

:::tabs
== streamCodec
<div class="member-signature"><span class="return-type">net.minecraft.network.codec.StreamCodec&lt;?,<wbr>?&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
Returns The codec used for streaming serialization..
<dl class="notes">
<dt>Returns:</dt>
<dd>The codec used for streaming serialization.</dd>
</dl>
:::


</section>

:::::
  

