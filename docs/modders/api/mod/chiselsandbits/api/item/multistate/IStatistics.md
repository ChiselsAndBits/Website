--- 
title: IStatistics
aside: false 
---
_Package:_ [mod.chiselsandbits.api.item.multistate](index.md)  
# Interface IStatistics  
**All Extended Interfaces:**  
[RawSerializable](../serialization/RawSerializable.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IStatistics</span><span class="extends-implements"><br/>  
extends <a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a></span></div>  

  

<div class="block">The statistics of a multi state itemstack.</div>
  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns all states (without count) that are contained in the object</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState()" class="member-name-link">getPrimaryState</a>()</code></td><td><div class="block">The primary state of the mutli state itemstacks this statistics object<br> belongs to.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Indicates if the multistate object is empty.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns all states (without count) that are contained in the object</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState()" class="member-name-link">getPrimaryState</a>()</code></td><td><div class="block">The primary state of the mutli state itemstacks this statistics object<br> belongs to.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Indicates if the multistate object is empty.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns all states (without count) that are contained in the object</div><br></td></tr>
  <tr><td><code><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></code></td><td><code><a href="#getPrimaryState()" class="member-name-link">getPrimaryState</a>()</code></td><td><div class="block">The primary state of the mutli state itemstacks this statistics object<br> belongs to.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Indicates if the multistate object is empty.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.serialization.<a href="../../serialization/RawSerializable.html" title="interface in mod.chiselsandbits.api.serialization">RawSerializable</a>
<a href="../../serialization/RawSerializable.html#codec()">codec</a>, <a href="../../serialization/RawSerializable.html#mapCodec()">mapCodec</a>, <a href="../../serialization/RawSerializable.html#streamCodec()">streamCodec</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getPrimaryState()">

:::tabs
== getPrimaryState
<div class="member-signature"><span class="return-type"><a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a></span>&nbsp;<span class="element-name">getPrimaryState</span>()</div>
<div class="block">The primary state of the mutli state itemstacks this statistics object
 belongs to.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The primary blockstate.</dd>
</dl>
:::


</section>

<section id="isEmpty()">

:::tabs
== isEmpty
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isEmpty</span>()</div>
<div class="block">Indicates if the multistate object is empty.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> for an empty multi state object.</dd>
</dl>
:::


</section>

<section id="getContainedStates()">

:::tabs
== getContainedStates
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util" class="external-link">Set</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&gt;</span>&nbsp;<span class="element-name">getContainedStates</span>()</div>
<div class="block">Returns all states (without count) that are contained in the object</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>All states in the object.</dd>
</dl>
:::


</section>

:::::
  

