--- 
title: IMultiStateItem
aside: false 
---
_Package:_ [mod.chiselsandbits.api.item.multistate](index.md)  
# Interface IMultiStateItem  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiStateItem</span></div>  

  

<div class="block">An item whose itemstacks contain multistate information.</div>
  

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
  <tr><td><code>@NotNull <a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#createItemStack(net.minecraft.world.item.ItemStack)" class="member-name-link">createItemStack</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates an itemstack aware context wrapper that gives access to the<br> multistate information contained within the given itemstack.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#createItemStack(net.minecraft.world.item.ItemStack)" class="member-name-link">createItemStack</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates an itemstack aware context wrapper that gives access to the<br> multistate information contained within the given itemstack.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></code></td><td><code><a href="#createItemStack(net.minecraft.world.item.ItemStack)" class="member-name-link">createItemStack</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Creates an itemstack aware context wrapper that gives access to the<br> multistate information contained within the given itemstack.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="createItemStack(net.minecraft.world.item.ItemStack)">

:::tabs
== createItemStack
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a></span>&nbsp;<span class="element-name">createItemStack</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Creates an itemstack aware context wrapper that gives access to the
 multistate information contained within the given itemstack.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to get an <a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate"><code>IMultiStateItemStack</code></a> for.</dd>
<dt>Returns:</dt>
<dd>The <a href="IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate"><code>IMultiStateItemStack</code></a> that represents the data in the given itemstack.</dd>
</dl>
:::


</section>

:::::
  

