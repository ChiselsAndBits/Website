--- 
title: ClassUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class ClassUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.ClassUtils  
  
---
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ClassUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for processing classes.  

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
  <tr><td><code>static &lt;T&gt;&nbsp;T</code></td><td><code><a href="#createOrGetInstance(java.lang.String,java.lang.Class,java.lang.Class,java.util.function.Function)" class="member-name-link">createOrGetInstance</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;className,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;T&gt;&nbsp;baseClass,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Annotation.html" title="class or interface in java.lang.annotation" class="external-link">Annotation</a>&gt;&nbsp;instanceAnnotation,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameFunction)</code></td><td><div class="block">Gets or creates a new instance of the class with the given name.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T&gt;&nbsp;T</code></td><td><code><a href="#createOrGetInstance(java.lang.String,java.lang.Class,java.lang.Class,java.util.function.Function)" class="member-name-link">createOrGetInstance</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;className,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;T&gt;&nbsp;baseClass,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Annotation.html" title="class or interface in java.lang.annotation" class="external-link">Annotation</a>&gt;&nbsp;instanceAnnotation,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameFunction)</code></td><td><div class="block">Gets or creates a new instance of the class with the given name.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T&gt;&nbsp;T</code></td><td><code><a href="#createOrGetInstance(java.lang.String,java.lang.Class,java.lang.Class,java.util.function.Function)" class="member-name-link">createOrGetInstance</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;className,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;T&gt;&nbsp;baseClass,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Annotation.html" title="class or interface in java.lang.annotation" class="external-link">Annotation</a>&gt;&nbsp;instanceAnnotation,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameFunction)</code></td><td><div class="block">Gets or creates a new instance of the class with the given name.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="createOrGetInstance(java.lang.String,java.lang.Class,java.lang.Class,java.util.function.Function)">

:::tabs
== createOrGetInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span>&nbsp;<span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">T</span>&nbsp;<span class="element-name">createOrGetInstance</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;className,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;T&gt;&nbsp;baseClass,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Annotation.html" title="class or interface in java.lang.annotation" class="external-link">Annotation</a>&gt;&nbsp;instanceAnnotation,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameFunction)</span></div>
Gets or creates a new instance of the class with the given name.
Verifies that the class is of a given base type, and checks if a field in this class potentially has the instance annotation.
If that annotation is present then the contents of that field are returned and verified for the requested type instance.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="createOrGetInstance(java.lang.String,java.lang.Class,java.lang.Class,java.util.function.Function)-type-param-T"><code>T</code> - The type of the base class.</span></dd>
<dt>Parameters:</dt>
<dd><code>className</code> - The name of the class to construct and load.</dd>
<dd><code>baseClass</code> - The base class to verify the class is of.</dd>
<dd><code>instanceAnnotation</code> - The annotation used to find a manually constructed instance.</dd>
<dd><code>nameFunction</code> - The function used to determine the name of the class, used for logging.</dd>
<dt>Returns:</dt>
<dd>An instance of the class, or null if the class is not of the given base type or construction fails.</dd>
</dl>
</div>
:::


</section>

:::::
  

