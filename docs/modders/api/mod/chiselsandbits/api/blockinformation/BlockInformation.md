--- 
title: BlockInformation
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.blockinformation](index.md)  
# Record Class BlockInformation  
**All Implemented Interfaces:**  
[Registry\<BlockInformation\>](../serialization/Serializable.Registry.md), [ISnapshotable\<BlockInformation\>](../util/ISnapshotable.md), Comparable\<BlockInformation\>  

---
<div class="type-signature"><span class="modifiers">public record </span><span class="element-name type-name-label">BlockInformation</span>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;&nbsp;variant)<br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a><br/>  
implements <a href="../serialization/Serializable.Registry.html" title="interface in mod.chiselsandbits.api.serialization">Serializable.Registry</a>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;, <a href="../util/ISnapshotable.html" title="interface in mod.chiselsandbits.api.util">ISnapshotable</a>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span></div>  

  

  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
Nested classes/interfaces inherited from interface&nbsp;mod.chiselsandbits.api.serialization.<a href="../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a><a href="../serialization/Serializable.Registry.html" title="interface in mod.chiselsandbits.api.serialization">Serializable.Registry</a>&lt;TSelf&gt;
:::::
  
  
<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#AIR" class="member-name-link">AIR</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#LEGACY_CODEC" class="member-name-link">LEGACY_CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final com.mojang.serialization.MapCodec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#MAP_CODEC" class="member-name-link">MAP_CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#STREAM_CODEC" class="member-name-link">STREAM_CODEC</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E(net.minecraft.world.level.block.state.BlockState,java.util.Optional)" class="member-name-link">BlockInformation</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;&nbsp;variant)</code></td><td><div class="block">Creates an instance of a <code>BlockInformation</code> record class.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#blockState()" class="member-name-link">blockState</a>()</code></td><td><div class="block">Returns the value of the <code>blockState</code> record component.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">compareTo</a><wbr>(@NotNull <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isAir()" class="member-name-link">isAir</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isFluid()" class="member-name-link">isFluid</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>@Nullable net.minecraft.world.level.block.entity.BlockEntity</code></td><td><code><a href="#newBlockEntity(net.minecraft.core.BlockPos)" class="member-name-link">newBlockEntity</a><wbr>(net.minecraft.core.BlockPos&nbsp;pos)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@Nullable net.minecraft.world.level.block.entity.BlockEntity</code></td><td><code><a href="#newBlockEntityAtZero()" class="member-name-link">newBlockEntityAtZero</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#variant()" class="member-name-link">variant</a>()</code></td><td><div class="block">Returns the value of the <code>variant</code> record component.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#blockState()" class="member-name-link">blockState</a>()</code></td><td><div class="block">Returns the value of the <code>blockState</code> record component.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">compareTo</a><wbr>(@NotNull <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isAir()" class="member-name-link">isAir</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isFluid()" class="member-name-link">isFluid</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>@Nullable net.minecraft.world.level.block.entity.BlockEntity</code></td><td><code><a href="#newBlockEntity(net.minecraft.core.BlockPos)" class="member-name-link">newBlockEntity</a><wbr>(net.minecraft.core.BlockPos&nbsp;pos)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@Nullable net.minecraft.world.level.block.entity.BlockEntity</code></td><td><code><a href="#newBlockEntityAtZero()" class="member-name-link">newBlockEntityAtZero</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#variant()" class="member-name-link">variant</a>()</code></td><td><div class="block">Returns the value of the <code>variant</code> record component.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#blockState()" class="member-name-link">blockState</a>()</code></td><td><div class="block">Returns the value of the <code>blockState</code> record component.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">compareTo</a><wbr>(@NotNull <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isAir()" class="member-name-link">isAir</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isFluid()" class="member-name-link">isFluid</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>@Nullable net.minecraft.world.level.block.entity.BlockEntity</code></td><td><code><a href="#newBlockEntity(net.minecraft.core.BlockPos)" class="member-name-link">newBlockEntity</a><wbr>(net.minecraft.core.BlockPos&nbsp;pos)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@Nullable net.minecraft.world.level.block.entity.BlockEntity</code></td><td><code><a href="#newBlockEntityAtZero()" class="member-name-link">newBlockEntityAtZero</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#variant()" class="member-name-link">variant</a>()</code></td><td><div class="block">Returns the value of the <code>variant</code> record component.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="LEGACY_CODEC">

:::tabs
== LEGACY_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">LEGACY_CODEC</span></div>
</div>
:::


</section>

<section id="CODEC">

:::tabs
== CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
</div>
:::


</section>

<section id="MAP_CODEC">

:::tabs
== MAP_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">MAP_CODEC</span></div>
</div>
:::


</section>

<section id="STREAM_CODEC">

:::tabs
== STREAM_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">STREAM_CODEC</span></div>
</div>
:::


</section>

<section id="AIR">

:::tabs
== AIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">AIR</span></div>
</div>
:::


</section>

:::::
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(net.minecraft.world.level.block.state.BlockState,java.util.Optional)">

:::tabs
== BlockInformation
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">BlockInformation</span><wbr><span class="parameters">(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;&nbsp;variant)</span></div>
Creates an instance of a <code>BlockInformation</code> record class.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockState</code> - the value for the <code>blockState</code> record component</dd>
<dd><code>variant</code> - the value for the <code>variant</code> record component</dd>
</dl>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="isFluid()">

:::tabs
== isFluid
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isFluid</span>()</div>
</div>
:::


</section>

<section id="isAir()">

:::tabs
== isAir
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isAir</span>()</div>
</div>
:::


</section>

<section id="createSnapshot()">

:::tabs
== createSnapshot
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">createSnapshot</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../util/ISnapshotable.html#createSnapshot()">createSnapshot</a></code>&nbsp;in interface&nbsp;<code><a href="../util/ISnapshotable.html" title="interface in mod.chiselsandbits.api.util">ISnapshotable</a>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></dd>
</dl>
</div>
:::


</section>

<section id="compareTo(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== compareTo
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">compareTo</span><wbr><span class="parameters">(@NotNull
 @NotNull <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang" class="external-link">compareTo</a></code>&nbsp;in interface&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></dd>
</dl>
</div>
:::


</section>

<section id="codec()">

:::tabs
== codec
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">codec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../serialization/Serializable.html#codec()">Serializable</a></code></span></div>
Returns The codec used for direct serialization..
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../serialization/RawSerializable.html#codec()">codec</a></code>&nbsp;in interface&nbsp;<code><a href="../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../serialization/Serializable.html#codec()">codec</a></code>&nbsp;in interface&nbsp;<code><a href="../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
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
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">mapCodec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../serialization/Serializable.html#mapCodec()">Serializable</a></code></span></div>
Returns The codec used for complex serialization..
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../serialization/RawSerializable.html#mapCodec()">mapCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../serialization/Serializable.html#mapCodec()">mapCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
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
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../serialization/Serializable.html#streamCodec()">Serializable</a></code></span></div>
Returns The codec used for streaming serialization..
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../serialization/RawSerializable.html#streamCodec()">streamCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../serialization/Serializable.html#streamCodec()">streamCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
<dt>Returns:</dt>
<dd>The codec used for streaming serialization.</dd>
</dl>
</div>
:::


</section>

<section id="newBlockEntityAtZero()">

:::tabs
== newBlockEntityAtZero
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span>&nbsp;<span class="return-type">@Nullable net.minecraft.world.level.block.entity.BlockEntity</span>&nbsp;<span class="element-name">newBlockEntityAtZero</span>()</div>
</div>
:::


</section>

<section id="newBlockEntity(net.minecraft.core.BlockPos)">

:::tabs
== newBlockEntity
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span>&nbsp;<span class="return-type">@Nullable net.minecraft.world.level.block.entity.BlockEntity</span>&nbsp;<span class="element-name">newBlockEntity</span><wbr><span class="parameters">(net.minecraft.core.BlockPos&nbsp;pos)</span></div>
</div>
:::


</section>

<section id="toString()">

:::tabs
== toString
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">toString</span>()</div>
Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html#toString()" title="class or interface in java.lang" class="external-link">toString</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of this object</dd>
</dl>
</div>
:::


</section>

<section id="hashCode()">

:::tabs
== hashCode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">hashCode</span>()</div>
Returns a hash code value for this object. The value is derived from the hash code of each of the record components.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Returns:</dt>
<dd>a hash code value for this object</dd>
</dl>
</div>
:::


</section>

<section id="equals(java.lang.Object)">

:::tabs
== equals
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">equals</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</span></div>
Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. All components in this record class are compared with <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Objects.html#equals(java.lang.Object,java.lang.Object)" title="class or interface in java.util" class="external-link"><code>Objects::equals(Object,Object)</code></a>.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - the object with which to compare</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this object is the same as the <code>o</code> argument; <code>false</code> otherwise.</dd>
</dl>
</div>
:::


</section>

<section id="blockState()">

:::tabs
== blockState
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.world.level.block.state.BlockState</span>&nbsp;<span class="element-name">blockState</span>()</div>
Returns the value of the <code>blockState</code> record component.
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>blockState</code> record component</dd>
</dl>
</div>
:::


</section>

<section id="variant()">

:::tabs
== variant
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">variant</span>()</div>
Returns the value of the <code>variant</code> record component.
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>variant</code> record component</dd>
</dl>
</div>
:::


</section>

:::::
  

