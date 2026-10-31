--- 
title: StateEntryPalette
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.storage](index)  
# Record Class StateEntryPalette  
---
<div class="type-signature"><span class="modifiers">public record </span><span class="element-name type-name-label">StateEntryPalette</span>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;&nbsp;paletteEntries, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;&nbsp;paletteMap)<br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></span></div>  

  

Maps block information to compact indices used by multistate storage.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="StateEntryPalette.Entry.html" class="type-name-link" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a></code></td><td><div class="block">Palette entry pairing a packed palette index with its block information.</div><br></td></tr>
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="StateEntryPalette.Result.html" class="type-name-link" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a>&lt;<a href="StateEntryPalette.Result.html#type-param-T" title="type parameter in StateEntryPalette.Result">T</a>&gt;</code></td><td><div class="block">Represents the result of a palette operation.</div><br></td></tr>
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="StateEntryPalette.SizeInformation.html" class="type-name-link" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></code></td><td><div class="block">Represents the size information of the palette.</div><br></td></tr>
  </tbody>
</table>
:::
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
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td><div class="block">Codec for serializing the palette's ordered entries.</div><br></td></tr>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&gt;</code></td><td><code><a href="#LEGACY_CODEC" class="member-name-link">LEGACY_CODEC</a></code></td><td><div class="block">Codec for reading palettes written with the legacy entry format.</div><br></td></tr>
  <tr><td><code>static final com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&gt;</code></td><td><code><a href="#MAP_CODEC" class="member-name-link">MAP_CODEC</a></code></td><td><div class="block">Map codec for embedding this palette in another serialized object.</div><br></td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&gt;</code></td><td><code><a href="#STREAM_CODEC" class="member-name-link">STREAM_CODEC</a></code></td><td><div class="block">Network codec for the ordered palette entries.</div><br></td></tr>
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
  <tr><td><code><a href="#%3Cinit%3E()" class="member-name-link">StateEntryPalette</a>()</code></td><td><div class="block">Creates an empty palette containing the required air entry.</div><br></td></tr>
  <tr><td><code><a href="#%3Cinit%3E(java.util.List)" class="member-name-link">StateEntryPalette</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;&nbsp;paletteEntries)</code></td><td><div class="block">Creates a palette and lookup map from the supplied entries.</div><br></td></tr>
  <tr><td><code><a href="#%3Cinit%3E(java.util.List,java.util.Map)" class="member-name-link">StateEntryPalette</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;&nbsp;paletteEntries,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;&nbsp;paletteMap)</code></td><td><div class="block">Creates a palette from its ordered entries and state lookup map, adding air if absent.</div><br></td></tr>
  <tr><td><code><a href="#%3Cinit%3E(mod.chiselsandbits.api.block.storage.StateEntryPalette)" class="member-name-link">StateEntryPalette</a><wbr>(<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&nbsp;palette)</code></td><td><div class="block">Copies the palette entries and lookup map from another palette.</div><br></td></tr>
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
  <tr><td><code><a href="StateEntryPalette.Result.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears all entries and restores the required air entry.</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockState(int)" class="member-name-link">getBlockState</a><wbr>(int&nbsp;blockStateId)</code></td><td><div class="block">Resolves a palette index to its block information, using air for invalid indices.</div><br></td></tr>
  <tr><td><code><a href="StateEntryPalette.Result.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getIndex(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getIndex</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state)</code></td><td><div class="block">Returns the existing index for a state, adding it to the palette when absent.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#paletteEntries()" class="member-name-link">paletteEntries</a>()</code></td><td><div class="block">Returns the palette entries in index order as an unmodifiable list.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#paletteMap()" class="member-name-link">paletteMap</a>()</code></td><td><div class="block">Returns the block-information lookup as an unmodifiable map.</div><br></td></tr>
  <tr><td><code>long</code></td><td><code><a href="#size()" class="member-name-link">size</a>()</code></td><td><div class="block">Returns the number of entries currently stored in the palette.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#states()" class="member-name-link">states</a>()</code></td><td><div class="block">Returns the block information values currently represented by this palette.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="StateEntryPalette.Result.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears all entries and restores the required air entry.</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockState(int)" class="member-name-link">getBlockState</a><wbr>(int&nbsp;blockStateId)</code></td><td><div class="block">Resolves a palette index to its block information, using air for invalid indices.</div><br></td></tr>
  <tr><td><code><a href="StateEntryPalette.Result.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getIndex(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getIndex</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state)</code></td><td><div class="block">Returns the existing index for a state, adding it to the palette when absent.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#paletteEntries()" class="member-name-link">paletteEntries</a>()</code></td><td><div class="block">Returns the palette entries in index order as an unmodifiable list.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#paletteMap()" class="member-name-link">paletteMap</a>()</code></td><td><div class="block">Returns the block-information lookup as an unmodifiable map.</div><br></td></tr>
  <tr><td><code>long</code></td><td><code><a href="#size()" class="member-name-link">size</a>()</code></td><td><div class="block">Returns the number of entries currently stored in the palette.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#states()" class="member-name-link">states</a>()</code></td><td><div class="block">Returns the block information values currently represented by this palette.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="StateEntryPalette.Result.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears all entries and restores the required air entry.</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockState(int)" class="member-name-link">getBlockState</a><wbr>(int&nbsp;blockStateId)</code></td><td><div class="block">Resolves a palette index to its block information, using air for invalid indices.</div><br></td></tr>
  <tr><td><code><a href="StateEntryPalette.Result.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getIndex(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getIndex</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state)</code></td><td><div class="block">Returns the existing index for a state, adding it to the palette when absent.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#paletteEntries()" class="member-name-link">paletteEntries</a>()</code></td><td><div class="block">Returns the palette entries in index order as an unmodifiable list.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</code></td><td><code><a href="#paletteMap()" class="member-name-link">paletteMap</a>()</code></td><td><div class="block">Returns the block-information lookup as an unmodifiable map.</div><br></td></tr>
  <tr><td><code>long</code></td><td><code><a href="#size()" class="member-name-link">size</a>()</code></td><td><div class="block">Returns the number of entries currently stored in the palette.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#states()" class="member-name-link">states</a>()</code></td><td><div class="block">Returns the block information values currently represented by this palette.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="CODEC">

:::tabs
== CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
Codec for serializing the palette's ordered entries.
</div>
:::


</section>

<section id="LEGACY_CODEC">

:::tabs
== LEGACY_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&gt;</span>&nbsp;<span class="element-name">LEGACY_CODEC</span></div>
Codec for reading palettes written with the legacy entry format.
</div>
:::


</section>

<section id="MAP_CODEC">

:::tabs
== MAP_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&gt;</span>&nbsp;<span class="element-name">MAP_CODEC</span></div>
Map codec for embedding this palette in another serialized object.
</div>
:::


</section>

<section id="STREAM_CODEC">

:::tabs
== STREAM_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&gt;</span>&nbsp;<span class="element-name">STREAM_CODEC</span></div>
Network codec for the ordered palette entries.
</div>
:::


</section>

:::::
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>()">

:::tabs
== StateEntryPalette
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">StateEntryPalette</span>()</div>
Creates an empty palette containing the required air entry.
</div>
:::


</section>

<section id="<init>(mod.chiselsandbits.api.block.storage.StateEntryPalette)">

:::tabs
== StateEntryPalette
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">StateEntryPalette</span><wbr><span class="parameters">(<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&nbsp;palette)</span></div>
Copies the palette entries and lookup map from another palette.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>palette</code> - palette whose entries and lookup map are copied</dd>
</dl>
</div>
:::


</section>

<section id="<init>(java.util.List)">

:::tabs
== StateEntryPalette
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">StateEntryPalette</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;&nbsp;paletteEntries)</span></div>
Creates a palette and lookup map from the supplied entries.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>paletteEntries</code> - entries to store in palette-index order</dd>
</dl>
</div>
:::


</section>

<section id="<init>(java.util.List,java.util.Map)">

:::tabs
== StateEntryPalette
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">StateEntryPalette</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;&nbsp;paletteEntries,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;&nbsp;paletteMap)</span></div>
Creates a palette from its ordered entries and state lookup map, adding air if absent.
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="paletteEntries()">

:::tabs
== paletteEntries
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">paletteEntries</span>()</div>
Returns the palette entries in index order as an unmodifiable list.
<dl class="notes">
<dt>Returns:</dt>
<dd>an unmodifiable view of the entries in palette-index order</dd>
</dl>
</div>
:::


</section>

<section id="paletteMap()">

:::tabs
== paletteMap
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="StateEntryPalette.Entry.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Entry</a>&gt;</span>&nbsp;<span class="element-name">paletteMap</span>()</div>
Returns the block-information lookup as an unmodifiable map.
<dl class="notes">
<dt>Returns:</dt>
<dd>an unmodifiable view mapping each block information value to its entry</dd>
</dl>
</div>
:::


</section>

<section id="size()">

:::tabs
== size
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">long</span>&nbsp;<span class="element-name">size</span>()</div>
Returns the number of entries currently stored in the palette.
<dl class="notes">
<dt>Returns:</dt>
<dd>the number of palette entries, including the required air entry</dd>
</dl>
</div>
:::


</section>

<section id="getIndex(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== getIndex
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="StateEntryPalette.Result.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getIndex</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state)</span></div>
Returns the existing index for a state, adding it to the palette when absent.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - block information to look up or add</dd>
<dt>Returns:</dt>
<dd>the palette index and whether adding the state changed the palette size</dd>
</dl>
</div>
:::


</section>

<section id="getBlockState(int)">

:::tabs
== getBlockState
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getBlockState</span><wbr><span class="parameters">(int&nbsp;blockStateId)</span></div>
Resolves a palette index to its block information, using air for invalid indices.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockStateId</code> - palette index to resolve</dd>
<dt>Returns:</dt>
<dd>the indexed block information, or air when the index is invalid</dd>
</dl>
</div>
:::


</section>

<section id="clear()">

:::tabs
== clear
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="StateEntryPalette.Result.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.Result</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">clear</span>()</div>
Clears all entries and restores the required air entry.
<dl class="notes">
<dt>Returns:</dt>
<dd>the palette index of the restored air entry and the resulting size change</dd>
</dl>
</div>
:::


</section>

<section id="states()">

:::tabs
== states
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">states</span>()</div>
Returns the block information values currently represented by this palette.
<dl class="notes">
<dt>Returns:</dt>
<dd>the block information keys currently present in the palette lookup</dd>
</dl>
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

:::::
  

