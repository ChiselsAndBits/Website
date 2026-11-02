---
title: serialization
sidebar: false
---

# Package: mod.chiselsandbits.api.serialization

---

```
package mod.chiselsandbits.api.serialization;
```
Serialization contracts and codecs for Chisels and Bits data.

### Package Contents

:::tabs key:PackageContents
== All Types
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="Serializable.Registry" title="Registry">Registry</a></td><td>Serializes specifically when a registry is involved.</td></tr>
  <tr><td><a href="CBCodecs.FallbackCodec" title="FallbackCodec">FallbackCodec</a></td><td>Codec that reads from primary then fallback, but always writes with primary.</td></tr>
  <tr><td><a href="CBStreamCodecs" title="CBStreamCodecs">CBStreamCodecs</a></td><td>Stream codecs for Chisels <br>&amp;<br> Bits values and common packet transformations.</td></tr>
  <tr><td><a href="CBCodecs.NbtAwareBitsetCodec" title="NbtAwareBitsetCodec">NbtAwareBitsetCodec</a></td><td>Reads legacy byte-array bitsets as well as the current long-stream representation.</td></tr>
  <tr><td><a href="CBCodecs" title="CBCodecs">CBCodecs</a></td><td>Codec helpers for Chisels <br>&amp;<br> Bits serialization formats and compatibility.</td></tr>
  <tr><td><a href="RawSerializable" title="RawSerializable">RawSerializable</a></td><td>Defines objects which can be serialized into a raw format.</td></tr>
  <tr><td><a href="Serializable" title="Serializable">Serializable</a></td><td>Defines objects which can be serialized into an exact format.</td></tr>
  </tbody>
</table>
== Interfaces
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="Serializable.Registry" title="Registry">Registry</a></td><td>Serializes specifically when a registry is involved.</td></tr>
  <tr><td><a href="CBStreamCodecs" title="CBStreamCodecs">CBStreamCodecs</a></td><td>Stream codecs for Chisels <br>&amp;<br> Bits values and common packet transformations.</td></tr>
  <tr><td><a href="CBCodecs" title="CBCodecs">CBCodecs</a></td><td>Codec helpers for Chisels <br>&amp;<br> Bits serialization formats and compatibility.</td></tr>
  <tr><td><a href="RawSerializable" title="RawSerializable">RawSerializable</a></td><td>Defines objects which can be serialized into a raw format.</td></tr>
  <tr><td><a href="Serializable" title="Serializable">Serializable</a></td><td>Defines objects which can be serialized into an exact format.</td></tr>
  </tbody>
</table>
== Classes
No types found.
== Enums
No types found.
== Records
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="CBCodecs.FallbackCodec" title="FallbackCodec">FallbackCodec</a></td><td>Codec that reads from primary then fallback, but always writes with primary.</td></tr>
  <tr><td><a href="CBCodecs.NbtAwareBitsetCodec" title="NbtAwareBitsetCodec">NbtAwareBitsetCodec</a></td><td>Reads legacy byte-array bitsets as well as the current long-stream representation.</td></tr>
  </tbody>
</table>
:::
