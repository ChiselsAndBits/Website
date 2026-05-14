--- 
title: ISupportsSealing
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.sealing](index.md)  
# Interface ISupportsSealing  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ISupportsSealing</span></div>  

  

Represents something which supports the sealing of itemstacks.  

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
  <tr><td><code>@NotNull net.minecraft.world.item.ItemStack</code></td><td><code><a href="#seal(net.minecraft.world.item.ItemStack)" class="member-name-link">seal</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;source)</code></td><td><div class="block">Performs the sealing operation on the given itemstack.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull net.minecraft.world.item.ItemStack</code></td><td><code><a href="#seal(net.minecraft.world.item.ItemStack)" class="member-name-link">seal</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;source)</code></td><td><div class="block">Performs the sealing operation on the given itemstack.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull net.minecraft.world.item.ItemStack</code></td><td><code><a href="#seal(net.minecraft.world.item.ItemStack)" class="member-name-link">seal</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;source)</code></td><td><div class="block">Performs the sealing operation on the given itemstack.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="seal(net.minecraft.world.item.ItemStack)">
:::tabs
== seal
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">seal</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.item.ItemStack&nbsp;source)</span>
                                          throws <span class="exceptions"><a href="../exceptions/SealingNotSupportedException.html" title="class in mod.chiselsandbits.api.exceptions">SealingNotSupportedException</a></span></div>
Performs the sealing operation on the given itemstack.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - The source itemstack to seal.</dd>
<dt>Returns:</dt>
<dd>The sealed variant of the itemstack.</dd>
<dt>Throws:</dt>
<dd><code><a href="../exceptions/SealingNotSupportedException.html" title="class in mod.chiselsandbits.api.exceptions">SealingNotSupportedException</a></code> - Thrown when the given stack could not be sealed.</dd>
</dl>
</div>
:::
</section>
:::::
  

