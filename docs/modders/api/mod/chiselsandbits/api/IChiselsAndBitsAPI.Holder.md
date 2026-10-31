--- 
title: Holder
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api](index)  
# Class Holder  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.Holder  
  
**Enclosing Class:**  
[IChiselsAndBitsAPI](IChiselsAndBitsAPI)  

---
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">IChiselsAndBitsAPI.Holder</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Holds the API instance installed by the platform bootstrap.  

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
  <tr><td><code><a href="#%3Cinit%3E()" class="member-name-link">Holder</a>()</code></td><td><div class="block">Creates the holder; the API instance is shared statically.</div><br></td></tr>
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
  <tr><td><code>static <a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Returns the API instance installed during bootstrap.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setInstance(mod.chiselsandbits.api.IChiselsAndBitsAPI)" class="member-name-link">setInstance</a><wbr>(<a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a>&nbsp;instance)</code></td><td><div class="block">Installs the API instance once during platform initialization.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Returns the API instance installed during bootstrap.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setInstance(mod.chiselsandbits.api.IChiselsAndBitsAPI)" class="member-name-link">setInstance</a><wbr>(<a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a>&nbsp;instance)</code></td><td><div class="block">Installs the API instance once during platform initialization.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Returns the API instance installed during bootstrap.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#setInstance(mod.chiselsandbits.api.IChiselsAndBitsAPI)" class="member-name-link">setInstance</a><wbr>(<a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a>&nbsp;instance)</code></td><td><div class="block">Installs the API instance once during platform initialization.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>()">

:::tabs
== Holder
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">Holder</span>()</div>
Creates the holder; the API instance is shared statically.
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
Returns the API instance installed during bootstrap.
<dl class="notes">
<dt>Returns:</dt>
<dd>the requested value.</dd>
</dl>
</div>
:::


</section>

<section id="setInstance(mod.chiselsandbits.api.IChiselsAndBitsAPI)">

:::tabs
== setInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setInstance</span><wbr><span class="parameters">(<a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a>&nbsp;instance)</span></div>
Installs the API instance once during platform initialization.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instance</code> - API implementation to install</dd>
</dl>
</div>
:::


</section>

:::::
  

