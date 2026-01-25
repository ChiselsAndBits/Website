--- 
title: IChangeType
aside: false 
---
_Package:_ [mod.chiselsandbits.api.change.changes](index.md)  
# Interface IChangeType  
**All Extended Interfaces:**  
ICustomRegistryEntry  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChangeType</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry</span></div>  

  

<div class="block">The type of registry entry that represents a change.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec for the change..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr>? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec for the change..</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec for the change..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr>? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec for the change..</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec for the change..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr>? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec for the change..</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.communi.suggestu.scena.core.registries.ICustomRegistryEntry
getRegistryName
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="codec()">

:::tabs
== codec
<div class="member-signature"><span class="return-type">com.mojang.serialization.MapCodec&lt;? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</span>&nbsp;<span class="element-name">codec</span>()</div>
<div class="block">Returns The codec for the change..</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The codec for the change.</dd>
</dl>
:::


</section>

<section id="streamCodec()">

:::tabs
== streamCodec
<div class="member-signature"><span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr>? extends <a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
<div class="block">Returns The stream codec for the change..</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The stream codec for the change.</dd>
</dl>
:::


</section>

:::::
  

