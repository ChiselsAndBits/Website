--- 
title: Serializable
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.serialization](index.md)  
# Interface Serializable\<TSelf,TBuffer extends FriendlyByteBuf\>  
**Type Parameters:**  
TSelf - The type of the implementing class.  
TBuffer - The type of the buffer to serialize to/from.  

**All Extended Interfaces:**  
[RawSerializable](RawSerializable.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Serializable&lt;TSelf, TBuffer extends net.minecraft.network.FriendlyByteBuf&gt;</span><span class="extends-implements"><br/>  
extends <a href="RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></span></div>  

  

Defines objects which can be serialized into an exact format.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Interface</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static interface&nbsp;</code></td><td><code><a href="Serializable.Registry.html" class="type-name-link" title="interface in mod.chiselsandbits.api.serialization">Serializable.Registry</a>&lt;<a href="Serializable.Registry.html#type-param-TSelf" title="type parameter in Serializable.Registry">TSelf</a>&gt;</code></td><td><div class="block">Serializes specifically when a registry is involved.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;<a href="#type-param-TBuffer" title="type parameter in Serializable">TBuffer</a>,<wbr><a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;<a href="#type-param-TBuffer" title="type parameter in Serializable">TBuffer</a>,<wbr><a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;<a href="#type-param-TBuffer" title="type parameter in Serializable">TBuffer</a>,<wbr><a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="codec()">

:::tabs
== codec
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">com.mojang.serialization.Codec&lt;<a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</span>&nbsp;<span class="element-name">codec</span>()</div>
Returns The codec used for direct serialization..
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="RawSerializable.html#codec()">codec</a></code>&nbsp;in interface&nbsp;<code><a href="RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Returns:</dt>
<dd>The codec used for direct serialization.</dd>
</dl>
</div>
:::


</section>

<section id="mapCodec()">

:::tabs
== mapCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</span>&nbsp;<span class="element-name">mapCodec</span>()</div>
Returns The codec used for complex serialization..
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="RawSerializable.html#mapCodec()">mapCodec</a></code>&nbsp;in interface&nbsp;<code><a href="RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Returns:</dt>
<dd>The codec used for complex serialization.</dd>
</dl>
</div>
:::


</section>

<section id="streamCodec()">

:::tabs
== streamCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.network.codec.StreamCodec&lt;<a href="#type-param-TBuffer" title="type parameter in Serializable">TBuffer</a>,<wbr><a href="#type-param-TSelf" title="type parameter in Serializable">TSelf</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
Returns The codec used for streaming serialization..
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="RawSerializable.html#streamCodec()">streamCodec</a></code>&nbsp;in interface&nbsp;<code><a href="RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Returns:</dt>
<dd>The codec used for streaming serialization.</dd>
</dl>
</div>
:::


</section>

:::::
  

