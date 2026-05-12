--- 
title: AbstractChiselsAndBitsWidget
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.screen.widget](index.md)  
# Class AbstractChiselsAndBitsWidget  
java.lang.Object  
&ensp;↳net.minecraft.client.gui.components.AbstractWidget  
&ensp;&ensp;↳mod.chiselsandbits.api.client.screen.widget.AbstractChiselsAndBitsWidget  
  
**All Implemented Interfaces:**  
[IChiselsAndBitsWidget](IChiselsAndBitsWidget.md)  

---
<div class="type-signature"><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractChiselsAndBitsWidget</span><br/>  
<span class="extends-implements">extends net.minecraft.client.gui.components.AbstractWidget<br/>  
implements <a href="IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a></span></div>  

  

All chisels and bits widgets inherit from this class.
Most notably provides init support, invoked when the window itself has its init method called.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
Nested classes/interfaces inherited from class&nbsp;net.minecraft.client.gui.components.AbstractWidgetnet.minecraft.client.gui.components.AbstractWidget.WithInactiveMessageNested classes/interfaces inherited from interface&nbsp;net.minecraft.client.gui.narration.NarratableEntrynet.minecraft.client.gui.narration.NarratableEntry.NarrationPriority
:::::
  
  
<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
Fields inherited from class&nbsp;net.minecraft.client.gui.components.AbstractWidgetactive, alpha, height, isHovered, message, visible, width
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E(int,int,int,int,net.minecraft.network.chat.Component)" class="member-name-link">AbstractChiselsAndBitsWidget</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;width,<br> int&nbsp;height,<br> net.minecraft.network.chat.Component&nbsp;narration)</code></td><td><div class="block">Creates a new widget.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected static com.communi.suggestu.scena.core.client.rendering.IExtendedGuiGraphics</code></td><td><code><a href="#getExtendedGraphicsExtractor(net.minecraft.client.gui.GuiGraphicsExtractor)" class="member-name-link">getExtendedGraphicsExtractor</a><wbr>(@NotNull net.minecraft.client.gui.GuiGraphicsExtractor&nbsp;graphics)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.client.gui.Font</code></td><td><code><a href="#getFont()" class="member-name-link">getFont</a>()</code></td><td><div class="block">The font used in this widget.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.client.Minecraft</code></td><td><code><a href="#getMinecraft()" class="member-name-link">getMinecraft</a>()</code></td><td><div class="block">Gives access to the current instance of minecraft.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td><div class="block">Invoked by the screen, when said screen is initialized.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td><div class="block">Invoked by the screen, when it is removed from the display.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#updateWidgetNarration(net.minecraft.client.gui.narration.NarrationElementOutput)" class="member-name-link">updateWidgetNarration</a><wbr>(@NotNull net.minecraft.client.gui.narration.NarrationElementOutput&nbsp;output)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected static com.communi.suggestu.scena.core.client.rendering.IExtendedGuiGraphics</code></td><td><code><a href="#getExtendedGraphicsExtractor(net.minecraft.client.gui.GuiGraphicsExtractor)" class="member-name-link">getExtendedGraphicsExtractor</a><wbr>(@NotNull net.minecraft.client.gui.GuiGraphicsExtractor&nbsp;graphics)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>@NotNull net.minecraft.client.gui.Font</code></td><td><code><a href="#getFont()" class="member-name-link">getFont</a>()</code></td><td><div class="block">The font used in this widget.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.client.Minecraft</code></td><td><code><a href="#getMinecraft()" class="member-name-link">getMinecraft</a>()</code></td><td><div class="block">Gives access to the current instance of minecraft.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td><div class="block">Invoked by the screen, when said screen is initialized.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td><div class="block">Invoked by the screen, when it is removed from the display.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#updateWidgetNarration(net.minecraft.client.gui.narration.NarrationElementOutput)" class="member-name-link">updateWidgetNarration</a><wbr>(@NotNull net.minecraft.client.gui.narration.NarrationElementOutput&nbsp;output)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected static com.communi.suggestu.scena.core.client.rendering.IExtendedGuiGraphics</code></td><td><code><a href="#getExtendedGraphicsExtractor(net.minecraft.client.gui.GuiGraphicsExtractor)" class="member-name-link">getExtendedGraphicsExtractor</a><wbr>(@NotNull net.minecraft.client.gui.GuiGraphicsExtractor&nbsp;graphics)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>@NotNull net.minecraft.client.gui.Font</code></td><td><code><a href="#getFont()" class="member-name-link">getFont</a>()</code></td><td><div class="block">The font used in this widget.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.client.Minecraft</code></td><td><code><a href="#getMinecraft()" class="member-name-link">getMinecraft</a>()</code></td><td><div class="block">Gives access to the current instance of minecraft.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td><div class="block">Invoked by the screen, when said screen is initialized.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td><div class="block">Invoked by the screen, when it is removed from the display.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#updateWidgetNarration(net.minecraft.client.gui.narration.NarrationElementOutput)" class="member-name-link">updateWidgetNarration</a><wbr>(@NotNull net.minecraft.client.gui.narration.NarrationElementOutput&nbsp;output)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;net.minecraft.client.gui.components.AbstractWidgetcreateNarrationMessage, defaultButtonNarrationText, extractRenderState, extractScrollingStringOverContents, extractWidgetRenderState, getAlpha, getBottom, getHeight, getMessage, getRectangle, getRight, getTabOrderGroup, getWidth, getX, getY, handleCursor, isActive, isFocused, isHovered, isHoveredOrFocused, isMouseOver, isValidClickButton, mouseClicked, mouseDragged, mouseReleased, narrationPriority, nextFocusPath, onClick, onDrag, onRelease, playButtonClickSound, playDownSound, setAlpha, setFocused, setHeight, setMessage, setRectangle, setSize, setTabOrderGroup, setTooltip, setTooltipDelay, setWidth, setX, setY, updateNarration, visitWidgets, wrapDefaultNarrationMessageMethods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>Methods inherited from interface&nbsp;net.minecraft.client.gui.components.events.GuiEventListenercharTyped, getBorderForArrowNavigation, getCurrentFocusPath, getRectangle, isFocused, isMouseOver, keyPressed, keyReleased, mouseClicked, mouseDragged, mouseMoved, mouseReleased, mouseScrolled, nextFocusPath, preeditUpdated, setFocused, shouldTakeFocusAfterInteractionMethods inherited from interface&nbsp;net.minecraft.client.gui.layouts.LayoutElementsetPositionMethods inherited from interface&nbsp;net.minecraft.client.gui.narration.NarratableEntrygetNarratablesMethods inherited from interface&nbsp;net.minecraft.client.gui.components.RenderableextractRenderStateMethods inherited from interface&nbsp;net.minecraft.client.gui.components.TabOrderedElementgetTabOrderGroup
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(int,int,int,int,net.minecraft.network.chat.Component)">

:::tabs
== AbstractChiselsAndBitsWidget
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">AbstractChiselsAndBitsWidget</span><wbr><span class="parameters">(int&nbsp;x,
 int&nbsp;y,
 int&nbsp;width,
 int&nbsp;height,
 net.minecraft.network.chat.Component&nbsp;narration)</span></div>
<div class="block">Creates a new widget.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - The x position.</dd>
<dd><code>y</code> - The y position.</dd>
<dd><code>width</code> - The width.</dd>
<dd><code>height</code> - The height.</dd>
<dd><code>narration</code> - The narration text when selected.</dd>
</dl>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getMinecraft()">

:::tabs
== getMinecraft
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">public</span>&nbsp;<span class="return-type">@NotNull net.minecraft.client.Minecraft</span>&nbsp;<span class="element-name">getMinecraft</span>()</div>
<div class="block">Gives access to the current instance of minecraft.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The current instance of minecraft.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getFont()">

:::tabs
== getFont
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">public</span>&nbsp;<span class="return-type">@NotNull net.minecraft.client.gui.Font</span>&nbsp;<span class="element-name">getFont</span>()</div>
<div class="block">The font used in this widget.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The font used to render text in this widget.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="init()">

:::tabs
== init
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">init</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="IChiselsAndBitsWidget.html#init()">IChiselsAndBitsWidget</a></code></span></div>
<div class="block">Invoked by the screen, when said screen is initialized.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IChiselsAndBitsWidget.html#init()">init</a></code>&nbsp;in interface&nbsp;<code><a href="IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a></code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="removed()">

:::tabs
== removed
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">removed</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="IChiselsAndBitsWidget.html#removed()">IChiselsAndBitsWidget</a></code></span></div>
<div class="block">Invoked by the screen, when it is removed from the display.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IChiselsAndBitsWidget.html#removed()">removed</a></code>&nbsp;in interface&nbsp;<code><a href="IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a></code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="updateWidgetNarration(net.minecraft.client.gui.narration.NarrationElementOutput)">

:::tabs
== updateWidgetNarration
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">protected</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">updateWidgetNarration</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.client.gui.narration.NarrationElementOutput&nbsp;output)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>updateWidgetNarration</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.components.AbstractWidget</code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getExtendedGraphicsExtractor(net.minecraft.client.gui.GuiGraphicsExtractor)">

:::tabs
== getExtendedGraphicsExtractor
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">protected static</span>&nbsp;<span class="return-type">com.communi.suggestu.scena.core.client.rendering.IExtendedGuiGraphics</span>&nbsp;<span class="element-name">getExtendedGraphicsExtractor</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.client.gui.GuiGraphicsExtractor&nbsp;graphics)</span></div>
</div>
:::


</section>

</li>
</ul>
:::::
  

