--- 
title: IEligibilityManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling.eligibility](index.md)  
# Interface IEligibilityManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IEligibilityManager</span></div>  

  

An object which can manage the eligibility of chiseling of blocks, blockstates,
 or itemstacks (which contain blocks eligible) for chiseling.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IEligibilityAnalysisResult.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityAnalysisResult</a></code></td><td><code><a href="#analyse(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">analyse</a><wbr>(@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Performs a chiselability analysis on the given block information.</div><br></td></tr>
  <tr><td><code><a href="IEligibilityAnalysisResult.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityAnalysisResult</a></code></td><td><code><a href="#analyse(net.minecraft.world.item.ItemStack)" class="member-name-link">analyse</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;provider)</code></td><td><div class="block">Performs a chiselability analysis on the given <code>ItemStack</code>.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canBeChiseled(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canBeChiseled</a><wbr>(@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if a given block information can be chiseled or is already chiseled.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canBeChiseled(net.minecraft.world.item.ItemStack)" class="member-name-link">canBeChiseled</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;provider)</code></td><td><div class="block">Checks if a given <code>ItemStack</code> can be chiseled or is already chiseled.</div><br></td></tr>
  <tr><td><code>static <a href="IEligibilityManager.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IEligibilityManager.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IEligibilityAnalysisResult.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityAnalysisResult</a></code></td><td><code><a href="#analyse(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">analyse</a><wbr>(@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Performs a chiselability analysis on the given block information.</div><br></td></tr>
  <tr><td><code><a href="IEligibilityAnalysisResult.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityAnalysisResult</a></code></td><td><code><a href="#analyse(net.minecraft.world.item.ItemStack)" class="member-name-link">analyse</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;provider)</code></td><td><div class="block">Performs a chiselability analysis on the given <code>ItemStack</code>.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canBeChiseled(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canBeChiseled</a><wbr>(@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if a given block information can be chiseled or is already chiseled.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canBeChiseled(net.minecraft.world.item.ItemStack)" class="member-name-link">canBeChiseled</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;provider)</code></td><td><div class="block">Checks if a given <code>ItemStack</code> can be chiseled or is already chiseled.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IEligibilityAnalysisResult.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityAnalysisResult</a></code></td><td><code><a href="#analyse(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">analyse</a><wbr>(@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Performs a chiselability analysis on the given block information.</div><br></td></tr>
  <tr><td><code><a href="IEligibilityAnalysisResult.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityAnalysisResult</a></code></td><td><code><a href="#analyse(net.minecraft.world.item.ItemStack)" class="member-name-link">analyse</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;provider)</code></td><td><div class="block">Performs a chiselability analysis on the given <code>ItemStack</code>.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#canBeChiseled(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canBeChiseled</a><wbr>(@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if a given block information can be chiseled or is already chiseled.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canBeChiseled(net.minecraft.world.item.ItemStack)" class="member-name-link">canBeChiseled</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;provider)</code></td><td><div class="block">Checks if a given <code>ItemStack</code> can be chiseled or is already chiseled.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IEligibilityManager.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="canBeChiseled(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== canBeChiseled
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">canBeChiseled</span><wbr><span class="parameters">(@NotNull
 @NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
Checks if a given block information can be chiseled or is already chiseled.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The given block information in question.</dd>
<dt>Returns:</dt>
<dd>True when chiselable or already chiseled.</dd>
</dl>
:::


</section>

<section id="canBeChiseled(net.minecraft.world.item.ItemStack)">

:::tabs
== canBeChiseled
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">canBeChiseled</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.item.ItemStack&nbsp;provider)</span></div>
Checks if a given <code>ItemStack</code> can be chiseled or is already chiseled.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The given <code>ItemStack</code> in question.</dd>
<dt>Returns:</dt>
<dd>True when chiselable or already chiseled.</dd>
</dl>
:::


</section>

<section id="analyse(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== analyse
<div class="member-signature"><span class="return-type"><a href="IEligibilityAnalysisResult.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityAnalysisResult</a></span>&nbsp;<span class="element-name">analyse</span><wbr><span class="parameters">(@NotNull
 @NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
Performs a chiselability analysis on the given block information.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information to analyze.</dd>
<dt>Returns:</dt>
<dd>The analysis result.</dd>
</dl>
:::


</section>

<section id="analyse(net.minecraft.world.item.ItemStack)">

:::tabs
== analyse
<div class="member-signature"><span class="return-type"><a href="IEligibilityAnalysisResult.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityAnalysisResult</a></span>&nbsp;<span class="element-name">analyse</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.item.ItemStack&nbsp;provider)</span></div>
Performs a chiselability analysis on the given <code>ItemStack</code>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The <code>ItemStack</code> to analyze.</dd>
<dt>Returns:</dt>
<dd>The analysis result.</dd>
</dl>
:::


</section>

:::::
  

