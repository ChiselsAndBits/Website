--- 
title: ByteArrayUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class ByteArrayUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.ByteArrayUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ByteArrayUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

  

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
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#fill(int,int,int)" class="member-name-link">fill</a><wbr>(int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;count)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValue(java.util.BitSet,int,int)" class="member-name-link">getValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValueAt(java.util.BitSet,int,int)" class="member-name-link">getValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValue(java.util.BitSet,int,int,int)" class="member-name-link">setValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueAt(java.util.BitSet,int,int,int)" class="member-name-link">setValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueWith(java.util.BitSet,int,int,int)" class="member-name-link">setValueWith</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#fill(int,int,int)" class="member-name-link">fill</a><wbr>(int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;count)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValue(java.util.BitSet,int,int)" class="member-name-link">getValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValueAt(java.util.BitSet,int,int)" class="member-name-link">getValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValue(java.util.BitSet,int,int,int)" class="member-name-link">setValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueAt(java.util.BitSet,int,int,int)" class="member-name-link">setValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueWith(java.util.BitSet,int,int,int)" class="member-name-link">setValueWith</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#fill(int,int,int)" class="member-name-link">fill</a><wbr>(int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;count)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValue(java.util.BitSet,int,int)" class="member-name-link">getValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValueAt(java.util.BitSet,int,int)" class="member-name-link">getValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValue(java.util.BitSet,int,int,int)" class="member-name-link">setValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueAt(java.util.BitSet,int,int,int)" class="member-name-link">setValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueWith(java.util.BitSet,int,int,int)" class="member-name-link">setValueWith</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;index)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="fill(int,int,int)">
:::tabs
== fill
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></span>&nbsp;<span class="element-name">fill</span><wbr><span class="parameters">(int&nbsp;value,
 int&nbsp;bitWidth,
 int&nbsp;count)</span></div>
</div>
:::
</section>
<section id="setValueAt(java.util.BitSet,int,int,int)">
:::tabs
== setValueAt
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setValueAt</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,
 int&nbsp;value,
 int&nbsp;bitWidth,
 int&nbsp;index)</span></div>
</div>
:::
</section>
<section id="setValueWith(java.util.BitSet,int,int,int)">
:::tabs
== setValueWith
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setValueWith</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,
 int&nbsp;value,
 int&nbsp;bitMask,
 int&nbsp;index)</span></div>
</div>
:::
</section>
<section id="setValue(java.util.BitSet,int,int,int)">
:::tabs
== setValue
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setValue</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,
 int&nbsp;value,
 int&nbsp;bitMask,
 int&nbsp;bitOffset)</span></div>
</div>
:::
</section>
<section id="getValueAt(java.util.BitSet,int,int)">
:::tabs
== getValueAt
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getValueAt</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,
 int&nbsp;bitWidth,
 int&nbsp;index)</span></div>
</div>
:::
</section>
<section id="getValue(java.util.BitSet,int,int)">
:::tabs
== getValue
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getValue</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,
 int&nbsp;bitMask,
 int&nbsp;bitOffset)</span></div>
</div>
:::
</section>
:::::
  

