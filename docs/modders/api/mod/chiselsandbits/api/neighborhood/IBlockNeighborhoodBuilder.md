--- 
title: IBlockNeighborhoodBuilder
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.neighborhood](index.md)  
# Interface IBlockNeighborhoodBuilder  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBlockNeighborhoodBuilder</span></div>  

  

Represents a system which can build unique block neighborhoods.  

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
  <tr><td><code>@NotNull <a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></code></td><td><code><a href="#build(java.util.function.Function,java.util.function.Function)" class="member-name-link">build</a><wbr>(@Nullable <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;net.minecraft.core.Direction,<wbr><a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;&nbsp;neighborhoodBlockStateProvider,<br> @Nullable <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;net.minecraft.core.Direction,<wbr><a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;&nbsp;neighborhoodAreaAccessorProvider)</code></td><td><div class="block">Builds a block neighborhood for the requested target.</div><br></td></tr>
  <tr><td><code>static @NotNull <a href="IBlockNeighborhoodBuilder.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhoodBuilder</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current builder instance.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static @NotNull <a href="IBlockNeighborhoodBuilder.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhoodBuilder</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current builder instance.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></code></td><td><code><a href="#build(java.util.function.Function,java.util.function.Function)" class="member-name-link">build</a><wbr>(@Nullable <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;net.minecraft.core.Direction,<wbr><a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;&nbsp;neighborhoodBlockStateProvider,<br> @Nullable <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;net.minecraft.core.Direction,<wbr><a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;&nbsp;neighborhoodAreaAccessorProvider)</code></td><td><div class="block">Builds a block neighborhood for the requested target.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></code></td><td><code><a href="#build(java.util.function.Function,java.util.function.Function)" class="member-name-link">build</a><wbr>(@Nullable <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;net.minecraft.core.Direction,<wbr><a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;&nbsp;neighborhoodBlockStateProvider,<br> @Nullable <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;net.minecraft.core.Direction,<wbr><a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;&nbsp;neighborhoodAreaAccessorProvider)</code></td><td><div class="block">Builds a block neighborhood for the requested target.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">static</span>&nbsp;<span class="return-type">@NotNull <a href="IBlockNeighborhoodBuilder.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhoodBuilder</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
Gives access to the current builder instance.
 Short circuit method for the central API call.
<dl class="notes">
<dt>Returns:</dt>
<dd>The current instance.</dd>
</dl>
:::


</section>

<section id="build(java.util.function.Function,java.util.function.Function)">

:::tabs
== build
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></span>&nbsp;<span class="element-name">build</span><wbr><span class="parameters">(@Nullable
 @Nullable <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;net.minecraft.core.Direction,<wbr><a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;&nbsp;neighborhoodBlockStateProvider,
 @Nullable
 @Nullable <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;net.minecraft.core.Direction,<wbr><a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;&nbsp;neighborhoodAreaAccessorProvider)</span></div>
Builds a block neighborhood for the requested target.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>neighborhoodBlockStateProvider</code> - The blockstate provider to pull the neighborhood data from.</dd>
<dd><code>neighborhoodAreaAccessorProvider</code> - The area accessor provider to pull the neighborhood data from.</dd>
<dt>Returns:</dt>
<dd>A comparable an unique element targeting the requested position and containing the neighborhood data of the target position.</dd>
</dl>
:::


</section>

:::::
  

