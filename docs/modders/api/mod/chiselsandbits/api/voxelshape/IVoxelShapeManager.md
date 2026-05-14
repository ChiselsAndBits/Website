--- 
title: IVoxelShapeManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.voxelshape](index)  
# Interface IVoxelShapeManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IVoxelShapeManager</span></div>  

  

A manager for dealing with voxelshapes related to chiseled blocks and areas.  

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
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,net.minecraft.core.BlockPos)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> net.minecraft.core.BlockPos&nbsp;offset)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  <tr><td><code>static <a href="IVoxelShapeManager.html" title="interface in mod.chiselsandbits.api.voxelshape">IVoxelShapeManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IVoxelShapeManager.html" title="interface in mod.chiselsandbits.api.voxelshape">IVoxelShapeManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,net.minecraft.core.BlockPos)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> net.minecraft.core.BlockPos&nbsp;offset)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,mod.chiselsandbits.api.axissize.CollisionType,boolean)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,<br> boolean&nbsp;simplify)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.phys.shapes.VoxelShape</code></td><td><code><a href="#get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,net.minecraft.core.BlockPos)" class="member-name-link">get</a><wbr>(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,<br> net.minecraft.core.BlockPos&nbsp;offset)</code></td><td><div class="block">Returns the shape of the multistate entries which are contained in the given area accessor.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</code></td><td><code><a href="#getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType)" class="member-name-link">getCached</a><wbr>(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,<br> net.minecraft.core.BlockPos&nbsp;offset,<br> <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType)</code></td><td><div class="block">Returns the shape that is referenced by a given area shape identifier.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IVoxelShapeManager.html" title="interface in mod.chiselsandbits.api.voxelshape">IVoxelShapeManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
</div>
:::


</section>

<section id="get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor)">

:::tabs
== get
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor)</span></div>
Returns the shape of the multistate entries which are contained in the given area accessor.
Excludes all air states.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>accessor</code> - The accessor to get the shape of.</dd>
<dt>Returns:</dt>
<dd>The shape of the accessor.</dd>
</dl>
</div>
:::


</section>

<section id="get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,net.minecraft.core.BlockPos)">

:::tabs
== get
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,
 net.minecraft.core.BlockPos&nbsp;offset)</span></div>
Returns the shape of the multistate entries which are contained in the given area accessor.
Excludes all air states.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>accessor</code> - The accessor to get the shape of.</dd>
<dd><code>offset</code> - The offset to apply to the voxelshape during calculation or cache lookup.</dd>
<dt>Returns:</dt>
<dd>The shape of the accessor.</dd>
</dl>
</div>
:::


</section>

<section id="get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,mod.chiselsandbits.api.axissize.CollisionType)">

:::tabs
== get
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,
 <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType)</span></div>
Returns the shape of the multistate entries which are contained in the given area accessor.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>accessor</code> - The accessor to get the shape of.</dd>
<dd><code>sizeType</code> - The type of the shape to include.</dd>
<dt>Returns:</dt>
<dd>The shape of the accessor.</dd>
</dl>
</div>
:::


</section>

<section id="get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,mod.chiselsandbits.api.axissize.CollisionType,boolean)">

:::tabs
== get
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,
 <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,
 boolean&nbsp;simplify)</span></div>
Returns the shape of the multistate entries which are contained in the given area accessor.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>accessor</code> - The accessor to get the shape of.</dd>
<dd><code>sizeType</code> - The type of the shape to include.</dd>
<dd><code>simplify</code> - Indicates if the returned voxelshape should be simplified. Generally good for performance, but might cause some shapes to not work properly.</dd>
<dt>Returns:</dt>
<dd>The shape of the accessor.</dd>
</dl>
</div>
:::


</section>

<section id="get(mod.chiselsandbits.api.multistate.accessor.IAreaAccessor,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType,boolean)">

:::tabs
== get
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.world.phys.shapes.VoxelShape</span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>&nbsp;accessor,
 net.minecraft.core.BlockPos&nbsp;offset,
 <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,
 boolean&nbsp;simplify)</span></div>
Returns the shape of the multistate entries which are contained in the given area accessor.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>accessor</code> - The accessor to get the shape of.</dd>
<dd><code>offset</code> - The offset to apply to the voxelshape during calculation or cache lookup.</dd>
<dd><code>sizeType</code> - The type to include.</dd>
<dd><code>simplify</code> - Indicates if the returned voxelshape should be simplified. Generally good for performance, but might cause some shapes to not work properly.</dd>
<dt>Returns:</dt>
<dd>The shape of the accessor.</dd>
</dl>
</div>
:::


</section>

<section id="getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos)">

:::tabs
== getCached
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</span>&nbsp;<span class="element-name">getCached</span><wbr><span class="parameters">(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,
 net.minecraft.core.BlockPos&nbsp;offset)</span></div>
Returns the shape that is referenced by a given area shape identifier.
If no shape with the given identifier is known then an empty optional is returned.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>identifier</code> - The identifier to get the voxel shape for.</dd>
<dd><code>offset</code> - The offset to apply to the voxelshape during cache lookup.</dd>
<dt>Returns:</dt>
<dd>The optional, optionally containing the voxel shape.</dd>
</dl>
</div>
:::


</section>

<section id="getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType)">

:::tabs
== getCached
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</span>&nbsp;<span class="element-name">getCached</span><wbr><span class="parameters">(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,
 net.minecraft.core.BlockPos&nbsp;offset,
 <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType)</span></div>
Returns the shape that is referenced by a given area shape identifier.
If no shape with the given identifier is known then an empty optional is returned.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>identifier</code> - The identifier to get the voxel shape for.</dd>
<dd><code>offset</code> - The offset to apply to the voxelshape during cache lookup.</dd>
<dd><code>sizeType</code> - The type include.</dd>
<dt>Returns:</dt>
<dd>The optional, optionally containing the voxel shape.</dd>
</dl>
</div>
:::


</section>

<section id="getCached(mod.chiselsandbits.api.multistate.accessor.identifier.IAreaShapeIdentifier,net.minecraft.core.BlockPos,mod.chiselsandbits.api.axissize.CollisionType,boolean)">

:::tabs
== getCached
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.phys.shapes.VoxelShape&gt;</span>&nbsp;<span class="element-name">getCached</span><wbr><span class="parameters">(<a href="../multistate/accessor/identifier/IAreaShapeIdentifier.html" title="interface in mod.chiselsandbits.api.multistate.accessor.identifier">IAreaShapeIdentifier</a>&nbsp;identifier,
 net.minecraft.core.BlockPos&nbsp;offset,
 <a href="../axissize/CollisionType.html" title="enum class in mod.chiselsandbits.api.axissize">CollisionType</a>&nbsp;sizeType,
 boolean&nbsp;simplify)</span></div>
Returns the shape that is referenced by a given area shape identifier.
If no shape with the given identifier is known then an empty optional is returned.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>identifier</code> - The identifier to get the voxel shape for.</dd>
<dd><code>offset</code> - The offset to apply to the voxelshape during cache lookup.</dd>
<dd><code>sizeType</code> - The type to include.</dd>
<dd><code>simplify</code> - Indicates if the returned voxelshape should be simplified. Generally good for performance, but might cause some shapes to not work properly.</dd>
<dt>Returns:</dt>
<dd>The optional, optionally containing the voxel shape.</dd>
</dl>
</div>
:::


</section>

:::::
  

