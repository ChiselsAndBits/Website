--- 
title: IToolMode
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.withmode](index.md)  
# Interface IToolMode\<G extends IToolModeGroup\>  
**All Extended Interfaces:**  
[IRenderableMode](IRenderableMode.md), [IWithColor](../../util/IWithColor.md), [IWithDisplayName](../../util/IWithDisplayName.md), [IWithIcon](../../util/IWithIcon.md), [IWithIconAndColor](../../util/IWithIconAndColor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IToolMode&lt;G extends <a href="group/IToolModeGroup.html" title="interface in mod.chiselsandbits.api.item.withmode.group">IToolModeGroup</a>&gt;</span><span class="extends-implements"><br/>  
extends <a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a>, <a href="IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a></span></div>  

  

A mode of a given tool.  

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
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="#type-param-G" title="type parameter in IToolMode">G</a>&gt;</code></td><td><code><a href="#getGroup()" class="member-name-link">getGroup</a>()</code></td><td><div class="block">An optional which indicates the group this tool mode<br>is part of.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="#type-param-G" title="type parameter in IToolMode">G</a>&gt;</code></td><td><code><a href="#getGroup()" class="member-name-link">getGroup</a>()</code></td><td><div class="block">An optional which indicates the group this tool mode<br>is part of.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="#type-param-G" title="type parameter in IToolMode">G</a>&gt;</code></td><td><code><a href="#getGroup()" class="member-name-link">getGroup</a>()</code></td><td><div class="block">An optional which indicates the group this tool mode<br>is part of.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a><a href="IRenderableMode.html#getColorVector()" title="getColorVector()">getColorVector</a>, <a href="IRenderableMode.html#getPositionVector()" title="getPositionVector()">getPositionVector</a>, <a href="IRenderableMode.html#getScaleVector()" title="getScaleVector()">getScaleVector</a>, <a href="IRenderableMode.html#isActive()" title="isActive()">isActive</a>, <a href="IRenderableMode.html#shouldRenderDisplayNameInMenu()" title="shouldRenderDisplayNameInMenu()">shouldRenderDisplayNameInMenu</a>, <a href="IRenderableMode.html#shouldRenderName()" title="shouldRenderName()">shouldRenderName</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a><a href="../../util/IWithColor.html#getAlphaChannel()" title="getAlphaChannel()">getAlphaChannel</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a><a href="../../util/IWithDisplayName.html#getDisplayName()" title="getDisplayName()">getDisplayName</a>, <a href="../../util/IWithDisplayName.html#getMultiLineDisplayName()" title="getMultiLineDisplayName()">getMultiLineDisplayName</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a><a href="../../util/IWithIcon.html#getIcon()" title="getIcon()">getIcon</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getGroup()">
:::tabs
== getGroup
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="#type-param-G" title="type parameter in IToolMode">G</a>&gt;</span>&nbsp;<span class="element-name">getGroup</span>()</div>
An optional which indicates the group this tool mode
is part of.
<dl class="notes">
<dt>Returns:</dt>
<dd>The optional tool mode group.</dd>
</dl>
</div>
:::
</section>
:::::
  

