--- 
title: IMultiUsePatternItem
aside: false 
---
_Package:_ [mod.chiselsandbits.api.item.pattern](index.md)  
# Interface IMultiUsePatternItem  
**All Extended Interfaces:**  
[IChangeTrackingItem](../change/IChangeTrackingItem.md), [IMultiStateItem](../multistate/IMultiStateItem.md), [IPatternItem](IPatternItem.md), [IWireframeProvidingItem](../wireframe/IWireframeProvidingItem.md), [IWithModeItem\<IPatternPlacementType\>](../withmode/IWithModeItem.md), [IPlaceable](../placement/IPlaceable.md), [IPlacementPreviewProvidingItem](../placement/IPlacementPreviewProvidingItem.md), [IPlacementProperties](../placement/IPlacementProperties.md), [ISupportsSealing](../sealing/ISupportsSealing.md), [ISupportsUnsealing](../sealing/ISupportsUnsealing.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiUsePatternItem</span><span class="extends-implements"><br/>  
extends <a href="IPatternItem.html" title="interface in mod.chiselsandbits.api.item.pattern">IPatternItem</a>, <a href="../../sealing/ISupportsUnsealing.html" title="interface in mod.chiselsandbits.api.sealing">ISupportsUnsealing</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.multistate.<a href="../multistate/IMultiStateItem.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItem</a>
<a href="../multistate/IMultiStateItem.html#createItemStack(net.minecraft.world.item.ItemStack)">createItemStack</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.pattern.<a href="IPatternItem.html" title="interface in mod.chiselsandbits.api.item.pattern">IPatternItem</a>
<a href="IPatternItem.html#getPlacementResult(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getPlacementResult</a>, <a href="IPatternItem.html#getTargetedPosition(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getTargetedPosition</a>, <a href="IPatternItem.html#getWireFrame(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getWireFrame</a>, <a href="IPatternItem.html#getWireFrameColor(net.minecraft.world.item.ItemStack,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.BlockHitResult)">getWireFrameColor</a>, <a href="IPatternItem.html#overridesOccupiedBits(net.minecraft.world.item.ItemStack)">overridesOccupiedBits</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.placement.<a href="../../placement/IPlacementPreviewProvidingItem.html" title="interface in mod.chiselsandbits.api.placement">IPlacementPreviewProvidingItem</a>
<a href="../../placement/IPlacementPreviewProvidingItem.html#ignoreDepth(net.minecraft.world.item.ItemStack)">ignoreDepth</a>, <a href="../../placement/IPlacementPreviewProvidingItem.html#ignoreDepthForPlacement(net.minecraft.world.item.ItemStack,mod.chiselsandbits.api.placement.PlacementResult)">ignoreDepthForPlacement</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.sealing.<a href="../../sealing/ISupportsSealing.html" title="interface in mod.chiselsandbits.api.sealing">ISupportsSealing</a>
<a href="../../sealing/ISupportsSealing.html#seal(net.minecraft.world.item.ItemStack)">seal</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.sealing.<a href="../../sealing/ISupportsUnsealing.html" title="interface in mod.chiselsandbits.api.sealing">ISupportsUnsealing</a>
<a href="../../sealing/ISupportsUnsealing.html#unseal(net.minecraft.world.item.ItemStack)">unseal</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a>
<a href="../withmode/IWithModeItem.html#getMode(net.minecraft.world.item.ItemStack)">getMode</a>, <a href="../withmode/IWithModeItem.html#getPossibleModes()">getPossibleModes</a>, <a href="../withmode/IWithModeItem.html#requiresUpdateOnClosure()">requiresUpdateOnClosure</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,int)">setMode</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,M)">setMode</a>
:::::
:::::::
  
  
  

  

  

  

  

  

  

