--- 
title: AbstractChiselsAndBitsButton
aside: false 
---
_Package:_ [mod.chiselsandbits.api.client.screen.widget](index.md)  
# Class AbstractChiselsAndBitsButton  
java.lang.Object  
&ensp;↳net.minecraft.client.gui.components.AbstractWidget  
&ensp;&ensp;↳net.minecraft.client.gui.components.WithInactiveMessage  
&ensp;&ensp;&ensp;↳net.minecraft.client.gui.components.AbstractButton  
&ensp;&ensp;&ensp;&ensp;↳net.minecraft.client.gui.components.Button  
&ensp;&ensp;&ensp;&ensp;&ensp;↳mod.chiselsandbits.api.client.screen.widget.AbstractChiselsAndBitsButton  
  
**All Implemented Interfaces:**  
[IChiselsAndBitsWidget](IChiselsAndBitsWidget.md)  

---
<div class="type-signature"><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractChiselsAndBitsButton</span><br/>  
<span class="extends-implements">extends net.minecraft.client.gui.components.Button<br/>  
implements <a href="IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a></span></div>  

  

<div class="block">An abstract chisels and bits button.
 Is used to be able to retroactively initialize a button when it's containing screen is initialized.</div>
  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 2 -->
::::::: info Nested Class Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from class&nbsp;net.minecraft.client.gui.components.Button
net.minecraft.client.gui.components.Button.Builder, net.minecraft.client.gui.components.Button.CreateNarration, net.minecraft.client.gui.components.Button.OnPress, net.minecraft.client.gui.components.Button.Plain
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from class&nbsp;net.minecraft.client.gui.components.AbstractWidget
net.minecraft.client.gui.components.AbstractWidget.WithInactiveMessage
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from interface&nbsp;net.minecraft.client.gui.narration.NarratableEntry
net.minecraft.client.gui.narration.NarratableEntry.NarrationPriority
:::::
:::::::
  
  
<!-- =========== FIELD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Field Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Fields inherited from class&nbsp;net.minecraft.client.gui.components.Button
BIG_WIDTH, createNarration, DEFAULT_HEIGHT, DEFAULT_NARRATION, DEFAULT_SPACING, DEFAULT_WIDTH, onPress, SMALL_WIDTH
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Fields inherited from class&nbsp;net.minecraft.client.gui.components.AbstractButton
TEXT_MARGIN
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Fields inherited from class&nbsp;net.minecraft.client.gui.components.AbstractWidget
active, alpha, height, isHovered, message, visible, width
:::::
:::::::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Summary  
:::tabs
== Constructors
<table>
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E(int,int,int,int,net.minecraft.network.chat.Component,net.minecraft.client.gui.components.Button.OnPress,net.minecraft.client.gui.components.Button.CreateNarration)" class="member-name-link">AbstractChiselsAndBitsButton</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;width,<br> int&nbsp;height,<br> net.minecraft.network.chat.Component&nbsp;narration,<br> net.minecraft.client.gui.components.Button.OnPress&nbsp;pressable,<br> net.minecraft.client.gui.components.Button.CreateNarration&nbsp;tooltip)</code></td><td><div class="block">Creates a new button with a tooltip.</div><br></td></tr>
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
  <tr><td><code>void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td><div class="block">Invoked by the screen, when said screen is initialized.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td><div class="block">Invoked by the screen, when it is removed from the display.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td><div class="block">Invoked by the screen, when said screen is initialized.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td><div class="block">Invoked by the screen, when it is removed from the display.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td><div class="block">Invoked by the screen, when said screen is initialized.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td><div class="block">Invoked by the screen, when it is removed from the display.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;net.minecraft.client.gui.components.Button
builder, createNarrationMessage, onPress, updateWidgetNarration
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;net.minecraft.client.gui.components.AbstractButton
keyPressed, onClick, renderContents, renderDefaultLabel, renderDefaultSprite, renderWidget, setOverrideRenderHighlightedSprite
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;net.minecraft.client.gui.components.AbstractWidget.WithInactiveMessage
defaultInactiveMessage, getMessage, setMessage
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;net.minecraft.client.gui.components.AbstractWidget
defaultButtonNarrationText, getAlpha, getBottom, getHeight, getRectangle, getRight, getTabOrderGroup, getWidth, getX, getY, handleCursor, isActive, isFocused, isHovered, isHoveredOrFocused, isMouseOver, isValidClickButton, mouseClicked, mouseDragged, mouseReleased, narrationPriority, nextFocusPath, onDrag, onRelease, playButtonClickSound, playDownSound, render, renderScrollingStringOverContents, setAlpha, setFocused, setHeight, setRectangle, setSize, setTabOrderGroup, setTooltip, setTooltipDelay, setWidth, setX, setY, updateNarration, visitWidgets, wrapDefaultNarrationMessage
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.client.gui.components.events.GuiEventListener
charTyped, getBorderForArrowNavigation, getCurrentFocusPath, getRectangle, isFocused, isMouseOver, keyPressed, keyReleased, mouseClicked, mouseDragged, mouseMoved, mouseReleased, mouseScrolled, nextFocusPath, setFocused, shouldTakeFocusAfterInteraction
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.client.gui.layouts.LayoutElement
setPosition
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.client.gui.narration.NarratableEntry
getNarratables
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.client.gui.components.Renderable
render
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.client.gui.components.TabOrderedElement
getTabOrderGroup
:::::
:::::::
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(int,int,int,int,net.minecraft.network.chat.Component,net.minecraft.client.gui.components.Button.OnPress,net.minecraft.client.gui.components.Button.CreateNarration)">

:::tabs
== AbstractChiselsAndBitsButton
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">AbstractChiselsAndBitsButton</span><wbr><span class="parameters">(int&nbsp;x,
 int&nbsp;y,
 int&nbsp;width,
 int&nbsp;height,
 net.minecraft.network.chat.Component&nbsp;narration,
 net.minecraft.client.gui.components.Button.OnPress&nbsp;pressable,
 net.minecraft.client.gui.components.Button.CreateNarration&nbsp;tooltip)</span></div>
<div class="block">Creates a new button with a tooltip.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - The x position.</dd>
<dd><code>y</code> - The y position.</dd>
<dd><code>width</code> - The width.</dd>
<dd><code>height</code> - The height.</dd>
<dd><code>narration</code> - The narration message.</dd>
<dd><code>pressable</code> - The press callback.</dd>
<dd><code>tooltip</code> - The tooltip handling logic.</dd>
</dl>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="init()">

:::tabs
== init
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">init</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="IChiselsAndBitsWidget.html#init()">IChiselsAndBitsWidget</a></code></span></div>
<div class="block">Invoked by the screen, when said screen is initialized.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IChiselsAndBitsWidget.html#init()">init</a></code>&nbsp;in interface&nbsp;<code><a href="IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a></code></dd>
</dl>
:::


</section>

<section id="removed()">

:::tabs
== removed
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">removed</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="IChiselsAndBitsWidget.html#removed()">IChiselsAndBitsWidget</a></code></span></div>
<div class="block">Invoked by the screen, when it is removed from the display.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IChiselsAndBitsWidget.html#removed()">removed</a></code>&nbsp;in interface&nbsp;<code><a href="IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a></code></dd>
</dl>
:::


</section>

:::::
  

