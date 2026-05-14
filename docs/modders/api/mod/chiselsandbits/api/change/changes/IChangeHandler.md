--- 
title: IChangeHandler
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.change.changes](index.md)  
# Interface IChangeHandler  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChangeHandler</span></div>  

  

Represents an entry point for a change that can be undone and redone.  

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
  <tr><td><code>boolean</code></td><td><code><a href="#canRedo(net.minecraft.world.entity.player.Player)" class="member-name-link">canRedo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Checks if the change can still be redone.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canUndo(net.minecraft.world.entity.player.Player)" class="member-name-link">canUndo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Checks if the change can still be undone.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#redo(net.minecraft.world.entity.player.Player)" class="member-name-link">redo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Redoes the change</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#undo(net.minecraft.world.entity.player.Player)" class="member-name-link">undo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Undoes the change.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canRedo(net.minecraft.world.entity.player.Player)" class="member-name-link">canRedo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Checks if the change can still be redone.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canUndo(net.minecraft.world.entity.player.Player)" class="member-name-link">canUndo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Checks if the change can still be undone.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#redo(net.minecraft.world.entity.player.Player)" class="member-name-link">redo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Redoes the change</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#undo(net.minecraft.world.entity.player.Player)" class="member-name-link">undo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Undoes the change.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canRedo(net.minecraft.world.entity.player.Player)" class="member-name-link">canRedo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Checks if the change can still be redone.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canUndo(net.minecraft.world.entity.player.Player)" class="member-name-link">canUndo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Checks if the change can still be undone.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#redo(net.minecraft.world.entity.player.Player)" class="member-name-link">redo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Redoes the change</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#undo(net.minecraft.world.entity.player.Player)" class="member-name-link">undo</a><wbr>(net.minecraft.world.entity.player.Player&nbsp;player)</code></td><td><div class="block">Undoes the change.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="canUndo(net.minecraft.world.entity.player.Player)">
:::tabs
== canUndo
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">canUndo</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player)</span></div>
Checks if the change can still be undone.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The player for which the can undo check is performed.</dd>
<dt>Returns:</dt>
<dd>True when the change can be undone.</dd>
</dl>
</div>
:::
</section>
<section id="canRedo(net.minecraft.world.entity.player.Player)">
:::tabs
== canRedo
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">canRedo</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player)</span></div>
Checks if the change can still be redone.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The player for which the can redo check is performed.</dd>
<dt>Returns:</dt>
<dd>True when the change can be redone.</dd>
</dl>
</div>
:::
</section>
<section id="undo(net.minecraft.world.entity.player.Player)">
:::tabs
== undo
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">undo</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player)</span>
   throws <span class="exceptions"><a href="IllegalChangeAttempt.html" title="class in mod.chiselsandbits.api.change.changes">IllegalChangeAttempt</a></span></div>
Undoes the change.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The player for which undoes the change.</dd>
<dt>Throws:</dt>
<dd><code><a href="IllegalChangeAttempt.html" title="class in mod.chiselsandbits.api.change.changes">IllegalChangeAttempt</a></code> - when the change can not be undone.</dd>
</dl>
</div>
:::
</section>
<section id="redo(net.minecraft.world.entity.player.Player)">
:::tabs
== redo
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">redo</span><wbr><span class="parameters">(net.minecraft.world.entity.player.Player&nbsp;player)</span>
   throws <span class="exceptions"><a href="IllegalChangeAttempt.html" title="class in mod.chiselsandbits.api.change.changes">IllegalChangeAttempt</a></span></div>
Redoes the change
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>player</code> - The player for which redoes the change.</dd>
<dt>Throws:</dt>
<dd><code><a href="IllegalChangeAttempt.html" title="class in mod.chiselsandbits.api.change.changes">IllegalChangeAttempt</a></code> - when the change can not be redone.</dd>
</dl>
</div>
:::
</section>
:::::
  

