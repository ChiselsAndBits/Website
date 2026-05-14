--- 
title: GroupingUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class GroupingUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.GroupingUtils  
  
---
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">GroupingUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for managing grouping of objects
in a collection, based on some key.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T,<wbr>O&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;T&gt;&gt;</code></td><td><code><a href="#groupByUsingList(java.lang.Iterable,java.util.function.Function)" class="member-name-link">groupByUsingList</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a>&lt;T&gt;&nbsp;source,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr>O&gt;&nbsp;extractor)</code></td><td><div class="block">Group the given collection by the given key.</div><br></td></tr>
  <tr><td><code>static &lt;T,<wbr>O&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;T&gt;&gt;</code></td><td><code><a href="#groupByUsingSet(java.lang.Iterable,java.util.function.Function)" class="member-name-link">groupByUsingSet</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a>&lt;T&gt;&nbsp;source,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr>O&gt;&nbsp;extractor)</code></td><td><div class="block">Group the given collection by the given key.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T,<wbr>O&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;T&gt;&gt;</code></td><td><code><a href="#groupByUsingList(java.lang.Iterable,java.util.function.Function)" class="member-name-link">groupByUsingList</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a>&lt;T&gt;&nbsp;source,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr>O&gt;&nbsp;extractor)</code></td><td><div class="block">Group the given collection by the given key.</div><br></td></tr>
  <tr><td><code>static &lt;T,<wbr>O&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;T&gt;&gt;</code></td><td><code><a href="#groupByUsingSet(java.lang.Iterable,java.util.function.Function)" class="member-name-link">groupByUsingSet</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a>&lt;T&gt;&nbsp;source,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr>O&gt;&nbsp;extractor)</code></td><td><div class="block">Group the given collection by the given key.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T,<wbr>O&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;T&gt;&gt;</code></td><td><code><a href="#groupByUsingList(java.lang.Iterable,java.util.function.Function)" class="member-name-link">groupByUsingList</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a>&lt;T&gt;&nbsp;source,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr>O&gt;&nbsp;extractor)</code></td><td><div class="block">Group the given collection by the given key.</div><br></td></tr>
  <tr><td><code>static &lt;T,<wbr>O&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;T&gt;&gt;</code></td><td><code><a href="#groupByUsingSet(java.lang.Iterable,java.util.function.Function)" class="member-name-link">groupByUsingSet</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a>&lt;T&gt;&nbsp;source,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr>O&gt;&nbsp;extractor)</code></td><td><div class="block">Group the given collection by the given key.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="groupByUsingSet(java.lang.Iterable,java.util.function.Function)">

:::tabs
== groupByUsingSet
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="type-parameters">&lt;T,<wbr>O&gt;</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;T&gt;&gt;</span>&nbsp;<span class="element-name">groupByUsingSet</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a>&lt;T&gt;&nbsp;source,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr>O&gt;&nbsp;extractor)</span></div>
Group the given collection by the given key.
Returns a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link"><code>Set</code></a> and as such eliminates duplicates.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="groupByUsingSet(java.lang.Iterable,java.util.function.Function)-type-param-T"><code>T</code> - The type of the objects to group.</span></dd>
<dd><span id="groupByUsingSet(java.lang.Iterable,java.util.function.Function)-type-param-O"><code>O</code> - The key to group by.</span></dd>
<dt>Parameters:</dt>
<dd><code>source</code> - The source collection to group.</dd>
<dd><code>extractor</code> - The key extractor.</dd>
<dt>Returns:</dt>
<dd>A collection of collections, which contain all objects which have the same key.</dd>
</dl>
</div>
:::


</section>

<section id="groupByUsingList(java.lang.Iterable,java.util.function.Function)">

:::tabs
== groupByUsingList
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="type-parameters">&lt;T,<wbr>O&gt;</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;T&gt;&gt;</span>&nbsp;<span class="element-name">groupByUsingList</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang" class="external-link">Iterable</a>&lt;T&gt;&nbsp;source,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr>O&gt;&nbsp;extractor)</span></div>
Group the given collection by the given key.
Returns a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link"><code>List</code></a> and as such does not eliminate duplicates.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="groupByUsingList(java.lang.Iterable,java.util.function.Function)-type-param-T"><code>T</code> - The type of the objects to group.</span></dd>
<dd><span id="groupByUsingList(java.lang.Iterable,java.util.function.Function)-type-param-O"><code>O</code> - The key to group by.</span></dd>
<dt>Parameters:</dt>
<dd><code>source</code> - The source collection to group.</dd>
<dd><code>extractor</code> - The key extractor.</dd>
<dt>Returns:</dt>
<dd>A collection of collections, which contain all objects which have the same key.</dd>
</dl>
</div>
:::


</section>

:::::
  

