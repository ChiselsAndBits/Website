--- 
title: IServerConfiguration
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.config](index.md)  
# Interface IServerConfiguration  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IServerConfiguration</span></div>  

  

Gives access to the current server's configuration. Elements in this configuration are relevant for both the server and client side of C&amp;B. Since this options
 influence gameplay mechanics they need to be kept in sync.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBagStackSize()" class="member-name-link">getBagStackSize</a>()</code></td><td><div class="block">The size of the bit stack in a bit bag.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../multistate/StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>&gt;</code></td><td><code><a href="#getBitSize()" class="member-name-link">getBitSize</a>()</code></td><td><div class="block">The size of a bit in the world.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getBlackListRandomTickingBlocks()" class="member-name-link">getBlackListRandomTickingBlocks</a>()</code></td><td><div class="block">Determines if random ticking blocks like grass or others should be eligible for chiselability.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getChangeTrackerSize()" class="member-name-link">getChangeTrackerSize</a>()</code></td><td><div class="block">Ths size of the change tracker, aka how much the user can undo.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getCompatabilityMode()" class="member-name-link">getCompatabilityMode</a>()</code></td><td><div class="block">Determines if the eligibility compatibility mode is active or not.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getDeleteExcessBits()" class="member-name-link">getDeleteExcessBits</a>()</code></td><td><div class="block">Indicates if Chisels and Bits will delete excess bits when a block is broken.</div><br></td></tr>
  <tr><td><code>static <a href="IServerConfiguration.html" title="interface in mod.chiselsandbits.api.config">IServerConfiguration</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current server's configuration.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang" class="external-link">Double</a>&gt;</code></td><td><code><a href="#getLightFactorMultiplier()" class="member-name-link">getLightFactorMultiplier</a>()</code></td><td><div class="block">Provides access to the factor with which the bit light strength is multiplied.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getRequireChiselInOffHandForBitBreaking()" class="member-name-link">getRequireChiselInOffHandForBitBreaking</a>()</code></td><td><div class="block">Indicates if the player should be required to have a chisel in their offhand to break bits with a bit block.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IServerConfiguration.html" title="interface in mod.chiselsandbits.api.config">IServerConfiguration</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current server's configuration.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBagStackSize()" class="member-name-link">getBagStackSize</a>()</code></td><td><div class="block">The size of the bit stack in a bit bag.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../multistate/StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>&gt;</code></td><td><code><a href="#getBitSize()" class="member-name-link">getBitSize</a>()</code></td><td><div class="block">The size of a bit in the world.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getBlackListRandomTickingBlocks()" class="member-name-link">getBlackListRandomTickingBlocks</a>()</code></td><td><div class="block">Determines if random ticking blocks like grass or others should be eligible for chiselability.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getChangeTrackerSize()" class="member-name-link">getChangeTrackerSize</a>()</code></td><td><div class="block">Ths size of the change tracker, aka how much the user can undo.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getCompatabilityMode()" class="member-name-link">getCompatabilityMode</a>()</code></td><td><div class="block">Determines if the eligibility compatibility mode is active or not.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getDeleteExcessBits()" class="member-name-link">getDeleteExcessBits</a>()</code></td><td><div class="block">Indicates if Chisels and Bits will delete excess bits when a block is broken.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang" class="external-link">Double</a>&gt;</code></td><td><code><a href="#getLightFactorMultiplier()" class="member-name-link">getLightFactorMultiplier</a>()</code></td><td><div class="block">Provides access to the factor with which the bit light strength is multiplied.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getRequireChiselInOffHandForBitBreaking()" class="member-name-link">getRequireChiselInOffHandForBitBreaking</a>()</code></td><td><div class="block">Indicates if the player should be required to have a chisel in their offhand to break bits with a bit block.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBagStackSize()" class="member-name-link">getBagStackSize</a>()</code></td><td><div class="block">The size of the bit stack in a bit bag.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="../multistate/StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>&gt;</code></td><td><code><a href="#getBitSize()" class="member-name-link">getBitSize</a>()</code></td><td><div class="block">The size of a bit in the world.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getBlackListRandomTickingBlocks()" class="member-name-link">getBlackListRandomTickingBlocks</a>()</code></td><td><div class="block">Determines if random ticking blocks like grass or others should be eligible for chiselability.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getChangeTrackerSize()" class="member-name-link">getChangeTrackerSize</a>()</code></td><td><div class="block">Ths size of the change tracker, aka how much the user can undo.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getCompatabilityMode()" class="member-name-link">getCompatabilityMode</a>()</code></td><td><div class="block">Determines if the eligibility compatibility mode is active or not.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getDeleteExcessBits()" class="member-name-link">getDeleteExcessBits</a>()</code></td><td><div class="block">Indicates if Chisels and Bits will delete excess bits when a block is broken.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang" class="external-link">Double</a>&gt;</code></td><td><code><a href="#getLightFactorMultiplier()" class="member-name-link">getLightFactorMultiplier</a>()</code></td><td><div class="block">Provides access to the factor with which the bit light strength is multiplied.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getRequireChiselInOffHandForBitBreaking()" class="member-name-link">getRequireChiselInOffHandForBitBreaking</a>()</code></td><td><div class="block">Indicates if the player should be required to have a chisel in their offhand to break bits with a bit block.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IServerConfiguration.html" title="interface in mod.chiselsandbits.api.config">IServerConfiguration</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
Gives access to the current server's configuration. Elements in this configuration are relevant for both the server and client side of C&amp;B. Since this options
 influence gameplay mechanics they need to be kept in sync.
<dl class="notes">
<dt>Returns:</dt>
<dd>The server configuration.</dd>
</dl>
:::


</section>

<section id="getBlackListRandomTickingBlocks()">

:::tabs
== getBlackListRandomTickingBlocks
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getBlackListRandomTickingBlocks</span>()</div>
Determines if random ticking blocks like grass or others should be eligible for chiselability.
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines if random ticking blocks should be chiselable.</dd>
</dl>
:::


</section>

<section id="getCompatabilityMode()">

:::tabs
== getCompatabilityMode
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getCompatabilityMode</span>()</div>
Determines if the eligibility compatibility mode is active or not.
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines if the compatibility mode is active or not.</dd>
</dl>
:::


</section>

<section id="getBagStackSize()">

:::tabs
== getBagStackSize
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getBagStackSize</span>()</div>
The size of the bit stack in a bit bag.
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines the size of the bit stack.</dd>
</dl>
:::


</section>

<section id="getBitSize()">

:::tabs
== getBitSize
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="../multistate/StateEntrySize.html" title="enum class in mod.chiselsandbits.api.multistate">StateEntrySize</a>&gt;</span>&nbsp;<span class="element-name">getBitSize</span>()</div>
The size of a bit in the world.
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines the size of a bit in the world.</dd>
</dl>
:::


</section>

<section id="getChangeTrackerSize()">

:::tabs
== getChangeTrackerSize
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getChangeTrackerSize</span>()</div>
Ths size of the change tracker, aka how much the user can undo.
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines the size of the change tracker.</dd>
</dl>
:::


</section>

<section id="getDeleteExcessBits()">

:::tabs
== getDeleteExcessBits
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getDeleteExcessBits</span>()</div>
Indicates if Chisels and Bits will delete excess bits when a block is broken.
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines if excess bits should be deleted.#</dd>
</dl>
:::


</section>

<section id="getLightFactorMultiplier()">

:::tabs
== getLightFactorMultiplier
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang" class="external-link">Double</a>&gt;</span>&nbsp;<span class="element-name">getLightFactorMultiplier</span>()</div>
Provides access to the factor with which the bit light strength is multiplied.
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines the factor with which the bit light strength is multiplied.</dd>
</dl>
:::


</section>

<section id="getRequireChiselInOffHandForBitBreaking()">

:::tabs
== getRequireChiselInOffHandForBitBreaking
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getRequireChiselInOffHandForBitBreaking</span>()</div>
Indicates if the player should be required to have a chisel in their offhand to break bits with a bit block.
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines if the player should be required to have a chisel in their offhand to break bits.</dd>
</dl>
:::


</section>

:::::
  

