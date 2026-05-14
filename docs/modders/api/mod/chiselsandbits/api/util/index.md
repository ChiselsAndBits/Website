---
title: util
sidebar: false
---

# Package: mod.chiselsandbits.api.util

---

```
package mod.chiselsandbits.api.util;
```
### Package Contents

:::tabs key:PackageContents
== All Types
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="MathUtil" title="MathUtil">MathUtil</a></td><td></td></tr>
  <tr><td><a href="BlockStatePredicates" title="BlockStatePredicates">BlockStatePredicates</a></td><td></td></tr>
  <tr><td><a href="HelpTextUtils" title="HelpTextUtils">HelpTextUtils</a></td><td>Utility class for processing help texts,<br>most notably used in tooltips of items and blocks.</td></tr>
  <tr><td><a href="Vector2i" title="Vector2i">Vector2i</a></td><td></td></tr>
  <tr><td><a href="BlockHitResultUtils" title="BlockHitResultUtils">BlockHitResultUtils</a></td><td></td></tr>
  <tr><td><a href="LambdaExceptionUtils.Consumer_WithExceptions" title="Consumer_WithExceptions">Consumer_WithExceptions</a></td><td></td></tr>
  <tr><td><a href="ByteArrayUtils" title="ByteArrayUtils">ByteArrayUtils</a></td><td></td></tr>
  <tr><td><a href="InventoryUtils" title="InventoryUtils">InventoryUtils</a></td><td></td></tr>
  <tr><td><a href="LambdaExceptionUtils" title="LambdaExceptionUtils">LambdaExceptionUtils</a></td><td></td></tr>
  <tr><td><a href="ArrayUtils" title="ArrayUtils">ArrayUtils</a></td><td>Utility class for manipulating arrays.</td></tr>
  <tr><td><a href="BlockStateSerializationUtils" title="BlockStateSerializationUtils">BlockStateSerializationUtils</a></td><td></td></tr>
  <tr><td><a href="BlockInformationUtils" title="BlockInformationUtils">BlockInformationUtils</a></td><td>Utility class for handling <br>{@link BlockState}<br>s.</td></tr>
  <tr><td><a href="IWithColor" title="IWithColor">IWithColor</a></td><td>An object with a color associated with it.</td></tr>
  <tr><td><a href="ColorUtils" title="ColorUtils">ColorUtils</a></td><td>Utility class for processing colors.</td></tr>
  <tr><td><a href="IBatchMutation" title="IBatchMutation">IBatchMutation</a></td><td>Marker interface which represents a batch mutation<br>update handler, which can be used with a try-with-resources<br>mechanic to control the update process of a batch mutation.</td></tr>
  <tr><td><a href="IQuadFunction" title="IQuadFunction">IQuadFunction</a></td><td></td></tr>
  <tr><td><a href="BitUtils" title="BitUtils">BitUtils</a></td><td></td></tr>
  <tr><td><a href="ClassUtils" title="ClassUtils">ClassUtils</a></td><td>Utility class for processing classes.</td></tr>
  <tr><td><a href="IWithIconAndColor" title="IWithIconAndColor">IWithIconAndColor</a></td><td></td></tr>
  <tr><td><a href="LambdaExceptionUtils.ToIntFunction_WithExceptions" title="ToIntFunction_WithExceptions">ToIntFunction_WithExceptions</a></td><td></td></tr>
  <tr><td><a href="ComparatorUtils" title="ComparatorUtils">ComparatorUtils</a></td><td></td></tr>
  <tr><td><a href="ParamValidator" title="ParamValidator">ParamValidator</a></td><td></td></tr>
  <tr><td><a href="BlockPosForEach" title="BlockPosForEach">BlockPosForEach</a></td><td></td></tr>
  <tr><td><a href="BlockPosStreamProvider" title="BlockPosStreamProvider">BlockPosStreamProvider</a></td><td>Utility class which provides a stream of BlockPos objects within a given range.</td></tr>
  <tr><td><a href="GroupingUtils" title="GroupingUtils">GroupingUtils</a></td><td>Utility class for managing grouping of objects<br>in a collection, based on some key.</td></tr>
  <tr><td><a href="RayTracingUtils" title="RayTracingUtils">RayTracingUtils</a></td><td>Utility class for dealing with raytracing.</td></tr>
  <tr><td><a href="IWithText" title="IWithText">IWithText</a></td><td>Represents an object with a text associated with it.</td></tr>
  <tr><td><a href="IWorldObject" title="IWorldObject">IWorldObject</a></td><td>Represents a 3D object in world.</td></tr>
  <tr><td><a href="ISnapshotable" title="ISnapshotable">ISnapshotable</a></td><td>Defines an object which is capable of making a deep clone of itself.</td></tr>
  <tr><td><a href="IWithDisplayName" title="IWithDisplayName">IWithDisplayName</a></td><td>Represents an object that is translatable.</td></tr>
  <tr><td><a href="StateEntryPredicates" title="StateEntryPredicates">StateEntryPredicates</a></td><td></td></tr>
  <tr><td><a href="LocalStrings" title="LocalStrings">LocalStrings</a></td><td></td></tr>
  <tr><td><a href="IWithIcon" title="IWithIcon">IWithIcon</a></td><td>An object with an icon to render.</td></tr>
  <tr><td><a href="IWithBatchableMutationSupport" title="IWithBatchableMutationSupport">IWithBatchableMutationSupport</a></td><td>Defines an object which supports batch mutations.</td></tr>
  <tr><td><a href="ReflectionUtils" title="ReflectionUtils">ReflectionUtils</a></td><td></td></tr>
  <tr><td><a href="VectorUtils" title="VectorUtils">VectorUtils</a></td><td></td></tr>
  </tbody>
</table>
== Interfaces
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="LambdaExceptionUtils.Consumer_WithExceptions" title="Consumer_WithExceptions">Consumer_WithExceptions</a></td><td></td></tr>
  <tr><td><a href="IWithColor" title="IWithColor">IWithColor</a></td><td>An object with a color associated with it.</td></tr>
  <tr><td><a href="IBatchMutation" title="IBatchMutation">IBatchMutation</a></td><td>Marker interface which represents a batch mutation<br>update handler, which can be used with a try-with-resources<br>mechanic to control the update process of a batch mutation.</td></tr>
  <tr><td><a href="IQuadFunction" title="IQuadFunction">IQuadFunction</a></td><td></td></tr>
  <tr><td><a href="IWithIconAndColor" title="IWithIconAndColor">IWithIconAndColor</a></td><td></td></tr>
  <tr><td><a href="LambdaExceptionUtils.ToIntFunction_WithExceptions" title="ToIntFunction_WithExceptions">ToIntFunction_WithExceptions</a></td><td></td></tr>
  <tr><td><a href="IWithText" title="IWithText">IWithText</a></td><td>Represents an object with a text associated with it.</td></tr>
  <tr><td><a href="IWorldObject" title="IWorldObject">IWorldObject</a></td><td>Represents a 3D object in world.</td></tr>
  <tr><td><a href="ISnapshotable" title="ISnapshotable">ISnapshotable</a></td><td>Defines an object which is capable of making a deep clone of itself.</td></tr>
  <tr><td><a href="IWithDisplayName" title="IWithDisplayName">IWithDisplayName</a></td><td>Represents an object that is translatable.</td></tr>
  <tr><td><a href="IWithIcon" title="IWithIcon">IWithIcon</a></td><td>An object with an icon to render.</td></tr>
  <tr><td><a href="IWithBatchableMutationSupport" title="IWithBatchableMutationSupport">IWithBatchableMutationSupport</a></td><td>Defines an object which supports batch mutations.</td></tr>
  </tbody>
</table>
== Classes
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="MathUtil" title="MathUtil">MathUtil</a></td><td></td></tr>
  <tr><td><a href="BlockStatePredicates" title="BlockStatePredicates">BlockStatePredicates</a></td><td></td></tr>
  <tr><td><a href="HelpTextUtils" title="HelpTextUtils">HelpTextUtils</a></td><td>Utility class for processing help texts,<br>most notably used in tooltips of items and blocks.</td></tr>
  <tr><td><a href="Vector2i" title="Vector2i">Vector2i</a></td><td></td></tr>
  <tr><td><a href="BlockHitResultUtils" title="BlockHitResultUtils">BlockHitResultUtils</a></td><td></td></tr>
  <tr><td><a href="ByteArrayUtils" title="ByteArrayUtils">ByteArrayUtils</a></td><td></td></tr>
  <tr><td><a href="InventoryUtils" title="InventoryUtils">InventoryUtils</a></td><td></td></tr>
  <tr><td><a href="LambdaExceptionUtils" title="LambdaExceptionUtils">LambdaExceptionUtils</a></td><td></td></tr>
  <tr><td><a href="ArrayUtils" title="ArrayUtils">ArrayUtils</a></td><td>Utility class for manipulating arrays.</td></tr>
  <tr><td><a href="BlockStateSerializationUtils" title="BlockStateSerializationUtils">BlockStateSerializationUtils</a></td><td></td></tr>
  <tr><td><a href="BlockInformationUtils" title="BlockInformationUtils">BlockInformationUtils</a></td><td>Utility class for handling <br>{@link BlockState}<br>s.</td></tr>
  <tr><td><a href="ColorUtils" title="ColorUtils">ColorUtils</a></td><td>Utility class for processing colors.</td></tr>
  <tr><td><a href="BitUtils" title="BitUtils">BitUtils</a></td><td></td></tr>
  <tr><td><a href="ClassUtils" title="ClassUtils">ClassUtils</a></td><td>Utility class for processing classes.</td></tr>
  <tr><td><a href="ComparatorUtils" title="ComparatorUtils">ComparatorUtils</a></td><td></td></tr>
  <tr><td><a href="ParamValidator" title="ParamValidator">ParamValidator</a></td><td></td></tr>
  <tr><td><a href="BlockPosForEach" title="BlockPosForEach">BlockPosForEach</a></td><td></td></tr>
  <tr><td><a href="BlockPosStreamProvider" title="BlockPosStreamProvider">BlockPosStreamProvider</a></td><td>Utility class which provides a stream of BlockPos objects within a given range.</td></tr>
  <tr><td><a href="GroupingUtils" title="GroupingUtils">GroupingUtils</a></td><td>Utility class for managing grouping of objects<br>in a collection, based on some key.</td></tr>
  <tr><td><a href="RayTracingUtils" title="RayTracingUtils">RayTracingUtils</a></td><td>Utility class for dealing with raytracing.</td></tr>
  <tr><td><a href="StateEntryPredicates" title="StateEntryPredicates">StateEntryPredicates</a></td><td></td></tr>
  <tr><td><a href="ReflectionUtils" title="ReflectionUtils">ReflectionUtils</a></td><td></td></tr>
  <tr><td><a href="VectorUtils" title="VectorUtils">VectorUtils</a></td><td></td></tr>
  </tbody>
</table>
== Enums
<table class="stretched-table">
  <thead>
    <tr><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="LocalStrings" title="LocalStrings">LocalStrings</a></td><td></td></tr>
  </tbody>
</table>
== Records
No types found.
:::

### Related

<table class="stretched-table">
  <thead>
    <tr><th>Package</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><a href="constants/index.md" title="mod.chiselsandbits.api.util.constants">mod.chiselsandbits.api.util.constants</a></td><td></td></tr>
  </tbody>
</table>
