--- 
title: IEligibilityAnalysisResult
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling.eligibility](index)  
# Interface IEligibilityAnalysisResult  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IEligibilityAnalysisResult</span></div>  

  

The results of an eligibility analysis.  

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
  <tr><td><code>boolean</code></td><td><code><a href="#canBeChiseled()" class="member-name-link">canBeChiseled</a>()</code></td><td><div class="block">Indicates if the requested object can be chiseled.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.chat.MutableComponent</code></td><td><code><a href="#getReason()" class="member-name-link">getReason</a>()</code></td><td><div class="block">The reason why a given eligibility result returned if it can be chiseled or not.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isAlreadyChiseled()" class="member-name-link">isAlreadyChiseled</a>()</code></td><td><div class="block">Indicates if the requested object is already chiseled.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canBeChiseled()" class="member-name-link">canBeChiseled</a>()</code></td><td><div class="block">Indicates if the requested object can be chiseled.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.chat.MutableComponent</code></td><td><code><a href="#getReason()" class="member-name-link">getReason</a>()</code></td><td><div class="block">The reason why a given eligibility result returned if it can be chiseled or not.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isAlreadyChiseled()" class="member-name-link">isAlreadyChiseled</a>()</code></td><td><div class="block">Indicates if the requested object is already chiseled.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canBeChiseled()" class="member-name-link">canBeChiseled</a>()</code></td><td><div class="block">Indicates if the requested object can be chiseled.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.chat.MutableComponent</code></td><td><code><a href="#getReason()" class="member-name-link">getReason</a>()</code></td><td><div class="block">The reason why a given eligibility result returned if it can be chiseled or not.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isAlreadyChiseled()" class="member-name-link">isAlreadyChiseled</a>()</code></td><td><div class="block">Indicates if the requested object is already chiseled.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="canBeChiseled()">

:::tabs
== canBeChiseled
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">canBeChiseled</span>()</div>
Indicates if the requested object can be chiseled.
<dl class="notes">
<dt>Returns:</dt>
<dd>True for chiselability.</dd>
</dl>
</div>
:::


</section>

<section id="isAlreadyChiseled()">

:::tabs
== isAlreadyChiseled
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isAlreadyChiseled</span>()</div>
Indicates if the requested object is already chiseled.
<dl class="notes">
<dt>Returns:</dt>
<dd>True when already chiseled.</dd>
</dl>
</div>
:::


</section>

<section id="getReason()">

:::tabs
== getReason
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.network.chat.MutableComponent</span>&nbsp;<span class="element-name">getReason</span>()</div>
The reason why a given eligibility result returned if it can be chiseled or not.
<dl class="notes">
<dt>Returns:</dt>
<dd>The displayable reason.</dd>
</dl>
</div>
:::


</section>

:::::
  

