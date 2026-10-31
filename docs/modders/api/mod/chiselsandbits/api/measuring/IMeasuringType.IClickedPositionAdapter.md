--- 
title: IClickedPositionAdapter
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.measuring](index)  
# Interface IClickedPositionAdapter  
**Enclosing Class:**  
[IMeasuringType](IMeasuringType)  

**Functional Interface:**  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang" class="external-link">@FunctionalInterface</a><br/>  
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">IMeasuringType.IClickedPositionAdapter</span></div>  

  

Adapts the location reported by a block hit before it becomes a measurement endpoint.  

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
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adapt(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adapt</a><wbr>(net.minecraft.world.phys.BlockHitResult&nbsp;startPosition)</code></td><td><div class="block">Adapts the location from a block hit.</div><br></td></tr>
  <tr><td><code>static <a href="IMeasuringType.IClickedPositionAdapter.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType.IClickedPositionAdapter</a></code></td><td><code><a href="#identity()" class="member-name-link">identity</a>()</code></td><td><div class="block">Creates an adapter that returns the hit result's location unchanged.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IMeasuringType.IClickedPositionAdapter.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType.IClickedPositionAdapter</a></code></td><td><code><a href="#identity()" class="member-name-link">identity</a>()</code></td><td><div class="block">Creates an adapter that returns the hit result's location unchanged.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adapt(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adapt</a><wbr>(net.minecraft.world.phys.BlockHitResult&nbsp;startPosition)</code></td><td><div class="block">Adapts the location from a block hit.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adapt(net.minecraft.world.phys.BlockHitResult)" class="member-name-link">adapt</a><wbr>(net.minecraft.world.phys.BlockHitResult&nbsp;startPosition)</code></td><td><div class="block">Adapts the location from a block hit.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="identity()">

:::tabs
== identity
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IMeasuringType.IClickedPositionAdapter.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringType.IClickedPositionAdapter</a></span>&nbsp;<span class="element-name">identity</span>()</div>
Creates an adapter that returns the hit result's location unchanged.
<dl class="notes">
<dt>Returns:</dt>
<dd>an adapter that uses the hit location without modification</dd>
</dl>
</div>
:::


</section>

<section id="adapt(net.minecraft.world.phys.BlockHitResult)">

:::tabs
== adapt
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">adapt</span><wbr><span class="parameters">(net.minecraft.world.phys.BlockHitResult&nbsp;startPosition)</span></div>
Adapts the location from a block hit.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>startPosition</code> - hit result to adapt</dd>
<dt>Returns:</dt>
<dd>adapted hit location</dd>
</dl>
</div>
:::


</section>

:::::
  

