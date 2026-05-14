--- 
title: StateEntrySize
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate](index.md)  
# Enum Class StateEntrySize  
---
<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">StateEntrySize</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>&lt;<a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>&gt;</span></div>  

  

The size of state entries in the current instance.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
Nested classes/interfaces inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">Enum.EnumDesc</a>&lt;E&gt;
:::::
  
  
<!-- JavaMarkContainer Depth: 1 -->
::::: info Enum Constant Summary  
:::tabs
== Enum Constants
<table class="stretched-table">
  <thead>
    <tr><th>Enum Constant</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#ONE" class="member-name-link">ONE</a></code></td><td><div class="block">1 Bit per block side.</div><br></td></tr>
  <tr><td><code><a href="#ONE_EIGHT" class="member-name-link">ONE_EIGHT</a></code></td><td><div class="block">8 Bits per block.</div><br></td></tr>
  <tr><td><code><a href="#ONE_HALF" class="member-name-link">ONE_HALF</a></code></td><td><div class="block">2 Bits per block.</div><br></td></tr>
  <tr><td><code><a href="#ONE_QUARTER" class="member-name-link">ONE_QUARTER</a></code></td><td><div class="block">4 Bits per block.</div><br></td></tr>
  <tr><td><code><a href="#ONE_SIXTEENTH" class="member-name-link">ONE_SIXTEENTH</a></code></td><td><div class="block">16 Bits per block.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#current()" class="member-name-link">current</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getArrayIndexForPosition(int,int,int)" class="member-name-link">getArrayIndexForPosition</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z)</code></td><td><div class="block">The array index for a given position when the current state entry size is used.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getArrayIndexForPosition(net.minecraft.core.Vec3i)" class="member-name-link">getArrayIndexForPosition</a><wbr>(net.minecraft.core.Vec3i&nbsp;coordinate)</code></td><td><div class="block">The array index for a given position when the current state entry size is used.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerBlock()" class="member-name-link">getBitsPerBlock</a>()</code></td><td><div class="block">The total amount of bits per block.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerBlockSide()" class="member-name-link">getBitsPerBlockSide</a>()</code></td><td><div class="block">The amount of bits in a single layer per side of the block.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getBitsPerBlockSideScalingVector()" class="member-name-link">getBitsPerBlockSideScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale up another vector with the amount of bits on a given side.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerLayer()" class="member-name-link">getBitsPerLayer</a>()</code></td><td><div class="block">The total amount of bits per layer.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getDamageFactor()" class="member-name-link">getDamageFactor</a>()</code></td><td><div class="block">Calculates how much damage should be applied to tools for the harvest of a given bit within this size.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSizePerBit()" class="member-name-link">getSizePerBit</a>()</code></td><td><div class="block">The size of a single bit if a block is a single unit of length.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSizePerBitScalingVector()" class="member-name-link">getSizePerBitScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale down another vector with the size of a single bit.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSizePerHalfBit()" class="member-name-link">getSizePerHalfBit</a>()</code></td><td><div class="block">The size of half a bit if a block is a single unit of length.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSizePerHalfBitScalingVector()" class="member-name-link">getSizePerHalfBitScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale down another vector with the size of half a bit.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#roundDownToNearest(net.minecraft.world.phys.Vec3)" class="member-name-link">roundDownToNearest</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;pos)</code></td><td><div class="block">Takes in a 3D vector and rounds its components down to the nearest multiple of the size of a single bit.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#upperLevelY()" class="member-name-link">upperLevelY</a>()</code></td><td><div class="block">The y coordinate of the upper of the block.</div><br></td></tr>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#current()" class="member-name-link">current</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#getArrayIndexForPosition(int,int,int)" class="member-name-link">getArrayIndexForPosition</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z)</code></td><td><div class="block">The array index for a given position when the current state entry size is used.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getArrayIndexForPosition(net.minecraft.core.Vec3i)" class="member-name-link">getArrayIndexForPosition</a><wbr>(net.minecraft.core.Vec3i&nbsp;coordinate)</code></td><td><div class="block">The array index for a given position when the current state entry size is used.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerBlock()" class="member-name-link">getBitsPerBlock</a>()</code></td><td><div class="block">The total amount of bits per block.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerBlockSide()" class="member-name-link">getBitsPerBlockSide</a>()</code></td><td><div class="block">The amount of bits in a single layer per side of the block.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getBitsPerBlockSideScalingVector()" class="member-name-link">getBitsPerBlockSideScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale up another vector with the amount of bits on a given side.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerLayer()" class="member-name-link">getBitsPerLayer</a>()</code></td><td><div class="block">The total amount of bits per layer.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getDamageFactor()" class="member-name-link">getDamageFactor</a>()</code></td><td><div class="block">Calculates how much damage should be applied to tools for the harvest of a given bit within this size.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSizePerBit()" class="member-name-link">getSizePerBit</a>()</code></td><td><div class="block">The size of a single bit if a block is a single unit of length.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSizePerBitScalingVector()" class="member-name-link">getSizePerBitScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale down another vector with the size of a single bit.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSizePerHalfBit()" class="member-name-link">getSizePerHalfBit</a>()</code></td><td><div class="block">The size of half a bit if a block is a single unit of length.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSizePerHalfBitScalingVector()" class="member-name-link">getSizePerHalfBitScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale down another vector with the size of half a bit.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#roundDownToNearest(net.minecraft.world.phys.Vec3)" class="member-name-link">roundDownToNearest</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;pos)</code></td><td><div class="block">Takes in a 3D vector and rounds its components down to the nearest multiple of the size of a single bit.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#upperLevelY()" class="member-name-link">upperLevelY</a>()</code></td><td><div class="block">The y coordinate of the upper of the block.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#current()" class="member-name-link">current</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getArrayIndexForPosition(int,int,int)" class="member-name-link">getArrayIndexForPosition</a><wbr>(int&nbsp;x,<br> int&nbsp;y,<br> int&nbsp;z)</code></td><td><div class="block">The array index for a given position when the current state entry size is used.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getArrayIndexForPosition(net.minecraft.core.Vec3i)" class="member-name-link">getArrayIndexForPosition</a><wbr>(net.minecraft.core.Vec3i&nbsp;coordinate)</code></td><td><div class="block">The array index for a given position when the current state entry size is used.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerBlock()" class="member-name-link">getBitsPerBlock</a>()</code></td><td><div class="block">The total amount of bits per block.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerBlockSide()" class="member-name-link">getBitsPerBlockSide</a>()</code></td><td><div class="block">The amount of bits in a single layer per side of the block.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getBitsPerBlockSideScalingVector()" class="member-name-link">getBitsPerBlockSideScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale up another vector with the amount of bits on a given side.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getBitsPerLayer()" class="member-name-link">getBitsPerLayer</a>()</code></td><td><div class="block">The total amount of bits per layer.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getDamageFactor()" class="member-name-link">getDamageFactor</a>()</code></td><td><div class="block">Calculates how much damage should be applied to tools for the harvest of a given bit within this size.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSizePerBit()" class="member-name-link">getSizePerBit</a>()</code></td><td><div class="block">The size of a single bit if a block is a single unit of length.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSizePerBitScalingVector()" class="member-name-link">getSizePerBitScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale down another vector with the size of a single bit.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSizePerHalfBit()" class="member-name-link">getSizePerHalfBit</a>()</code></td><td><div class="block">The size of half a bit if a block is a single unit of length.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#getSizePerHalfBitScalingVector()" class="member-name-link">getSizePerHalfBitScalingVector</a>()</code></td><td><div class="block">Returns the vector used to scale down another vector with the size of half a bit.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.Vec3</code></td><td><code><a href="#roundDownToNearest(net.minecraft.world.phys.Vec3)" class="member-name-link">roundDownToNearest</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;pos)</code></td><td><div class="block">Takes in a 3D vector and rounds its components down to the nearest multiple of the size of a single bit.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#upperLevelY()" class="member-name-link">upperLevelY</a>()</code></td><td><div class="block">The y coordinate of the upper of the block.</div><br></td></tr>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang" class="external-link">compareTo</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang" class="external-link">describeConstable</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang" class="external-link">getDeclaringClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang" class="external-link">name</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang" class="external-link">ordinal</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang" class="external-link">valueOf</a>Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
  
  
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Enum Constant Details  
<section id="ONE_SIXTEENTH">

:::tabs
== ONE_SIXTEENTH
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></span>&nbsp;<span class="element-name">ONE_SIXTEENTH</span></div>
16 Bits per block.</div>
:::


</section>

<section id="ONE_EIGHT">

:::tabs
== ONE_EIGHT
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></span>&nbsp;<span class="element-name">ONE_EIGHT</span></div>
8 Bits per block.</div>
:::


</section>

<section id="ONE_QUARTER">

:::tabs
== ONE_QUARTER
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></span>&nbsp;<span class="element-name">ONE_QUARTER</span></div>
4 Bits per block.</div>
:::


</section>

<section id="ONE_HALF">

:::tabs
== ONE_HALF
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></span>&nbsp;<span class="element-name">ONE_HALF</span></div>
2 Bits per block.</div>
:::


</section>

<section id="ONE">

:::tabs
== ONE
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></span>&nbsp;<span class="element-name">ONE</span></div>
1 Bit per block side.
Generally only used for testing.</div>
:::


</section>

:::::
  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="values()">
:::tabs
== values
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>[]</span>&nbsp;<span class="element-name">values</span>()</div>
Returns an array containing the constants of this enum class, in
the order they are declared.
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</div>
:::
</section>
<section id="valueOf(java.lang.String)">
:::tabs
== valueOf
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></span>&nbsp;<span class="element-name">valueOf</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</span></div>
Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang" class="external-link">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</div>
:::
</section>
<section id="current()">
:::tabs
== current
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a></span>&nbsp;<span class="element-name">current</span>()</div>
</div>
:::
</section>
<section id="getBitsPerBlockSide()">
:::tabs
== getBitsPerBlockSide
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getBitsPerBlockSide</span>()</div>
The amount of bits in a single layer per side of the block.
<dl class="notes">
<dt>Returns:</dt>
<dd>The amount of bits in a layer on a single side of the block.</dd>
</dl>
</div>
:::
</section>
<section id="getBitsPerBlock()">
:::tabs
== getBitsPerBlock
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getBitsPerBlock</span>()</div>
The total amount of bits per block.
This is <a href="#getBitsPerBlockSide()"><code>getBitsPerBlockSide()</code></a> ^ 3.
<dl class="notes">
<dt>Returns:</dt>
<dd>The total amount of bits in a block.</dd>
</dl>
</div>
:::
</section>
<section id="getBitsPerLayer()">
:::tabs
== getBitsPerLayer
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getBitsPerLayer</span>()</div>
The total amount of bits per layer.
This is <a href="#getBitsPerBlockSide()"><code>getBitsPerBlockSide()</code></a> ^ 2.
<dl class="notes">
<dt>Returns:</dt>
<dd>The total amount of bits in a layer.</dd>
</dl>
</div>
:::
</section>
<section id="getSizePerBit()">
:::tabs
== getSizePerBit
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">float</span>&nbsp;<span class="element-name">getSizePerBit</span>()</div>
The size of a single bit if a block is a single unit of length.
Is always 1 / <a href="#getBitsPerBlockSide()"><code>getBitsPerBlockSide()</code></a>.
<dl class="notes">
<dt>Returns:</dt>
<dd>The size of a bit.</dd>
</dl>
</div>
:::
</section>
<section id="getSizePerBitScalingVector()">
:::tabs
== getSizePerBitScalingVector
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getSizePerBitScalingVector</span>()</div>
Returns the vector used to scale down another vector with the size of a single bit.
Useful for passing to <code>Vec3.multiply(Vec3)</code>
<dl class="notes">
<dt>Returns:</dt>
<dd>The scaling vector.</dd>
</dl>
</div>
:::
</section>
<section id="getSizePerHalfBitScalingVector()">
:::tabs
== getSizePerHalfBitScalingVector
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getSizePerHalfBitScalingVector</span>()</div>
Returns the vector used to scale down another vector with the size of half a bit.
Useful for passing to <code>Vec3.multiply(Vec3)</code>
<dl class="notes">
<dt>Returns:</dt>
<dd>The scaling vector.</dd>
</dl>
</div>
:::
</section>
<section id="getBitsPerBlockSideScalingVector()">
:::tabs
== getBitsPerBlockSideScalingVector
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">getBitsPerBlockSideScalingVector</span>()</div>
Returns the vector used to scale up another vector with the amount of bits on a given side.
Useful for passing to <code>Vec3.multiply(Vec3)</code>
<dl class="notes">
<dt>Returns:</dt>
<dd>The scaling vector.</dd>
</dl>
</div>
:::
</section>
<section id="getSizePerHalfBit()">
:::tabs
== getSizePerHalfBit
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">float</span>&nbsp;<span class="element-name">getSizePerHalfBit</span>()</div>
The size of half a bit if a block is a single unit of length.
Is always <a href="#getSizePerBit()"><code>getSizePerBit()</code></a> / 2.
<dl class="notes">
<dt>Returns:</dt>
<dd>The size of half a single bit.</dd>
</dl>
</div>
:::
</section>
<section id="upperLevelY()">
:::tabs
== upperLevelY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">float</span>&nbsp;<span class="element-name">upperLevelY</span>()</div>
The y coordinate of the upper of the block.
<dl class="notes">
<dt>Returns:</dt>
<dd>The y coordinate.</dd>
</dl>
</div>
:::
</section>
<section id="getArrayIndexForPosition(net.minecraft.core.Vec3i)">
:::tabs
== getArrayIndexForPosition
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getArrayIndexForPosition</span><wbr><span class="parameters">(net.minecraft.core.Vec3i&nbsp;coordinate)</span></div>
The array index for a given position when the current state entry size is used.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinate</code> - The coordinate to get the array index for.</dd>
<dt>Returns:</dt>
<dd>The array index.</dd>
</dl>
</div>
:::
</section>
<section id="getArrayIndexForPosition(int,int,int)">
:::tabs
== getArrayIndexForPosition
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getArrayIndexForPosition</span><wbr><span class="parameters">(int&nbsp;x,
 int&nbsp;y,
 int&nbsp;z)</span></div>
The array index for a given position when the current state entry size is used.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - The x coordinate.</dd>
<dd><code>y</code> - The y coordinate.</dd>
<dd><code>z</code> - The z coordinate.</dd>
<dt>Returns:</dt>
<dd>The array index.</dd>
</dl>
</div>
:::
</section>
<section id="roundDownToNearest(net.minecraft.world.phys.Vec3)">
:::tabs
== roundDownToNearest
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.world.phys.Vec3</span>&nbsp;<span class="element-name">roundDownToNearest</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;pos)</span></div>
Takes in a 3D vector and rounds its components down to the nearest multiple of the size of a single bit.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pos</code> - The position to round down.</dd>
<dt>Returns:</dt>
<dd>The rounded down position.</dd>
</dl>
</div>
:::
</section>
<section id="getDamageFactor()">
:::tabs
== getDamageFactor
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">getDamageFactor</span>()</div>
Calculates how much damage should be applied to tools for the harvest of a given bit within this size.
<p>
    The scale factor is 1 for 1/16, and grows with the cubicly per level, with the amount of 1/16 bits that the size represents.
    So for 1/8, it is 8 (as 2x2x2 1/16th bits fit in one 1/8 bit)
    For 1/4, it is 64 (as 4x4x4 1/16th bits fit in one 1/4 bit)
    etc.
</p>
<dl class="notes">
<dt>Returns:</dt>
<dd>The damage scale factor per one bit harvested.</dd>
</dl>
</div>
:::
</section>
:::::
  

