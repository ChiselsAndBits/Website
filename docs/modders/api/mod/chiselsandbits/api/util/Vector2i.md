--- 
title: Vector2i
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Class Vector2i  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.Vector2i  
  
**All Implemented Interfaces:**  
Comparable\<Vector2i\>  

---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Vector2i</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><br/>  
implements <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&gt;</span></div>  

  

Mutable integer vector with two coordinates and helpers for grid-distance calculations.  

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
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td><div class="block">Codec for a two-coordinate vector represented by an integer stream.</div><br></td></tr>
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
  <tr><td><code><a href="#%3Cinit%3E(double,double)" class="member-name-link">Vector2i</a><wbr>(double&nbsp;xIn,<br> double&nbsp;yIn)</code></td><td><div class="block">Creates a vector by flooring each coordinate to the nearest integer not greater than it.</div><br></td></tr>
  <tr><td><code><a href="#%3Cinit%3E(int,int)" class="member-name-link">Vector2i</a><wbr>(int&nbsp;xIn,<br> int&nbsp;yIn)</code></td><td><div class="block">Creates a vector from integer coordinates.</div><br></td></tr>
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
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">compareTo</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;p_compareTo_1_)</code></td><td><div class="block">Orders vectors by y coordinate, then by x coordinate.</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(double,double,boolean)" class="member-name-link">distanceSq</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> boolean&nbsp;useCenter)</code></td><td><div class="block">Calculates squared distance to a point, optionally measuring from this vector's cell center.</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">distanceSq</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;to)</code></td><td><div class="block">Calculates squared distance from this cell's center to the given vector.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down()" class="member-name-link">down</a>()</code></td><td><div class="block">Returns this vector offset by one step downward.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down(int)" class="member-name-link">down</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Returns this vector offset downward by the requested number of steps.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;p_equals_1_)</code></td><td><div class="block">Compares this vector with another object by x and y coordinates.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getCoordinatesAsString()" class="member-name-link">getCoordinatesAsString</a>()</code></td><td><div class="block">Returns the coordinates as a comma-separated <code>x, y</code> string.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getX()" class="member-name-link">getX</a>()</code></td><td><div class="block">Gets the X coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getY()" class="member-name-link">getY</a>()</code></td><td><div class="block">Gets the Y coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash derived from this vector's coordinates.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#manhattanDistance(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">manhattanDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector)</code></td><td><div class="block">Calculates the Manhattan distance between this vector and another.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#offset(net.minecraft.core.Direction,int)" class="member-name-link">offset</a><wbr>(net.minecraft.core.Direction&nbsp;facing,<br> int&nbsp;n)</code></td><td><div class="block">Offsets this vector <code>n</code> steps in the given direction.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setX(int)" class="member-name-link">setX</a><wbr>(int&nbsp;xIn)</code></td><td><div class="block">Sets the X coordinate.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setY(int)" class="member-name-link">setY</a><wbr>(int&nbsp;yIn)</code></td><td><div class="block">Sets the Y coordinate.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string containing this vector's x and y coordinates.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up()" class="member-name-link">up</a>()</code></td><td><div class="block">Returns this vector offset by one step upward.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up(int)" class="member-name-link">up</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offsets this vector <code>n</code> steps upward.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(mod.chiselsandbits.api.util.Vector2i,double)" class="member-name-link">withinDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector,<br> double&nbsp;distance)</code></td><td><div class="block">Tests whether the squared distance between the coordinates is less than the squared limit.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(net.minecraft.core.Position,double)" class="member-name-link">withinDistance</a><wbr>(net.minecraft.core.Position&nbsp;position,<br> double&nbsp;distance)</code></td><td><div class="block">Tests whether this vector's cell center is strictly within the given distance of a position.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">compareTo</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;p_compareTo_1_)</code></td><td><div class="block">Orders vectors by y coordinate, then by x coordinate.</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(double,double,boolean)" class="member-name-link">distanceSq</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> boolean&nbsp;useCenter)</code></td><td><div class="block">Calculates squared distance to a point, optionally measuring from this vector's cell center.</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">distanceSq</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;to)</code></td><td><div class="block">Calculates squared distance from this cell's center to the given vector.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down()" class="member-name-link">down</a>()</code></td><td><div class="block">Returns this vector offset by one step downward.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down(int)" class="member-name-link">down</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Returns this vector offset downward by the requested number of steps.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;p_equals_1_)</code></td><td><div class="block">Compares this vector with another object by x and y coordinates.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getCoordinatesAsString()" class="member-name-link">getCoordinatesAsString</a>()</code></td><td><div class="block">Returns the coordinates as a comma-separated <code>x, y</code> string.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getX()" class="member-name-link">getX</a>()</code></td><td><div class="block">Gets the X coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getY()" class="member-name-link">getY</a>()</code></td><td><div class="block">Gets the Y coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash derived from this vector's coordinates.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#manhattanDistance(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">manhattanDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector)</code></td><td><div class="block">Calculates the Manhattan distance between this vector and another.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#offset(net.minecraft.core.Direction,int)" class="member-name-link">offset</a><wbr>(net.minecraft.core.Direction&nbsp;facing,<br> int&nbsp;n)</code></td><td><div class="block">Offsets this vector <code>n</code> steps in the given direction.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setX(int)" class="member-name-link">setX</a><wbr>(int&nbsp;xIn)</code></td><td><div class="block">Sets the X coordinate.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setY(int)" class="member-name-link">setY</a><wbr>(int&nbsp;yIn)</code></td><td><div class="block">Sets the Y coordinate.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string containing this vector's x and y coordinates.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up()" class="member-name-link">up</a>()</code></td><td><div class="block">Returns this vector offset by one step upward.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up(int)" class="member-name-link">up</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offsets this vector <code>n</code> steps upward.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(mod.chiselsandbits.api.util.Vector2i,double)" class="member-name-link">withinDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector,<br> double&nbsp;distance)</code></td><td><div class="block">Tests whether the squared distance between the coordinates is less than the squared limit.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(net.minecraft.core.Position,double)" class="member-name-link">withinDistance</a><wbr>(net.minecraft.core.Position&nbsp;position,<br> double&nbsp;distance)</code></td><td><div class="block">Tests whether this vector's cell center is strictly within the given distance of a position.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#compareTo(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">compareTo</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;p_compareTo_1_)</code></td><td><div class="block">Orders vectors by y coordinate, then by x coordinate.</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(double,double,boolean)" class="member-name-link">distanceSq</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> boolean&nbsp;useCenter)</code></td><td><div class="block">Calculates squared distance to a point, optionally measuring from this vector's cell center.</div><br></td></tr>
  <tr><td><code>double</code></td><td><code><a href="#distanceSq(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">distanceSq</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;to)</code></td><td><div class="block">Calculates squared distance from this cell's center to the given vector.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down()" class="member-name-link">down</a>()</code></td><td><div class="block">Returns this vector offset by one step downward.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#down(int)" class="member-name-link">down</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Returns this vector offset downward by the requested number of steps.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#equals(java.lang.Object)" class="member-name-link">equals</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;p_equals_1_)</code></td><td><div class="block">Compares this vector with another object by x and y coordinates.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#getCoordinatesAsString()" class="member-name-link">getCoordinatesAsString</a>()</code></td><td><div class="block">Returns the coordinates as a comma-separated <code>x, y</code> string.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getX()" class="member-name-link">getX</a>()</code></td><td><div class="block">Gets the X coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getY()" class="member-name-link">getY</a>()</code></td><td><div class="block">Gets the Y coordinate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#hashCode()" class="member-name-link">hashCode</a>()</code></td><td><div class="block">Returns a hash derived from this vector's coordinates.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#manhattanDistance(mod.chiselsandbits.api.util.Vector2i)" class="member-name-link">manhattanDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector)</code></td><td><div class="block">Calculates the Manhattan distance between this vector and another.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#offset(net.minecraft.core.Direction,int)" class="member-name-link">offset</a><wbr>(net.minecraft.core.Direction&nbsp;facing,<br> int&nbsp;n)</code></td><td><div class="block">Offsets this vector <code>n</code> steps in the given direction.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setX(int)" class="member-name-link">setX</a><wbr>(int&nbsp;xIn)</code></td><td><div class="block">Sets the X coordinate.</div><br></td></tr>
  <tr><td><code>protected void</code></td><td><code><a href="#setY(int)" class="member-name-link">setY</a><wbr>(int&nbsp;yIn)</code></td><td><div class="block">Sets the Y coordinate.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#toString()" class="member-name-link">toString</a>()</code></td><td><div class="block">Returns a string containing this vector's x and y coordinates.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up()" class="member-name-link">up</a>()</code></td><td><div class="block">Returns this vector offset by one step upward.</div><br></td></tr>
  <tr><td><code><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></code></td><td><code><a href="#up(int)" class="member-name-link">up</a><wbr>(int&nbsp;n)</code></td><td><div class="block">Offsets this vector <code>n</code> steps upward.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(mod.chiselsandbits.api.util.Vector2i,double)" class="member-name-link">withinDistance</a><wbr>(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector,<br> double&nbsp;distance)</code></td><td><div class="block">Tests whether the squared distance between the coordinates is less than the squared limit.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#withinDistance(net.minecraft.core.Position,double)" class="member-name-link">withinDistance</a><wbr>(net.minecraft.core.Position&nbsp;position,<br> double&nbsp;distance)</code></td><td><div class="block">Tests whether this vector's cell center is strictly within the given distance of a position.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="CODEC">

:::tabs
== CODEC
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
Codec for a two-coordinate vector represented by an integer stream.
</div>
:::


</section>

<section id="NULL_VECTOR">

:::tabs
== NULL_VECTOR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">NULL_VECTOR</span></div>
An immutable vector with zero as all coordinates.
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
Creates a vector by flooring each coordinate to the nearest integer not greater than it.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>xIn</code> - the x coordinate before flooring</dd>
<dd><code>yIn</code> - the y coordinate before flooring</dd>
</dl>
</div>
:::


</section>

<section id="<init>(int,int)">

:::tabs
== Vector2i
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">Vector2i</span><wbr><span class="parameters">(int&nbsp;xIn,
 int&nbsp;yIn)</span></div>
Creates a vector from integer coordinates.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>xIn</code> - the x coordinate</dd>
<dd><code>yIn</code> - the y coordinate</dd>
</dl>
</div>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="hashCode()">

:::tabs
== hashCode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">hashCode</span>()</div>
Returns a hash derived from this vector's coordinates.
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
</dl>
</div>
:::


</section>

<section id="equals(java.lang.Object)">

:::tabs
== equals
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">equals</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>&nbsp;p_equals_1_)</span></div>
Compares this vector with another object by x and y coordinates.
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
<dt>Parameters:</dt>
<dd><code>p_equals_1_</code> - the object to compare</dd>
<dt>Returns:</dt>
<dd><code>true</code> when the object is a vector with matching coordinates</dd>
</dl>
</div>
:::


</section>

<section id="getX()">

:::tabs
== getX
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getX</span>()</div>
Gets the X coordinate.
<dl class="notes">
<dt>Returns:</dt>
<dd>The x part of the coordinate.</dd>
</dl>
</div>
:::


</section>

<section id="getY()">

:::tabs
== getY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getY</span>()</div>
Gets the Y coordinate.
<dl class="notes">
<dt>Returns:</dt>
<dd>The y part of the coordinate.</dd>
</dl>
</div>
:::


</section>

<section id="setY(int)">

:::tabs
== setY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">protected</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setY</span><wbr><span class="parameters">(int&nbsp;yIn)</span></div>
Sets the Y coordinate.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>yIn</code> - The new y part of the coordinate</dd>
</dl>
</div>
:::


</section>

<section id="setX(int)">

:::tabs
== setX
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">protected</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setX</span><wbr><span class="parameters">(int&nbsp;xIn)</span></div>
Sets the X coordinate.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>xIn</code> - The new x part of the coordinate.</dd>
</dl>
</div>
:::


</section>

<section id="toString()">

:::tabs
== toString
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">toString</span>()</div>
Returns a string containing this vector's x and y coordinates.
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a></code>&nbsp;in class&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></code></dd>
</dl>
</div>
:::


</section>

<section id="compareTo(mod.chiselsandbits.api.util.Vector2i)">

:::tabs
== compareTo
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">compareTo</span><wbr><span class="parameters">(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;p_compareTo_1_)</span></div>
Orders vectors by y coordinate, then by x coordinate.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang" class="external-link">compareTo</a></code>&nbsp;in interface&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang" class="external-link">Comparable</a>&lt;<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>p_compareTo_1_</code> - the vector to compare with</dd>
<dt>Returns:</dt>
<dd>a negative value, zero, or a positive value according to the coordinate ordering</dd>
</dl>
</div>
:::


</section>

<section id="up()">

:::tabs
== up
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">up</span>()</div>
Returns this vector offset by one step upward.
<dl class="notes">
<dt>Returns:</dt>
<dd>the offset vector</dd>
</dl>
</div>
:::


</section>

<section id="up(int)">

:::tabs
== up
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">up</span><wbr><span class="parameters">(int&nbsp;n)</span></div>
Offsets this vector <code>n</code> steps upward.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>n</code> - number of steps to move</dd>
<dt>Returns:</dt>
<dd>the offset vector, or this vector when <code>n</code> is zero</dd>
</dl>
</div>
:::


</section>

<section id="offset(net.minecraft.core.Direction,int)">

:::tabs
== offset
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">offset</span><wbr><span class="parameters">(net.minecraft.core.Direction&nbsp;facing,
 int&nbsp;n)</span></div>
Offsets this vector <code>n</code> steps in the given direction.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>facing</code> - direction of movement</dd>
<dd><code>n</code> - number of steps to move</dd>
<dt>Returns:</dt>
<dd>the offset vector, or this vector when <code>n</code> is zero</dd>
</dl>
</div>
:::


</section>

<section id="down()">

:::tabs
== down
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">down</span>()</div>
Returns this vector offset by one step downward.
<dl class="notes">
<dt>Returns:</dt>
<dd>the offset vector</dd>
</dl>
</div>
:::


</section>

<section id="down(int)">

:::tabs
== down
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a></span>&nbsp;<span class="element-name">down</span><wbr><span class="parameters">(int&nbsp;n)</span></div>
Returns this vector offset downward by the requested number of steps.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>n</code> - number of steps to move</dd>
<dt>Returns:</dt>
<dd>the offset vector, or this vector when <code>n</code> is zero</dd>
</dl>
</div>
:::


</section>

<section id="withinDistance(mod.chiselsandbits.api.util.Vector2i,double)">

:::tabs
== withinDistance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">withinDistance</span><wbr><span class="parameters">(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector,
 double&nbsp;distance)</span></div>
Tests whether the squared distance between the coordinates is less than the squared limit.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector</code> - the other vector</dd>
<dd><code>distance</code> - maximum distance</dd>
<dt>Returns:</dt>
<dd><code>true</code> when the vectors are strictly closer than <code>distance</code></dd>
</dl>
</div>
:::


</section>

<section id="distanceSq(double,double,boolean)">

:::tabs
== distanceSq
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">distanceSq</span><wbr><span class="parameters">(double&nbsp;x,
 double&nbsp;y,
 boolean&nbsp;useCenter)</span></div>
Calculates squared distance to a point, optionally measuring from this vector's cell center.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - target x coordinate</dd>
<dd><code>y</code> - target y coordinate</dd>
<dd><code>useCenter</code> - whether to offset this vector's coordinates by one half</dd>
<dt>Returns:</dt>
<dd>squared Euclidean distance</dd>
</dl>
</div>
:::


</section>

<section id="withinDistance(net.minecraft.core.Position,double)">

:::tabs
== withinDistance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">withinDistance</span><wbr><span class="parameters">(net.minecraft.core.Position&nbsp;position,
 double&nbsp;distance)</span></div>
Tests whether this vector's cell center is strictly within the given distance of a position.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>position</code> - the position to measure to</dd>
<dd><code>distance</code> - maximum distance</dd>
<dt>Returns:</dt>
<dd><code>true</code> when the distance is less than <code>distance</code></dd>
</dl>
</div>
:::


</section>

<section id="distanceSq(mod.chiselsandbits.api.util.Vector2i)">

:::tabs
== distanceSq
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">distanceSq</span><wbr><span class="parameters">(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;to)</span></div>
Calculates squared distance from this cell's center to the given vector.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>to</code> - target vector</dd>
<dt>Returns:</dt>
<dd>squared Euclidean distance</dd>
</dl>
</div>
:::


</section>

<section id="manhattanDistance(mod.chiselsandbits.api.util.Vector2i)">

:::tabs
== manhattanDistance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">manhattanDistance</span><wbr><span class="parameters">(<a href="Vector2i.html" title="class in mod.chiselsandbits.api.util">Vector2i</a>&nbsp;vector)</span></div>
Calculates the Manhattan distance between this vector and another.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector</code> - the other vector</dd>
<dt>Returns:</dt>
<dd>the sum of absolute coordinate differences</dd>
</dl>
</div>
:::


</section>

<section id="getCoordinatesAsString()">

:::tabs
== getCoordinatesAsString
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">getCoordinatesAsString</span>()</div>
Returns the coordinates as a comma-separated <code>x, y</code> string.
<dl class="notes">
<dt>Returns:</dt>
<dd>the x and y coordinates separated by a comma and space</dd>
</dl>
</div>
:::


</section>

:::::
  

