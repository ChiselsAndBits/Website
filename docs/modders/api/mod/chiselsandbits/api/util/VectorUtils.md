--- 
title: VectorUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class VectorUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.VectorUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">VectorUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final double</code></td><td><code><a href="#DEG_TO_RAD_FACTOR" class="member-name-link">DEG_TO_RAD_FACTOR</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.world.phys.Vec3</code></td><td><code><a href="#ONE" class="member-name-link">ONE</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
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
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#absolute(net.minecraft.world.phys.Vec3)" class="member-name-link">absolute</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#allValuesBetweenInclusive(org.joml.Vector4f,float,float)" class="member-name-link">allValuesBetweenInclusive</a><wbr>(org.joml.Vector4f&nbsp;vector4f,<br> float&nbsp;min,<br> float&nbsp;max)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#divide(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">divide</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;left,<br> net.minecraft.world.phys.Vec3&nbsp;right)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#getMaximalComponent(net.minecraft.world.phys.Vec3)" class="member-name-link">getMaximalComponent</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#invert(net.minecraft.core.BlockPos)" class="member-name-link">invert</a><wbr>(net.minecraft.core.BlockPos&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#invert(net.minecraft.world.phys.Vec3)" class="member-name-link">invert</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#makePositive(net.minecraft.world.phys.Vec3)" class="member-name-link">makePositive</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inBlockOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximizeAwayFromZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximizeAwayFromZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimizeTowardsZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimizeTowardsZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyNegatives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyNegatives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyPositives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyPositives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#offsetRandomly(net.minecraft.world.phys.Vec3,net.minecraft.util.RandomSource,float)" class="member-name-link">offsetRandomly</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;source,<br> net.minecraft.util.RandomSource&nbsp;random,<br> float&nbsp;radius)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotate</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInRadian)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotate90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateDegrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotateDegrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInDegrees)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateHalfRadian(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotateHalfRadian</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateMultipleTimes90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotateMultipleTimes90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;times)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#scaleToOne(net.minecraft.world.phys.Vec3)" class="member-name-link">scaleToOne</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#toBlockPos(net.minecraft.world.phys.Vec3)" class="member-name-link">toBlockPos</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(double,double,double)" class="member-name-link">toInteger</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> double&nbsp;z)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(net.minecraft.world.phys.Vec3)" class="member-name-link">toInteger</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#absolute(net.minecraft.world.phys.Vec3)" class="member-name-link">absolute</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#allValuesBetweenInclusive(org.joml.Vector4f,float,float)" class="member-name-link">allValuesBetweenInclusive</a><wbr>(org.joml.Vector4f&nbsp;vector4f,<br> float&nbsp;min,<br> float&nbsp;max)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#divide(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">divide</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;left,<br> net.minecraft.world.phys.Vec3&nbsp;right)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#getMaximalComponent(net.minecraft.world.phys.Vec3)" class="member-name-link">getMaximalComponent</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#invert(net.minecraft.core.BlockPos)" class="member-name-link">invert</a><wbr>(net.minecraft.core.BlockPos&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#invert(net.minecraft.world.phys.Vec3)" class="member-name-link">invert</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#makePositive(net.minecraft.world.phys.Vec3)" class="member-name-link">makePositive</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inBlockOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximizeAwayFromZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximizeAwayFromZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimizeTowardsZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimizeTowardsZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyNegatives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyNegatives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyPositives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyPositives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#offsetRandomly(net.minecraft.world.phys.Vec3,net.minecraft.util.RandomSource,float)" class="member-name-link">offsetRandomly</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;source,<br> net.minecraft.util.RandomSource&nbsp;random,<br> float&nbsp;radius)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotate</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInRadian)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotate90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateDegrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotateDegrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInDegrees)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateHalfRadian(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotateHalfRadian</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateMultipleTimes90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotateMultipleTimes90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;times)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#scaleToOne(net.minecraft.world.phys.Vec3)" class="member-name-link">scaleToOne</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#toBlockPos(net.minecraft.world.phys.Vec3)" class="member-name-link">toBlockPos</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(double,double,double)" class="member-name-link">toInteger</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> double&nbsp;z)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(net.minecraft.world.phys.Vec3)" class="member-name-link">toInteger</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#absolute(net.minecraft.world.phys.Vec3)" class="member-name-link">absolute</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#allValuesBetweenInclusive(org.joml.Vector4f,float,float)" class="member-name-link">allValuesBetweenInclusive</a><wbr>(org.joml.Vector4f&nbsp;vector4f,<br> float&nbsp;min,<br> float&nbsp;max)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#divide(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">divide</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;left,<br> net.minecraft.world.phys.Vec3&nbsp;right)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#getMaximalComponent(net.minecraft.world.phys.Vec3)" class="member-name-link">getMaximalComponent</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#invert(net.minecraft.core.BlockPos)" class="member-name-link">invert</a><wbr>(net.minecraft.core.BlockPos&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#invert(net.minecraft.world.phys.Vec3)" class="member-name-link">invert</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#makePositive(net.minecraft.world.phys.Vec3)" class="member-name-link">makePositive</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inBlockOffset)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximizeAwayFromZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximizeAwayFromZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimizeTowardsZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimizeTowardsZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyNegatives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyNegatives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyPositives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyPositives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#offsetRandomly(net.minecraft.world.phys.Vec3,net.minecraft.util.RandomSource,float)" class="member-name-link">offsetRandomly</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;source,<br> net.minecraft.util.RandomSource&nbsp;random,<br> float&nbsp;radius)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotate</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInRadian)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotate90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateDegrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotateDegrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInDegrees)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateHalfRadian(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotateHalfRadian</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateMultipleTimes90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotateMultipleTimes90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;times)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#scaleToOne(net.minecraft.world.phys.Vec3)" class="member-name-link">scaleToOne</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#toBlockPos(net.minecraft.world.phys.Vec3)" class="member-name-link">toBlockPos</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(double,double,double)" class="member-name-link">toInteger</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> double&nbsp;z)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(net.minecraft.world.phys.Vec3)" class="member-name-link">toInteger</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="DEG_TO_RAD_FACTOR">

:::tabs
== DEG_TO_RAD_FACTOR
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">DEG_TO_RAD_FACTOR</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="ONE">

:::tabs
== ONE
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">ONE</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="rotateMultipleTimes90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,int)">

:::tabs
== rotateMultipleTimes90Degrees
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotateMultipleTimes90Degrees</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis,
 int&nbsp;times)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="rotate90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)">

:::tabs
== rotate90Degrees
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotate90Degrees</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="rotateHalfRadian(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)">

:::tabs
== rotateHalfRadian
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotateHalfRadian</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="rotateDegrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)">

:::tabs
== rotateDegrees
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotateDegrees</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis,
 double&nbsp;angleInDegrees)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="rotate(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)">

:::tabs
== rotate
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotate</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis,
 double&nbsp;angleInRadian)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="scaleToOne(net.minecraft.world.phys.Vec3)">

:::tabs
== scaleToOne
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">scaleToOne</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;v)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="getMaximalComponent(net.minecraft.world.phys.Vec3)">

:::tabs
== getMaximalComponent
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">getMaximalComponent</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;v)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="invert(net.minecraft.world.phys.Vec3)">

:::tabs
== invert
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">invert</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;v)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="invert(net.minecraft.core.BlockPos)">

:::tabs
== invert
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">invert</span><wbr><span class="parameters">(net.minecraft.core.BlockPos&nbsp;v)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="minimizeTowardsZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== minimizeTowardsZero
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">minimizeTowardsZero</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;start,
 net.minecraft.world.phys.Vec3&nbsp;end)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="maximizeAwayFromZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== maximizeAwayFromZero
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">maximizeAwayFromZero</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;start,
 net.minecraft.world.phys.Vec3&nbsp;end)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="absolute(net.minecraft.world.phys.Vec3)">

:::tabs
== absolute
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">absolute</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="offsetRandomly(net.minecraft.world.phys.Vec3,net.minecraft.util.RandomSource,float)">

:::tabs
== offsetRandomly
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">offsetRandomly</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;source,
 net.minecraft.util.RandomSource&nbsp;random,
 float&nbsp;radius)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="minimize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== minimize
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">minimize</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;a,
 net.minecraft.world.phys.Vec3&nbsp;b)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="maximize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== maximize
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">maximize</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;a,
 net.minecraft.world.phys.Vec3&nbsp;b)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="makePositive(net.minecraft.world.phys.Vec3)">

:::tabs
== makePositive
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">makePositive</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;inBlockOffset)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="allValuesBetweenInclusive(org.joml.Vector4f,float,float)">

:::tabs
== allValuesBetweenInclusive
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">allValuesBetweenInclusive</span><wbr><span class="parameters">(org.joml.Vector4f&nbsp;vector4f,
 float&nbsp;min,
 float&nbsp;max)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="nullifyNegatives(net.minecraft.world.phys.Vec3)">

:::tabs
== nullifyNegatives
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">nullifyNegatives</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;input)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="nullifyPositives(net.minecraft.world.phys.Vec3)">

:::tabs
== nullifyPositives
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">nullifyPositives</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;input)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="divide(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== divide
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">divide</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;left,
 net.minecraft.world.phys.Vec3&nbsp;right)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="toBlockPos(net.minecraft.world.phys.Vec3)">

:::tabs
== toBlockPos
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">toBlockPos</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vec3)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="toInteger(net.minecraft.world.phys.Vec3)">

:::tabs
== toInteger
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.Vec3i</span>&nbsp;<span class="element-name">toInteger</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vec3)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="toInteger(double,double,double)">

:::tabs
== toInteger
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.Vec3i</span>&nbsp;<span class="element-name">toInteger</span><wbr><span class="parameters">(double&nbsp;x,
 double&nbsp;y,
 double&nbsp;z)</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

