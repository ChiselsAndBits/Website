--- 
title: CBCodecs
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.serialization](index.md)  
# Interface CBCodecs  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">CBCodecs</span></div>  

  

  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Interface</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="CBCodecs.FallbackCodec.html" class="type-name-link" title="class in mod.chiselsandbits.api.serialization">CBCodecs.FallbackCodec</a>&lt;<a href="CBCodecs.FallbackCodec.html#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="CBCodecs.NbtAwareBitsetCodec.html" class="type-name-link" title="class in mod.chiselsandbits.api.serialization">CBCodecs.NbtAwareBitsetCodec</a></code></td><td>&nbsp;</td></tr>
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
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</code></td><td><code><a href="#BIT_SET" class="member-name-link">BIT_SET</a></code></td><td><div class="block">Codec for a bit set.</div><br></td></tr>
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
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#compressed(com.mojang.serialization.Codec)" class="member-name-link">compressed</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</code></td><td><div class="block">Creates a codec that compresses the data using LZ4.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#lazyNbtAware(com.mojang.serialization.Codec,java.util.function.Supplier)" class="member-name-link">lazyNbtAware</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;codec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;? extends net.minecraft.nbt.Tag&gt;&nbsp;lazyTagSupplier)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.MapCodec<wbr>&lt;T&gt;</code></td><td><code><a href="#lazyNbtAware(com.mojang.serialization.MapCodec,java.util.function.Function)" class="member-name-link">lazyNbtAware</a><wbr>(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;codec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T, net.minecraft.nbt.CompoundTag&gt;&nbsp;lazyTagSupplier)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#readLegacyCompressed(com.mojang.serialization.Codec)" class="member-name-link">readLegacyCompressed</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</code></td><td><div class="block">Creates a codec that compresses the data using LZ4.</div><br></td></tr>
  <tr><td><code>static &lt;K,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedComplexMap(com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">unboundedComplexMap</a><wbr>(com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;K,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedComplexMap(java.lang.String,com.mojang.serialization.Codec,java.lang.String,com.mojang.serialization.Codec)" class="member-name-link">unboundedComplexMap</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,<br> com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;value,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;R,<wbr>C,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">unboundedTable</a><wbr>(com.mojang.serialization.Codec&lt;R&gt;&nbsp;row,<br> com.mojang.serialization.Codec&lt;C&gt;&nbsp;column,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;value)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#versioned(com.mojang.serialization.MapCodec,com.mojang.serialization.Codec)" class="member-name-link">versioned</a><wbr>(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;singleVersionCodec,<br> com.mojang.serialization.Codec&lt;T&gt;&nbsp;fallback)</code></td><td><div class="block">Creates a codec that is versioned, but currently only has a single version.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#versioned(java.util.Map,com.mojang.serialization.MapCodec)" class="member-name-link">versioned</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>, com.mojang.serialization.MapCodec&lt;T&gt;&gt;&nbsp;versions,<br> com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;fallback)</code></td><td><div class="block">Creates a codec that is versioned.</div><br></td></tr>
  <tr><td><code>static &lt;F&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;F&gt;</code></td><td><code><a href="#withFallback(com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">withFallback</a><wbr>(com.mojang.serialization.Codec&lt;F&gt;&nbsp;first,<br> com.mojang.serialization.Codec&lt;F&gt;&nbsp;second)</code></td><td><div class="block">Creates a codec that attempts deserialization first using the first codec,<br>and if that fails using the second codec.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#compressed(com.mojang.serialization.Codec)" class="member-name-link">compressed</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</code></td><td><div class="block">Creates a codec that compresses the data using LZ4.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#lazyNbtAware(com.mojang.serialization.Codec,java.util.function.Supplier)" class="member-name-link">lazyNbtAware</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;codec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;? extends net.minecraft.nbt.Tag&gt;&nbsp;lazyTagSupplier)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.MapCodec<wbr>&lt;T&gt;</code></td><td><code><a href="#lazyNbtAware(com.mojang.serialization.MapCodec,java.util.function.Function)" class="member-name-link">lazyNbtAware</a><wbr>(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;codec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T, net.minecraft.nbt.CompoundTag&gt;&nbsp;lazyTagSupplier)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#readLegacyCompressed(com.mojang.serialization.Codec)" class="member-name-link">readLegacyCompressed</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</code></td><td><div class="block">Creates a codec that compresses the data using LZ4.</div><br></td></tr>
  <tr><td><code>static &lt;K,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedComplexMap(com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">unboundedComplexMap</a><wbr>(com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;K,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedComplexMap(java.lang.String,com.mojang.serialization.Codec,java.lang.String,com.mojang.serialization.Codec)" class="member-name-link">unboundedComplexMap</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,<br> com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;value,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;R,<wbr>C,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">unboundedTable</a><wbr>(com.mojang.serialization.Codec&lt;R&gt;&nbsp;row,<br> com.mojang.serialization.Codec&lt;C&gt;&nbsp;column,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;value)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#versioned(com.mojang.serialization.MapCodec,com.mojang.serialization.Codec)" class="member-name-link">versioned</a><wbr>(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;singleVersionCodec,<br> com.mojang.serialization.Codec&lt;T&gt;&nbsp;fallback)</code></td><td><div class="block">Creates a codec that is versioned, but currently only has a single version.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#versioned(java.util.Map,com.mojang.serialization.MapCodec)" class="member-name-link">versioned</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>, com.mojang.serialization.MapCodec&lt;T&gt;&gt;&nbsp;versions,<br> com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;fallback)</code></td><td><div class="block">Creates a codec that is versioned.</div><br></td></tr>
  <tr><td><code>static &lt;F&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;F&gt;</code></td><td><code><a href="#withFallback(com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">withFallback</a><wbr>(com.mojang.serialization.Codec&lt;F&gt;&nbsp;first,<br> com.mojang.serialization.Codec&lt;F&gt;&nbsp;second)</code></td><td><div class="block">Creates a codec that attempts deserialization first using the first codec,<br>and if that fails using the second codec.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="BIT_SET">

:::tabs
== BIT_SET
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</span>&nbsp;<span class="element-name">BIT_SET</span></div>
<div class="block">Codec for a bit set.</div>
</div>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="withFallback(com.mojang.serialization.Codec,com.mojang.serialization.Codec)">

:::tabs
== withFallback
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;F&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;F&gt;</span>&nbsp;<span class="element-name">withFallback</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;F&gt;&nbsp;first,
 com.mojang.serialization.Codec&lt;F&gt;&nbsp;second)</span></div>
<div class="block">Creates a codec that attempts deserialization first using the first codec,
and if that fails using the second codec.
<p>
Serialization always is triggered through the first codec.
</p></div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="withFallback(com.mojang.serialization.Codec,com.mojang.serialization.Codec)-type-param-F"><code>F</code> - The object type that is encoded.</span></dd>
<dt>Parameters:</dt>
<dd><code>first</code> - The first codec to attempt.</dd>
<dd><code>second</code> - The second codec to attempt.</dd>
<dt>Returns:</dt>
<dd>The fallback codec.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="versioned(com.mojang.serialization.MapCodec,com.mojang.serialization.Codec)">

:::tabs
== versioned
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">versioned</span><wbr><span class="parameters">(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;singleVersionCodec,
 com.mojang.serialization.Codec&lt;T&gt;&nbsp;fallback)</span></div>
<div class="block">Creates a codec that is versioned, but currently only has a single version.
The version is stored as an integer in the payload, its value will always be 0</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="versioned(com.mojang.serialization.MapCodec,com.mojang.serialization.Codec)-type-param-T"><code>T</code> - The type of the codec.</span></dd>
<dt>Parameters:</dt>
<dd><code>singleVersionCodec</code> - The versions to use.</dd>
<dt>Returns:</dt>
<dd>The codec.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="versioned(java.util.Map,com.mojang.serialization.MapCodec)">

:::tabs
== versioned
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">versioned</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>, com.mojang.serialization.MapCodec&lt;T&gt;&gt;&nbsp;versions,
 com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;fallback)</span></div>
<div class="block">Creates a codec that is versioned.
The version is stored as an integer in the payload.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="versioned(java.util.Map,com.mojang.serialization.MapCodec)-type-param-T"><code>T</code> - The type of the codec.</span></dd>
<dt>Parameters:</dt>
<dd><code>versions</code> - The versions to use.</dd>
<dt>Returns:</dt>
<dd>The codec.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="readLegacyCompressed(com.mojang.serialization.Codec)">

:::tabs
== readLegacyCompressed
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">readLegacyCompressed</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</span></div>
<div class="block">Creates a codec that compresses the data using LZ4.
The compressed data is stored as a byte array in the payload.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inner</code> - The inner codec.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="compressed(com.mojang.serialization.Codec)">

:::tabs
== compressed
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">compressed</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</span></div>
<div class="block">Creates a codec that compresses the data using LZ4.
The compressed data is stored as a byte array in the payload.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inner</code> - The inner codec.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)">

:::tabs
== unboundedTable
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;R,<wbr>C,<wbr>V&gt;</span>
<span class="return-type">com.mojang.serialization.Codec&lt;com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</span>&nbsp;<span class="element-name">unboundedTable</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;R&gt;&nbsp;row,
 com.mojang.serialization.Codec&lt;C&gt;&nbsp;column,
 com.mojang.serialization.Codec&lt;V&gt;&nbsp;value)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="lazyNbtAware(com.mojang.serialization.Codec,java.util.function.Supplier)">

:::tabs
== lazyNbtAware
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">lazyNbtAware</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;T&gt;&nbsp;codec,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;? extends net.minecraft.nbt.Tag&gt;&nbsp;lazyTagSupplier)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="lazyNbtAware(com.mojang.serialization.MapCodec,java.util.function.Function)">

:::tabs
== lazyNbtAware
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;T&gt;</span>&nbsp;<span class="element-name">lazyNbtAware</span><wbr><span class="parameters">(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;codec,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T, net.minecraft.nbt.CompoundTag&gt;&nbsp;lazyTagSupplier)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="unboundedComplexMap(com.mojang.serialization.Codec,com.mojang.serialization.Codec)">

:::tabs
== unboundedComplexMap
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;K,<wbr>V&gt;</span>
<span class="return-type">com.mojang.serialization.Codec&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</span>&nbsp;<span class="element-name">unboundedComplexMap</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,
 com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="unboundedComplexMap(java.lang.String,com.mojang.serialization.Codec,java.lang.String,com.mojang.serialization.Codec)">

:::tabs
== unboundedComplexMap
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;K,<wbr>V&gt;</span>
<span class="return-type">com.mojang.serialization.Codec&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</span>&nbsp;<span class="element-name">unboundedComplexMap</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,
 com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;value,
 com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</span></div>
</div>
:::


</section>

</li>
</ul>
:::::
  

