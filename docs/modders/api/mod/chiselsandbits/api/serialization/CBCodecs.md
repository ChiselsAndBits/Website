--- 
title: CBCodecs
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.serialization](index)  
# Interface CBCodecs  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">CBCodecs</span></div>  

  

Codec helpers for Chisels &amp; Bits serialization formats and compatibility.  

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
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="CBCodecs.FallbackCodec.html" class="type-name-link" title="class in mod.chiselsandbits.api.serialization">CBCodecs.FallbackCodec</a>&lt;<a href="CBCodecs.FallbackCodec.html#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></td><td><div class="block">Codec that reads from primary then fallback, but always writes with primary.</div><br></td></tr>
  <tr><td><code>static final record&nbsp;</code></td><td><code><a href="CBCodecs.NbtAwareBitsetCodec.html" class="type-name-link" title="class in mod.chiselsandbits.api.serialization">CBCodecs.NbtAwareBitsetCodec</a></code></td><td><div class="block">Reads legacy byte-array bitsets as well as the current long-stream representation.</div><br></td></tr>
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
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#lazyNbtAware(com.mojang.serialization.Codec,java.util.function.Supplier)" class="member-name-link">lazyNbtAware</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;codec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;? extends net.minecraft.nbt.Tag&gt;&nbsp;lazyTagSupplier)</code></td><td><div class="block">Wraps a codec so a supplied NBT tag can be reused directly when encoding.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.MapCodec<wbr>&lt;T&gt;</code></td><td><code><a href="#lazyNbtAware(com.mojang.serialization.MapCodec,java.util.function.Function)" class="member-name-link">lazyNbtAware</a><wbr>(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;codec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T, net.minecraft.nbt.CompoundTag&gt;&nbsp;lazyTagSupplier)</code></td><td><div class="block">Wraps a map codec so fields from a supplied NBT compound can be reused when encoding.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#readLegacyCompressed(com.mojang.serialization.Codec)" class="member-name-link">readLegacyCompressed</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</code></td><td><div class="block">Creates a codec that compresses the data using LZ4.</div><br></td></tr>
  <tr><td><code>static &lt;K,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedComplexMap(com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">unboundedComplexMap</a><wbr>(com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</code></td><td><div class="block">Creates a map codec using the default <code>key</code> and <code>value</code> field names.</div><br></td></tr>
  <tr><td><code>static &lt;K,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedComplexMap(java.lang.String,com.mojang.serialization.Codec,java.lang.String,com.mojang.serialization.Codec)" class="member-name-link">unboundedComplexMap</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,<br> com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;value,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</code></td><td><div class="block">Creates a map codec whose entries use the supplied key and value field names.</div><br></td></tr>
  <tr><td><code>static &lt;R,<wbr>C,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">unboundedTable</a><wbr>(com.mojang.serialization.Codec&lt;R&gt;&nbsp;row,<br> com.mojang.serialization.Codec&lt;C&gt;&nbsp;column,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;value)</code></td><td><div class="block">Creates a codec for a table with arbitrary row and column keys.</div><br></td></tr>
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
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#lazyNbtAware(com.mojang.serialization.Codec,java.util.function.Supplier)" class="member-name-link">lazyNbtAware</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;codec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;? extends net.minecraft.nbt.Tag&gt;&nbsp;lazyTagSupplier)</code></td><td><div class="block">Wraps a codec so a supplied NBT tag can be reused directly when encoding.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.MapCodec<wbr>&lt;T&gt;</code></td><td><code><a href="#lazyNbtAware(com.mojang.serialization.MapCodec,java.util.function.Function)" class="member-name-link">lazyNbtAware</a><wbr>(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;codec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T, net.minecraft.nbt.CompoundTag&gt;&nbsp;lazyTagSupplier)</code></td><td><div class="block">Wraps a map codec so fields from a supplied NBT compound can be reused when encoding.</div><br></td></tr>
  <tr><td><code>static &lt;T&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;T&gt;</code></td><td><code><a href="#readLegacyCompressed(com.mojang.serialization.Codec)" class="member-name-link">readLegacyCompressed</a><wbr>(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</code></td><td><div class="block">Creates a codec that compresses the data using LZ4.</div><br></td></tr>
  <tr><td><code>static &lt;K,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedComplexMap(com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">unboundedComplexMap</a><wbr>(com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</code></td><td><div class="block">Creates a map codec using the default <code>key</code> and <code>value</code> field names.</div><br></td></tr>
  <tr><td><code>static &lt;K,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedComplexMap(java.lang.String,com.mojang.serialization.Codec,java.lang.String,com.mojang.serialization.Codec)" class="member-name-link">unboundedComplexMap</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,<br> com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;value,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</code></td><td><div class="block">Creates a map codec whose entries use the supplied key and value field names.</div><br></td></tr>
  <tr><td><code>static &lt;R,<wbr>C,<wbr>V&gt;&nbsp;com.mojang.serialization.Codec<wbr>&lt;com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</code></td><td><code><a href="#unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">unboundedTable</a><wbr>(com.mojang.serialization.Codec&lt;R&gt;&nbsp;row,<br> com.mojang.serialization.Codec&lt;C&gt;&nbsp;column,<br> com.mojang.serialization.Codec&lt;V&gt;&nbsp;value)</code></td><td><div class="block">Creates a codec for a table with arbitrary row and column keys.</div><br></td></tr>
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
Codec for a bit set.
</div>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="withFallback(com.mojang.serialization.Codec,com.mojang.serialization.Codec)">

:::tabs
== withFallback
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;F&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;F&gt;</span>&nbsp;<span class="element-name">withFallback</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;F&gt;&nbsp;first,
 com.mojang.serialization.Codec&lt;F&gt;&nbsp;second)</span></div>
Creates a codec that attempts deserialization first using the first codec,
and if that fails using the second codec.
<p>
Serialization always is triggered through the first codec.
</p>
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

<section id="versioned(com.mojang.serialization.MapCodec,com.mojang.serialization.Codec)">

:::tabs
== versioned
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">versioned</span><wbr><span class="parameters">(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;singleVersionCodec,
 com.mojang.serialization.Codec&lt;T&gt;&nbsp;fallback)</span></div>
Creates a codec that is versioned, but currently only has a single version.
The version is stored as an integer in the payload, its value will always be 0
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="versioned(com.mojang.serialization.MapCodec,com.mojang.serialization.Codec)-type-param-T"><code>T</code> - The type of the codec.</span></dd>
<dt>Parameters:</dt>
<dd><code>singleVersionCodec</code> - The versions to use.</dd>
<dd><code>fallback</code> - codec used to read values from the legacy representation</dd>
<dt>Returns:</dt>
<dd>a versioned codec that writes version zero and can read the fallback format</dd>
</dl>
</div>
:::


</section>

<section id="versioned(java.util.Map,com.mojang.serialization.MapCodec)">

:::tabs
== versioned
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">versioned</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>, com.mojang.serialization.MapCodec&lt;T&gt;&gt;&nbsp;versions,
 com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;fallback)</span></div>
Creates a codec that is versioned.
The version is stored as an integer in the payload.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="versioned(java.util.Map,com.mojang.serialization.MapCodec)-type-param-T"><code>T</code> - The type of the codec.</span></dd>
<dt>Parameters:</dt>
<dd><code>versions</code> - The versions to use.</dd>
<dd><code>fallback</code> - codec used when reading data without a recognized version</dd>
<dt>Returns:</dt>
<dd>a codec that writes the newest supplied version and reads supported versions</dd>
</dl>
</div>
:::


</section>

<section id="readLegacyCompressed(com.mojang.serialization.Codec)">

:::tabs
== readLegacyCompressed
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">readLegacyCompressed</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</span></div>
Creates a codec that compresses the data using LZ4.
The compressed data is stored as a byte array in the payload.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="readLegacyCompressed(com.mojang.serialization.Codec)-type-param-T"><code>T</code> - the decoded value type</span></dd>
<dt>Parameters:</dt>
<dd><code>inner</code> - codec for the uncompressed payload</dd>
<dt>Returns:</dt>
<dd>a codec that reads legacy LZ4-compressed NBT and rejects encoding</dd>
</dl>
</div>
:::


</section>

<section id="compressed(com.mojang.serialization.Codec)">

:::tabs
== compressed
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">compressed</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;T&gt;&nbsp;inner)</span></div>
Creates a codec that compresses the data using LZ4.
The compressed data is stored as a byte array in the payload.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="compressed(com.mojang.serialization.Codec)-type-param-T"><code>T</code> - the encoded value type</span></dd>
<dt>Parameters:</dt>
<dd><code>inner</code> - codec for the uncompressed payload</dd>
<dt>Returns:</dt>
<dd>a codec that reads and writes LZ4-compressed NBT</dd>
</dl>
</div>
:::


</section>

<section id="unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)">

:::tabs
== unboundedTable
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;R,<wbr>C,<wbr>V&gt;</span>
<span class="return-type">com.mojang.serialization.Codec&lt;com.google.common.collect.Table&lt;R,<wbr>C,<wbr>V&gt;&gt;</span>&nbsp;<span class="element-name">unboundedTable</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;R&gt;&nbsp;row,
 com.mojang.serialization.Codec&lt;C&gt;&nbsp;column,
 com.mojang.serialization.Codec&lt;V&gt;&nbsp;value)</span></div>
Creates a codec for a table with arbitrary row and column keys.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)-type-param-R"><code>R</code> - row-key type</span></dd>
<dd><span id="unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)-type-param-C"><code>C</code> - column-key type</span></dd>
<dd><span id="unboundedTable(com.mojang.serialization.Codec,com.mojang.serialization.Codec,com.mojang.serialization.Codec)-type-param-V"><code>V</code> - cell-value type</span></dd>
<dt>Parameters:</dt>
<dd><code>row</code> - codec for table row keys</dd>
<dd><code>column</code> - codec for table column keys</dd>
<dd><code>value</code> - codec for table cell values</dd>
<dt>Returns:</dt>
<dd>a codec that serializes the table as nested row and column maps</dd>
</dl>
</div>
:::


</section>

<section id="lazyNbtAware(com.mojang.serialization.Codec,java.util.function.Supplier)">

:::tabs
== lazyNbtAware
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;T&gt;</span>&nbsp;<span class="element-name">lazyNbtAware</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;T&gt;&nbsp;codec,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;? extends net.minecraft.nbt.Tag&gt;&nbsp;lazyTagSupplier)</span></div>
Wraps a codec so a supplied NBT tag can be reused directly when encoding.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="lazyNbtAware(com.mojang.serialization.Codec,java.util.function.Supplier)-type-param-T"><code>T</code> - value type handled by the codec</span></dd>
<dt>Parameters:</dt>
<dd><code>codec</code> - codec used when no pre-serialized tag is available</dd>
<dd><code>lazyTagSupplier</code> - supplies a reusable encoded tag, or <code>null</code> when unavailable</dd>
<dt>Returns:</dt>
<dd>a codec that uses the supplied tag for encoding when available and delegates decoding</dd>
</dl>
</div>
:::


</section>

<section id="lazyNbtAware(com.mojang.serialization.MapCodec,java.util.function.Function)">

:::tabs
== lazyNbtAware
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.MapCodec&lt;T&gt;</span>&nbsp;<span class="element-name">lazyNbtAware</span><wbr><span class="parameters">(com.mojang.serialization.MapCodec&lt;T&gt;&nbsp;codec,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T, net.minecraft.nbt.CompoundTag&gt;&nbsp;lazyTagSupplier)</span></div>
Wraps a map codec so fields from a supplied NBT compound can be reused when encoding.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="lazyNbtAware(com.mojang.serialization.MapCodec,java.util.function.Function)-type-param-T"><code>T</code> - value type handled by the map codec</span></dd>
<dt>Parameters:</dt>
<dd><code>codec</code> - map codec used when no pre-serialized compound is available</dd>
<dd><code>lazyTagSupplier</code> - extracts a reusable encoded compound, or <code>null</code> when unavailable</dd>
<dt>Returns:</dt>
<dd>a map codec that reuses the supplied compound's fields when available</dd>
</dl>
</div>
:::


</section>

<section id="unboundedComplexMap(com.mojang.serialization.Codec,com.mojang.serialization.Codec)">

:::tabs
== unboundedComplexMap
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;K,<wbr>V&gt;</span>
<span class="return-type">com.mojang.serialization.Codec&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</span>&nbsp;<span class="element-name">unboundedComplexMap</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,
 com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</span></div>
Creates a map codec using the default <code>key</code> and <code>value</code> field names.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="unboundedComplexMap(com.mojang.serialization.Codec,com.mojang.serialization.Codec)-type-param-K"><code>K</code> - map-key type</span></dd>
<dd><span id="unboundedComplexMap(com.mojang.serialization.Codec,com.mojang.serialization.Codec)-type-param-V"><code>V</code> - map-value type</span></dd>
<dt>Parameters:</dt>
<dd><code>keyCodec</code> - codec for map keys</dd>
<dd><code>valueCodec</code> - codec for map values</dd>
<dt>Returns:</dt>
<dd>a codec that stores each entry under <code>key</code> and <code>value</code> fields</dd>
</dl>
</div>
:::


</section>

<section id="unboundedComplexMap(java.lang.String,com.mojang.serialization.Codec,java.lang.String,com.mojang.serialization.Codec)">

:::tabs
== unboundedComplexMap
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;K,<wbr>V&gt;</span>
<span class="return-type">com.mojang.serialization.Codec&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;K,<wbr>V&gt;&gt;</span>&nbsp;<span class="element-name">unboundedComplexMap</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,
 com.mojang.serialization.Codec&lt;K&gt;&nbsp;keyCodec,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;value,
 com.mojang.serialization.Codec&lt;V&gt;&nbsp;valueCodec)</span></div>
Creates a map codec whose entries use the supplied key and value field names.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="unboundedComplexMap(java.lang.String,com.mojang.serialization.Codec,java.lang.String,com.mojang.serialization.Codec)-type-param-K"><code>K</code> - map-key type</span></dd>
<dd><span id="unboundedComplexMap(java.lang.String,com.mojang.serialization.Codec,java.lang.String,com.mojang.serialization.Codec)-type-param-V"><code>V</code> - map-value type</span></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - field name used for each map key</dd>
<dd><code>keyCodec</code> - codec for map keys</dd>
<dd><code>value</code> - field name used for each map value</dd>
<dd><code>valueCodec</code> - codec for map values</dd>
<dt>Returns:</dt>
<dd>a codec that serializes map entries using the supplied field names</dd>
</dl>
</div>
:::


</section>

:::::
  

