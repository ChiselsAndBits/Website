--- 
title: VectorUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Class VectorUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.VectorUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">VectorUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility methods for converting, normalizing, and transforming Minecraft vectors.  

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
  <tr><td><code>static final double</code></td><td><code><a href="#DEG_TO_RAD_FACTOR" class="member-name-link">DEG_TO_RAD_FACTOR</a></code></td><td><div class="block">Factor for converting degrees to radians.</div><br></td></tr>
  <tr><td><code>static final net.minecraft.world.phys.Vec3</code></td><td><code><a href="#ONE" class="member-name-link">ONE</a></code></td><td><div class="block">Unit vector with all three coordinates equal to one.</div><br></td></tr>
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
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#absolute(net.minecraft.world.phys.Vec3)" class="member-name-link">absolute</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d)</code></td><td><div class="block">Returns a vector containing the absolute value of each component.</div><br></td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#allValuesBetweenInclusive(org.joml.Vector4f,float,float)" class="member-name-link">allValuesBetweenInclusive</a><wbr>(org.joml.Vector4f&nbsp;vector4f,<br> float&nbsp;min,<br> float&nbsp;max)</code></td><td><div class="block">Tests whether all four components lie within the inclusive interval.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#divide(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">divide</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;left,<br> net.minecraft.world.phys.Vec3&nbsp;right)</code></td><td><div class="block">Divides each component of the left vector by the corresponding right component.</div><br></td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#getMaximalComponent(net.minecraft.world.phys.Vec3)" class="member-name-link">getMaximalComponent</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Returns the signed component with the greatest absolute magnitude.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#invert(net.minecraft.core.BlockPos)" class="member-name-link">invert</a><wbr>(net.minecraft.core.BlockPos&nbsp;v)</code></td><td><div class="block">Negates all coordinates of the supplied block position.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#invert(net.minecraft.world.phys.Vec3)" class="member-name-link">invert</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Negates all components of the supplied vector.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#makePositive(net.minecraft.world.phys.Vec3)" class="member-name-link">makePositive</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inBlockOffset)</code></td><td><div class="block">Makes each component of a block-relative offset non-negative.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td><div class="block">Returns the component-wise maximum of two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximizeAwayFromZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximizeAwayFromZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td><div class="block">Chooses, component by component, the value farther from zero between two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td><div class="block">Returns the component-wise minimum of two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimizeTowardsZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimizeTowardsZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td><div class="block">Chooses, component by component, the value closer to zero between two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyNegatives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyNegatives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td><div class="block">Replaces negative vector components with zero.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyPositives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyPositives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td><div class="block">Replaces positive vector components with zero.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#offsetRandomly(net.minecraft.world.phys.Vec3,net.minecraft.util.RandomSource,float)" class="member-name-link">offsetRandomly</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;source,<br> net.minecraft.util.RandomSource&nbsp;random,<br> float&nbsp;radius)</code></td><td><div class="block">Adds a random offset in the range <code>[-radius, radius]</code> to each component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotate</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInRadian)</code></td><td><div class="block">Rotates a vector by an angle in radians around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotate90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates a vector 90 degrees around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateDegrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotateDegrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInDegrees)</code></td><td><div class="block">Rotates a vector by an angle in degrees around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateHalfRadian(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotateHalfRadian</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates a vector by half a radian around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateMultipleTimes90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotateMultipleTimes90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;times)</code></td><td><div class="block">Rotates a vector around an axis by a multiple of 90 degrees.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#scaleToOne(net.minecraft.world.phys.Vec3)" class="member-name-link">scaleToOne</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Scales a vector so that its largest absolute component is one.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#toBlockPos(net.minecraft.world.phys.Vec3)" class="member-name-link">toBlockPos</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td><div class="block">Converts a vector to block coordinates by flooring each component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(double,double,double)" class="member-name-link">toInteger</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> double&nbsp;z)</code></td><td><div class="block">Creates integer coordinates by flooring each supplied component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(net.minecraft.world.phys.Vec3)" class="member-name-link">toInteger</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td><div class="block">Converts a vector to integer coordinates by flooring each component.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#absolute(net.minecraft.world.phys.Vec3)" class="member-name-link">absolute</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d)</code></td><td><div class="block">Returns a vector containing the absolute value of each component.</div><br></td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#allValuesBetweenInclusive(org.joml.Vector4f,float,float)" class="member-name-link">allValuesBetweenInclusive</a><wbr>(org.joml.Vector4f&nbsp;vector4f,<br> float&nbsp;min,<br> float&nbsp;max)</code></td><td><div class="block">Tests whether all four components lie within the inclusive interval.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#divide(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">divide</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;left,<br> net.minecraft.world.phys.Vec3&nbsp;right)</code></td><td><div class="block">Divides each component of the left vector by the corresponding right component.</div><br></td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#getMaximalComponent(net.minecraft.world.phys.Vec3)" class="member-name-link">getMaximalComponent</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Returns the signed component with the greatest absolute magnitude.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#invert(net.minecraft.core.BlockPos)" class="member-name-link">invert</a><wbr>(net.minecraft.core.BlockPos&nbsp;v)</code></td><td><div class="block">Negates all coordinates of the supplied block position.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#invert(net.minecraft.world.phys.Vec3)" class="member-name-link">invert</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Negates all components of the supplied vector.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#makePositive(net.minecraft.world.phys.Vec3)" class="member-name-link">makePositive</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inBlockOffset)</code></td><td><div class="block">Makes each component of a block-relative offset non-negative.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td><div class="block">Returns the component-wise maximum of two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximizeAwayFromZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximizeAwayFromZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td><div class="block">Chooses, component by component, the value farther from zero between two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td><div class="block">Returns the component-wise minimum of two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimizeTowardsZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimizeTowardsZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td><div class="block">Chooses, component by component, the value closer to zero between two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyNegatives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyNegatives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td><div class="block">Replaces negative vector components with zero.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyPositives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyPositives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td><div class="block">Replaces positive vector components with zero.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#offsetRandomly(net.minecraft.world.phys.Vec3,net.minecraft.util.RandomSource,float)" class="member-name-link">offsetRandomly</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;source,<br> net.minecraft.util.RandomSource&nbsp;random,<br> float&nbsp;radius)</code></td><td><div class="block">Adds a random offset in the range <code>[-radius, radius]</code> to each component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotate</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInRadian)</code></td><td><div class="block">Rotates a vector by an angle in radians around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotate90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates a vector 90 degrees around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateDegrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotateDegrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInDegrees)</code></td><td><div class="block">Rotates a vector by an angle in degrees around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateHalfRadian(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotateHalfRadian</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates a vector by half a radian around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateMultipleTimes90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotateMultipleTimes90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;times)</code></td><td><div class="block">Rotates a vector around an axis by a multiple of 90 degrees.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#scaleToOne(net.minecraft.world.phys.Vec3)" class="member-name-link">scaleToOne</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Scales a vector so that its largest absolute component is one.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#toBlockPos(net.minecraft.world.phys.Vec3)" class="member-name-link">toBlockPos</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td><div class="block">Converts a vector to block coordinates by flooring each component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(double,double,double)" class="member-name-link">toInteger</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> double&nbsp;z)</code></td><td><div class="block">Creates integer coordinates by flooring each supplied component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(net.minecraft.world.phys.Vec3)" class="member-name-link">toInteger</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td><div class="block">Converts a vector to integer coordinates by flooring each component.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#absolute(net.minecraft.world.phys.Vec3)" class="member-name-link">absolute</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d)</code></td><td><div class="block">Returns a vector containing the absolute value of each component.</div><br></td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#allValuesBetweenInclusive(org.joml.Vector4f,float,float)" class="member-name-link">allValuesBetweenInclusive</a><wbr>(org.joml.Vector4f&nbsp;vector4f,<br> float&nbsp;min,<br> float&nbsp;max)</code></td><td><div class="block">Tests whether all four components lie within the inclusive interval.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#divide(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">divide</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;left,<br> net.minecraft.world.phys.Vec3&nbsp;right)</code></td><td><div class="block">Divides each component of the left vector by the corresponding right component.</div><br></td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#getMaximalComponent(net.minecraft.world.phys.Vec3)" class="member-name-link">getMaximalComponent</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Returns the signed component with the greatest absolute magnitude.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#invert(net.minecraft.core.BlockPos)" class="member-name-link">invert</a><wbr>(net.minecraft.core.BlockPos&nbsp;v)</code></td><td><div class="block">Negates all coordinates of the supplied block position.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#invert(net.minecraft.world.phys.Vec3)" class="member-name-link">invert</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Negates all components of the supplied vector.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#makePositive(net.minecraft.world.phys.Vec3)" class="member-name-link">makePositive</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inBlockOffset)</code></td><td><div class="block">Makes each component of a block-relative offset non-negative.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td><div class="block">Returns the component-wise maximum of two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#maximizeAwayFromZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">maximizeAwayFromZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td><div class="block">Chooses, component by component, the value farther from zero between two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimize</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;a,<br> net.minecraft.world.phys.Vec3&nbsp;b)</code></td><td><div class="block">Returns the component-wise minimum of two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#minimizeTowardsZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">minimizeTowardsZero</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;start,<br> net.minecraft.world.phys.Vec3&nbsp;end)</code></td><td><div class="block">Chooses, component by component, the value closer to zero between two vectors.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyNegatives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyNegatives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td><div class="block">Replaces negative vector components with zero.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#nullifyPositives(net.minecraft.world.phys.Vec3)" class="member-name-link">nullifyPositives</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;input)</code></td><td><div class="block">Replaces positive vector components with zero.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#offsetRandomly(net.minecraft.world.phys.Vec3,net.minecraft.util.RandomSource,float)" class="member-name-link">offsetRandomly</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;source,<br> net.minecraft.util.RandomSource&nbsp;random,<br> float&nbsp;radius)</code></td><td><div class="block">Adds a random offset in the range <code>[-radius, radius]</code> to each component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotate</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInRadian)</code></td><td><div class="block">Rotates a vector by an angle in radians around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotate90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotate90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates a vector 90 degrees around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateDegrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)" class="member-name-link">rotateDegrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> double&nbsp;angleInDegrees)</code></td><td><div class="block">Rotates a vector by an angle in degrees around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateHalfRadian(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)" class="member-name-link">rotateHalfRadian</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Rotates a vector by half a radian around the given axis.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#rotateMultipleTimes90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,int)" class="member-name-link">rotateMultipleTimes90Degrees</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vector3d,<br> net.minecraft.core.Direction.Axis&nbsp;axis,<br> int&nbsp;times)</code></td><td><div class="block">Rotates a vector around an axis by a multiple of 90 degrees.</div><br></td></tr>
  <tr><td><code>static net.minecraft.world.phys.Vec3</code></td><td><code><a href="#scaleToOne(net.minecraft.world.phys.Vec3)" class="member-name-link">scaleToOne</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;v)</code></td><td><div class="block">Scales a vector so that its largest absolute component is one.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.BlockPos</code></td><td><code><a href="#toBlockPos(net.minecraft.world.phys.Vec3)" class="member-name-link">toBlockPos</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td><div class="block">Converts a vector to block coordinates by flooring each component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(double,double,double)" class="member-name-link">toInteger</a><wbr>(double&nbsp;x,<br> double&nbsp;y,<br> double&nbsp;z)</code></td><td><div class="block">Creates integer coordinates by flooring each supplied component.</div><br></td></tr>
  <tr><td><code>static net.minecraft.core.Vec3i</code></td><td><code><a href="#toInteger(net.minecraft.world.phys.Vec3)" class="member-name-link">toInteger</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;vec3)</code></td><td><div class="block">Converts a vector to integer coordinates by flooring each component.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="DEG_TO_RAD_FACTOR">

:::tabs
== DEG_TO_RAD_FACTOR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">DEG_TO_RAD_FACTOR</span></div>
Factor for converting degrees to radians.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#mod.chiselsandbits.api.util.VectorUtils.DEG_TO_RAD_FACTOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="ONE">

:::tabs
== ONE
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">ONE</span></div>
Unit vector with all three coordinates equal to one.
</div>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="rotateMultipleTimes90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,int)">

:::tabs
== rotateMultipleTimes90Degrees
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotateMultipleTimes90Degrees</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis,
 int&nbsp;times)</span></div>
Rotates a vector around an axis by a multiple of 90 degrees.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector3d</code> - vector to rotate</dd>
<dd><code>axis</code> - rotation axis</dd>
<dd><code>times</code> - number of quarter-turns</dd>
<dt>Returns:</dt>
<dd>the rotated vector</dd>
</dl>
</div>
:::


</section>

<section id="rotate90Degrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)">

:::tabs
== rotate90Degrees
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotate90Degrees</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis)</span></div>
Rotates a vector 90 degrees around the given axis.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector3d</code> - vector to rotate</dd>
<dd><code>axis</code> - axis about which to rotate</dd>
<dt>Returns:</dt>
<dd>the vector after a positive quarter-turn around <code>axis</code></dd>
</dl>
</div>
:::


</section>

<section id="rotateHalfRadian(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis)">

:::tabs
== rotateHalfRadian
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotateHalfRadian</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis)</span></div>
Rotates a vector by half a radian around the given axis.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector3d</code> - vector to rotate</dd>
<dd><code>axis</code> - axis about which to rotate</dd>
<dt>Returns:</dt>
<dd>the vector after a half-radian rotation around <code>axis</code></dd>
</dl>
</div>
:::


</section>

<section id="rotateDegrees(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)">

:::tabs
== rotateDegrees
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotateDegrees</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis,
 double&nbsp;angleInDegrees)</span></div>
Rotates a vector by an angle in degrees around the given axis.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector3d</code> - vector to rotate</dd>
<dd><code>axis</code> - axis about which to rotate</dd>
<dd><code>angleInDegrees</code> - rotation angle in degrees</dd>
<dt>Returns:</dt>
<dd>the rotated vector</dd>
</dl>
</div>
:::


</section>

<section id="rotate(net.minecraft.world.phys.Vec3,net.minecraft.core.Direction.Axis,double)">

:::tabs
== rotate
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">rotate</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d,
 net.minecraft.core.Direction.Axis&nbsp;axis,
 double&nbsp;angleInRadian)</span></div>
Rotates a vector by an angle in radians around the given axis.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector3d</code> - vector to rotate</dd>
<dd><code>axis</code> - axis about which to rotate</dd>
<dd><code>angleInRadian</code> - rotation angle in radians</dd>
<dt>Returns:</dt>
<dd>the rotated vector</dd>
</dl>
</div>
:::


</section>

<section id="scaleToOne(net.minecraft.world.phys.Vec3)">

:::tabs
== scaleToOne
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">scaleToOne</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;v)</span></div>
Scales a vector so that its largest absolute component is one.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - vector to scale</dd>
<dt>Returns:</dt>
<dd>a vector whose largest absolute component is one, or <code>Vec3.ZERO</code> for a zero vector</dd>
</dl>
</div>
:::


</section>

<section id="getMaximalComponent(net.minecraft.world.phys.Vec3)">

:::tabs
== getMaximalComponent
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">getMaximalComponent</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;v)</span></div>
Returns the signed component with the greatest absolute magnitude.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - vector whose components are compared</dd>
<dt>Returns:</dt>
<dd>the component with the greatest absolute magnitude, retaining its sign</dd>
</dl>
</div>
:::


</section>

<section id="invert(net.minecraft.world.phys.Vec3)">

:::tabs
== invert
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">invert</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;v)</span></div>
Negates all components of the supplied vector.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - vector to negate</dd>
<dt>Returns:</dt>
<dd>a new vector with each component negated</dd>
</dl>
</div>
:::


</section>

<section id="invert(net.minecraft.core.BlockPos)">

:::tabs
== invert
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">invert</span><wbr><span class="parameters">(net.minecraft.core.BlockPos&nbsp;v)</span></div>
Negates all coordinates of the supplied block position.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - block position to negate</dd>
<dt>Returns:</dt>
<dd>a new block position with each coordinate negated</dd>
</dl>
</div>
:::


</section>

<section id="minimizeTowardsZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== minimizeTowardsZero
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">minimizeTowardsZero</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;start,
 net.minecraft.world.phys.Vec3&nbsp;end)</span></div>
Chooses, component by component, the value closer to zero between two vectors.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>start</code> - first vector</dd>
<dd><code>end</code> - second vector</dd>
<dt>Returns:</dt>
<dd>a vector containing the component-wise values closer to zero</dd>
</dl>
</div>
:::


</section>

<section id="maximizeAwayFromZero(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== maximizeAwayFromZero
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">maximizeAwayFromZero</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;start,
 net.minecraft.world.phys.Vec3&nbsp;end)</span></div>
Chooses, component by component, the value farther from zero between two vectors.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>start</code> - first vector</dd>
<dd><code>end</code> - second vector</dd>
<dt>Returns:</dt>
<dd>a vector containing the component-wise values farther from zero</dd>
</dl>
</div>
:::


</section>

<section id="absolute(net.minecraft.world.phys.Vec3)">

:::tabs
== absolute
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">absolute</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vector3d)</span></div>
Returns a vector containing the absolute value of each component.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector3d</code> - vector whose components are made non-negative</dd>
<dt>Returns:</dt>
<dd>a vector containing the absolute values of the input components</dd>
</dl>
</div>
:::


</section>

<section id="offsetRandomly(net.minecraft.world.phys.Vec3,net.minecraft.util.RandomSource,float)">

:::tabs
== offsetRandomly
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">offsetRandomly</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;source,
 net.minecraft.util.RandomSource&nbsp;random,
 float&nbsp;radius)</span></div>
Adds a random offset in the range <code>[-radius, radius]</code> to each component.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - vector to offset</dd>
<dd><code>random</code> - random source for the three offsets</dd>
<dd><code>radius</code> - maximum absolute offset on each component</dd>
<dt>Returns:</dt>
<dd>the offset vector</dd>
</dl>
</div>
:::


</section>

<section id="minimize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== minimize
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">minimize</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;a,
 net.minecraft.world.phys.Vec3&nbsp;b)</span></div>
Returns the component-wise minimum of two vectors.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - first vector</dd>
<dd><code>b</code> - second vector</dd>
<dt>Returns:</dt>
<dd>a vector containing the smaller component from each input pair</dd>
</dl>
</div>
:::


</section>

<section id="maximize(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== maximize
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">maximize</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;a,
 net.minecraft.world.phys.Vec3&nbsp;b)</span></div>
Returns the component-wise maximum of two vectors.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - first vector</dd>
<dd><code>b</code> - second vector</dd>
<dt>Returns:</dt>
<dd>a vector containing the larger component from each input pair</dd>
</dl>
</div>
:::


</section>

<section id="makePositive(net.minecraft.world.phys.Vec3)">

:::tabs
== makePositive
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">makePositive</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;inBlockOffset)</span></div>
Makes each component of a block-relative offset non-negative.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inBlockOffset</code> - block-relative offset to normalize</dd>
<dt>Returns:</dt>
<dd>a vector with each component in the range <code>[0, 1)</code></dd>
</dl>
</div>
:::


</section>

<section id="allValuesBetweenInclusive(org.joml.Vector4f,float,float)">

:::tabs
== allValuesBetweenInclusive
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">allValuesBetweenInclusive</span><wbr><span class="parameters">(org.joml.Vector4f&nbsp;vector4f,
 float&nbsp;min,
 float&nbsp;max)</span></div>
Tests whether all four components lie within the inclusive interval.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector4f</code> - four-component vector to test</dd>
<dd><code>min</code> - inclusive lower bound for each component</dd>
<dd><code>max</code> - inclusive upper bound for each component</dd>
<dt>Returns:</dt>
<dd><code>true</code> if every component is between <code>min</code> and <code>max</code>, inclusive</dd>
</dl>
</div>
:::


</section>

<section id="nullifyNegatives(net.minecraft.world.phys.Vec3)">

:::tabs
== nullifyNegatives
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">nullifyNegatives</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;input)</span></div>
Replaces negative vector components with zero.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - vector to clamp</dd>
<dt>Returns:</dt>
<dd>a vector with negative components replaced by zero</dd>
</dl>
</div>
:::


</section>

<section id="nullifyPositives(net.minecraft.world.phys.Vec3)">

:::tabs
== nullifyPositives
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">nullifyPositives</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;input)</span></div>
Replaces positive vector components with zero.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - vector to clamp</dd>
<dt>Returns:</dt>
<dd>a vector with positive components replaced by zero</dd>
</dl>
</div>
:::


</section>

<section id="divide(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== divide
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">divide</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;left,
 net.minecraft.world.phys.Vec3&nbsp;right)</span></div>
Divides each component of the left vector by the corresponding right component.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>left</code> - vector providing the numerators</dd>
<dd><code>right</code> - vector providing the denominators</dd>
<dt>Returns:</dt>
<dd>the component-wise quotient</dd>
</dl>
</div>
:::


</section>

<section id="toBlockPos(net.minecraft.world.phys.Vec3)">

:::tabs
== toBlockPos
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">toBlockPos</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vec3)</span></div>
Converts a vector to block coordinates by flooring each component.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vec3</code> - vector to convert.</dd>
<dt>Returns:</dt>
<dd>the converted value.</dd>
</dl>
</div>
:::


</section>

<section id="toInteger(net.minecraft.world.phys.Vec3)">

:::tabs
== toInteger
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.Vec3i</span>&nbsp;<span class="element-name">toInteger</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;vec3)</span></div>
Converts a vector to integer coordinates by flooring each component.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vec3</code> - vector to convert.</dd>
<dt>Returns:</dt>
<dd>the converted value.</dd>
</dl>
</div>
:::


</section>

<section id="toInteger(double,double,double)">

:::tabs
== toInteger
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.core.Vec3i</span>&nbsp;<span class="element-name">toInteger</span><wbr><span class="parameters">(double&nbsp;x,
 double&nbsp;y,
 double&nbsp;z)</span></div>
Creates integer coordinates by flooring each supplied component.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - x coordinate.</dd>
<dd><code>y</code> - y coordinate.</dd>
<dd><code>z</code> - z coordinate.</dd>
<dt>Returns:</dt>
<dd>the converted value.</dd>
</dl>
</div>
:::


</section>

:::::
  

