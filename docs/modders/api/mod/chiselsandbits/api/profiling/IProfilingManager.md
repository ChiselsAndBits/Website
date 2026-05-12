--- 
title: IProfilingManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.profiling](index.md)  
# Interface IProfilingManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IProfilingManager</span></div>  

  

A profiling manager to handle the profiling of different interactions or managements.  

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
  <tr><td><code><a href="IProfilerResult.html" title="interface in mod.chiselsandbits.api.profiling">IProfilerResult</a></code></td><td><code><a href="#endProfiling(mod.chiselsandbits.api.profiling.IProfiler)" class="member-name-link">endProfiling</a><wbr>(<a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a>&nbsp;profiler)</code></td><td><div class="block">Ends the profiling of a given profiler</div><br></td></tr>
  <tr><td><code>static <a href="IProfilingManager.html" title="interface in mod.chiselsandbits.api.profiling">IProfilingManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current profiling manager.</div><br></td></tr>
  <tr><td><code><a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a></code></td><td><code><a href="#startProfiling(net.minecraft.util.profiling.jfr.Environment)" class="member-name-link">startProfiling</a><wbr>(net.minecraft.util.profiling.jfr.Environment&nbsp;profilingEnvironment)</code></td><td><div class="block">Creates a new profiler.</div><br></td></tr>
  <tr><td><code><a href="IProfilerResult.html" title="interface in mod.chiselsandbits.api.profiling">IProfilerResult</a></code></td><td><code><a href="#stopProfiling(mod.chiselsandbits.api.profiling.IProfiler)" class="member-name-link">stopProfiling</a><wbr>(<a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a>&nbsp;profiler)</code></td><td><div class="block">This stops the profiler given and clears out any profiling data, returns the collected data and stops further profiling.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IProfilingManager.html" title="interface in mod.chiselsandbits.api.profiling">IProfilingManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current profiling manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IProfilerResult.html" title="interface in mod.chiselsandbits.api.profiling">IProfilerResult</a></code></td><td><code><a href="#endProfiling(mod.chiselsandbits.api.profiling.IProfiler)" class="member-name-link">endProfiling</a><wbr>(<a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a>&nbsp;profiler)</code></td><td><div class="block">Ends the profiling of a given profiler</div><br></td></tr>
  <tr><td><code><a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a></code></td><td><code><a href="#startProfiling(net.minecraft.util.profiling.jfr.Environment)" class="member-name-link">startProfiling</a><wbr>(net.minecraft.util.profiling.jfr.Environment&nbsp;profilingEnvironment)</code></td><td><div class="block">Creates a new profiler.</div><br></td></tr>
  <tr><td><code><a href="IProfilerResult.html" title="interface in mod.chiselsandbits.api.profiling">IProfilerResult</a></code></td><td><code><a href="#stopProfiling(mod.chiselsandbits.api.profiling.IProfiler)" class="member-name-link">stopProfiling</a><wbr>(<a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a>&nbsp;profiler)</code></td><td><div class="block">This stops the profiler given and clears out any profiling data, returns the collected data and stops further profiling.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IProfilerResult.html" title="interface in mod.chiselsandbits.api.profiling">IProfilerResult</a></code></td><td><code><a href="#endProfiling(mod.chiselsandbits.api.profiling.IProfiler)" class="member-name-link">endProfiling</a><wbr>(<a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a>&nbsp;profiler)</code></td><td><div class="block">Ends the profiling of a given profiler</div><br></td></tr>
  <tr><td><code><a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a></code></td><td><code><a href="#startProfiling(net.minecraft.util.profiling.jfr.Environment)" class="member-name-link">startProfiling</a><wbr>(net.minecraft.util.profiling.jfr.Environment&nbsp;profilingEnvironment)</code></td><td><div class="block">Creates a new profiler.</div><br></td></tr>
  <tr><td><code><a href="IProfilerResult.html" title="interface in mod.chiselsandbits.api.profiling">IProfilerResult</a></code></td><td><code><a href="#stopProfiling(mod.chiselsandbits.api.profiling.IProfiler)" class="member-name-link">stopProfiling</a><wbr>(<a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a>&nbsp;profiler)</code></td><td><div class="block">This stops the profiler given and clears out any profiling data, returns the collected data and stops further profiling.</div><br></td></tr>
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
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IProfilingManager.html" title="interface in mod.chiselsandbits.api.profiling">IProfilingManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">Gives access to the current profiling manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The current profiling manager.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="startProfiling(net.minecraft.util.profiling.jfr.Environment)">

:::tabs
== startProfiling
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a></span>&nbsp;<span class="element-name">startProfiling</span><wbr><span class="parameters">(net.minecraft.util.profiling.jfr.Environment&nbsp;profilingEnvironment)</span></div>
<div class="block">Creates a new profiler.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>profilingEnvironment</code> - The environment the profiler runs in.</dd>
<dt>Returns:</dt>
<dd>The profiler</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="endProfiling(mod.chiselsandbits.api.profiling.IProfiler)">

:::tabs
== endProfiling
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IProfilerResult.html" title="interface in mod.chiselsandbits.api.profiling">IProfilerResult</a></span>&nbsp;<span class="element-name">endProfiling</span><wbr><span class="parameters">(<a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a>&nbsp;profiler)</span></div>
<div class="block">Ends the profiling of a given profiler</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>profiler</code> - The profiler to end profiling.</dd>
<dt>Returns:</dt>
<dd>The result of the profiling.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="stopProfiling(mod.chiselsandbits.api.profiling.IProfiler)">

:::tabs
== stopProfiling
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IProfilerResult.html" title="interface in mod.chiselsandbits.api.profiling">IProfilerResult</a></span>&nbsp;<span class="element-name">stopProfiling</span><wbr><span class="parameters">(<a href="IProfiler.html" title="interface in mod.chiselsandbits.api.profiling">IProfiler</a>&nbsp;profiler)</span></div>
<div class="block">This stops the profiler given and clears out any profiling data, returns the collected data and stops further profiling.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>profiler</code> - The profiler to stop and cleanup.</dd>
<dt>Returns:</dt>
<dd>The result of the profiler.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

