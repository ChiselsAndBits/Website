--- 
title: ChiselingOperation
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling](index.md)  
# Enum Class ChiselingOperation  
---
<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">ChiselingOperation</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>&lt;<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&gt;</span></div>  

  

Represents the mode of operandus of the current chiseling context.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 2 -->
::::::: info Nested Class Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">Enum.EnumDesc</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">E</a> extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">E</a>&gt;&gt;
:::::
:::::::
  
  
<!-- JavaMarkContainer Depth: 1 -->
::::: info Enum Constant Summary  
:::tabs
== Enum Constants
<table>
  <thead>
    <tr><th>Enum Constant</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#CHISELING" class="member-name-link">CHISELING</a></code></td><td><div class="block">The current operation is a chisel.</div><br></td></tr>
  <tr><td><code><a href="#PLACING" class="member-name-link">PLACING</a></code></td><td><div class="block">The current operation is a bit.</div><br></td></tr>
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
  <tr><td><code>boolean</code></td><td><code><a href="#isChiseling()" class="member-name-link">isChiseling</a>()</code></td><td><div class="block">Indicates if the current mode is a chiseling mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isPlacing()" class="member-name-link">isPlacing</a>()</code></td><td><div class="block">Indicates if the current mode is a placing mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#processesAir()" class="member-name-link">processesAir</a>()</code></td><td><div class="block">Indicates if this operation processes air.</div><br></td></tr>
  <tr><td><code>static <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isChiseling()" class="member-name-link">isChiseling</a>()</code></td><td><div class="block">Indicates if the current mode is a chiseling mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isPlacing()" class="member-name-link">isPlacing</a>()</code></td><td><div class="block">Indicates if the current mode is a placing mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#processesAir()" class="member-name-link">processesAir</a>()</code></td><td><div class="block">Indicates if this operation processes air.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isChiseling()" class="member-name-link">isChiseling</a>()</code></td><td><div class="block">Indicates if the current mode is a chiseling mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isPlacing()" class="member-name-link">isPlacing</a>()</code></td><td><div class="block">Indicates if the current mode is a placing mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#processesAir()" class="member-name-link">processesAir</a>()</code></td><td><div class="block">Indicates if this operation processes air.</div><br></td></tr>
  <tr><td><code>static <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang" class="external-link">compareTo</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang" class="external-link">describeConstable</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang" class="external-link">getDeclaringClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang" class="external-link">name</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang" class="external-link">ordinal</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang" class="external-link">valueOf</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Enum Constant Details  
<section id="CHISELING">

:::tabs
== CHISELING
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></span>&nbsp;<span class="element-name">CHISELING</span></div>
The current operation is a chisel.
 As such it removes the bit underneath the cursor.
<dl class="notes"></dl>
:::


</section>

<section id="PLACING">

:::tabs
== PLACING
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></span>&nbsp;<span class="element-name">PLACING</span></div>
The current operation is a bit.
 As such it places the bit underneath the cursor.
<dl class="notes"></dl>
:::


</section>

:::::
  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="values()">

:::tabs
== values
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>[]</span>&nbsp;<span class="element-name">values</span>()</div>
Returns an array containing the constants of this enum class, in
the order they are declared.
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
:::


</section>

<section id="valueOf(java.lang.String)">

:::tabs
== valueOf
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></span>&nbsp;<span class="element-name">valueOf</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</span></div>
Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang" class="external-link">NullPointerException</a></code> - if the argument is null</dd>
</dl>
:::


</section>

<section id="processesAir()">

:::tabs
== processesAir
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">processesAir</span>()</div>
Indicates if this operation processes air.
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if this operation processes air, <code>false</code> otherwise.</dd>
</dl>
:::


</section>

<section id="isChiseling()">

:::tabs
== isChiseling
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isChiseling</span>()</div>
Indicates if the current mode is a chiseling mode.
<dl class="notes">
<dt>Returns:</dt>
<dd>True when this is a chiseling mode, false otherwise.</dd>
</dl>
:::


</section>

<section id="isPlacing()">

:::tabs
== isPlacing
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isPlacing</span>()</div>
Indicates if the current mode is a placing mode.
<dl class="notes">
<dt>Returns:</dt>
<dd>True when this is a placing mode, false otherwise.</dd>
</dl>
:::


</section>

:::::
  

