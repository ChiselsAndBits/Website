--- 
title: IToolMode
aside: false 
---
_Package:_ [mod.chiselsandbits.api.item.withmode](index.md)  
# Interface IToolMode\<G extends IToolModeGroup\>  
**All Extended Interfaces:**  
[IRenderableMode](IRenderableMode.md), [IWithColor](../util/IWithColor.md), [IWithDisplayName](../util/IWithDisplayName.md), [IWithIcon](../util/IWithIcon.md), [IWithIconAndColor](../util/IWithIconAndColor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IToolMode&lt;G extends <a href="group/IToolModeGroup.html" title="interface in mod.chiselsandbits.api.item.withmode.group">IToolModeGroup</a>&gt;</span><span class="extends-implements"><br/>  
extends <a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a>, <a href="IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a></span></div>  

  

<div class="block">A mode of a given tool.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IToolMode.html" title="type parameter in IToolMode">G</a>&gt;</code></td><td><code><a href="#getGroup()" class="member-name-link">getGroup</a>()</code></td><td><div class="block">An optional which indicates the group this tool mode<br> is part of.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IToolMode.html" title="type parameter in IToolMode">G</a>&gt;</code></td><td><code><a href="#getGroup()" class="member-name-link">getGroup</a>()</code></td><td><div class="block">An optional which indicates the group this tool mode<br> is part of.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IToolMode.html" title="type parameter in IToolMode">G</a>&gt;</code></td><td><code><a href="#getGroup()" class="member-name-link">getGroup</a>()</code></td><td><div class="block">An optional which indicates the group this tool mode<br> is part of.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a>
<a href="IRenderableMode.html#getColorVector()">getColorVector</a>, <a href="IRenderableMode.html#getPositionVector()">getPositionVector</a>, <a href="IRenderableMode.html#getScaleVector()">getScaleVector</a>, <a href="IRenderableMode.html#isActive()">isActive</a>, <a href="IRenderableMode.html#shouldRenderDisplayNameInMenu()">shouldRenderDisplayNameInMenu</a>, <a href="IRenderableMode.html#shouldRenderName()">shouldRenderName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a>
<a href="../../util/IWithColor.html#getAlphaChannel()">getAlphaChannel</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a>
<a href="../../util/IWithDisplayName.html#getDisplayName()">getDisplayName</a>, <a href="../../util/IWithDisplayName.html#getMultiLineDisplayName()">getMultiLineDisplayName</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a>
<a href="../../util/IWithIcon.html#getIcon()">getIcon</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getGroup()">

:::tabs
== getGroup
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IToolMode.html" title="type parameter in IToolMode">G</a>&gt;</span>&nbsp;<span class="element-name">getGroup</span>()</div>
<div class="block">An optional which indicates the group this tool mode
 is part of.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The optional tool mode group.</dd>
</dl>
:::


</section>

:::::
  

