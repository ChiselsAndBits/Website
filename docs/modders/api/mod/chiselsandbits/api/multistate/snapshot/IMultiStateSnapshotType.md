--- 
title: IMultiStateSnapshotType
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.snapshot](index)  
# Interface IMultiStateSnapshotType  
**All Extended Interfaces:**  
ICustomRegistryEntry  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiStateSnapshotType</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry</span></div>  

  

The type of a multi state snapshot.  

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
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Gets the codec for the snapshot.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, ? extends <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Gets the stream codec for the snapshot.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Gets the codec for the snapshot.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, ? extends <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Gets the stream codec for the snapshot.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Gets the codec for the snapshot.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, ? extends <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Gets the stream codec for the snapshot.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.communi.suggestu.scena.core.registries.ICustomRegistryEntry
getRegistryName
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="codec()">

:::tabs
== codec
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">com.mojang.serialization.MapCodec&lt;? extends <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</span>&nbsp;<span class="element-name">codec</span>()</div>
Gets the codec for the snapshot.
<dl class="notes">
<dt>Returns:</dt>
<dd>The codec.</dd>
</dl>
</div>
:::


</section>

<section id="streamCodec()">

:::tabs
== streamCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, ? extends <a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
Gets the stream codec for the snapshot.
<dl class="notes">
<dt>Returns:</dt>
<dd>The stream codec.</dd>
</dl>
</div>
:::


</section>

:::::
  

