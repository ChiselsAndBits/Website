---
title: api
sidebar: false
---

# Package: mod.chiselsandbits.api

---

```
@org.jspecify.annotations.NullMarked 
package mod.chiselsandbits.api;
```
Public entry points for Chisels and Bits integrations.

### Package Contents

:::tabs key:PackageContents
== All Types
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="IgnoreBlockLogic" title="IgnoreBlockLogic">IgnoreBlockLogic</a></td><td>When checking for blocks to allow for chiseling Chisels and Bits checks various methods...</td></tr>
  <tr><td><a href="IChiselsAndBitsAPI" title="IChiselsAndBitsAPI">IChiselsAndBitsAPI</a></td><td>Do not implement it can be accessed via its <br>{@link #getInstance()}<br>-method.</td></tr>
  <tr><td><a href="IChiselsAndBitsAPI.Holder" title="Holder">Holder</a></td><td>Holds the API instance installed by the platform bootstrap.</td></tr>
  </tbody>
</table>
== Interfaces
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="IgnoreBlockLogic" title="IgnoreBlockLogic">IgnoreBlockLogic</a></td><td>When checking for blocks to allow for chiseling Chisels and Bits checks various methods...</td></tr>
  <tr><td><a href="IChiselsAndBitsAPI" title="IChiselsAndBitsAPI">IChiselsAndBitsAPI</a></td><td>Do not implement it can be accessed via its <br>{@link #getInstance()}<br>-method.</td></tr>
  </tbody>
</table>
== Classes
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="IChiselsAndBitsAPI.Holder" title="Holder">Holder</a></td><td>Holds the API instance installed by the platform bootstrap.</td></tr>
  </tbody>
</table>
== Enums
No types found.
== Records
No types found.
:::

### Related

<table class="stretched-table">
  <thead>
    <tr><th>Package</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="registries/index" title="mod.chiselsandbits.api.registries">mod.chiselsandbits.api.registries</a></td><td>Access to the registries used by Chisels and Bits.</td></tr>
  <tr><td><a href="block/index" title="mod.chiselsandbits.api.block">mod.chiselsandbits.api.block</a></td><td>Block contracts for multistate content.</td></tr>
  <tr><td><a href="measuring/index" title="mod.chiselsandbits.api.measuring">mod.chiselsandbits.api.measuring</a></td><td>World measurements, measuring modes, and grid-snapping rules.</td></tr>
  <tr><td><a href="launch/index" title="mod.chiselsandbits.api.launch">mod.chiselsandbits.api.launch</a></td><td>Properties that affect game launch and runtime behavior.</td></tr>
  <tr><td><a href="sealing/index" title="mod.chiselsandbits.api.sealing">mod.chiselsandbits.api.sealing</a></td><td>Sealing and unsealing support for item stacks.</td></tr>
  <tr><td><a href="permissions/index" title="mod.chiselsandbits.api.permissions">mod.chiselsandbits.api.permissions</a></td><td>Permission checks for player edits to world areas.</td></tr>
  <tr><td><a href="util/index" title="mod.chiselsandbits.api.util">mod.chiselsandbits.api.util</a></td><td>Shared utilities and small contracts used throughout the API.</td></tr>
  <tr><td><a href="multistate/index" title="mod.chiselsandbits.api.multistate">mod.chiselsandbits.api.multistate</a></td><td>Resolution of state entries within multistate objects.</td></tr>
  <tr><td><a href="serialization/index" title="mod.chiselsandbits.api.serialization">mod.chiselsandbits.api.serialization</a></td><td>Serialization contracts and codecs for Chisels and Bits data.</td></tr>
  <tr><td><a href="aabb/index" title="mod.chiselsandbits.api.aabb">mod.chiselsandbits.api.aabb</a></td><td>Contracts for objects with axis-aligned bounding boxes.</td></tr>
  <tr><td><a href="change/index" title="mod.chiselsandbits.api.change">mod.chiselsandbits.api.change</a></td><td>Tracking and grouping of edits to multistate blocks.</td></tr>
  <tr><td><a href="glueing/index" title="mod.chiselsandbits.api.glueing">mod.chiselsandbits.api.glueing</a></td><td>Block-entity support for structures connected with glue.</td></tr>
  <tr><td><a href="voxelshape/index" title="mod.chiselsandbits.api.voxelshape">mod.chiselsandbits.api.voxelshape</a></td><td>Voxel-shape calculation for multistate blocks and areas.</td></tr>
  <tr><td><a href="chiseling/index" title="mod.chiselsandbits.api.chiseling">mod.chiselsandbits.api.chiseling</a></td><td>Coordination and context of chiseling operations.</td></tr>
  <tr><td><a href="profiling/index" title="mod.chiselsandbits.api.profiling">mod.chiselsandbits.api.profiling</a></td><td>Timing and profiling of Chisels and Bits operations.</td></tr>
  <tr><td><a href="blockinformation/index" title="mod.chiselsandbits.api.blockinformation">mod.chiselsandbits.api.blockinformation</a></td><td>Immutable descriptions of the materials stored in multistate objects.</td></tr>
  <tr><td><a href="neighborhood/index" title="mod.chiselsandbits.api.neighborhood">mod.chiselsandbits.api.neighborhood</a></td><td>Block-neighborhood descriptions for environment-dependent cache keys.</td></tr>
  <tr><td><a href="plugin/index" title="mod.chiselsandbits.api.plugin">mod.chiselsandbits.api.plugin</a></td><td>Discovery, metadata, and lifecycle callbacks for integration plugins.</td></tr>
  <tr><td><a href="axissize/index" title="mod.chiselsandbits.api.axissize">mod.chiselsandbits.api.axissize</a></td><td>Axis bounds and occupancy rules for multistate objects.</td></tr>
  <tr><td><a href="placement/index" title="mod.chiselsandbits.api.placement">mod.chiselsandbits.api.placement</a></td><td>World placement contracts, options, previews, and results.</td></tr>
  <tr><td><a href="config/index" title="mod.chiselsandbits.api.config">mod.chiselsandbits.api.config</a></td><td>Access to client, common, and server configuration values.</td></tr>
  <tr><td><a href="notifications/index" title="mod.chiselsandbits.api.notifications">mod.chiselsandbits.api.notifications</a></td><td>Player-facing notifications for in-game events.</td></tr>
  <tr><td><a href="reloading/index" title="mod.chiselsandbits.api.reloading">mod.chiselsandbits.api.reloading</a></td><td>Cache invalidation during reloads.</td></tr>
  <tr><td><a href="exceptions/index" title="mod.chiselsandbits.api.exceptions">mod.chiselsandbits.api.exceptions</a></td><td>Exceptions describing invalid or unsupported multistate interactions.</td></tr>
  <tr><td><a href="item/index" title="mod.chiselsandbits.api.item">mod.chiselsandbits.api.item</a></td><td>Shared item integration contracts.</td></tr>
  </tbody>
</table>
