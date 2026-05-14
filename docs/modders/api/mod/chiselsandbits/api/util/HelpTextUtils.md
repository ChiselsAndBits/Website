--- 
title: HelpTextUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class HelpTextUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.HelpTextUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">HelpTextUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for processing help texts,
most notably used in tooltips of items and blocks.  

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
  <tr><td><code>static void</code></td><td><code><a href="#build(mod.chiselsandbits.api.util.LocalStrings,java.util.function.Consumer,java.lang.Object...)" class="member-name-link">build</a><wbr>(<a href="LocalStrings.html" title="enum class in mod.chiselsandbits.api.util">LocalStrings</a>&nbsp;helpText,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>...&nbsp;variables)</code></td><td><div class="block">Builds a new help tooltip if this is enabled by the player.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#build(mod.chiselsandbits.api.util.LocalStrings,java.util.List,java.lang.Object...)" class="member-name-link">build</a><wbr>(<a href="LocalStrings.html" title="enum class in mod.chiselsandbits.api.util">LocalStrings</a>&nbsp;helpText,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>...&nbsp;variables)</code></td><td><div class="block">Builds a new help tooltip if this is enabled by the player.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static void</code></td><td><code><a href="#build(mod.chiselsandbits.api.util.LocalStrings,java.util.function.Consumer,java.lang.Object...)" class="member-name-link">build</a><wbr>(<a href="LocalStrings.html" title="enum class in mod.chiselsandbits.api.util">LocalStrings</a>&nbsp;helpText,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>...&nbsp;variables)</code></td><td><div class="block">Builds a new help tooltip if this is enabled by the player.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#build(mod.chiselsandbits.api.util.LocalStrings,java.util.List,java.lang.Object...)" class="member-name-link">build</a><wbr>(<a href="LocalStrings.html" title="enum class in mod.chiselsandbits.api.util">LocalStrings</a>&nbsp;helpText,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>...&nbsp;variables)</code></td><td><div class="block">Builds a new help tooltip if this is enabled by the player.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static void</code></td><td><code><a href="#build(mod.chiselsandbits.api.util.LocalStrings,java.util.function.Consumer,java.lang.Object...)" class="member-name-link">build</a><wbr>(<a href="LocalStrings.html" title="enum class in mod.chiselsandbits.api.util">LocalStrings</a>&nbsp;helpText,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>...&nbsp;variables)</code></td><td><div class="block">Builds a new help tooltip if this is enabled by the player.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#build(mod.chiselsandbits.api.util.LocalStrings,java.util.List,java.lang.Object...)" class="member-name-link">build</a><wbr>(<a href="LocalStrings.html" title="enum class in mod.chiselsandbits.api.util">LocalStrings</a>&nbsp;helpText,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>...&nbsp;variables)</code></td><td><div class="block">Builds a new help tooltip if this is enabled by the player.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="build(mod.chiselsandbits.api.util.LocalStrings,java.util.List,java.lang.Object...)">

:::tabs
== build
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">build</span><wbr><span class="parameters">(<a href="LocalStrings.html" title="enum class in mod.chiselsandbits.api.util">LocalStrings</a>&nbsp;helpText,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>...&nbsp;variables)</span></div>
Builds a new help tooltip if this is enabled by the player.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>helpText</code> - The help tooltip.</dd>
<dd><code>tooltip</code> - The tooltip lines to append to.</dd>
<dd><code>variables</code> - The variables to inject.</dd>
</dl>
</div>
:::


</section>

<section id="build(mod.chiselsandbits.api.util.LocalStrings,java.util.function.Consumer,java.lang.Object...)">

:::tabs
== build
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">build</span><wbr><span class="parameters">(<a href="LocalStrings.html" title="enum class in mod.chiselsandbits.api.util">LocalStrings</a>&nbsp;helpText,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>...&nbsp;variables)</span></div>
Builds a new help tooltip if this is enabled by the player.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>helpText</code> - The help tooltip.</dd>
<dd><code>tooltip</code> - The tooltip lines to append to.</dd>
<dd><code>variables</code> - The variables to inject.</dd>
</dl>
</div>
:::


</section>

:::::
  

