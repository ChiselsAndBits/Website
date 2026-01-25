--- 
title: IIconManager
aside: false 
---
_Package:_ [mod.chiselsandbits.api.client.icon](index.md)  
# Interface IIconManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IIconManager</span></div>  

  

  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpFirstIcon()" class="member-name-link">getBagPicksUpFirstIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpSecondIcon()" class="member-name-link">getBagPicksUpSecondIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getFilterBagModeIcon()" class="member-name-link">getFilterBagModeIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getIcon(net.minecraft.resources.Identifier)" class="member-name-link">getIcon</a><wbr>(net.minecraft.resources.Identifier&nbsp;name)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getNormalBagModeIcon()" class="member-name-link">getNormalBagModeIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getPlaceIcon()" class="member-name-link">getPlaceIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRedoIcon()" class="member-name-link">getRedoIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollXIcon()" class="member-name-link">getRollXIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollZIcon()" class="member-name-link">getRollZIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSortIcon()" class="member-name-link">getSortIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSwapIcon()" class="member-name-link">getSwapIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getTrashIcon()" class="member-name-link">getTrashIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getUndoIcon()" class="member-name-link">getUndoIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getWhiteIcon()" class="member-name-link">getWhiteIcon</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpFirstIcon()" class="member-name-link">getBagPicksUpFirstIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpSecondIcon()" class="member-name-link">getBagPicksUpSecondIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getFilterBagModeIcon()" class="member-name-link">getFilterBagModeIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getIcon(net.minecraft.resources.Identifier)" class="member-name-link">getIcon</a><wbr>(net.minecraft.resources.Identifier&nbsp;name)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getNormalBagModeIcon()" class="member-name-link">getNormalBagModeIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getPlaceIcon()" class="member-name-link">getPlaceIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRedoIcon()" class="member-name-link">getRedoIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollXIcon()" class="member-name-link">getRollXIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollZIcon()" class="member-name-link">getRollZIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSortIcon()" class="member-name-link">getSortIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSwapIcon()" class="member-name-link">getSwapIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getTrashIcon()" class="member-name-link">getTrashIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getUndoIcon()" class="member-name-link">getUndoIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getWhiteIcon()" class="member-name-link">getWhiteIcon</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpFirstIcon()" class="member-name-link">getBagPicksUpFirstIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpSecondIcon()" class="member-name-link">getBagPicksUpSecondIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getFilterBagModeIcon()" class="member-name-link">getFilterBagModeIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getIcon(net.minecraft.resources.Identifier)" class="member-name-link">getIcon</a><wbr>(net.minecraft.resources.Identifier&nbsp;name)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getNormalBagModeIcon()" class="member-name-link">getNormalBagModeIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getPlaceIcon()" class="member-name-link">getPlaceIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRedoIcon()" class="member-name-link">getRedoIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollXIcon()" class="member-name-link">getRollXIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollZIcon()" class="member-name-link">getRollZIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSortIcon()" class="member-name-link">getSortIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSwapIcon()" class="member-name-link">getSwapIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getTrashIcon()" class="member-name-link">getTrashIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getUndoIcon()" class="member-name-link">getUndoIcon</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getWhiteIcon()" class="member-name-link">getWhiteIcon</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getIcon(net.minecraft.resources.Identifier)">

:::tabs
== getIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getIcon</span><wbr><span class="parameters">(net.minecraft.resources.Identifier&nbsp;name)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="getSwapIcon()">

:::tabs
== getSwapIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getSwapIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getPlaceIcon()">

:::tabs
== getPlaceIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getPlaceIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getUndoIcon()">

:::tabs
== getUndoIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getUndoIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getRedoIcon()">

:::tabs
== getRedoIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getRedoIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getTrashIcon()">

:::tabs
== getTrashIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getTrashIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getSortIcon()">

:::tabs
== getSortIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getSortIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getRollXIcon()">

:::tabs
== getRollXIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getRollXIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getRollZIcon()">

:::tabs
== getRollZIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getRollZIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getWhiteIcon()">

:::tabs
== getWhiteIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getWhiteIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getFilterBagModeIcon()">

:::tabs
== getFilterBagModeIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getFilterBagModeIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getNormalBagModeIcon()">

:::tabs
== getNormalBagModeIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getNormalBagModeIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getBagPicksUpFirstIcon()">

:::tabs
== getBagPicksUpFirstIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getBagPicksUpFirstIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getBagPicksUpSecondIcon()">

:::tabs
== getBagPicksUpSecondIcon
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getBagPicksUpSecondIcon</span>()</div>
<dl class="notes"></dl>
:::


</section>

:::::
  

