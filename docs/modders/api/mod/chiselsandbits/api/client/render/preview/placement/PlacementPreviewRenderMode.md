--- 
title: PlacementPreviewRenderMode
aside: false 
---
_Package:_ [mod.chiselsandbits.api.client.render.preview.placement](index.md)  
# Enum PlacementPreviewRenderMode  
---
<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">PlacementPreviewRenderMode</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>&lt;<a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>&gt;</span></div>  

  

<div class="block">Determines the way chiseled block and pattern placement previews will render.
 This value can be independently set for how successful and failed placement renders.</div>
  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 2 -->
::::::: info Nested Class Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">Enum.EnumDesc</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">E</a> extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">E</a>&gt;&gt;
:::::
:::::::
  
  
<!-- JavaMarkContainer Depth: 1 -->
::::: info Enum Constant Summary  
:::tabs
== Enum Constants
<table>
  <thead>
    <tr><th>Enum Constant</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#GHOST_BLOCK_MODEL" class="member-name-link">GHOST_BLOCK_MODEL</a></code></td><td><div class="block">Causes the preview to render as a ghost of the model of the block to be placed</div><br></td></tr>
  <tr><td><code><a href="#GHOST_BLOCK_MODEL_SOLID_COLOR" class="member-name-link">GHOST_BLOCK_MODEL_SOLID_COLOR</a></code></td><td><div class="block">Causes the preview to render the model of the block, such that the block's textures are<br> ignored, and each quad  is rendered with the RGBA value specified by the result of placement</div><br></td></tr>
  <tr><td><code><a href="#WIREFRAME" class="member-name-link">WIREFRAME</a></code></td><td><div class="block">Causes the preview to render a wireframe comprised of the edges of the block's model<br> with the RGB value specified by the result of placement</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
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
  <tr><td><code>boolean</code></td><td><code><a href="#isColoredGhost()" class="member-name-link">isColoredGhost</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isGhost()" class="member-name-link">isGhost</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isWireframe()" class="member-name-link">isWireframe</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isColoredGhost()" class="member-name-link">isColoredGhost</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isGhost()" class="member-name-link">isGhost</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isWireframe()" class="member-name-link">isWireframe</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isColoredGhost()" class="member-name-link">isColoredGhost</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isGhost()" class="member-name-link">isGhost</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isWireframe()" class="member-name-link">isWireframe</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang" class="external-link">compareTo</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang" class="external-link">describeConstable</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang" class="external-link">getDeclaringClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang" class="external-link">name</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang" class="external-link">ordinal</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang" class="external-link">valueOf</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Enum Constant Details  
<section id="GHOST_BLOCK_MODEL">

:::tabs
== GHOST_BLOCK_MODEL
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a></span>&nbsp;<span class="element-name">GHOST_BLOCK_MODEL</span></div>
<div class="block">Causes the preview to render as a ghost of the model of the block to be placed</div>
<dl class="notes"></dl>
:::


</section>

<section id="GHOST_BLOCK_MODEL_SOLID_COLOR">

:::tabs
== GHOST_BLOCK_MODEL_SOLID_COLOR
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a></span>&nbsp;<span class="element-name">GHOST_BLOCK_MODEL_SOLID_COLOR</span></div>
<div class="block">Causes the preview to render the model of the block, such that the block's textures are
 ignored, and each quad  is rendered with the RGBA value specified by the result of placement</div>
<dl class="notes"></dl>
:::


</section>

<section id="WIREFRAME">

:::tabs
== WIREFRAME
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a></span>&nbsp;<span class="element-name">WIREFRAME</span></div>
<div class="block">Causes the preview to render a wireframe comprised of the edges of the block's model
 with the RGB value specified by the result of placement</div>
<dl class="notes"></dl>
:::


</section>

:::::
  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="values()">

:::tabs
== values
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a>[]</span>&nbsp;<span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
:::


</section>

<section id="valueOf(java.lang.String)">

:::tabs
== valueOf
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementPreviewRenderMode.html" title="enum class in mod.chiselsandbits.api.client.render.preview.placement">PlacementPreviewRenderMode</a></span>&nbsp;<span class="element-name">valueOf</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang" class="external-link">NullPointerException</a></code> - if the argument is null</dd>
</dl>
:::


</section>

<section id="isGhost()">

:::tabs
== isGhost
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isGhost</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="isColoredGhost()">

:::tabs
== isColoredGhost
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isColoredGhost</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="isWireframe()">

:::tabs
== isWireframe
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isWireframe</span>()</div>
<dl class="notes"></dl>
:::


</section>

:::::
  

