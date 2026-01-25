--- 
title: CollisionType
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.axissize](index.md)  
# Enum CollisionType  
---
<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">CollisionType</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>&lt;<a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&gt;</span></div>  

  

  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 2 -->
::::::: info Nested Class Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Nested classes/interfaces inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">Enum.EnumDesc</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">E</a> extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang" class="external-link">E</a>&gt;&gt;
:::::
:::::::
  
  
<!-- JavaMarkContainer Depth: 1 -->
::::: info Enum Constant Summary  
:::tabs
== Enum Constants
<table>
  <thead>
    <tr><th>Enum Constant</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#ALL" class="member-name-link">ALL</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="#COLLIDEABLE_ONLY" class="member-name-link">COLLIDEABLE_ONLY</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="#NONE_AIR" class="member-name-link">NONE_AIR</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- =========== FIELD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Summary  
:::tabs
== Fields
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final com.mojang.serialization.Codec<wbr>&lt;<a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&gt;</code></td><td><code><a href="#CODEC" class="member-name-link">CODEC</a></code></td><td>&nbsp;</td></tr>
  <tr><td><code>static final net.minecraft.network.codec.StreamCodec<wbr>&lt;io.netty.buffer.ByteBuf,<wbr><a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&gt;</code></td><td><code><a href="#STREAM_CODEC" class="member-name-link">STREAM_CODEC</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canBeEmptyWithJustFluids()" class="member-name-link">canBeEmptyWithJustFluids</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#getExampleState()" class="member-name-link">getExampleState</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidFor(mod.chiselsandbits.api.multistate.accessor.IStateEntryInfo)" class="member-name-link">isValidFor</a><wbr>(<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&nbsp;info)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidFor(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">isValidFor</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canBeEmptyWithJustFluids()" class="member-name-link">canBeEmptyWithJustFluids</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#getExampleState()" class="member-name-link">getExampleState</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidFor(mod.chiselsandbits.api.multistate.accessor.IStateEntryInfo)" class="member-name-link">isValidFor</a><wbr>(<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&nbsp;info)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidFor(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">isValidFor</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canBeEmptyWithJustFluids()" class="member-name-link">canBeEmptyWithJustFluids</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#getExampleState()" class="member-name-link">getExampleState</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidFor(mod.chiselsandbits.api.multistate.accessor.IStateEntryInfo)" class="member-name-link">isValidFor</a><wbr>(<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&nbsp;info)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidFor(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">isValidFor</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a></code></td><td><code><a href="#valueOf(java.lang.String)" class="member-name-link">valueOf</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</code></td><td><div class="block">Returns the enum constant of this class with the specified name.</div><br></td></tr>
  <tr><td><code>static <a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>[]</code></td><td><code><a href="#values()" class="member-name-link">values</a>()</code></td><td><div class="block">Returns an array containing the constants of this enum class, in<br>the order they are declared.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang" class="external-link">Enum</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang" class="external-link">compareTo</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang" class="external-link">describeConstable</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang" class="external-link">getDeclaringClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang" class="external-link">name</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang" class="external-link">ordinal</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang" class="external-link">valueOf</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Enum Constant Details  
<section id="NONE_AIR">

:::tabs
== NONE_AIR
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a></span>&nbsp;<span class="element-name">NONE_AIR</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="COLLIDEABLE_ONLY">

:::tabs
== COLLIDEABLE_ONLY
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a></span>&nbsp;<span class="element-name">COLLIDEABLE_ONLY</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="ALL">

:::tabs
== ALL
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a></span>&nbsp;<span class="element-name">ALL</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="CODEC">

:::tabs
== CODEC
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;<a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&gt;</span>&nbsp;<span class="element-name">CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="STREAM_CODEC">

:::tabs
== STREAM_CODEC
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.network.codec.StreamCodec&lt;io.netty.buffer.ByteBuf,<wbr><a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&gt;</span>&nbsp;<span class="element-name">STREAM_CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="values()">

:::tabs
== values
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>[]</span>&nbsp;<span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
:::


</section>

<section id="valueOf(java.lang.String)">

:::tabs
== valueOf
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a></span>&nbsp;<span class="element-name">valueOf</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang" class="external-link">NullPointerException</a></code> - if the argument is null</dd>
</dl>
:::


</section>

<section id="isValidFor(mod.chiselsandbits.api.multistate.accessor.IStateEntryInfo)">

:::tabs
== isValidFor
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isValidFor</span><wbr><span class="parameters">(<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&nbsp;info)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="isValidFor(net.minecraft.world.level.block.state.BlockState)">

:::tabs
== isValidFor
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isValidFor</span><wbr><span class="parameters">(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="canBeEmptyWithJustFluids()">

:::tabs
== canBeEmptyWithJustFluids
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">canBeEmptyWithJustFluids</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getExampleState()">

:::tabs
== getExampleState
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.world.level.block.state.BlockState</span>&nbsp;<span class="element-name">getExampleState</span>()</div>
<dl class="notes"></dl>
:::


</section>

:::::
  

