--- 
title: IPatternSharingManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.sharing](index.md)  
# Interface IPatternSharingManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPatternSharingManager</span></div>  

  

<div class="block">Central manager which handles sharing of patterns.
 This manager only works on the client side, and does nothing on the server side.</div>
  

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
  <tr><td><code>void</code></td><td><code><a href="#exportPattern(mod.chiselsandbits.api.item.multistate.IMultiStateItemStack,java.lang.String)" class="member-name-link">exportPattern</a><wbr>(<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Exports the given pattern to disk.</div><br></td></tr>
  <tr><td><code>static <a href="IPatternSharingManager.html" title="interface in mod.chiselsandbits.api.client.sharing">IPatternSharingManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>com.mojang.datafixers.util.Either<wbr>&lt;<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>,<wbr><a href="PatternIOException.html" title="class in mod.chiselsandbits.api.client.sharing">PatternIOException</a>&gt;</code></td><td><code><a href="#importPattern(java.lang.String)" class="member-name-link">importPattern</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Imports the pattern from disk.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IPatternSharingManager.html" title="interface in mod.chiselsandbits.api.client.sharing">IPatternSharingManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#exportPattern(mod.chiselsandbits.api.item.multistate.IMultiStateItemStack,java.lang.String)" class="member-name-link">exportPattern</a><wbr>(<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Exports the given pattern to disk.</div><br></td></tr>
  <tr><td><code>com.mojang.datafixers.util.Either<wbr>&lt;<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>,<wbr><a href="PatternIOException.html" title="class in mod.chiselsandbits.api.client.sharing">PatternIOException</a>&gt;</code></td><td><code><a href="#importPattern(java.lang.String)" class="member-name-link">importPattern</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Imports the pattern from disk.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#exportPattern(mod.chiselsandbits.api.item.multistate.IMultiStateItemStack,java.lang.String)" class="member-name-link">exportPattern</a><wbr>(<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Exports the given pattern to disk.</div><br></td></tr>
  <tr><td><code>com.mojang.datafixers.util.Either<wbr>&lt;<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>,<wbr><a href="PatternIOException.html" title="class in mod.chiselsandbits.api.client.sharing">PatternIOException</a>&gt;</code></td><td><code><a href="#importPattern(java.lang.String)" class="member-name-link">importPattern</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Imports the pattern from disk.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPatternSharingManager.html" title="interface in mod.chiselsandbits.api.client.sharing">IPatternSharingManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="exportPattern(mod.chiselsandbits.api.item.multistate.IMultiStateItemStack,java.lang.String)">

:::tabs
== exportPattern
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">exportPattern</span><wbr><span class="parameters">(<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack,
 <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</span></div>
<div class="block">Exports the given pattern to disk.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>multiStateItemStack</code> - The multistate itemstack to export.</dd>
<dd><code>name</code> - The name of the export.</dd>
</dl>
:::


</section>

<section id="importPattern(java.lang.String)">

:::tabs
== importPattern
<div class="member-signature"><span class="return-type">com.mojang.datafixers.util.Either&lt;<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>,<wbr><a href="PatternIOException.html" title="class in mod.chiselsandbits.api.client.sharing">PatternIOException</a>&gt;</span>&nbsp;<span class="element-name">importPattern</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</span></div>
<div class="block">Imports the pattern from disk.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - The name of the pattern to import.</dd>
<dt>Returns:</dt>
<dd>The name of the export.</dd>
</dl>
:::


</section>

:::::
  

