--- 
title: Vector2i
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class Vector2i  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.Vector2i  
  
**All Implemented Interfaces:**  
Comparable\<Vector2i\>  

---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Vector2i</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><br/>  
implements <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&gt;</span></div>  

  

  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final <a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#NULL_VECTOR" class="member-name-link">NULL_VECTOR</a></code></td><td><div class="block">An immutable vector with zero as all coordinates.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E(double,double)" class="member-name-link">Vector2i</a><wbr>(double&nbsp;xIn,<br> double&nbsp;yIn)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="#%3Cinit%3E(int,int)" class="member-name-link">Vector2i</a><wbr>(int&nbsp;xIn,<br> int&nbsp;yIn)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">compareTo</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;p_compareTo_1_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(double,double,boolean)" class="member-name-link">distanceSq</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> boolean&nbsp;useCenter)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">distanceSq</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;to)</code></td><td><div class="block">Calculate squared distance to the given Vector</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down()" class="member-name-link">down</a>()</code></td><td><div class="block">Offset this BlockPos 1 block down</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down(int)" class="member-name-link">down</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offset this BlockPos n blocks down</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;p_equals_1_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getCoordinatesAsString()" class="member-name-link">getCoordinatesAsString</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getX()" class="member-name-link">getX</a>()</code></td><td><div class="block">Gets the X coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getY()" class="member-name-link">getY</a>()</code></td><td><div class="block">Gets the Y coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#manhattanDistance(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">manhattanDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#offset(net.minecraft.core.Direction,int)" class="member-name-link">offset</a><wbr>(net.minecraft.core.Direction&nbsp;facing,<br> int&nbsp;n)</code></td><td><div class="block">Offsets this BlockPos n blocks in the given direction</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setX(int)" class="member-name-link">setX</a><wbr>(int&nbsp;xIn)</code></td><td><div class="block">Sets the X coordinate.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setY(int)" class="member-name-link">setY</a><wbr>(int&nbsp;yIn)</code></td><td><div class="block">Sets the Y coordinate.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up()" class="member-name-link">up</a>()</code></td><td><div class="block">Offset this BlockPos 1 block up</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up(int)" class="member-name-link">up</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offset this BlockPos n blocks up</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(mod.chiselsandbits.api.util.Vector2i,double)" class="member-name-link">withinDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector,<br> double&nbsp;distance)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(net.minecraft.core.Position,double)" class="member-name-link">withinDistance</a><wbr>(net.minecraft.core.Position&nbsp;position,<br> double&nbsp;distance)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">compareTo</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;p_compareTo_1_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(double,double,boolean)" class="member-name-link">distanceSq</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> boolean&nbsp;useCenter)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">distanceSq</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;to)</code></td><td><div class="block">Calculate squared distance to the given Vector</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down()" class="member-name-link">down</a>()</code></td><td><div class="block">Offset this BlockPos 1 block down</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down(int)" class="member-name-link">down</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offset this BlockPos n blocks down</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;p_equals_1_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getCoordinatesAsString()" class="member-name-link">getCoordinatesAsString</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getX()" class="member-name-link">getX</a>()</code></td><td><div class="block">Gets the X coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getY()" class="member-name-link">getY</a>()</code></td><td><div class="block">Gets the Y coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#manhattanDistance(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">manhattanDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#offset(net.minecraft.core.Direction,int)" class="member-name-link">offset</a><wbr>(net.minecraft.core.Direction&nbsp;facing,<br> int&nbsp;n)</code></td><td><div class="block">Offsets this BlockPos n blocks in the given direction</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setX(int)" class="member-name-link">setX</a><wbr>(int&nbsp;xIn)</code></td><td><div class="block">Sets the X coordinate.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setY(int)" class="member-name-link">setY</a><wbr>(int&nbsp;yIn)</code></td><td><div class="block">Sets the Y coordinate.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up()" class="member-name-link">up</a>()</code></td><td><div class="block">Offset this BlockPos 1 block up</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up(int)" class="member-name-link">up</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offset this BlockPos n blocks up</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(mod.chiselsandbits.api.util.Vector2i,double)" class="member-name-link">withinDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector,<br> double&nbsp;distance)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(net.minecraft.core.Position,double)" class="member-name-link">withinDistance</a><wbr>(net.minecraft.core.Position&nbsp;position,<br> double&nbsp;distance)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">compareTo</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;p_compareTo_1_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(double,double,boolean)" class="member-name-link">distanceSq</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> boolean&nbsp;useCenter)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">distanceSq</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;to)</code></td><td><div class="block">Calculate squared distance to the given Vector</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down()" class="member-name-link">down</a>()</code></td><td><div class="block">Offset this BlockPos 1 block down</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down(int)" class="member-name-link">down</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offset this BlockPos n blocks down</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;p_equals_1_)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getCoordinatesAsString()" class="member-name-link">getCoordinatesAsString</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getX()" class="member-name-link">getX</a>()</code></td><td><div class="block">Gets the X coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getY()" class="member-name-link">getY</a>()</code></td><td><div class="block">Gets the Y coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#manhattanDistance(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">manhattanDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector)</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#offset(net.minecraft.core.Direction,int)" class="member-name-link">offset</a><wbr>(net.minecraft.core.Direction&nbsp;facing,<br> int&nbsp;n)</code></td><td><div class="block">Offsets this BlockPos n blocks in the given direction</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setX(int)" class="member-name-link">setX</a><wbr>(int&nbsp;xIn)</code></td><td><div class="block">Sets the X coordinate.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setY(int)" class="member-name-link">setY</a><wbr>(int&nbsp;yIn)</code></td><td><div class="block">Sets the Y coordinate.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up()" class="member-name-link">up</a>()</code></td><td><div class="block">Offset this BlockPos 1 block up</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up(int)" class="member-name-link">up</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offset this BlockPos n blocks up</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(mod.chiselsandbits.api.util.Vector2i,double)" class="member-name-link">withinDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector,<br> double&nbsp;distance)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(net.minecraft.core.Position,double)" class="member-name-link">withinDistance</a><wbr>(net.minecraft.core.Position&nbsp;position,<br> double&nbsp;distance)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="CODEC">

:::tabs
== CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
</div>
:::


</section>

<section id="NULL_VECTOR">

:::tabs
== NULL_VECTOR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">NULL_VECTOR</span></div>
<div class="block">An immutable vector with zero as all coordinates.</div>
</div>
:::


</section>

:::::
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(double,double)">

:::tabs
== Vector2i
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">Vector2i</span><wbr><span class="parameters">(double&nbsp;xIn,
 double&nbsp;yIn)</span></div>
</div>
:::


</section>

<section id="<init>(int,int)">

:::tabs
== Vector2i
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">Vector2i</span><wbr><span class="parameters">(int&nbsp;xIn,
 int&nbsp;yIn)</span></div>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="hashCode()">

:::tabs
== hashCode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="equals(java.lang.Object)">

:::tabs
== equals
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">equals</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;p_equals_1_)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getX()">

:::tabs
== getX
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getX</span>()</div>
<div class="block">Gets the X coordinate.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The x part of the coordinate.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getY()">

:::tabs
== getY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getY</span>()</div>
<div class="block">Gets the Y coordinate.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The y part of the coordinate.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="setY(int)">

:::tabs
== setY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">protected</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setY</span><wbr><span class="parameters">(int&nbsp;yIn)</span></div>
<div class="block">Sets the Y coordinate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>yIn</code> - The new y part of the coordinate</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="setX(int)">

:::tabs
== setX
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">protected</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setX</span><wbr><span class="parameters">(int&nbsp;xIn)</span></div>
<div class="block">Sets the X coordinate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>xIn</code> - The new x part of the coordinate.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="toString()">

:::tabs
== toString
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="compareTo(mod.chiselsandbits.api.util.Vector2i)">

:::tabs
== compareTo
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">compareTo</span><wbr><span class="parameters">(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;p_compareTo_1_)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang" class="external-link">compareTo</a></code>&nbsp;in interface&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&gt;</code></dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="up()">

:::tabs
== up
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">up</span>()</div>
<div class="block">Offset this BlockPos 1 block up</div>
</div>
:::


</section>

</li>
<li>
<section id="up(int)">

:::tabs
== up
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">up</span><wbr><span class="parameters">(int&nbsp;n)</span></div>
<div class="block">Offset this BlockPos n blocks up</div>
</div>
:::


</section>

</li>
<li>
<section id="offset(net.minecraft.core.Direction,int)">

:::tabs
== offset
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">offset</span><wbr><span class="parameters">(net.minecraft.core.Direction&nbsp;facing,
 int&nbsp;n)</span></div>
<div class="block">Offsets this BlockPos n blocks in the given direction</div>
</div>
:::


</section>

</li>
<li>
<section id="down()">

:::tabs
== down
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">down</span>()</div>
<div class="block">Offset this BlockPos 1 block down</div>
</div>
:::


</section>

</li>
<li>
<section id="down(int)">

:::tabs
== down
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">down</span><wbr><span class="parameters">(int&nbsp;n)</span></div>
<div class="block">Offset this BlockPos n blocks down</div>
</div>
:::


</section>

</li>
<li>
<section id="withinDistance(mod.chiselsandbits.api.util.Vector2i,double)">

:::tabs
== withinDistance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">withinDistance</span><wbr><span class="parameters">(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector,
 double&nbsp;distance)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="distanceSq(double,double,boolean)">

:::tabs
== distanceSq
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">distanceSq</span><wbr><span class="parameters">(double&nbsp;x,
 double&nbsp;y,
 boolean&nbsp;useCenter)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="withinDistance(net.minecraft.core.Position,double)">

:::tabs
== withinDistance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">withinDistance</span><wbr><span class="parameters">(net.minecraft.core.Position&nbsp;position,
 double&nbsp;distance)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="distanceSq(mod.chiselsandbits.api.util.Vector2i)">

:::tabs
== distanceSq
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">distanceSq</span><wbr><span class="parameters">(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;to)</span></div>
<div class="block">Calculate squared distance to the given Vector</div>
</div>
:::


</section>

</li>
<li>
<section id="manhattanDistance(mod.chiselsandbits.api.util.Vector2i)">

:::tabs
== manhattanDistance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">manhattanDistance</span><wbr><span class="parameters">(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="getCoordinatesAsString()">

:::tabs
== getCoordinatesAsString
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">getCoordinatesAsString</span>()</div>
</div>
:::


</section>

</li>
</ul>
:::::
  

