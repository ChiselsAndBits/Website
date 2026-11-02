--- 
title: IMeasuringMode
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.measuring](index)  
# Interface IMeasuringMode  
**All Extended Interfaces:**  
[IRenderableMode](../item/withmode/IRenderableMode), [IToolMode\<IMeasuringType\>](../item/withmode/IToolMode), [IWithColor](../util/IWithColor), [IWithDisplayName](../util/IWithDisplayName), [IWithIcon](../util/IWithIcon), [IWithIconAndColor](../util/IWithIconAndColor)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMeasuringMode</span><span class="extends-implements"><br/>  
extends <a href="../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>&lt;<a href="IMeasuringType.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType</a>&gt;</span></div>  

  

Describes a mode for selecting and displaying measurements in the world.  

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
  <tr><td><code>net.minecraft.world.item.DyeColor</code></td><td><code><a href="#getColor()" class="member-name-link">getColor</a>()</code></td><td><div class="block">Returns the color associated with this measuring mode.</div><br></td></tr>
  <tr><td><code><a href="IMeasuringType.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Returns the measuring type associated with this mode.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderOnHotBar()" class="member-name-link">shouldRenderOnHotBar</a>()</code></td><td><div class="block">Indicates whether this group should render as a mode icon on the player hotbar.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.item.DyeColor</code></td><td><code><a href="#getColor()" class="member-name-link">getColor</a>()</code></td><td><div class="block">Returns the color associated with this measuring mode.</div><br></td></tr>
  <tr><td><code><a href="IMeasuringType.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Returns the measuring type associated with this mode.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderOnHotBar()" class="member-name-link">shouldRenderOnHotBar</a>()</code></td><td><div class="block">Indicates whether this group should render as a mode icon on the player hotbar.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.item.DyeColor</code></td><td><code><a href="#getColor()" class="member-name-link">getColor</a>()</code></td><td><div class="block">Returns the color associated with this measuring mode.</div><br></td></tr>
  <tr><td><code><a href="IMeasuringType.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType</a></code></td><td><code><a href="#getType()" class="member-name-link">getType</a>()</code></td><td><div class="block">Returns the measuring type associated with this mode.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderOnHotBar()" class="member-name-link">shouldRenderOnHotBar</a>()</code></td><td><div class="block">Indicates whether this group should render as a mode icon on the player hotbar.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../item/withmode/IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a>
<a href="../item/withmode/IRenderableMode.html#getColorVector()" title="getColorVector()">getColorVector</a>, <a href="../item/withmode/IRenderableMode.html#getPositionVector()" title="getPositionVector()">getPositionVector</a>, <a href="../item/withmode/IRenderableMode.html#getScaleVector()" title="getScaleVector()">getScaleVector</a>, <a href="../item/withmode/IRenderableMode.html#isActive()" title="isActive()">isActive</a>, <a href="../item/withmode/IRenderableMode.html#shouldRenderDisplayNameInMenu()" title="shouldRenderDisplayNameInMenu()">shouldRenderDisplayNameInMenu</a>, <a href="../item/withmode/IRenderableMode.html#shouldRenderName()" title="shouldRenderName()">shouldRenderName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>
<a href="../item/withmode/IToolMode.html#getGroup()" title="getGroup()">getGroup</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a>
<a href="../util/IWithColor.html#getAlphaChannel()" title="getAlphaChannel()">getAlphaChannel</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a>
<a href="../util/IWithDisplayName.html#getDisplayName()" title="getDisplayName()">getDisplayName</a>, <a href="../util/IWithDisplayName.html#getMultiLineDisplayName()" title="getMultiLineDisplayName()">getMultiLineDisplayName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a>
<a href="../util/IWithIcon.html#getIcon()" title="getIcon()">getIcon</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getColor()">

:::tabs
== getColor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.item.DyeColor</span>&nbsp;<span class="element-name">getColor</span>()</div>
Returns the color associated with this measuring mode.
<dl class="notes">
<dt>Returns:</dt>
<dd>this mode's measurement color</dd>
</dl>
</div>
:::


</section>

<section id="getType()">

:::tabs
== getType
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IMeasuringType.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType</a></span>&nbsp;<span class="element-name">getType</span>()</div>
Returns the measuring type associated with this mode.
<dl class="notes">
<dt>Returns:</dt>
<dd>the measurement type configured for this mode</dd>
</dl>
</div>
:::


</section>

<section id="shouldRenderOnHotBar()">

:::tabs
== shouldRenderOnHotBar
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">shouldRenderOnHotBar</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="../util/IWithIcon.html#shouldRenderOnHotBar()">IWithIcon</a></code></span></div>
Indicates whether this group should render as a mode icon on the player hotbar.
<p>
By default, this is disabled.
Only specific gameplay aspects which have icons turn this on to aid the player.
</p>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../util/IWithIcon.html#shouldRenderOnHotBar()">shouldRenderOnHotBar</a></code>&nbsp;in interface&nbsp;<code><a href="../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> when we should render it on the hotbar.</dd>
</dl>
</div>
:::


</section>

:::::
  

