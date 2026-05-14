--- 
title: IMeasurement
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.measuring](index.md)  
# Interface IMeasurement  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMeasurement</span></div>  

  

Represents a measurement made in a given world by a given player.  

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
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getFrom()" class="member-name-link">getFrom</a>()</code></td><td><div class="block">The lower left front corner of the measurement.</div><br></td></tr>
  <tr><td><code><a href="IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a></code></td><td><code><a href="#getMode()" class="member-name-link">getMode</a>()</code></td><td><div class="block">The mode of the measurement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a></code></td><td><code><a href="#getOwner()" class="member-name-link">getOwner</a>()</code></td><td><div class="block">The id of the player who made the measurement.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSize()" class="member-name-link">getSize</a>()</code></td><td><div class="block">The size of the measurement.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTo()" class="member-name-link">getTo</a>()</code></td><td><div class="block">The top right back corner of the measurement.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getWorldKey()" class="member-name-link">getWorldKey</a>()</code></td><td><div class="block">The id of the world that this measurement was made in.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getFrom()" class="member-name-link">getFrom</a>()</code></td><td><div class="block">The lower left front corner of the measurement.</div><br></td></tr>
  <tr><td><code><a href="IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a></code></td><td><code><a href="#getMode()" class="member-name-link">getMode</a>()</code></td><td><div class="block">The mode of the measurement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a></code></td><td><code><a href="#getOwner()" class="member-name-link">getOwner</a>()</code></td><td><div class="block">The id of the player who made the measurement.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSize()" class="member-name-link">getSize</a>()</code></td><td><div class="block">The size of the measurement.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTo()" class="member-name-link">getTo</a>()</code></td><td><div class="block">The top right back corner of the measurement.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getWorldKey()" class="member-name-link">getWorldKey</a>()</code></td><td><div class="block">The id of the world that this measurement was made in.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getFrom()" class="member-name-link">getFrom</a>()</code></td><td><div class="block">The lower left front corner of the measurement.</div><br></td></tr>
  <tr><td><code><a href="IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a></code></td><td><code><a href="#getMode()" class="member-name-link">getMode</a>()</code></td><td><div class="block">The mode of the measurement.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a></code></td><td><code><a href="#getOwner()" class="member-name-link">getOwner</a>()</code></td><td><div class="block">The id of the player who made the measurement.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getTo()" class="member-name-link">getTo</a>()</code></td><td><div class="block">The top right back corner of the measurement.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getWorldKey()" class="member-name-link">getWorldKey</a>()</code></td><td><div class="block">The id of the world that this measurement was made in.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSize()" class="member-name-link">getSize</a>()</code></td><td><div class="block">The size of the measurement.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getOwner()">
:::tabs
== getOwner
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a></span>&nbsp;<span class="element-name">getOwner</span>()</div>
The id of the player who made the measurement.
<dl class="notes">
<dt>Returns:</dt>
<dd>The id of the owner.</dd>
</dl>
</div>
:::
</section>
<section id="getFrom()">
:::tabs
== getFrom
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getFrom</span>()</div>
The lower left front corner of the measurement.
<dl class="notes">
<dt>Returns:</dt>
<dd>The start point of the measurement.</dd>
</dl>
</div>
:::
</section>
<section id="getTo()">
:::tabs
== getTo
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getTo</span>()</div>
The top right back corner of the measurement.
<dl class="notes">
<dt>Returns:</dt>
<dd>The end point of the measurement.</dd>
</dl>
</div>
:::
</section>
<section id="getSize()">
:::tabs
== getSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getSize</span>()</div>
The size of the measurement.
<dl class="notes">
<dt>Returns:</dt>
<dd>The size of the measurement.</dd>
</dl>
</div>
:::
</section>
<section id="getMode()">
:::tabs
== getMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a></span>&nbsp;<span class="element-name">getMode</span>()</div>
The mode of the measurement.
<dl class="notes">
<dt>Returns:</dt>
<dd>The mode of the measurement.</dd>
</dl>
</div>
:::
</section>
<section id="getWorldKey()">
:::tabs
== getWorldKey
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.resources.Identifier</span>&nbsp;<span class="element-name">getWorldKey</span>()</div>
The id of the world that this measurement was made in.
<dl class="notes">
<dt>Returns:</dt>
<dd>The id of the world.</dd>
</dl>
</div>
:::
</section>
:::::
  

