--- 
title: IWithDisplayName
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Interface IWithDisplayName  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWithDisplayName</span></div>  

  

Represents an object that is translatable.  

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
  <tr><td><code>net.minecraft.network.chat.Component</code></td><td><code><a href="#getDisplayName()" class="member-name-link">getDisplayName</a>()</code></td><td><div class="block">Returns the display name of the object in a text component.</div><br></td></tr>
  <tr><td><code>default net.minecraft.network.chat.Component</code></td><td><code><a href="#getMultiLineDisplayName()" class="member-name-link">getMultiLineDisplayName</a>()</code></td><td><div class="block">Returns the display name of the object in a text component.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.network.chat.Component</code></td><td><code><a href="#getDisplayName()" class="member-name-link">getDisplayName</a>()</code></td><td><div class="block">Returns the display name of the object in a text component.</div><br></td></tr>
  <tr><td><code>default net.minecraft.network.chat.Component</code></td><td><code><a href="#getMultiLineDisplayName()" class="member-name-link">getMultiLineDisplayName</a>()</code></td><td><div class="block">Returns the display name of the object in a text component.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.network.chat.Component</code></td><td><code><a href="#getDisplayName()" class="member-name-link">getDisplayName</a>()</code></td><td><div class="block">Returns the display name of the object in a text component.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.network.chat.Component</code></td><td><code><a href="#getMultiLineDisplayName()" class="member-name-link">getMultiLineDisplayName</a>()</code></td><td><div class="block">Returns the display name of the object in a text component.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getDisplayName()">

:::tabs
== getDisplayName
<div class="member-signature"><span class="return-type">net.minecraft.network.chat.Component</span>&nbsp;<span class="element-name">getDisplayName</span>()</div>
Returns the display name of the object in a text component.
<dl class="notes">
<dt>Returns:</dt>
<dd>The display name.</dd>
</dl>
:::


</section>

<section id="getMultiLineDisplayName()">

:::tabs
== getMultiLineDisplayName
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.network.chat.Component</span>&nbsp;<span class="element-name">getMultiLineDisplayName</span>()</div>
Returns the display name of the object in a text component.
 This display name may contain several newline statements which can be wrapped.
<dl class="notes">
<dt>Returns:</dt>
<dd>The multiline display name.</dd>
</dl>
:::


</section>

:::::
  

