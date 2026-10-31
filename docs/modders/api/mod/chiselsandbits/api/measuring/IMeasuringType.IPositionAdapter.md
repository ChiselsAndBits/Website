--- 
title: IPositionAdapter
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.measuring](index)  
# Interface IPositionAdapter  
**Enclosing Class:**  
[IMeasuringType](IMeasuringType)  

**Functional Interface:**  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang" class="external-link">@FunctionalInterface</a><br/>  
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">IMeasuringType.IPositionAdapter</span></div>  

  

Adapts a pair of measurement endpoints using the clicked face.  

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
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adapt(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adapt</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the two endpoints to the measuring mode's coordinate rules.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adapt(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adapt</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the two endpoints to the measuring mode's coordinate rules.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#adapt(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)" class="member-name-link">adapt</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;startPosition,<br> net.minecraft.world.phys.Vec3&nbsp;endPosition,<br> net.minecraft.core.Direction&nbsp;hitFace)</code></td><td><div class="block">Adapts the two endpoints to the measuring mode's coordinate rules.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="adapt(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction)">

:::tabs
== adapt
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">adapt</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;startPosition,
 net.minecraft.world.phys.Vec3&nbsp;endPosition,
 net.minecraft.core.Direction&nbsp;hitFace)</span></div>
Adapts the two endpoints to the measuring mode's coordinate rules.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>startPosition</code> - first endpoint</dd>
<dd><code>endPosition</code> - second endpoint</dd>
<dd><code>hitFace</code> - face used to resolve alignment</dd>
<dt>Returns:</dt>
<dd>adapted position</dd>
</dl>
</div>
:::


</section>

:::::
  

