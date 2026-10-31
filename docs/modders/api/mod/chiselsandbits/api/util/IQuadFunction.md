--- 
title: IQuadFunction
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Interface IQuadFunction\<T1,T2,T3,T4,R\>  
**Type Parameters:**  
T1 - type of the first input  
T2 - type of the second input  
T3 - type of the third input  
T4 - type of the fourth input  
R - result type  

**Functional Interface:**  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang" class="external-link">@FunctionalInterface</a><br/>  
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IQuadFunction&lt;T1,<wbr>T2,<wbr>T3,<wbr>T4,<wbr>R&gt;</span></div>  

  

Function that accepts four arguments and produces a result.  

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
  <tr><td><code><a href="#type-param-R" title="type parameter in IQuadFunction">R</a></code></td><td><code><a href="#apply(T1,T2,T3,T4)" class="member-name-link">apply</a><wbr>(<a href="#type-param-T1" title="type parameter in IQuadFunction">T1</a>&nbsp;one,<br> <a href="#type-param-T2" title="type parameter in IQuadFunction">T2</a>&nbsp;two,<br> <a href="#type-param-T3" title="type parameter in IQuadFunction">T3</a>&nbsp;three,<br> <a href="#type-param-T4" title="type parameter in IQuadFunction">T4</a>&nbsp;four)</code></td><td><div class="block">Applies this function to four arguments.</div><br></td></tr>
  <tr><td><code>static &lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;<br><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a><wbr>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G1&gt;</code></td><td><code><a href="#firstIdentity()" class="member-name-link">firstIdentity</a>()</code></td><td><div class="block">Creates a four-argument function that returns its first argument.</div><br></td></tr>
  <tr><td><code>static &lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;<br><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a><wbr>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G4&gt;</code></td><td><code><a href="#fourthIdentity()" class="member-name-link">fourthIdentity</a>()</code></td><td><div class="block">Creates a four-argument function that returns its fourth argument.</div><br></td></tr>
  <tr><td><code>static &lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;<br><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a><wbr>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G2&gt;</code></td><td><code><a href="#secondIdentity()" class="member-name-link">secondIdentity</a>()</code></td><td><div class="block">Creates a four-argument function that returns its second argument.</div><br></td></tr>
  <tr><td><code>static &lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;<br><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a><wbr>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G3&gt;</code></td><td><code><a href="#thirdIdentity()" class="member-name-link">thirdIdentity</a>()</code></td><td><div class="block">Creates a four-argument function that returns its third argument.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static &lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;<br><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a><wbr>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G1&gt;</code></td><td><code><a href="#firstIdentity()" class="member-name-link">firstIdentity</a>()</code></td><td><div class="block">Creates a four-argument function that returns its first argument.</div><br></td></tr>
  <tr><td><code>static &lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;<br><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a><wbr>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G4&gt;</code></td><td><code><a href="#fourthIdentity()" class="member-name-link">fourthIdentity</a>()</code></td><td><div class="block">Creates a four-argument function that returns its fourth argument.</div><br></td></tr>
  <tr><td><code>static &lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;<br><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a><wbr>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G2&gt;</code></td><td><code><a href="#secondIdentity()" class="member-name-link">secondIdentity</a>()</code></td><td><div class="block">Creates a four-argument function that returns its second argument.</div><br></td></tr>
  <tr><td><code>static &lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;<br><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a><wbr>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G3&gt;</code></td><td><code><a href="#thirdIdentity()" class="member-name-link">thirdIdentity</a>()</code></td><td><div class="block">Creates a four-argument function that returns its third argument.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#type-param-R" title="type parameter in IQuadFunction">R</a></code></td><td><code><a href="#apply(T1,T2,T3,T4)" class="member-name-link">apply</a><wbr>(<a href="#type-param-T1" title="type parameter in IQuadFunction">T1</a>&nbsp;one,<br> <a href="#type-param-T2" title="type parameter in IQuadFunction">T2</a>&nbsp;two,<br> <a href="#type-param-T3" title="type parameter in IQuadFunction">T3</a>&nbsp;three,<br> <a href="#type-param-T4" title="type parameter in IQuadFunction">T4</a>&nbsp;four)</code></td><td><div class="block">Applies this function to four arguments.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#type-param-R" title="type parameter in IQuadFunction">R</a></code></td><td><code><a href="#apply(T1,T2,T3,T4)" class="member-name-link">apply</a><wbr>(<a href="#type-param-T1" title="type parameter in IQuadFunction">T1</a>&nbsp;one,<br> <a href="#type-param-T2" title="type parameter in IQuadFunction">T2</a>&nbsp;two,<br> <a href="#type-param-T3" title="type parameter in IQuadFunction">T3</a>&nbsp;three,<br> <a href="#type-param-T4" title="type parameter in IQuadFunction">T4</a>&nbsp;four)</code></td><td><div class="block">Applies this function to four arguments.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="apply(T1,T2,T3,T4)">

:::tabs
== apply
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="#type-param-R" title="type parameter in IQuadFunction">R</a></span>&nbsp;<span class="element-name">apply</span><wbr><span class="parameters">(<a href="#type-param-T1" title="type parameter in IQuadFunction">T1</a>&nbsp;one,
 <a href="#type-param-T2" title="type parameter in IQuadFunction">T2</a>&nbsp;two,
 <a href="#type-param-T3" title="type parameter in IQuadFunction">T3</a>&nbsp;three,
 <a href="#type-param-T4" title="type parameter in IQuadFunction">T4</a>&nbsp;four)</span></div>
Applies this function to four arguments.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>one</code> - the first argument</dd>
<dd><code>two</code> - the second argument</dd>
<dd><code>three</code> - the third argument</dd>
<dd><code>four</code> - the fourth argument</dd>
<dt>Returns:</dt>
<dd>the function result</dd>
</dl>
</div>
:::


</section>

<section id="firstIdentity()">

:::tabs
== firstIdentity
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;</span>&nbsp;<span class="return-type"><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G1&gt;</span>&nbsp;<span class="element-name">firstIdentity</span>()</div>
Creates a four-argument function that returns its first argument.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="firstIdentity()-type-param-G1"><code>G1</code> - type of the first argument and function result</span></dd>
<dd><span id="firstIdentity()-type-param-G2"><code>G2</code> - type of the second argument</span></dd>
<dd><span id="firstIdentity()-type-param-G3"><code>G3</code> - type of the third argument</span></dd>
<dd><span id="firstIdentity()-type-param-G4"><code>G4</code> - type of the fourth argument</span></dd>
<dt>Returns:</dt>
<dd>a function that returns its first argument</dd>
</dl>
</div>
:::


</section>

<section id="secondIdentity()">

:::tabs
== secondIdentity
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;</span>&nbsp;<span class="return-type"><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G2&gt;</span>&nbsp;<span class="element-name">secondIdentity</span>()</div>
Creates a four-argument function that returns its second argument.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="secondIdentity()-type-param-G1"><code>G1</code> - type of the first argument</span></dd>
<dd><span id="secondIdentity()-type-param-G2"><code>G2</code> - type of the second argument and function result</span></dd>
<dd><span id="secondIdentity()-type-param-G3"><code>G3</code> - type of the third argument</span></dd>
<dd><span id="secondIdentity()-type-param-G4"><code>G4</code> - type of the fourth argument</span></dd>
<dt>Returns:</dt>
<dd>a function that returns its second argument</dd>
</dl>
</div>
:::


</section>

<section id="thirdIdentity()">

:::tabs
== thirdIdentity
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;</span>&nbsp;<span class="return-type"><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G3&gt;</span>&nbsp;<span class="element-name">thirdIdentity</span>()</div>
Creates a four-argument function that returns its third argument.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="thirdIdentity()-type-param-G1"><code>G1</code> - type of the first argument</span></dd>
<dd><span id="thirdIdentity()-type-param-G2"><code>G2</code> - type of the second argument</span></dd>
<dd><span id="thirdIdentity()-type-param-G3"><code>G3</code> - type of the third argument and function result</span></dd>
<dd><span id="thirdIdentity()-type-param-G4"><code>G4</code> - type of the fourth argument</span></dd>
<dt>Returns:</dt>
<dd>a function that returns its third argument</dd>
</dl>
</div>
:::


</section>

<section id="fourthIdentity()">

:::tabs
== fourthIdentity
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="type-parameters">&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4&gt;</span>&nbsp;<span class="return-type"><a href="IQuadFunction.html" title="interface in mod.chiselsandbits.api.util">IQuadFunction</a>&lt;G1,<wbr>G2,<wbr>G3,<wbr>G4,<wbr>G4&gt;</span>&nbsp;<span class="element-name">fourthIdentity</span>()</div>
Creates a four-argument function that returns its fourth argument.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="fourthIdentity()-type-param-G1"><code>G1</code> - type of the first argument</span></dd>
<dd><span id="fourthIdentity()-type-param-G2"><code>G2</code> - type of the second argument</span></dd>
<dd><span id="fourthIdentity()-type-param-G3"><code>G3</code> - type of the third argument</span></dd>
<dd><span id="fourthIdentity()-type-param-G4"><code>G4</code> - type of the fourth argument and function result</span></dd>
<dt>Returns:</dt>
<dd>a function that returns its fourth argument</dd>
</dl>
</div>
:::


</section>

:::::
  

