--- 
title: IBitItemManager
aside: false 
---
_Package:_ [mod.chiselsandbits.api.item.bit](index.md)  
# Interface IBitItemManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBitItemManager</span></div>  

  

<div class="block">A manager which deals with items for bits.</div>
  

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
  <tr><td><code>default net.minecraft.world.item.ItemStack</code></td><td><code><a href="#create(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">create</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Creates an itemstack that contains a bit of the given block information with a size of 1.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#create(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">create</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Creates an itemstack that contains a bit of the given block information and is of the given size.</div><br></td></tr>
  <tr><td><code>static <a href="IBitItemManager.html" title="interface in mod.chiselsandbits.api.item.bit">IBitItemManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IBitItemManager.html" title="interface in mod.chiselsandbits.api.item.bit">IBitItemManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.item.ItemStack</code></td><td><code><a href="#create(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">create</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Creates an itemstack that contains a bit of the given block information with a size of 1.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#create(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">create</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Creates an itemstack that contains a bit of the given block information and is of the given size.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#create(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">create</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Creates an itemstack that contains a bit of the given block information and is of the given size.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.item.ItemStack</code></td><td><code><a href="#create(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">create</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Creates an itemstack that contains a bit of the given block information with a size of 1.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IBitItemManager.html" title="interface in mod.chiselsandbits.api.item.bit">IBitItemManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="create(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">

:::tabs
== create
<div class="member-signature"><span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 int&nbsp;count)</span></div>
<div class="block">Creates an itemstack that contains a bit of the given block information and is of the given size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The given block information.</dd>
<dd><code>count</code> - The amount of bits.</dd>
<dt>Returns:</dt>
<dd>The itemstack with the given bits.</dd>
</dl>
:::


</section>

<section id="create(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== create
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Creates an itemstack that contains a bit of the given block information with a size of 1.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The given block information.</dd>
<dt>Returns:</dt>
<dd>The itemstack with the given bit.</dd>
</dl>
:::


</section>

:::::
  

