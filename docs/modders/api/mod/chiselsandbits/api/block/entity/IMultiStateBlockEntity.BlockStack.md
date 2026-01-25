--- 
title: BlockStack
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.entity](index.md)  
# Record Class BlockStack  
**Enclosing Class:**  
[IMultiStateBlockEntity](IMultiStateBlockEntity.md)  

---
<div class="type-signature"><span class="modifiers">public static record </span><span class="element-name type-name-label">IMultiStateBlockEntity.BlockStack</span>(net.minecraft.world.item.ItemStack&nbsp;stack, <a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack)<br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Summary  
:::tabs
== Constructors
<table>
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E(net.minecraft.world.item.ItemStack,mod.chiselsandbits.api.item.multistate.IMultiStateItemStack)" class="member-name-link">BlockStack</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> <a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack)</code></td><td><div class="block">Creates an instance of a <code>BlockStack</code> record class.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateBlockEntity.BlockStack.html" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></code></td><td><code><a href="#copy()" class="member-name-link">copy</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code><a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#multiStateItemStack()" class="member-name-link">multiStateItemStack</a>()</code></td><td><div class="block">Returns the value of the <code>multiStateItemStack</code> record component.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#stack()" class="member-name-link">stack</a>()</code></td><td><div class="block">Returns the value of the <code>stack</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateBlockEntity.BlockStack.html" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></code></td><td><code><a href="#copy()" class="member-name-link">copy</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code><a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#multiStateItemStack()" class="member-name-link">multiStateItemStack</a>()</code></td><td><div class="block">Returns the value of the <code>multiStateItemStack</code> record component.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#stack()" class="member-name-link">stack</a>()</code></td><td><div class="block">Returns the value of the <code>stack</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateBlockEntity.BlockStack.html" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></code></td><td><code><a href="#copy()" class="member-name-link">copy</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>final boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</code></td><td><div class="block">Indicates whether some other object is "equal to" this one.</div><br></td></tr>
  <tr><td><code>final int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash code value for this object.</div><br></td></tr>
  <tr><td><code><a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#multiStateItemStack()" class="member-name-link">multiStateItemStack</a>()</code></td><td><div class="block">Returns the value of the <code>multiStateItemStack</code> record component.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#stack()" class="member-name-link">stack</a>()</code></td><td><div class="block">Returns the value of the <code>stack</code> record component.</div><br></td></tr>
  <tr><td><code>final <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string representation of this record class.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(net.minecraft.world.item.ItemStack,mod.chiselsandbits.api.item.multistate.IMultiStateItemStack)">

:::tabs
== BlockStack
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">BlockStack</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack,
 <a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack)</span></div>
Creates an instance of a <code>BlockStack</code> record class.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - the value for the <code>stack</code> record component</dd>
<dd><code>multiStateItemStack</code> - the value for the <code>multiStateItemStack</code> record component</dd>
</dl>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="copy()">

:::tabs
== copy
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="IMultiStateBlockEntity.BlockStack.html" title="class in mod.chiselsandbits.api.block.entity">IMultiStateBlockEntity.BlockStack</a></span>&nbsp;<span class="element-name">copy</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="toString()">

:::tabs
== toString
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">toString</span>()</div>
Returns a string representation of this record class. The representation contains the name of the class, followed by the name and value of each of the record components.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html#toString()" title="class or interface in java.lang" class="external-link">toString</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of this object</dd>
</dl>
:::


</section>

<section id="hashCode()">

:::tabs
== hashCode
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">hashCode</span>()</div>
Returns a hash code value for this object. The value is derived from the hash code of each of the record components.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Returns:</dt>
<dd>a hash code value for this object</dd>
</dl>
:::


</section>

<section id="equals(java.lang.Object)">

:::tabs
== equals
<div class="member-signature"><span class="modifiers">public final</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">equals</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;o)</span></div>
Indicates whether some other object is "equal to" this one. The objects are equal if the other object is of the same class and if all the record components are equal. All components in this record class are compared with <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Objects.html#equals(java.lang.Object,java.lang.Object)" title="class or interface in java.util" class="external-link"><code>Objects::equals(Object,Object)</code></a>.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Record.html" title="class or interface in java.lang" class="external-link">Record</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - the object with which to compare</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this object is the same as the <code>o</code> argument; <code>false</code> otherwise.</dd>
</dl>
:::


</section>

<section id="stack()">

:::tabs
== stack
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">stack</span>()</div>
Returns the value of the <code>stack</code> record component.
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>stack</code> record component</dd>
</dl>
:::


</section>

<section id="multiStateItemStack()">

:::tabs
== multiStateItemStack
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></span>&nbsp;<span class="element-name">multiStateItemStack</span>()</div>
Returns the value of the <code>multiStateItemStack</code> record component.
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the <code>multiStateItemStack</code> record component</dd>
</dl>
:::


</section>

:::::
  

