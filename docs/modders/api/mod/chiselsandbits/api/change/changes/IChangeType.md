--- 
title: IChangeType
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.change.changes](index.md)  
# Interface IChangeType  
**All Extended Interfaces:**  
ICustomRegistryEntry  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChangeType</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry</span></div>  

  

The type of registry entry that represents a change.  

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
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec for the change..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, ? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec for the change..</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec for the change..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, ? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec for the change..</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec for the change..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, ? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec for the change..</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;com.communi.suggestu.scena.core.registries.ICustomRegistryEntrygetRegistryName
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="codec()">

:::tabs
== codec
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">com.mojang.serialization.MapCodec&lt;? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</span>&nbsp;<span class="element-name">codec</span>()</div>
Returns The codec for the change..
<dl class="notes">
<dt>Returns:</dt>
<dd>The codec for the change.</dd>
</dl>
</div>
:::


</section>

<section id="streamCodec()">

:::tabs
== streamCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, ? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
Returns The stream codec for the change..
<dl class="notes">
<dt>Returns:</dt>
<dd>The stream codec for the change.</dd>
</dl>
</div>
:::


</section>

:::::
  

