--- 
title: IClientConfiguration
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.config](index.md)  
# Interface IClientConfiguration  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IClientConfiguration</span></div>  

  

All client configuration values that are relevant for the client side of C&amp;B.

These options are only available on the client, and are not synced between
the server and the client.  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getBitStorageContentCacheSize()" class="member-name-link">getBitStorageContentCacheSize</a>()</code></td><td><div class="block">Indicates the size of the bit storage content model cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getClipboardSize()" class="member-name-link">getClipboardSize</a>()</code></td><td><div class="block">Indicates the amount of itemstacks that can be stored in the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getCullTestingCacheSize()" class="member-name-link">getCullTestingCacheSize</a>()</code></td><td><div class="block">Indicates the size of the cull testing cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableFaceLightmapExtraction()" class="member-name-link">getEnableFaceLightmapExtraction</a>()</code></td><td><div class="block">Indicates if the lightmap values of a face should be used to extract lighting information for a model.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableMouseIndicatorInRadialMenu()" class="member-name-link">getEnableMouseIndicatorInRadialMenu</a>()</code></td><td><div class="block">Indicates if a mouse indicator should be shown when the mouse is in a selection area in the radial menu.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getFaceLayerCacheSize()" class="member-name-link">getFaceLayerCacheSize</a>()</code></td><td><div class="block">Indicates how many faces should be kept in the face layer cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../client/render/preview/placement/PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</code></td><td><code><a href="#getFailedPlacementRenderMode()" class="member-name-link">getFailedPlacementRenderMode</a>()</code></td><td><div class="block">Determines the render mode used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code>static <a href="IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The client configuration.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getInvertBitBagFullness()" class="member-name-link">getInvertBitBagFullness</a>()</code></td><td><div class="block">Indicates if currently the bit bag fullness indication via the damage bar of the stack<br>shows fullness or emptiness.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getInvertPickBlockBehaviour()" class="member-name-link">getInvertPickBlockBehaviour</a>()</code></td><td><div class="block">Indicates if the block picking behaviour of chiseled blocks needs to be inverted.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getMissingBitsOrSpacePatternPlacementColor()" class="member-name-link">getMissingBitsOrSpacePatternPlacementColor</a>()</code></td><td><div class="block">Determines the color which indicates that the player is either missing bits, or does not have<br>enough space to pick up the bits.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getModelBuildingThreadCount()" class="member-name-link">getModelBuildingThreadCount</a>()</code></td><td><div class="block">Indicates how many threads should be used during building of the model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getModelCacheSize()" class="member-name-link">getModelCacheSize</a>()</code></td><td><div class="block">Indicates how many block models should be kept in the model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getMutatorPreviewChiselingColor()" class="member-name-link">getMutatorPreviewChiselingColor</a>()</code></td><td><div class="block">Determines the color used during debug rendering of the mutator area when chiseling.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getMutatorPreviewDebug()" class="member-name-link">getMutatorPreviewDebug</a>()</code></td><td><div class="block">Indicates if the preview rendering should run in debug mode.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getMutatorPreviewPlacementColor()" class="member-name-link">getMutatorPreviewPlacementColor</a>()</code></td><td><div class="block">Determines the color used during debug rendering of the mutator area when placing.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getNotFittingPatternPlacementColor()" class="member-name-link">getNotFittingPatternPlacementColor</a>()</code></td><td><div class="block">Determines the color used for pattern placement which does not fit on the targeted position.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getPatternExportPath()" class="member-name-link">getPatternExportPath</a>()</code></td><td><div class="block">Indicates the path where chisels and bits will export and import patterns from.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getPreviewChiselingColor()" class="member-name-link">getPreviewChiselingColor</a>()</code></td><td><div class="block">Provides the RGBA color channels for the color of the chiseling outline.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getPreviewPlacementColor()" class="member-name-link">getPreviewPlacementColor</a>()</code></td><td><div class="block">Provides the RGBA color channels for the color of the placement outline.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getPreviewRenderer()" class="member-name-link">getPreviewRenderer</a>()</code></td><td><div class="block">Indicates which preview renderer should be used.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getPrinterContentCacheSize()" class="member-name-link">getPrinterContentCacheSize</a>()</code></td><td><div class="block">Indicates the size of the printer content model cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldBrokenBlocksBeAddedToClipboard()" class="member-name-link">getShouldBrokenBlocksBeAddedToClipboard</a>()</code></td><td><div class="block">Indicates if a broken chiseled block should be added to the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldPickedBlocksBeAddedToClipboard()" class="member-name-link">getShouldPickedBlocksBeAddedToClipboard</a>()</code></td><td><div class="block">Indicates if a picked chiseled block should be added to the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldScrollInteractionsChangeMode()" class="member-name-link">getShouldScrollInteractionsChangeMode</a>()</code></td><td><div class="block">Indicates if a scroll interactions should change the mode of a held item.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShowCoolDownError()" class="member-name-link">getShowCoolDownError</a>()</code></td><td><div class="block">Indicates if an error notification should be shown when the player attempts to chisel during a cool down or not.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getStackModelCacheSize()" class="member-name-link">getStackModelCacheSize</a>()</code></td><td><div class="block">Indicates the size of the stack model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getSuccessfulPlacementColor()" class="member-name-link">getSuccessfulPlacementColor</a>()</code></td><td><div class="block">Determines the color used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../client/render/preview/placement/PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</code></td><td><code><a href="#getSuccessfulPlacementRenderMode()" class="member-name-link">getSuccessfulPlacementRenderMode</a>()</code></td><td><div class="block">Determines the render mode used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getToolModeRenderer()" class="member-name-link">getToolModeRenderer</a>()</code></td><td><div class="block">Indicates which tool mode renderer should be used.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getUseGetLightValue()" class="member-name-link">getUseGetLightValue</a>()</code></td><td><div class="block">Indicates if the light emission values of a block should be used to extract lighting information for a model.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The client configuration.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getBitStorageContentCacheSize()" class="member-name-link">getBitStorageContentCacheSize</a>()</code></td><td><div class="block">Indicates the size of the bit storage content model cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getClipboardSize()" class="member-name-link">getClipboardSize</a>()</code></td><td><div class="block">Indicates the amount of itemstacks that can be stored in the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getCullTestingCacheSize()" class="member-name-link">getCullTestingCacheSize</a>()</code></td><td><div class="block">Indicates the size of the cull testing cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableFaceLightmapExtraction()" class="member-name-link">getEnableFaceLightmapExtraction</a>()</code></td><td><div class="block">Indicates if the lightmap values of a face should be used to extract lighting information for a model.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableMouseIndicatorInRadialMenu()" class="member-name-link">getEnableMouseIndicatorInRadialMenu</a>()</code></td><td><div class="block">Indicates if a mouse indicator should be shown when the mouse is in a selection area in the radial menu.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getFaceLayerCacheSize()" class="member-name-link">getFaceLayerCacheSize</a>()</code></td><td><div class="block">Indicates how many faces should be kept in the face layer cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../client/render/preview/placement/PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</code></td><td><code><a href="#getFailedPlacementRenderMode()" class="member-name-link">getFailedPlacementRenderMode</a>()</code></td><td><div class="block">Determines the render mode used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getInvertBitBagFullness()" class="member-name-link">getInvertBitBagFullness</a>()</code></td><td><div class="block">Indicates if currently the bit bag fullness indication via the damage bar of the stack<br>shows fullness or emptiness.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getInvertPickBlockBehaviour()" class="member-name-link">getInvertPickBlockBehaviour</a>()</code></td><td><div class="block">Indicates if the block picking behaviour of chiseled blocks needs to be inverted.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getMissingBitsOrSpacePatternPlacementColor()" class="member-name-link">getMissingBitsOrSpacePatternPlacementColor</a>()</code></td><td><div class="block">Determines the color which indicates that the player is either missing bits, or does not have<br>enough space to pick up the bits.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getModelBuildingThreadCount()" class="member-name-link">getModelBuildingThreadCount</a>()</code></td><td><div class="block">Indicates how many threads should be used during building of the model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getModelCacheSize()" class="member-name-link">getModelCacheSize</a>()</code></td><td><div class="block">Indicates how many block models should be kept in the model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getMutatorPreviewChiselingColor()" class="member-name-link">getMutatorPreviewChiselingColor</a>()</code></td><td><div class="block">Determines the color used during debug rendering of the mutator area when chiseling.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getMutatorPreviewDebug()" class="member-name-link">getMutatorPreviewDebug</a>()</code></td><td><div class="block">Indicates if the preview rendering should run in debug mode.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getMutatorPreviewPlacementColor()" class="member-name-link">getMutatorPreviewPlacementColor</a>()</code></td><td><div class="block">Determines the color used during debug rendering of the mutator area when placing.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getNotFittingPatternPlacementColor()" class="member-name-link">getNotFittingPatternPlacementColor</a>()</code></td><td><div class="block">Determines the color used for pattern placement which does not fit on the targeted position.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getPatternExportPath()" class="member-name-link">getPatternExportPath</a>()</code></td><td><div class="block">Indicates the path where chisels and bits will export and import patterns from.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getPreviewChiselingColor()" class="member-name-link">getPreviewChiselingColor</a>()</code></td><td><div class="block">Provides the RGBA color channels for the color of the chiseling outline.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getPreviewPlacementColor()" class="member-name-link">getPreviewPlacementColor</a>()</code></td><td><div class="block">Provides the RGBA color channels for the color of the placement outline.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getPreviewRenderer()" class="member-name-link">getPreviewRenderer</a>()</code></td><td><div class="block">Indicates which preview renderer should be used.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getPrinterContentCacheSize()" class="member-name-link">getPrinterContentCacheSize</a>()</code></td><td><div class="block">Indicates the size of the printer content model cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldBrokenBlocksBeAddedToClipboard()" class="member-name-link">getShouldBrokenBlocksBeAddedToClipboard</a>()</code></td><td><div class="block">Indicates if a broken chiseled block should be added to the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldPickedBlocksBeAddedToClipboard()" class="member-name-link">getShouldPickedBlocksBeAddedToClipboard</a>()</code></td><td><div class="block">Indicates if a picked chiseled block should be added to the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldScrollInteractionsChangeMode()" class="member-name-link">getShouldScrollInteractionsChangeMode</a>()</code></td><td><div class="block">Indicates if a scroll interactions should change the mode of a held item.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShowCoolDownError()" class="member-name-link">getShowCoolDownError</a>()</code></td><td><div class="block">Indicates if an error notification should be shown when the player attempts to chisel during a cool down or not.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getStackModelCacheSize()" class="member-name-link">getStackModelCacheSize</a>()</code></td><td><div class="block">Indicates the size of the stack model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getSuccessfulPlacementColor()" class="member-name-link">getSuccessfulPlacementColor</a>()</code></td><td><div class="block">Determines the color used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../client/render/preview/placement/PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</code></td><td><code><a href="#getSuccessfulPlacementRenderMode()" class="member-name-link">getSuccessfulPlacementRenderMode</a>()</code></td><td><div class="block">Determines the render mode used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getToolModeRenderer()" class="member-name-link">getToolModeRenderer</a>()</code></td><td><div class="block">Indicates which tool mode renderer should be used.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getUseGetLightValue()" class="member-name-link">getUseGetLightValue</a>()</code></td><td><div class="block">Indicates if the light emission values of a block should be used to extract lighting information for a model.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getBitStorageContentCacheSize()" class="member-name-link">getBitStorageContentCacheSize</a>()</code></td><td><div class="block">Indicates the size of the bit storage content model cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getClipboardSize()" class="member-name-link">getClipboardSize</a>()</code></td><td><div class="block">Indicates the amount of itemstacks that can be stored in the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getCullTestingCacheSize()" class="member-name-link">getCullTestingCacheSize</a>()</code></td><td><div class="block">Indicates the size of the cull testing cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableFaceLightmapExtraction()" class="member-name-link">getEnableFaceLightmapExtraction</a>()</code></td><td><div class="block">Indicates if the lightmap values of a face should be used to extract lighting information for a model.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableMouseIndicatorInRadialMenu()" class="member-name-link">getEnableMouseIndicatorInRadialMenu</a>()</code></td><td><div class="block">Indicates if a mouse indicator should be shown when the mouse is in a selection area in the radial menu.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getFaceLayerCacheSize()" class="member-name-link">getFaceLayerCacheSize</a>()</code></td><td><div class="block">Indicates how many faces should be kept in the face layer cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../client/render/preview/placement/PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</code></td><td><code><a href="#getFailedPlacementRenderMode()" class="member-name-link">getFailedPlacementRenderMode</a>()</code></td><td><div class="block">Determines the render mode used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getInvertBitBagFullness()" class="member-name-link">getInvertBitBagFullness</a>()</code></td><td><div class="block">Indicates if currently the bit bag fullness indication via the damage bar of the stack<br>shows fullness or emptiness.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getInvertPickBlockBehaviour()" class="member-name-link">getInvertPickBlockBehaviour</a>()</code></td><td><div class="block">Indicates if the block picking behaviour of chiseled blocks needs to be inverted.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getMissingBitsOrSpacePatternPlacementColor()" class="member-name-link">getMissingBitsOrSpacePatternPlacementColor</a>()</code></td><td><div class="block">Determines the color which indicates that the player is either missing bits, or does not have<br>enough space to pick up the bits.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getModelBuildingThreadCount()" class="member-name-link">getModelBuildingThreadCount</a>()</code></td><td><div class="block">Indicates how many threads should be used during building of the model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getModelCacheSize()" class="member-name-link">getModelCacheSize</a>()</code></td><td><div class="block">Indicates how many block models should be kept in the model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getMutatorPreviewChiselingColor()" class="member-name-link">getMutatorPreviewChiselingColor</a>()</code></td><td><div class="block">Determines the color used during debug rendering of the mutator area when chiseling.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getMutatorPreviewDebug()" class="member-name-link">getMutatorPreviewDebug</a>()</code></td><td><div class="block">Indicates if the preview rendering should run in debug mode.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getMutatorPreviewPlacementColor()" class="member-name-link">getMutatorPreviewPlacementColor</a>()</code></td><td><div class="block">Determines the color used during debug rendering of the mutator area when placing.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getNotFittingPatternPlacementColor()" class="member-name-link">getNotFittingPatternPlacementColor</a>()</code></td><td><div class="block">Determines the color used for pattern placement which does not fit on the targeted position.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getPatternExportPath()" class="member-name-link">getPatternExportPath</a>()</code></td><td><div class="block">Indicates the path where chisels and bits will export and import patterns from.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getPreviewChiselingColor()" class="member-name-link">getPreviewChiselingColor</a>()</code></td><td><div class="block">Provides the RGBA color channels for the color of the chiseling outline.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</code></td><td><code><a href="#getPreviewPlacementColor()" class="member-name-link">getPreviewPlacementColor</a>()</code></td><td><div class="block">Provides the RGBA color channels for the color of the placement outline.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getPreviewRenderer()" class="member-name-link">getPreviewRenderer</a>()</code></td><td><div class="block">Indicates which preview renderer should be used.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getPrinterContentCacheSize()" class="member-name-link">getPrinterContentCacheSize</a>()</code></td><td><div class="block">Indicates the size of the printer content model cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldBrokenBlocksBeAddedToClipboard()" class="member-name-link">getShouldBrokenBlocksBeAddedToClipboard</a>()</code></td><td><div class="block">Indicates if a broken chiseled block should be added to the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldPickedBlocksBeAddedToClipboard()" class="member-name-link">getShouldPickedBlocksBeAddedToClipboard</a>()</code></td><td><div class="block">Indicates if a picked chiseled block should be added to the clipboard.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShouldScrollInteractionsChangeMode()" class="member-name-link">getShouldScrollInteractionsChangeMode</a>()</code></td><td><div class="block">Indicates if a scroll interactions should change the mode of a held item.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getShowCoolDownError()" class="member-name-link">getShowCoolDownError</a>()</code></td><td><div class="block">Indicates if an error notification should be shown when the player attempts to chisel during a cool down or not.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getStackModelCacheSize()" class="member-name-link">getStackModelCacheSize</a>()</code></td><td><div class="block">Indicates the size of the stack model cache.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;org.joml.Vector4f&gt;</code></td><td><code><a href="#getSuccessfulPlacementColor()" class="member-name-link">getSuccessfulPlacementColor</a>()</code></td><td><div class="block">Determines the color used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../client/render/preview/placement/PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</code></td><td><code><a href="#getSuccessfulPlacementRenderMode()" class="member-name-link">getSuccessfulPlacementRenderMode</a>()</code></td><td><div class="block">Determines the render mode used for successful pattern or chiseled block placement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</code></td><td><code><a href="#getToolModeRenderer()" class="member-name-link">getToolModeRenderer</a>()</code></td><td><div class="block">Indicates which tool mode renderer should be used.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getUseGetLightValue()" class="member-name-link">getUseGetLightValue</a>()</code></td><td><div class="block">Indicates if the light emission values of a block should be used to extract lighting information for a model.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
The client configuration.
Elements in this configuration are only relevant for the client side of C&amp;B.
This configuration does not need to be in-sync with the server values.
<dl class="notes">
<dt>Returns:</dt>
<dd>The client configuration.</dd>
</dl>
</div>
:::


</section>

<section id="getInvertBitBagFullness()">

:::tabs
== getInvertBitBagFullness
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getInvertBitBagFullness</span>()</div>
Indicates if currently the bit bag fullness indication via the damage bar of the stack
shows fullness or emptiness.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current bit bag fullness indication system.</dd>
</dl>
</div>
:::


</section>

<section id="getSuccessfulPlacementRenderMode()">

:::tabs
== getSuccessfulPlacementRenderMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="../client/render/preview/placement/PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</span>&nbsp;<span class="element-name">getSuccessfulPlacementRenderMode</span>()</div>
Determines the render mode used for successful pattern or chiseled block placement.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current successful placement render mode.</dd>
</dl>
</div>
:::


</section>

<section id="getFailedPlacementRenderMode()">

:::tabs
== getFailedPlacementRenderMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="../client/render/preview/placement/PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</span>&nbsp;<span class="element-name">getFailedPlacementRenderMode</span>()</div>
Determines the render mode used for successful pattern or chiseled block placement.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current successful placement render mode.</dd>
</dl>
</div>
:::


</section>

<section id="getSuccessfulPlacementColor()">

:::tabs
== getSuccessfulPlacementColor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;</span>&nbsp;<span class="element-name">getSuccessfulPlacementColor</span>()</div>
Determines the color used for successful pattern or chiseled block placement.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current successful placement color.</dd>
</dl>
</div>
:::


</section>

<section id="getNotFittingPatternPlacementColor()">

:::tabs
== getNotFittingPatternPlacementColor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;</span>&nbsp;<span class="element-name">getNotFittingPatternPlacementColor</span>()</div>
Determines the color used for pattern placement which does not fit on the targeted position.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current not fitting placement color.</dd>
</dl>
</div>
:::


</section>

<section id="getMissingBitsOrSpacePatternPlacementColor()">

:::tabs
== getMissingBitsOrSpacePatternPlacementColor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;</span>&nbsp;<span class="element-name">getMissingBitsOrSpacePatternPlacementColor</span>()</div>
Determines the color which indicates that the player is either missing bits, or does not have
enough space to pick up the bits.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current missing bits or insufficient space placement color.</dd>
</dl>
</div>
:::


</section>

<section id="getPreviewChiselingColor()">

:::tabs
== getPreviewChiselingColor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</span>&nbsp;<span class="element-name">getPreviewChiselingColor</span>()</div>
Provides the RGBA color channels for the color of the chiseling outline.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current chiseling outline color.</dd>
</dl>
</div>
:::


</section>

<section id="getPreviewPlacementColor()">

:::tabs
== getPreviewPlacementColor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</span>&nbsp;<span class="element-name">getPreviewPlacementColor</span>()</div>
Provides the RGBA color channels for the color of the placement outline.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current placement outline color.</dd>
</dl>
</div>
:::


</section>

<section id="getPreviewRenderer()">

:::tabs
== getPreviewRenderer
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</span>&nbsp;<span class="element-name">getPreviewRenderer</span>()</div>
Indicates which preview renderer should be used.
Returns the id of the preview renderer.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current preview renderer.</dd>
</dl>
</div>
:::


</section>

<section id="getToolModeRenderer()">

:::tabs
== getToolModeRenderer
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</span>&nbsp;<span class="element-name">getToolModeRenderer</span>()</div>
Indicates which tool mode renderer should be used.
Returns the id of the tool mode renderer.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current tool mode renderer.</dd>
</dl>
</div>
:::


</section>

<section id="getInvertPickBlockBehaviour()">

:::tabs
== getInvertPickBlockBehaviour
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getInvertPickBlockBehaviour</span>()</div>
Indicates if the block picking behaviour of chiseled blocks needs to be inverted.
By default, a bit is picked from a chiseled block, if this is true however
then the full block is picked and shift needs to be held to pick the bit.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates if the block picking behaviour of chiseled blocks needs to be inverted.</dd>
</dl>
</div>
:::


</section>

<section id="getBitStorageContentCacheSize()">

:::tabs
== getBitStorageContentCacheSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</span>&nbsp;<span class="element-name">getBitStorageContentCacheSize</span>()</div>
Indicates the size of the bit storage content model cache size.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current bit storage content cache size.</dd>
</dl>
</div>
:::


</section>

<section id="getPrinterContentCacheSize()">

:::tabs
== getPrinterContentCacheSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</span>&nbsp;<span class="element-name">getPrinterContentCacheSize</span>()</div>
Indicates the size of the printer content model cache size.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates the current printer content cache size.</dd>
</dl>
</div>
:::


</section>

<section id="getEnableFaceLightmapExtraction()">

:::tabs
== getEnableFaceLightmapExtraction
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getEnableFaceLightmapExtraction</span>()</div>
Indicates if the lightmap values of a face should be used to extract lighting information for a model.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates if the lightmap values of a face should be used to extract lighting information for a model.</dd>
</dl>
</div>
:::


</section>

<section id="getUseGetLightValue()">

:::tabs
== getUseGetLightValue
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getUseGetLightValue</span>()</div>
Indicates if the light emission values of a block should be used to extract lighting information for a model.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier that indicates if the light emission values of a block should be used to extract lighting information for a model.</dd>
</dl>
</div>
:::


</section>

<section id="getEnableMouseIndicatorInRadialMenu()">

:::tabs
== getEnableMouseIndicatorInRadialMenu
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getEnableMouseIndicatorInRadialMenu</span>()</div>
Indicates if a mouse indicator should be shown when the mouse is in a selection area in the radial menu.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates if a mouse indicator should be rendered in the radial menu.</dd>
</dl>
</div>
:::


</section>

<section id="getModelCacheSize()">

:::tabs
== getModelCacheSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</span>&nbsp;<span class="element-name">getModelCacheSize</span>()</div>
Indicates how many block models should be kept in the model cache.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates how many block models should be kept in the model cache.</dd>
</dl>
</div>
:::


</section>

<section id="getFaceLayerCacheSize()">

:::tabs
== getFaceLayerCacheSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</span>&nbsp;<span class="element-name">getFaceLayerCacheSize</span>()</div>
Indicates how many faces should be kept in the face layer cache.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates how many faces should be kept in the face layer cache.</dd>
</dl>
</div>
:::


</section>

<section id="getModelBuildingThreadCount()">

:::tabs
== getModelBuildingThreadCount
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getModelBuildingThreadCount</span>()</div>
Indicates how many threads should be used during building of the model cache.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates how many threads should be used.</dd>
</dl>
</div>
:::


</section>

<section id="getClipboardSize()">

:::tabs
== getClipboardSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getClipboardSize</span>()</div>
Indicates the amount of itemstacks that can be stored in the clipboard.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates the amount of itemstacks that can be stored in the clipboard.</dd>
</dl>
</div>
:::


</section>

<section id="getShouldBrokenBlocksBeAddedToClipboard()">

:::tabs
== getShouldBrokenBlocksBeAddedToClipboard
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getShouldBrokenBlocksBeAddedToClipboard</span>()</div>
Indicates if a broken chiseled block should be added to the clipboard.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates if a broken chiseled block should be added to the clipboard.</dd>
</dl>
</div>
:::


</section>

<section id="getShouldPickedBlocksBeAddedToClipboard()">

:::tabs
== getShouldPickedBlocksBeAddedToClipboard
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getShouldPickedBlocksBeAddedToClipboard</span>()</div>
Indicates if a picked chiseled block should be added to the clipboard.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates if a picked chiseled block should be added to the clipboard.</dd>
</dl>
</div>
:::


</section>

<section id="getPatternExportPath()">

:::tabs
== getPatternExportPath
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;</span>&nbsp;<span class="element-name">getPatternExportPath</span>()</div>
Indicates the path where chisels and bits will export and import patterns from.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates the path where chisels and bits will export and import patterns from.</dd>
</dl>
</div>
:::


</section>

<section id="getStackModelCacheSize()">

:::tabs
== getStackModelCacheSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</span>&nbsp;<span class="element-name">getStackModelCacheSize</span>()</div>
Indicates the size of the stack model cache.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates the size of the stack model cache.</dd>
</dl>
</div>
:::


</section>

<section id="getCullTestingCacheSize()">

:::tabs
== getCullTestingCacheSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</span>&nbsp;<span class="element-name">getCullTestingCacheSize</span>()</div>
Indicates the size of the cull testing cache.
<dl class="notes">
<dt>Returns:</dt>
<dd>The size of the cull testing cache.</dd>
</dl>
</div>
:::


</section>

<section id="getMutatorPreviewChiselingColor()">

:::tabs
== getMutatorPreviewChiselingColor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</span>&nbsp;<span class="element-name">getMutatorPreviewChiselingColor</span>()</div>
Determines the color used during debug rendering of the mutator area when chiseling.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates the color used during debug rendering of the mutator area when chiseling.</dd>
</dl>
</div>
:::


</section>

<section id="getMutatorPreviewPlacementColor()">

:::tabs
== getMutatorPreviewPlacementColor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;? extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang" class="external-link">Float</a>&gt;&gt;</span>&nbsp;<span class="element-name">getMutatorPreviewPlacementColor</span>()</div>
Determines the color used during debug rendering of the mutator area when placing.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates the color used during debug rendering of the mutator area when placing.</dd>
</dl>
</div>
:::


</section>

<section id="getMutatorPreviewDebug()">

:::tabs
== getMutatorPreviewDebug
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getMutatorPreviewDebug</span>()</div>
Indicates if the preview rendering should run in debug mode.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates if the preview rendering should run in debug mode.</dd>
</dl>
</div>
:::


</section>

<section id="getShowCoolDownError()">

:::tabs
== getShowCoolDownError
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getShowCoolDownError</span>()</div>
Indicates if an error notification should be shown when the player attempts to chisel during a cool down or not.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates if an error notification should be shown when the player attempts to chisel during a cool down or not.</dd>
</dl>
</div>
:::


</section>

<section id="getShouldScrollInteractionsChangeMode()">

:::tabs
== getShouldScrollInteractionsChangeMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getShouldScrollInteractionsChangeMode</span>()</div>
Indicates if a scroll interactions should change the mode of a held item.
<dl class="notes">
<dt>Returns:</dt>
<dd>A configuration supplier which indicates if a scroll interactions should change the mode of a held item.</dd>
</dl>
</div>
:::


</section>

:::::
  

