--- 
title: ILaunchPropertyManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.launch](index.md)  
# Interface ILaunchPropertyManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ILaunchPropertyManager</span></div>  

  

Defines a manager that handles properties related to how the game is launcher
Important here is that these properties can effect launch and game behaviour and need to be
the same as the properties of the server you are connecting to.  

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
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#get(java.lang.String,java.lang.String)" class="member-name-link">get</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;defaultValue)</code></td><td><div class="block">Retrieves the value of the launch property with the given key.</div><br></td></tr>
  <tr><td><code>static <a href="ILaunchPropertyManager.html" title="interface in mod.chiselsandbits.api.launch">ILaunchPropertyManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The current instance of the launch property manager.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="ILaunchPropertyManager.html" title="interface in mod.chiselsandbits.api.launch">ILaunchPropertyManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The current instance of the launch property manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#get(java.lang.String,java.lang.String)" class="member-name-link">get</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;defaultValue)</code></td><td><div class="block">Retrieves the value of the launch property with the given key.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#get(java.lang.String,java.lang.String)" class="member-name-link">get</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;defaultValue)</code></td><td><div class="block">Retrieves the value of the launch property with the given key.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="ILaunchPropertyManager.html" title="interface in mod.chiselsandbits.api.launch">ILaunchPropertyManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
The current instance of the launch property manager.
<dl class="notes">
<dt>Returns:</dt>
<dd>The current instance.</dd>
</dl>
</div>
:::


</section>

<section id="get(java.lang.String,java.lang.String)">

:::tabs
== get
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;key,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;defaultValue)</span></div>
Retrieves the value of the launch property with the given key.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - The key to get the launch property of.</dd>
<dd><code>defaultValue</code> - The default value if not configured.</dd>
<dt>Returns:</dt>
<dd>The current value of the property.</dd>
</dl>
</div>
:::


</section>

:::::
  

