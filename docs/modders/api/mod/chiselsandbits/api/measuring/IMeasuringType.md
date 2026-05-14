--- 
title: IMeasuringType
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.measuring](index.md)  
# Interface IMeasuringType  
**All Extended Interfaces:**  
[IToolModeGroup](../item/withmode/group/IToolModeGroup.md), [IRenderableMode](../item/withmode/IRenderableMode.md), [IWithColor](../util/IWithColor.md), [IWithDisplayName](../util/IWithDisplayName.md), [IWithIcon](../util/IWithIcon.md), [IWithIconAndColor](../util/IWithIconAndColor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMeasuringType</span><span class="extends-implements"><br/>  
extends <a href="../item/withmode/group/IToolModeGroup.html" title="interface in mod.chiselsandbits.api.item.withmode.group">IToolModeGroup</a></span></div>  

  

  

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
  <tr><td><code>static interface&nbsp;</code></td><td><code><a href="IMeasuringType.IClickedPositionAdapter.html" class="type-name-link" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType.IClickedPositionAdapter</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static interface&nbsp;</code></td><td><code><a href="IMeasuringType.IPositionAdapter.html" class="type-name-link" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType.IPositionAdapter</a></code></td><td>&nbsp;</td></tr>
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
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptClickedPosition(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adaptClickedPosition</a><wbr>(@NotNull net.minecraft.world.phys.BlockHitResult&nbsp;blockHitResult)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptEndCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptEndCorner</a><wbr>(@NotNull net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> @NotNull net.minecraft.core.Direction&nbsp;hitFace)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptStartCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptStartCorner</a><wbr>(@NotNull net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> @NotNull net.minecraft.core.Direction&nbsp;hitFace)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getResolution()" class="member-name-link">getResolution</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isNeedsNormalization()" class="member-name-link">isNeedsNormalization</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptClickedPosition(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adaptClickedPosition</a><wbr>(@NotNull net.minecraft.world.phys.BlockHitResult&nbsp;blockHitResult)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptEndCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptEndCorner</a><wbr>(@NotNull net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> @NotNull net.minecraft.core.Direction&nbsp;hitFace)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptStartCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptStartCorner</a><wbr>(@NotNull net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> @NotNull net.minecraft.core.Direction&nbsp;hitFace)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getResolution()" class="member-name-link">getResolution</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isNeedsNormalization()" class="member-name-link">isNeedsNormalization</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptClickedPosition(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adaptClickedPosition</a><wbr>(@NotNull net.minecraft.world.phys.BlockHitResult&nbsp;blockHitResult)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptEndCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptEndCorner</a><wbr>(@NotNull net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> @NotNull net.minecraft.core.Direction&nbsp;hitFace)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adaptStartCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adaptStartCorner</a><wbr>(@NotNull net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> @NotNull net.minecraft.core.Direction&nbsp;hitFace)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getResolution()" class="member-name-link">getResolution</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isNeedsNormalization()" class="member-name-link">isNeedsNormalization</a>()</code></td><td>&nbsp;</td></tr>
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
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">adaptClickedPosition</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.phys.BlockHitResult&nbsp;blockHitResult)</span></div>
</div>
:::


</section>

<section id="adaptStartCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)">

:::tabs
== adaptStartCorner
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">adaptStartCorner</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.phys.Vec3&nbsp;startPosition,
 @NotNull
 @NotNull net.minecraft.world.phys.Vec3&nbsp;endPosition,
 @NotNull
 @NotNull net.minecraft.core.Direction&nbsp;hitFace)</span></div>
</div>
:::


</section>

<section id="adaptEndCorner(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)">

:::tabs
== adaptEndCorner
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">adaptEndCorner</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.phys.Vec3&nbsp;startPosition,
 @NotNull
 @NotNull net.minecraft.world.phys.Vec3&nbsp;endPosition,
 @NotNull
 @NotNull net.minecraft.core.Direction&nbsp;hitFace)</span></div>
</div>
:::


</section>

<section id="getResolution()">

:::tabs
== getResolution
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getResolution</span>()</div>
</div>
:::


</section>

<section id="isNeedsNormalization()">

:::tabs
== isNeedsNormalization
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isNeedsNormalization</span>()</div>
</div>
:::


</section>

:::::
  

