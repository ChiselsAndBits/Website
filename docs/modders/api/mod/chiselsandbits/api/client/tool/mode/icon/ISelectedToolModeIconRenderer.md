--- 
title: ISelectedToolModeIconRenderer
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.tool.mode.icon](index.md)  
# Interface ISelectedToolModeIconRenderer  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ISelectedToolModeIconRenderer</span></div>  

  

Used to render the icons on the hot bar for the selected tool mode.  

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
  <tr><td><code>void</code></td><td><code><a href="#extractGraphics(net.minecraft.client.gui.GuiGraphicsExtractor,net.minecraft.world.item.ItemStack)" class="member-name-link">extractGraphics</a><wbr>(net.minecraft.client.gui.GuiGraphicsExtractor&nbsp;guiGraphics,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked to render the stacks tool mode icon in the given itemstack.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of the renderer.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#extractGraphics(net.minecraft.client.gui.GuiGraphicsExtractor,net.minecraft.world.item.ItemStack)" class="member-name-link">extractGraphics</a><wbr>(net.minecraft.client.gui.GuiGraphicsExtractor&nbsp;guiGraphics,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked to render the stacks tool mode icon in the given itemstack.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of the renderer.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#extractGraphics(net.minecraft.client.gui.GuiGraphicsExtractor,net.minecraft.world.item.ItemStack)" class="member-name-link">extractGraphics</a><wbr>(net.minecraft.client.gui.GuiGraphicsExtractor&nbsp;guiGraphics,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked to render the stacks tool mode icon in the given itemstack.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getId()" class="member-name-link">getId</a>()</code></td><td><div class="block">The id of the renderer.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getId()">

:::tabs
== getId
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.resources.Identifier</span>&nbsp;<span class="element-name">getId</span>()</div>
<div class="block">The id of the renderer.
Used to give the player a selection option for the preview renderer.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The id of the preview renderer.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="extractGraphics(net.minecraft.client.gui.GuiGraphicsExtractor,net.minecraft.world.item.ItemStack)">

:::tabs
== extractGraphics
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">extractGraphics</span><wbr><span class="parameters">(net.minecraft.client.gui.GuiGraphicsExtractor&nbsp;guiGraphics,
 net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Invoked to render the stacks tool mode icon in the given itemstack.
This is invoked already translated to the top left pixel of the slot in question.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>guiGraphics</code> - The matrix stack.</dd>
<dd><code>stack</code> - The stack.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

