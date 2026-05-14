--- 
title: IMeasuringTapeItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.measuring](index.md)  
# Interface IMeasuringTapeItem  
**All Extended Interfaces:**  
[IRightClickControllingItem](../click/IRightClickControllingItem.md), [INoHitEffectsItem](../INoHitEffectsItem.md), [IWithModeItem\<IMeasuringMode\>](../withmode/IWithModeItem.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMeasuringTapeItem</span><span class="extends-implements"><br/>  
extends <a href="../INoHitEffectsItem.html" title="interface in mod.chiselsandbits.api.item">INoHitEffectsItem</a>, <a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a>&lt;<a href="../../measuring/IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a>&gt;, <a href="../click/IRightClickControllingItem.html" title="interface in mod.chiselsandbits.api.item.click">IRightClickControllingItem</a></span></div>  

  

  

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
  <tr><td><code>void</code></td><td><code><a href="#clear(net.minecraft.world.item.ItemStack)" class="member-name-link">clear</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Clears the measurement state of a given stack.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.Vec3&gt;</code></td><td><code><a href="#getStart(net.minecraft.world.item.ItemStack)" class="member-name-link">getStart</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Determines the start point stored in the stack of the item.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onRightClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a right-clicking procedure has ended.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setStart(net.minecraft.world.item.ItemStack,net.minecraft.world.phys.Vec3)" class="member-name-link">setStart</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;start)</code></td><td><div class="block">Sets the start point of the current measurement.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear(net.minecraft.world.item.ItemStack)" class="member-name-link">clear</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Clears the measurement state of a given stack.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.Vec3&gt;</code></td><td><code><a href="#getStart(net.minecraft.world.item.ItemStack)" class="member-name-link">getStart</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Determines the start point stored in the stack of the item.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onRightClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a right-clicking procedure has ended.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setStart(net.minecraft.world.item.ItemStack,net.minecraft.world.phys.Vec3)" class="member-name-link">setStart</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;start)</code></td><td><div class="block">Sets the start point of the current measurement.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear(net.minecraft.world.item.ItemStack)" class="member-name-link">clear</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Clears the measurement state of a given stack.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.Vec3&gt;</code></td><td><code><a href="#getStart(net.minecraft.world.item.ItemStack)" class="member-name-link">getStart</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Determines the start point stored in the stack of the item.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setStart(net.minecraft.world.item.ItemStack,net.minecraft.world.phys.Vec3)" class="member-name-link">setStart</a><wbr>(@NotNull net.minecraft.world.item.ItemStack&nbsp;stack,<br> @NotNull net.minecraft.world.phys.Vec3&nbsp;start)</code></td><td><div class="block">Sets the start point of the current measurement.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onRightClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a right-clicking procedure has ended.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.click.<a href="../click/IRightClickControllingItem.html" title="interface in mod.chiselsandbits.api.item.click">IRightClickControllingItem</a><a href="../click/IRightClickControllingItem.html#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" title="canUse(Player, ItemStack)">canUse</a>, <a href="../click/IRightClickControllingItem.html#handleRightClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" title="handleRightClickProcessing(Player, InteractionHand, BlockPos, Direction, ClickProcessingState)">handleRightClickProcessing</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.withmode.<a href="../withmode/IWithModeItem.html" title="interface in mod.chiselsandbits.api.item.withmode">IWithModeItem</a><a href="../withmode/IWithModeItem.html#getMode(net.minecraft.world.item.ItemStack)" title="getMode(ItemStack)">getMode</a>, <a href="../withmode/IWithModeItem.html#getPossibleModes()" title="getPossibleModes()">getPossibleModes</a>, <a href="../withmode/IWithModeItem.html#requiresUpdateOnClosure()" title="requiresUpdateOnClosure()">requiresUpdateOnClosure</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,int)" title="setMode(ItemStack, int)">setMode</a>, <a href="../withmode/IWithModeItem.html#setMode(net.minecraft.world.item.ItemStack,M)" title="setMode(ItemStack, IMeasuringMode)">setMode</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getStart(net.minecraft.world.item.ItemStack)">

:::tabs
== getStart
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.phys.Vec3&gt;</span>&nbsp;<span class="element-name">getStart</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Determines the start point stored in the stack of the item.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to get the start point from if it is available.</dd>
<dt>Returns:</dt>
<dd>An optional with the start point if it is set.</dd>
</dl>
</div>
:::


</section>

<section id="setStart(net.minecraft.world.item.ItemStack,net.minecraft.world.phys.Vec3)">

:::tabs
== setStart
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setStart</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.item.ItemStack&nbsp;stack,
 @NotNull
 @NotNull net.minecraft.world.phys.Vec3&nbsp;start)</span></div>
Sets the start point of the current measurement.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to set the start on.</dd>
<dd><code>start</code> - The start point.</dd>
</dl>
</div>
:::


</section>

<section id="clear(net.minecraft.world.item.ItemStack)">

:::tabs
== clear
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clear</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Clears the measurement state of a given stack.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to clear the measurement state from.</dd>
</dl>
</div>
:::


</section>

<section id="onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)">

:::tabs
== onRightClickProcessingEnd
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">onRightClickProcessingEnd</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player,
 net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Invoked by the platform to indicate to this item that a right-clicking procedure has ended.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../click/IRightClickControllingItem.html#onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)">onRightClickProcessingEnd</a></code>&nbsp;in interface&nbsp;<code><a href="../click/IRightClickControllingItem.html" title="interface in mod.chiselsandbits.api.item.click">IRightClickControllingItem</a></code></dd>
<dt>Parameters:</dt>
<dd><code>player</code> - The player who stopped right-clicking.</dd>
<dd><code>stack</code> - The stack on which the clicking ended.</dd>
</dl>
</div>
:::


</section>

:::::
  

