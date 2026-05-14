--- 
title: IGlueableBlockEntity
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.glueing](index)  
# Interface IGlueableBlockEntity  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IGlueableBlockEntity</span></div>  

  

  

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
  <tr><td><code>net.minecraft.world.level.BlockGetter</code></td><td><code><a href="#blockGetter()" class="member-name-link">blockGetter</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#blockPos()" class="member-name-link">blockPos</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#connectedPositions()" class="member-name-link">connectedPositions</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#createGluedDrop()" class="member-name-link">createGluedDrop</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/EnumSet.html" title="class or interface in java.util" class="external-link">EnumSet</a><wbr>&lt;net.minecraft.core.Direction&gt;</code></td><td><code><a href="#gluedSides()" class="member-name-link">gluedSides</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.level.BlockGetter</code></td><td><code><a href="#blockGetter()" class="member-name-link">blockGetter</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#blockPos()" class="member-name-link">blockPos</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#connectedPositions()" class="member-name-link">connectedPositions</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#createGluedDrop()" class="member-name-link">createGluedDrop</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/EnumSet.html" title="class or interface in java.util" class="external-link">EnumSet</a><wbr>&lt;net.minecraft.core.Direction&gt;</code></td><td><code><a href="#gluedSides()" class="member-name-link">gluedSides</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.level.BlockGetter</code></td><td><code><a href="#blockGetter()" class="member-name-link">blockGetter</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#blockPos()" class="member-name-link">blockPos</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.item.ItemStack</code></td><td><code><a href="#createGluedDrop()" class="member-name-link">createGluedDrop</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/EnumSet.html" title="class or interface in java.util" class="external-link">EnumSet</a><wbr>&lt;net.minecraft.core.Direction&gt;</code></td><td><code><a href="#gluedSides()" class="member-name-link">gluedSides</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#connectedPositions()" class="member-name-link">connectedPositions</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="blockGetter()">

:::tabs
== blockGetter
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.level.BlockGetter</span>&nbsp;<span class="element-name">blockGetter</span>()</div>
</div>
:::


</section>

<section id="blockPos()">

:::tabs
== blockPos
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">blockPos</span>()</div>
</div>
:::


</section>

<section id="gluedSides()">

:::tabs
== gluedSides
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/EnumSet.html" title="class or interface in java.util" class="external-link">EnumSet</a>&lt;net.minecraft.core.Direction&gt;</span>&nbsp;<span class="element-name">gluedSides</span>()</div>
</div>
:::


</section>

<section id="createGluedDrop()">

:::tabs
== createGluedDrop
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">createGluedDrop</span>()</div>
</div>
:::


</section>

<section id="connectedPositions()">

:::tabs
== connectedPositions
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">connectedPositions</span>()</div>
</div>
:::


</section>

:::::
  

