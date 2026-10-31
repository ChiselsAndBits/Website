--- 
title: BlockStatePredicates
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Class BlockStatePredicates  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.BlockStatePredicates  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">BlockStatePredicates</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Common <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link"><code>Predicate</code></a> instances for filtering <code>BlockState</code> values.  

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
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a><wbr>&lt;net.minecraft.world.level.block.state.BlockState&gt;</code></td><td><code><a href="#ALL" class="member-name-link">ALL</a></code></td><td><div class="block">A predicate that always matches, regardless of the evaluated <code>BlockState</code>.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a><wbr>&lt;net.minecraft.world.level.block.state.BlockState&gt;</code></td><td><code><a href="#COLLIDEABLE_ONLY" class="member-name-link">COLLIDEABLE_ONLY</a></code></td><td><div class="block">A predicate matching only states that occupy space — non-air with an empty fluid state (excluding air and liquids/gases).</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a><wbr>&lt;net.minecraft.world.level.block.state.BlockState&gt;</code></td><td><code><a href="#NOT_AIR" class="member-name-link">NOT_AIR</a></code></td><td><div class="block">A predicate matching any non-air <code>BlockState</code>.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="NOT_AIR">

:::tabs
== NOT_AIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;net.minecraft.world.level.block.state.BlockState&gt;</span>&nbsp;<span class="element-name">NOT_AIR</span></div>
A predicate matching any non-air <code>BlockState</code>.
</div>
:::


</section>

<section id="ALL">

:::tabs
== ALL
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;net.minecraft.world.level.block.state.BlockState&gt;</span>&nbsp;<span class="element-name">ALL</span></div>
A predicate that always matches, regardless of the evaluated <code>BlockState</code>.
</div>
:::


</section>

<section id="COLLIDEABLE_ONLY">

:::tabs
== COLLIDEABLE_ONLY
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;net.minecraft.world.level.block.state.BlockState&gt;</span>&nbsp;<span class="element-name">COLLIDEABLE_ONLY</span></div>
A predicate matching only states that occupy space — non-air with an empty fluid state (excluding air and liquids/gases).
Okey,
</div>
:::


</section>

:::::
  

  

  

  

