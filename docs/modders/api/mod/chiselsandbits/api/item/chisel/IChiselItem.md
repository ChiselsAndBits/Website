--- 
title: IChiselItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.chisel](index.md)  
# Interface IChiselItem  
**All Extended Interfaces:**  
[IChangeTrackingItem](../change/IChangeTrackingItem.md), [IChiselingItem](IChiselingItem.md), [ILeftClickControllingItem](../click/ILeftClickControllingItem.md), [IWithHighlightItem](../withhighlight/IWithHighlightItem.md), [IWithModeItem\<IChiselMode\>](../withmode/IWithModeItem.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselItem</span><span class="extends-implements"><br/>  
extends <a href="IChiselingItem.html" title="interface in mod.chiselsandbits.api.item.chisel">IChiselingItem</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.chisel.<a href="IChiselingItem.html" title="interface in mod.chiselsandbits.api.item.chisel">IChiselingItem</a><a href="IChiselingItem.html#isDamageableDuringChiseling()" title="isDamageableDuringChiseling()">isDamageableDuringChiseling</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.click.<a href="../click/ILeftClickControllingItem.html" title="interface in mod.chiselsandbits.api.item.click">ILeftClickControllingItem</a><a href="../click/ILeftClickControllingItem.html#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" title="canUse(Player, ItemStack)">canUse</a>, <a href="../click/ILeftClickControllingItem.html#handleLeftClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" title="handleLeftClickProcessing(Player, InteractionHand, BlockPos, Direction, ClickProcessingState)">handleLeftClickProcessing</a>, <a href="../click/ILeftClickControllingItem.html#onLeftClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" title="onLeftClickProcessingEnd(Player, ItemStack)">onLeftClickProcessingEnd</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withhighlight.<a href="../withhighlight/IWithHighlightItem.html" title="interface in mod.chiselsandbits.api.item.withhighlight">IWithHighlightItem</a><a href="../withhighlight/IWithHighlightItem.html#renderHighlight(net.minecraft.world.entity.player.Player,net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float)" title="renderHighlight(Player, LevelRenderer, PoseStack, MultiBufferSource.BufferSource, LevelRenderState, float)">renderHighlight</a>, <a href="../withhighlight/IWithHighlightItem.html#shouldDrawDefaultHighlight(net.minecraft.world.entity.player.Player)" title="shouldDrawDefaultHighlight(Player)">shouldDrawDefaultHighlight</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a><a href="../withmode/IWithModeItem.html#getMode(net.minecraft.world.item.ItemStack)" title="getMode(ItemStack)">getMode</a>, <a href="../withmode/IWithModeItem.html#getPossibleModes()" title="getPossibleModes()">getPossibleModes</a>, <a href="../withmode/IWithModeItem.html#requiresUpdateOnClosure()" title="requiresUpdateOnClosure()">requiresUpdateOnClosure</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,int)" title="setMode(ItemStack, int)">setMode</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,M)" title="setMode(ItemStack, IChiselMode)">setMode</a>
  
  
  

  

  

  

  

  

  

