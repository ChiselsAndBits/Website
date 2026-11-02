---
title: plugin
sidebar: false
---

# Package: mod.chiselsandbits.api.plugin

---

```
package mod.chiselsandbits.api.plugin;
```
Discovery, metadata, and lifecycle callbacks for integration plugins.

### Package Contents

:::tabs key:PackageContents
== All Types
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="IPluginManager" title="IPluginManager">IPluginManager</a></td><td>The manager for plugins.</td></tr>
  <tr><td><a href="IChiselsAndBitsPlugin" title="IChiselsAndBitsPlugin">IChiselsAndBitsPlugin</a></td><td>Represents a plugin for ChiselsAndBits.</td></tr>
  <tr><td><a href="IPluginDiscoverer" title="IPluginDiscoverer">IPluginDiscoverer</a></td><td>The platform plugin manager which can load the plugins for C<br>{@literal &}<br>B on a given platform.</td></tr>
  <tr><td><a href="PluginData" title="PluginData">PluginData</a></td><td>Pairs a discovered plugin instance with its service metadata.</td></tr>
  <tr><td><a href="IPluginDiscoverer.AbstractPluginDiscoverer" title="AbstractPluginDiscoverer">AbstractPluginDiscoverer</a></td><td>Shared service-loader implementation that filters plugins by platform availability and experimental status.</td></tr>
  <tr><td><a href="ChiselsAndBitsPlugin" title="ChiselsAndBitsPlugin">ChiselsAndBitsPlugin</a></td><td>Annotation which marks a given class as being a chisels and bits plugin.</td></tr>
  </tbody>
</table>
== Interfaces
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="IPluginManager" title="IPluginManager">IPluginManager</a></td><td>The manager for plugins.</td></tr>
  <tr><td><a href="IChiselsAndBitsPlugin" title="IChiselsAndBitsPlugin">IChiselsAndBitsPlugin</a></td><td>Represents a plugin for ChiselsAndBits.</td></tr>
  <tr><td><a href="IPluginDiscoverer" title="IPluginDiscoverer">IPluginDiscoverer</a></td><td>The platform plugin manager which can load the plugins for C<br>{@literal &}<br>B on a given platform.</td></tr>
  <tr><td><a href="ChiselsAndBitsPlugin" title="ChiselsAndBitsPlugin">ChiselsAndBitsPlugin</a></td><td>Annotation which marks a given class as being a chisels and bits plugin.</td></tr>
  </tbody>
</table>
== Classes
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="IPluginDiscoverer.AbstractPluginDiscoverer" title="AbstractPluginDiscoverer">AbstractPluginDiscoverer</a></td><td>Shared service-loader implementation that filters plugins by platform availability and experimental status.</td></tr>
  </tbody>
</table>
== Enums
No types found.
== Records
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="PluginData" title="PluginData">PluginData</a></td><td>Pairs a discovered plugin instance with its service metadata.</td></tr>
  </tbody>
</table>
:::
