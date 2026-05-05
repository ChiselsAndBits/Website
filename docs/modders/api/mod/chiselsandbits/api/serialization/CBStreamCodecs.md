--- 
title: CBStreamCodecs
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.serialization](index.md)  
# Interface CBStreamCodecs  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">CBStreamCodecs</span></div>  

  

  

<dl class="notes"></dl>  

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
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.FriendlyByteBuf, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</code></td><td><code><a href="#BIT_SET" class="member-name-link">BIT_SET</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.FriendlyByteBuf, long[]&gt;</code></td><td><code><a href="#LONG_ARRAY" class="member-name-link">LONG_ARRAY</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;io.netty.buffer.ByteBuf, net.minecraft.world.phys.Vec3&gt;</code></td><td><code><a href="#VEC_3" class="member-name-link">VEC_3</a></code></td><td>&nbsp;</td></tr>
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
  <tr><td><code>static &lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>C&gt;</code></td><td><code><a href="#composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)" class="member-name-link">composite</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,<br> com.mojang.datafixers.util.Function7&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>C&gt;&nbsp;p_331335_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>C&gt;</code></td><td><code><a href="#composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)" class="member-name-link">composite</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T8&gt;&nbsp;codec8,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T8&gt;&nbsp;getter8,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T9&gt;&nbsp;codec9,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T9&gt;&nbsp;getter9,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T10&gt;&nbsp;codec10,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T10&gt;&nbsp;getter10,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T11&gt;&nbsp;codec11,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T11&gt;&nbsp;getter11,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T12&gt;&nbsp;codec12,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T12&gt;&nbsp;getter12,<br> com.mojang.datafixers.util.Function12&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12,<wbr>C&gt;&nbsp;p_331335_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;</code></td><td><code><a href="#compressed(net.minecraft.network.codec.StreamCodec)" class="member-name-link">compressed</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;&nbsp;codec)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;B,<wbr>R,<wbr>D&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>R&gt;</code></td><td><code><a href="#dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)" class="member-name-link">dispatch</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, D&gt;&nbsp;dispatcherCodec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;D, net.minecraft.network.codec.StreamCodec&lt;B, ? extends R&gt;&gt;&nbsp;decoderFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;R,<wbr>D&gt;&nbsp;dispatcherSelector)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;B,<wbr>T&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>T&gt;</code></td><td><code><a href="#lazyInitialized(java.util.function.Supplier)" class="member-name-link">lazyInitialized</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.network.codec.StreamCodec&lt;B,<wbr>T&gt;&gt;&nbsp;supplier)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;B extends net.minecraft.network.FriendlyByteBuf, S&gt;<br>net.minecraft.network.codec.StreamCodec.CodecOperation<wbr>&lt;B,<wbr>S,<wbr>S&gt;</code></td><td><code><a href="#nullable()" class="member-name-link">nullable</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;R, C, V, B extends io.netty.buffer.ByteBuf&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;? super B, com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</code></td><td><code><a href="#table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)" class="member-name-link">table</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;R,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&gt;&nbsp;mapFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapSupplier,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, R&gt;&nbsp;rowCodec,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, C&gt;&nbsp;columnCodec,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, V&gt;&nbsp;valueCodec)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>C&gt;</code></td><td><code><a href="#composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function7)" class="member-name-link">composite</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,<br> com.mojang.datafixers.util.Function7&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>C&gt;&nbsp;p_331335_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;B,<wbr>C,<wbr>T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>C&gt;</code></td><td><code><a href="#composite(net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,net.minecraft.network.codec.StreamCodec,java.util.function.Function,com.mojang.datafixers.util.Function12)" class="member-name-link">composite</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, T1&gt;&nbsp;codec1,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T1&gt;&nbsp;getter1,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T2&gt;&nbsp;codec2,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T2&gt;&nbsp;getter2,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T3&gt;&nbsp;codec3,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T3&gt;&nbsp;getter3,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T4&gt;&nbsp;codec4,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T4&gt;&nbsp;getter4,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T5&gt;&nbsp;codec5,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T5&gt;&nbsp;getter5,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T6&gt;&nbsp;codec6,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T6&gt;&nbsp;getter6,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T7&gt;&nbsp;codec7,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T7&gt;&nbsp;getter7,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T8&gt;&nbsp;codec8,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T8&gt;&nbsp;getter8,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T9&gt;&nbsp;codec9,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T9&gt;&nbsp;getter9,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T10&gt;&nbsp;codec10,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T10&gt;&nbsp;getter10,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T11&gt;&nbsp;codec11,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T11&gt;&nbsp;getter11,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, T12&gt;&nbsp;codec12,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;C,<wbr>T12&gt;&nbsp;getter12,<br> com.mojang.datafixers.util.Function12&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>T5,<wbr>T6,<wbr>T7,<wbr>T8,<wbr>T9,<wbr>T10,<wbr>T11,<wbr>T12,<wbr>C&gt;&nbsp;p_331335_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;</code></td><td><code><a href="#compressed(net.minecraft.network.codec.StreamCodec)" class="member-name-link">compressed</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;&nbsp;codec)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;B,<wbr>R,<wbr>D&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>R&gt;</code></td><td><code><a href="#dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)" class="member-name-link">dispatch</a><wbr>(net.minecraft.network.codec.StreamCodec&lt;? super B, D&gt;&nbsp;dispatcherCodec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;D, net.minecraft.network.codec.StreamCodec&lt;B, ? extends R&gt;&gt;&nbsp;decoderFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;R,<wbr>D&gt;&nbsp;dispatcherSelector)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;B,<wbr>T&gt;&nbsp;net.minecraft.network.codec.StreamCodec<wbr>&lt;B,<wbr>T&gt;</code></td><td><code><a href="#lazyInitialized(java.util.function.Supplier)" class="member-name-link">lazyInitialized</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.network.codec.StreamCodec&lt;B,<wbr>T&gt;&gt;&nbsp;supplier)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;B extends net.minecraft.network.FriendlyByteBuf, S&gt;<br>net.minecraft.network.codec.StreamCodec.CodecOperation<wbr>&lt;B,<wbr>S,<wbr>S&gt;</code></td><td><code><a href="#nullable()" class="member-name-link">nullable</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;R, C, V, B extends io.netty.buffer.ByteBuf&gt;<br>net.minecraft.network.codec.StreamCodec<wbr>&lt;? super B, com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</code></td><td><code><a href="#table(java.util.function.IntFunction,java.util.function.IntFunction,java.util.function.Supplier,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec,net.minecraft.network.codec.StreamCodec)" class="member-name-link">table</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;R,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&gt;&nbsp;mapFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapFactory,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;C,<wbr>V&gt;&gt;&nbsp;innerMapSupplier,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, R&gt;&nbsp;rowCodec,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, C&gt;&nbsp;columnCodec,<br> net.minecraft.network.codec.StreamCodec&lt;? super B, V&gt;&nbsp;valueCodec)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="LONG_ARRAY">

:::tabs
== LONG_ARRAY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.FriendlyByteBuf, long[]&gt;</span>&nbsp;<span class="element-name">LONG_ARRAY</span></div>
</div>
:::


</section>

<section id="BIT_SET">

:::tabs
== BIT_SET
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.FriendlyByteBuf, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</span>&nbsp;<span class="element-name">BIT_SET</span></div>
</div>
:::


</section>

<section id="VEC_3">

:::tabs
== VEC_3
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;io.netty.buffer.ByteBuf, net.minecraft.world.phys.Vec3&gt;</span>&nbsp;<span class="element-name">VEC_3</span></div>
</div>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
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
</div>
:::


</section>

</li>
<li>
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
</div>
:::


</section>

</li>
<li>
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
</div>
:::


</section>

</li>
<li>
<section id="compressed(net.minecraft.network.codec.StreamCodec)">

:::tabs
== compressed
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;</span>&nbsp;<span class="element-name">compressed</span><wbr><span class="parameters">(net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, T&gt;&nbsp;codec)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="dispatch(net.minecraft.network.codec.StreamCodec,java.util.function.Function,java.util.function.Function)">

:::tabs
== dispatch
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;B,<wbr>R,<wbr>D&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;B,<wbr>R&gt;</span>&nbsp;<span class="element-name">dispatch</span><wbr><span class="parameters">(net.minecraft.network.codec.StreamCodec&lt;? super B, D&gt;&nbsp;dispatcherCodec,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;D, net.minecraft.network.codec.StreamCodec&lt;B, ? extends R&gt;&gt;&nbsp;decoderFactory,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;R,<wbr>D&gt;&nbsp;dispatcherSelector)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="lazyInitialized(java.util.function.Supplier)">

:::tabs
== lazyInitialized
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;B,<wbr>T&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;B,<wbr>T&gt;</span>&nbsp;<span class="element-name">lazyInitialized</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.network.codec.StreamCodec&lt;B,<wbr>T&gt;&gt;&nbsp;supplier)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="nullable()">

:::tabs
== nullable
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;B extends net.minecraft.network.FriendlyByteBuf, S&gt;</span>
<span class="return-type">net.minecraft.network.codec.StreamCodec.CodecOperation&lt;B,<wbr>S,<wbr>S&gt;</span>&nbsp;<span class="element-name">nullable</span>()</div>
</div>
:::


</section>

</li>
</ul>
:::::
  

