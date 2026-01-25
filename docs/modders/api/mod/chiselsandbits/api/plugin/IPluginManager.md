--- 
title: IPluginManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.plugin](index.md)  
# Interface IPluginManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPluginManager</span></div>  

  

<div class="block">The manager for plugins.</div>
  

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
  <tr><td><code>static <a href="IPluginManager.html" title="interface in mod.chiselsandbits.api.plugin">IPluginManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The instance of the plugin manager.</div><br></td></tr>
  <tr><td><code>com.google.common.collect.ImmutableSet<wbr>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;</code></td><td><code><a href="#getPlugins()" class="member-name-link">getPlugins</a>()</code></td><td><div class="block">Gets the plugins.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#run(java.util.function.Consumer)" class="member-name-link">run</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&nbsp;callback)</code></td><td><div class="block">Runs a specific task on all available plugins.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IPluginManager.html" title="interface in mod.chiselsandbits.api.plugin">IPluginManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The instance of the plugin manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.google.common.collect.ImmutableSet<wbr>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;</code></td><td><code><a href="#getPlugins()" class="member-name-link">getPlugins</a>()</code></td><td><div class="block">Gets the plugins.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#run(java.util.function.Consumer)" class="member-name-link">run</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&nbsp;callback)</code></td><td><div class="block">Runs a specific task on all available plugins.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>com.google.common.collect.ImmutableSet<wbr>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;</code></td><td><code><a href="#getPlugins()" class="member-name-link">getPlugins</a>()</code></td><td><div class="block">Gets the plugins.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#run(java.util.function.Consumer)" class="member-name-link">run</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&nbsp;callback)</code></td><td><div class="block">Runs a specific task on all available plugins.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPluginManager.html" title="interface in mod.chiselsandbits.api.plugin">IPluginManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">The instance of the plugin manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The plugin manager.</dd>
</dl>
:::


</section>

<section id="getPlugins()">

:::tabs
== getPlugins
<div class="member-signature"><span class="return-type">com.google.common.collect.ImmutableSet&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;</span>&nbsp;<span class="element-name">getPlugins</span>()</div>
<div class="block">Gets the plugins.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>An immutable set with the plugins.</dd>
</dl>
:::


</section>

<section id="run(java.util.function.Consumer)">

:::tabs
== run
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">run</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&nbsp;callback)</span></div>
<div class="block">Runs a specific task on all available plugins.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - The task to run for each plugin.</dd>
</dl>
:::


</section>

:::::
  

