--- 
title: SizeInformation
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.storage](index.md)  
# Record Class SizeInformation  
**Enclosing Class:**  
[StateEntryPalette](StateEntryPalette.md)  

---
<div class="type-signature"><span class="modifiers">public static record </span><span class="element-name type-name-label">StateEntryPalette.SizeInformation</span>(boolean&nbsp;hasChanged, int&nbsp;size)<br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></span></div>  

  

Represents the size information of the palette.
<p>
    The size is only accurate if it has changed.
</p>  

<dl class="notes"></dl>  

<!-- ======== CONSTRUCTOR SUMMARY ======== -->
Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E(boolean,int)" class="member-name-link">SizeInformation</a><wbr>(boolean&nbsp;hasChanged,<br> int&nbsp;size)</code></td><td><div class="block">Creates an instance of a <code>SizeInformation</code> record class.</div><br></td></tr>
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
  <tr><td><code>static <a href="StateEntryPalette.SizeInformation.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></code></td><td><code><a href="#changed(int)" class="member-name-link">changed</a><wbr>(int&nbsp;size)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#hasChanged()" class="member-name-link">hasChanged</a>()</code></td><td><div class="block">Returns the value of the <a href="#param-hasChanged"><code>hasChanged</code></a> record component.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>static <a href="StateEntryPalette.SizeInformation.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></code></td><td><code><a href="#notChanged()" class="member-name-link">notChanged</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#size()" class="member-name-link">size</a>()</code></td><td><div class="block">Returns the value of the <a href="#param-size"><code>size</code></a> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="StateEntryPalette.SizeInformation.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></code></td><td><code><a href="#changed(int)" class="member-name-link">changed</a><wbr>(int&nbsp;size)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="StateEntryPalette.SizeInformation.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></code></td><td><code><a href="#notChanged()" class="member-name-link">notChanged</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#hasChanged()" class="member-name-link">hasChanged</a>()</code></td><td><div class="block">Returns the value of the <a href="#param-hasChanged"><code>hasChanged</code></a> record component.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#size()" class="member-name-link">size</a>()</code></td><td><div class="block">Returns the value of the <a href="#param-size"><code>size</code></a> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="StateEntryPalette.SizeInformation.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></code></td><td><code><a href="#changed(int)" class="member-name-link">changed</a><wbr>(int&nbsp;size)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#hasChanged()" class="member-name-link">hasChanged</a>()</code></td><td><div class="block">Returns the value of the <a href="#param-hasChanged"><code>hasChanged</code></a> record component.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>static <a href="StateEntryPalette.SizeInformation.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></code></td><td><code><a href="#notChanged()" class="member-name-link">notChanged</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#size()" class="member-name-link">size</a>()</code></td><td><div class="block">Returns the value of the <a href="#param-size"><code>size</code></a> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(boolean,int)">

:::tabs
== SizeInformation
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">SizeInformation</span><wbr><span class="parameters">(boolean&nbsp;hasChanged,
 int&nbsp;size)</span></div>
<div class="block">Creates an instance of a <code>SizeInformation</code> record class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hasChanged</code> - the value for the <a href="#param-hasChanged"><code>hasChanged</code></a> record component</dd>
<dd><code>size</code> - the value for the <a href="#param-size"><code>size</code></a> record component</dd>
</dl>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="notChanged()">

:::tabs
== notChanged
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="StateEntryPalette.SizeInformation.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></span>&nbsp;<span class="element-name">notChanged</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="changed(int)">

:::tabs
== changed
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="StateEntryPalette.SizeInformation.html" title="class in mod.chiselsandbits.api.block.storage">StateEntryPalette.SizeInformation</a></span>&nbsp;<span class="element-name">changed</span><wbr><span class="parameters">(int&nbsp;size)</span></div>
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
<div class="block">Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. All components in this record class are compared with the <code>compare</code> method from their corresponding wrapper classes.</div>
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
<section id="hasChanged()">

:::tabs
== hasChanged
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">hasChanged</span>()</div>
<div class="block">Returns the value of the <a href="#param-hasChanged"><code>hasChanged</code></a> record component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <a href="#param-hasChanged"><code>hasChanged</code></a> record component</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="size()">

:::tabs
== size
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">size</span>()</div>
<div class="block">Returns the value of the <a href="#param-size"><code>size</code></a> record component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <a href="#param-size"><code>size</code></a> record component</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

