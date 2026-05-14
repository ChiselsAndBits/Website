--- 
title: IMultiStateObjectStatistics
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.statistics](index.md)  
# Interface IMultiStateObjectStatistics  
**All Extended Interfaces:**  
[IStatistics](../../item/multistate/IStatistics.md), [RawSerializable](../../serialization/RawSerializable.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultiStateObjectStatistics</span><span class="extends-implements"><br/>  
extends <a href="../../item/multistate/IStatistics.html" title="interface in mod.chiselsandbits.api.item.multistate">IStatistics</a></span></div>  

  

The statistics of a multistate block.  

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
  <tr><td><code>boolean</code></td><td><code><a href="#canPropagateSkylight()" class="member-name-link">canPropagateSkylight</a>()</code></td><td><div class="block">Indicates if the current multistate block can propagate skylight.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canSustainGrassBelow()" class="member-name-link">canSustainGrassBelow</a>()</code></td><td><div class="block">Indicates if the current multistate block can sustain grass below.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns all states (without count) that are contained in the object</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getFullnessFactor()" class="member-name-link">getFullnessFactor</a>()</code></td><td><div class="block">Gives access to the fullness factor of the current block.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getLightBlockingFactor()" class="member-name-link">getLightBlockingFactor</a>()</code></td><td><div class="block">The factor with which the bits block light.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getLightEmissionFactor()" class="member-name-link">getLightEmissionFactor</a>()</code></td><td><div class="block">The factor of how much light is emitted by the block.</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState()" class="member-name-link">getPrimaryState</a>()</code></td><td><div class="block">The primary blockstate.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getRelativeBlockHardness(net.minecraft.world.entity.player.Player)" class="member-name-link">getRelativeBlockHardness</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Indicates the relative block hardness for a given player.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSlipperiness()" class="member-name-link">getSlipperiness</a>()</code></td><td><div class="block">Indicates the slipperiness of the current block.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getStateCounts()" class="member-name-link">getStateCounts</a>()</code></td><td><div class="block">An immutable copy of the map that contains the counts of all blockstates in the multistate block.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isEmptyBlock()" class="member-name-link">isEmptyBlock</a>()</code></td><td><div class="block">Indicates if the current multistate block is empty.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isFullBlock()" class="member-name-link">isFullBlock</a>()</code></td><td><div class="block">Indicates if the current block is full.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldCheckWeakPower()" class="member-name-link">shouldCheckWeakPower</a>()</code></td><td><div class="block">Indicates if the block that this statistics belongs to should check for weak power.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canPropagateSkylight()" class="member-name-link">canPropagateSkylight</a>()</code></td><td><div class="block">Indicates if the current multistate block can propagate skylight.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canSustainGrassBelow()" class="member-name-link">canSustainGrassBelow</a>()</code></td><td><div class="block">Indicates if the current multistate block can sustain grass below.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns all states (without count) that are contained in the object</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getFullnessFactor()" class="member-name-link">getFullnessFactor</a>()</code></td><td><div class="block">Gives access to the fullness factor of the current block.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getLightBlockingFactor()" class="member-name-link">getLightBlockingFactor</a>()</code></td><td><div class="block">The factor with which the bits block light.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getLightEmissionFactor()" class="member-name-link">getLightEmissionFactor</a>()</code></td><td><div class="block">The factor of how much light is emitted by the block.</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState()" class="member-name-link">getPrimaryState</a>()</code></td><td><div class="block">The primary blockstate.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getRelativeBlockHardness(net.minecraft.world.entity.player.Player)" class="member-name-link">getRelativeBlockHardness</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Indicates the relative block hardness for a given player.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSlipperiness()" class="member-name-link">getSlipperiness</a>()</code></td><td><div class="block">Indicates the slipperiness of the current block.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getStateCounts()" class="member-name-link">getStateCounts</a>()</code></td><td><div class="block">An immutable copy of the map that contains the counts of all blockstates in the multistate block.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isEmptyBlock()" class="member-name-link">isEmptyBlock</a>()</code></td><td><div class="block">Indicates if the current multistate block is empty.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isFullBlock()" class="member-name-link">isFullBlock</a>()</code></td><td><div class="block">Indicates if the current block is full.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldCheckWeakPower()" class="member-name-link">shouldCheckWeakPower</a>()</code></td><td><div class="block">Indicates if the block that this statistics belongs to should check for weak power.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canPropagateSkylight()" class="member-name-link">canPropagateSkylight</a>()</code></td><td><div class="block">Indicates if the current multistate block can propagate skylight.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canSustainGrassBelow()" class="member-name-link">canSustainGrassBelow</a>()</code></td><td><div class="block">Indicates if the current multistate block can sustain grass below.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getFullnessFactor()" class="member-name-link">getFullnessFactor</a>()</code></td><td><div class="block">Gives access to the fullness factor of the current block.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getLightBlockingFactor()" class="member-name-link">getLightBlockingFactor</a>()</code></td><td><div class="block">The factor with which the bits block light.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getLightEmissionFactor()" class="member-name-link">getLightEmissionFactor</a>()</code></td><td><div class="block">The factor of how much light is emitted by the block.</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState()" class="member-name-link">getPrimaryState</a>()</code></td><td><div class="block">The primary blockstate.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getRelativeBlockHardness(net.minecraft.world.entity.player.Player)" class="member-name-link">getRelativeBlockHardness</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Indicates the relative block hardness for a given player.</div><br></td></tr>
  <tr><td><code>float</code></td><td><code><a href="#getSlipperiness()" class="member-name-link">getSlipperiness</a>()</code></td><td><div class="block">Indicates the slipperiness of the current block.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getStateCounts()" class="member-name-link">getStateCounts</a>()</code></td><td><div class="block">An immutable copy of the map that contains the counts of all blockstates in the multistate block.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldCheckWeakPower()" class="member-name-link">shouldCheckWeakPower</a>()</code></td><td><div class="block">Indicates if the block that this statistics belongs to should check for weak power.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns all states (without count) that are contained in the object</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isEmptyBlock()" class="member-name-link">isEmptyBlock</a>()</code></td><td><div class="block">Indicates if the current multistate block is empty.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#isFullBlock()" class="member-name-link">isFullBlock</a>()</code></td><td><div class="block">Indicates if the current block is full.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;mod.chiselsandbits.api.item.multistate.<a href="../../item/multistate/IStatistics.html" title="interface in mod.chiselsandbits.api.item.multistate">IStatistics</a><a href="../../item/multistate/IStatistics.html#isEmpty()" title="isEmpty()">isEmpty</a>Methods inherited from interface&nbsp;mod.chiselsandbits.api.serialization.<a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a><a href="../../serialization/RawSerializable.html#codec()" title="codec()">codec</a>, <a href="../../serialization/RawSerializable.html#mapCodec()" title="mapCodec()">mapCodec</a>, <a href="../../serialization/RawSerializable.html#streamCodec()" title="streamCodec()">streamCodec</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getPrimaryState()">
:::tabs
== getPrimaryState
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getPrimaryState</span>()</div>
The primary blockstate.
If the multistate block is empty, then <code>Block.defaultBlockState()</code> is returned.
Generally speaking this is the blockstate that occurs the most often
in the multistate block.
But this is not guaranteed.
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../item/multistate/IStatistics.html#getPrimaryState()">getPrimaryState</a></code>&nbsp;in interface&nbsp;<code><a href="../../item/multistate/IStatistics.html" title="interface in mod.chiselsandbits.api.item.multistate">IStatistics</a></code></dd>
<dt>Returns:</dt>
<dd>The primary block state of the multi state block.</dd>
</dl>
</div>
:::
</section>
<section id="getStateCounts()">
:::tabs
== getStateCounts
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getStateCounts</span>()</div>
An immutable copy of the map that contains the counts of all blockstates in the multistate block.
<dl class="notes">
<dt>Returns:</dt>
<dd>The blockstate count map.</dd>
</dl>
</div>
:::
</section>
<section id="getContainedStates()">
:::tabs
== getContainedStates
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">getContainedStates</span>()</div>
Returns all states (without count) that are contained in the object
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../item/multistate/IStatistics.html#getContainedStates()">getContainedStates</a></code>&nbsp;in interface&nbsp;<code><a href="../../item/multistate/IStatistics.html" title="interface in mod.chiselsandbits.api.item.multistate">IStatistics</a></code></dd>
<dt>Returns:</dt>
<dd>All states in the object.</dd>
</dl>
</div>
:::
</section>
<section id="shouldCheckWeakPower()">
:::tabs
== shouldCheckWeakPower
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">shouldCheckWeakPower</span>()</div>
Indicates if the block that this statistics belongs to should check for weak power.
<dl class="notes">
<dt>Returns:</dt>
<dd>Indicates if this block should check for weak power.</dd>
</dl>
</div>
:::
</section>
<section id="getFullnessFactor()">
:::tabs
== getFullnessFactor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">float</span>&nbsp;<span class="element-name">getFullnessFactor</span>()</div>
Gives access to the fullness factor of the current block.
<dl class="notes">
<dt>Returns:</dt>
<dd>The fullness factor.</dd>
</dl>
</div>
:::
</section>
<section id="isFullBlock()">
:::tabs
== isFullBlock
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isFullBlock</span>()</div>
Indicates if the current block is full.
Generally coincides with <a href="#getFullnessFactor()"><code>getFullnessFactor()</code></a> being equal to <code>1f</code>.
<dl class="notes">
<dt>Returns:</dt>
<dd>Indicates if this block is full or not.</dd>
</dl>
</div>
:::
</section>
<section id="getSlipperiness()">
:::tabs
== getSlipperiness
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">float</span>&nbsp;<span class="element-name">getSlipperiness</span>()</div>
Indicates the slipperiness of the current block.
<dl class="notes">
<dt>Returns:</dt>
<dd>The slipperiness.</dd>
</dl>
</div>
:::
</section>
<section id="getLightEmissionFactor()">
:::tabs
== getLightEmissionFactor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">float</span>&nbsp;<span class="element-name">getLightEmissionFactor</span>()</div>
The factor of how much light is emitted by the block.
<dl class="notes">
<dt>Returns:</dt>
<dd>A factor of how much light is emitted by the block, between 0 and 1.</dd>
</dl>
</div>
:::
</section>
<section id="getLightBlockingFactor()">
:::tabs
== getLightBlockingFactor
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">float</span>&nbsp;<span class="element-name">getLightBlockingFactor</span>()</div>
The factor with which the bits block light.
<dl class="notes">
<dt>Returns:</dt>
<dd>A factor of how much light is blocked by the block, between 0 and 1.</dd>
</dl>
</div>
:::
</section>
<section id="getRelativeBlockHardness(net.minecraft.world.entity.player.Player)">
:::tabs
== getRelativeBlockHardness
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">float</span>&nbsp;<span class="element-name">getRelativeBlockHardness</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player)</span></div>
Indicates the relative block hardness for a given player.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The players to get the hardness for.</dd>
<dt>Returns:</dt>
<dd>The relative block hardness.</dd>
</dl>
</div>
:::
</section>
<section id="isEmptyBlock()">
:::tabs
== isEmptyBlock
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isEmptyBlock</span>()</div>
Indicates if the current multistate block is empty.
<dl class="notes">
<dt>Returns:</dt>
<dd>The current multistate block.</dd>
</dl>
</div>
:::
</section>
<section id="canPropagateSkylight()">
:::tabs
== canPropagateSkylight
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">canPropagateSkylight</span>()</div>
Indicates if the current multistate block can propagate skylight.
<dl class="notes">
<dt>Returns:</dt>
<dd>True when the block can propagate skylight, false when not.</dd>
</dl>
</div>
:::
</section>
<section id="canSustainGrassBelow()">
:::tabs
== canSustainGrassBelow
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">canSustainGrassBelow</span>()</div>
Indicates if the current multistate block can sustain grass below.
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> for grass sustainers, <code>false</code> for non-grass sustainers.</dd>
</dl>
</div>
:::
</section>
:::::
  

