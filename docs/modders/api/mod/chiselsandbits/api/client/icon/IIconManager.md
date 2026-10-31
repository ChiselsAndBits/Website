--- 
title: IIconManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.icon](index)  
# Interface IIconManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IIconManager</span></div>  

  

Provides atlas sprites used by Chisels &amp; Bits UI and interaction overlays.  

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
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpFirstIcon()" class="member-name-link">getBagPicksUpFirstIcon</a>()</code></td><td><div class="block">Returns the icon for the pickup mode that gives the bag first priority.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpSecondIcon()" class="member-name-link">getBagPicksUpSecondIcon</a>()</code></td><td><div class="block">Returns the icon for the pickup mode that gives the player first priority.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getFilterBagModeIcon()" class="member-name-link">getFilterBagModeIcon</a>()</code></td><td><div class="block">Returns the icon indicating filtered bit-bag pickup.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getIcon(net.minecraft.resources.Identifier)" class="member-name-link">getIcon</a><wbr>(net.minecraft.resources.Identifier&nbsp;name)</code></td><td><div class="block">Looks up a sprite by its resource identifier.</div><br></td></tr>
  <tr><td><code>static <a href="IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Returns the icon manager exposed by the active API instance.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getNormalBagModeIcon()" class="member-name-link">getNormalBagModeIcon</a>()</code></td><td><div class="block">Returns the icon indicating normal bit-bag pickup.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getPlaceIcon()" class="member-name-link">getPlaceIcon</a>()</code></td><td><div class="block">Returns the icon used for placement actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRedoIcon()" class="member-name-link">getRedoIcon</a>()</code></td><td><div class="block">Returns the icon used for redo actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollXIcon()" class="member-name-link">getRollXIcon</a>()</code></td><td><div class="block">Returns the icon used to roll or rotate content around the x axis.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollZIcon()" class="member-name-link">getRollZIcon</a>()</code></td><td><div class="block">Returns the icon used to roll or rotate content around the z axis.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSortIcon()" class="member-name-link">getSortIcon</a>()</code></td><td><div class="block">Returns the icon used for sorting inventory contents.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSwapIcon()" class="member-name-link">getSwapIcon</a>()</code></td><td><div class="block">Returns the icon used for swapping or exchanging items.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getTrashIcon()" class="member-name-link">getTrashIcon</a>()</code></td><td><div class="block">Returns the icon used for discarding or removing items.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getUndoIcon()" class="member-name-link">getUndoIcon</a>()</code></td><td><div class="block">Returns the icon used for undo actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getWhiteIcon()" class="member-name-link">getWhiteIcon</a>()</code></td><td><div class="block">Returns the solid white sprite used as a tintable UI texture.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Returns the icon manager exposed by the active API instance.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpFirstIcon()" class="member-name-link">getBagPicksUpFirstIcon</a>()</code></td><td><div class="block">Returns the icon for the pickup mode that gives the bag first priority.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpSecondIcon()" class="member-name-link">getBagPicksUpSecondIcon</a>()</code></td><td><div class="block">Returns the icon for the pickup mode that gives the player first priority.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getFilterBagModeIcon()" class="member-name-link">getFilterBagModeIcon</a>()</code></td><td><div class="block">Returns the icon indicating filtered bit-bag pickup.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getIcon(net.minecraft.resources.Identifier)" class="member-name-link">getIcon</a><wbr>(net.minecraft.resources.Identifier&nbsp;name)</code></td><td><div class="block">Looks up a sprite by its resource identifier.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getNormalBagModeIcon()" class="member-name-link">getNormalBagModeIcon</a>()</code></td><td><div class="block">Returns the icon indicating normal bit-bag pickup.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getPlaceIcon()" class="member-name-link">getPlaceIcon</a>()</code></td><td><div class="block">Returns the icon used for placement actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRedoIcon()" class="member-name-link">getRedoIcon</a>()</code></td><td><div class="block">Returns the icon used for redo actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollXIcon()" class="member-name-link">getRollXIcon</a>()</code></td><td><div class="block">Returns the icon used to roll or rotate content around the x axis.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollZIcon()" class="member-name-link">getRollZIcon</a>()</code></td><td><div class="block">Returns the icon used to roll or rotate content around the z axis.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSortIcon()" class="member-name-link">getSortIcon</a>()</code></td><td><div class="block">Returns the icon used for sorting inventory contents.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSwapIcon()" class="member-name-link">getSwapIcon</a>()</code></td><td><div class="block">Returns the icon used for swapping or exchanging items.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getTrashIcon()" class="member-name-link">getTrashIcon</a>()</code></td><td><div class="block">Returns the icon used for discarding or removing items.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getUndoIcon()" class="member-name-link">getUndoIcon</a>()</code></td><td><div class="block">Returns the icon used for undo actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getWhiteIcon()" class="member-name-link">getWhiteIcon</a>()</code></td><td><div class="block">Returns the solid white sprite used as a tintable UI texture.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpFirstIcon()" class="member-name-link">getBagPicksUpFirstIcon</a>()</code></td><td><div class="block">Returns the icon for the pickup mode that gives the bag first priority.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getBagPicksUpSecondIcon()" class="member-name-link">getBagPicksUpSecondIcon</a>()</code></td><td><div class="block">Returns the icon for the pickup mode that gives the player first priority.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getFilterBagModeIcon()" class="member-name-link">getFilterBagModeIcon</a>()</code></td><td><div class="block">Returns the icon indicating filtered bit-bag pickup.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getIcon(net.minecraft.resources.Identifier)" class="member-name-link">getIcon</a><wbr>(net.minecraft.resources.Identifier&nbsp;name)</code></td><td><div class="block">Looks up a sprite by its resource identifier.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getNormalBagModeIcon()" class="member-name-link">getNormalBagModeIcon</a>()</code></td><td><div class="block">Returns the icon indicating normal bit-bag pickup.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getPlaceIcon()" class="member-name-link">getPlaceIcon</a>()</code></td><td><div class="block">Returns the icon used for placement actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRedoIcon()" class="member-name-link">getRedoIcon</a>()</code></td><td><div class="block">Returns the icon used for redo actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollXIcon()" class="member-name-link">getRollXIcon</a>()</code></td><td><div class="block">Returns the icon used to roll or rotate content around the x axis.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getRollZIcon()" class="member-name-link">getRollZIcon</a>()</code></td><td><div class="block">Returns the icon used to roll or rotate content around the z axis.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSortIcon()" class="member-name-link">getSortIcon</a>()</code></td><td><div class="block">Returns the icon used for sorting inventory contents.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getSwapIcon()" class="member-name-link">getSwapIcon</a>()</code></td><td><div class="block">Returns the icon used for swapping or exchanging items.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getTrashIcon()" class="member-name-link">getTrashIcon</a>()</code></td><td><div class="block">Returns the icon used for discarding or removing items.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getUndoIcon()" class="member-name-link">getUndoIcon</a>()</code></td><td><div class="block">Returns the icon used for undo actions.</div><br></td></tr>
  <tr><td><code>net.minecraft.client.renderer.texture.TextureAtlasSprite</code></td><td><code><a href="#getWhiteIcon()" class="member-name-link">getWhiteIcon</a>()</code></td><td><div class="block">Returns the solid white sprite used as a tintable UI texture.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IIconManager.html" title="interface in mod.chiselsandbits.api.client.icon">IIconManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
Returns the icon manager exposed by the active API instance.
<dl class="notes">
<dt>Returns:</dt>
<dd>the active icon manager</dd>
</dl>
</div>
:::


</section>

<section id="getIcon(net.minecraft.resources.Identifier)">

:::tabs
== getIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getIcon</span><wbr><span class="parameters">(net.minecraft.resources.Identifier&nbsp;name)</span></div>
Looks up a sprite by its resource identifier.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - sprite resource identifier</dd>
<dt>Returns:</dt>
<dd>the matching atlas sprite</dd>
</dl>
</div>
:::


</section>

<section id="getSwapIcon()">

:::tabs
== getSwapIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getSwapIcon</span>()</div>
Returns the icon used for swapping or exchanging items.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon used for swapping or exchanging items</dd>
</dl>
</div>
:::


</section>

<section id="getPlaceIcon()">

:::tabs
== getPlaceIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getPlaceIcon</span>()</div>
Returns the icon used for placement actions.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon used for placement actions</dd>
</dl>
</div>
:::


</section>

<section id="getUndoIcon()">

:::tabs
== getUndoIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getUndoIcon</span>()</div>
Returns the icon used for undo actions.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon used for undo actions</dd>
</dl>
</div>
:::


</section>

<section id="getRedoIcon()">

:::tabs
== getRedoIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getRedoIcon</span>()</div>
Returns the icon used for redo actions.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon used for redo actions</dd>
</dl>
</div>
:::


</section>

<section id="getTrashIcon()">

:::tabs
== getTrashIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getTrashIcon</span>()</div>
Returns the icon used for discarding or removing items.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon used for discarding or removing items</dd>
</dl>
</div>
:::


</section>

<section id="getSortIcon()">

:::tabs
== getSortIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getSortIcon</span>()</div>
Returns the icon used for sorting inventory contents.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon used for sorting inventory contents</dd>
</dl>
</div>
:::


</section>

<section id="getRollXIcon()">

:::tabs
== getRollXIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getRollXIcon</span>()</div>
Returns the icon used to roll or rotate content around the x axis.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon used to roll or rotate content around the x axis</dd>
</dl>
</div>
:::


</section>

<section id="getRollZIcon()">

:::tabs
== getRollZIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getRollZIcon</span>()</div>
Returns the icon used to roll or rotate content around the z axis.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon used to roll or rotate content around the z axis</dd>
</dl>
</div>
:::


</section>

<section id="getWhiteIcon()">

:::tabs
== getWhiteIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getWhiteIcon</span>()</div>
Returns the solid white sprite used as a tintable UI texture.
<dl class="notes">
<dt>Returns:</dt>
<dd>the solid white sprite used as a tintable UI texture</dd>
</dl>
</div>
:::


</section>

<section id="getFilterBagModeIcon()">

:::tabs
== getFilterBagModeIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getFilterBagModeIcon</span>()</div>
Returns the icon indicating filtered bit-bag pickup.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon indicating filtered bit-bag pickup</dd>
</dl>
</div>
:::


</section>

<section id="getNormalBagModeIcon()">

:::tabs
== getNormalBagModeIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getNormalBagModeIcon</span>()</div>
Returns the icon indicating normal bit-bag pickup.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon indicating normal bit-bag pickup</dd>
</dl>
</div>
:::


</section>

<section id="getBagPicksUpFirstIcon()">

:::tabs
== getBagPicksUpFirstIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getBagPicksUpFirstIcon</span>()</div>
Returns the icon for the pickup mode that gives the bag first priority.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon for the pickup mode that gives the bag first priority</dd>
</dl>
</div>
:::


</section>

<section id="getBagPicksUpSecondIcon()">

:::tabs
== getBagPicksUpSecondIcon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.client.renderer.texture.TextureAtlasSprite</span>&nbsp;<span class="element-name">getBagPicksUpSecondIcon</span>()</div>
Returns the icon for the pickup mode that gives the player first priority.
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon for the pickup mode that gives the player first priority</dd>
</dl>
</div>
:::


</section>

:::::
  

