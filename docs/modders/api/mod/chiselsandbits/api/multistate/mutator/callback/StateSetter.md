--- 
title: StateSetter
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.multistate.mutator.callback](index.md)  
# Interface StateSetter  
**Functional Interface:**  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang" class="external-link">@FunctionalInterface</a><br/>  
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">StateSetter</span></div>  

  

Functional callback interface for setting the state of a bit.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#set(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">set</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Sets the block information of the targeted bit to the given block information.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#set(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">set</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Sets the block information of the targeted bit to the given block information.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#set(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)" class="member-name-link">set</a><wbr>(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</code></td><td><div class="block">Sets the block information of the targeted bit to the given block information.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="set(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.phys.Vec3)">

:::tabs
== set
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">set</span><wbr><span class="parameters">(<a href="../../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 net.minecraft.world.phys.Vec3&nbsp;inAreaTarget)</span>
  throws <span class="exceptions"><a href="../../../exceptions/SpaceOccupiedException.html" title="class in mod.chiselsandbits.api.exceptions">SpaceOccupiedException</a></span></div>
Sets the block information of the targeted bit to the given block information.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information to set the bit to.</dd>
<dd><code>inAreaTarget</code> - The target area.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../../exceptions/SpaceOccupiedException.html" title="class in mod.chiselsandbits.api.exceptions">SpaceOccupiedException</a></code> - If the target area is occupied.</dd>
</dl>
:::


</section>

:::::
  

