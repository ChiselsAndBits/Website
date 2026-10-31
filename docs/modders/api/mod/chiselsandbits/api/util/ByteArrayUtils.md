--- 
title: ByteArrayUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Class ByteArrayUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.ByteArrayUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ByteArrayUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for reading and writing integer values inside a <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link"><code>BitSet</code></a>, packing one value into a fixed range of bits.  

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
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#fill(int,int,int)" class="member-name-link">fill</a><wbr>(int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;count)</code></td><td><div class="block">Builds a new <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link"><code>BitSet</code></a> containing <code>value</code> repeated <code>count</code> times, each copy occupying <code>bitWidth</code> consecutive bits at successive offsets.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValue(java.util.BitSet,int,int)" class="member-name-link">getValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td><div class="block">Reads a value from <code>target</code> starting at <code>bitOffset</code>, reconstructing it from the bits selected by <code>bitMask</code>.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValueAt(java.util.BitSet,int,int)" class="member-name-link">getValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td><div class="block">Reads the <code>bitWidth</code>-bit field starting at slot <code>index</code> from <code>target</code>.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValue(java.util.BitSet,int,int,int)" class="member-name-link">setValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td><div class="block">Writes <code>value</code> into <code>target</code> starting at <code>bitOffset</code>, clearing the field first and setting only the bits selected by <code>bitMask</code>.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueAt(java.util.BitSet,int,int,int)" class="member-name-link">setValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td><div class="block">Overwrites the <code>bitWidth</code>-bit field starting at slot <code>index</code> within <code>target</code> with the given value.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueWith(java.util.BitSet,int,int,int)" class="member-name-link">setValueWith</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;index)</code></td><td><div class="block">Overwrites the field starting at slot <code>index</code> within <code>target</code>, deriving its width from <code>bitMask</code>.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#fill(int,int,int)" class="member-name-link">fill</a><wbr>(int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;count)</code></td><td><div class="block">Builds a new <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link"><code>BitSet</code></a> containing <code>value</code> repeated <code>count</code> times, each copy occupying <code>bitWidth</code> consecutive bits at successive offsets.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValue(java.util.BitSet,int,int)" class="member-name-link">getValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td><div class="block">Reads a value from <code>target</code> starting at <code>bitOffset</code>, reconstructing it from the bits selected by <code>bitMask</code>.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValueAt(java.util.BitSet,int,int)" class="member-name-link">getValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td><div class="block">Reads the <code>bitWidth</code>-bit field starting at slot <code>index</code> from <code>target</code>.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValue(java.util.BitSet,int,int,int)" class="member-name-link">setValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td><div class="block">Writes <code>value</code> into <code>target</code> starting at <code>bitOffset</code>, clearing the field first and setting only the bits selected by <code>bitMask</code>.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueAt(java.util.BitSet,int,int,int)" class="member-name-link">setValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td><div class="block">Overwrites the <code>bitWidth</code>-bit field starting at slot <code>index</code> within <code>target</code> with the given value.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueWith(java.util.BitSet,int,int,int)" class="member-name-link">setValueWith</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;index)</code></td><td><div class="block">Overwrites the field starting at slot <code>index</code> within <code>target</code>, deriving its width from <code>bitMask</code>.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></code></td><td><code><a href="#fill(int,int,int)" class="member-name-link">fill</a><wbr>(int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;count)</code></td><td><div class="block">Builds a new <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link"><code>BitSet</code></a> containing <code>value</code> repeated <code>count</code> times, each copy occupying <code>bitWidth</code> consecutive bits at successive offsets.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValue(java.util.BitSet,int,int)" class="member-name-link">getValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td><div class="block">Reads a value from <code>target</code> starting at <code>bitOffset</code>, reconstructing it from the bits selected by <code>bitMask</code>.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#getValueAt(java.util.BitSet,int,int)" class="member-name-link">getValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td><div class="block">Reads the <code>bitWidth</code>-bit field starting at slot <code>index</code> from <code>target</code>.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValue(java.util.BitSet,int,int,int)" class="member-name-link">setValue</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;bitOffset)</code></td><td><div class="block">Writes <code>value</code> into <code>target</code> starting at <code>bitOffset</code>, clearing the field first and setting only the bits selected by <code>bitMask</code>.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueAt(java.util.BitSet,int,int,int)" class="member-name-link">setValueAt</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitWidth,<br> int&nbsp;index)</code></td><td><div class="block">Overwrites the <code>bitWidth</code>-bit field starting at slot <code>index</code> within <code>target</code> with the given value.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setValueWith(java.util.BitSet,int,int,int)" class="member-name-link">setValueWith</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a>&nbsp;target,<br> int&nbsp;value,<br> int&nbsp;bitMask,<br> int&nbsp;index)</code></td><td><div class="block">Overwrites the field starting at slot <code>index</code> within <code>target</code>, deriving its width from <code>bitMask</code>.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="fill(int,int,int)">

:::tabs
== fill
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link">BitSet</a></span>&nbsp;<span class="element-name">fill</span><wbr><span class="parameters">(int&nbsp;value,
 int&nbsp;bitWidth,
 int&nbsp;count)</span></div>
Builds a new <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/BitSet.html" title="class or interface in java.util" class="external-link"><code>BitSet</code></a> containing <code>value</code> repeated <code>count</code> times, each copy occupying <code>bitWidth</code> consecutive bits at successive offsets.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - The value to store in each slot.</dd>
<dd><code>bitWidth</code> - The number of bits used for each stored value.</dd>
<dd><code>count</code> - How many values to pack into the set.</dd>
<dt>Returns:</dt>
<dd>A fresh BitSet sized <code>bitWidth * count</code>, with each of the first <code>count</code> slots holding a masked copy of <code>value</code>.</dd>
</dl>
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
Overwrites the <code>bitWidth</code>-bit field starting at slot <code>index</code> within <code>target</code> with the given value.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - The BitSet to modify in place.</dd>
<dd><code>value</code> - The value to store, masked to <code>bitWidth</code> bits.</dd>
<dd><code>bitWidth</code> - The number of bits used for this field.</dd>
<dd><code>index</code> - The slot whose bits should be updated.</dd>
</dl>
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
Overwrites the field starting at slot <code>index</code> within <code>target</code>, deriving its width from <code>bitMask</code>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - The BitSet to modify in place.</dd>
<dd><code>value</code> - The value to store.</dd>
<dd><code>bitMask</code> - A mask whose width defines how many bits of the field are used.</dd>
<dd><code>index</code> - The slot whose bits should be updated.</dd>
</dl>
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
Writes <code>value</code> into <code>target</code> starting at <code>bitOffset</code>, clearing the field first and setting only the bits selected by <code>bitMask</code>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - The BitSet to modify in place.</dd>
<dd><code>value</code> - The value to store.</dd>
<dd><code>bitMask</code> - A mask selecting which of the low bits carry data; its width determines how many bits are written.</dd>
<dd><code>bitOffset</code> - The position in the set at which the field begins.</dd>
</dl>
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
Reads the <code>bitWidth</code>-bit field starting at slot <code>index</code> from <code>target</code>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - The BitSet to read from.</dd>
<dd><code>bitWidth</code> - The number of bits used for this field.</dd>
<dd><code>index</code> - The slot whose value should be read.</dd>
<dt>Returns:</dt>
<dd>The value stored in the field, reconstructed from its constituent bits.</dd>
</dl>
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
Reads a value from <code>target</code> starting at <code>bitOffset</code>, reconstructing it from the bits selected by <code>bitMask</code>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - The BitSet to read from.</dd>
<dd><code>bitMask</code> - A mask selecting which low bits carry data; its width determines how many bits are read.</dd>
<dd><code>bitOffset</code> - The position in the set at which the field begins.</dd>
<dt>Returns:</dt>
<dd>The value formed by the selected bits, with the least-significant bit aligned to <code>bitOffset</code>.</dd>
</dl>
</div>
:::


</section>

:::::
  

