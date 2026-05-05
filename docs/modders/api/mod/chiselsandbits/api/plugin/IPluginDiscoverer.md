--- 
title: IPluginDiscoverer
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.plugin](index.md)  
# Interface IPluginDiscoverer  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPluginDiscoverer</span></div>  

  

The platform plugin manager which can load the plugins for C&amp;B on a given platform.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the platform's plugin manager.</div><br></td></tr>
  <tr><td><code>&lt;A, I extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Annotation.html" title="class or interface in java.lang.annotation" class="external-link">Annotation</a>, T&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;T&gt;&gt;</code></td><td><code><a href="#loadPlugins(java.lang.Class,java.lang.Class,java.lang.Class,java.util.function.Function)" class="member-name-link">loadPlugins</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;A&gt;&nbsp;annotationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;I&gt;&nbsp;instanceAnnotationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;T&gt;&nbsp;pluginSpecificationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;idExtractor)</code></td><td><div class="block">Loads the plugins of a given type, potentially marked with a given annotation type.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the platform's plugin manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>&lt;A, I extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Annotation.html" title="class or interface in java.lang.annotation" class="external-link">Annotation</a>, T&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;T&gt;&gt;</code></td><td><code><a href="#loadPlugins(java.lang.Class,java.lang.Class,java.lang.Class,java.util.function.Function)" class="member-name-link">loadPlugins</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;A&gt;&nbsp;annotationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;I&gt;&nbsp;instanceAnnotationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;T&gt;&nbsp;pluginSpecificationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;idExtractor)</code></td><td><div class="block">Loads the plugins of a given type, potentially marked with a given annotation type.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>&lt;A, I extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Annotation.html" title="class or interface in java.lang.annotation" class="external-link">Annotation</a>, T&gt;<br><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;T&gt;&gt;</code></td><td><code><a href="#loadPlugins(java.lang.Class,java.lang.Class,java.lang.Class,java.util.function.Function)" class="member-name-link">loadPlugins</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;A&gt;&nbsp;annotationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;I&gt;&nbsp;instanceAnnotationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;T&gt;&nbsp;pluginSpecificationType,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;idExtractor)</code></td><td><div class="block">Loads the plugins of a given type, potentially marked with a given annotation type.</div><br></td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">Gives access to the platform's plugin manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The platform's plugin manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="loadPlugins(java.lang.Class,java.lang.Class,java.lang.Class,java.util.function.Function)">

:::tabs
== loadPlugins
<div class="horizontal-scroll">
<div class="member-signature"><span class="type-parameters">&lt;A, I extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Annotation.html" title="class or interface in java.lang.annotation" class="external-link">Annotation</a>, T&gt;</span>
<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="PluginData.html" title="class in mod.chiselsandbits.api.plugin">PluginData</a>&lt;T&gt;&gt;</span>&nbsp;<span class="element-name">loadPlugins</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;A&gt;&nbsp;annotationType,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;I&gt;&nbsp;instanceAnnotationType,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;T&gt;&nbsp;pluginSpecificationType,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;T,<wbr><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;idExtractor)</span></div>
<div class="block">Loads the plugins of a given type, potentially marked with a given annotation type.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="loadPlugins(java.lang.Class,java.lang.Class,java.lang.Class,java.util.function.Function)-type-param-A"><code>A</code> - The type of the annotation.</span></dd>
<dd><span id="loadPlugins(java.lang.Class,java.lang.Class,java.lang.Class,java.util.function.Function)-type-param-I"><code>I</code> - The type of the instance annotation.</span></dd>
<dd><span id="loadPlugins(java.lang.Class,java.lang.Class,java.lang.Class,java.util.function.Function)-type-param-T"><code>T</code> - The type of the interface.</span></dd>
<dt>Parameters:</dt>
<dd><code>annotationType</code> - The annotation type to look for.</dd>
<dd><code>instanceAnnotationType</code> - The annotation type that marks the instance of the plugin.</dd>
<dd><code>pluginSpecificationType</code> - The plugin specification interface type to look for.</dd>
<dd><code>idExtractor</code> - The function to extract the id from the plugin specification.</dd>
<dt>Returns:</dt>
<dd>All loaded plugins available.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

