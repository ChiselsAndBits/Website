--- 
title: IClientStateVariantProvider
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.variant.state](index.md)  
# Interface IClientStateVariantProvider  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IClientStateVariantProvider</span></div>  

  

A state variant provider for client side interactions.  

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
  <tr><td><code>void</code></td><td><code><a href="#appendHoverText(mod.chiselsandbits.api.variant.state.IStateVariant,net.minecraft.world.item.Item.TooltipContext,java.util.List,net.minecraft.world.item.TooltipFlag)" class="member-name-link">appendHoverText</a><wbr>(<a href="../../../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;variant,<br> net.minecraft.world.item.Item.TooltipContext&nbsp;context,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> net.minecraft.world.item.TooltipFlag&nbsp;flags)</code></td><td><div class="block">Invoked to add tooltip lines to the tooltip of an item containing the given variant.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.client.models.data.IBlockModelData</code></td><td><code><a href="#getBlockModelData(mod.chiselsandbits.api.variant.state.IStateVariant)" class="member-name-link">getBlockModelData</a><wbr>(<a href="../../../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;variant)</code></td><td><div class="block">Retrieves the block model data for the given state variant.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#appendHoverText(mod.chiselsandbits.api.variant.state.IStateVariant,net.minecraft.world.item.Item.TooltipContext,java.util.List,net.minecraft.world.item.TooltipFlag)" class="member-name-link">appendHoverText</a><wbr>(<a href="../../../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;variant,<br> net.minecraft.world.item.Item.TooltipContext&nbsp;context,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> net.minecraft.world.item.TooltipFlag&nbsp;flags)</code></td><td><div class="block">Invoked to add tooltip lines to the tooltip of an item containing the given variant.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.client.models.data.IBlockModelData</code></td><td><code><a href="#getBlockModelData(mod.chiselsandbits.api.variant.state.IStateVariant)" class="member-name-link">getBlockModelData</a><wbr>(<a href="../../../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;variant)</code></td><td><div class="block">Retrieves the block model data for the given state variant.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#appendHoverText(mod.chiselsandbits.api.variant.state.IStateVariant,net.minecraft.world.item.Item.TooltipContext,java.util.List,net.minecraft.world.item.TooltipFlag)" class="member-name-link">appendHoverText</a><wbr>(<a href="../../../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;variant,<br> net.minecraft.world.item.Item.TooltipContext&nbsp;context,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,<br> net.minecraft.world.item.TooltipFlag&nbsp;flags)</code></td><td><div class="block">Invoked to add tooltip lines to the tooltip of an item containing the given variant.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.client.models.data.IBlockModelData</code></td><td><code><a href="#getBlockModelData(mod.chiselsandbits.api.variant.state.IStateVariant)" class="member-name-link">getBlockModelData</a><wbr>(<a href="../../../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;variant)</code></td><td><div class="block">Retrieves the block model data for the given state variant.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getBlockModelData(mod.chiselsandbits.api.variant.state.IStateVariant)">

:::tabs
== getBlockModelData
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">com.communi.suggestu.scena.core.client.models.data.IBlockModelData</span>&nbsp;<span class="element-name">getBlockModelData</span><wbr><span class="parameters">(<a href="../../../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;variant)</span></div>
<div class="block">Retrieves the block model data for the given state variant.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variant</code> - The state variant.</dd>
<dt>Returns:</dt>
<dd>The block model data.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="appendHoverText(mod.chiselsandbits.api.variant.state.IStateVariant,net.minecraft.world.item.Item.TooltipContext,java.util.List,net.minecraft.world.item.TooltipFlag)">

:::tabs
== appendHoverText
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">appendHoverText</span><wbr><span class="parameters">(<a href="../../../variant/state/IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;variant,
 net.minecraft.world.item.Item.TooltipContext&nbsp;context,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltip,
 net.minecraft.world.item.TooltipFlag&nbsp;flags)</span></div>
<div class="block">Invoked to add tooltip lines to the tooltip of an item containing the given variant.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variant</code> - The variant contained in the stack in question.</dd>
<dd><code>context</code> - The context.</dd>
<dd><code>tooltip</code> - The tooltip lines</dd>
<dd><code>flags</code> - The tooltip flags.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

