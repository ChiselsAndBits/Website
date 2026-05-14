--- 
title: IProfiler
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.profiling](index.md)  
# Interface IProfiler  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IProfiler</span></div>  

  

A profiler used to track the time certain operations inside Chisels and Bits take.  

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
  <tr><td><code>void</code></td><td><code><a href="#endSection()" class="member-name-link">endSection</a>()</code></td><td><div class="block">Ends the current section.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#endStartSection(java.lang.String)" class="member-name-link">endStartSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">End the current section and start a new section with the given name.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#endStartSection(java.util.function.Supplier)" class="member-name-link">endStartSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameSupplier)</code></td><td><div class="block">End the current section and start a new section with the name supplied by the given supplier.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#startSection(java.lang.String)" class="member-name-link">startSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Start a section with the given name.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#startSection(java.util.function.Supplier)" class="member-name-link">startSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameSupplier)</code></td><td><div class="block">Start section with the name provided by the given supplier.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#endSection()" class="member-name-link">endSection</a>()</code></td><td><div class="block">Ends the current section.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#endStartSection(java.lang.String)" class="member-name-link">endStartSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">End the current section and start a new section with the given name.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#endStartSection(java.util.function.Supplier)" class="member-name-link">endStartSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameSupplier)</code></td><td><div class="block">End the current section and start a new section with the name supplied by the given supplier.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#startSection(java.lang.String)" class="member-name-link">startSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Start a section with the given name.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#startSection(java.util.function.Supplier)" class="member-name-link">startSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameSupplier)</code></td><td><div class="block">Start section with the name provided by the given supplier.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#endSection()" class="member-name-link">endSection</a>()</code></td><td><div class="block">Ends the current section.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#startSection(java.lang.String)" class="member-name-link">startSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Start a section with the given name.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#startSection(java.util.function.Supplier)" class="member-name-link">startSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameSupplier)</code></td><td><div class="block">Start section with the name provided by the given supplier.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#endStartSection(java.lang.String)" class="member-name-link">endStartSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">End the current section and start a new section with the given name.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#endStartSection(java.util.function.Supplier)" class="member-name-link">endStartSection</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameSupplier)</code></td><td><div class="block">End the current section and start a new section with the name supplied by the given supplier.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="startSection(java.lang.String)">
:::tabs
== startSection
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">startSection</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</span></div>
Start a section with the given name.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name to start the section with.</dd>
</dl>
</div>
:::
</section>
<section id="startSection(java.util.function.Supplier)">
:::tabs
== startSection
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">startSection</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameSupplier)</span></div>
Start section with the name provided by the given supplier.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>nameSupplier</code> - the supplier for the name of the new section.</dd>
</dl>
</div>
:::
</section>
<section id="endSection()">
:::tabs
== endSection
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">endSection</span>()</div>
Ends the current section.</div>
:::
</section>
<section id="endStartSection(java.lang.String)">
:::tabs
== endStartSection
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">endStartSection</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</span></div>
End the current section and start a new section with the given name.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name to start the new section with.</dd>
</dl>
</div>
:::
</section>
<section id="endStartSection(java.util.function.Supplier)">
:::tabs
== endStartSection
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">endStartSection</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;nameSupplier)</span></div>
End the current section and start a new section with the name supplied by the given supplier.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>nameSupplier</code> - the supplier for the name to start the new section with.</dd>
</dl>
</div>
:::
</section>
:::::
  

