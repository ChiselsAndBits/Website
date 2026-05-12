--- 
title: IChiselMode
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling.mode](index.md)  
# Interface IChiselMode  
**All Extended Interfaces:**  
ICustomRegistryEntry, [IRenderableMode](../../item/withmode/IRenderableMode.md), [IToolMode\<IToolModeGroup\>](../../item/withmode/IToolMode.md), [IWithColor](../../util/IWithColor.md), [IWithDisplayName](../../util/IWithDisplayName.md), [IWithIcon](../../util/IWithIcon.md), [IWithIconAndColor](../../util/IWithIconAndColor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselMode</span><span class="extends-implements"><br/>  
extends com.communi.suggestu.scena.core.registries.ICustomRegistryEntry, <a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>&lt;<a href="../../item/withmode/group/IToolModeGroup.html" title="interface in mod.chiselsandbits.api.item.withmode.group">IToolModeGroup</a>&gt;</span></div>  

  

Represents a chiselable operation that can be completed by a chisel or bit for example.
<p>
    Has to be immutable as it is used in data components.
</p>  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;</code></td><td><code><a href="#getCurrentAccessor(mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">getCurrentAccessor</a><wbr>(<a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Performs an extraction and potential modification of the accessor for the given context as determined by this mode.</div><br></td></tr>
  <tr><td><code>static <a href="IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></code></td><td><code><a href="#getDefaultMode()" class="member-name-link">getDefaultMode</a>()</code></td><td><div class="block">The default mode of the chisel or bit.</div><br></td></tr>
  <tr><td><code>static com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;</code></td><td><code><a href="#getRegistry()" class="member-name-link">getRegistry</a>()</code></td><td><div class="block">The underlying registry that contains the different modes a chisel can assume.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getShape(mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">getShape</a><wbr>(<a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Defines the shape of the area that is to be chiseled.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isSingleClickUse()" class="member-name-link">isSingleClickUse</a>()</code></td><td><div class="block">Indicates if this mode requires a single click to trigger or not.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isStillValid(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext,mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">isStillValid</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context,<br> <a href="../ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperation)</code></td><td><div class="block">Checks if the passed context is still valid for the given entity.</div><br></td></tr>
  <tr><td><code><a href="../../item/click/ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#onLeftClickBy(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onLeftClickBy</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when a chisel or a bit is left clicked to perform an associated operation.</div><br></td></tr>
  <tr><td><code><a href="../../item/click/ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#onRightClickBy(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onRightClickBy</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when a chisel or a bit is right clicked to perform an associated operation.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onStoppedLeftClicking(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onStoppedLeftClicking</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when the player has released the left click button.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onStoppedRightClicking(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onStoppedRightClicking</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when the player has released the right click button.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#requiresPlaceableEditStack()" class="member-name-link">requiresPlaceableEditStack</a>()</code></td><td><div class="block">Indicates that this mode is only available on a stack which has a placeable mode.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></code></td><td><code><a href="#getDefaultMode()" class="member-name-link">getDefaultMode</a>()</code></td><td><div class="block">The default mode of the chisel or bit.</div><br></td></tr>
  <tr><td><code>static com.communi.suggestu.scena.core.registries.ICustomRegistry<wbr>&lt;<a href="IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;</code></td><td><code><a href="#getRegistry()" class="member-name-link">getRegistry</a>()</code></td><td><div class="block">The underlying registry that contains the different modes a chisel can assume.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;</code></td><td><code><a href="#getCurrentAccessor(mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">getCurrentAccessor</a><wbr>(<a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Performs an extraction and potential modification of the accessor for the given context as determined by this mode.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getShape(mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">getShape</a><wbr>(<a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Defines the shape of the area that is to be chiseled.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isSingleClickUse()" class="member-name-link">isSingleClickUse</a>()</code></td><td><div class="block">Indicates if this mode requires a single click to trigger or not.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isStillValid(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext,mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">isStillValid</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context,<br> <a href="../ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperation)</code></td><td><div class="block">Checks if the passed context is still valid for the given entity.</div><br></td></tr>
  <tr><td><code><a href="../../item/click/ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#onLeftClickBy(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onLeftClickBy</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when a chisel or a bit is left clicked to perform an associated operation.</div><br></td></tr>
  <tr><td><code><a href="../../item/click/ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#onRightClickBy(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onRightClickBy</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when a chisel or a bit is right clicked to perform an associated operation.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onStoppedLeftClicking(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onStoppedLeftClicking</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when the player has released the left click button.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onStoppedRightClicking(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onStoppedRightClicking</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when the player has released the right click button.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#requiresPlaceableEditStack()" class="member-name-link">requiresPlaceableEditStack</a>()</code></td><td><div class="block">Indicates that this mode is only available on a stack which has a placeable mode.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;</code></td><td><code><a href="#getCurrentAccessor(mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">getCurrentAccessor</a><wbr>(<a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Performs an extraction and potential modification of the accessor for the given context as determined by this mode.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#getShape(mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">getShape</a><wbr>(<a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Defines the shape of the area that is to be chiseled.</div><br></td></tr>
  <tr><td><code><a href="../../item/click/ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#onLeftClickBy(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onLeftClickBy</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when a chisel or a bit is left clicked to perform an associated operation.</div><br></td></tr>
  <tr><td><code><a href="../../item/click/ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#onRightClickBy(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onRightClickBy</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when a chisel or a bit is right clicked to perform an associated operation.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onStoppedLeftClicking(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onStoppedLeftClicking</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when the player has released the left click button.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onStoppedRightClicking(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)" class="member-name-link">onStoppedRightClicking</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</code></td><td><div class="block">Invoked by the system when the player has released the right click button.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#isSingleClickUse()" class="member-name-link">isSingleClickUse</a>()</code></td><td><div class="block">Indicates if this mode requires a single click to trigger or not.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isStillValid(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext,mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">isStillValid</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context,<br> <a href="../ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperation)</code></td><td><div class="block">Checks if the passed context is still valid for the given entity.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#requiresPlaceableEditStack()" class="member-name-link">requiresPlaceableEditStack</a>()</code></td><td><div class="block">Indicates that this mode is only available on a stack which has a placeable mode.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;com.communi.suggestu.scena.core.registries.ICustomRegistryEntrygetRegistryNameMethods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../../item/withmode/IRenderableMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IRenderableMode</a><a href="../../item/withmode/IRenderableMode.html#getColorVector()" title="getColorVector()">getColorVector</a>, <a href="../../item/withmode/IRenderableMode.html#getPositionVector()" title="getPositionVector()">getPositionVector</a>, <a href="../../item/withmode/IRenderableMode.html#getScaleVector()" title="getScaleVector()">getScaleVector</a>, <a href="../../item/withmode/IRenderableMode.html#isActive()" title="isActive()">isActive</a>, <a href="../../item/withmode/IRenderableMode.html#shouldRenderDisplayNameInMenu()" title="shouldRenderDisplayNameInMenu()">shouldRenderDisplayNameInMenu</a>, <a href="../../item/withmode/IRenderableMode.html#shouldRenderName()" title="shouldRenderName()">shouldRenderName</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../../item/withmode/IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a><a href="../../item/withmode/IToolMode.html#getGroup()" title="getGroup()">getGroup</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithColor.html" title="interface in mod.chiselsandbits.api.util">IWithColor</a><a href="../../util/IWithColor.html#getAlphaChannel()" title="getAlphaChannel()">getAlphaChannel</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithDisplayName.html" title="interface in mod.chiselsandbits.api.util">IWithDisplayName</a><a href="../../util/IWithDisplayName.html#getDisplayName()" title="getDisplayName()">getDisplayName</a>, <a href="../../util/IWithDisplayName.html#getMultiLineDisplayName()" title="getMultiLineDisplayName()">getMultiLineDisplayName</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.util.<a href="../../util/IWithIcon.html" title="interface in mod.chiselsandbits.api.util">IWithIcon</a><a href="../../util/IWithIcon.html#getIcon()" title="getIcon()">getIcon</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getDefaultMode()">

:::tabs
== getDefaultMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></span>&nbsp;<span class="element-name">getDefaultMode</span>()</div>
<div class="block">The default mode of the chisel or bit.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The default mode.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getRegistry()">

:::tabs
== getRegistry
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type">com.communi.suggestu.scena.core.registries.ICustomRegistry&lt;<a href="IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&gt;</span>&nbsp;<span class="element-name">getRegistry</span>()</div>
<div class="block">The underlying registry that contains the different modes a chisel can assume.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The underlying forge registry.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="onLeftClickBy(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)">

:::tabs
== onLeftClickBy
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../../item/click/ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></span>&nbsp;<span class="element-name">onLeftClickBy</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</span></div>
<div class="block">Invoked by the system when a chisel or a bit is left clicked to perform an associated operation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The entity that is executing the operation.</dd>
<dd><code>context</code> - The chiseling context.</dd>
<dt>Returns:</dt>
<dd>The processing state, which indicates how the interaction should proceed.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="onStoppedLeftClicking(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)">

:::tabs
== onStoppedLeftClicking
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">onStoppedLeftClicking</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</span></div>
<div class="block">Invoked by the system when the player has released the left click button.

Currently not invoked by the system. Future endpoint.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player who released the button.</dd>
<dd><code>context</code> - The chiseling context.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="onRightClickBy(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)">

:::tabs
== onRightClickBy
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../../item/click/ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></span>&nbsp;<span class="element-name">onRightClickBy</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</span></div>
<div class="block">Invoked by the system when a chisel or a bit is right clicked to perform an associated operation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The entity that is executing the operation.</dd>
<dd><code>context</code> - The chiseling context.</dd>
<dt>Returns:</dt>
<dd>The processing state, which indicates how the interaction should proceed.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="onStoppedRightClicking(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext)">

:::tabs
== onStoppedRightClicking
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">onStoppedRightClicking</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</span></div>
<div class="block">Invoked by the system when the player has released the right click button.

Currently not invoked by the system. Future endpoint.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player who released the button.</dd>
<dd><code>context</code> - The chiseling context.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getCurrentAccessor(mod.chiselsandbits.api.chiseling.IChiselingContext)">

:::tabs
== getCurrentAccessor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="../../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&gt;</span>&nbsp;<span class="element-name">getCurrentAccessor</span><wbr><span class="parameters">(<a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</span></div>
<div class="block">Performs an extraction and potential modification of the accessor for the given context as determined by this mode.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The chiseling context.</dd>
<dt>Returns:</dt>
<dd>An optional, potentially containing an area accessor.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="isStillValid(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.IChiselingContext,mod.chiselsandbits.api.chiseling.ChiselingOperation)">

:::tabs
== isStillValid
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isStillValid</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context,
 <a href="../ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperation)</span></div>
<div class="block">Checks if the passed context is still valid for the given entity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The entity to check for.</dd>
<dd><code>context</code> - The context to check.</dd>
<dd><code>modeOfOperation</code> - The mode of operandus for the check.</dd>
<dt>Returns:</dt>
<dd>True when still valid, false when not.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="requiresPlaceableEditStack()">

:::tabs
== requiresPlaceableEditStack
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">requiresPlaceableEditStack</span>()</div>
<div class="block">Indicates that this mode is only available on a stack which has a placeable mode.
Useful when placement and removal perform the same task AND requires a bit to be held.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>True when a "bit" needs to be held.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getShape(mod.chiselsandbits.api.chiseling.IChiselingContext)">

:::tabs
== getShape
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">getShape</span><wbr><span class="parameters">(<a href="../IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&nbsp;context)</span></div>
<div class="block">Defines the shape of the area that is to be chiseled.
This is the general shape, so a sphere, cube, or line any area specific changes are not returned by this method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The current context that it is supposed to be for.</dd>
<dt>Returns:</dt>
<dd>The shape of the area to be chiseled.</dd>
<dt>Note on the Implementation</dt>
<dd>This shape should make use of a heavily cached version, it will be called during rendering.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="isSingleClickUse()">

:::tabs
== isSingleClickUse
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isSingleClickUse</span>()</div>
<div class="block">Indicates if this mode requires a single click to trigger or not.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>True if single click, false if multiple clicks are needed.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

