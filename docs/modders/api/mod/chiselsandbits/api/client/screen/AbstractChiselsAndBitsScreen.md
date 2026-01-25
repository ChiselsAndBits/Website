--- 
title: AbstractChiselsAndBitsScreen
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.screen](index.md)  
# Class AbstractChiselsAndBitsScreen  
java.lang.Object  
&ensp;↳net.minecraft.client.gui.components.events.AbstractContainerEventHandler  
&ensp;&ensp;↳net.minecraft.client.gui.screens.Screen  
&ensp;&ensp;&ensp;↳mod.chiselsandbits.api.client.screen.AbstractChiselsAndBitsScreen  
  
**All Implemented Interfaces:**  
[IChiselsAndBitsScreen](IChiselsAndBitsScreen.md)  

---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">AbstractChiselsAndBitsScreen</span><br/>  
<span class="extends-implements">extends net.minecraft.client.gui.screens.Screen<br/>  
implements <a href="IChiselsAndBitsScreen.html" title="interface in mod.chiselsandbits.api.client.screen">IChiselsAndBitsScreen</a></span></div>  

  

<div class="block">Custom screens which inherit from this class implement custom logic related to chisels and bits widgets and buttons.</div>
  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 2 -->
::::::: info Nested Class Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from class&nbsp;net.minecraft.client.gui.screens.Screen
net.minecraft.client.gui.screens.Screen.NarratableSearchResult
:::::
:::::::
  
  
<!-- =========== FIELD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Field Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Fields inherited from class&nbsp;net.minecraft.client.gui.screens.Screen
children, FADE_IN_TIME, font, FOOTER_SEPARATOR, HEADER_SEPARATOR, height, INWORLD_FOOTER_SEPARATOR, INWORLD_HEADER_SEPARATOR, MENU_BACKGROUND, minecraft, narratables, narratorButton, screenExecutor, title, width
:::::
:::::::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Summary  
:::tabs
== Constructors
<table>
  <thead>
    <tr><th>Modifier</th><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected </code></td><td><code><a href="#%3Cinit%3E(net.minecraft.network.chat.Component)" class="member-name-link">AbstractChiselsAndBitsScreen</a><wbr>(net.minecraft.network.chat.Component&nbsp;narrationMessage)</code></td><td><div class="block">Creates a new screen, playing the narration message when opened.</div><br></td></tr>
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
  <tr><td><code>protected &lt;T extends net.minecraft.client.gui.components.Renderable&gt;<br>T</code></td><td><code><a href="#addRenderableOnly(T)" class="member-name-link">addRenderableOnly</a><wbr>(T&nbsp;widget)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T extends net.minecraft.client.gui.components.events.GuiEventListener &amp; net.minecraft.client.gui.components.Renderable &amp; net.minecraft.client.gui.narration.NarratableEntry&gt;<br>T</code></td><td><code><a href="#addRenderableWidget(T)" class="member-name-link">addRenderableWidget</a><wbr>(T&nbsp;button)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T extends net.minecraft.client.gui.components.events.GuiEventListener &amp; net.minecraft.client.gui.narration.NarratableEntry&gt;<br>T</code></td><td><code><a href="#addWidget(T)" class="member-name-link">addWidget</a><wbr>(T&nbsp;widget)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#clearWidgets()" class="member-name-link">clearWidgets</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="widget/IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a>&gt;</code></td><td><code><a href="#getWidgets()" class="member-name-link">getWidgets</a>()</code></td><td><div class="block">Returns the widgets which are included in the screen.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInitialized()" class="member-name-link">isInitialized</a>()</code></td><td><div class="block">Indicates if the screen has been initialized or not.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeWidget(net.minecraft.client.gui.components.events.GuiEventListener)" class="member-name-link">removeWidget</a><wbr>(@NotNull net.minecraft.client.gui.components.events.GuiEventListener&nbsp;listener)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#render(net.minecraft.client.gui.GuiGraphics,int,int,float)" class="member-name-link">render</a><wbr>(@NotNull net.minecraft.client.gui.GuiGraphics&nbsp;guiGraphics,<br> int&nbsp;mouseX,<br> int&nbsp;mouseY,<br> float&nbsp;partialTickTime)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected &lt;T extends net.minecraft.client.gui.components.Renderable&gt;<br>T</code></td><td><code><a href="#addRenderableOnly(T)" class="member-name-link">addRenderableOnly</a><wbr>(T&nbsp;widget)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T extends net.minecraft.client.gui.components.events.GuiEventListener &amp; net.minecraft.client.gui.components.Renderable &amp; net.minecraft.client.gui.narration.NarratableEntry&gt;<br>T</code></td><td><code><a href="#addRenderableWidget(T)" class="member-name-link">addRenderableWidget</a><wbr>(T&nbsp;button)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T extends net.minecraft.client.gui.components.events.GuiEventListener &amp; net.minecraft.client.gui.narration.NarratableEntry&gt;<br>T</code></td><td><code><a href="#addWidget(T)" class="member-name-link">addWidget</a><wbr>(T&nbsp;widget)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#clearWidgets()" class="member-name-link">clearWidgets</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="widget/IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a>&gt;</code></td><td><code><a href="#getWidgets()" class="member-name-link">getWidgets</a>()</code></td><td><div class="block">Returns the widgets which are included in the screen.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInitialized()" class="member-name-link">isInitialized</a>()</code></td><td><div class="block">Indicates if the screen has been initialized or not.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeWidget(net.minecraft.client.gui.components.events.GuiEventListener)" class="member-name-link">removeWidget</a><wbr>(@NotNull net.minecraft.client.gui.components.events.GuiEventListener&nbsp;listener)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#render(net.minecraft.client.gui.GuiGraphics,int,int,float)" class="member-name-link">render</a><wbr>(@NotNull net.minecraft.client.gui.GuiGraphics&nbsp;guiGraphics,<br> int&nbsp;mouseX,<br> int&nbsp;mouseY,<br> float&nbsp;partialTickTime)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>protected &lt;T extends net.minecraft.client.gui.components.Renderable&gt;<br>T</code></td><td><code><a href="#addRenderableOnly(T)" class="member-name-link">addRenderableOnly</a><wbr>(T&nbsp;widget)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T extends net.minecraft.client.gui.components.events.GuiEventListener &amp; net.minecraft.client.gui.components.Renderable &amp; net.minecraft.client.gui.narration.NarratableEntry&gt;<br>T</code></td><td><code><a href="#addRenderableWidget(T)" class="member-name-link">addRenderableWidget</a><wbr>(T&nbsp;button)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>&lt;T extends net.minecraft.client.gui.components.events.GuiEventListener &amp; net.minecraft.client.gui.narration.NarratableEntry&gt;<br>T</code></td><td><code><a href="#addWidget(T)" class="member-name-link">addWidget</a><wbr>(T&nbsp;widget)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#clearWidgets()" class="member-name-link">clearWidgets</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="widget/IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a>&gt;</code></td><td><code><a href="#getWidgets()" class="member-name-link">getWidgets</a>()</code></td><td><div class="block">Returns the widgets which are included in the screen.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#init()" class="member-name-link">init</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInitialized()" class="member-name-link">isInitialized</a>()</code></td><td><div class="block">Indicates if the screen has been initialized or not.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removed()" class="member-name-link">removed</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeWidget(net.minecraft.client.gui.components.events.GuiEventListener)" class="member-name-link">removeWidget</a><wbr>(@NotNull net.minecraft.client.gui.components.events.GuiEventListener&nbsp;listener)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#render(net.minecraft.client.gui.GuiGraphics,int,int,float)" class="member-name-link">render</a><wbr>(@NotNull net.minecraft.client.gui.GuiGraphics&nbsp;guiGraphics,<br> int&nbsp;mouseX,<br> int&nbsp;mouseY,<br> float&nbsp;partialTickTime)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;net.minecraft.client.gui.screens.Screen
added, afterKeyboardAction, afterMouseAction, afterMouseMove, canInterruptWithAnotherScreen, changeFocus, children, clearFocus, clickCommandAction, clickUrlAction, defaultHandleClickEvent, defaultHandleGameClickEvent, fadeWidgets, fillCrashDetails, findNarratableWidget, getBackgroundMusic, getFont, getNarrationMessage, getRectangle, getTitle, getTooltipFromItem, getUsageNarration, handleDelayedNarration, init, insertText, isAllowedInPortal, isInGameUi, isMouseOver, isPauseScreen, isValidCharacterForName, keyPressed, onClose, onFilesDrop, panoramaShouldSpin, rebuildWidgets, renderBackground, renderBlurredBackground, renderMenuBackground, renderMenuBackground, renderMenuBackgroundTexture, renderPanorama, renderTransparentBackground, renderWithTooltipAndSubtitles, repositionElements, resize, setInitialFocus, setInitialFocus, shouldCloseOnEsc, shouldNarrateNavigation, showsActiveEffects, tick, triggerImmediateNarration, updateNarratedWidget, updateNarrationState, updateNarratorStatus
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;net.minecraft.client.gui.components.events.AbstractContainerEventHandler
getFocused, isDragging, setDragging, setFocused
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.client.gui.components.events.ContainerEventHandler
charTyped, getChildAt, getCurrentFocusPath, isFocused, keyReleased, mouseClicked, mouseDragged, mouseReleased, mouseScrolled, nextFocusPath, setFocused
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.client.gui.components.events.GuiEventListener
getBorderForArrowNavigation, mouseMoved, shouldTakeFocusAfterInteraction
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;net.minecraft.client.gui.components.TabOrderedElement
getTabOrderGroup
:::::
:::::::
  
  
  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(net.minecraft.network.chat.Component)">

:::tabs
== AbstractChiselsAndBitsScreen
<div class="member-signature"><span class="modifiers">protected</span>&nbsp;<span class="element-name">AbstractChiselsAndBitsScreen</span><wbr><span class="parameters">(net.minecraft.network.chat.Component&nbsp;narrationMessage)</span></div>
<div class="block">Creates a new screen, playing the narration message when opened.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>narrationMessage</code> - The narration message for the screen.</dd>
</dl>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="init()">

:::tabs
== init
<div class="member-signature"><span class="modifiers">protected</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">init</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>init</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.screens.Screen</code></dd>
</dl>
:::


</section>

<section id="addRenderableWidget(T)">

:::tabs
== addRenderableWidget
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">public</span>&nbsp;<span class="type-parameters-long">&lt;T extends net.minecraft.client.gui.components.events.GuiEventListener &amp; net.minecraft.client.gui.components.Renderable &amp; net.minecraft.client.gui.narration.NarratableEntry&gt;</span>
<span class="return-type">T</span>&nbsp;<span class="element-name">addRenderableWidget</span><wbr><span class="parameters">(@NotNull
 T&nbsp;button)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addRenderableWidget</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.screens.Screen</code></dd>
</dl>
:::


</section>

<section id="addRenderableOnly(T)">

:::tabs
== addRenderableOnly
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">protected</span>&nbsp;<span class="type-parameters-long">&lt;T extends net.minecraft.client.gui.components.Renderable&gt;</span>
<span class="return-type">T</span>&nbsp;<span class="element-name">addRenderableOnly</span><wbr><span class="parameters">(@NotNull
 T&nbsp;widget)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addRenderableOnly</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.screens.Screen</code></dd>
</dl>
:::


</section>

<section id="addWidget(T)">

:::tabs
== addWidget
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">public</span>&nbsp;<span class="type-parameters-long">&lt;T extends net.minecraft.client.gui.components.events.GuiEventListener &amp; net.minecraft.client.gui.narration.NarratableEntry&gt;</span>
<span class="return-type">T</span>&nbsp;<span class="element-name">addWidget</span><wbr><span class="parameters">(@NotNull
 T&nbsp;widget)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addWidget</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.screens.Screen</code></dd>
</dl>
:::


</section>

<section id="removeWidget(net.minecraft.client.gui.components.events.GuiEventListener)">

:::tabs
== removeWidget
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">removeWidget</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.client.gui.components.events.GuiEventListener&nbsp;listener)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>removeWidget</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.screens.Screen</code></dd>
</dl>
:::


</section>

<section id="clearWidgets()">

:::tabs
== clearWidgets
<div class="member-signature"><span class="modifiers">protected</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">clearWidgets</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>clearWidgets</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.screens.Screen</code></dd>
</dl>
:::


</section>

<section id="removed()">

:::tabs
== removed
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">removed</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>removed</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.screens.Screen</code></dd>
</dl>
:::


</section>

<section id="isInitialized()">

:::tabs
== isInitialized
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isInitialized</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface:&nbsp;<code><a href="IChiselsAndBitsScreen.html#isInitialized()">IChiselsAndBitsScreen</a></code></span></div>
<div class="block">Indicates if the screen has been initialized or not.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IChiselsAndBitsScreen.html#isInitialized()">isInitialized</a></code>&nbsp;in interface&nbsp;<code><a href="IChiselsAndBitsScreen.html" title="interface in mod.chiselsandbits.api.client.screen">IChiselsAndBitsScreen</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if the screen has been initialized, <code>false</code> otherwise.</dd>
</dl>
:::


</section>

<section id="getWidgets()">

:::tabs
== getWidgets
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="widget/IChiselsAndBitsWidget.html" title="interface in mod.chiselsandbits.api.client.screen.widget">IChiselsAndBitsWidget</a>&gt;</span>&nbsp;<span class="element-name">getWidgets</span>()</div>
<div class="block">Returns the widgets which are included in the screen.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The widgets on this screen.</dd>
</dl>
:::


</section>

<section id="render(net.minecraft.client.gui.GuiGraphics,int,int,float)">

:::tabs
== render
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">render</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.client.gui.GuiGraphics&nbsp;guiGraphics,
 int&nbsp;mouseX,
 int&nbsp;mouseY,
 float&nbsp;partialTickTime)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>render</code>&nbsp;in interface&nbsp;<code>net.minecraft.client.gui.components.Renderable</code></dd>
<dt>Overrides:</dt>
<dd><code>render</code>&nbsp;in class&nbsp;<code>net.minecraft.client.gui.screens.Screen</code></dd>
</dl>
:::


</section>

:::::
  

