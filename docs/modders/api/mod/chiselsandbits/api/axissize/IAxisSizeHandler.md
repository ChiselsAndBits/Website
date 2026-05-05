--- 
title: IAxisSizeHandler
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.axissize](index.md)  
# Interface IAxisSizeHandler  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IAxisSizeHandler</span></div>  

  

Represents a handler which can indicate the current active maximum and minimum size
of the multistate object.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IAxisSizeHandler.html" title="interface in mod.chiselsandbits.api.axissize">IAxisSizeHandler</a></code></td><td><code><a href="#empty()" class="member-name-link">empty</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getHighest()" class="member-name-link">getHighest</a>()</code></td><td><div class="block">The highest set value on the axis of the size handler.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getLowest()" class="member-name-link">getLowest</a>()</code></td><td><div class="block">The lowest set value on the axis of the size handler.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IAxisSizeHandler.html" title="interface in mod.chiselsandbits.api.axissize">IAxisSizeHandler</a></code></td><td><code><a href="#empty()" class="member-name-link">empty</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#getHighest()" class="member-name-link">getHighest</a>()</code></td><td><div class="block">The highest set value on the axis of the size handler.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getLowest()" class="member-name-link">getLowest</a>()</code></td><td><div class="block">The lowest set value on the axis of the size handler.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>int</code></td><td><code><a href="#getHighest()" class="member-name-link">getHighest</a>()</code></td><td><div class="block">The highest set value on the axis of the size handler.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getLowest()" class="member-name-link">getLowest</a>()</code></td><td><div class="block">The lowest set value on the axis of the size handler.</div><br></td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="empty()">

:::tabs
== empty
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IAxisSizeHandler.html" title="interface in mod.chiselsandbits.api.axissize">IAxisSizeHandler</a></span>&nbsp;<span class="element-name">empty</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getLowest()">

:::tabs
== getLowest
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">int</span>&nbsp;<span class="element-name">getLowest</span>()</div>
<div class="block">The lowest set value on the axis of the size handler.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The lowest set value.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getHighest()">

:::tabs
== getHighest
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">int</span>&nbsp;<span class="element-name">getHighest</span>()</div>
<div class="block">The highest set value on the axis of the size handler.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The highest set value.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

