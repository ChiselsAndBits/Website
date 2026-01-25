--- 
title: IBlockNeighborhood
aside: false 
---
_Package:_ [mod.chiselsandbits.api.neighborhood](index.md)  
# Interface IBlockNeighborhood  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBlockNeighborhood</span></div>  

  

<div class="block">Marker interface used to detect block neighborhoods in cache keys.</div>
  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Summary  
:::tabs
== Fields
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final <a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></code></td><td><code><a href="#EMPTY" class="member-name-link">EMPTY</a></code></td><td><div class="block">Empty neighborhood.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
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
  <tr><td><code>@Nullable <a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#getAreaAccessor(net.minecraft.core.Direction)" class="member-name-link">getAreaAccessor</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks potential area accessor neighbor in the given direction.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.core.Direction)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks neighbor in the given direction.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@Nullable <a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#getAreaAccessor(net.minecraft.core.Direction)" class="member-name-link">getAreaAccessor</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks potential area accessor neighbor in the given direction.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.core.Direction)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks neighbor in the given direction.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@Nullable <a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></code></td><td><code><a href="#getAreaAccessor(net.minecraft.core.Direction)" class="member-name-link">getAreaAccessor</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks potential area accessor neighbor in the given direction.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.core.Direction)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.core.Direction&nbsp;direction)</code></td><td><div class="block">Returns the blocks neighbor in the given direction.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="EMPTY">

:::tabs
== EMPTY
<div class="member-signature"><span class="modifiers">static final</span>&nbsp;<span class="return-type"><a href="IBlockNeighborhood.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhood</a></span>&nbsp;<span class="element-name">EMPTY</span></div>
<div class="block">Empty neighborhood.</div>
<dl class="notes"></dl>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getBlockInformation(net.minecraft.core.Direction)">

:::tabs
== getBlockInformation
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getBlockInformation</span><wbr><span class="parameters">(net.minecraft.core.Direction&nbsp;direction)</span></div>
<div class="block">Returns the blocks neighbor in the given direction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - The direction.</dd>
<dt>Returns:</dt>
<dd>The blockstate</dd>
</dl>
:::


</section>

<section id="getAreaAccessor(net.minecraft.core.Direction)">

:::tabs
== getAreaAccessor
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type">@Nullable <a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a></span>&nbsp;<span class="element-name">getAreaAccessor</span><wbr><span class="parameters">(net.minecraft.core.Direction&nbsp;direction)</span></div>
<div class="block">Returns the blocks potential area accessor neighbor in the given direction.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - The direction.</dd>
<dt>Returns:</dt>
<dd>The area accessor.</dd>
</dl>
:::


</section>

:::::
  

