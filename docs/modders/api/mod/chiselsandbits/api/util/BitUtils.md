--- 
title: BitUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Class BitUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.BitUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">BitUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class of helpers for working with raw bits and their masks.  

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
  <tr><td><code>static int</code></td><td><code><a href="#getBitMask(int)" class="member-name-link">getBitMask</a><wbr>(int&nbsp;bitWidth)</code></td><td><div class="block">Returns an int whose lowest <code>bitWidth</code> bits are all set to one; when <code>bitWidth</code> equals 32 the full 32-bit mask is returned.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getByteCount(int)" class="member-name-link">getByteCount</a><wbr>(int&nbsp;totalBitCount)</code></td><td><div class="block">Returns the number of bytes required to store <code>totalBitCount</code> bits, rounding up so any partial last byte counts as a full byte.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getMaskWidth(int)" class="member-name-link">getMaskWidth</a><wbr>(int&nbsp;bitMask)</code></td><td><div class="block">Returns the width in bits of <code>bitMask</code>, equal to one plus the position of its highest set bit (and 32 when every bit is set).</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static int</code></td><td><code><a href="#getBitMask(int)" class="member-name-link">getBitMask</a><wbr>(int&nbsp;bitWidth)</code></td><td><div class="block">Returns an int whose lowest <code>bitWidth</code> bits are all set to one; when <code>bitWidth</code> equals 32 the full 32-bit mask is returned.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getByteCount(int)" class="member-name-link">getByteCount</a><wbr>(int&nbsp;totalBitCount)</code></td><td><div class="block">Returns the number of bytes required to store <code>totalBitCount</code> bits, rounding up so any partial last byte counts as a full byte.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getMaskWidth(int)" class="member-name-link">getMaskWidth</a><wbr>(int&nbsp;bitMask)</code></td><td><div class="block">Returns the width in bits of <code>bitMask</code>, equal to one plus the position of its highest set bit (and 32 when every bit is set).</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static int</code></td><td><code><a href="#getBitMask(int)" class="member-name-link">getBitMask</a><wbr>(int&nbsp;bitWidth)</code></td><td><div class="block">Returns an int whose lowest <code>bitWidth</code> bits are all set to one; when <code>bitWidth</code> equals 32 the full 32-bit mask is returned.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getByteCount(int)" class="member-name-link">getByteCount</a><wbr>(int&nbsp;totalBitCount)</code></td><td><div class="block">Returns the number of bytes required to store <code>totalBitCount</code> bits, rounding up so any partial last byte counts as a full byte.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getMaskWidth(int)" class="member-name-link">getMaskWidth</a><wbr>(int&nbsp;bitMask)</code></td><td><div class="block">Returns the width in bits of <code>bitMask</code>, equal to one plus the position of its highest set bit (and 32 when every bit is set).</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getBitMask(int)">

:::tabs
== getBitMask
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getBitMask</span><wbr><span class="parameters">(int&nbsp;bitWidth)</span></div>
Returns an int whose lowest <code>bitWidth</code> bits are all set to one; when <code>bitWidth</code> equals 32 the full 32-bit mask is returned.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bitWidth</code> - The number of low bits to set.</dd>
<dt>Returns:</dt>
<dd>A bitmask with the given number of trailing set bits, or all 32 bits set if <code>bitWidth</code> is 32.</dd>
</dl>
</div>
:::


</section>

<section id="getByteCount(int)">

:::tabs
== getByteCount
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getByteCount</span><wbr><span class="parameters">(int&nbsp;totalBitCount)</span></div>
Returns the number of bytes required to store <code>totalBitCount</code> bits, rounding up so any partial last byte counts as a full byte.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalBitCount</code> - The total number of bits to encode.</dd>
<dt>Returns:</dt>
<dd>The count of bytes needed for the given bit count, rounded up to a whole byte.</dd>
</dl>
</div>
:::


</section>

<section id="getMaskWidth(int)">

:::tabs
== getMaskWidth
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getMaskWidth</span><wbr><span class="parameters">(int&nbsp;bitMask)</span></div>
Returns the width in bits of <code>bitMask</code>, equal to one plus the position of its highest set bit (and 32 when every bit is set).
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bitMask</code> - The mask whose bit-width is measured.</dd>
<dt>Returns:</dt>
<dd>The number of low bits spanned by the mask, or 32 if all bits are already set.</dd>
</dl>
</div>
:::


</section>

:::::
  

