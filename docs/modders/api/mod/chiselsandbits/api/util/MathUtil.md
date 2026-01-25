--- 
title: MathUtil
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class MathUtil  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.MathUtil  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">MathUtil</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

  

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
  <tr><td><code>static boolean</code></td><td><code><a href="#almostEqual(java.lang.Number,java.lang.Number)" class="member-name-link">almostEqual</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;l,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;r)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#almostEqual(java.lang.Number,java.lang.Number,java.lang.Number)" class="member-name-link">almostEqual</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;l,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;r,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;epsilon)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#makePositive(double)" class="member-name-link">makePositive</a><wbr>(double&nbsp;d)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#maximizeAwayFromZero(double,double)" class="member-name-link">maximizeAwayFromZero</a><wbr>(double&nbsp;l,<br> double&nbsp;r)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#minimizeTowardsZero(double,double)" class="member-name-link">minimizeTowardsZero</a><wbr>(double&nbsp;l,<br> double&nbsp;r)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static boolean</code></td><td><code><a href="#almostEqual(java.lang.Number,java.lang.Number)" class="member-name-link">almostEqual</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;l,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;r)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#almostEqual(java.lang.Number,java.lang.Number,java.lang.Number)" class="member-name-link">almostEqual</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;l,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;r,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;epsilon)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#makePositive(double)" class="member-name-link">makePositive</a><wbr>(double&nbsp;d)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#maximizeAwayFromZero(double,double)" class="member-name-link">maximizeAwayFromZero</a><wbr>(double&nbsp;l,<br> double&nbsp;r)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#minimizeTowardsZero(double,double)" class="member-name-link">minimizeTowardsZero</a><wbr>(double&nbsp;l,<br> double&nbsp;r)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static boolean</code></td><td><code><a href="#almostEqual(java.lang.Number,java.lang.Number)" class="member-name-link">almostEqual</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;l,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;r)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static boolean</code></td><td><code><a href="#almostEqual(java.lang.Number,java.lang.Number,java.lang.Number)" class="member-name-link">almostEqual</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;l,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;r,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;epsilon)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#makePositive(double)" class="member-name-link">makePositive</a><wbr>(double&nbsp;d)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#maximizeAwayFromZero(double,double)" class="member-name-link">maximizeAwayFromZero</a><wbr>(double&nbsp;l,<br> double&nbsp;r)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static double</code></td><td><code><a href="#minimizeTowardsZero(double,double)" class="member-name-link">minimizeTowardsZero</a><wbr>(double&nbsp;l,<br> double&nbsp;r)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="almostEqual(java.lang.Number,java.lang.Number)">

:::tabs
== almostEqual
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">almostEqual</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;l,
 <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;r)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="almostEqual(java.lang.Number,java.lang.Number,java.lang.Number)">

:::tabs
== almostEqual
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">almostEqual</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;l,
 <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;r,
 <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang" class="external-link">Number</a>&nbsp;epsilon)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="minimizeTowardsZero(double,double)">

:::tabs
== minimizeTowardsZero
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">minimizeTowardsZero</span><wbr><span class="parameters">(double&nbsp;l,
 double&nbsp;r)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="maximizeAwayFromZero(double,double)">

:::tabs
== maximizeAwayFromZero
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">maximizeAwayFromZero</span><wbr><span class="parameters">(double&nbsp;l,
 double&nbsp;r)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="makePositive(double)">

:::tabs
== makePositive
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">double</span>&nbsp;<span class="element-name">makePositive</span><wbr><span class="parameters">(double&nbsp;d)</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

