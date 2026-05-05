--- 
title: ColorUtils
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class ColorUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.ColorUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ColorUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class for processing colors.  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final int</code></td><td><code><a href="#EMPTY_CHANNEL" class="member-name-link">EMPTY_CHANNEL</a></code></td><td><div class="block">The minimal value for a given color channel.</div><br></td></tr>
  <tr><td><code>static final int</code></td><td><code><a href="#FULL_CHANNEL" class="member-name-link">FULL_CHANNEL</a></code></td><td><div class="block">The maximal value for a given color channel.</div><br></td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
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
  <tr><td><code>static int</code></td><td><code><a href="#pack(float%5B%5D)" class="member-name-link">pack</a><wbr>(float[]&nbsp;color)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(float,float,float,float)" class="member-name-link">pack</a><wbr>(float&nbsp;r,<br> float&nbsp;g,<br> float&nbsp;b,<br> float&nbsp;a)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int)" class="member-name-link">pack</a><wbr>(int&nbsp;c)</code></td><td><div class="block">Packs all three color channels (plus a full alpha channel) with the same value into an integer.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int,int,int)" class="member-name-link">pack</a><wbr>(int&nbsp;r,<br> int&nbsp;g,<br> int&nbsp;b)</code></td><td><div class="block">Packs all three color channels (plus a full alpha channel) with the values into an integer.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int,int,int,int)" class="member-name-link">pack</a><wbr>(int&nbsp;r,<br> int&nbsp;g,<br> int&nbsp;b,<br> int&nbsp;a)</code></td><td><div class="block">Packs all four color channels with the values into an integer.</div><br></td></tr>
  <tr><td><code>static float[]</code></td><td><code><a href="#unpack(int)" class="member-name-link">unpack</a><wbr>(int&nbsp;color)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static int</code></td><td><code><a href="#pack(float%5B%5D)" class="member-name-link">pack</a><wbr>(float[]&nbsp;color)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(float,float,float,float)" class="member-name-link">pack</a><wbr>(float&nbsp;r,<br> float&nbsp;g,<br> float&nbsp;b,<br> float&nbsp;a)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int)" class="member-name-link">pack</a><wbr>(int&nbsp;c)</code></td><td><div class="block">Packs all three color channels (plus a full alpha channel) with the same value into an integer.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int,int,int)" class="member-name-link">pack</a><wbr>(int&nbsp;r,<br> int&nbsp;g,<br> int&nbsp;b)</code></td><td><div class="block">Packs all three color channels (plus a full alpha channel) with the values into an integer.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int,int,int,int)" class="member-name-link">pack</a><wbr>(int&nbsp;r,<br> int&nbsp;g,<br> int&nbsp;b,<br> int&nbsp;a)</code></td><td><div class="block">Packs all four color channels with the values into an integer.</div><br></td></tr>
  <tr><td><code>static float[]</code></td><td><code><a href="#unpack(int)" class="member-name-link">unpack</a><wbr>(int&nbsp;color)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static int</code></td><td><code><a href="#pack(float%5B%5D)" class="member-name-link">pack</a><wbr>(float[]&nbsp;color)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(float,float,float,float)" class="member-name-link">pack</a><wbr>(float&nbsp;r,<br> float&nbsp;g,<br> float&nbsp;b,<br> float&nbsp;a)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int)" class="member-name-link">pack</a><wbr>(int&nbsp;c)</code></td><td><div class="block">Packs all three color channels (plus a full alpha channel) with the same value into an integer.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int,int,int)" class="member-name-link">pack</a><wbr>(int&nbsp;r,<br> int&nbsp;g,<br> int&nbsp;b)</code></td><td><div class="block">Packs all three color channels (plus a full alpha channel) with the values into an integer.</div><br></td></tr>
  <tr><td><code>static int</code></td><td><code><a href="#pack(int,int,int,int)" class="member-name-link">pack</a><wbr>(int&nbsp;r,<br> int&nbsp;g,<br> int&nbsp;b,<br> int&nbsp;a)</code></td><td><div class="block">Packs all four color channels with the values into an integer.</div><br></td></tr>
  <tr><td><code>static float[]</code></td><td><code><a href="#unpack(int)" class="member-name-link">unpack</a><wbr>(int&nbsp;color)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a></section>
</li>
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="FULL_CHANNEL">

:::tabs
== FULL_CHANNEL
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">FULL_CHANNEL</span></div>
<div class="block">The maximal value for a given color channel.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#mod.chiselsandbits.api.util.ColorUtils.FULL_CHANNEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="EMPTY_CHANNEL">

:::tabs
== EMPTY_CHANNEL
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">EMPTY_CHANNEL</span></div>
<div class="block">The minimal value for a given color channel.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#mod.chiselsandbits.api.util.ColorUtils.EMPTY_CHANNEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="pack(int)">

:::tabs
== pack
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">pack</span><wbr><span class="parameters">(int&nbsp;c)</span></div>
<div class="block">Packs all three color channels (plus a full alpha channel) with the same value into an integer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>c</code> - The value of the color channels to pack.</dd>
<dt>Returns:</dt>
<dd>A packed integer, representing the color with all three channels set to the same value.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="pack(int,int,int)">

:::tabs
== pack
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">pack</span><wbr><span class="parameters">(int&nbsp;r,
 int&nbsp;g,
 int&nbsp;b)</span></div>
<div class="block">Packs all three color channels (plus a full alpha channel) with the values into an integer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - The value for the red channel.</dd>
<dd><code>g</code> - The value for the green channel.</dd>
<dd><code>b</code> - The value for the blue channel.</dd>
<dt>Returns:</dt>
<dd>A packed integer, representing the color.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="pack(int,int,int,int)">

:::tabs
== pack
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">pack</span><wbr><span class="parameters">(int&nbsp;r,
 int&nbsp;g,
 int&nbsp;b,
 int&nbsp;a)</span></div>
<div class="block">Packs all four color channels with the values into an integer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - The value for the red channel.</dd>
<dd><code>g</code> - The value for the green channel.</dd>
<dd><code>b</code> - The value for the blue channel.</dd>
<dd><code>a</code> - The value for the alpha channel.</dd>
<dt>Returns:</dt>
<dd>A packed integer, representing the color.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="pack(float,float,float,float)">

:::tabs
== pack
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">pack</span><wbr><span class="parameters">(float&nbsp;r,
 float&nbsp;g,
 float&nbsp;b,
 float&nbsp;a)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="pack(float[])">

:::tabs
== pack
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">pack</span><wbr><span class="parameters">(float[]&nbsp;color)</span></div>
</div>
:::


</section>

</li>
<li>
<section id="unpack(int)">

:::tabs
== unpack
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">float[]</span>&nbsp;<span class="element-name">unpack</span><wbr><span class="parameters">(int&nbsp;color)</span></div>
</div>
:::


</section>

</li>
</ul>
:::::
  

