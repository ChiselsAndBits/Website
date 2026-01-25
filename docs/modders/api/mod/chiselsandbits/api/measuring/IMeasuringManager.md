--- 
title: IMeasuringManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.measuring](index.md)  
# Interface IMeasuringManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IMeasuringManager</span></div>  

  

A manager for dealing with measurements made by different players in different worlds.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a></code></td><td><code><a href="#create(net.minecraft.world.level.Level,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction,mod.chiselsandbits.api.measuring.IMeasuringMode)" class="member-name-link">create</a><wbr>(net.minecraft.world.level.Level&nbsp;world,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to,<br> net.minecraft.core.Direction&nbsp;hitFace,<br> <a href="IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a>&nbsp;mode)</code></td><td><div class="block">Creates a new measurement for the given player in the given world.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getForPlayer(java.util.UUID)" class="member-name-link">getForPlayer</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a>&nbsp;playerId)</code></td><td><div class="block">Determines the active measurements for a given player represented by his unique UUID.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getForPlayer(net.minecraft.world.entity.player.Player)" class="member-name-link">getForPlayer</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Determines the active measurements for a given player.</div><br></td></tr>
  <tr><td><code>static <a href="IMeasuringManager.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getInWorld(net.minecraft.resources.Identifier)" class="member-name-link">getInWorld</a><wbr>(net.minecraft.resources.Identifier&nbsp;worldKey)</code></td><td><div class="block">Determines the active measurements in a given world which is identified by the given world key.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getInWorld(net.minecraft.world.level.Level)" class="member-name-link">getInWorld</a><wbr>(net.minecraft.world.level.Level&nbsp;world)</code></td><td><div class="block">Determines the active measurements in a given world.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#resetMeasurementsFor(java.util.UUID)" class="member-name-link">resetMeasurementsFor</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a>&nbsp;playerId)</code></td><td><div class="block">Resets all measurements for a given player represented by the given id.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#resetMeasurementsFor(net.minecraft.world.entity.player.Player)" class="member-name-link">resetMeasurementsFor</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Resets all measurements for a given player.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IMeasuringManager.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a></code></td><td><code><a href="#create(net.minecraft.world.level.Level,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction,mod.chiselsandbits.api.measuring.IMeasuringMode)" class="member-name-link">create</a><wbr>(net.minecraft.world.level.Level&nbsp;world,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to,<br> net.minecraft.core.Direction&nbsp;hitFace,<br> <a href="IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a>&nbsp;mode)</code></td><td><div class="block">Creates a new measurement for the given player in the given world.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getForPlayer(java.util.UUID)" class="member-name-link">getForPlayer</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a>&nbsp;playerId)</code></td><td><div class="block">Determines the active measurements for a given player represented by his unique UUID.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getForPlayer(net.minecraft.world.entity.player.Player)" class="member-name-link">getForPlayer</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Determines the active measurements for a given player.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getInWorld(net.minecraft.resources.Identifier)" class="member-name-link">getInWorld</a><wbr>(net.minecraft.resources.Identifier&nbsp;worldKey)</code></td><td><div class="block">Determines the active measurements in a given world which is identified by the given world key.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getInWorld(net.minecraft.world.level.Level)" class="member-name-link">getInWorld</a><wbr>(net.minecraft.world.level.Level&nbsp;world)</code></td><td><div class="block">Determines the active measurements in a given world.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#resetMeasurementsFor(java.util.UUID)" class="member-name-link">resetMeasurementsFor</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a>&nbsp;playerId)</code></td><td><div class="block">Resets all measurements for a given player represented by the given id.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#resetMeasurementsFor(net.minecraft.world.entity.player.Player)" class="member-name-link">resetMeasurementsFor</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Resets all measurements for a given player.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a></code></td><td><code><a href="#create(net.minecraft.world.level.Level,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction,mod.chiselsandbits.api.measuring.IMeasuringMode)" class="member-name-link">create</a><wbr>(net.minecraft.world.level.Level&nbsp;world,<br> net.minecraft.world.entity.player.Player&nbsp;playerEntity,<br> net.minecraft.world.phys.Vec3&nbsp;from,<br> net.minecraft.world.phys.Vec3&nbsp;to,<br> net.minecraft.core.Direction&nbsp;hitFace,<br> <a href="IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a>&nbsp;mode)</code></td><td><div class="block">Creates a new measurement for the given player in the given world.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getForPlayer(java.util.UUID)" class="member-name-link">getForPlayer</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a>&nbsp;playerId)</code></td><td><div class="block">Determines the active measurements for a given player represented by his unique UUID.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getInWorld(net.minecraft.resources.Identifier)" class="member-name-link">getInWorld</a><wbr>(net.minecraft.resources.Identifier&nbsp;worldKey)</code></td><td><div class="block">Determines the active measurements in a given world which is identified by the given world key.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#resetMeasurementsFor(java.util.UUID)" class="member-name-link">resetMeasurementsFor</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a>&nbsp;playerId)</code></td><td><div class="block">Resets all measurements for a given player represented by the given id.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getForPlayer(net.minecraft.world.entity.player.Player)" class="member-name-link">getForPlayer</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Determines the active measurements for a given player.</div><br></td></tr>
  <tr><td><code>default <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</code></td><td><code><a href="#getInWorld(net.minecraft.world.level.Level)" class="member-name-link">getInWorld</a><wbr>(net.minecraft.world.level.Level&nbsp;world)</code></td><td><div class="block">Determines the active measurements in a given world.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#resetMeasurementsFor(net.minecraft.world.entity.player.Player)" class="member-name-link">resetMeasurementsFor</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</code></td><td><div class="block">Resets all measurements for a given player.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IMeasuringManager.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getInWorld(net.minecraft.world.level.Level)">

:::tabs
== getInWorld
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</span>&nbsp;<span class="element-name">getInWorld</span><wbr><span class="parameters">(net.minecraft.world.level.Level&nbsp;world)</span></div>
Determines the active measurements in a given world.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world in question.</dd>
<dt>Returns:</dt>
<dd>A collection of measurements which are active in the given world.</dd>
</dl>
:::


</section>

<section id="getInWorld(net.minecraft.resources.Identifier)">

:::tabs
== getInWorld
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</span>&nbsp;<span class="element-name">getInWorld</span><wbr><span class="parameters">(net.minecraft.resources.Identifier&nbsp;worldKey)</span></div>
Determines the active measurements in a given world which is identified by the given world key.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>worldKey</code> - The world key in question.</dd>
<dt>Returns:</dt>
<dd>A collection of measurements which are active in the given world.</dd>
</dl>
:::


</section>

<section id="getForPlayer(net.minecraft.world.entity.player.Player)">

:::tabs
== getForPlayer
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</span>&nbsp;<span class="element-name">getForPlayer</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</span></div>
Determines the active measurements for a given player.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player in question.</dd>
<dt>Returns:</dt>
<dd>A collection of measurements which are active for the given player.</dd>
</dl>
:::


</section>

<section id="getForPlayer(java.util.UUID)">

:::tabs
== getForPlayer
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;? extends <a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a>&gt;</span>&nbsp;<span class="element-name">getForPlayer</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a>&nbsp;playerId)</span></div>
Determines the active measurements for a given player represented by his unique UUID.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerId</code> - The if of the player in question.</dd>
<dt>Returns:</dt>
<dd>A collection of measurements which are active for the given player.</dd>
</dl>
:::


</section>

<section id="create(net.minecraft.world.level.Level,net.minecraft.world.entity.player.Player,net.minecraft.world.phys.Vec3,net.minecraft.world.phys.Vec3,net.minecraft.core.Direction,mod.chiselsandbits.api.measuring.IMeasuringMode)">

:::tabs
== create
<div class="member-signature"><span class="return-type"><a href="IMeasurement.html" title="interface in mod.chiselsandbits.api.measuring">IMeasurement</a></span>&nbsp;<span class="element-name">create</span><wbr><span class="parameters">(net.minecraft.world.level.Level&nbsp;world,
 net.minecraft.world.entity.player.Player&nbsp;playerEntity,
 net.minecraft.world.phys.Vec3&nbsp;from,
 net.minecraft.world.phys.Vec3&nbsp;to,
 net.minecraft.core.Direction&nbsp;hitFace,
 <a href="IMeasuringMode.html" title="interface in mod.chiselsandbits.api.measuring">IMeasuringMode</a>&nbsp;mode)</span></div>
Creates a new measurement for the given player in the given world.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>world</code> - The world to create the measurement in.</dd>
<dd><code>playerEntity</code> - The player to create the given measurement for.</dd>
<dd><code>from</code> - The start-point of the measurement.</dd>
<dd><code>to</code> - The end-point of the measurement.</dd>
<dd><code>hitFace</code> - </dd>
<dd><code>mode</code> - The measurement mode.</dd>
<dt>Returns:</dt>
<dd>The newly created and processed measurement.</dd>
</dl>
:::


</section>

<section id="resetMeasurementsFor(net.minecraft.world.entity.player.Player)">

:::tabs
== resetMeasurementsFor
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">resetMeasurementsFor</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;playerEntity)</span></div>
Resets all measurements for a given player. (Removing them from the game and memory).
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerEntity</code> - The player to remove the measurements for.</dd>
</dl>
:::


</section>

<section id="resetMeasurementsFor(java.util.UUID)">

:::tabs
== resetMeasurementsFor
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">resetMeasurementsFor</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util" class="external-link">UUID</a>&nbsp;playerId)</span></div>
Resets all measurements for a given player represented by the given id. (Removing them from the game and memory).
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>playerId</code> - The id of the player to remove the measurements for.</dd>
</dl>
:::


</section>

:::::
  

