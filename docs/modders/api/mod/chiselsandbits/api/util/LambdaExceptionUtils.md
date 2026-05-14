--- 
title: LambdaExceptionUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class LambdaExceptionUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.LambdaExceptionUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">LambdaExceptionUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static interface&nbsp;</code></td><td><code><a href="LambdaExceptionUtils.Consumer_WithExceptions.html" class="type-name-link" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.Consumer_WithExceptions</a>&lt;<a href="LambdaExceptionUtils.Consumer_WithExceptions.html#type-param-T" title="type parameter in LambdaExceptionUtils.Consumer_WithExceptions">T</a>, <a href="LambdaExceptionUtils.Consumer_WithExceptions.html#type-param-E" title="type parameter in LambdaExceptionUtils.Consumer_WithExceptions">E</a> extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static interface&nbsp;</code></td><td><code><a href="LambdaExceptionUtils.ToIntFunction_WithExceptions.html" class="type-name-link" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.ToIntFunction_WithExceptions</a>&lt;<a href="LambdaExceptionUtils.ToIntFunction_WithExceptions.html#type-param-T" title="type parameter in LambdaExceptionUtils.ToIntFunction_WithExceptions">T</a>, <a href="LambdaExceptionUtils.ToIntFunction_WithExceptions.html#type-param-E" title="type parameter in LambdaExceptionUtils.ToIntFunction_WithExceptions">E</a> extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E()" class="member-name-link">LambdaExceptionUtils</a>()</code></td><td>&nbsp;</td></tr>
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
  <tr><td><code>static &lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a><wbr>&lt;T&gt;</code></td><td><code><a href="#rethrowConsumer(mod.chiselsandbits.api.util.LambdaExceptionUtils.Consumer_WithExceptions)" class="member-name-link">rethrowConsumer</a><wbr>(<a href="LambdaExceptionUtils.Consumer_WithExceptions.html" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.Consumer_WithExceptions</a>&lt;T,<wbr>E&gt;&nbsp;consumer)</code></td><td><div class="block">.forEach(rethrowConsumer(name -&gt; System.out.println(Class.forName(name)))); or .forEach(rethrowConsumer(ClassNameUtil::println));</div><br></td></tr>
  <tr><td><code>static &lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/ToIntFunction.html" title="class or interface in java.util.function" class="external-link">ToIntFunction</a><wbr>&lt;T&gt;</code></td><td><code><a href="#rethrowToIntFunction(mod.chiselsandbits.api.util.LambdaExceptionUtils.ToIntFunction_WithExceptions)" class="member-name-link">rethrowToIntFunction</a><wbr>(<a href="LambdaExceptionUtils.ToIntFunction_WithExceptions.html" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.ToIntFunction_WithExceptions</a>&lt;T,<wbr>E&gt;&nbsp;consumer)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a><wbr>&lt;T&gt;</code></td><td><code><a href="#rethrowConsumer(mod.chiselsandbits.api.util.LambdaExceptionUtils.Consumer_WithExceptions)" class="member-name-link">rethrowConsumer</a><wbr>(<a href="LambdaExceptionUtils.Consumer_WithExceptions.html" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.Consumer_WithExceptions</a>&lt;T,<wbr>E&gt;&nbsp;consumer)</code></td><td><div class="block">.forEach(rethrowConsumer(name -&gt; System.out.println(Class.forName(name)))); or .forEach(rethrowConsumer(ClassNameUtil::println));</div><br></td></tr>
  <tr><td><code>static &lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/ToIntFunction.html" title="class or interface in java.util.function" class="external-link">ToIntFunction</a><wbr>&lt;T&gt;</code></td><td><code><a href="#rethrowToIntFunction(mod.chiselsandbits.api.util.LambdaExceptionUtils.ToIntFunction_WithExceptions)" class="member-name-link">rethrowToIntFunction</a><wbr>(<a href="LambdaExceptionUtils.ToIntFunction_WithExceptions.html" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.ToIntFunction_WithExceptions</a>&lt;T,<wbr>E&gt;&nbsp;consumer)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a><wbr>&lt;T&gt;</code></td><td><code><a href="#rethrowConsumer(mod.chiselsandbits.api.util.LambdaExceptionUtils.Consumer_WithExceptions)" class="member-name-link">rethrowConsumer</a><wbr>(<a href="LambdaExceptionUtils.Consumer_WithExceptions.html" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.Consumer_WithExceptions</a>&lt;T,<wbr>E&gt;&nbsp;consumer)</code></td><td><div class="block">.forEach(rethrowConsumer(name -&gt; System.out.println(Class.forName(name)))); or .forEach(rethrowConsumer(ClassNameUtil::println));</div><br></td></tr>
  <tr><td><code>static &lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/ToIntFunction.html" title="class or interface in java.util.function" class="external-link">ToIntFunction</a><wbr>&lt;T&gt;</code></td><td><code><a href="#rethrowToIntFunction(mod.chiselsandbits.api.util.LambdaExceptionUtils.ToIntFunction_WithExceptions)" class="member-name-link">rethrowToIntFunction</a><wbr>(<a href="LambdaExceptionUtils.ToIntFunction_WithExceptions.html" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.ToIntFunction_WithExceptions</a>&lt;T,<wbr>E&gt;&nbsp;consumer)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>()">

:::tabs
== LambdaExceptionUtils
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">LambdaExceptionUtils</span>()</div>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="rethrowConsumer(mod.chiselsandbits.api.util.LambdaExceptionUtils.Consumer_WithExceptions)">
:::tabs
== rethrowConsumer
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="type-parameters">&lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;T&gt;</span>&nbsp;<span class="element-name">rethrowConsumer</span><wbr><span class="parameters">(<a href="LambdaExceptionUtils.Consumer_WithExceptions.html" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.Consumer_WithExceptions</a>&lt;T,<wbr>E&gt;&nbsp;consumer)</span></div>
.forEach(rethrowConsumer(name -&gt; System.out.println(Class.forName(name)))); or .forEach(rethrowConsumer(ClassNameUtil::println));</div>
:::
</section>
<section id="rethrowToIntFunction(mod.chiselsandbits.api.util.LambdaExceptionUtils.ToIntFunction_WithExceptions)">
:::tabs
== rethrowToIntFunction
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="type-parameters">&lt;T, E extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang" class="external-link">Exception</a>&gt;</span>
<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/ToIntFunction.html" title="class or interface in java.util.function" class="external-link">ToIntFunction</a>&lt;T&gt;</span>&nbsp;<span class="element-name">rethrowToIntFunction</span><wbr><span class="parameters">(<a href="LambdaExceptionUtils.ToIntFunction_WithExceptions.html" title="interface in mod.chiselsandbits.api.util">LambdaExceptionUtils.ToIntFunction_WithExceptions</a>&lt;T,<wbr>E&gt;&nbsp;consumer)</span></div>
</div>
:::
</section>
:::::
  

