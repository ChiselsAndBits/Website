--- 
title: IMutableStateEntryInfo
aside: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.mutator](index.md)  
# Interface IMutableStateEntryInfo  
**All Extended Interfaces:**  
[IAABBOwner](../aabb/IAABBOwner.md), [IStateEntryInfo](../accessor/IStateEntryInfo.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMutableStateEntryInfo</span><span class="extends-implements"><br/>  
extends <a href="../accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a></span></div>  

  

  

<dl class="notes"></dl>  

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
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears the current state entries blockstate.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#overrideState(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">overrideState</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Overrides the current entries block information</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setBlockInformation(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setBlockInformation</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Sets the current entries block information.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears the current state entries blockstate.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#overrideState(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">overrideState</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Overrides the current entries block information</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setBlockInformation(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setBlockInformation</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Sets the current entries block information.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clear()" class="member-name-link">clear</a>()</code></td><td><div class="block">Clears the current state entries blockstate.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setBlockInformation(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setBlockInformation</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Sets the current entries block information.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#overrideState(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">overrideState</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Overrides the current entries block information</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>
<a href="../accessor/IStateEntryInfo.html#getBlockInformation()">getBlockInformation</a>, <a href="../accessor/IStateEntryInfo.html#getBoundingBox()">getBoundingBox</a>, <a href="../accessor/IStateEntryInfo.html#getCenterPoint()">getCenterPoint</a>, <a href="../accessor/IStateEntryInfo.html#getEndPoint()">getEndPoint</a>, <a href="../accessor/IStateEntryInfo.html#getStartPoint()">getStartPoint</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="setBlockInformation(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== setBlockInformation
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setBlockInformation</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span>
                  throws <span class="exceptions"><a href="../../exceptions/SpaceOccupiedException.html" title="class in mod.chiselsandbits.api.exceptions">SpaceOccupiedException</a></span></div>
<div class="block">Sets the current entries block information.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The new block information of the entry.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../exceptions/SpaceOccupiedException.html" title="class in mod.chiselsandbits.api.exceptions">SpaceOccupiedException</a></code> - When the space is not clear and as such the bit can not be set.</dd>
</dl>
:::


</section>

<section id="clear()">

:::tabs
== clear
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clear</span>()</div>
<div class="block">Clears the current state entries blockstate.
 Effectively setting the current blockstate to air.</div>
<dl class="notes"></dl>
:::


</section>

<section id="overrideState(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== overrideState
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">overrideState</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Overrides the current entries block information</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The new block information of the entry.</dd>
</dl>
:::


</section>

:::::
  

