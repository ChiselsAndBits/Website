--- 
title: IConversionManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling.conversion](index.md)  
# Interface IConversionManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IConversionManager</span></div>  

  

Manages converting none chiseled objects into chiseled variants and back.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.block.Block)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.block.Block&nbsp;block)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given block.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given blockstate.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.ItemLike)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.ItemLike&nbsp;provider)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given item.</div><br></td></tr>
  <tr><td><code>static <a href="IConversionManager.html" title="interface in mod.chiselsandbits.api.chiseling.conversion">IConversionManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The instance of the manager.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IConversionManager.html" title="interface in mod.chiselsandbits.api.chiseling.conversion">IConversionManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The instance of the manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.block.Block)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.block.Block&nbsp;block)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given block.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given blockstate.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.ItemLike)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.ItemLike&nbsp;provider)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given item.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.block.Block)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.block.Block&nbsp;block)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given block.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given blockstate.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.level.block.Block&gt;</code></td><td><code><a href="#getChiseledVariantOf(net.minecraft.world.level.ItemLike)" class="member-name-link">getChiseledVariantOf</a><wbr>(net.minecraft.world.level.ItemLike&nbsp;provider)</code></td><td><div class="block">Allows you to get the chiseled block variant of a given item.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IConversionManager.html" title="interface in mod.chiselsandbits.api.chiseling.conversion">IConversionManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
The instance of the manager.
<dl class="notes">
<dt>Returns:</dt>
<dd>The manager.</dd>
</dl>
:::


</section>

<section id="getChiseledVariantOf(net.minecraft.world.level.block.state.BlockState)">

:::tabs
== getChiseledVariantOf
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.level.block.Block&gt;</span>&nbsp;<span class="element-name">getChiseledVariantOf</span><wbr><span class="parameters">(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</span></div>
Allows you to get the chiseled block variant of a given blockstate.
 In general this is material dependent.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockState</code> - The blockstate to convert.</dd>
<dt>Returns:</dt>
<dd>An optional, containing the converted block, if the given blockstate is convertible.</dd>
</dl>
:::


</section>

<section id="getChiseledVariantOf(net.minecraft.world.level.block.Block)">

:::tabs
== getChiseledVariantOf
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.level.block.Block&gt;</span>&nbsp;<span class="element-name">getChiseledVariantOf</span><wbr><span class="parameters">(net.minecraft.world.level.block.Block&nbsp;block)</span></div>
Allows you to get the chiseled block variant of a given block.
 In general this is material dependent.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>block</code> - The block to convert.</dd>
<dt>Returns:</dt>
<dd>An optional, containing the converted block, if the given block is convertible.</dd>
</dl>
:::


</section>

<section id="getChiseledVariantOf(net.minecraft.world.level.ItemLike)">

:::tabs
== getChiseledVariantOf
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.level.block.Block&gt;</span>&nbsp;<span class="element-name">getChiseledVariantOf</span><wbr><span class="parameters">(net.minecraft.world.level.ItemLike&nbsp;provider)</span></div>
Allows you to get the chiseled block variant of a given item.
 In general this is material dependent.
 If an item is passed in which is not a <code>BlockItem</code> then an empty optional is returned.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The item provider to convert.</dd>
<dt>Returns:</dt>
<dd>An optional, containing the converted block, if the given item in the provider represents a convertible block.</dd>
</dl>
:::


</section>

:::::
  

