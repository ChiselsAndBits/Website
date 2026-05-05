--- 
title: IPermissionChecker
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.permissions](index.md)  
# Interface IPermissionChecker  
**Functional Interface:**  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.  

---
<div class="type-signature"><span class="annotations"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang" class="external-link">@FunctionalInterface</a><br/>  
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IPermissionChecker</span></div>  

  

Represents a permission checker, which can indicate if a particular
area is allowed to be edited or not.

If at least one checker registered to the handler prevents the edit,
then the edit is not allowed.  

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
  <tr><td><code>boolean</code></td><td><code><a href="#isAllowed(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">isAllowed</a><wbr>(@Nullable net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isAllowed(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">isAllowed</a><wbr>(@Nullable net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#isAllowed(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">isAllowed</a><wbr>(@Nullable net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
</section>
</li>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="isAllowed(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)">

:::tabs
== isAllowed
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isAllowed</span><wbr><span class="parameters">(@Nullable
 @Nullable net.minecraft.world.entity.player.Player&nbsp;player,
 <a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - </dd>
<dd><code>worldAreaAccessor</code> - </dd>
<dt>Returns:</dt>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

