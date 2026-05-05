--- 
title: BlockInformationUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class BlockInformationUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.BlockInformationUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">BlockInformationUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for handling <code>BlockState</code>s.  

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
  <tr><td><code>static <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getRandomSupportedInformation(net.minecraft.util.RandomSource)" class="member-name-link">getRandomSupportedInformation</a><wbr>(net.minecraft.util.RandomSource&nbsp;random)</code></td><td><div class="block">Gets a random chiselable block information from the blocks in the registry.</div><br></td></tr>
  <tr><td><code>static <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>[]</code></td><td><code><a href="#getRandomSupportedInformation(net.minecraft.util.RandomSource,int)" class="member-name-link">getRandomSupportedInformation</a><wbr>(net.minecraft.util.RandomSource&nbsp;random,<br> int&nbsp;count)</code></td><td><div class="block">Gets a random chiselable block information from the blocks in the registry.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getRandomSupportedInformation(net.minecraft.util.RandomSource)" class="member-name-link">getRandomSupportedInformation</a><wbr>(net.minecraft.util.RandomSource&nbsp;random)</code></td><td><div class="block">Gets a random chiselable block information from the blocks in the registry.</div><br></td></tr>
  <tr><td><code>static <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>[]</code></td><td><code><a href="#getRandomSupportedInformation(net.minecraft.util.RandomSource,int)" class="member-name-link">getRandomSupportedInformation</a><wbr>(net.minecraft.util.RandomSource&nbsp;random,<br> int&nbsp;count)</code></td><td><div class="block">Gets a random chiselable block information from the blocks in the registry.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getRandomSupportedInformation(net.minecraft.util.RandomSource)" class="member-name-link">getRandomSupportedInformation</a><wbr>(net.minecraft.util.RandomSource&nbsp;random)</code></td><td><div class="block">Gets a random chiselable block information from the blocks in the registry.</div><br></td></tr>
  <tr><td><code>static <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>[]</code></td><td><code><a href="#getRandomSupportedInformation(net.minecraft.util.RandomSource,int)" class="member-name-link">getRandomSupportedInformation</a><wbr>(net.minecraft.util.RandomSource&nbsp;random,<br> int&nbsp;count)</code></td><td><div class="block">Gets a random chiselable block information from the blocks in the registry.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a></section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getRandomSupportedInformation(net.minecraft.util.RandomSource)">

:::tabs
== getRandomSupportedInformation
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getRandomSupportedInformation</span><wbr><span class="parameters">(net.minecraft.util.RandomSource&nbsp;random)</span></div>
<div class="block">Gets a random chiselable block information from the blocks in the registry.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>random</code> - The random to get the random ids from.</dd>
<dt>Returns:</dt>
<dd>The default random information of a supported chiselable block.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getRandomSupportedInformation(net.minecraft.util.RandomSource,int)">

:::tabs
== getRandomSupportedInformation
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>[]</span>&nbsp;<span class="element-name">getRandomSupportedInformation</span><wbr><span class="parameters">(net.minecraft.util.RandomSource&nbsp;random,
 int&nbsp;count)</span></div>
<div class="block">Gets a random chiselable block information from the blocks in the registry.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>random</code> - The random to get the random ids from.</dd>
<dd><code>count</code> - The amount of random block information to get.</dd>
<dt>Returns:</dt>
<dd>The default random information of a supported chiselable block.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

