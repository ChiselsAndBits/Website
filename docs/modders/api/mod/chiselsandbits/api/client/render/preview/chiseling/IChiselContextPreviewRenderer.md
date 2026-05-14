--- 
title: IChiselContextPreviewRenderer
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.render.preview.chiseling](index.md)  
# Interface IChiselContextPreviewRenderer  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselContextPreviewRenderer</span></div>  

  

Renderer which is used to render the chiseling preview.  

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
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of teh renderer.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#renderExistingContextsBoundingBox(net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">renderExistingContextsBoundingBox</a><wbr>(net.minecraft.client.renderer.LevelRenderer&nbsp;levelRenderer,<br> com.mojang.blaze3d.vertex.PoseStack&nbsp;matrixStack,<br> net.minecraft.client.renderer.MultiBufferSource.BufferSource&nbsp;bufferSource,<br> net.minecraft.client.renderer.state.level.LevelRenderState&nbsp;levelRenderState,<br> float&nbsp;partialTicks,<br> <a href="../../../../chiseling/IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;currentContextSnapshot)</code></td><td><div class="block">Invoked by the engine to render previews of the given <a href="../../../../chiseling/IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling"><code>IChiselingContext</code></a>.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of teh renderer.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#renderExistingContextsBoundingBox(net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">renderExistingContextsBoundingBox</a><wbr>(net.minecraft.client.renderer.LevelRenderer&nbsp;levelRenderer,<br> com.mojang.blaze3d.vertex.PoseStack&nbsp;matrixStack,<br> net.minecraft.client.renderer.MultiBufferSource.BufferSource&nbsp;bufferSource,<br> net.minecraft.client.renderer.state.level.LevelRenderState&nbsp;levelRenderState,<br> float&nbsp;partialTicks,<br> <a href="../../../../chiseling/IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;currentContextSnapshot)</code></td><td><div class="block">Invoked by the engine to render previews of the given <a href="../../../../chiseling/IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling"><code>IChiselingContext</code></a>.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of teh renderer.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#renderExistingContextsBoundingBox(net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">renderExistingContextsBoundingBox</a><wbr>(net.minecraft.client.renderer.LevelRenderer&nbsp;levelRenderer,<br> com.mojang.blaze3d.vertex.PoseStack&nbsp;matrixStack,<br> net.minecraft.client.renderer.MultiBufferSource.BufferSource&nbsp;bufferSource,<br> net.minecraft.client.renderer.state.level.LevelRenderState&nbsp;levelRenderState,<br> float&nbsp;partialTicks,<br> <a href="../../../../chiseling/IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;currentContextSnapshot)</code></td><td><div class="block">Invoked by the engine to render previews of the given <a href="../../../../chiseling/IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling"><code>IChiselingContext</code></a>.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getId()">

:::tabs
== getId
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.resources.Identifier</span>&nbsp;<span class="element-name">getId</span>()</div>
The id of teh renderer.
Used to give the player a selection option for the preview renderer.
<dl class="notes">
<dt>Returns:</dt>
<dd>The id of the preview renderer.</dd>
</dl>
</div>
:::


</section>

<section id="renderExistingContextsBoundingBox(net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float,mod.chiselsandbits.api.chiseling.IChiselingContext)">

:::tabs
== renderExistingContextsBoundingBox
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">renderExistingContextsBoundingBox</span><wbr><span class="parameters">(net.minecraft.client.renderer.LevelRenderer&nbsp;levelRenderer,
 com.mojang.blaze3d.vertex.PoseStack&nbsp;matrixStack,
 net.minecraft.client.renderer.MultiBufferSource.BufferSource&nbsp;bufferSource,
 net.minecraft.client.renderer.state.level.LevelRenderState&nbsp;levelRenderState,
 float&nbsp;partialTicks,
 <a href="../../../../chiseling/IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;currentContextSnapshot)</span></div>
Invoked by the engine to render previews of the given <a href="../../../../chiseling/IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling"><code>IChiselingContext</code></a>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>levelRenderer</code> - The level renderer in which the bounding box is being rendered.</dd>
<dd><code>matrixStack</code> - The matrix stack to render into.</dd>
<dd><code>bufferSource</code> - The buffer source to get the outline vertex consumers for-</dd>
<dd><code>levelRenderState</code> - The current level render state</dd>
<dd><code>partialTicks</code> - The partial ticks</dd>
<dd><code>currentContextSnapshot</code> - The current snapshot to render.</dd>
</dl>
</div>
:::


</section>

:::::
  

