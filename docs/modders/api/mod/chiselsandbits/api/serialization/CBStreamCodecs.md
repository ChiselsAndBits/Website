--- 
title: CBStreamCodecs
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.serialization](index)  
# Interface CBStreamCodecs  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">CBStreamCodecs</span></div>  

  

Stream codecs for Chisels &amp; Bits values and common packet transformations.  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.FriendlyByteBuf, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</code></td><td><code><a href="#BIT_SET" class="member-name-link">BIT_SET</a></code></td><td><div class="block">Network codec for bit sets represented as arrays of 64-bit words.</div><br></td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.FriendlyByteBuf, long[]&gt;</code></td><td><code><a href="#LONG_ARRAY" class="member-name-link">LONG_ARRAY</a></code></td><td><div class="block">Network codec for arrays of 64-bit values.</div><br></td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;io.netty.buffer.ByteBuf, net.minecraft.world.phys.Vec3&gt;</code></td><td><code><a href="#VEC_3" class="member-name-link">VEC_3</a></code></td><td><div class="block">Network codec for a three-component floating-point vector.</div><br></td></tr>
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
  <tr><td><code>static &lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>C&gt;</code></td><td><code><a href="#composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)" class="member-name-link">composite</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,<br> com.mojang.datafixers.util.Function7&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>C&gt;&nbsp;p_331335_)</code></td><td><div class="block">Combines seven field codecs, accessors, and a constructor into a codec for a composite value.</div><br></td></tr>
  <tr><td><code>static &lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>C&gt;</code></td><td><code><a href="#composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)" class="member-name-link">composite</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T8&gt;&nbsp;codec8,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T8&gt;&nbsp;getter8,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T9&gt;&nbsp;codec9,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T9&gt;&nbsp;getter9,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T10&gt;&nbsp;codec10,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T10&gt;&nbsp;getter10,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T11&gt;&nbsp;codec11,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T11&gt;&nbsp;getter11,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T12&gt;&nbsp;codec12,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T12&gt;&nbsp;getter12,<br> com.mojang.datafixers.util.Function12&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12,<wbr>C&gt;&nbsp;p_331335_)</code></td><td><div class="block">Combines twelve field codecs, accessors, and a constructor into a codec for a composite value.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;</code></td><td><code><a href="#compressed(net.minecraft.network.codec.StreamCodec)" class="member-name-link">compressed</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;&nbsp;codec)</code></td><td><div class="block">Compresses a registry-aware packet payload with LZ4.</div><br></td></tr>
  <tr><td><code>static &lt;B,<wbr>R,<wbr>D&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>R&gt;</code></td><td><code><a href="#dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)" class="member-name-link">dispatch</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, D&gt;&nbsp;dispatcherCodec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;D, net.minecraft.network.codec.StreamCodec&lt;B, ? extends R&gt;&gt;&nbsp;decoderFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;R,<wbr>D&gt;&nbsp;dispatcherSelector)</code></td><td><div class="block">Selects a payload codec from a discriminator encoded before the payload.</div><br></td></tr>
  <tr><td><code>static &lt;B,<wbr>T&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>T&gt;</code></td><td><code><a href="#lazyInitialized(java.util.function.Supplier)" class="member-name-link">lazyInitialized</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.network.codec.StreamCodec&lt;B,<wbr>T&gt;&gt;&nbsp;supplier)</code></td><td><div class="block">Defers creation of a stream codec until its first encode or decode operation.</div><br></td></tr>
  <tr><td><code>static &lt;B extends net.minecraft.network.FriendlyByteBuf, S&gt;<br>net.minecraft.network.codec.StreamCodec.CodecOperation<wbr>&lt;B,<wbr>S,<wbr>S&gt;</code></td><td><code><a href="#nullable()" class="member-name-link">nullable</a>()</code></td><td><div class="block">Adds a presence bit around a codec so values may be encoded as null.</div><br></td></tr>
  <tr><td><code>static &lt;R, C, V, B extends io.netty.buffer.ByteBuf&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;? super B, com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</code></td><td><code><a href="#table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)" class="member-name-link">table</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;R,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&gt;&nbsp;mapFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapSupplier,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, R&gt;&nbsp;rowCodec,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, C&gt;&nbsp;columnCodec,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, V&gt;&nbsp;valueCodec)</code></td><td><div class="block">Creates a codec that serializes a table as nested row-to-column maps.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>C&gt;</code></td><td><code><a href="#composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)" class="member-name-link">composite</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,<br> com.mojang.datafixers.util.Function7&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>C&gt;&nbsp;p_331335_)</code></td><td><div class="block">Combines seven field codecs, accessors, and a constructor into a codec for a composite value.</div><br></td></tr>
  <tr><td><code>static &lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>C&gt;</code></td><td><code><a href="#composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)" class="member-name-link">composite</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T8&gt;&nbsp;codec8,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T8&gt;&nbsp;getter8,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T9&gt;&nbsp;codec9,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T9&gt;&nbsp;getter9,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T10&gt;&nbsp;codec10,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T10&gt;&nbsp;getter10,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T11&gt;&nbsp;codec11,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T11&gt;&nbsp;getter11,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T12&gt;&nbsp;codec12,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T12&gt;&nbsp;getter12,<br> com.mojang.datafixers.util.Function12&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12,<wbr>C&gt;&nbsp;p_331335_)</code></td><td><div class="block">Combines twelve field codecs, accessors, and a constructor into a codec for a composite value.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;</code></td><td><code><a href="#compressed(net.minecraft.network.codec.StreamCodec)" class="member-name-link">compressed</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;&nbsp;codec)</code></td><td><div class="block">Compresses a registry-aware packet payload with LZ4.</div><br></td></tr>
  <tr><td><code>static &lt;B,<wbr>R,<wbr>D&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>R&gt;</code></td><td><code><a href="#dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)" class="member-name-link">dispatch</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, D&gt;&nbsp;dispatcherCodec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;D, net.minecraft.network.codec.StreamCodec&lt;B, ? extends R&gt;&gt;&nbsp;decoderFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;R,<wbr>D&gt;&nbsp;dispatcherSelector)</code></td><td><div class="block">Selects a payload codec from a discriminator encoded before the payload.</div><br></td></tr>
  <tr><td><code>static &lt;B,<wbr>T&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>T&gt;</code></td><td><code><a href="#lazyInitialized(java.util.function.Supplier)" class="member-name-link">lazyInitialized</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.network.codec.StreamCodec&lt;B,<wbr>T&gt;&gt;&nbsp;supplier)</code></td><td><div class="block">Defers creation of a stream codec until its first encode or decode operation.</div><br></td></tr>
  <tr><td><code>static &lt;B extends net.minecraft.network.FriendlyByteBuf, S&gt;<br>net.minecraft.network.codec.StreamCodec.CodecOperation<wbr>&lt;B,<wbr>S,<wbr>S&gt;</code></td><td><code><a href="#nullable()" class="member-name-link">nullable</a>()</code></td><td><div class="block">Adds a presence bit around a codec so values may be encoded as null.</div><br></td></tr>
  <tr><td><code>static &lt;R, C, V, B extends io.netty.buffer.ByteBuf&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;? super B, com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</code></td><td><code><a href="#table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)" class="member-name-link">table</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;R,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&gt;&nbsp;mapFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapSupplier,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, R&gt;&nbsp;rowCodec,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, C&gt;&nbsp;columnCodec,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, V&gt;&nbsp;valueCodec)</code></td><td><div class="block">Creates a codec that serializes a table as nested row-to-column maps.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="LONG_ARRAY">

:::tabs
== LONG_ARRAY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.FriendlyByteBuf, long[]&gt;</span>&nbsp;<span class="element-name">LONG_ARRAY</span></div>
Network codec for arrays of 64-bit values.
</div>
:::


</section>

<section id="BIT_SET">

:::tabs
== BIT_SET
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.FriendlyByteBuf, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</span>&nbsp;<span class="element-name">BIT_SET</span></div>
Network codec for bit sets represented as arrays of 64-bit words.
</div>
:::


</section>

<section id="VEC_3">

:::tabs
== VEC_3
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;io.netty.buffer.ByteBuf, net.minecraft.world.phys.Vec3&gt;</span>&nbsp;<span class="element-name">VEC_3</span></div>
Network codec for a three-component floating-point vector.
</div>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)">

:::tabs
== table
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;R, C, V, B extends io.netty.buffer.ByteBuf&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;? super B, com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</span>&nbsp;<span class="element-name">table</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;R,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&gt;&nbsp;mapFactory,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapFactory,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapSupplier,
 net.minecraft.network.codec.StreamCodec&lt;? super B, R&gt;&nbsp;rowCodec,
 net.minecraft.network.codec.StreamCodec&lt;? super B, C&gt;&nbsp;columnCodec,
 net.minecraft.network.codec.StreamCodec&lt;? super B, V&gt;&nbsp;valueCodec)</span></div>
Creates a codec that serializes a table as nested row-to-column maps.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)-type-param-R"><code>R</code> - row-key type</span></dd>
<dd><span id="table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)-type-param-C"><code>C</code> - column-key type</span></dd>
<dd><span id="table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)-type-param-V"><code>V</code> - cell-value type</span></dd>
<dd><span id="table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)-type-param-B"><code>B</code> - buffer type</span></dd>
<dt>Parameters:</dt>
<dd><code>mapFactory</code> - factory for the outer row map</dd>
<dd><code>innerMapFactory</code> - factory for each row's column map</dd>
<dd><code>innerMapSupplier</code> - supplier for a new column map</dd>
<dd><code>rowCodec</code> - codec for row keys</dd>
<dd><code>columnCodec</code> - codec for column keys</dd>
<dd><code>valueCodec</code> - codec for cell values</dd>
<dt>Returns:</dt>
<dd>a codec that encodes and decodes the table's rows, columns, and values</dd>
</dl>
</div>
:::


</section>

<section id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)">

:::tabs
== composite
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;B,<wbr>C&gt;</span>&nbsp;<span class="element-name">composite</span><wbr><span class="parameters">(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,
 com.mojang.datafixers.util.Function7&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>C&gt;&nbsp;p_331335_)</span></div>
Combines seven field codecs, accessors, and a constructor into a codec for a composite value.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-B"><code>B</code> - buffer type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-C"><code>C</code> - composite value type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-T1"><code>T1</code> - first field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-T2"><code>T2</code> - second field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-T3"><code>T3</code> - third field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-T4"><code>T4</code> - fourth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-T5"><code>T5</code> - fifth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-T6"><code>T6</code> - sixth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)-type-param-T7"><code>T7</code> - seventh field type</span></dd>
<dt>Parameters:</dt>
<dd><code>codec1</code> - codec for the first field</dd>
<dd><code>getter1</code> - accessor for the first field</dd>
<dd><code>codec2</code> - codec for the second field</dd>
<dd><code>getter2</code> - accessor for the second field</dd>
<dd><code>codec3</code> - codec for the third field</dd>
<dd><code>getter3</code> - accessor for the third field</dd>
<dd><code>codec4</code> - codec for the fourth field</dd>
<dd><code>getter4</code> - accessor for the fourth field</dd>
<dd><code>codec5</code> - codec for the fifth field</dd>
<dd><code>getter5</code> - accessor for the fifth field</dd>
<dd><code>codec6</code> - codec for the sixth field</dd>
<dd><code>getter6</code> - accessor for the sixth field</dd>
<dd><code>codec7</code> - codec for the seventh field</dd>
<dd><code>getter7</code> - accessor for the seventh field</dd>
<dd><code>p_331335_</code> - function that constructs the composite value from the decoded fields</dd>
<dt>Returns:</dt>
<dd>a codec that reads and writes the seven fields in order</dd>
</dl>
</div>
:::


</section>

<section id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)">

:::tabs
== composite
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;B,<wbr>C&gt;</span>&nbsp;<span class="element-name">composite</span><wbr><span class="parameters">(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T8&gt;&nbsp;codec8,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T8&gt;&nbsp;getter8,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T9&gt;&nbsp;codec9,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T9&gt;&nbsp;getter9,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T10&gt;&nbsp;codec10,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T10&gt;&nbsp;getter10,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T11&gt;&nbsp;codec11,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T11&gt;&nbsp;getter11,
 net.minecraft.network.codec.StreamCodec&lt;? super B, T12&gt;&nbsp;codec12,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T12&gt;&nbsp;getter12,
 com.mojang.datafixers.util.Function12&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12,<wbr>C&gt;&nbsp;p_331335_)</span></div>
Combines twelve field codecs, accessors, and a constructor into a codec for a composite value.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-B"><code>B</code> - buffer type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-C"><code>C</code> - composite value type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T1"><code>T1</code> - first field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T2"><code>T2</code> - second field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T3"><code>T3</code> - third field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T4"><code>T4</code> - fourth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T5"><code>T5</code> - fifth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T6"><code>T6</code> - sixth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T7"><code>T7</code> - seventh field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T8"><code>T8</code> - eighth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T9"><code>T9</code> - ninth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T10"><code>T10</code> - tenth field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T11"><code>T11</code> - eleventh field type</span></dd>
<dd><span id="composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)-type-param-T12"><code>T12</code> - twelfth field type</span></dd>
<dt>Parameters:</dt>
<dd><code>codec1</code> - codec for the first field</dd>
<dd><code>getter1</code> - accessor for the first field</dd>
<dd><code>codec2</code> - codec for the second field</dd>
<dd><code>getter2</code> - accessor for the second field</dd>
<dd><code>codec3</code> - codec for the third field</dd>
<dd><code>getter3</code> - accessor for the third field</dd>
<dd><code>codec4</code> - codec for the fourth field</dd>
<dd><code>getter4</code> - accessor for the fourth field</dd>
<dd><code>codec5</code> - codec for the fifth field</dd>
<dd><code>getter5</code> - accessor for the fifth field</dd>
<dd><code>codec6</code> - codec for the sixth field</dd>
<dd><code>getter6</code> - accessor for the sixth field</dd>
<dd><code>codec7</code> - codec for the seventh field</dd>
<dd><code>getter7</code> - accessor for the seventh field</dd>
<dd><code>codec8</code> - codec for the eighth field</dd>
<dd><code>getter8</code> - accessor for the eighth field</dd>
<dd><code>codec9</code> - codec for the ninth field</dd>
<dd><code>getter9</code> - accessor for the ninth field</dd>
<dd><code>codec10</code> - codec for the tenth field</dd>
<dd><code>getter10</code> - accessor for the tenth field</dd>
<dd><code>codec11</code> - codec for the eleventh field</dd>
<dd><code>getter11</code> - accessor for the eleventh field</dd>
<dd><code>codec12</code> - codec for the twelfth field</dd>
<dd><code>getter12</code> - accessor for the twelfth field</dd>
<dd><code>p_331335_</code> - function that constructs the composite value from the decoded fields</dd>
<dt>Returns:</dt>
<dd>a codec that reads and writes the twelve fields in order</dd>
</dl>
</div>
:::


</section>

<section id="compressed(net.minecraft.network.codec.StreamCodec)">

:::tabs
== compressed
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;</span>&nbsp;<span class="element-name">compressed</span><wbr><span class="parameters">(net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;&nbsp;codec)</span></div>
Compresses a registry-aware packet payload with LZ4.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="compressed(net.minecraft.network.codec.StreamCodec)-type-param-T"><code>T</code> - payload type</span></dd>
<dt>Parameters:</dt>
<dd><code>codec</code> - codec for the uncompressed payload</dd>
<dt>Returns:</dt>
<dd>a codec that compresses encoded payloads and decompresses them before decoding</dd>
</dl>
</div>
:::


</section>

<section id="dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)">

:::tabs
== dispatch
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;B,<wbr>R,<wbr>D&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;B,<wbr>R&gt;</span>&nbsp;<span class="element-name">dispatch</span><wbr><span class="parameters">(net.minecraft.network.codec.StreamCodec&lt;? super B, D&gt;&nbsp;dispatcherCodec,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;D, net.minecraft.network.codec.StreamCodec&lt;B, ? extends R&gt;&gt;&nbsp;decoderFactory,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;R,<wbr>D&gt;&nbsp;dispatcherSelector)</span></div>
Selects a payload codec from a discriminator encoded before the payload.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)-type-param-B"><code>B</code> - buffer type</span></dd>
<dd><span id="dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)-type-param-R"><code>R</code> - payload type</span></dd>
<dd><span id="dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)-type-param-D"><code>D</code> - discriminator type</span></dd>
<dt>Parameters:</dt>
<dd><code>dispatcherCodec</code> - codec for the discriminator</dd>
<dd><code>decoderFactory</code> - selects the payload codec for a decoded discriminator</dd>
<dd><code>dispatcherSelector</code> - extracts the discriminator from a value when encoding</dd>
<dt>Returns:</dt>
<dd>a codec that writes the discriminator before the corresponding payload</dd>
</dl>
</div>
:::


</section>

<section id="lazyInitialized(java.util.function.Supplier)">

:::tabs
== lazyInitialized
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;B,<wbr>T&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;B,<wbr>T&gt;</span>&nbsp;<span class="element-name">lazyInitialized</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.network.codec.StreamCodec&lt;B,<wbr>T&gt;&gt;&nbsp;supplier)</span></div>
Defers creation of a stream codec until its first encode or decode operation.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="lazyInitialized(java.util.function.Supplier)-type-param-B"><code>B</code> - buffer type</span></dd>
<dd><span id="lazyInitialized(java.util.function.Supplier)-type-param-T"><code>T</code> - payload type</span></dd>
<dt>Parameters:</dt>
<dd><code>supplier</code> - supplies the codec on its first use</dd>
<dt>Returns:</dt>
<dd>a codec that initializes and caches the supplied codec on first use</dd>
</dl>
</div>
:::


</section>

<section id="nullable()">

:::tabs
== nullable
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;B extends net.minecraft.network.FriendlyByteBuf, S&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec.CodecOperation&lt;B,<wbr>S,<wbr>S&gt;</span>&nbsp;<span class="element-name">nullable</span>()</div>
Adds a presence bit around a codec so values may be encoded as null.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="nullable()-type-param-B"><code>B</code> - friendly byte-buffer type</span></dd>
<dd><span id="nullable()-type-param-S"><code>S</code> - non-null payload type handled by the wrapped codec</span></dd>
<dt>Returns:</dt>
<dd>a codec operation that encodes a presence bit before any non-null value</dd>
</dl>
</div>
:::


</section>

:::::
  

