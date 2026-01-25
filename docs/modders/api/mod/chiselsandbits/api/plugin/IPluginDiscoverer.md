--- 
title: IPluginDiscoverer
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.plugin](index.md)  
# Interface IPluginDiscoverer  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPluginDiscoverer</span></div>  

  

<div class="block">The platform plugin manager which can load the plugins for C&amp;B on a given platform.</div>
  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Interface</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static class&nbsp;</code></td><td><code><a href="IPluginDiscoverer.AbstractPluginDiscoverer.html" class="type-name-link" title="class in mod.chiselsandbits.api.plugin">IPluginDiscoverer.AbstractPluginDiscoverer</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
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
  <tr><td><code>static <a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the platform's plugin manager.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&gt;</code></td><td><code><a href="#loadPlugins()" class="member-name-link">loadPlugins</a>()</code></td><td><div class="block">Loads the plugins.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the platform's plugin manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&gt;</code></td><td><code><a href="#loadPlugins()" class="member-name-link">loadPlugins</a>()</code></td><td><div class="block">Loads the plugins.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&gt;</code></td><td><code><a href="#loadPlugins()" class="member-name-link">loadPlugins</a>()</code></td><td><div class="block">Loads the plugins.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">Gives access to the platform's plugin manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The platform's plugin manager.</dd>
</dl>
:::


</section>

<section id="loadPlugins()">

:::tabs
== loadPlugins
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&gt;</span>&nbsp;<span class="element-name">loadPlugins</span>()</div>
<div class="block">Loads the plugins.
 Already has performed the instantiation logic and validation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The loaded plugins.</dd>
</dl>
:::


</section>

:::::
  

