--- 
title: IBitItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.bit](index.md)  
# Interface IBitItem  
**All Extended Interfaces:**  
[IChangeTrackingItem](../change/IChangeTrackingItem.md), [IRightClickControllingItem](../click/IRightClickControllingItem.md), [IWithHighlightItem](../withhighlight/IWithHighlightItem.md), [IWithModeItem\<IChiselMode\>](../withmode/IWithModeItem.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBitItem</span><span class="extends-implements"><br/>  
extends <a href="../click/IRightClickControllingItem.html" title="interface in mod.chiselsandbits.api.item.click">IRightClickControllingItem</a>, <a href="../withhighlight/IWithHighlightItem.html" title="interface in mod.chiselsandbits.api.item.withhighlight">IWithHighlightItem</a>, <a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a>&lt;<a href="../../chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;, <a href="../change/IChangeTrackingItem.html" title="interface in mod.chiselsandbits.api.item.change">IChangeTrackingItem</a></span></div>  

  

Represents an item which is a single bit.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.world.item.ItemStack)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Returns the block information which is contained in a stack with the<br> given bit item.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onMergeOperationWithBagBeginning()" class="member-name-link">onMergeOperationWithBagBeginning</a>()</code></td><td><div class="block">Invoked when a merge operation of a bit inside a bitbag is beginning during a shift-click interaction<br> in the bit bag UI.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onMergeOperationWithBagEnding()" class="member-name-link">onMergeOperationWithBagEnding</a>()</code></td><td><div class="block">Invoked when a merge operation of a bit inside a bitbag is ending during a shift-click interaction<br> in the bit bag UI.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.world.item.ItemStack)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Returns the block information which is contained in a stack with the<br> given bit item.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onMergeOperationWithBagBeginning()" class="member-name-link">onMergeOperationWithBagBeginning</a>()</code></td><td><div class="block">Invoked when a merge operation of a bit inside a bitbag is beginning during a shift-click interaction<br> in the bit bag UI.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onMergeOperationWithBagEnding()" class="member-name-link">onMergeOperationWithBagEnding</a>()</code></td><td><div class="block">Invoked when a merge operation of a bit inside a bitbag is ending during a shift-click interaction<br> in the bit bag UI.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getBlockInformation(net.minecraft.world.item.ItemStack)" class="member-name-link">getBlockInformation</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Returns the block information which is contained in a stack with the<br> given bit item.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onMergeOperationWithBagBeginning()" class="member-name-link">onMergeOperationWithBagBeginning</a>()</code></td><td><div class="block">Invoked when a merge operation of a bit inside a bitbag is beginning during a shift-click interaction<br> in the bit bag UI.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onMergeOperationWithBagEnding()" class="member-name-link">onMergeOperationWithBagEnding</a>()</code></td><td><div class="block">Invoked when a merge operation of a bit inside a bitbag is ending during a shift-click interaction<br> in the bit bag UI.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.click.<a href="../click/IRightClickControllingItem.html" title="interface in mod.chiselsandbits.api.item.click">IRightClickControllingItem</a>
<a href="../click/IRightClickControllingItem.html#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)">canUse</a>, <a href="../click/IRightClickControllingItem.html#handleRightClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)">handleRightClickProcessing</a>, <a href="../click/IRightClickControllingItem.html#onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)">onRightClickProcessingEnd</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withhighlight.<a href="../withhighlight/IWithHighlightItem.html" title="interface in mod.chiselsandbits.api.item.withhighlight">IWithHighlightItem</a>
<a href="../withhighlight/IWithHighlightItem.html#renderHighlight(net.minecraft.world.entity.player.Player,net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.LevelRenderState,float)">renderHighlight</a>, <a href="../withhighlight/IWithHighlightItem.html#shouldDrawDefaultHighlight(net.minecraft.world.entity.player.Player)">shouldDrawDefaultHighlight</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a>
<a href="../withmode/IWithModeItem.html#getMode(net.minecraft.world.item.ItemStack)">getMode</a>, <a href="../withmode/IWithModeItem.html#getPossibleModes()">getPossibleModes</a>, <a href="../withmode/IWithModeItem.html#requiresUpdateOnClosure()">requiresUpdateOnClosure</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,int)">setMode</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,M)">setMode</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getBlockInformation(net.minecraft.world.item.ItemStack)">

:::tabs
== getBlockInformation
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getBlockInformation</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Returns the block information which is contained in a stack with the
 given bit item.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack which contains this bit item.</dd>
<dt>Returns:</dt>
<dd>The block information contained in this bit item.</dd>
</dl>
:::


</section>

<section id="onMergeOperationWithBagBeginning()">

:::tabs
== onMergeOperationWithBagBeginning
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">onMergeOperationWithBagBeginning</span>()</div>
Invoked when a merge operation of a bit inside a bitbag is beginning during a shift-click interaction
 in the bit bag UI.
<dl class="notes"></dl>
:::


</section>

<section id="onMergeOperationWithBagEnding()">

:::tabs
== onMergeOperationWithBagEnding
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">onMergeOperationWithBagEnding</span>()</div>
Invoked when a merge operation of a bit inside a bitbag is ending during a shift-click interaction
 in the bit bag UI.
<dl class="notes"></dl>
:::


</section>

:::::
  

