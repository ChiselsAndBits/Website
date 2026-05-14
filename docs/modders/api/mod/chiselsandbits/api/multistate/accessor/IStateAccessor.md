--- 
title: IStateAccessor
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.accessor](index.md)  
# Interface IStateAccessor  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IStateAccessor</span></div>  

  

  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#getInAreaTarget(net.minecraft.world.phys.Vec3)" class="member-name-link">getInAreaTarget</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Gets the target state in the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">getInBlockTarget</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Gets the target state in the current area, using the in area block position offset as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#getInAreaTarget(net.minecraft.world.phys.Vec3)" class="member-name-link">getInAreaTarget</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Gets the target state in the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">getInBlockTarget</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Gets the target state in the current area, using the in area block position offset as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#getInAreaTarget(net.minecraft.world.phys.Vec3)" class="member-name-link">getInAreaTarget</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Gets the target state in the current area, using the offset from the area as well as the in area target offset.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</code></td><td><code><a href="#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">getInBlockTarget</a><wbr>(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,<br> net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</code></td><td><div class="block">Gets the target state in the current area, using the in area block position offset as well as the in block target offset to calculate the in area offset for setting.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInAreaTarget(net.minecraft.world.phys.Vec3)">

:::tabs
== getInAreaTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</span>&nbsp;<span class="element-name">getInAreaTarget</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</span></div>
Gets the target state in the current area, using the offset from the area as well as the in area target offset.
Note if this accessor potentially targets more than 1 block position (even if it does not in reality the potential is what matters here)
you will need to pass in the world position exactly.
If this accessor can not potentially ever target more than 1 block position, you can pass in the relative position.
This is a nasty implementation detail, and matters most when you are making new chisel or pattern placement modes!
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inAreaTarget</code> - The in area offset.</dd>
<dt>Returns:</dt>
<dd>An optional potentially containing the state entry of the requested target.</dd>
</dl>
</div>
:::


</section>

<section id="getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">

:::tabs
== getInBlockTarget
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;</span>&nbsp;<span class="element-name">getInBlockTarget</span><wbr><span class="parameters">(net.minecraft.core.BlockPos&nbsp;inAreaBlockPosOffset,
 net.minecraft.world.phys.Vec3&nbsp;inBlockTarget)</span></div>
Gets the target state in the current area, using the in area block position offset as well as the in block target offset to calculate the in area offset for setting.
Note if this accessor potentially targets more than 1 block position (even if it does not in reality the potential is what matters here)
you will need to pass in the world position exactly.
If this accessor can not potentially ever target more than 1 block position, you can pass in the relative position.
This is a nasty implementation detail, and matters most when you are making new chisel or pattern placement modes!
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inAreaBlockPosOffset</code> - The offset of blocks in the current area.</dd>
<dd><code>inBlockTarget</code> - The offset in the targeted block.</dd>
<dt>Returns:</dt>
<dd>An optional potentially containing the state entry of the requested target.</dd>
</dl>
</div>
:::


</section>

:::::
  

