--- 
title: IChiselsAndBitsPlugin
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.plugin](index.md)  
# Interface IChiselsAndBitsPlugin  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselsAndBitsPlugin</span></div>  

  

Represents a plugin for ChiselsAndBits.
 <p>
     Plugins have callbacks that can be invoked by chisels and bits.
     See their documentation for more information.
 </p>
 <p>
     All methods are potentially invoked in parallel with other plugins, or even chisels and bits itself.
 </p>
 <p>
     Plugins are loaded through the <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ServiceLoader.html" title="class or interface in java.util" class="external-link"><code>ServiceLoader</code></a>. If annotated by <a href="ChiselsAndBitsPlugin.html" title="annotation interface in mod.chiselsandbits.api.plugin"><code>ChiselsAndBitsPlugin</code></a>
     then additional metadata is checked, like required mods or experimental flags.
 </p>  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of the plugin.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onClientConstruction()" class="member-name-link">onClientConstruction</a>()</code></td><td><div class="block">Called after ChiselsAndBits client construction completes.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onConstruction()" class="member-name-link">onConstruction</a>()</code></td><td><div class="block">Invoked when the plugin is constructed.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onInitialize()" class="member-name-link">onInitialize</a>()</code></td><td><div class="block">Invoked by chisels and bits when the platform it runs on (so forge or fabric) indicates that mod initialization should happen.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of the plugin.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onClientConstruction()" class="member-name-link">onClientConstruction</a>()</code></td><td><div class="block">Called after ChiselsAndBits client construction completes.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onConstruction()" class="member-name-link">onConstruction</a>()</code></td><td><div class="block">Invoked when the plugin is constructed.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onInitialize()" class="member-name-link">onInitialize</a>()</code></td><td><div class="block">Invoked by chisels and bits when the platform it runs on (so forge or fabric) indicates that mod initialization should happen.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of the plugin.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#onClientConstruction()" class="member-name-link">onClientConstruction</a>()</code></td><td><div class="block">Called after ChiselsAndBits client construction completes.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onConstruction()" class="member-name-link">onConstruction</a>()</code></td><td><div class="block">Invoked when the plugin is constructed.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onInitialize()" class="member-name-link">onInitialize</a>()</code></td><td><div class="block">Invoked by chisels and bits when the platform it runs on (so forge or fabric) indicates that mod initialization should happen.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getId()">

:::tabs
== getId
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">getId</span>()</div>
The id of the plugin.
 Has to be unique over all plugins.
<dl class="notes">
<dt>Returns:</dt>
<dd>The id.</dd>
</dl>
:::


</section>

<section id="onConstruction()">

:::tabs
== onConstruction
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">onConstruction</span>()</div>
Invoked when the plugin is constructed.
<dl class="notes"></dl>
:::


</section>

<section id="onClientConstruction()">

:::tabs
== onClientConstruction
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">onClientConstruction</span>()</div>
Called after ChiselsAndBits client construction completes.
<dl class="notes"></dl>
:::


</section>

<section id="onInitialize()">

:::tabs
== onInitialize
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">onInitialize</span>()</div>
Invoked by chisels and bits when the platform it runs on (so forge or fabric) indicates that mod initialization should happen.
<dl class="notes"></dl>
:::


</section>

:::::
  

