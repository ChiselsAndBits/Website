--- 
title: ToIntFunction_WithExceptions
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Interface ToIntFunction_WithExceptions\<T,E extends Exception\>  
**Type Parameters:**  
T - type of input value  
E - checked exception type that may be thrown  

**Enclosing Class:**  
[LambdaExceptionUtils](LambdaExceptionUtils)  

**Functional Interface:**  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang" class="external-link">@FunctionalInterface</a><br/>  
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">LambdaExceptionUtils.ToIntFunction_WithExceptions&lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;</span></div>  

  

Integer-returning function whose operation may throw a checked exception.  

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
  <tr><td><code>int</code></td><td><code><a href="#applyAsInt(T)" class="member-name-link">applyAsInt</a><wbr>(<a href="#type-param-T" title="type parameter in LambdaExceptionUtils.ToIntFunction_WithExceptions">T</a>&nbsp;t)</code></td><td><div class="block">Applies the function and may throw the declared exception.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#applyAsInt(T)" class="member-name-link">applyAsInt</a><wbr>(<a href="#type-param-T" title="type parameter in LambdaExceptionUtils.ToIntFunction_WithExceptions">T</a>&nbsp;t)</code></td><td><div class="block">Applies the function and may throw the declared exception.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#applyAsInt(T)" class="member-name-link">applyAsInt</a><wbr>(<a href="#type-param-T" title="type parameter in LambdaExceptionUtils.ToIntFunction_WithExceptions">T</a>&nbsp;t)</code></td><td><div class="block">Applies the function and may throw the declared exception.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="applyAsInt(T)">

:::tabs
== applyAsInt
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">int</span>&nbsp;<span class="element-name">applyAsInt</span><wbr><span class="parameters">(<a href="#type-param-T" title="type parameter in LambdaExceptionUtils.ToIntFunction_WithExceptions">T</a>&nbsp;t)</span>
        throws <span class="exceptions">E</span></div>
Applies the function and may throw the declared exception.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>t</code> - input value</dd>
<dt>Returns:</dt>
<dd>the computed integer</dd>
<dt>Throws:</dt>
<dd><code>E</code> - if the operation fails</dd>
</dl>
</div>
:::


</section>

:::::
  

