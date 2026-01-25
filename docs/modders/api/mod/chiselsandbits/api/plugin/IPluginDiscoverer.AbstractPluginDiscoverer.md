--- 
title: AbstractPluginDiscoverer
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.plugin](index.md)  
# Class AbstractPluginDiscoverer  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.plugin.AbstractPluginDiscoverer  
  
**All Implemented Interfaces:**  
[IPluginDiscoverer](IPluginDiscoverer.md)  

**Enclosing Class:**  
[IPluginDiscoverer](IPluginDiscoverer.md)  

---
<div class="type-signature"><span class="modifiers">public abstract static class </span><span class="element-name type-name-label">IPluginDiscoverer.AbstractPluginDiscoverer</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><br/>  
implements <a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 2 -->
::::::: info Nested Class Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from interface&nbsp;mod.chiselsandbits.api.plugin.<a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a>
<a href="IPluginDiscoverer.AbstractPluginDiscoverer.html" title="class in mod.chiselsandbits.api.plugin">IPluginDiscoverer.AbstractPluginDiscoverer</a>
:::::
:::::::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E()" class="member-name-link">AbstractPluginDiscoverer</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected abstract boolean</code></td><td><code><a href="#isModNotLoaded(java.lang.String)" class="member-name-link">isModNotLoaded</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;modId)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&gt;</code></td><td><code><a href="#loadPlugins()" class="member-name-link">loadPlugins</a>()</code></td><td><div class="block">Loads the plugins.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected abstract boolean</code></td><td><code><a href="#isModNotLoaded(java.lang.String)" class="member-name-link">isModNotLoaded</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;modId)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&gt;</code></td><td><code><a href="#loadPlugins()" class="member-name-link">loadPlugins</a>()</code></td><td><div class="block">Loads the plugins.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected abstract boolean</code></td><td><code><a href="#isModNotLoaded(java.lang.String)" class="member-name-link">isModNotLoaded</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;modId)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&gt;</code></td><td><code><a href="#loadPlugins()" class="member-name-link">loadPlugins</a>()</code></td><td><div class="block">Loads the plugins.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>()">

:::tabs
== AbstractPluginDiscoverer
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">AbstractPluginDiscoverer</span>()</div>
<dl class="notes"></dl>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="loadPlugins()">

:::tabs
== loadPlugins
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;<a href="IChiselsAndBitsPlugin.html" title="interface in mod.chiselsandbits.api.plugin">IChiselsAndBitsPlugin</a>&gt;&gt;</span>&nbsp;<span class="element-name">loadPlugins</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="IPluginDiscoverer.html#loadPlugins()">IPluginDiscoverer</a></code></span></div>
Loads the plugins.
 Already has performed the instantiation logic and validation.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IPluginDiscoverer.html#loadPlugins()">loadPlugins</a></code>&nbsp;in interface&nbsp;<code><a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></code></dd>
<dt>Returns:</dt>
<dd>The loaded plugins.</dd>
</dl>
:::


</section>

<section id="isModNotLoaded(java.lang.String)">

:::tabs
== isModNotLoaded
<div class="member-signature"><span class="modifiers">protected abstract</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isModNotLoaded</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;modId)</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

