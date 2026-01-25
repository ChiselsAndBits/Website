--- 
title: IChange
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.change.changes](index.md)  
# Interface IChange  
**All Extended Interfaces:**  
[IChangeHandler](IChangeHandler.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChange</span><span class="extends-implements"><br/>  
extends <a href="IChangeHandler.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeHandler</a></span></div>  

  

Represents a single change that has been created with bits.  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</code></td><td><code><a href="#STREAM_CODEC" class="member-name-link">STREAM_CODEC</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IChangeType.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Returns The type of the change..</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IChangeType.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Returns The type of the change..</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IChangeType.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Returns The type of the change..</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.change.changes.<a href="IChangeHandler.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeHandler</a>
<a href="IChangeHandler.html#canRedo(net.minecraft.world.entity.player.Player)">canRedo</a>, <a href="IChangeHandler.html#canUndo(net.minecraft.world.entity.player.Player)">canUndo</a>, <a href="IChangeHandler.html#redo(net.minecraft.world.entity.player.Player)">redo</a>, <a href="IChangeHandler.html#undo(net.minecraft.world.entity.player.Player)">undo</a>
:::::
:::::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="CODEC">

:::tabs
== CODEC
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="STREAM_CODEC">

:::tabs
== STREAM_CODEC
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="IChange.html" title="interface in mod.chiselsandbits.api.change.changes">IChange</a>&gt;</span>&nbsp;<span class="element-name">STREAM_CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getType()">

:::tabs
== getType
<div class="member-signature"><span class="return-type"><a href="IChangeType.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeType</a></span>&nbsp;<span class="element-name">getType</span>()</div>
Returns The type of the change..
<dl class="notes">
<dt>Returns:</dt>
<dd>The type of the change.</dd>
</dl>
:::


</section>

:::::
  

