--- 
title: IChiselsAndBitsConfiguration
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.config](index.md)  
# Interface IChiselsAndBitsConfiguration  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselsAndBitsConfiguration</span></div>  

  

Represents the configuration of chisels and bits.  

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
  <tr><td><code><a href="IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a></code></td><td><code><a href="#getClient()" class="member-name-link">getClient</a>()</code></td><td><div class="block">The client configuration.</div><br></td></tr>
  <tr><td><code><a href="ICommonConfiguration.html" title="interface in mod.chiselsandbits.api.config">ICommonConfiguration</a></code></td><td><code><a href="#getCommon()" class="member-name-link">getCommon</a>()</code></td><td><div class="block">The common configuration.</div><br></td></tr>
  <tr><td><code>static <a href="IChiselsAndBitsConfiguration.html" title="interface in mod.chiselsandbits.api.config">IChiselsAndBitsConfiguration</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current configuration of C&amp;B.</div><br></td></tr>
  <tr><td><code><a href="IServerConfiguration.html" title="interface in mod.chiselsandbits.api.config">IServerConfiguration</a></code></td><td><code><a href="#getServer()" class="member-name-link">getServer</a>()</code></td><td><div class="block">Gives access to the current server's configuration.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IChiselsAndBitsConfiguration.html" title="interface in mod.chiselsandbits.api.config">IChiselsAndBitsConfiguration</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current configuration of C&amp;B.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a></code></td><td><code><a href="#getClient()" class="member-name-link">getClient</a>()</code></td><td><div class="block">The client configuration.</div><br></td></tr>
  <tr><td><code><a href="ICommonConfiguration.html" title="interface in mod.chiselsandbits.api.config">ICommonConfiguration</a></code></td><td><code><a href="#getCommon()" class="member-name-link">getCommon</a>()</code></td><td><div class="block">The common configuration.</div><br></td></tr>
  <tr><td><code><a href="IServerConfiguration.html" title="interface in mod.chiselsandbits.api.config">IServerConfiguration</a></code></td><td><code><a href="#getServer()" class="member-name-link">getServer</a>()</code></td><td><div class="block">Gives access to the current server's configuration.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a></code></td><td><code><a href="#getClient()" class="member-name-link">getClient</a>()</code></td><td><div class="block">The client configuration.</div><br></td></tr>
  <tr><td><code><a href="ICommonConfiguration.html" title="interface in mod.chiselsandbits.api.config">ICommonConfiguration</a></code></td><td><code><a href="#getCommon()" class="member-name-link">getCommon</a>()</code></td><td><div class="block">The common configuration.</div><br></td></tr>
  <tr><td><code><a href="IServerConfiguration.html" title="interface in mod.chiselsandbits.api.config">IServerConfiguration</a></code></td><td><code><a href="#getServer()" class="member-name-link">getServer</a>()</code></td><td><div class="block">Gives access to the current server's configuration.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IChiselsAndBitsConfiguration.html" title="interface in mod.chiselsandbits.api.config">IChiselsAndBitsConfiguration</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
Gives access to the current configuration of C&amp;B.
<dl class="notes">
<dt>Returns:</dt>
<dd>The current configuration.</dd>
</dl>
</div>
:::


</section>

<section id="getClient()">

:::tabs
== getClient
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a></span>&nbsp;<span class="element-name">getClient</span>()</div>
The client configuration.
Elements in this configuration are only relevant for the client side of C&amp;B.
This configuration does not need to be in-sync with the server values.
<dl class="notes">
<dt>Returns:</dt>
<dd>The client configuration.</dd>
</dl>
</div>
:::


</section>

<section id="getCommon()">

:::tabs
== getCommon
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="ICommonConfiguration.html" title="interface in mod.chiselsandbits.api.config">ICommonConfiguration</a></span>&nbsp;<span class="element-name">getCommon</span>()</div>
The common configuration.
Elements in this configuration are relevant for both the server and the client side of C&amp;B.
This configuration does not need to be in-sync with the server values.
<dl class="notes">
<dt>Returns:</dt>
<dd>The common configuration.</dd>
</dl>
</div>
:::


</section>

<section id="getServer()">

:::tabs
== getServer
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IServerConfiguration.html" title="interface in mod.chiselsandbits.api.config">IServerConfiguration</a></span>&nbsp;<span class="element-name">getServer</span>()</div>
Gives access to the current server's configuration.
Elements in this configuration are relevant for both the server and client side of C&amp;B.
Since this options influence gameplay mechanics they need to be kept in sync.
<dl class="notes">
<dt>Returns:</dt>
<dd>The server configuration.</dd>
</dl>
</div>
:::


</section>

:::::
  

