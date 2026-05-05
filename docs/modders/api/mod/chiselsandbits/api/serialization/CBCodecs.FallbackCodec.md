--- 
title: FallbackCodec
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.serialization](index.md)  
# Record Class FallbackCodec\<F\>  
**All Implemented Interfaces:**  
Codec\<F\>  

**Enclosing Class:**  
[CBCodecs](CBCodecs.md)  

---
<div class="type-signature"><span class="modifiers">public static record </span><span class="element-name type-name-label">CBCodecs.FallbackCodec&lt;F&gt;</span>(com.mojang.serialization.Codec&lt;<a href="CBCodecs.FallbackCodec.html#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;&nbsp;primary, com.mojang.serialization.Codec&lt;<a href="CBCodecs.FallbackCodec.html#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;&nbsp;fallback)<br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a><br/>  
implements com.mojang.serialization.Codec&lt;F&gt;</span></div>  

  

  

<dl class="notes"></dl>  

<li>
<section class="nested-class-summary" id="nested-class-summary">Nested Class Summary  
Nested classes/interfaces inherited from interface&nbsp;com.mojang.serialization.Codeccom.mojang.serialization.Codec.RecursiveCodec&lt;T&gt;, com.mojang.serialization.Codec.ResultFunction&lt;A&gt;Nested classes/interfaces inherited from interface&nbsp;com.mojang.serialization.Decodercom.mojang.serialization.Decoder.Boxed&lt;A&gt;, com.mojang.serialization.Decoder.Simple&lt;A&gt;, com.mojang.serialization.Decoder.Terminal&lt;A&gt;</section>
</li>
  
  
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">Field Summary  
Fields inherited from interface&nbsp;com.mojang.serialization.CodecBOOL, BYTE, BYTE_BUFFER, DOUBLE, EMPTY, FLOAT, INT, INT_STREAM, LONG, LONG_STREAM, PASSTHROUGH, SHORT, STRING</section>
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
  <tr><td><code><a href="#%3Cinit%3E(com.mojang.serialization.Codec,com.mojang.serialization.Codec)" class="member-name-link">FallbackCodec</a><wbr>(com.mojang.serialization.Codec&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;&nbsp;primary,<br> com.mojang.serialization.Codec&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;&nbsp;fallback)</code></td><td><div class="block">Creates an instance of a <code>FallbackCodec</code> record class.</div><br></td></tr>
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
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;com.mojang.datafixers.util.Pair&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>,<wbr>T&gt;&gt;</code></td><td><code><a href="#decode(com.mojang.serialization.DynamicOps,T)" class="member-name-link">decode</a><wbr>(com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;T&gt;</code></td><td><code><a href="#encode(F,com.mojang.serialization.DynamicOps,T)" class="member-name-link">encode</a><wbr>(<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&nbsp;input,<br> com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;prefix)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></td><td><code><a href="#fallback()" class="member-name-link">fallback</a>()</code></td><td><div class="block">Returns the value of the <code>fallback</code> record component.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></td><td><code><a href="#primary()" class="member-name-link">primary</a>()</code></td><td><div class="block">Returns the value of the <code>primary</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;com.mojang.datafixers.util.Pair&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>,<wbr>T&gt;&gt;</code></td><td><code><a href="#decode(com.mojang.serialization.DynamicOps,T)" class="member-name-link">decode</a><wbr>(com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;T&gt;</code></td><td><code><a href="#encode(F,com.mojang.serialization.DynamicOps,T)" class="member-name-link">encode</a><wbr>(<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&nbsp;input,<br> com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;prefix)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></td><td><code><a href="#fallback()" class="member-name-link">fallback</a>()</code></td><td><div class="block">Returns the value of the <code>fallback</code> record component.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></td><td><code><a href="#primary()" class="member-name-link">primary</a>()</code></td><td><div class="block">Returns the value of the <code>primary</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;com.mojang.datafixers.util.Pair&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>,<wbr>T&gt;&gt;</code></td><td><code><a href="#decode(com.mojang.serialization.DynamicOps,T)" class="member-name-link">decode</a><wbr>(com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;com.mojang.serialization.DataResult<wbr>&lt;T&gt;</code></td><td><code><a href="#encode(F,com.mojang.serialization.DynamicOps,T)" class="member-name-link">encode</a><wbr>(<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&nbsp;input,<br> com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,<br> T&nbsp;prefix)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></td><td><code><a href="#fallback()" class="member-name-link">fallback</a>()</code></td><td><div class="block">Returns the value of the <code>fallback</code> record component.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.Codec<wbr>&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></td><td><code><a href="#primary()" class="member-name-link">primary</a>()</code></td><td><div class="block">Returns the value of the <code>primary</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>Methods inherited from interface&nbsp;com.mojang.serialization.CodeccomapFlatMap, deprecated, dispatch, dispatch, dispatchMap, dispatchMap, dispatchStable, fieldOf, flatComapMap, flatXmap, lenientOptionalFieldOf, lenientOptionalFieldOf, lenientOptionalFieldOf, lenientOptionalFieldOf, listOf, listOf, mapResult, optionalFieldOf, optionalFieldOf, optionalFieldOf, optionalFieldOf, orElse, orElse, orElse, orElseGet, orElseGet, orElseGet, partialDispatch, promotePartial, sizeLimitedListOf, stable, validate, withAlternative, withAlternative, withLifecycle, xmapMethods inherited from interface&nbsp;com.mojang.serialization.Decoderboxed, decode, flatMap, map, parse, parse, simple, terminalMethods inherited from interface&nbsp;com.mojang.serialization.Encodercomap, encodeStart, flatComap</section>
</li>
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(com.mojang.serialization.Codec,com.mojang.serialization.Codec)">

:::tabs
== FallbackCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">FallbackCodec</span><wbr><span class="parameters">(com.mojang.serialization.Codec&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;&nbsp;primary,
 com.mojang.serialization.Codec&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;&nbsp;fallback)</span></div>
<div class="block">Creates an instance of a <code>FallbackCodec</code> record class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>primary</code> - the value for the <code>primary</code> record component</dd>
<dd><code>fallback</code> - the value for the <code>fallback</code> record component</dd>
</dl>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="decode(com.mojang.serialization.DynamicOps,T)">

:::tabs
== decode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>
<span class="return-type">com.mojang.serialization.DataResult&lt;com.mojang.datafixers.util.Pair&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>,<wbr>T&gt;&gt;</span>&nbsp;<span class="element-name">decode</span><wbr><span class="parameters">(com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,
 T&nbsp;input)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>decode</code>&nbsp;in interface&nbsp;<code>com.mojang.serialization.Decoder&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="encode(F,com.mojang.serialization.DynamicOps,T)">

:::tabs
== encode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">com.mojang.serialization.DataResult&lt;T&gt;</span>&nbsp;<span class="element-name">encode</span><wbr><span class="parameters">(<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&nbsp;input,
 com.mojang.serialization.DynamicOps&lt;T&gt;&nbsp;ops,
 T&nbsp;prefix)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>encode</code>&nbsp;in interface&nbsp;<code>com.mojang.serialization.Encoder&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</code></dd>
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
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">toString</span>()</div>
<div class="block">Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html#toString()" title="class or interface in java.lang" class="external-link">toString</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of this object</dd>
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
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">hashCode</span>()</div>
<div class="block">Returns a hash code value for this object. The value is derived from the hash code of each of the record components.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Returns:</dt>
<dd>a hash code value for this object</dd>
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
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">equals</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</span></div>
<div class="block">Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. All components in this record class are compared with <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Objects.html#equals(java.lang.Object,java.lang.Object)" title="class or interface in java.util" class="external-link"><code>Objects::equals(Object,Object)</code></a>.</div>
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

</li>
<li>
<section id="primary()">

:::tabs
== primary
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</span>&nbsp;<span class="element-name">primary</span>()</div>
<div class="block">Returns the value of the <code>primary</code> record component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>primary</code> record component</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="fallback()">

:::tabs
== fallback
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="#type-param-F" title="type parameter in CBCodecs.FallbackCodec">F</a>&gt;</span>&nbsp;<span class="element-name">fallback</span>()</div>
<div class="block">Returns the value of the <code>fallback</code> record component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>fallback</code> record component</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

