--- 
title: IInteractableItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.interactable](index.md)  
# Interface IInteractableItem  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IInteractableItem</span></div>  

  

Represents an item which can be used to interact with other items in the other hand.  

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
  <tr><td><code>float</code></td><td><code><a href="#getBobbingTickCount()" class="member-name-link">getBobbingTickCount</a>()</code></td><td><div class="block">Indicates how often the bobbing animation needs to play inside the use time of the item.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#getInteractionTarget(net.minecraft.world.item.ItemStack)" class="member-name-link">getInteractionTarget</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Gives access to the stack the interaction is occurring with.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInteracting(net.minecraft.world.item.ItemStack)" class="member-name-link">isInteracting</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the current given itemstack is in use during an interaction.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isRunningASimulatedInteraction(net.minecraft.world.item.ItemStack)" class="member-name-link">isRunningASimulatedInteraction</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the interactable stack is used in a simulation for display purposes.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>float</code></td><td><code><a href="#getBobbingTickCount()" class="member-name-link">getBobbingTickCount</a>()</code></td><td><div class="block">Indicates how often the bobbing animation needs to play inside the use time of the item.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#getInteractionTarget(net.minecraft.world.item.ItemStack)" class="member-name-link">getInteractionTarget</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Gives access to the stack the interaction is occurring with.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInteracting(net.minecraft.world.item.ItemStack)" class="member-name-link">isInteracting</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the current given itemstack is in use during an interaction.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isRunningASimulatedInteraction(net.minecraft.world.item.ItemStack)" class="member-name-link">isRunningASimulatedInteraction</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the interactable stack is used in a simulation for display purposes.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>float</code></td><td><code><a href="#getBobbingTickCount()" class="member-name-link">getBobbingTickCount</a>()</code></td><td><div class="block">Indicates how often the bobbing animation needs to play inside the use time of the item.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#getInteractionTarget(net.minecraft.world.item.ItemStack)" class="member-name-link">getInteractionTarget</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Gives access to the stack the interaction is occurring with.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isInteracting(net.minecraft.world.item.ItemStack)" class="member-name-link">isInteracting</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the current given itemstack is in use during an interaction.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isRunningASimulatedInteraction(net.minecraft.world.item.ItemStack)" class="member-name-link">isRunningASimulatedInteraction</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Indicates if the interactable stack is used in a simulation for display purposes.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="isInteracting(net.minecraft.world.item.ItemStack)">

:::tabs
== isInteracting
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isInteracting</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Indicates if the current given itemstack is in use during an interaction.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack in question.</dd>
<dt>Returns:</dt>
<dd><code>true</code> when an interaction with the given stack is going on.</dd>
</dl>
</div>
:::


</section>

<section id="getInteractionTarget(net.minecraft.world.item.ItemStack)">

:::tabs
== getInteractionTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">getInteractionTarget</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Gives access to the stack the interaction is occurring with.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack that is leading the interaction.</dd>
<dt>Returns:</dt>
<dd>The stack that the interaction is occuring with.</dd>
</dl>
</div>
:::


</section>

<section id="isRunningASimulatedInteraction(net.minecraft.world.item.ItemStack)">

:::tabs
== isRunningASimulatedInteraction
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isRunningASimulatedInteraction</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Indicates if the interactable stack is used in a simulation for display purposes.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack in question</dd>
<dt>Returns:</dt>
<dd><code>true</code> when a simulation is taking place.</dd>
</dl>
</div>
:::


</section>

<section id="getBobbingTickCount()">

:::tabs
== getBobbingTickCount
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">float</span>&nbsp;<span class="element-name">getBobbingTickCount</span>()</div>
Indicates how often the bobbing animation needs to play inside the use time of the item.
This is done by returning the bobbing animation length from this method.
<dl class="notes">
<dt>Returns:</dt>
<dd>The amount of ticks a bobbing animation takes.</dd>
</dl>
</div>
:::


</section>

:::::
  

