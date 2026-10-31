--- 
title: ComparatorUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Class ComparatorUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.ComparatorUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ComparatorUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for building <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a>s that order <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values, comparing their contents and ranking empty values last.  

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
  <tr><td><code>static &lt;T extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;T&gt;&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;&gt;</code></td><td><code><a href="#createOptionalComparator()" class="member-name-link">createOptionalComparator</a>()</code></td><td><div class="block">Creates a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a> that orders <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values by their contents in natural order, treating any present value as greater than an empty one.</div><br></td></tr>
  <tr><td><code>static &lt;T extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;T&gt;&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;&gt;</code></td><td><code><a href="#createOptionalComparator(java.util.Comparator)" class="member-name-link">createOptionalComparator</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a>&lt;T&gt;&nbsp;comparator)</code></td><td><div class="block">Creates a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a> that orders <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values by the supplied comparator for present contents, treating any present value as greater than an empty one.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;T&gt;&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;&gt;</code></td><td><code><a href="#createOptionalComparator()" class="member-name-link">createOptionalComparator</a>()</code></td><td><div class="block">Creates a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a> that orders <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values by their contents in natural order, treating any present value as greater than an empty one.</div><br></td></tr>
  <tr><td><code>static &lt;T extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;T&gt;&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;&gt;</code></td><td><code><a href="#createOptionalComparator(java.util.Comparator)" class="member-name-link">createOptionalComparator</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a>&lt;T&gt;&nbsp;comparator)</code></td><td><div class="block">Creates a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a> that orders <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values by the supplied comparator for present contents, treating any present value as greater than an empty one.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;T&gt;&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;&gt;</code></td><td><code><a href="#createOptionalComparator()" class="member-name-link">createOptionalComparator</a>()</code></td><td><div class="block">Creates a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a> that orders <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values by their contents in natural order, treating any present value as greater than an empty one.</div><br></td></tr>
  <tr><td><code>static &lt;T extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;T&gt;&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;&gt;</code></td><td><code><a href="#createOptionalComparator(java.util.Comparator)" class="member-name-link">createOptionalComparator</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a>&lt;T&gt;&nbsp;comparator)</code></td><td><div class="block">Creates a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a> that orders <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values by the supplied comparator for present contents, treating any present value as greater than an empty one.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="createOptionalComparator()">

:::tabs
== createOptionalComparator
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="type-parameters">&lt;T extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;T&gt;&gt;</span>
<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;&gt;</span>&nbsp;<span class="element-name">createOptionalComparator</span>()</div>
Creates a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a> that orders <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values by their contents in natural order, treating any present value as greater than an empty one.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="createOptionalComparator()-type-param-T"><code>T</code> - The type of the wrapped, comparable element.</span></dd>
<dt>Returns:</dt>
<dd>A comparator over <code>Optional&lt;T&gt;</code> that compares present values and ranks empties below them.</dd>
</dl>
</div>
:::


</section>

<section id="createOptionalComparator(java.util.Comparator)">

:::tabs
== createOptionalComparator
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="type-parameters">&lt;T extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;T&gt;&gt;</span>
<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;&gt;</span>&nbsp;<span class="element-name">createOptionalComparator</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link">Comparator</a>&lt;T&gt;&nbsp;comparator)</span></div>
Creates a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util" class="external-link"><code>Comparator</code></a> that orders <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> values by the supplied comparator for present contents, treating any present value as greater than an empty one.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="createOptionalComparator(java.util.Comparator)-type-param-T"><code>T</code> - The type of the wrapped element compared by <code>comparator</code>.</span></dd>
<dt>Parameters:</dt>
<dd><code>comparator</code> - The ordering to apply to present values.</dd>
<dt>Returns:</dt>
<dd>A comparator over <code>Optional&lt;T&gt;</code> that delegates present comparisons and ranks empties below them.</dd>
</dl>
</div>
:::


</section>

:::::
  

