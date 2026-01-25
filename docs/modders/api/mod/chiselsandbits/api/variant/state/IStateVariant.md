--- 
title: IStateVariant
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.variant.state](index.md)  
# Interface IStateVariant  
**All Extended Interfaces:**  
Comparable\<IStateVariant\>, [ISnapshotable\<IStateVariant\>](../../util/ISnapshotable.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IStateVariant</span><span class="extends-implements"><br/>  
extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;, <a href="../../util/ISnapshotable.html" title="interface in mod.chiselsandbits.api.util">ISnapshotable</a>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span></div>  

  

Object which provides additional information about a state.
 <p>
     This has to be immutable as it is used in data components in the game.
</p>  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Summary  
:::tabs
== Fields
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td><div class="block">The codec that can be used to serialize a state variant.</div><br></td></tr>
  <tr><td><code>static final com.mojang.serialization.MapCodec<wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#MAP_CODEC" class="member-name-link">MAP_CODEC</a></code></td><td><div class="block">The map codec that can be used to serialize a state variant.</div><br></td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#STREAM_CODEC" class="member-name-link">STREAM_CODEC</a></code></td><td><div class="block">The stream codec that can be used to serialize a state variant.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
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
  <tr><td><code><a href="IStateVariantProvider.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariantProvider</a></code></td><td><code><a href="#provider()" class="member-name-link">provider</a>()</code></td><td><div class="block">Returns The provider that created this state variant..</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#updateBlockEntity(net.minecraft.world.level.block.entity.BlockEntity)" class="member-name-link">updateBlockEntity</a><wbr>(net.minecraft.world.level.block.entity.BlockEntity&nbsp;blockEntity)</code></td><td><div class="block">Updates a block entity with the correct state of this variant.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IStateVariantProvider.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariantProvider</a></code></td><td><code><a href="#provider()" class="member-name-link">provider</a>()</code></td><td><div class="block">Returns The provider that created this state variant..</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#updateBlockEntity(net.minecraft.world.level.block.entity.BlockEntity)" class="member-name-link">updateBlockEntity</a><wbr>(net.minecraft.world.level.block.entity.BlockEntity&nbsp;blockEntity)</code></td><td><div class="block">Updates a block entity with the correct state of this variant.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IStateVariantProvider.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariantProvider</a></code></td><td><code><a href="#provider()" class="member-name-link">provider</a>()</code></td><td><div class="block">Returns The provider that created this state variant..</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#updateBlockEntity(net.minecraft.world.level.block.entity.BlockEntity)" class="member-name-link">updateBlockEntity</a><wbr>(net.minecraft.world.level.block.entity.BlockEntity&nbsp;blockEntity)</code></td><td><div class="block">Updates a block entity with the correct state of this variant.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang" class="external-link">compareTo</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/ISnapshotable.html" title="interface in mod.chiselsandbits.api.util">ISnapshotable</a>
<a href="../../util/ISnapshotable.html#createSnapshot()">createSnapshot</a>
:::::
:::::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="CODEC">

:::tabs
== CODEC
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
The codec that can be used to serialize a state variant.
<dl class="notes"></dl>
:::


</section>

<section id="MAP_CODEC">

:::tabs
== MAP_CODEC
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">MAP_CODEC</span></div>
The map codec that can be used to serialize a state variant.
<dl class="notes"></dl>
:::


</section>

<section id="STREAM_CODEC">

:::tabs
== STREAM_CODEC
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">STREAM_CODEC</span></div>
The stream codec that can be used to serialize a state variant.
<dl class="notes"></dl>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="provider()">

:::tabs
== provider
<div class="member-signature"><span class="return-type"><a href="IStateVariantProvider.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariantProvider</a></span>&nbsp;<span class="element-name">provider</span>()</div>
Returns The provider that created this state variant..
<dl class="notes">
<dt>Returns:</dt>
<dd>The provider that created this state variant.</dd>
</dl>
:::


</section>

<section id="updateBlockEntity(net.minecraft.world.level.block.entity.BlockEntity)">

:::tabs
== updateBlockEntity
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">updateBlockEntity</span><wbr><span class="parameters">(net.minecraft.world.level.block.entity.BlockEntity&nbsp;blockEntity)</span></div>
Updates a block entity with the correct state of this variant.
 <p>
     By default, this does nothing, however a particular implementation can decide to properly instantiate it so that
     the model extraction system can provide other minecraft subsystems, like coloring, the correct information needed
     for this variant.
 </p>
<dl class="notes"></dl>
:::


</section>

:::::
  

