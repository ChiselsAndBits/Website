--- 
title: ChiselsAndBitsPlugin
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.plugin](index.md)  
# Annotation Interface ChiselsAndBitsPlugin  
**All Extended Interfaces:**  
Annotation  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Target.html" title="class or interface in java.lang.annotation" class="external-link">@Target</a>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/ElementType.html#TYPE" title="class or interface in java.lang.annotation" class="external-link">TYPE</a>)<br/>  
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/Retention.html" title="class or interface in java.lang.annotation" class="external-link">@Retention</a>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/annotation/RetentionPolicy.html#RUNTIME" title="class or interface in java.lang.annotation" class="external-link">RUNTIME</a>)<br/>  
</span><span class="modifiers">public @interface </span><span class="element-name type-name-label">ChiselsAndBitsPlugin</span></div>  

  

Annotation which marks a given class as being a chisels and bits plugin.  

<dl class="notes"></dl>  

<!-- =========== ANNOTATION INTERFACE OPTIONAL MEMBER SUMMARY =========== -->
Optional Element Summary  
:::tabs
== Optional Elements
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Optional Element</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isExperimental()" class="member-name-link">isExperimental</a></code></td><td><div class="block">Indicator for an experimental plugin.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>[]</code></td><td><code><a href="#requiredMods()" class="member-name-link">requiredMods</a></code></td><td><div class="block">Mod ids of the mods required to load this plugin.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

<!-- ============ ANNOTATION INTERFACE MEMBER DETAIL =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Element Details  
<section id="requiredMods()">
:::tabs
== requiredMods
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>[]</span>&nbsp;<span class="element-name">requiredMods</span></div>
Mod ids of the mods required to load this plugin.
Leave on the default empty to not care for mod specific filtering.
<dl class="notes">
<dt>Returns:</dt>
<dd>The ids of the mods required to load.</dd>
</dl>
<dl class="notes">
<dt>Default:</dt>
<dd><code>{}</code></dd>
</dl>
</div>
:::
</section>
<section id="isExperimental()">
:::tabs
== isExperimental
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isExperimental</span></div>
Indicator for an experimental plugin.
Is only loaded when the user enables experimental plugins in the config.
<p>
Experimental plugins get constructed if their mods list matches, however their
initialization methods are never called!</p>
<dl class="notes">
<dt>Returns:</dt>
<dd>True for an experimental plugin.</dd>
</dl>
<dl class="notes">
<dt>Default:</dt>
<dd><code>false</code></dd>
</dl>
</div>
:::
</section>
:::::
  

  

