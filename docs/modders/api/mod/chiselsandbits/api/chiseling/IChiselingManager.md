--- 
title: IChiselingManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling](index.md)  
# Interface IChiselingManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselingManager</span></div>  

  

  

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
  <tr><td><code><a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#create(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation,boolean,net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus,<br> boolean&nbsp;simulation,<br> net.minecraft.world.item.ItemStack&nbsp;causingItemStack)</code></td><td><div class="block">Creates a new context for a given player.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode)" class="member-name-link">get</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode)</code></td><td><div class="block">Gives access to the chiseling context of the player, if it exists.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">get</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus)</code></td><td><div class="block">Gives access to the chiseling context of the player, if it exists.</div><br></td></tr>
  <tr><td><code>static <a href="IChiselingManager.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>default <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#getOrCreateContext(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation,boolean,net.minecraft.world.item.ItemStack)" class="member-name-link">getOrCreateContext</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus,<br> boolean&nbsp;simulation,<br> net.minecraft.world.item.ItemStack&nbsp;causingItemStack)</code></td><td><div class="block">Gets or creates a new chiseling context for the given player.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IChiselingManager.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#create(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation,boolean,net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus,<br> boolean&nbsp;simulation,<br> net.minecraft.world.item.ItemStack&nbsp;causingItemStack)</code></td><td><div class="block">Creates a new context for a given player.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode)" class="member-name-link">get</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode)</code></td><td><div class="block">Gives access to the chiseling context of the player, if it exists.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">get</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus)</code></td><td><div class="block">Gives access to the chiseling context of the player, if it exists.</div><br></td></tr>
  <tr><td><code>default <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#getOrCreateContext(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation,boolean,net.minecraft.world.item.ItemStack)" class="member-name-link">getOrCreateContext</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus,<br> boolean&nbsp;simulation,<br> net.minecraft.world.item.ItemStack&nbsp;causingItemStack)</code></td><td><div class="block">Gets or creates a new chiseling context for the given player.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#create(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation,boolean,net.minecraft.world.item.ItemStack)" class="member-name-link">create</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus,<br> boolean&nbsp;simulation,<br> net.minecraft.world.item.ItemStack&nbsp;causingItemStack)</code></td><td><div class="block">Creates a new context for a given player.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode)" class="member-name-link">get</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode)</code></td><td><div class="block">Gives access to the chiseling context of the player, if it exists.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</code></td><td><code><a href="#get(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation)" class="member-name-link">get</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus)</code></td><td><div class="block">Gives access to the chiseling context of the player, if it exists.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#getOrCreateContext(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation,boolean,net.minecraft.world.item.ItemStack)" class="member-name-link">getOrCreateContext</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,<br> <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus,<br> boolean&nbsp;simulation,<br> net.minecraft.world.item.ItemStack&nbsp;causingItemStack)</code></td><td><div class="block">Gets or creates a new chiseling context for the given player.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IChiselingManager.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
</div>
:::


</section>

<section id="getOrCreateContext(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation,boolean,net.minecraft.world.item.ItemStack)">

:::tabs
== getOrCreateContext
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></span>&nbsp;<span class="element-name">getOrCreateContext</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,
 <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus,
 boolean&nbsp;simulation,
 net.minecraft.world.item.ItemStack&nbsp;causingItemStack)</span></div>
Gets or creates a new chiseling context for the given player.
A new context is created when either one of the following conditions is met:
 - No context has been created before.
 - The world of the player and the world of the existing context are not equal
 - The new chisel mode and the chisel mode of the existing context are not equal.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player for which the context is looked up.</dd>
<dd><code>mode</code> - The mode which the player wants to chisel in.</dd>
<dd><code>modeOfOperandus</code> - The mode of operation for the current context.</dd>
<dd><code>simulation</code> - Indicates if the context should be created as a simulation context if it does not exist. If the context does not exist, a simulation context is not stored in the manager. A simulation context will also be a snapshot of the current context if one already exists.</dd>
<dd><code>causingItemStack</code> - The stack that triggered the chiseling operation.</dd>
<dt>Returns:</dt>
<dd>The context.</dd>
</dl>
</div>
:::


</section>

<section id="get(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode)">

:::tabs
== get
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode)</span></div>
Gives access to the chiseling context of the player, if it exists.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player for which the context is looked up.</dd>
<dd><code>mode</code> - The mode which the player wants to chisel in</dd>
<dt>Returns:</dt>
<dd>An optional potentially containing the current context of the player.</dd>
</dl>
</div>
:::


</section>

<section id="get(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation)">

:::tabs
== get
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a>&gt;</span>&nbsp;<span class="element-name">get</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,
 <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus)</span></div>
Gives access to the chiseling context of the player, if it exists.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player for which the context is looked up.</dd>
<dd><code>mode</code> - The mode which the player wants to chisel in.</dd>
<dd><code>modeOfOperandus</code> - The mode of operation for the current context.</dd>
<dt>Returns:</dt>
<dd>An optional potentially containing the current context of the player.</dd>
</dl>
</div>
:::


</section>

<section id="create(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.chiseling.mode.IChiselMode,mod.chiselsandbits.api.chiseling.ChiselingOperation,boolean,net.minecraft.world.item.ItemStack)">

:::tabs
== create
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a>&nbsp;mode,
 <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a>&nbsp;modeOfOperandus,
 boolean&nbsp;simulation,
 net.minecraft.world.item.ItemStack&nbsp;causingItemStack)</span></div>
Creates a new context for a given player.
If <code>simulate</code> is false and an a context for the player already exists, then that context is overriden.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player for which the context is created.</dd>
<dd><code>mode</code> - The mode which the player wants to chisel in.</dd>
<dd><code>modeOfOperandus</code> - The mode of operation for the current context.</dd>
<dd><code>simulation</code> - Indicates if the context is used in contextual simulation. <code>true</code>, prevents overriding of the current context and also does not save the context in the manager.</dd>
<dd><code>causingItemStack</code> - The stack that triggered the chiseling operation.</dd>
<dt>Returns:</dt>
<dd>The newly created context.</dd>
</dl>
</div>
:::


</section>

:::::
  

