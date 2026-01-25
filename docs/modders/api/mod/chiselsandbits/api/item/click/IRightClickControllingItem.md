--- 
title: IRightClickControllingItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.click](index.md)  
# Interface IRightClickControllingItem  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IRightClickControllingItem</span></div>  

  

<div class="block">Deals with the way items are able to handle left click interactions.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">canUse</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the player can use the item in the current interaction.</div><br></td></tr>
  <tr><td><code><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#handleRightClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" class="member-name-link">handleRightClickProcessing</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.InteractionHand&nbsp;hand,<br> net.minecraft.core.BlockPos&nbsp;position,<br> net.minecraft.core.Direction&nbsp;face,<br> <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a>&nbsp;currentState)</code></td><td><div class="block">Callback invoked when a supported item is used to right click.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onRightClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a right-clicking procedure has ended.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">canUse</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the player can use the item in the current interaction.</div><br></td></tr>
  <tr><td><code><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#handleRightClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" class="member-name-link">handleRightClickProcessing</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.InteractionHand&nbsp;hand,<br> net.minecraft.core.BlockPos&nbsp;position,<br> net.minecraft.core.Direction&nbsp;face,<br> <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a>&nbsp;currentState)</code></td><td><div class="block">Callback invoked when a supported item is used to right click.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onRightClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a right-clicking procedure has ended.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#handleRightClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" class="member-name-link">handleRightClickProcessing</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.InteractionHand&nbsp;hand,<br> net.minecraft.core.BlockPos&nbsp;position,<br> net.minecraft.core.Direction&nbsp;face,<br> <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a>&nbsp;currentState)</code></td><td><div class="block">Callback invoked when a supported item is used to right click.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onRightClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a right-clicking procedure has ended.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">canUse</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the player can use the item in the current interaction.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="handleRightClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)">

:::tabs
== handleRightClickProcessing
<div class="member-signature"><span class="return-type"><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></span>&nbsp;<span class="element-name">handleRightClickProcessing</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.InteractionHand&nbsp;hand,
 net.minecraft.core.BlockPos&nbsp;position,
 net.minecraft.core.Direction&nbsp;face,
 <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a>&nbsp;currentState)</span></div>
<div class="block">Callback invoked when a supported item is used to right click.

 Allows for said item to take over the processing logic of the right clicking
 and can afterwards block the further vanilla processing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The entity who right clicked.</dd>
<dd><code>hand</code> - The hand with which the entity right clicked.</dd>
<dd><code>position</code> - The position on which the entity right clicked.</dd>
<dd><code>face</code> - The face on which the entity right clicked.</dd>
<dd><code>currentState</code> - The current state of the right click processing.</dd>
<dt>Returns:</dt>
<dd>The processing state with which the processing of the right click should continue.</dd>
</dl>
:::


</section>

<section id="onRightClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)">

:::tabs
== onRightClickProcessingEnd
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">onRightClickProcessingEnd</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player,
 net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Invoked by the platform to indicate to this item that a right-clicking procedure has ended.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The player who stopped right-clicking.</dd>
<dd><code>stack</code> - The stack on which the clicking ended.</dd>
</dl>
:::


</section>

<section id="canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)">

:::tabs
== canUse
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">canUse</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Indicates if the player can use the item in the current interaction.
 If this returns false, then no processing is performed and the interaction
 event is cancelled.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player in question.</dd>
<dt>Returns:</dt>
<dd>True when useable, false when not.</dd>
</dl>
:::


</section>

:::::
  

