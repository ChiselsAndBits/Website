--- 
title: IMirrorAndRotateble
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.mutator](index)  
# Interface IMirrorAndRotateble  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMirrorAndRotateble</span></div>  

  

  

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
  <tr><td><code>void</code></td><td><code><a href="#mirror(net.minecraft.core.Direction.Axis)" class="member-name-link">mirror</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Mirrors the current multistate block around the given axis.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates the current multistate block exactly once 90 degrees around the given axis.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#mirror(net.minecraft.core.Direction.Axis)" class="member-name-link">mirror</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Mirrors the current multistate block around the given axis.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates the current multistate block exactly once 90 degrees around the given axis.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#mirror(net.minecraft.core.Direction.Axis)" class="member-name-link">mirror</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Mirrors the current multistate block around the given axis.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;rotationCount)</code></td><td><div class="block">Rotates the current multistate block 90 degrees around the given axis with the given rotation count.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#rotate(net.minecraft.core.Direction.Axis)" class="member-name-link">rotate</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates the current multistate block exactly once 90 degrees around the given axis.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="rotate(net.minecraft.core.Direction.Axis,int)">

:::tabs
== rotate
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">rotate</span><wbr><span class="parameters">(net.minecraft.core.Direction.Axis&nbsp;axis,
 int&nbsp;rotationCount)</span></div>
Rotates the current multistate block 90 degrees around the given axis with the given rotation count.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>axis</code> - The axis to rotate around.</dd>
<dd><code>rotationCount</code> - The amount of times to rotate the</dd>
</dl>
</div>
:::


</section>

<section id="rotate(net.minecraft.core.Direction.Axis)">

:::tabs
== rotate
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">rotate</span><wbr><span class="parameters">(net.minecraft.core.Direction.Axis&nbsp;axis)</span></div>
Rotates the current multistate block exactly once 90 degrees around the given axis.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>axis</code> - The axis to rotate around.</dd>
</dl>
</div>
:::


</section>

<section id="mirror(net.minecraft.core.Direction.Axis)">

:::tabs
== mirror
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">mirror</span><wbr><span class="parameters">(net.minecraft.core.Direction.Axis&nbsp;axis)</span></div>
Mirrors the current multistate block around the given axis.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>axis</code> - The axis to mirror over.</dd>
</dl>
</div>
:::


</section>

:::::
  

