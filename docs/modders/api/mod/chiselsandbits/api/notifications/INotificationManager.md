--- 
title: INotificationManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.notifications](index.md)  
# Interface INotificationManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">INotificationManager</span></div>  

  

Manager which handles notifying players of events in the game.  

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
  <tr><td><code>static <a href="INotificationManager.html" title="interface in mod.chiselsandbits.api.notifications">INotificationManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The current instance of the notification manager.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#notify(mod.chiselsandbits.api.notifications.INotification)" class="member-name-link">notify</a><wbr>(<a href="INotification.html" title="interface in mod.chiselsandbits.api.notifications">INotification</a>&nbsp;notification)</code></td><td><div class="block">Notifies the player with the given notification.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#notify(net.minecraft.resources.Identifier,net.minecraft.network.chat.Component)" class="member-name-link">notify</a><wbr>(net.minecraft.resources.Identifier&nbsp;icon,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Notifies the player with a simple message and icon.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#notify(net.minecraft.resources.Identifier,net.minecraft.world.phys.Vec3,net.minecraft.network.chat.Component)" class="member-name-link">notify</a><wbr>(net.minecraft.resources.Identifier&nbsp;icon,<br> net.minecraft.world.phys.Vec3&nbsp;color,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Notifies the player with a simple message, icon and color.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="INotificationManager.html" title="interface in mod.chiselsandbits.api.notifications">INotificationManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The current instance of the notification manager.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#notify(mod.chiselsandbits.api.notifications.INotification)" class="member-name-link">notify</a><wbr>(<a href="INotification.html" title="interface in mod.chiselsandbits.api.notifications">INotification</a>&nbsp;notification)</code></td><td><div class="block">Notifies the player with the given notification.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#notify(net.minecraft.resources.Identifier,net.minecraft.network.chat.Component)" class="member-name-link">notify</a><wbr>(net.minecraft.resources.Identifier&nbsp;icon,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Notifies the player with a simple message and icon.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#notify(net.minecraft.resources.Identifier,net.minecraft.world.phys.Vec3,net.minecraft.network.chat.Component)" class="member-name-link">notify</a><wbr>(net.minecraft.resources.Identifier&nbsp;icon,<br> net.minecraft.world.phys.Vec3&nbsp;color,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Notifies the player with a simple message, icon and color.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#notify(mod.chiselsandbits.api.notifications.INotification)" class="member-name-link">notify</a><wbr>(<a href="INotification.html" title="interface in mod.chiselsandbits.api.notifications">INotification</a>&nbsp;notification)</code></td><td><div class="block">Notifies the player with the given notification.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default void</code></td><td><code><a href="#notify(net.minecraft.resources.Identifier,net.minecraft.network.chat.Component)" class="member-name-link">notify</a><wbr>(net.minecraft.resources.Identifier&nbsp;icon,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Notifies the player with a simple message and icon.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#notify(net.minecraft.resources.Identifier,net.minecraft.world.phys.Vec3,net.minecraft.network.chat.Component)" class="member-name-link">notify</a><wbr>(net.minecraft.resources.Identifier&nbsp;icon,<br> net.minecraft.world.phys.Vec3&nbsp;color,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Notifies the player with a simple message, icon and color.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="INotificationManager.html" title="interface in mod.chiselsandbits.api.notifications">INotificationManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
The current instance of the notification manager.
<dl class="notes">
<dt>Returns:</dt>
<dd>The notification manager.</dd>
</dl>
:::


</section>

<section id="notify(net.minecraft.resources.Identifier,net.minecraft.world.phys.Vec3,net.minecraft.network.chat.Component)">

:::tabs
== notify
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">notify</span><wbr><span class="parameters">(net.minecraft.resources.Identifier&nbsp;icon,
 net.minecraft.world.phys.Vec3&nbsp;color,
 net.minecraft.network.chat.Component&nbsp;message)</span></div>
Notifies the player with a simple message, icon and color.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - The icon to display.</dd>
<dd><code>color</code> - The color of the icon.</dd>
<dd><code>message</code> - The message to display.</dd>
</dl>
:::


</section>

<section id="notify(net.minecraft.resources.Identifier,net.minecraft.network.chat.Component)">

:::tabs
== notify
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">notify</span><wbr><span class="parameters">(net.minecraft.resources.Identifier&nbsp;icon,
 net.minecraft.network.chat.Component&nbsp;message)</span></div>
Notifies the player with a simple message and icon.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - The icon to display.</dd>
<dd><code>message</code> - The message to display.</dd>
</dl>
:::


</section>

<section id="notify(mod.chiselsandbits.api.notifications.INotification)">

:::tabs
== notify
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">notify</span><wbr><span class="parameters">(<a href="INotification.html" title="interface in mod.chiselsandbits.api.notifications">INotification</a>&nbsp;notification)</span></div>
Notifies the player with the given notification.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - The notification to display.</dd>
</dl>
:::


</section>

:::::
  

