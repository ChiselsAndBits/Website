--- 
title: StateEntryStorage
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.storage](index.md)  
# Class StateEntryStorage  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.block.storage.StateEntryStorage  
  
**All Implemented Interfaces:**  
[IMirrorAndRotateble](../../multistate/mutator/IMirrorAndRotateble.md), [IWithBatchableMutationSupport](../../util/IWithBatchableMutationSupport.md), [Serializable\<StateEntryStorage,RegistryFriendlyByteBuf\>](../../serialization/Serializable.md)  

---
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">StateEntryStorage</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><br/>  
implements <a href="../../multistate/mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a>, <a href="../../util/IWithBatchableMutationSupport.html" title="interface in mod.chiselsandbits.api.util">IWithBatchableMutationSupport</a>, <a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>, net.minecraft.network.RegistryFriendlyByteBuf&gt;</span></div>  

  

  

<dl class="notes"></dl>  

<li>
<section class="nested-class-summary" id="nested-class-summary">Nested Class Summary  
Nested classes/interfaces inherited from interface&nbsp;mod.chiselsandbits.api.serialization.<a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a><a href="../../serialization/Serializable.Registry.html" title="interface in mod.chiselsandbits.api.serialization">Serializable.Registry</a>&lt;TSelf&gt;</section>
</li>
  
  
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#LEGACY_CODEC" class="member-name-link">LEGACY_CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#MAP_CODEC" class="member-name-link">MAP_CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#STREAM_CODEC" class="member-name-link">STREAM_CODEC</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E()" class="member-name-link">StateEntryStorage</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="#%3Cinit%3E(int)" class="member-name-link">StateEntryStorage</a><wbr>(int&nbsp;size)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="#%3Cinit%3E(mod.chiselsandbits.api.block.storage.StateEntryPalette,java.util.BitSet)" class="member-name-link">StateEntryStorage</a><wbr>(<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&nbsp;palette,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;data)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../util/IBatchMutation.html" title="interface in mod.chiselsandbits.api.util">IBatchMutation</a></code></td><td><code><a href="#batch()" class="member-name-link">batch</a>()</code></td><td><div class="block">Trigger a batch mutation start.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#count()" class="member-name-link">count</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#count(java.util.function.BiConsumer)" class="member-name-link">count</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/BiConsumer.html" title="class or interface in java.util.function" class="external-link">BiConsumer</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;&nbsp;storageConsumer)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#fillFromBottom(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">fillFromBottom</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state,<br> int&nbsp;entries)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(int,int,int)" class="member-name-link">getBlockInformation</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#getData()" class="member-name-link">getData</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>long[]</code></td><td><code><a href="#getRawData()" class="member-name-link">getRawData</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getSize()" class="member-name-link">getSize</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#initializeWith(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">initializeWith</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;currentState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a></code></td><td><code><a href="#limitedToProgress(float)" class="member-name-link">limitedToProgress</a><wbr>(float&nbsp;progress)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#loadFromChunkSection(net.minecraft.world.level.chunk.LevelChunkSection)" class="member-name-link">loadFromChunkSection</a><wbr>(net.minecraft.world.level.chunk.LevelChunkSection&nbsp;chunkSection)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#mirror(net.minecraft.core.Direction.Axis)" class="member-name-link">mirror</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Mirrors the current multistate block around the given axis.</div><br></td></tr>
  <tr><td><code><a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a></code></td><td><code><a href="#palette()" class="member-name-link">palette</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setBlockInformation(int,int,int,mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setBlockInformation</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z,<br> <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#states()" class="member-name-link">states</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../util/IBatchMutation.html" title="interface in mod.chiselsandbits.api.util">IBatchMutation</a></code></td><td><code><a href="#batch()" class="member-name-link">batch</a>()</code></td><td><div class="block">Trigger a batch mutation start.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#count()" class="member-name-link">count</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#count(java.util.function.BiConsumer)" class="member-name-link">count</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/BiConsumer.html" title="class or interface in java.util.function" class="external-link">BiConsumer</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;&nbsp;storageConsumer)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#fillFromBottom(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">fillFromBottom</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state,<br> int&nbsp;entries)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(int,int,int)" class="member-name-link">getBlockInformation</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#getData()" class="member-name-link">getData</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>long[]</code></td><td><code><a href="#getRawData()" class="member-name-link">getRawData</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getSize()" class="member-name-link">getSize</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#initializeWith(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">initializeWith</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;currentState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a></code></td><td><code><a href="#limitedToProgress(float)" class="member-name-link">limitedToProgress</a><wbr>(float&nbsp;progress)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#loadFromChunkSection(net.minecraft.world.level.chunk.LevelChunkSection)" class="member-name-link">loadFromChunkSection</a><wbr>(net.minecraft.world.level.chunk.LevelChunkSection&nbsp;chunkSection)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#mirror(net.minecraft.core.Direction.Axis)" class="member-name-link">mirror</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Mirrors the current multistate block around the given axis.</div><br></td></tr>
  <tr><td><code><a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a></code></td><td><code><a href="#palette()" class="member-name-link">palette</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setBlockInformation(int,int,int,mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setBlockInformation</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z,<br> <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#states()" class="member-name-link">states</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="../../util/IBatchMutation.html" title="interface in mod.chiselsandbits.api.util">IBatchMutation</a></code></td><td><code><a href="#batch()" class="member-name-link">batch</a>()</code></td><td><div class="block">Trigger a batch mutation start.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#codec()" class="member-name-link">codec</a>()</code></td><td><div class="block">Returns The codec used for direct serialization..</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#count()" class="member-name-link">count</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#count(java.util.function.BiConsumer)" class="member-name-link">count</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/BiConsumer.html" title="class or interface in java.util.function" class="external-link">BiConsumer</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;&nbsp;storageConsumer)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#fillFromBottom(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">fillFromBottom</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state,<br> int&nbsp;entries)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(int,int,int)" class="member-name-link">getBlockInformation</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#getData()" class="member-name-link">getData</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>long[]</code></td><td><code><a href="#getRawData()" class="member-name-link">getRawData</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getSize()" class="member-name-link">getSize</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#initializeWith(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">initializeWith</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;currentState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a></code></td><td><code><a href="#limitedToProgress(float)" class="member-name-link">limitedToProgress</a><wbr>(float&nbsp;progress)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#loadFromChunkSection(net.minecraft.world.level.chunk.LevelChunkSection)" class="member-name-link">loadFromChunkSection</a><wbr>(net.minecraft.world.level.chunk.LevelChunkSection&nbsp;chunkSection)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns The codec used for complex serialization..</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#mirror(net.minecraft.core.Direction.Axis)" class="member-name-link">mirror</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Mirrors the current multistate block around the given axis.</div><br></td></tr>
  <tr><td><code><a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a></code></td><td><code><a href="#palette()" class="member-name-link">palette</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setBlockInformation(int,int,int,mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setBlockInformation</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z,<br> <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#states()" class="member-name-link">states</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The codec used for streaming serialization..</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.mutator.<a href="../../multistate/mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a><a href="../../multistate/mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis)" title="rotate(Direction.Axis)">rotate</a></section>
</li>
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="CODEC">

:::tabs
== CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
</div>
:::


</section>

<section id="LEGACY_CODEC">

:::tabs
== LEGACY_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</span>&nbsp;<span class="element-name">LEGACY_CODEC</span></div>
</div>
:::


</section>

<section id="MAP_CODEC">

:::tabs
== MAP_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</span>&nbsp;<span class="element-name">MAP_CODEC</span></div>
</div>
:::


</section>

<section id="STREAM_CODEC">

:::tabs
== STREAM_CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</span>&nbsp;<span class="element-name">STREAM_CODEC</span></div>
</div>
:::


</section>

:::::
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>()">

:::tabs
== StateEntryStorage
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">StateEntryStorage</span>()</div>
</div>
:::


</section>

<section id="<init>(int)">

:::tabs
== StateEntryStorage
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">StateEntryStorage</span><wbr><span class="parameters">(int&nbsp;size)</span></div>
</div>
:::


</section>

<section id="<init>(mod.chiselsandbits.api.block.storage.StateEntryPalette,java.util.BitSet)">

:::tabs
== StateEntryStorage
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">StateEntryStorage</span><wbr><span class="parameters">(<a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a>&nbsp;palette,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;data)</span></div>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getSize()">

:::tabs
== getSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getSize</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="clear()">

:::tabs
== clear
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">clear</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="initializeWith(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== initializeWith
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">initializeWith</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;currentState)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="loadFromChunkSection(net.minecraft.world.level.chunk.LevelChunkSection)">

:::tabs
== loadFromChunkSection
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">loadFromChunkSection</span><wbr><span class="parameters">(net.minecraft.world.level.chunk.LevelChunkSection&nbsp;chunkSection)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="getBlockInformation(int,int,int)">

:::tabs
== getBlockInformation
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getBlockInformation</span><wbr><span class="parameters">(int&nbsp;x,
 int&nbsp;y,
 int&nbsp;z)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="setBlockInformation(int,int,int,mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== setBlockInformation
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setBlockInformation</span><wbr><span class="parameters">(int&nbsp;x,
 int&nbsp;y,
 int&nbsp;z,
 <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockState)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="count(java.util.function.BiConsumer)">

:::tabs
== count
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">count</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/BiConsumer.html" title="class or interface in java.util.function" class="external-link">BiConsumer</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;&nbsp;storageConsumer)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="count()">

:::tabs
== count
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">count</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getData()">

:::tabs
== getData
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></span>&nbsp;<span class="element-name">getData</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getRawData()">

:::tabs
== getRawData
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">long[]</span>&nbsp;<span class="element-name">getRawData</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="createSnapshot()">

:::tabs
== createSnapshot
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a></span>&nbsp;<span class="element-name">createSnapshot</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="fillFromBottom(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">

:::tabs
== fillFromBottom
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">fillFromBottom</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;state,
 int&nbsp;entries)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="limitedToProgress(float)">

:::tabs
== limitedToProgress
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a></span>&nbsp;<span class="element-name">limitedToProgress</span><wbr><span class="parameters">(float&nbsp;progress)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="palette()">

:::tabs
== palette
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="StateEntryPalette.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette</a></span>&nbsp;<span class="element-name">palette</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="states()">

:::tabs
== states
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">states</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="rotate(net.minecraft.core.Direction.Axis,int)">

:::tabs
== rotate
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">rotate</span><wbr><span class="parameters">(net.minecraft.core.Direction.Axis&nbsp;axis,
 int&nbsp;rotationCount)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../multistate/mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis,int)">IMirrorAndRotateble</a></code></span></div>
<div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../multistate/mutator/IMirrorAndRotateble.html#rotate(net.minecraft.core.Direction.Axis,int)">rotate</a></code>&nbsp;in interface&nbsp;<code><a href="../../multistate/mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a></code></dd>
<dt>Parameters:</dt>
<dd><code>axis</code> - The axis to rotate around.</dd>
<dd><code>rotationCount</code> - The amount of times to rotate the</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="mirror(net.minecraft.core.Direction.Axis)">

:::tabs
== mirror
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">mirror</span><wbr><span class="parameters">(net.minecraft.core.Direction.Axis&nbsp;axis)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../multistate/mutator/IMirrorAndRotateble.html#mirror(net.minecraft.core.Direction.Axis)">IMirrorAndRotateble</a></code></span></div>
<div class="block">Mirrors the current multistate block around the given axis.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../multistate/mutator/IMirrorAndRotateble.html#mirror(net.minecraft.core.Direction.Axis)">mirror</a></code>&nbsp;in interface&nbsp;<code><a href="../../multistate/mutator/IMirrorAndRotateble.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMirrorAndRotateble</a></code></dd>
<dt>Parameters:</dt>
<dd><code>axis</code> - The axis to mirror over.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="batch()">

:::tabs
== batch
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="../../util/IBatchMutation.html" title="interface in mod.chiselsandbits.api.util">IBatchMutation</a></span>&nbsp;<span class="element-name">batch</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../util/IWithBatchableMutationSupport.html#batch()">IWithBatchableMutationSupport</a></code></span></div>
<div class="block">Trigger a batch mutation start.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../util/IWithBatchableMutationSupport.html#batch()">batch</a></code>&nbsp;in interface&nbsp;<code><a href="../../util/IWithBatchableMutationSupport.html" title="interface in mod.chiselsandbits.api.util">IWithBatchableMutationSupport</a></code></dd>
<dt>Returns:</dt>
<dd>The batch mutation lock.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="equals(java.lang.Object)">

:::tabs
== equals
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">equals</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="hashCode()">

:::tabs
== hashCode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="toString()">

:::tabs
== toString
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="codec()">

:::tabs
== codec
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</span>&nbsp;<span class="element-name">codec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../serialization/Serializable.html#codec()">Serializable</a></code></span></div>
<div class="block">Returns The codec used for direct serialization..</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/RawSerializable.html#codec()">codec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/Serializable.html#codec()">codec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>, net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
<dt>Returns:</dt>
<dd>The codec used for direct serialization.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="mapCodec()">

:::tabs
== mapCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</span>&nbsp;<span class="element-name">mapCodec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../serialization/Serializable.html#mapCodec()">Serializable</a></code></span></div>
<div class="block">Returns The codec used for complex serialization..</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/RawSerializable.html#mapCodec()">mapCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/Serializable.html#mapCodec()">mapCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>, net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
<dt>Returns:</dt>
<dd>The codec used for complex serialization.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="streamCodec()">

:::tabs
== streamCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../serialization/Serializable.html#streamCodec()">Serializable</a></code></span></div>
<div class="block">Returns The codec used for streaming serialization..</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/RawSerializable.html#streamCodec()">streamCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../serialization/Serializable.html#streamCodec()">streamCodec</a></code>&nbsp;in interface&nbsp;<code><a href="../../serialization/Serializable.html" title="interface in mod.chiselsandbits.api.serialization">Serializable</a>&lt;<a href="StateEntryStorage.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryStorage</a>, net.minecraft.network.RegistryFriendlyByteBuf&gt;</code></dd>
<dt>Returns:</dt>
<dd>The codec used for streaming serialization.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

