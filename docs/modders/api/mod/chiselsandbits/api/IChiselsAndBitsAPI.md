--- 
title: IChiselsAndBitsAPI
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api](index.md)  
# Interface IChiselsAndBitsAPI  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselsAndBitsAPI</span></div>  

  

Do not implement it can be accessed via its <a href="IChiselsAndBitsAPI.html#getInstance()"><code>IChiselsAndBitsAPI.getInstance()</code></a>-method.  

<dl class="notes"></dl>  

<li>
<section class="nested-class-summary" id="nested-class-summary">Nested Class Summary  
:::tabs
== Nested Classes
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Interface</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static class&nbsp;</code></td><td><code><a href="IChiselsAndBitsAPI.Holder.html" class="type-name-link" title="class in mod.chiselsandbits.api">IChiselsAndBitsAPI.Holder</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
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
  <tr><td><code>@NotNull <a href="multistate/accessor/IAccessorFactory.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAccessorFactory</a></code></td><td><code><a href="#getAccessorFactory()" class="member-name-link">getAccessorFactory</a>()</code></td><td><div class="block">Gives access to the factory that can produce different accessors.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="inventory/bit/IAdaptingBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.bit">IAdaptingBitInventoryManager</a></code></td><td><code><a href="#getAdaptingBitInventoryManager()" class="member-name-link">getAdaptingBitInventoryManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="inventory/management/IBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.management">IBitInventoryManager</a></code></td><td><code><a href="#getBitInventoryManager()" class="member-name-link">getBitInventoryManager</a>()</code></td><td><div class="block">Gives access to the bits inventory manager, which allows the conversion of normal inventory systems to bit inventories.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="item/bit/IBitItemManager.html" title="interface in mod.chiselsandbits.api.item.bit">IBitItemManager</a></code></td><td><code><a href="#getBitItemManager()" class="member-name-link">getBitItemManager</a>()</code></td><td><div class="block">The bit item manager.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.tags.TagKey<wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getBlockedTag()" class="member-name-link">getBlockedTag</a>()</code></td><td><div class="block">Returns the tag used in the eligibility system to block compatibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="neighborhood/IBlockNeighborhoodBuilder.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhoodBuilder</a></code></td><td><code><a href="#getBlockNeighborhoodBuilder()" class="member-name-link">getBlockNeighborhoodBuilder</a>()</code></td><td><div class="block">Gives access to the block neighborhood builder.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="block/state/id/IBlockStateIdManager.html" title="interface in mod.chiselsandbits.api.block.state.id">IBlockStateIdManager</a></code></td><td><code><a href="#getBlockStateIdManager()" class="member-name-link">getBlockStateIdManager</a>()</code></td><td><div class="block">The manager which deals with calculating the given blockstate ids in the current running session.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="change/IChangeTrackerManager.html" title="interface in mod.chiselsandbits.api.change">IChangeTrackerManager</a></code></td><td><code><a href="#getChangeTrackerManager()" class="member-name-link">getChangeTrackerManager</a>()</code></td><td><div class="block">The change tracker manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/render/preview/chiseling/IChiselContextPreviewRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.render.preview.chiseling">IChiselContextPreviewRendererRegistry</a></code></td><td><code><a href="#getChiselContextPreviewRendererRegistry()" class="member-name-link">getChiselContextPreviewRendererRegistry</a>()</code></td><td><div class="block">Gives access to the chisel context preview renderer registry.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/IChiselingManager.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingManager</a></code></td><td><code><a href="#getChiselingManager()" class="member-name-link">getChiselingManager</a>()</code></td><td><div class="block">Gives access to the manager which controls chiseling operations.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/variant/state/IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></code></td><td><code><a href="#getClientStateVariantManager()" class="member-name-link">getClientStateVariantManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="config/IChiselsAndBitsConfiguration.html" title="interface in mod.chiselsandbits.api.config">IChiselsAndBitsConfiguration</a></code></td><td><code><a href="#getConfiguration()" class="member-name-link">getConfiguration</a>()</code></td><td><div class="block">The configuration on top of which chisels and bits is running.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/conversion/IConversionManager.html" title="interface in mod.chiselsandbits.api.chiseling.conversion">IConversionManager</a></code></td><td><code><a href="#getConversionManager()" class="member-name-link">getConversionManager</a>()</code></td><td><div class="block">Manager which deals with converting eligible blocks, blockstates and IItemProviders into their chiseled<br>variants.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/clipboard/ICreativeClipboardManager.html" title="interface in mod.chiselsandbits.api.client.clipboard">ICreativeClipboardManager</a></code></td><td><code><a href="#getCreativeClipboardManager()" class="member-name-link">getCreativeClipboardManager</a>()</code></td><td><div class="block">Returns the clipboard manager for the creative clipboard.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></code></td><td><code><a href="#getDefaultChiselMode()" class="member-name-link">getDefaultChiselMode</a>()</code></td><td><div class="block">Represents the default mode for the chiseling system.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="cutting/operation/ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a></code></td><td><code><a href="#getDefaultCuttingOperation()" class="member-name-link">getDefaultCuttingOperation</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="glueing/operation/IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a></code></td><td><code><a href="#getDefaultGlueingOperation()" class="member-name-link">getDefaultGlueingOperation</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a></code></td><td><code><a href="#getDefaultModificationOperation()" class="member-name-link">getDefaultModificationOperation</a>()</code></td><td><div class="block">The default mode for performing modification operations if no other is supplied.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/eligibility/IEligibilityManager.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityManager</a></code></td><td><code><a href="#getEligibilityManager()" class="member-name-link">getEligibilityManager</a>()</code></td><td><div class="block">Manager which deals with chiseling eligibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/eligibility/IEligibilityOptions.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityOptions</a></code></td><td><code><a href="#getEligibilityOptions()" class="member-name-link">getEligibilityOptions</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.tags.TagKey<wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getForcedTag()" class="member-name-link">getForcedTag</a>()</code></td><td><div class="block">Returns the tag used in the eligibility system to force compatibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/icon/IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></code></td><td><code><a href="#getIconManager()" class="member-name-link">getIconManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the api instance.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="launch/ILaunchPropertyManager.html" title="interface in mod.chiselsandbits.api.launch">ILaunchPropertyManager</a></code></td><td><code><a href="#getLaunchPropertyManager()" class="member-name-link">getLaunchPropertyManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="chiseling/ILocalChiselingContextCache.html" title="interface in mod.chiselsandbits.api.chiseling">ILocalChiselingContextCache</a></code></td><td><code><a href="#getLocalChiselingContextCache()" class="member-name-link">getLocalChiselingContextCache</a>()</code></td><td><div class="block">This method gives access to the client side local chiseling context cache.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="measuring/IMeasuringManager.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringManager</a></code></td><td><code><a href="#getMeasuringManager()" class="member-name-link">getMeasuringManager</a>()</code></td><td><div class="block">The measuring manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="item/multistate/IMultiStateItemFactory.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemFactory</a></code></td><td><code><a href="#getMultiStateItemFactory()" class="member-name-link">getMultiStateItemFactory</a>()</code></td><td><div class="block">A factory which can produce a multistate item from a given source.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="multistate/mutator/IMutatorFactory.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutatorFactory</a></code></td><td><code><a href="#getMutatorFactory()" class="member-name-link">getMutatorFactory</a>()</code></td><td><div class="block">Gives access to the factory that can produce different mutators.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="notifications/INotificationManager.html" title="interface in mod.chiselsandbits.api.notifications">INotificationManager</a></code></td><td><code><a href="#getNotificationManager()" class="member-name-link">getNotificationManager</a>()</code></td><td><div class="block">Handles showing notifications to the player.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/sharing/IPatternSharingManager.html" title="interface in mod.chiselsandbits.api.client.sharing">IPatternSharingManager</a></code></td><td><code><a href="#getPatternSharingManager()" class="member-name-link">getPatternSharingManager</a>()</code></td><td><div class="block">The pattern sharing manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="permissions/IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionHandler</a></code></td><td><code><a href="#getPermissionHandler()" class="member-name-link">getPermissionHandler</a>()</code></td><td><div class="block">Returns the permission handler which is used to check if a particular area<br>is chiselable or not.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="plugin/IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></code></td><td><code><a href="#getPluginDiscoverer()" class="member-name-link">getPluginDiscoverer</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="plugin/IPluginManager.html" title="interface in mod.chiselsandbits.api.plugin">IPluginManager</a></code></td><td><code><a href="#getPluginManager()" class="member-name-link">getPluginManager</a>()</code></td><td><div class="block">Gives access to the plugin manager that is used to process chisels and bits plugins</div><br></td></tr>
  <tr><td><code>@NotNull <a href="profiling/IProfilingManager.html" title="interface in mod.chiselsandbits.api.profiling">IProfilingManager</a></code></td><td><code><a href="#getProfilingManager()" class="member-name-link">getProfilingManager</a>()</code></td><td><div class="block">The profiling manager, allows for the profiling of operations related Chisels and Bits.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="registries/IRegistryManager.html" title="interface in mod.chiselsandbits.api.registries">IRegistryManager</a></code></td><td><code><a href="#getRegistryManager()" class="member-name-link">getRegistryManager</a>()</code></td><td><div class="block">Gives access to all registries which are used by chisels and bits.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/tool/mode/icon/ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></code></td><td><code><a href="#getSelectedToolModeIconRenderer()" class="member-name-link">getSelectedToolModeIconRenderer</a>()</code></td><td><div class="block">Gives access to the selected tool mode icon renderer registry.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="multistate/snapshot/ISnapshotFactory.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">ISnapshotFactory</a></code></td><td><code><a href="#getSnapshotFactory()" class="member-name-link">getSnapshotFactory</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default @NotNull <a href="multistate/StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#getStateEntrySize()" class="member-name-link">getStateEntrySize</a>()</code></td><td><div class="block">Represents the size of the bits in the current instance.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="variant/state/IStateVariantManager.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariantManager</a></code></td><td><code><a href="#getStateVariantManager()" class="member-name-link">getStateVariantManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="voxelshape/IVoxelShapeManager.html" title="interface in mod.chiselsandbits.api.voxelshape">IVoxelShapeManager</a></code></td><td><code><a href="#getVoxelShapeManager()" class="member-name-link">getVoxelShapeManager</a>()</code></td><td><div class="block">Manager which deals with calculating, and optionally caching, the voxel shapes, which<br>can be constructed from a given area.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the api instance.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="multistate/accessor/IAccessorFactory.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAccessorFactory</a></code></td><td><code><a href="#getAccessorFactory()" class="member-name-link">getAccessorFactory</a>()</code></td><td><div class="block">Gives access to the factory that can produce different accessors.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="inventory/bit/IAdaptingBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.bit">IAdaptingBitInventoryManager</a></code></td><td><code><a href="#getAdaptingBitInventoryManager()" class="member-name-link">getAdaptingBitInventoryManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="inventory/management/IBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.management">IBitInventoryManager</a></code></td><td><code><a href="#getBitInventoryManager()" class="member-name-link">getBitInventoryManager</a>()</code></td><td><div class="block">Gives access to the bits inventory manager, which allows the conversion of normal inventory systems to bit inventories.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="item/bit/IBitItemManager.html" title="interface in mod.chiselsandbits.api.item.bit">IBitItemManager</a></code></td><td><code><a href="#getBitItemManager()" class="member-name-link">getBitItemManager</a>()</code></td><td><div class="block">The bit item manager.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.tags.TagKey<wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getBlockedTag()" class="member-name-link">getBlockedTag</a>()</code></td><td><div class="block">Returns the tag used in the eligibility system to block compatibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="neighborhood/IBlockNeighborhoodBuilder.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhoodBuilder</a></code></td><td><code><a href="#getBlockNeighborhoodBuilder()" class="member-name-link">getBlockNeighborhoodBuilder</a>()</code></td><td><div class="block">Gives access to the block neighborhood builder.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="block/state/id/IBlockStateIdManager.html" title="interface in mod.chiselsandbits.api.block.state.id">IBlockStateIdManager</a></code></td><td><code><a href="#getBlockStateIdManager()" class="member-name-link">getBlockStateIdManager</a>()</code></td><td><div class="block">The manager which deals with calculating the given blockstate ids in the current running session.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="change/IChangeTrackerManager.html" title="interface in mod.chiselsandbits.api.change">IChangeTrackerManager</a></code></td><td><code><a href="#getChangeTrackerManager()" class="member-name-link">getChangeTrackerManager</a>()</code></td><td><div class="block">The change tracker manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/render/preview/chiseling/IChiselContextPreviewRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.render.preview.chiseling">IChiselContextPreviewRendererRegistry</a></code></td><td><code><a href="#getChiselContextPreviewRendererRegistry()" class="member-name-link">getChiselContextPreviewRendererRegistry</a>()</code></td><td><div class="block">Gives access to the chisel context preview renderer registry.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/IChiselingManager.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingManager</a></code></td><td><code><a href="#getChiselingManager()" class="member-name-link">getChiselingManager</a>()</code></td><td><div class="block">Gives access to the manager which controls chiseling operations.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/variant/state/IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></code></td><td><code><a href="#getClientStateVariantManager()" class="member-name-link">getClientStateVariantManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="config/IChiselsAndBitsConfiguration.html" title="interface in mod.chiselsandbits.api.config">IChiselsAndBitsConfiguration</a></code></td><td><code><a href="#getConfiguration()" class="member-name-link">getConfiguration</a>()</code></td><td><div class="block">The configuration on top of which chisels and bits is running.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/conversion/IConversionManager.html" title="interface in mod.chiselsandbits.api.chiseling.conversion">IConversionManager</a></code></td><td><code><a href="#getConversionManager()" class="member-name-link">getConversionManager</a>()</code></td><td><div class="block">Manager which deals with converting eligible blocks, blockstates and IItemProviders into their chiseled<br>variants.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/clipboard/ICreativeClipboardManager.html" title="interface in mod.chiselsandbits.api.client.clipboard">ICreativeClipboardManager</a></code></td><td><code><a href="#getCreativeClipboardManager()" class="member-name-link">getCreativeClipboardManager</a>()</code></td><td><div class="block">Returns the clipboard manager for the creative clipboard.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></code></td><td><code><a href="#getDefaultChiselMode()" class="member-name-link">getDefaultChiselMode</a>()</code></td><td><div class="block">Represents the default mode for the chiseling system.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="cutting/operation/ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a></code></td><td><code><a href="#getDefaultCuttingOperation()" class="member-name-link">getDefaultCuttingOperation</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="glueing/operation/IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a></code></td><td><code><a href="#getDefaultGlueingOperation()" class="member-name-link">getDefaultGlueingOperation</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a></code></td><td><code><a href="#getDefaultModificationOperation()" class="member-name-link">getDefaultModificationOperation</a>()</code></td><td><div class="block">The default mode for performing modification operations if no other is supplied.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/eligibility/IEligibilityManager.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityManager</a></code></td><td><code><a href="#getEligibilityManager()" class="member-name-link">getEligibilityManager</a>()</code></td><td><div class="block">Manager which deals with chiseling eligibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/eligibility/IEligibilityOptions.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityOptions</a></code></td><td><code><a href="#getEligibilityOptions()" class="member-name-link">getEligibilityOptions</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.tags.TagKey<wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getForcedTag()" class="member-name-link">getForcedTag</a>()</code></td><td><div class="block">Returns the tag used in the eligibility system to force compatibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/icon/IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></code></td><td><code><a href="#getIconManager()" class="member-name-link">getIconManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="launch/ILaunchPropertyManager.html" title="interface in mod.chiselsandbits.api.launch">ILaunchPropertyManager</a></code></td><td><code><a href="#getLaunchPropertyManager()" class="member-name-link">getLaunchPropertyManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="chiseling/ILocalChiselingContextCache.html" title="interface in mod.chiselsandbits.api.chiseling">ILocalChiselingContextCache</a></code></td><td><code><a href="#getLocalChiselingContextCache()" class="member-name-link">getLocalChiselingContextCache</a>()</code></td><td><div class="block">This method gives access to the client side local chiseling context cache.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="measuring/IMeasuringManager.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringManager</a></code></td><td><code><a href="#getMeasuringManager()" class="member-name-link">getMeasuringManager</a>()</code></td><td><div class="block">The measuring manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="item/multistate/IMultiStateItemFactory.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemFactory</a></code></td><td><code><a href="#getMultiStateItemFactory()" class="member-name-link">getMultiStateItemFactory</a>()</code></td><td><div class="block">A factory which can produce a multistate item from a given source.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="multistate/mutator/IMutatorFactory.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutatorFactory</a></code></td><td><code><a href="#getMutatorFactory()" class="member-name-link">getMutatorFactory</a>()</code></td><td><div class="block">Gives access to the factory that can produce different mutators.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="notifications/INotificationManager.html" title="interface in mod.chiselsandbits.api.notifications">INotificationManager</a></code></td><td><code><a href="#getNotificationManager()" class="member-name-link">getNotificationManager</a>()</code></td><td><div class="block">Handles showing notifications to the player.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/sharing/IPatternSharingManager.html" title="interface in mod.chiselsandbits.api.client.sharing">IPatternSharingManager</a></code></td><td><code><a href="#getPatternSharingManager()" class="member-name-link">getPatternSharingManager</a>()</code></td><td><div class="block">The pattern sharing manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="permissions/IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionHandler</a></code></td><td><code><a href="#getPermissionHandler()" class="member-name-link">getPermissionHandler</a>()</code></td><td><div class="block">Returns the permission handler which is used to check if a particular area<br>is chiselable or not.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="plugin/IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></code></td><td><code><a href="#getPluginDiscoverer()" class="member-name-link">getPluginDiscoverer</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="plugin/IPluginManager.html" title="interface in mod.chiselsandbits.api.plugin">IPluginManager</a></code></td><td><code><a href="#getPluginManager()" class="member-name-link">getPluginManager</a>()</code></td><td><div class="block">Gives access to the plugin manager that is used to process chisels and bits plugins</div><br></td></tr>
  <tr><td><code>@NotNull <a href="profiling/IProfilingManager.html" title="interface in mod.chiselsandbits.api.profiling">IProfilingManager</a></code></td><td><code><a href="#getProfilingManager()" class="member-name-link">getProfilingManager</a>()</code></td><td><div class="block">The profiling manager, allows for the profiling of operations related Chisels and Bits.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="registries/IRegistryManager.html" title="interface in mod.chiselsandbits.api.registries">IRegistryManager</a></code></td><td><code><a href="#getRegistryManager()" class="member-name-link">getRegistryManager</a>()</code></td><td><div class="block">Gives access to all registries which are used by chisels and bits.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/tool/mode/icon/ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></code></td><td><code><a href="#getSelectedToolModeIconRenderer()" class="member-name-link">getSelectedToolModeIconRenderer</a>()</code></td><td><div class="block">Gives access to the selected tool mode icon renderer registry.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="multistate/snapshot/ISnapshotFactory.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">ISnapshotFactory</a></code></td><td><code><a href="#getSnapshotFactory()" class="member-name-link">getSnapshotFactory</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default @NotNull <a href="multistate/StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#getStateEntrySize()" class="member-name-link">getStateEntrySize</a>()</code></td><td><div class="block">Represents the size of the bits in the current instance.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="variant/state/IStateVariantManager.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariantManager</a></code></td><td><code><a href="#getStateVariantManager()" class="member-name-link">getStateVariantManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="voxelshape/IVoxelShapeManager.html" title="interface in mod.chiselsandbits.api.voxelshape">IVoxelShapeManager</a></code></td><td><code><a href="#getVoxelShapeManager()" class="member-name-link">getVoxelShapeManager</a>()</code></td><td><div class="block">Manager which deals with calculating, and optionally caching, the voxel shapes, which<br>can be constructed from a given area.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="multistate/accessor/IAccessorFactory.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAccessorFactory</a></code></td><td><code><a href="#getAccessorFactory()" class="member-name-link">getAccessorFactory</a>()</code></td><td><div class="block">Gives access to the factory that can produce different accessors.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="inventory/bit/IAdaptingBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.bit">IAdaptingBitInventoryManager</a></code></td><td><code><a href="#getAdaptingBitInventoryManager()" class="member-name-link">getAdaptingBitInventoryManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="inventory/management/IBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.management">IBitInventoryManager</a></code></td><td><code><a href="#getBitInventoryManager()" class="member-name-link">getBitInventoryManager</a>()</code></td><td><div class="block">Gives access to the bits inventory manager, which allows the conversion of normal inventory systems to bit inventories.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="item/bit/IBitItemManager.html" title="interface in mod.chiselsandbits.api.item.bit">IBitItemManager</a></code></td><td><code><a href="#getBitItemManager()" class="member-name-link">getBitItemManager</a>()</code></td><td><div class="block">The bit item manager.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.tags.TagKey<wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getBlockedTag()" class="member-name-link">getBlockedTag</a>()</code></td><td><div class="block">Returns the tag used in the eligibility system to block compatibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="neighborhood/IBlockNeighborhoodBuilder.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhoodBuilder</a></code></td><td><code><a href="#getBlockNeighborhoodBuilder()" class="member-name-link">getBlockNeighborhoodBuilder</a>()</code></td><td><div class="block">Gives access to the block neighborhood builder.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="block/state/id/IBlockStateIdManager.html" title="interface in mod.chiselsandbits.api.block.state.id">IBlockStateIdManager</a></code></td><td><code><a href="#getBlockStateIdManager()" class="member-name-link">getBlockStateIdManager</a>()</code></td><td><div class="block">The manager which deals with calculating the given blockstate ids in the current running session.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="change/IChangeTrackerManager.html" title="interface in mod.chiselsandbits.api.change">IChangeTrackerManager</a></code></td><td><code><a href="#getChangeTrackerManager()" class="member-name-link">getChangeTrackerManager</a>()</code></td><td><div class="block">The change tracker manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/render/preview/chiseling/IChiselContextPreviewRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.render.preview.chiseling">IChiselContextPreviewRendererRegistry</a></code></td><td><code><a href="#getChiselContextPreviewRendererRegistry()" class="member-name-link">getChiselContextPreviewRendererRegistry</a>()</code></td><td><div class="block">Gives access to the chisel context preview renderer registry.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/IChiselingManager.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingManager</a></code></td><td><code><a href="#getChiselingManager()" class="member-name-link">getChiselingManager</a>()</code></td><td><div class="block">Gives access to the manager which controls chiseling operations.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/variant/state/IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></code></td><td><code><a href="#getClientStateVariantManager()" class="member-name-link">getClientStateVariantManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="config/IChiselsAndBitsConfiguration.html" title="interface in mod.chiselsandbits.api.config">IChiselsAndBitsConfiguration</a></code></td><td><code><a href="#getConfiguration()" class="member-name-link">getConfiguration</a>()</code></td><td><div class="block">The configuration on top of which chisels and bits is running.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/conversion/IConversionManager.html" title="interface in mod.chiselsandbits.api.chiseling.conversion">IConversionManager</a></code></td><td><code><a href="#getConversionManager()" class="member-name-link">getConversionManager</a>()</code></td><td><div class="block">Manager which deals with converting eligible blocks, blockstates and IItemProviders into their chiseled<br>variants.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/clipboard/ICreativeClipboardManager.html" title="interface in mod.chiselsandbits.api.client.clipboard">ICreativeClipboardManager</a></code></td><td><code><a href="#getCreativeClipboardManager()" class="member-name-link">getCreativeClipboardManager</a>()</code></td><td><div class="block">Returns the clipboard manager for the creative clipboard.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></code></td><td><code><a href="#getDefaultChiselMode()" class="member-name-link">getDefaultChiselMode</a>()</code></td><td><div class="block">Represents the default mode for the chiseling system.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="cutting/operation/ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a></code></td><td><code><a href="#getDefaultCuttingOperation()" class="member-name-link">getDefaultCuttingOperation</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="glueing/operation/IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a></code></td><td><code><a href="#getDefaultGlueingOperation()" class="member-name-link">getDefaultGlueingOperation</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a></code></td><td><code><a href="#getDefaultModificationOperation()" class="member-name-link">getDefaultModificationOperation</a>()</code></td><td><div class="block">The default mode for performing modification operations if no other is supplied.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/eligibility/IEligibilityManager.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityManager</a></code></td><td><code><a href="#getEligibilityManager()" class="member-name-link">getEligibilityManager</a>()</code></td><td><div class="block">Manager which deals with chiseling eligibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="chiseling/eligibility/IEligibilityOptions.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityOptions</a></code></td><td><code><a href="#getEligibilityOptions()" class="member-name-link">getEligibilityOptions</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.tags.TagKey<wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getForcedTag()" class="member-name-link">getForcedTag</a>()</code></td><td><div class="block">Returns the tag used in the eligibility system to force compatibility.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/icon/IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></code></td><td><code><a href="#getIconManager()" class="member-name-link">getIconManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="launch/ILaunchPropertyManager.html" title="interface in mod.chiselsandbits.api.launch">ILaunchPropertyManager</a></code></td><td><code><a href="#getLaunchPropertyManager()" class="member-name-link">getLaunchPropertyManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="chiseling/ILocalChiselingContextCache.html" title="interface in mod.chiselsandbits.api.chiseling">ILocalChiselingContextCache</a></code></td><td><code><a href="#getLocalChiselingContextCache()" class="member-name-link">getLocalChiselingContextCache</a>()</code></td><td><div class="block">This method gives access to the client side local chiseling context cache.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="measuring/IMeasuringManager.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringManager</a></code></td><td><code><a href="#getMeasuringManager()" class="member-name-link">getMeasuringManager</a>()</code></td><td><div class="block">The measuring manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="item/multistate/IMultiStateItemFactory.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemFactory</a></code></td><td><code><a href="#getMultiStateItemFactory()" class="member-name-link">getMultiStateItemFactory</a>()</code></td><td><div class="block">A factory which can produce a multistate item from a given source.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="multistate/mutator/IMutatorFactory.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutatorFactory</a></code></td><td><code><a href="#getMutatorFactory()" class="member-name-link">getMutatorFactory</a>()</code></td><td><div class="block">Gives access to the factory that can produce different mutators.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="notifications/INotificationManager.html" title="interface in mod.chiselsandbits.api.notifications">INotificationManager</a></code></td><td><code><a href="#getNotificationManager()" class="member-name-link">getNotificationManager</a>()</code></td><td><div class="block">Handles showing notifications to the player.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/sharing/IPatternSharingManager.html" title="interface in mod.chiselsandbits.api.client.sharing">IPatternSharingManager</a></code></td><td><code><a href="#getPatternSharingManager()" class="member-name-link">getPatternSharingManager</a>()</code></td><td><div class="block">The pattern sharing manager.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="permissions/IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionHandler</a></code></td><td><code><a href="#getPermissionHandler()" class="member-name-link">getPermissionHandler</a>()</code></td><td><div class="block">Returns the permission handler which is used to check if a particular area<br>is chiselable or not.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="plugin/IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></code></td><td><code><a href="#getPluginDiscoverer()" class="member-name-link">getPluginDiscoverer</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="plugin/IPluginManager.html" title="interface in mod.chiselsandbits.api.plugin">IPluginManager</a></code></td><td><code><a href="#getPluginManager()" class="member-name-link">getPluginManager</a>()</code></td><td><div class="block">Gives access to the plugin manager that is used to process chisels and bits plugins</div><br></td></tr>
  <tr><td><code>@NotNull <a href="profiling/IProfilingManager.html" title="interface in mod.chiselsandbits.api.profiling">IProfilingManager</a></code></td><td><code><a href="#getProfilingManager()" class="member-name-link">getProfilingManager</a>()</code></td><td><div class="block">The profiling manager, allows for the profiling of operations related Chisels and Bits.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="registries/IRegistryManager.html" title="interface in mod.chiselsandbits.api.registries">IRegistryManager</a></code></td><td><code><a href="#getRegistryManager()" class="member-name-link">getRegistryManager</a>()</code></td><td><div class="block">Gives access to all registries which are used by chisels and bits.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="client/tool/mode/icon/ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></code></td><td><code><a href="#getSelectedToolModeIconRenderer()" class="member-name-link">getSelectedToolModeIconRenderer</a>()</code></td><td><div class="block">Gives access to the selected tool mode icon renderer registry.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="multistate/snapshot/ISnapshotFactory.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">ISnapshotFactory</a></code></td><td><code><a href="#getSnapshotFactory()" class="member-name-link">getSnapshotFactory</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="variant/state/IStateVariantManager.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariantManager</a></code></td><td><code><a href="#getStateVariantManager()" class="member-name-link">getStateVariantManager</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull <a href="voxelshape/IVoxelShapeManager.html" title="interface in mod.chiselsandbits.api.voxelshape">IVoxelShapeManager</a></code></td><td><code><a href="#getVoxelShapeManager()" class="member-name-link">getVoxelShapeManager</a>()</code></td><td><div class="block">Manager which deals with calculating, and optionally caching, the voxel shapes, which<br>can be constructed from a given area.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default @NotNull <a href="multistate/StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#getStateEntrySize()" class="member-name-link">getStateEntrySize</a>()</code></td><td><div class="block">Represents the size of the bits in the current instance.</div><br></td></tr>
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
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IChiselsAndBitsAPI.html" title="interface in mod.chiselsandbits.api">IChiselsAndBitsAPI</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">Gives access to the api instance.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The api.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getAccessorFactory()">

:::tabs
== getAccessorFactory
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="multistate/accessor/IAccessorFactory.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAccessorFactory</a></span>&nbsp;<span class="element-name">getAccessorFactory</span>()</div>
<div class="block">Gives access to the factory that can produce different accessors.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The factory used to create new accessors.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getMutatorFactory()">

:::tabs
== getMutatorFactory
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="multistate/mutator/IMutatorFactory.html" title="interface in mod.chiselsandbits.api.multistate.mutator">IMutatorFactory</a></span>&nbsp;<span class="element-name">getMutatorFactory</span>()</div>
<div class="block">Gives access to the factory that can produce different mutators.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The factory used to create new mutators.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getEligibilityManager()">

:::tabs
== getEligibilityManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="chiseling/eligibility/IEligibilityManager.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityManager</a></span>&nbsp;<span class="element-name">getEligibilityManager</span>()</div>
<div class="block">Manager which deals with chiseling eligibility.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getConversionManager()">

:::tabs
== getConversionManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="chiseling/conversion/IConversionManager.html" title="interface in mod.chiselsandbits.api.chiseling.conversion">IConversionManager</a></span>&nbsp;<span class="element-name">getConversionManager</span>()</div>
<div class="block">Manager which deals with converting eligible blocks, blockstates and IItemProviders into their chiseled
variants.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The conversion manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getVoxelShapeManager()">

:::tabs
== getVoxelShapeManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="voxelshape/IVoxelShapeManager.html" title="interface in mod.chiselsandbits.api.voxelshape">IVoxelShapeManager</a></span>&nbsp;<span class="element-name">getVoxelShapeManager</span>()</div>
<div class="block">Manager which deals with calculating, and optionally caching, the voxel shapes, which
can be constructed from a given area.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The voxel shape manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getMultiStateItemFactory()">

:::tabs
== getMultiStateItemFactory
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="item/multistate/IMultiStateItemFactory.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemFactory</a></span>&nbsp;<span class="element-name">getMultiStateItemFactory</span>()</div>
<div class="block">A factory which can produce a multistate item from a given source.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The factory.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getDefaultChiselMode()">

:::tabs
== getDefaultChiselMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="chiseling/mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></span>&nbsp;<span class="element-name">getDefaultChiselMode</span>()</div>
<div class="block">Represents the default mode for the chiseling system.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The default mode.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getRegistryManager()">

:::tabs
== getRegistryManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="registries/IRegistryManager.html" title="interface in mod.chiselsandbits.api.registries">IRegistryManager</a></span>&nbsp;<span class="element-name">getRegistryManager</span>()</div>
<div class="block">Gives access to all registries which are used by chisels and bits.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The manager for registries used by chisels and bits.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getChiselingManager()">

:::tabs
== getChiselingManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="chiseling/IChiselingManager.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingManager</a></span>&nbsp;<span class="element-name">getChiselingManager</span>()</div>
<div class="block">Gives access to the manager which controls chiseling operations.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The current chiseling manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getConfiguration()">

:::tabs
== getConfiguration
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="config/IChiselsAndBitsConfiguration.html" title="interface in mod.chiselsandbits.api.config">IChiselsAndBitsConfiguration</a></span>&nbsp;<span class="element-name">getConfiguration</span>()</div>
<div class="block">The configuration on top of which chisels and bits is running.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The current configuration.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getBlockStateIdManager()">

:::tabs
== getBlockStateIdManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="block/state/id/IBlockStateIdManager.html" title="interface in mod.chiselsandbits.api.block.state.id">IBlockStateIdManager</a></span>&nbsp;<span class="element-name">getBlockStateIdManager</span>()</div>
<div class="block">The manager which deals with calculating the given blockstate ids in the current running session.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The blockstate id manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getBitInventoryManager()">

:::tabs
== getBitInventoryManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="inventory/management/IBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.management">IBitInventoryManager</a></span>&nbsp;<span class="element-name">getBitInventoryManager</span>()</div>
<div class="block">Gives access to the bits inventory manager, which allows the conversion of normal inventory systems to bit inventories.
These special bit inventories respect the core interfaces that make up an object that can hold or is a bit.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The manager for dealing with bits.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getBitItemManager()">

:::tabs
== getBitItemManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="item/bit/IBitItemManager.html" title="interface in mod.chiselsandbits.api.item.bit">IBitItemManager</a></span>&nbsp;<span class="element-name">getBitItemManager</span>()</div>
<div class="block">The bit item manager.
Allows for the creation of bit based itemstacks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The bit item manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getMeasuringManager()">

:::tabs
== getMeasuringManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="measuring/IMeasuringManager.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringManager</a></span>&nbsp;<span class="element-name">getMeasuringManager</span>()</div>
<div class="block">The measuring manager.
Gives access to measurements created by a given player.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The measuring manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getStateEntrySize()">

:::tabs
== getStateEntrySize
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">default</span>&nbsp;<span class="return-type">@NotNull <a href="multistate/StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></span>&nbsp;<span class="element-name">getStateEntrySize</span>()</div>
<div class="block">Represents the size of the bits in the current instance.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The size of the state entries in the current instance.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getProfilingManager()">

:::tabs
== getProfilingManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="profiling/IProfilingManager.html" title="interface in mod.chiselsandbits.api.profiling">IProfilingManager</a></span>&nbsp;<span class="element-name">getProfilingManager</span>()</div>
<div class="block">The profiling manager, allows for the profiling of operations related Chisels and Bits.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The profiling manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getLocalChiselingContextCache()">

:::tabs
== getLocalChiselingContextCache
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="chiseling/ILocalChiselingContextCache.html" title="interface in mod.chiselsandbits.api.chiseling">ILocalChiselingContextCache</a></span>&nbsp;<span class="element-name">getLocalChiselingContextCache</span>()</div>
<div class="block">This method gives access to the client side local chiseling context cache.
Although this method also exists on the server side, it should be considered a cross tick cache for the latest chiseling context in use by the current player,
without it becoming the active context for that player.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The <a href="chiseling/ILocalChiselingContextCache.html" title="interface in mod.chiselsandbits.api.chiseling"><code>ILocalChiselingContextCache</code></a>.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getChangeTrackerManager()">

:::tabs
== getChangeTrackerManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="change/IChangeTrackerManager.html" title="interface in mod.chiselsandbits.api.change">IChangeTrackerManager</a></span>&nbsp;<span class="element-name">getChangeTrackerManager</span>()</div>
<div class="block">The change tracker manager.
Gives access to each players change tracker.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The change tracker manager</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getBlockNeighborhoodBuilder()">

:::tabs
== getBlockNeighborhoodBuilder
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="neighborhood/IBlockNeighborhoodBuilder.html" title="interface in mod.chiselsandbits.api.neighborhood">IBlockNeighborhoodBuilder</a></span>&nbsp;<span class="element-name">getBlockNeighborhoodBuilder</span>()</div>
<div class="block">Gives access to the block neighborhood builder.
Allows for building block specific cache keys when the block environment is required.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The block neighborhood builder.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getDefaultModificationOperation()">

:::tabs
== getDefaultModificationOperation
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="modification/operation/IModificationOperation.html" title="interface in mod.chiselsandbits.api.modification.operation">IModificationOperation</a></span>&nbsp;<span class="element-name">getDefaultModificationOperation</span>()</div>
<div class="block">The default mode for performing modification operations if no other is supplied.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The default modification operation.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getPluginManager()">

:::tabs
== getPluginManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="plugin/IPluginManager.html" title="interface in mod.chiselsandbits.api.plugin">IPluginManager</a></span>&nbsp;<span class="element-name">getPluginManager</span>()</div>
<div class="block">Gives access to the plugin manager that is used to process chisels and bits plugins</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The plugin manager</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getChiselContextPreviewRendererRegistry()">

:::tabs
== getChiselContextPreviewRendererRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="client/render/preview/chiseling/IChiselContextPreviewRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.render.preview.chiseling">IChiselContextPreviewRendererRegistry</a></span>&nbsp;<span class="element-name">getChiselContextPreviewRendererRegistry</span>()</div>
<div class="block">Gives access to the chisel context preview renderer registry.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The registry.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getSelectedToolModeIconRenderer()">

:::tabs
== getSelectedToolModeIconRenderer
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="client/tool/mode/icon/ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></span>&nbsp;<span class="element-name">getSelectedToolModeIconRenderer</span>()</div>
<div class="block">Gives access to the selected tool mode icon renderer registry.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The registry.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getForcedTag()">

:::tabs
== getForcedTag
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.tags.TagKey&lt;net.minecraft.world.level.block.Block&gt;</span>&nbsp;<span class="element-name">getForcedTag</span>()</div>
<div class="block">Returns the tag used in the eligibility system to force compatibility.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The forced compatibility tag.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getBlockedTag()">

:::tabs
== getBlockedTag
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.tags.TagKey&lt;net.minecraft.world.level.block.Block&gt;</span>&nbsp;<span class="element-name">getBlockedTag</span>()</div>
<div class="block">Returns the tag used in the eligibility system to block compatibility.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The blocked compatibility tag.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getPermissionHandler()">

:::tabs
== getPermissionHandler
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="permissions/IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionHandler</a></span>&nbsp;<span class="element-name">getPermissionHandler</span>()</div>
<div class="block">Returns the permission handler which is used to check if a particular area
is chiselable or not.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The permission handler.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getCreativeClipboardManager()">

:::tabs
== getCreativeClipboardManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="client/clipboard/ICreativeClipboardManager.html" title="interface in mod.chiselsandbits.api.client.clipboard">ICreativeClipboardManager</a></span>&nbsp;<span class="element-name">getCreativeClipboardManager</span>()</div>
<div class="block">Returns the clipboard manager for the creative clipboard.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The clipboard manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getPatternSharingManager()">

:::tabs
== getPatternSharingManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="client/sharing/IPatternSharingManager.html" title="interface in mod.chiselsandbits.api.client.sharing">IPatternSharingManager</a></span>&nbsp;<span class="element-name">getPatternSharingManager</span>()</div>
<div class="block">The pattern sharing manager.
This manager only works on the client side, and will do nothing on the server side.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The pattern sharing manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getNotificationManager()">

:::tabs
== getNotificationManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="notifications/INotificationManager.html" title="interface in mod.chiselsandbits.api.notifications">INotificationManager</a></span>&nbsp;<span class="element-name">getNotificationManager</span>()</div>
<div class="block">Handles showing notifications to the player.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The notifications manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getStateVariantManager()">

:::tabs
== getStateVariantManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="variant/state/IStateVariantManager.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariantManager</a></span>&nbsp;<span class="element-name">getStateVariantManager</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getDefaultCuttingOperation()">

:::tabs
== getDefaultCuttingOperation
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="cutting/operation/ICuttingOperation.html" title="interface in mod.chiselsandbits.api.cutting.operation">ICuttingOperation</a></span>&nbsp;<span class="element-name">getDefaultCuttingOperation</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getDefaultGlueingOperation()">

:::tabs
== getDefaultGlueingOperation
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="glueing/operation/IGlueingOperation.html" title="interface in mod.chiselsandbits.api.glueing.operation">IGlueingOperation</a></span>&nbsp;<span class="element-name">getDefaultGlueingOperation</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getSnapshotFactory()">

:::tabs
== getSnapshotFactory
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="multistate/snapshot/ISnapshotFactory.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">ISnapshotFactory</a></span>&nbsp;<span class="element-name">getSnapshotFactory</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getEligibilityOptions()">

:::tabs
== getEligibilityOptions
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="chiseling/eligibility/IEligibilityOptions.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityOptions</a></span>&nbsp;<span class="element-name">getEligibilityOptions</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getAdaptingBitInventoryManager()">

:::tabs
== getAdaptingBitInventoryManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="inventory/bit/IAdaptingBitInventoryManager.html" title="interface in mod.chiselsandbits.api.inventory.bit">IAdaptingBitInventoryManager</a></span>&nbsp;<span class="element-name">getAdaptingBitInventoryManager</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getPluginDiscoverer()">

:::tabs
== getPluginDiscoverer
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="plugin/IPluginDiscoverer.html" title="interface in mod.chiselsandbits.api.plugin">IPluginDiscoverer</a></span>&nbsp;<span class="element-name">getPluginDiscoverer</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getClientStateVariantManager()">

:::tabs
== getClientStateVariantManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="client/variant/state/IClientStateVariantManager.html" title="interface in mod.chiselsandbits.api.client.variant.state">IClientStateVariantManager</a></span>&nbsp;<span class="element-name">getClientStateVariantManager</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getLaunchPropertyManager()">

:::tabs
== getLaunchPropertyManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="launch/ILaunchPropertyManager.html" title="interface in mod.chiselsandbits.api.launch">ILaunchPropertyManager</a></span>&nbsp;<span class="element-name">getLaunchPropertyManager</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getIconManager()">

:::tabs
== getIconManager
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="client/icon/IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></span>&nbsp;<span class="element-name">getIconManager</span>()</div>
</div>
:::


</section>

</li>
</ul>
:::::
  

