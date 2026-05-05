--- 
title: ISelectedToolModeIconRendererRegistry
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.tool.mode.icon](index.md)  
# Interface ISelectedToolModeIconRendererRegistry  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ISelectedToolModeIconRendererRegistry</span></div>  

  

Registry for registering possible selected tool mode icon renderers,
and for getting the current renderer back out.  

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
  <tr><td><code><a href="ISelectedToolModeIconRenderer.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRenderer</a></code></td><td><code><a href="#getCurrent()" class="member-name-link">getCurrent</a>()</code></td><td><div class="block">The currently configured renderer as per configuration of the player.</div><br></td></tr>
  <tr><td><code>static <a href="ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></code></td><td><code><a href="#register(mod.chiselsandbits.api.client.tool.mode.icon.ISelectedToolModeIconRenderer...)" class="member-name-link">register</a><wbr>(<a href="ISelectedToolModeIconRenderer.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRenderer</a>...&nbsp;renderers)</code></td><td><div class="block">Adds the passed in renderer instances as possible candidates.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="ISelectedToolModeIconRenderer.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRenderer</a></code></td><td><code><a href="#getCurrent()" class="member-name-link">getCurrent</a>()</code></td><td><div class="block">The currently configured renderer as per configuration of the player.</div><br></td></tr>
  <tr><td><code><a href="ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></code></td><td><code><a href="#register(mod.chiselsandbits.api.client.tool.mode.icon.ISelectedToolModeIconRenderer...)" class="member-name-link">register</a><wbr>(<a href="ISelectedToolModeIconRenderer.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRenderer</a>...&nbsp;renderers)</code></td><td><div class="block">Adds the passed in renderer instances as possible candidates.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="ISelectedToolModeIconRenderer.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRenderer</a></code></td><td><code><a href="#getCurrent()" class="member-name-link">getCurrent</a>()</code></td><td><div class="block">The currently configured renderer as per configuration of the player.</div><br></td></tr>
  <tr><td><code><a href="ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></code></td><td><code><a href="#register(mod.chiselsandbits.api.client.tool.mode.icon.ISelectedToolModeIconRenderer...)" class="member-name-link">register</a><wbr>(<a href="ISelectedToolModeIconRenderer.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRenderer</a>...&nbsp;renderers)</code></td><td><div class="block">Adds the passed in renderer instances as possible candidates.</div><br></td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
</div>
:::


</section>

</li>
<li>
<section id="getCurrent()">

:::tabs
== getCurrent
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="ISelectedToolModeIconRenderer.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRenderer</a></span>&nbsp;<span class="element-name">getCurrent</span>()</div>
<div class="block">The currently configured renderer as per configuration of the player.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The renderer.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="register(mod.chiselsandbits.api.client.tool.mode.icon.ISelectedToolModeIconRenderer...)">

:::tabs
== register
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="ISelectedToolModeIconRendererRegistry.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRendererRegistry</a></span>&nbsp;<span class="element-name">register</span><wbr><span class="parameters">(<a href="ISelectedToolModeIconRenderer.html" title="interface in mod.chiselsandbits.api.client.tool.mode.icon">ISelectedToolModeIconRenderer</a>...&nbsp;renderers)</span></div>
<div class="block">Adds the passed in renderer instances as possible candidates.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>renderers</code> - The candidates.</dd>
<dt>Returns:</dt>
<dd>The registry.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

