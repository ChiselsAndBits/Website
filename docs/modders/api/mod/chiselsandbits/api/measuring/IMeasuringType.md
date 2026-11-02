--- 
title: IMeasuringType
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.measuring](index)  
# Interface IMeasuringType  
**All Extended Interfaces:**  
[IToolModeGroup](../item/withmode/group/IToolModeGroup), [IRenderableMode](../item/withmode/IRenderableMode), [IWithColor](../util/IWithColor), [IWithDisplayName](../util/IWithDisplayName), [IWithIcon](../util/IWithIcon), [IWithIconAndColor](../util/IWithIconAndColor)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMeasuringType</span><span class="extends-implements"><br/>  
extends <a href="../item/withmode/group/IToolModeGroup.html" title="interface in mod.chiselsandbits.api.item.withmode.group">IToolModeGroup</a></span></div>  

  

Defines how a measuring mode snaps clicked positions and measurement corners to a grid.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Interface</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static interface&nbsp;</code></td><td><code><a href="IMeasuringType.IClickedPositionAdapter.html" class="type-name-link" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType.IClickedPositionAdapter</a></code></td><td><div class="block">Adapts the location reported by a block hit before it becomes a measurement endpoint.</div><br></td></tr>
  <tr><td><code>static interface&nbsp;</code></td><td><code><a href="IMeasuringType.IPositionAdapter.html" class="type-name-link" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType.IPositionAdapter</a></code></td><td><div class="block">Adapts a pair of measurement endpoints using the clicked face.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptClickedPosition(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adaptClickedPosition</a><wbr>(net.minecraft.world.phys.BlockHitResult&nbsp;blockHitResult)</code></td><td><div class="block">Adapts the hit location used as the initial measurement point.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptEndCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptEndCorner</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the second corner of a measurement to this mode's grid.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptStartCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptStartCorner</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the first corner of a measurement to this mode's grid.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getResolution()" class="member-name-link">getResolution</a>()</code></td><td><div class="block">Returns the coordinate spacing used by this measuring mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isNeedsNormalization()" class="member-name-link">isNeedsNormalization</a>()</code></td><td><div class="block">Returns whether adapted measurement positions should be normalized.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderOnHotBar()" class="member-name-link">shouldRenderOnHotBar</a>()</code></td><td><div class="block">Indicates whether this group should render as a mode icon on the player hotbar.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptClickedPosition(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adaptClickedPosition</a><wbr>(net.minecraft.world.phys.BlockHitResult&nbsp;blockHitResult)</code></td><td><div class="block">Adapts the hit location used as the initial measurement point.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptEndCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptEndCorner</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the second corner of a measurement to this mode's grid.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptStartCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptStartCorner</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the first corner of a measurement to this mode's grid.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getResolution()" class="member-name-link">getResolution</a>()</code></td><td><div class="block">Returns the coordinate spacing used by this measuring mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isNeedsNormalization()" class="member-name-link">isNeedsNormalization</a>()</code></td><td><div class="block">Returns whether adapted measurement positions should be normalized.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#shouldRenderOnHotBar()" class="member-name-link">shouldRenderOnHotBar</a>()</code></td><td><div class="block">Indicates whether this group should render as a mode icon on the player hotbar.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptClickedPosition(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adaptClickedPosition</a><wbr>(net.minecraft.world.phys.BlockHitResult&nbsp;blockHitResult)</code></td><td><div class="block">Adapts the hit location used as the initial measurement point.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptEndCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptEndCorner</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the second corner of a measurement to this mode's grid.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptStartCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptStartCorner</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the first corner of a measurement to this mode's grid.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getResolution()" class="member-name-link">getResolution</a>()</code></td><td><div class="block">Returns the coordinate spacing used by this measuring mode.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isNeedsNormalization()" class="member-name-link">isNeedsNormalization</a>()</code></td><td><div class="block">Returns whether adapted measurement positions should be normalized.</div><br></td></tr>
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
<section id="adaptClickedPosition(net.minecraft.world.phys.BlockHitResult)">

:::tabs
== adaptClickedPosition
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">adaptClickedPosition</span><wbr><span class="parameters">(net.minecraft.world.phys.BlockHitResult&nbsp;blockHitResult)</span></div>
Adapts the hit location used as the initial measurement point.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockHitResult</code> - hit result for the clicked block</dd>
<dt>Returns:</dt>
<dd>the adapted measurement position</dd>
</dl>
</div>
:::


</section>

<section id="adaptStartCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)">

:::tabs
== adaptStartCorner
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">adaptStartCorner</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;startPosition,
 net.minecraft.world.phys.Vec3&nbsp;endPosition,
 net.minecraft.core.Direction&nbsp;hitFace)</span></div>
Adapts the first corner of a measurement to this mode's grid.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>startPosition</code> - clicked start position</dd>
<dd><code>endPosition</code> - other measurement endpoint</dd>
<dd><code>hitFace</code> - face used to resolve alignment</dd>
<dt>Returns:</dt>
<dd>adapted start corner</dd>
</dl>
</div>
:::


</section>

<section id="adaptEndCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)">

:::tabs
== adaptEndCorner
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">adaptEndCorner</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;startPosition,
 net.minecraft.world.phys.Vec3&nbsp;endPosition,
 net.minecraft.core.Direction&nbsp;hitFace)</span></div>
Adapts the second corner of a measurement to this mode's grid.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>startPosition</code> - other measurement endpoint</dd>
<dd><code>endPosition</code> - clicked end position</dd>
<dd><code>hitFace</code> - face used to resolve alignment</dd>
<dt>Returns:</dt>
<dd>adapted end corner</dd>
</dl>
</div>
:::


</section>

<section id="getResolution()">

:::tabs
== getResolution
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getResolution</span>()</div>
Returns the coordinate spacing used by this measuring mode.
<dl class="notes">
<dt>Returns:</dt>
<dd>the requested value.</dd>
</dl>
</div>
:::


</section>

<section id="isNeedsNormalization()">

:::tabs
== isNeedsNormalization
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isNeedsNormalization</span>()</div>
Returns whether adapted measurement positions should be normalized.
<dl class="notes">
<dt>Returns:</dt>
<dd>whether the requested condition holds.</dd>
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
<dd><code><a href="../item/withmode/group/IToolModeGroup.html#shouldRenderOnHotBar()">shouldRenderOnHotBar</a></code>&nbsp;in interface&nbsp;<code><a href="../item/withmode/group/IToolModeGroup.html" title="interface in mod.chiselsandbits.api.item.withmode.group">IToolModeGroup</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../util/IWithIcon.html#shouldRenderOnHotBar()">shouldRenderOnHotBar</a></code>&nbsp;in interface&nbsp;<code><a href="../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> when we should render it on the hotbar.</dd>
</dl>
</div>
:::


</section>

:::::
  

