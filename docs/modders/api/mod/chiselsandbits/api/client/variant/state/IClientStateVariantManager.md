--- 
title: IClientStateVariantManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.variant.state](index.md)  
# Interface IClientStateVariantManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IClientStateVariantManager</span></div>  

  

The state variant provider for the client.
Handles client specific logic related to the state variant.  

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
  <tr><td><code>void</code></td><td><code><a href="#appendHoverText(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.item.Item.TooltipContext,net.minecraft.world.item.component.TooltipDisplay,java.util.function.Consumer,net.minecraft.world.item.TooltipFlag)" class="member-name-link">appendHoverText</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.item.Item.TooltipContext&nbsp;context,<br> net.minecraft.world.item.component.TooltipDisplay&nbsp;tooltipDisplay,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltipAdder,<br> net.minecraft.world.item.TooltipFlag&nbsp;flag)</code></td><td><div class="block">Invoked to append a tooltip for the given variant in the block information.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.client.models.data.IBlockModelData</code></td><td><code><a href="#getBlockModelData(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getBlockModelData</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Retrieves the block model data for the state block information.</div><br></td></tr>
  <tr><td><code>static <a href="IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></code></td><td><code><a href="#registerStateVariantProvider(java.util.function.Supplier,mod.chiselsandbits.api.client.variant.state.IClientStateVariantProvider)" class="member-name-link">registerStateVariantProvider</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.world.level.block.Block&gt;&nbsp;block,<br> <a href="IClientStateVariantProvider.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantProvider</a>&nbsp;provider)</code></td><td><div class="block">Registers a new state variant provider.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#appendHoverText(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.item.Item.TooltipContext,net.minecraft.world.item.component.TooltipDisplay,java.util.function.Consumer,net.minecraft.world.item.TooltipFlag)" class="member-name-link">appendHoverText</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.item.Item.TooltipContext&nbsp;context,<br> net.minecraft.world.item.component.TooltipDisplay&nbsp;tooltipDisplay,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltipAdder,<br> net.minecraft.world.item.TooltipFlag&nbsp;flag)</code></td><td><div class="block">Invoked to append a tooltip for the given variant in the block information.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.client.models.data.IBlockModelData</code></td><td><code><a href="#getBlockModelData(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getBlockModelData</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Retrieves the block model data for the state block information.</div><br></td></tr>
  <tr><td><code><a href="IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></code></td><td><code><a href="#registerStateVariantProvider(java.util.function.Supplier,mod.chiselsandbits.api.client.variant.state.IClientStateVariantProvider)" class="member-name-link">registerStateVariantProvider</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.world.level.block.Block&gt;&nbsp;block,<br> <a href="IClientStateVariantProvider.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantProvider</a>&nbsp;provider)</code></td><td><div class="block">Registers a new state variant provider.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#appendHoverText(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.item.Item.TooltipContext,net.minecraft.world.item.component.TooltipDisplay,java.util.function.Consumer,net.minecraft.world.item.TooltipFlag)" class="member-name-link">appendHoverText</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.item.Item.TooltipContext&nbsp;context,<br> net.minecraft.world.item.component.TooltipDisplay&nbsp;tooltipDisplay,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltipAdder,<br> net.minecraft.world.item.TooltipFlag&nbsp;flag)</code></td><td><div class="block">Invoked to append a tooltip for the given variant in the block information.</div><br></td></tr>
  <tr><td><code>com.communi.suggestu.scena.core.client.models.data.IBlockModelData</code></td><td><code><a href="#getBlockModelData(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getBlockModelData</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Retrieves the block model data for the state block information.</div><br></td></tr>
  <tr><td><code><a href="IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></code></td><td><code><a href="#registerStateVariantProvider(java.util.function.Supplier,mod.chiselsandbits.api.client.variant.state.IClientStateVariantProvider)" class="member-name-link">registerStateVariantProvider</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.world.level.block.Block&gt;&nbsp;block,<br> <a href="IClientStateVariantProvider.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantProvider</a>&nbsp;provider)</code></td><td><div class="block">Registers a new state variant provider.</div><br></td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="registerStateVariantProvider(java.util.function.Supplier,mod.chiselsandbits.api.client.variant.state.IClientStateVariantProvider)">

:::tabs
== registerStateVariantProvider
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></span>&nbsp;<span class="element-name">registerStateVariantProvider</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;net.minecraft.world.level.block.Block&gt;&nbsp;block,
 <a href="IClientStateVariantProvider.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantProvider</a>&nbsp;provider)</span></div>
<div class="block">Registers a new state variant provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The provider to register.</dd>
<dt>Returns:</dt>
<dd>The manager instance.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getBlockModelData(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== getBlockModelData
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">com.communi.suggestu.scena.core.client.models.data.IBlockModelData</span>&nbsp;<span class="element-name">getBlockModelData</span><wbr><span class="parameters">(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Retrieves the block model data for the state block information.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The state block information.</dd>
<dt>Returns:</dt>
<dd>The block model data.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="appendHoverText(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.item.Item.TooltipContext,net.minecraft.world.item.component.TooltipDisplay,java.util.function.Consumer,net.minecraft.world.item.TooltipFlag)">

:::tabs
== appendHoverText
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">appendHoverText</span><wbr><span class="parameters">(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 net.minecraft.world.item.Item.TooltipContext&nbsp;context,
 net.minecraft.world.item.component.TooltipDisplay&nbsp;tooltipDisplay,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.network.chat.Component&gt;&nbsp;tooltipAdder,
 net.minecraft.world.item.TooltipFlag&nbsp;flag)</span></div>
<div class="block">Invoked to append a tooltip for the given variant in the block information.
If no variant is found this method does nothing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information to append the tooltip for.</dd>
<dd><code>context</code> - The context.</dd>
<dd><code>tooltipDisplay</code> - The display information regarding the tooltip.</dd>
<dd><code>tooltipAdder</code> - The tooltip adder which can be invoked to add a tool tip.</dd>
<dd><code>flag</code> - The flags</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

