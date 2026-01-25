--- 
title: InventoryUtils
aside: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class InventoryUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.InventoryUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">InventoryUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static void</code></td><td><code><a href="#extractChiseledStackMatchingSnapshot(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">extractChiseledStackMatchingSnapshot</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;snapshot)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.item.ItemStack</code></td><td><code><a href="#getChiseledStackMatchingSnapshot(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">getChiseledStackMatchingSnapshot</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;snapshot)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static void</code></td><td><code><a href="#extractChiseledStackMatchingSnapshot(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">extractChiseledStackMatchingSnapshot</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;snapshot)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.item.ItemStack</code></td><td><code><a href="#getChiseledStackMatchingSnapshot(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">getChiseledStackMatchingSnapshot</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;snapshot)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static void</code></td><td><code><a href="#extractChiseledStackMatchingSnapshot(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">extractChiseledStackMatchingSnapshot</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;snapshot)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.item.ItemStack</code></td><td><code><a href="#getChiseledStackMatchingSnapshot(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)" class="member-name-link">getChiseledStackMatchingSnapshot</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;snapshot)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getChiseledStackMatchingSnapshot(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)">

:::tabs
== getChiseledStackMatchingSnapshot
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">getChiseledStackMatchingSnapshot</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player,
 <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;snapshot)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="extractChiseledStackMatchingSnapshot(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)">

:::tabs
== extractChiseledStackMatchingSnapshot
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">extractChiseledStackMatchingSnapshot</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player,
 <a href="../multistate/snapshot/IMultiStateSnapshot.html" title="interface in mod.chiselsandbits.api.multistate.snapshot">IMultiStateSnapshot</a>&nbsp;snapshot)</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

