--- 
title: IEligibilityOptions
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling.eligibility](index.md)  
# Interface IEligibilityOptions  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IEligibilityOptions</span></div>  

  

Determines the additional eligibility options for a given platform.  

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
  <tr><td><code>static <a href="IEligibilityOptions.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityOptions</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The eligibility manager that is active for the current platform.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidExplosionDefinitionClass(java.lang.Class)" class="member-name-link">isValidExplosionDefinitionClass</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;?&gt;&nbsp;explosionDefinitionClass)</code></td><td><div class="block">Indicates if the class that defines the explosion resistance is valid for compatibility.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IEligibilityOptions.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityOptions</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The eligibility manager that is active for the current platform.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidExplosionDefinitionClass(java.lang.Class)" class="member-name-link">isValidExplosionDefinitionClass</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;?&gt;&nbsp;explosionDefinitionClass)</code></td><td><div class="block">Indicates if the class that defines the explosion resistance is valid for compatibility.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isValidExplosionDefinitionClass(java.lang.Class)" class="member-name-link">isValidExplosionDefinitionClass</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;?&gt;&nbsp;explosionDefinitionClass)</code></td><td><div class="block">Indicates if the class that defines the explosion resistance is valid for compatibility.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IEligibilityOptions.html" title="interface in mod.chiselsandbits.api.chiseling.eligibility">IEligibilityOptions</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">The eligibility manager that is active for the current platform.
Allows for the modification of the eligibility analysis on the given platform.
Useful in case the platform defines different default classes for the processing logic.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The platform's eligibility manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="isValidExplosionDefinitionClass(java.lang.Class)">

:::tabs
== isValidExplosionDefinitionClass
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isValidExplosionDefinitionClass</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang" class="external-link">Class</a>&lt;?&gt;&nbsp;explosionDefinitionClass)</span></div>
<div class="block">Indicates if the class that defines the explosion resistance is valid for compatibility.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>explosionDefinitionClass</code> - The class that defines the explosion resistance.</dd>
<dt>Returns:</dt>
<dd>True when the class is valid, false when not.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

