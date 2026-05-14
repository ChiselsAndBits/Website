--- 
title: IChiselingItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.chisel](index.md)  
# Interface IChiselingItem  
**All Extended Interfaces:**  
[IChangeTrackingItem](../change/IChangeTrackingItem.md), [ILeftClickControllingItem](../click/ILeftClickControllingItem.md), [IWithHighlightItem](../withhighlight/IWithHighlightItem.md), [IWithModeItem\<IChiselMode\>](../withmode/IWithModeItem.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselingItem</span><span class="extends-implements"><br/>  
extends <a href="../click/ILeftClickControllingItem.html" title="interface in mod.chiselsandbits.api.item.click">ILeftClickControllingItem</a>, <a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a>&lt;<a href="../../chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;, <a href="../withhighlight/IWithHighlightItem.html" title="interface in mod.chiselsandbits.api.item.withhighlight">IWithHighlightItem</a>, <a href="../change/IChangeTrackingItem.html" title="interface in mod.chiselsandbits.api.item.change">IChangeTrackingItem</a></span></div>  

  

  

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
  <tr><td><code>boolean</code></td><td><code><a href="#isDamageableDuringChiseling()" class="member-name-link">isDamageableDuringChiseling</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isDamageableDuringChiseling()" class="member-name-link">isDamageableDuringChiseling</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isDamageableDuringChiseling()" class="member-name-link">isDamageableDuringChiseling</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.click.<a href="../click/ILeftClickControllingItem.html" title="interface in mod.chiselsandbits.api.item.click">ILeftClickControllingItem</a>
<a href="../click/ILeftClickControllingItem.html#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" title="canUse(Player, ItemStack)">canUse</a>, <a href="../click/ILeftClickControllingItem.html#handleLeftClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" title="handleLeftClickProcessing(Player, InteractionHand, BlockPos, Direction, ClickProcessingState)">handleLeftClickProcessing</a>, <a href="../click/ILeftClickControllingItem.html#onLeftClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" title="onLeftClickProcessingEnd(Player, ItemStack)">onLeftClickProcessingEnd</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withhighlight.<a href="../withhighlight/IWithHighlightItem.html" title="interface in mod.chiselsandbits.api.item.withhighlight">IWithHighlightItem</a>
<a href="../withhighlight/IWithHighlightItem.html#renderHighlight(net.minecraft.world.entity.player.Player,net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float)" title="renderHighlight(Player, LevelRenderer, PoseStack, MultiBufferSource.BufferSource, LevelRenderState, float)">renderHighlight</a>, <a href="../withhighlight/IWithHighlightItem.html#shouldDrawDefaultHighlight(net.minecraft.world.entity.player.Player)" title="shouldDrawDefaultHighlight(Player)">shouldDrawDefaultHighlight</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a>
<a href="../withmode/IWithModeItem.html#getMode(net.minecraft.world.item.ItemStack)" title="getMode(ItemStack)">getMode</a>, <a href="../withmode/IWithModeItem.html#getPossibleModes()" title="getPossibleModes()">getPossibleModes</a>, <a href="../withmode/IWithModeItem.html#requiresUpdateOnClosure()" title="requiresUpdateOnClosure()">requiresUpdateOnClosure</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,int)" title="setMode(ItemStack, int)">setMode</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,M)" title="setMode(ItemStack, IChiselMode)">setMode</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="isDamageableDuringChiseling()">

:::tabs
== isDamageableDuringChiseling
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isDamageableDuringChiseling</span>()</div>
</div>
:::


</section>

:::::
  

