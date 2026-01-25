--- 
title: Entry
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.storage](index.md)  
# Record Entry  
**All Implemented Interfaces:**  
[Registry\<Entry\>](../serialization/Serializable.Registry.md)  

**Enclosing Class:**  
[StateEntryPalette](StateEntryPalette.md)  

---
<div class="type-signature"><span class="modifiers">public static record </span><span class="element-name type-name-label">StateEntryPalette.Entry</span>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)<br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a><br/>  
implements <a href="../../serialization/Serializable.Registry.html" title="interface in mod.chiselsandbits.api.serialization">Serializable.Registry</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span></div>  

  

  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 2 -->
::::::: info Nested Class Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from interface&nbsp;mod.chiselsandbits.api.serialization.<a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>
<a href="../../serialization/Serializable.Registry.html" title="interface in mod.chiselsandbits.api.serialization">Serializable.Registry</a>&lt;<a href="../../serialization/Serializable.Registry.html" title="type parameter in Serializable.Registry">TSelf</a>&gt;
:::::
:::::::
  
  
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
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#LEGACY_CODEC" class="member-name-link">LEGACY_CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#MAP_CODEC" class="member-name-link">MAP_CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#STREAM_CODEC" class="member-name-link">STREAM_CODEC</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Summary  
:::tabs
== Constructors
<table>
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">Entry</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Creates an instance of a <code>Entry</code> record class.</div><br></td></tr>
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
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#blockInformation()" class="member-name-link">blockInformation</a>()</code></td><td><div class="block">Returns the value of the <code>blockInformation</code> record component.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#blockInformation()" class="member-name-link">blockInformation</a>()</code></td><td><div class="block">Returns the value of the <code>blockInformation</code> record component.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#blockInformation()" class="member-name-link">blockInformation</a>()</code></td><td><div class="block">Returns the value of the <code>blockInformation</code> record component.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="LEGACY_CODEC">

:::tabs
== LEGACY_CODEC
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">LEGACY_CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="CODEC">

:::tabs
== CODEC
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="MAP_CODEC">

:::tabs
== MAP_CODEC
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">MAP_CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="STREAM_CODEC">

:::tabs
== STREAM_CODEC
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">STREAM_CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== Entry
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">Entry</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Creates an instance of a <code>Entry</code> record class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - the value for the <code>blockInformation</code> record component</dd>
</dl>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="codec()">

:::tabs
== codec
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">codec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../serialization/Serializable.html#codec()">Serializable</a></code></span></div>
<div class="block">Returns The codec used for direct serialization..</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/RawSerializable.html#codec()">codec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/Serializable.html#codec()">codec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>,<wbr>net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
<dt>Returns:</dt>
<dd>The codec used for direct serialization.</dd>
</dl>
:::


</section>

<section id="mapCodec()">

:::tabs
== mapCodec
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">mapCodec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../serialization/Serializable.html#mapCodec()">Serializable</a></code></span></div>
<div class="block">Returns The codec used for complex serialization..</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/RawSerializable.html#mapCodec()">mapCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/Serializable.html#mapCodec()">mapCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>,<wbr>net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
<dt>Returns:</dt>
<dd>The codec used for complex serialization.</dd>
</dl>
:::


</section>

<section id="streamCodec()">

:::tabs
== streamCodec
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf,<wbr><a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../serialization/Serializable.html#streamCodec()">Serializable</a></code></span></div>
<div class="block">Returns The codec used for streaming serialization..</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/RawSerializable.html#streamCodec()">streamCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/Serializable.html#streamCodec()">streamCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>,<wbr>net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
<dt>Returns:</dt>
<dd>The codec used for streaming serialization.</dd>
</dl>
:::


</section>

<section id="toString()">

:::tabs
== toString
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">toString</span>()</div>
<div class="block">Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html#toString()" title="class or interface in java.lang" class="external-link">toString</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of this object</dd>
</dl>
:::


</section>

<section id="hashCode()">

:::tabs
== hashCode
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">hashCode</span>()</div>
<div class="block">Returns a hash code value for this object. The value is derived from the hash code of each of the record components.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Returns:</dt>
<dd>a hash code value for this object</dd>
</dl>
:::


</section>

<section id="equals(java.lang.Object)">

:::tabs
== equals
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">equals</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</span></div>
<div class="block">Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. All components in this record class are compared with <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Objects.html#equals(java.lang.Object,java.lang.Object)" title="class or interface in java.util" class="external-link"><code>Objects::equals(Object,Object)</code></a>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - the object with which to compare</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this object is the same as the <code>o</code> argument; <code>false</code> otherwise.</dd>
</dl>
:::


</section>

<section id="blockInformation()">

:::tabs
== blockInformation
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">blockInformation</span>()</div>
<div class="block">Returns the value of the <code>blockInformation</code> record component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>blockInformation</code> record component</dd>
</dl>
:::


</section>

:::::
  

