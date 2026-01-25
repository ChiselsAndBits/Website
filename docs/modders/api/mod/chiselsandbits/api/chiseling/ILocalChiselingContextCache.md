--- 
title: ILocalChiselingContextCache
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling](index.md)  
# Interface ILocalChiselingContextCache  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ILocalChiselingContextCache</span></div>  

  

<div class="block">This small cache is used on the client side, primarily, to store a single active context
 which is valid across multiple frames.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear(mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">clear</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation)</code></td><td><div class="block">Clears the current context.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">get</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation)</code></td><td><div class="block">The current active context for the last few frames.</div><br></td></tr>
  <tr><td><code>static <a href="ILocalChiselingContextCache.html" title="interface in mod.chiselsandbits.api.chiseling">ILocalChiselingContextCache</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the instance.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#set(mod.chiselsandbits.api.chiseling.ChiselingOperation,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">set</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation,<br> <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Sets the current context in the cache.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="ILocalChiselingContextCache.html" title="interface in mod.chiselsandbits.api.chiseling">ILocalChiselingContextCache</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the instance.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear(mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">clear</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation)</code></td><td><div class="block">Clears the current context.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">get</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation)</code></td><td><div class="block">The current active context for the last few frames.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#set(mod.chiselsandbits.api.chiseling.ChiselingOperation,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">set</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation,<br> <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Sets the current context in the cache.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear(mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">clear</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation)</code></td><td><div class="block">Clears the current context.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">get</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation)</code></td><td><div class="block">The current active context for the last few frames.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#set(mod.chiselsandbits.api.chiseling.ChiselingOperation,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">set</a><wbr>(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation,<br> <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Sets the current context in the cache.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="ILocalChiselingContextCache.html" title="interface in mod.chiselsandbits.api.chiseling">ILocalChiselingContextCache</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">Gives access to the instance.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The instance.</dd>
</dl>
:::


</section>

<section id="get(mod.chiselsandbits.api.chiseling.ChiselingOperation)">

:::tabs
== get
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation)</span></div>
<div class="block">The current active context for the last few frames.
 The caller needs to validate that the returned value is still valid for his usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - The operation to get the context for from the cache.</dd>
<dt>Returns:</dt>
<dd>An optional with the last current active instance.</dd>
</dl>
:::


</section>

<section id="set(mod.chiselsandbits.api.chiseling.ChiselingOperation,mod.chiselsandbits.api.chiseling.IChiselingContext)">

:::tabs
== set
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">set</span><wbr><span class="parameters">(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation,
 <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</span></div>
<div class="block">Sets the current context in the cache.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - The operation to get the context for from the cache.</dd>
<dd><code>context</code> - The new cached context.</dd>
</dl>
:::


</section>

<section id="clear(mod.chiselsandbits.api.chiseling.ChiselingOperation)">

:::tabs
== clear
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clear</span><wbr><span class="parameters">(<a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;operation)</span></div>
<div class="block">Clears the current context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - The operation to get the context for from the cache.</dd>
</dl>
:::


</section>

:::::
  

