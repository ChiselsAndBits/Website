--- 
title: ArrayUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class ArrayUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.ArrayUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ArrayUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for manipulating arrays.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T extends <a href="ISnapshotable.html" title="interface in mod.chiselsandbits.api.util">ISnapshotable</a>&lt;? extends T&gt;&gt;<br>T[]</code></td><td><code><a href="#createDeepClone(T%5B%5D,java.util.function.IntFunction)" class="member-name-link">createDeepClone</a><wbr>(T[]&nbsp;additionalStateInfos,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;T[]&gt;&nbsp;arrayCreator)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static float[]</code></td><td><code><a href="#multiply(float%5B%5D,float)" class="member-name-link">multiply</a><wbr>(float[]&nbsp;input,<br> float&nbsp;count)</code></td><td><div class="block">Multiplies the given array by the given factor.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T extends <a href="ISnapshotable.html" title="interface in mod.chiselsandbits.api.util">ISnapshotable</a>&lt;? extends T&gt;&gt;<br>T[]</code></td><td><code><a href="#createDeepClone(T%5B%5D,java.util.function.IntFunction)" class="member-name-link">createDeepClone</a><wbr>(T[]&nbsp;additionalStateInfos,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;T[]&gt;&nbsp;arrayCreator)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static float[]</code></td><td><code><a href="#multiply(float%5B%5D,float)" class="member-name-link">multiply</a><wbr>(float[]&nbsp;input,<br> float&nbsp;count)</code></td><td><div class="block">Multiplies the given array by the given factor.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T extends <a href="ISnapshotable.html" title="interface in mod.chiselsandbits.api.util">ISnapshotable</a>&lt;? extends T&gt;&gt;<br>T[]</code></td><td><code><a href="#createDeepClone(T%5B%5D,java.util.function.IntFunction)" class="member-name-link">createDeepClone</a><wbr>(T[]&nbsp;additionalStateInfos,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;T[]&gt;&nbsp;arrayCreator)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static float[]</code></td><td><code><a href="#multiply(float%5B%5D,float)" class="member-name-link">multiply</a><wbr>(float[]&nbsp;input,<br> float&nbsp;count)</code></td><td><div class="block">Multiplies the given array by the given factor.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="multiply(float[],float)">

:::tabs
== multiply
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">float[]</span>&nbsp;<span class="element-name">multiply</span><wbr><span class="parameters">(float[]&nbsp;input,
 float&nbsp;count)</span></div>
Multiplies the given array by the given factor.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - The input array.</dd>
<dd><code>count</code> - The factor to multiply the arrays values by.</dd>
<dt>Returns:</dt>
<dd>A new array with the values of the old array multiplied by the given factor.</dd>
</dl>
:::


</section>

<section id="createDeepClone(T[],java.util.function.IntFunction)">

:::tabs
== createDeepClone
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="type-parameters">&lt;T extends <a href="ISnapshotable.html" title="interface in mod.chiselsandbits.api.util">ISnapshotable</a>&lt;? extends T&gt;&gt;</span>
<span class="return-type">T[]</span>&nbsp;<span class="element-name">createDeepClone</span><wbr><span class="parameters">(T[]&nbsp;additionalStateInfos,
 <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/IntFunction.html" title="class or interface in java.util.function" class="external-link">IntFunction</a>&lt;T[]&gt;&nbsp;arrayCreator)</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

