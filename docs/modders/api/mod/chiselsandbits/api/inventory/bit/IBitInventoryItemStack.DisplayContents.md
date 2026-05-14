--- 
title: DisplayContents
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.inventory.bit](index.md)  
# Record Class DisplayContents  
**Enclosing Class:**  
[IBitInventoryItemStack](IBitInventoryItemStack.md)  

---
<div class="type-signature"><span class="modifiers">public static record </span><span class="element-name type-name-label">IBitInventoryItemStack.DisplayContents</span>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;displayComponents, boolean&nbsp;isEmpty, boolean&nbsp;clipped)<br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></span></div>  

  

  

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
  <tr><td><code><a href="#%3Cinit%3E(java.util.List,boolean,boolean)" class="member-name-link">DisplayContents</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;displayComponents,<br> boolean&nbsp;isEmpty,<br> boolean&nbsp;clipped)</code></td><td><div class="block">Creates an instance of a <code>DisplayContents</code> record class.</div><br></td></tr>
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
  <tr><td><code>boolean</code></td><td><code><a href="#clipped()" class="member-name-link">clipped</a>()</code></td><td><div class="block">Returns the value of the <code>clipped</code> record component.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;net.minecraft.network.chat.Component&gt;</code></td><td><code><a href="#displayComponents()" class="member-name-link">displayComponents</a>()</code></td><td><div class="block">Returns the value of the <code>displayComponents</code> record component.</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Returns the value of the <code>isEmpty</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#clipped()" class="member-name-link">clipped</a>()</code></td><td><div class="block">Returns the value of the <code>clipped</code> record component.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;net.minecraft.network.chat.Component&gt;</code></td><td><code><a href="#displayComponents()" class="member-name-link">displayComponents</a>()</code></td><td><div class="block">Returns the value of the <code>displayComponents</code> record component.</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Returns the value of the <code>isEmpty</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#clipped()" class="member-name-link">clipped</a>()</code></td><td><div class="block">Returns the value of the <code>clipped</code> record component.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;net.minecraft.network.chat.Component&gt;</code></td><td><code><a href="#displayComponents()" class="member-name-link">displayComponents</a>()</code></td><td><div class="block">Returns the value of the <code>displayComponents</code> record component.</div><br></td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Returns the value of the <code>isEmpty</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(java.util.List,boolean,boolean)">

:::tabs
== DisplayContents
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">DisplayContents</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;displayComponents,
 boolean&nbsp;isEmpty,
 boolean&nbsp;clipped)</span></div>
Creates an instance of a <code>DisplayContents</code> record class.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayComponents</code> - the value for the <code>displayComponents</code> record component</dd>
<dd><code>isEmpty</code> - the value for the <code>isEmpty</code> record component</dd>
<dd><code>clipped</code> - the value for the <code>clipped</code> record component</dd>
</dl>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
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
Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. Reference components are compared with <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Objects.html#equals(java.lang.Object,java.lang.Object)" title="class or interface in java.util" class="external-link"><code>Objects::equals(Object,Object)</code></a>; primitive components are compared with the <code>compare</code> method from their corresponding wrapper classes.
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

<section id="displayComponents()">

:::tabs
== displayComponents
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;</span>&nbsp;<span class="element-name">displayComponents</span>()</div>
Returns the value of the <code>displayComponents</code> record component.
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>displayComponents</code> record component</dd>
</dl>
</div>
:::


</section>

<section id="isEmpty()">

:::tabs
== isEmpty
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isEmpty</span>()</div>
Returns the value of the <code>isEmpty</code> record component.
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>isEmpty</code> record component</dd>
</dl>
</div>
:::


</section>

<section id="clipped()">

:::tabs
== clipped
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">clipped</span>()</div>
Returns the value of the <code>clipped</code> record component.
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>clipped</code> record component</dd>
</dl>
</div>
:::


</section>

:::::
  

