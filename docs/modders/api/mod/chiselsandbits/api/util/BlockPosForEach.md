--- 
title: BlockPosForEach
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Class BlockPosForEach  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.BlockPosForEach  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">BlockPosForEach</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Iterates over every <code>BlockPos</code> within an axis-aligned range of integer coordinates.  

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
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,int,int,int,int,int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;minX,<br> int&nbsp;minY,<br> int&nbsp;minZ,<br> int&nbsp;maxX,<br> int&nbsp;maxY,<br> int&nbsp;maxZ,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position within the inclusive bounds <code>minX..maxX</code> by <code>minY..maxY</code> by <code>minZ..maxZ</code>, invoking <code>consumer</code> for each.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,int,int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;xSize,<br> int&nbsp;ySize,<br> int&nbsp;zSize,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position in the <code>xSize</code> by <code>ySize</code> by <code>zSize</code> volume starting at the origin, invoking <code>consumer</code> for each.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;size,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over the cube <code>[0, size)</code> along each axis from the origin, invoking <code>consumer</code> for each position.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;min,<br> net.minecraft.world.phys.Vec3&nbsp;max,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position between the given minimum and maximum coordinates (inclusive), converting them to integer positions via <a href="VectorUtils.html#toBlockPos(net.minecraft.world.phys.Vec3)"><code>VectorUtils.toBlockPos(Vec3)</code></a>.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,int,int,int,int,int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;minX,<br> int&nbsp;minY,<br> int&nbsp;minZ,<br> int&nbsp;maxX,<br> int&nbsp;maxY,<br> int&nbsp;maxZ,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position within the inclusive bounds <code>minX..maxX</code> by <code>minY..maxY</code> by <code>minZ..maxZ</code>, invoking <code>consumer</code> for each.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,int,int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;xSize,<br> int&nbsp;ySize,<br> int&nbsp;zSize,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position in the <code>xSize</code> by <code>ySize</code> by <code>zSize</code> volume starting at the origin, invoking <code>consumer</code> for each.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;size,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over the cube <code>[0, size)</code> along each axis from the origin, invoking <code>consumer</code> for each position.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;min,<br> net.minecraft.world.phys.Vec3&nbsp;max,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position between the given minimum and maximum coordinates (inclusive), converting them to integer positions via <a href="VectorUtils.html#toBlockPos(net.minecraft.world.phys.Vec3)"><code>VectorUtils.toBlockPos(Vec3)</code></a>.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,int,int,int,int,int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;minX,<br> int&nbsp;minY,<br> int&nbsp;minZ,<br> int&nbsp;maxX,<br> int&nbsp;maxY,<br> int&nbsp;maxZ,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position within the inclusive bounds <code>minX..maxX</code> by <code>minY..maxY</code> by <code>minZ..maxZ</code>, invoking <code>consumer</code> for each.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,int,int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;xSize,<br> int&nbsp;ySize,<br> int&nbsp;zSize,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position in the <code>xSize</code> by <code>ySize</code> by <code>zSize</code> volume starting at the origin, invoking <code>consumer</code> for each.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(int,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(int&nbsp;size,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over the cube <code>[0, size)</code> along each axis from the origin, invoking <code>consumer</code> for each position.</div><br></td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#forEachInRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,java.util.function.Consumer)" class="member-name-link">forEachInRange</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;min,<br> net.minecraft.world.phys.Vec3&nbsp;max,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</code></td><td><div class="block">Iterates over every block position between the given minimum and maximum coordinates (inclusive), converting them to integer positions via <a href="VectorUtils.html#toBlockPos(net.minecraft.world.phys.Vec3)"><code>VectorUtils.toBlockPos(Vec3)</code></a>.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="forEachInRange(int,java.util.function.Consumer)">

:::tabs
== forEachInRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">forEachInRange</span><wbr><span class="parameters">(int&nbsp;size,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</span></div>
Iterates over the cube <code>[0, size)</code> along each axis from the origin, invoking <code>consumer</code> for each position.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - the exclusive upper bound for each coordinate</dd>
<dd><code>consumer</code> - receives each position in the range</dd>
</dl>
</div>
:::


</section>

<section id="forEachInRange(int,int,int,java.util.function.Consumer)">

:::tabs
== forEachInRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">forEachInRange</span><wbr><span class="parameters">(int&nbsp;xSize,
 int&nbsp;ySize,
 int&nbsp;zSize,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</span></div>
Iterates over every block position in the <code>xSize</code> by <code>ySize</code> by <code>zSize</code> volume starting at the origin, invoking <code>consumer</code> for each.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>xSize</code> - the exclusive upper bound for the x coordinate</dd>
<dd><code>ySize</code> - the exclusive upper bound for the y coordinate</dd>
<dd><code>zSize</code> - the exclusive upper bound for the z coordinate</dd>
<dd><code>consumer</code> - receives each position in the range</dd>
</dl>
</div>
:::


</section>

<section id="forEachInRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,java.util.function.Consumer)">

:::tabs
== forEachInRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">forEachInRange</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;min,
 net.minecraft.world.phys.Vec3&nbsp;max,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</span></div>
Iterates over every block position between the given minimum and maximum coordinates (inclusive), converting them to integer positions via <a href="VectorUtils.html#toBlockPos(net.minecraft.world.phys.Vec3)"><code>VectorUtils.toBlockPos(Vec3)</code></a>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>min</code> - minimum corner of the range</dd>
<dd><code>max</code> - maximum corner of the range</dd>
<dd><code>consumer</code> - receives each position in the range</dd>
</dl>
</div>
:::


</section>

<section id="forEachInRange(int,int,int,int,int,int,java.util.function.Consumer)">

:::tabs
== forEachInRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">forEachInRange</span><wbr><span class="parameters">(int&nbsp;minX,
 int&nbsp;minY,
 int&nbsp;minZ,
 int&nbsp;maxX,
 int&nbsp;maxY,
 int&nbsp;maxZ,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;net.minecraft.core.BlockPos&gt;&nbsp;consumer)</span></div>
Iterates over every block position within the inclusive bounds <code>minX..maxX</code> by <code>minY..maxY</code> by <code>minZ..maxZ</code>, invoking <code>consumer</code> for each.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>minX</code> - inclusive lower x bound</dd>
<dd><code>minY</code> - inclusive lower y bound</dd>
<dd><code>minZ</code> - inclusive lower z bound</dd>
<dd><code>maxX</code> - inclusive upper x bound</dd>
<dd><code>maxY</code> - inclusive upper y bound</dd>
<dd><code>maxZ</code> - inclusive upper z bound</dd>
<dd><code>consumer</code> - receives each position in the range</dd>
</dl>
</div>
:::


</section>

:::::
  

