--- 
title: IPositionMutator
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor.sortable](index.md)  
# Interface IPositionMutator  
**Functional Interface:**  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang" class="external-link">@FunctionalInterface</a><br/>  
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IPositionMutator</span></div>  

  

Represents an object which can mutate the order of the coordinate members
before they are retrieved from storage.

The default loop order is XYZ.
However by swapping for example the X and Y coordinate member of the
passed coordinates a YXZ loop order can be achieved without
the performance degradation of sorting.  

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
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#fromAxis(net.minecraft.core.Direction.Axis)" class="member-name-link">fromAxis</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Returns the mutator which primary iterates over the given direction and then over the others.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#identity()" class="member-name-link">identity</a>()</code></td><td><div class="block">The identity operator.</div><br></td></tr>
  <tr><td><code>net.minecraft.core.Vec3i</code></td><td><code><a href="#mutate(net.minecraft.core.Vec3i)" class="member-name-link">mutate</a><wbr>(net.minecraft.core.Vec3i&nbsp;input)</code></td><td><div class="block">Applies the mutation that this mutator performs on a given position.</div><br></td></tr>
  <tr><td><code>default <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#then(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" class="member-name-link">then</a><wbr>(<a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;next)</code></td><td><div class="block">Creates a new mutator which chains the current and the next mutator into one.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#xyz()" class="member-name-link">xyz</a>()</code></td><td><div class="block">The xyz operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#xzy()" class="member-name-link">xzy</a>()</code></td><td><div class="block">The xzy operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#yxz()" class="member-name-link">yxz</a>()</code></td><td><div class="block">The yxz operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#yzx()" class="member-name-link">yzx</a>()</code></td><td><div class="block">The yzx operator<br>Is a combination of xzy and zyx.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#zxy()" class="member-name-link">zxy</a>()</code></td><td><div class="block">The zxy operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#zyx()" class="member-name-link">zyx</a>()</code></td><td><div class="block">The zyx operator.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#fromAxis(net.minecraft.core.Direction.Axis)" class="member-name-link">fromAxis</a><wbr>(net.minecraft.core.Direction.Axis&nbsp;axis)</code></td><td><div class="block">Returns the mutator which primary iterates over the given direction and then over the others.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#identity()" class="member-name-link">identity</a>()</code></td><td><div class="block">The identity operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#xyz()" class="member-name-link">xyz</a>()</code></td><td><div class="block">The xyz operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#xzy()" class="member-name-link">xzy</a>()</code></td><td><div class="block">The xzy operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#yxz()" class="member-name-link">yxz</a>()</code></td><td><div class="block">The yxz operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#yzx()" class="member-name-link">yzx</a>()</code></td><td><div class="block">The yzx operator<br>Is a combination of xzy and zyx.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#zxy()" class="member-name-link">zxy</a>()</code></td><td><div class="block">The zxy operator.</div><br></td></tr>
  <tr><td><code>static <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#zyx()" class="member-name-link">zyx</a>()</code></td><td><div class="block">The zyx operator.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.core.Vec3i</code></td><td><code><a href="#mutate(net.minecraft.core.Vec3i)" class="member-name-link">mutate</a><wbr>(net.minecraft.core.Vec3i&nbsp;input)</code></td><td><div class="block">Applies the mutation that this mutator performs on a given position.</div><br></td></tr>
  <tr><td><code>default <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#then(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" class="member-name-link">then</a><wbr>(<a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;next)</code></td><td><div class="block">Creates a new mutator which chains the current and the next mutator into one.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.core.Vec3i</code></td><td><code><a href="#mutate(net.minecraft.core.Vec3i)" class="member-name-link">mutate</a><wbr>(net.minecraft.core.Vec3i&nbsp;input)</code></td><td><div class="block">Applies the mutation that this mutator performs on a given position.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></code></td><td><code><a href="#then(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)" class="member-name-link">then</a><wbr>(<a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;next)</code></td><td><div class="block">Creates a new mutator which chains the current and the next mutator into one.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="mutate(net.minecraft.core.Vec3i)">

:::tabs
== mutate
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.core.Vec3i</span>&nbsp;<span class="element-name">mutate</span><wbr><span class="parameters">(net.minecraft.core.Vec3i&nbsp;input)</span></div>
Applies the mutation that this mutator performs on a given position.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - The input position.</dd>
<dt>Returns:</dt>
<dd>The mutated output.</dd>
</dl>
</div>
:::


</section>

<section id="then(mod.chiselsandbits.api.multistate.accessor.sortable.IPositionMutator)">

:::tabs
== then
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">then</span><wbr><span class="parameters">(<a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a>&nbsp;next)</span></div>
Creates a new mutator which chains the current and the next mutator into one.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>next</code> - The mutator that needs to be applied after the current mutator.</dd>
<dt>Returns:</dt>
<dd>The combined mutator.</dd>
</dl>
</div>
:::


</section>

<section id="identity()">

:::tabs
== identity
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">identity</span>()</div>
The identity operator.
Performs no change to the passed in position.
<dl class="notes">
<dt>Returns:</dt>
<dd>An identity position mutator.</dd>
</dl>
</div>
:::


</section>

<section id="xyz()">

:::tabs
== xyz
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">xyz</span>()</div>
The xyz operator.
Generally also perceived as the identity mutator.
<dl class="notes">
<dt>Returns:</dt>
<dd>The identity mutator.</dd>
</dl>
</div>
:::


</section>

<section id="xzy()">

:::tabs
== xzy
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">xzy</span>()</div>
The xzy operator.
<dl class="notes">
<dt>Returns:</dt>
<dd>The mutator which switches the Y and Z coordinate members</dd>
</dl>
</div>
:::


</section>

<section id="zyx()">

:::tabs
== zyx
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">zyx</span>()</div>
The zyx operator.
<dl class="notes">
<dt>Returns:</dt>
<dd>The mutator which switches the X and Z coordinate members</dd>
</dl>
</div>
:::


</section>

<section id="yxz()">

:::tabs
== yxz
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">yxz</span>()</div>
The yxz operator.
<dl class="notes">
<dt>Returns:</dt>
<dd>The mutator which switches the X and Y coordinate members</dd>
</dl>
</div>
:::


</section>

<section id="zxy()">

:::tabs
== zxy
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">zxy</span>()</div>
The zxy operator.
<dl class="notes">
<dt>Returns:</dt>
<dd>The mutator which switches the X with the Z and then the Y with the moved X coordinate members</dd>
</dl>
</div>
:::


</section>

<section id="yzx()">

:::tabs
== yzx
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">yzx</span>()</div>
The yzx operator
Is a combination of xzy and zyx.
<dl class="notes">
<dt>Returns:</dt>
<dd>The mutator which primary switches the Y and Z and then the X and Z coordinates.</dd>
</dl>
</div>
:::


</section>

<section id="fromAxis(net.minecraft.core.Direction.Axis)">

:::tabs
== fromAxis
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPositionMutator.html" title="interface in mod.chiselsandbits.api.multistate.accessor.sortable">IPositionMutator</a></span>&nbsp;<span class="element-name">fromAxis</span><wbr><span class="parameters">(net.minecraft.core.Direction.Axis&nbsp;axis)</span></div>
Returns the mutator which primary iterates over the given direction and then over the others.
The order of the other axi is not fixed.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>axis</code> - The axis to iterate over primary.</dd>
<dt>Returns:</dt>
<dd>The position mutator for the given axis.</dd>
</dl>
</div>
:::


</section>

:::::
  

