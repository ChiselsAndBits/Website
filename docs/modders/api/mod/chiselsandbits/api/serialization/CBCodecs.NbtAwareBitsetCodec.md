--- 
title: NbtAwareBitsetCodec
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.serialization](index.md)  
# Record Class NbtAwareBitsetCodec  
**All Implemented Interfaces:**  
Codec\<BitSet\>  

**Enclosing Class:**  
[CBCodecs](CBCodecs.md)  

---
<div class="type-signature"><span class="modifiers">public static record </span><span class="element-name type-name-label">CBCodecs.NbtAwareBitsetCodec</span>()<br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a><br/>  
implements com.mojang.serialization.Codec&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</span></div>  

  

  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 2 -->
::::::: info Nested Class Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from interface&nbsp;com.mojang.serialization.Codec
com.mojang.serialization.Codec.RecursiveCodec&lt;T&gt;, com.mojang.serialization.Codec.ResultFunction&lt;A&gt;
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from interface&nbsp;com.mojang.serialization.Decoder
com.mojang.serialization.Decoder.Boxed&lt;A&gt;, com.mojang.serialization.Decoder.Simple&lt;A&gt;, com.mojang.serialization.Decoder.Terminal&lt;A&gt;
:::::
:::::::
  
  
<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Fields inherited from interface&nbsp;com.mojang.serialization.Codec
BOOL, BYTE, BYTE_BUFFER, DOUBLE, EMPTY, FLOAT, INT, INT_STREAM, LONG, LONG_STREAM, PASSTHROUGH, SHORT, STRING
:::::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E()" class="member-name-link">NbtAwareBitsetCodec</a>()</code></td><td><div class="block">Creates an instance of a <code>NbtAwareBitsetCodec</code> record class.</div><br></td></tr>
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
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;com.mojang.datafixers.util.Pair&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>,<wbr>T&gt;&gt;</code></td><td><code><a href="#decode(com.mojang.serialization.DynamicOps,T)" class="member-name-link">decode</a><wbr>(com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;T&gt;</code></td><td><code><a href="#encode(java.util.BitSet,com.mojang.serialization.DynamicOps,T)" class="member-name-link">encode</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;input,<br> com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;prefix)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;com.mojang.datafixers.util.Pair&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>,<wbr>T&gt;&gt;</code></td><td><code><a href="#decode(com.mojang.serialization.DynamicOps,T)" class="member-name-link">decode</a><wbr>(com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;T&gt;</code></td><td><code><a href="#encode(java.util.BitSet,com.mojang.serialization.DynamicOps,T)" class="member-name-link">encode</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;input,<br> com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;prefix)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;com.mojang.datafixers.util.Pair&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>,<wbr>T&gt;&gt;</code></td><td><code><a href="#decode(com.mojang.serialization.DynamicOps,T)" class="member-name-link">decode</a><wbr>(com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;T&gt;</code></td><td><code><a href="#encode(java.util.BitSet,com.mojang.serialization.DynamicOps,T)" class="member-name-link">encode</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;input,<br> com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;prefix)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.mojang.serialization.Codec
comapFlatMap, deprecated, dispatch, dispatch, dispatchMap, dispatchMap, dispatchStable, fieldOf, flatComapMap, flatXmap, lenientOptionalFieldOf, lenientOptionalFieldOf, lenientOptionalFieldOf, lenientOptionalFieldOf, listOf, listOf, mapResult, optionalFieldOf, optionalFieldOf, optionalFieldOf, optionalFieldOf, orElse, orElse, orElse, orElseGet, orElseGet, orElseGet, partialDispatch, promotePartial, sizeLimitedListOf, stable, validate, withAlternative, withAlternative, withLifecycle, xmap
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.mojang.serialization.Decoder
boxed, decode, flatMap, map, parse, parse, simple, terminal
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;com.mojang.serialization.Encoder
comap, encodeStart, flatComap
:::::
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>()">

:::tabs
== NbtAwareBitsetCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">NbtAwareBitsetCodec</span>()</div>
Creates an instance of a <code>NbtAwareBitsetCodec</code> record class.
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="decode(com.mojang.serialization.DynamicOps,T)">

:::tabs
== decode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>
<span class="return-type">com.mojang.serialization.DataResult&lt;com.mojang.datafixers.util.Pair&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>,<wbr>T&gt;&gt;</span>&nbsp;<span class="element-name">decode</span><wbr><span class="parameters">(com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,
 T&nbsp;input)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>decode</code>&nbsp;in interface&nbsp;<code>com.mojang.serialization.Decoder&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</code></dd>
</dl>
</div>
:::


</section>

<section id="encode(java.util.BitSet,com.mojang.serialization.DynamicOps,T)">

:::tabs
== encode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.DataResult&lt;T&gt;</span>&nbsp;<span class="element-name">encode</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;input,
 com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,
 T&nbsp;prefix)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>encode</code>&nbsp;in interface&nbsp;<code>com.mojang.serialization.Encoder&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&gt;</code></dd>
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
Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. 
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
  

