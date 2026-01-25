--- 
title: RayTracingUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class RayTracingUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.RayTracingUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">RayTracingUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for dealing with raytracing.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#getFullFacingVector(net.minecraft.world.entity.player.Player)" class="member-name-link">getFullFacingVector</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.HitResult</code></td><td><code><a href="#rayTracePlayer(net.minecraft.world.entity.player.Player)" class="member-name-link">rayTracePlayer</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Performs a raytrace result within the given reach distance of the given player.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#getFullFacingVector(net.minecraft.world.entity.player.Player)" class="member-name-link">getFullFacingVector</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.HitResult</code></td><td><code><a href="#rayTracePlayer(net.minecraft.world.entity.player.Player)" class="member-name-link">rayTracePlayer</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Performs a raytrace result within the given reach distance of the given player.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#getFullFacingVector(net.minecraft.world.entity.player.Player)" class="member-name-link">getFullFacingVector</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.HitResult</code></td><td><code><a href="#rayTracePlayer(net.minecraft.world.entity.player.Player)" class="member-name-link">rayTracePlayer</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Performs a raytrace result within the given reach distance of the given player.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="rayTracePlayer(net.minecraft.world.entity.player.Player)">

:::tabs
== rayTracePlayer
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.HitResult</span>&nbsp;<span class="element-name">rayTracePlayer</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</span></div>
Performs a raytrace result within the given reach distance of the given player.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player to run a raytrace for.</dd>
<dt>Returns:</dt>
<dd>The raytrace result.</dd>
</dl>
:::


</section>

<section id="getFullFacingVector(net.minecraft.world.entity.player.Player)">

:::tabs
== getFullFacingVector
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.Vec3i</span>&nbsp;<span class="element-name">getFullFacingVector</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

