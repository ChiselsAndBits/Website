--- 
title: IRenderableMode
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.withmode](index)  
# Interface IRenderableMode  
**All Extended Interfaces:**  
[IWithColor](../../util/IWithColor), [IWithDisplayName](../../util/IWithDisplayName), [IWithIcon](../../util/IWithIcon), [IWithIconAndColor](../../util/IWithIconAndColor)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IRenderableMode</span><span class="extends-implements"><br/>  
extends <a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a>, <a href="../../util/IWithIconAndColor.html" title="interface in mod.chiselsandbits.api.util">IWithIconAndColor</a></span></div>  

  

Represents a tool mode which can be rendered.  

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
  <tr><td><code>default @NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getColorVector()" class="member-name-link">getColorVector</a>()</code></td><td><div class="block">The color used to render.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec2</code></td><td><code><a href="#getPositionVector()" class="member-name-link">getPositionVector</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec2</code></td><td><code><a href="#getScaleVector()" class="member-name-link">getScaleVector</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isActive()" class="member-name-link">isActive</a>()</code></td><td><div class="block">Indicates if the mode is currently active and as such should be rendered or not.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderDisplayNameInMenu()" class="member-name-link">shouldRenderDisplayNameInMenu</a>()</code></td><td><div class="block">Indicates if this mode should render his name in the menu.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderName()" class="member-name-link">shouldRenderName</a>()</code></td><td><div class="block">Indicates if the name of the mode should be rendered.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default @NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getColorVector()" class="member-name-link">getColorVector</a>()</code></td><td><div class="block">The color used to render.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec2</code></td><td><code><a href="#getPositionVector()" class="member-name-link">getPositionVector</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec2</code></td><td><code><a href="#getScaleVector()" class="member-name-link">getScaleVector</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isActive()" class="member-name-link">isActive</a>()</code></td><td><div class="block">Indicates if the mode is currently active and as such should be rendered or not.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderDisplayNameInMenu()" class="member-name-link">shouldRenderDisplayNameInMenu</a>()</code></td><td><div class="block">Indicates if this mode should render his name in the menu.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderName()" class="member-name-link">shouldRenderName</a>()</code></td><td><div class="block">Indicates if the name of the mode should be rendered.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default @NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getColorVector()" class="member-name-link">getColorVector</a>()</code></td><td><div class="block">The color used to render.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec2</code></td><td><code><a href="#getPositionVector()" class="member-name-link">getPositionVector</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec2</code></td><td><code><a href="#getScaleVector()" class="member-name-link">getScaleVector</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isActive()" class="member-name-link">isActive</a>()</code></td><td><div class="block">Indicates if the mode is currently active and as such should be rendered or not.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderDisplayNameInMenu()" class="member-name-link">shouldRenderDisplayNameInMenu</a>()</code></td><td><div class="block">Indicates if this mode should render his name in the menu.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderName()" class="member-name-link">shouldRenderName</a>()</code></td><td><div class="block">Indicates if the name of the mode should be rendered.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a>
<a href="../../util/IWithColor.html#getAlphaChannel()" title="getAlphaChannel()">getAlphaChannel</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a>
<a href="../../util/IWithDisplayName.html#getDisplayName()" title="getDisplayName()">getDisplayName</a>, <a href="../../util/IWithDisplayName.html#getMultiLineDisplayName()" title="getMultiLineDisplayName()">getMultiLineDisplayName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a>
<a href="../../util/IWithIcon.html#getIcon()" title="getIcon()">getIcon</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="isActive()">

:::tabs
== isActive
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isActive</span>()</div>
Indicates if the mode is currently active and as such should be rendered or not.
<dl class="notes">
<dt>Returns:</dt>
<dd>True for active modes, false for not.</dd>
</dl>
</div>
:::


</section>

<section id="shouldRenderName()">

:::tabs
== shouldRenderName
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">shouldRenderName</span>()</div>
Indicates if the name of the mode should be rendered.
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> when the name should be rendered.</dd>
</dl>
</div>
:::


</section>

<section id="shouldRenderDisplayNameInMenu()">

:::tabs
== shouldRenderDisplayNameInMenu
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">shouldRenderDisplayNameInMenu</span>()</div>
Indicates if this mode should render his name in the menu.
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> when then name should be rendered in the menu.</dd>
</dl>
</div>
:::


</section>

<section id="getColorVector()">

:::tabs
== getColorVector
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">default</span>&nbsp;<span class="return-type">@NotNull net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getColorVector</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../../util/IWithColor.html#getColorVector()">IWithColor</a></code></span></div>
The color used to render.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../util/IWithColor.html#getColorVector()">getColorVector</a></code>&nbsp;in interface&nbsp;<code><a href="../../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a></code></dd>
<dt>Returns:</dt>
<dd>The color in a 3d double vector as RGB.</dd>
</dl>
</div>
:::


</section>

<section id="getPositionVector()">

:::tabs
== getPositionVector
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec2</span>&nbsp;<span class="element-name">getPositionVector</span>()</div>
</div>
:::


</section>

<section id="getScaleVector()">

:::tabs
== getScaleVector
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec2</span>&nbsp;<span class="element-name">getScaleVector</span>()</div>
</div>
:::


</section>

:::::
  

