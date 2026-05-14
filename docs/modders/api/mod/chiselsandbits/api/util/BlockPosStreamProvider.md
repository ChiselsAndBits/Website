--- 
title: BlockPosStreamProvider
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index)  
# Class BlockPosStreamProvider  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.BlockPosStreamProvider  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">BlockPosStreamProvider</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Utility class which provides a stream of BlockPos objects within a given range.  

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
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForAccessor(mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">getForAccessor</a><wbr>(<a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world accessor.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(double,double,double,double,double,double)" class="member-name-link">getForRange</a><wbr>(double&nbsp;minX,<br> double&nbsp;minY,<br> double&nbsp;minZ,<br> double&nbsp;maxX,<br> double&nbsp;maxY,<br> double&nbsp;maxZ)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;size)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range which is <code>size</code> cubed in size.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int,int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;min,<br> int&nbsp;max)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value (on all axis).</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int,int,int,int,int,int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;minX,<br> int&nbsp;minY,<br> int&nbsp;minZ,<br> int&nbsp;maxX,<br> int&nbsp;maxY,<br> int&nbsp;maxZ)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">getForRange</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;min,<br> net.minecraft.world.phys.Vec3&nbsp;max)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForWorldObject(mod.chiselsandbits.api.util.IWorldObject)" class="member-name-link">getForWorldObject</a><wbr>(<a href="IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>&nbsp;worldObject)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world object.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForWorldObject(mod.chiselsandbits.api.util.IWorldObject,boolean)" class="member-name-link">getForWorldObject</a><wbr>(<a href="IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>&nbsp;worldObject,<br> boolean&nbsp;subtractBitSize)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world object.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForAccessor(mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">getForAccessor</a><wbr>(<a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world accessor.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(double,double,double,double,double,double)" class="member-name-link">getForRange</a><wbr>(double&nbsp;minX,<br> double&nbsp;minY,<br> double&nbsp;minZ,<br> double&nbsp;maxX,<br> double&nbsp;maxY,<br> double&nbsp;maxZ)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;size)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range which is <code>size</code> cubed in size.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int,int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;min,<br> int&nbsp;max)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value (on all axis).</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int,int,int,int,int,int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;minX,<br> int&nbsp;minY,<br> int&nbsp;minZ,<br> int&nbsp;maxX,<br> int&nbsp;maxY,<br> int&nbsp;maxZ)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">getForRange</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;min,<br> net.minecraft.world.phys.Vec3&nbsp;max)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForWorldObject(mod.chiselsandbits.api.util.IWorldObject)" class="member-name-link">getForWorldObject</a><wbr>(<a href="IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>&nbsp;worldObject)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world object.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForWorldObject(mod.chiselsandbits.api.util.IWorldObject,boolean)" class="member-name-link">getForWorldObject</a><wbr>(<a href="IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>&nbsp;worldObject,<br> boolean&nbsp;subtractBitSize)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world object.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForAccessor(mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">getForAccessor</a><wbr>(<a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world accessor.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(double,double,double,double,double,double)" class="member-name-link">getForRange</a><wbr>(double&nbsp;minX,<br> double&nbsp;minY,<br> double&nbsp;minZ,<br> double&nbsp;maxX,<br> double&nbsp;maxY,<br> double&nbsp;maxZ)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;size)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range which is <code>size</code> cubed in size.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int,int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;min,<br> int&nbsp;max)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value (on all axis).</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(int,int,int,int,int,int)" class="member-name-link">getForRange</a><wbr>(int&nbsp;minX,<br> int&nbsp;minY,<br> int&nbsp;minZ,<br> int&nbsp;maxX,<br> int&nbsp;maxY,<br> int&nbsp;maxZ)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)" class="member-name-link">getForRange</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;min,<br> net.minecraft.world.phys.Vec3&nbsp;max)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForWorldObject(mod.chiselsandbits.api.util.IWorldObject)" class="member-name-link">getForWorldObject</a><wbr>(<a href="IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>&nbsp;worldObject)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world object.</div><br></td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a><wbr>&lt;net.minecraft.core.BlockPos&gt;</code></td><td><code><a href="#getForWorldObject(mod.chiselsandbits.api.util.IWorldObject,boolean)" class="member-name-link">getForWorldObject</a><wbr>(<a href="IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>&nbsp;worldObject,<br> boolean&nbsp;subtractBitSize)</code></td><td><div class="block">Provides a stream of BlockPos objects within a given world object.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getForRange(int)">

:::tabs
== getForRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">getForRange</span><wbr><span class="parameters">(int&nbsp;size)</span></div>
Provides a stream of BlockPos objects within a given range which is <code>size</code> cubed in size.
The coordinates will as such (on each axis) run from 0 to <code>size - 1</code>.
<p>
Internally invokes <a href="#getForRange(int,int)"><code>getForRange(int, int)</code></a>, with <code>0</code> as the min value,
and <code>size - 1</code> as max value.</p>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - The size of each axis for the block positions stream.</dd>
<dt>Returns:</dt>
<dd>A stream of blockpositions in the <code>size</code> cubed in area.</dd>
</dl>
</div>
:::


</section>

<section id="getForRange(int,int)">

:::tabs
== getForRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">getForRange</span><wbr><span class="parameters">(int&nbsp;min,
 int&nbsp;max)</span></div>
Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value (on all axis).
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>min</code> - The minimal value of the block positions stream on all axis.</dd>
<dd><code>max</code> - The maximal value of the block positions stream on all axis.</dd>
<dt>Returns:</dt>
<dd>The block position stream within the given range.</dd>
</dl>
</div>
:::


</section>

<section id="getForWorldObject(mod.chiselsandbits.api.util.IWorldObject)">

:::tabs
== getForWorldObject
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">getForWorldObject</span><wbr><span class="parameters">(<a href="IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>&nbsp;worldObject)</span></div>
Provides a stream of BlockPos objects within a given world object.
<p>
This rounds the vectors down to the block positions they are in, and then extracts the minimal and maximal values
for each axis.
</p><p>
Internally invokes <a href="#getForRange(int,int,int,int,int,int)"><code>getForRange(int, int, int, int, int, int)</code></a>, with the rounded down vectors as the min and max values.</p>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>worldObject</code> - The world object to iterate over.</dd>
<dt>Returns:</dt>
<dd>The block position stream within the given range.</dd>
</dl>
</div>
:::


</section>

<section id="getForAccessor(mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)">

:::tabs
== getForAccessor
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">getForAccessor</span><wbr><span class="parameters">(<a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</span></div>
Provides a stream of BlockPos objects within a given world accessor.
<p>
This rounds the vectors down to the block positions they are in, and then extracts the minimal and maximal values
for each axis.
</p><p>
Internally invokes <a href="#getForRange(int,int,int,int,int,int)"><code>getForRange(int, int, int, int, int, int)</code></a>, with the rounded down vectors as the min and max values.</p>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>worldAreaAccessor</code> - The world accessor to iterate over.</dd>
<dt>Returns:</dt>
<dd>The block position stream within the given range.</dd>
</dl>
</div>
:::


</section>

<section id="getForWorldObject(mod.chiselsandbits.api.util.IWorldObject,boolean)">

:::tabs
== getForWorldObject
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">getForWorldObject</span><wbr><span class="parameters">(<a href="IWorldObject.html" title="interface in mod.chiselsandbits.api.util">IWorldObject</a>&nbsp;worldObject,
 boolean&nbsp;subtractBitSize)</span></div>
Provides a stream of BlockPos objects within a given world object.
<p>
This rounds the vectors down to the block positions they are in, and then extracts the minimal and maximal values
for each axis.
</p><p>
Internally invokes <a href="#getForRange(int,int,int,int,int,int)"><code>getForRange(int, int, int, int, int, int)</code></a>, with the rounded down vectors as the min and max values.</p>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>worldObject</code> - The world object to iterate over.</dd>
<dd><code>subtractBitSize</code> - Indicates if from the end a bit size should be subtracted to not run out of the area.</dd>
<dt>Returns:</dt>
<dd>The block position stream within the given range.</dd>
</dl>
</div>
:::


</section>

<section id="getForRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)">

:::tabs
== getForRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">getForRange</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;min,
 net.minecraft.world.phys.Vec3&nbsp;max)</span></div>
Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.
<p>
This rounds the vectors down to the block positions they are in, and then extracts the minimal and maximal values
for each axis.
</p><p>
Internally invokes <a href="#getForRange(int,int,int,int,int,int)"><code>getForRange(int, int, int, int, int, int)</code></a>, with the rounded down vectors as the min and max values.</p>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>min</code> - The unrounded minimal value of the block positions stream on all axis.</dd>
<dd><code>max</code> - The unrounded maximal value of the block positions stream on all axis.</dd>
<dt>Returns:</dt>
<dd>The block position stream within the given range.</dd>
</dl>
</div>
:::


</section>

<section id="getForRange(double,double,double,double,double,double)">

:::tabs
== getForRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">getForRange</span><wbr><span class="parameters">(double&nbsp;minX,
 double&nbsp;minY,
 double&nbsp;minZ,
 double&nbsp;maxX,
 double&nbsp;maxY,
 double&nbsp;maxZ)</span></div>
Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.
<p>
Internally this calls <a href="#getForRange(net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3)"><code>getForRange(Vec3, Vec3)</code></a>, with vectors constructed from the minimal and maximal values.
All of its logic (so the rounding) is as such also applied.</p>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>minX</code> - The minimal value of the X coordinate.</dd>
<dd><code>minY</code> - The minimal value of the Y coordinate.</dd>
<dd><code>minZ</code> - The minimal value of the Z coordinate.</dd>
<dd><code>maxX</code> - The maximal value of the X coordinate.</dd>
<dd><code>maxY</code> - The maximal value of the Y coordinate.</dd>
<dd><code>maxZ</code> - The maximal value of the Z coordinate.</dd>
<dt>Returns:</dt>
<dd>The block position stream within the given range.</dd>
</dl>
</div>
:::


</section>

<section id="getForRange(int,int,int,int,int,int)">

:::tabs
== getForRange
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream" class="external-link">Stream</a>&lt;net.minecraft.core.BlockPos&gt;</span>&nbsp;<span class="element-name">getForRange</span><wbr><span class="parameters">(int&nbsp;minX,
 int&nbsp;minY,
 int&nbsp;minZ,
 int&nbsp;maxX,
 int&nbsp;maxY,
 int&nbsp;maxZ)</span></div>
Provides a stream of BlockPos objects within a given range from the given minimal value to the given maximal value.
<p>
If the minimal and maximal values are the same, then the stream will contain only one block position.</p>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>minX</code> - The minimal value of the X coordinate.</dd>
<dd><code>minY</code> - The minimal value of the Y coordinate.</dd>
<dd><code>minZ</code> - The minimal value of the Z coordinate.</dd>
<dd><code>maxX</code> - The maximal value of the X coordinate.</dd>
<dd><code>maxY</code> - The maximal value of the Y coordinate.</dd>
<dd><code>maxZ</code> - The maximal value of the Z coordinate.</dd>
<dt>Returns:</dt>
<dd>The block position stream within the given range.</dd>
</dl>
</div>
:::


</section>

:::::
  

