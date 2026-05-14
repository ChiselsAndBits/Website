--- 
title: IPermissionHandler
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.permissions](index.md)  
# Interface IPermissionHandler  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IPermissionHandler</span></div>  

  

Permission handler for checking if a particular user can manipulate a particular area.  

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
  <tr><td><code>boolean</code></td><td><code><a href="#canManipulate(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">canManipulate</a><wbr>(@NotNull net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td><div class="block">Allows for external systems to check if a particular player<br>can edit a particular area.</div><br></td></tr>
  <tr><td><code>static <a href="IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionHandler</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current permission handler.</div><br></td></tr>
  <tr><td><code><a href="ICheckerRegistration.html" title="interface in mod.chiselsandbits.api.permissions">ICheckerRegistration</a></code></td><td><code><a href="#registerChecker(mod.chiselsandbits.api.permissions.IPermissionChecker)" class="member-name-link">registerChecker</a><wbr>(<a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionChecker</a>&nbsp;checker)</code></td><td><div class="block">Registers a new <a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions"><code>IPermissionChecker</code></a> with the permission handler.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionHandler</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">Gives access to the current permission handler.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canManipulate(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">canManipulate</a><wbr>(@NotNull net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td><div class="block">Allows for external systems to check if a particular player<br>can edit a particular area.</div><br></td></tr>
  <tr><td><code><a href="ICheckerRegistration.html" title="interface in mod.chiselsandbits.api.permissions">ICheckerRegistration</a></code></td><td><code><a href="#registerChecker(mod.chiselsandbits.api.permissions.IPermissionChecker)" class="member-name-link">registerChecker</a><wbr>(<a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionChecker</a>&nbsp;checker)</code></td><td><div class="block">Registers a new <a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions"><code>IPermissionChecker</code></a> with the permission handler.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canManipulate(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)" class="member-name-link">canManipulate</a><wbr>(@NotNull net.minecraft.world.entity.player.Player&nbsp;player,<br> <a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</code></td><td><div class="block">Allows for external systems to check if a particular player<br>can edit a particular area.</div><br></td></tr>
  <tr><td><code><a href="ICheckerRegistration.html" title="interface in mod.chiselsandbits.api.permissions">ICheckerRegistration</a></code></td><td><code><a href="#registerChecker(mod.chiselsandbits.api.permissions.IPermissionChecker)" class="member-name-link">registerChecker</a><wbr>(<a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionChecker</a>&nbsp;checker)</code></td><td><div class="block">Registers a new <a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions"><code>IPermissionChecker</code></a> with the permission handler.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">
:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionHandler</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
Gives access to the current permission handler.
<dl class="notes">
<dt>Returns:</dt>
<dd>The current permission handler.</dd>
</dl>
</div>
:::
</section>
<section id="registerChecker(mod.chiselsandbits.api.permissions.IPermissionChecker)">
:::tabs
== registerChecker
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="ICheckerRegistration.html" title="interface in mod.chiselsandbits.api.permissions">ICheckerRegistration</a></span>&nbsp;<span class="element-name">registerChecker</span><wbr><span class="parameters">(<a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions">IPermissionChecker</a>&nbsp;checker)</span></div>
Registers a new <a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions"><code>IPermissionChecker</code></a> with the permission handler.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>checker</code> - The new permission checker</dd>
<dt>Returns:</dt>
<dd>The registration token which can be used to unregister the checker.</dd>
</dl>
</div>
:::
</section>
<section id="canManipulate(net.minecraft.world.entity.player.Player,mod.chiselsandbits.api.multistate.accessor.world.IWorldAreaAccessor)">
:::tabs
== canManipulate
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">canManipulate</span><wbr><span class="parameters">(@NotNull
 @NotNull net.minecraft.world.entity.player.Player&nbsp;player,
 <a href="../multistate/accessor/world/IWorldAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor.world">IWorldAreaAccessor</a>&nbsp;worldAreaAccessor)</span></div>
Allows for external systems to check if a particular player
can edit a particular area.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The player which wants to edit the area, possibly null if the player is not known.</dd>
<dd><code>worldAreaAccessor</code> - The area which is being edited.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the area is marked as editable, <code>false</code> otherwise.</dd>
</dl>
</div>
:::
</section>
:::::
  

