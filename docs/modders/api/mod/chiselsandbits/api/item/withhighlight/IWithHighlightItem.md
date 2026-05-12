--- 
title: IWithHighlightItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.withhighlight](index.md)  
# Interface IWithHighlightItem  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWithHighlightItem</span></div>  

  

Indicates an item that is used to draw custom highlights,
using custom logic instead of the default one.  

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
  <tr><td><code>void</code></td><td><code><a href="#renderHighlight(net.minecraft.world.entity.player.Player,net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float)" class="member-name-link">renderHighlight</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.client.renderer.LevelRenderer&nbsp;worldRenderer,<br> com.mojang.blaze3d.vertex.PoseStack&nbsp;matrixStack,<br> net.minecraft.client.renderer.MultiBufferSource.BufferSource&nbsp;bufferSource,<br> net.minecraft.client.renderer.state.level.LevelRenderState&nbsp;levelRenderState,<br> float&nbsp;partialTicks)</code></td><td><div class="block">Renders the highlight for the current item.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldDrawDefaultHighlight(net.minecraft.world.entity.player.Player)" class="member-name-link">shouldDrawDefaultHighlight</a><wbr>(@NotNull net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Indicates if the given player is allowed to use the<br>default render method.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#renderHighlight(net.minecraft.world.entity.player.Player,net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float)" class="member-name-link">renderHighlight</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.client.renderer.LevelRenderer&nbsp;worldRenderer,<br> com.mojang.blaze3d.vertex.PoseStack&nbsp;matrixStack,<br> net.minecraft.client.renderer.MultiBufferSource.BufferSource&nbsp;bufferSource,<br> net.minecraft.client.renderer.state.level.LevelRenderState&nbsp;levelRenderState,<br> float&nbsp;partialTicks)</code></td><td><div class="block">Renders the highlight for the current item.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldDrawDefaultHighlight(net.minecraft.world.entity.player.Player)" class="member-name-link">shouldDrawDefaultHighlight</a><wbr>(@NotNull net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Indicates if the given player is allowed to use the<br>default render method.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#renderHighlight(net.minecraft.world.entity.player.Player,net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float)" class="member-name-link">renderHighlight</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.client.renderer.LevelRenderer&nbsp;worldRenderer,<br> com.mojang.blaze3d.vertex.PoseStack&nbsp;matrixStack,<br> net.minecraft.client.renderer.MultiBufferSource.BufferSource&nbsp;bufferSource,<br> net.minecraft.client.renderer.state.level.LevelRenderState&nbsp;levelRenderState,<br> float&nbsp;partialTicks)</code></td><td><div class="block">Renders the highlight for the current item.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldDrawDefaultHighlight(net.minecraft.world.entity.player.Player)" class="member-name-link">shouldDrawDefaultHighlight</a><wbr>(@NotNull net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Indicates if the given player is allowed to use the<br>default render method.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="shouldDrawDefaultHighlight(net.minecraft.world.entity.player.Player)">

:::tabs
== shouldDrawDefaultHighlight
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">shouldDrawDefaultHighlight</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.entity.player.Player&nbsp;playerEntity)</span></div>
<div class="block">Indicates if the given player is allowed to use the
default render method.

If this is false. The default highlight rendering is cancelled.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player entity in question.</dd>
<dt>Returns:</dt>
<dd>True to let minecraft handle the highlight rendering, false when not.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="renderHighlight(net.minecraft.world.entity.player.Player,net.minecraft.client.renderer.LevelRenderer,com.mojang.blaze3d.vertex.PoseStack,net.minecraft.client.renderer.MultiBufferSource.BufferSource,net.minecraft.client.renderer.state.level.LevelRenderState,float)">

:::tabs
== renderHighlight
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">renderHighlight</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.client.renderer.LevelRenderer&nbsp;worldRenderer,
 com.mojang.blaze3d.vertex.PoseStack&nbsp;matrixStack,
 net.minecraft.client.renderer.MultiBufferSource.BufferSource&nbsp;bufferSource,
 net.minecraft.client.renderer.state.level.LevelRenderState&nbsp;levelRenderState,
 float&nbsp;partialTicks)</span></div>
<div class="block">Renders the highlight for the current item.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player entity in question.</dd>
<dd><code>worldRenderer</code> - The rendering world renderer.</dd>
<dd><code>matrixStack</code> - The matrix stack used to render the world.</dd>
<dd><code>bufferSource</code> - The buffer source to get the relevant vertex consumer from.</dd>
<dd><code>levelRenderState</code> - The current levels render state.</dd>
<dd><code>partialTicks</code> - The partial ticks used for animations.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

