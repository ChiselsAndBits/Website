--- 
title: ISnapshotFactory
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.snapshot](index)  
# Interface ISnapshotFactory  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ISnapshotFactory</span></div>  

  

A factory to create simple snapshots.  

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
  <tr><td><code>static <a href="ISnapshotFactory.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">ISnapshotFactory</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#singleBlock()" class="member-name-link">singleBlock</a>()</code></td><td><div class="block">Creates a new simple single block snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#singleBlock(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">singleBlock</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Creates a new simple single block snapshot.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="ISnapshotFactory.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">ISnapshotFactory</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#singleBlock()" class="member-name-link">singleBlock</a>()</code></td><td><div class="block">Creates a new simple single block snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#singleBlock(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">singleBlock</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Creates a new simple single block snapshot.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#singleBlock()" class="member-name-link">singleBlock</a>()</code></td><td><div class="block">Creates a new simple single block snapshot.</div><br></td></tr>
  <tr><td><code><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></code></td><td><code><a href="#singleBlock(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">singleBlock</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Creates a new simple single block snapshot.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="ISnapshotFactory.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">ISnapshotFactory</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
</div>
:::


</section>

<section id="singleBlock()">

:::tabs
== singleBlock
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></span>&nbsp;<span class="element-name">singleBlock</span>()</div>
Creates a new simple single block snapshot.
<dl class="notes">
<dt>Returns:</dt>
<dd>The new snapshot.</dd>
</dl>
</div>
:::


</section>

<section id="singleBlock(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== singleBlock
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a></span>&nbsp;<span class="element-name">singleBlock</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
Creates a new simple single block snapshot.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information which will fill up the entire snapshot once returned.</dd>
<dt>Returns:</dt>
<dd>The new snapshot.</dd>
</dl>
</div>
:::


</section>

:::::
  

