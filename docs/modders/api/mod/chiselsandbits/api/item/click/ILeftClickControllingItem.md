--- 
title: ILeftClickControllingItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.click](index.md)  
# Interface ILeftClickControllingItem  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ILeftClickControllingItem</span></div>  

  

Deals with the way items are able to handle left click interactions.  

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
  <tr><td><code>default boolean</code></td><td><code><a href="#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">canUse</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the player can use the item in the current interaction.</div><br></td></tr>
  <tr><td><code><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#handleLeftClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" class="member-name-link">handleLeftClickProcessing</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.InteractionHand&nbsp;hand,<br> net.minecraft.core.BlockPos&nbsp;position,<br> net.minecraft.core.Direction&nbsp;face,<br> <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a>&nbsp;currentState)</code></td><td><div class="block">Callback invoked when a supported item is used to left click.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onLeftClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onLeftClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a left-clicking procedure has ended.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">canUse</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the player can use the item in the current interaction.</div><br></td></tr>
  <tr><td><code><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#handleLeftClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" class="member-name-link">handleLeftClickProcessing</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.InteractionHand&nbsp;hand,<br> net.minecraft.core.BlockPos&nbsp;position,<br> net.minecraft.core.Direction&nbsp;face,<br> <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a>&nbsp;currentState)</code></td><td><div class="block">Callback invoked when a supported item is used to left click.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onLeftClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onLeftClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a left-clicking procedure has ended.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#handleLeftClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)" class="member-name-link">handleLeftClickProcessing</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.InteractionHand&nbsp;hand,<br> net.minecraft.core.BlockPos&nbsp;position,<br> net.minecraft.core.Direction&nbsp;face,<br> <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a>&nbsp;currentState)</code></td><td><div class="block">Callback invoked when a supported item is used to left click.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#onLeftClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">onLeftClickProcessingEnd</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Invoked by the platform to indicate to this item that a left-clicking procedure has ended.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)" class="member-name-link">canUse</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the player can use the item in the current interaction.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="handleLeftClickProcessing(net.minecraft.world.entity.player.Player,net.minecraft.world.InteractionHand,net.minecraft.core.BlockPos,net.minecraft.core.Direction,mod.chiselsandbits.api.item.click.ClickProcessingState)">

:::tabs
== handleLeftClickProcessing
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></span>&nbsp;<span class="element-name">handleLeftClickProcessing</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.InteractionHand&nbsp;hand,
 net.minecraft.core.BlockPos&nbsp;position,
 net.minecraft.core.Direction&nbsp;face,
 <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a>&nbsp;currentState)</span></div>
Callback invoked when a supported item is used to left click.
Allows for said item to take over the processing logic of the left clicking
and can afterwards block the further vanilla processing.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The entity who left clicked.</dd>
<dd><code>hand</code> - The hand with which the entity left clicked.</dd>
<dd><code>position</code> - The position on which the entity left clicked.</dd>
<dd><code>face</code> - The face on which the entity left clicked.</dd>
<dd><code>currentState</code> - The current state of the left click processing.</dd>
<dt>Returns:</dt>
<dd>The processing state with which the processing of the left click should continue.</dd>
</dl>
</div>
:::


</section>

<section id="onLeftClickProcessingEnd(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)">

:::tabs
== onLeftClickProcessingEnd
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">onLeftClickProcessingEnd</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player,
 net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Invoked by the platform to indicate to this item that a left-clicking procedure has ended.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The player who stopped left-clicking.</dd>
<dd><code>stack</code> - The stack on which the clicking ended.</dd>
</dl>
</div>
:::


</section>

<section id="canUse(net.minecraft.world.entity.player.Player,net.minecraft.world.item.ItemStack)">

:::tabs
== canUse
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">canUse</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Indicates if the player can use the item in the current interaction.
If this returns false, then no processing is performed and the interaction
event is cancelled.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player in question.</dd>
<dt>Returns:</dt>
<dd>True when useable, false when not.</dd>
</dl>
</div>
:::


</section>

:::::
  

