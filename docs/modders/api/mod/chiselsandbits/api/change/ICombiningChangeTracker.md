--- 
title: ICombiningChangeTracker
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.change](index.md)  
# Interface ICombiningChangeTracker  
**All Extended Interfaces:**  
AutoCloseable, [IChangeHandler](../changes/IChangeHandler.md), [IChangeTracker](IChangeTracker.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ICombiningChangeTracker</span><span class="extends-implements"><br/>  
extends <a href="IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang" class="external-link">AutoCloseable</a></span></div>  

  

<div class="block">Represents a change tracker which is used to combine several change steps into one action.
 Use with a try-with-resources block.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang" class="external-link">AutoCloseable</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close()" title="class or interface in java.lang" class="external-link">close</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.change.changes.<a href="changes/IChangeHandler.html" title="interface in mod.chiselsandbits.api.change.changes">IChangeHandler</a>
<a href="changes/IChangeHandler.html#canRedo(net.minecraft.world.entity.player.Player)">canRedo</a>, <a href="changes/IChangeHandler.html#canUndo(net.minecraft.world.entity.player.Player)">canUndo</a>, <a href="changes/IChangeHandler.html#redo(net.minecraft.world.entity.player.Player)">redo</a>, <a href="changes/IChangeHandler.html#undo(net.minecraft.world.entity.player.Player)">undo</a>
:::::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;mod.chiselsandbits.api.change.<a href="IChangeTracker.html" title="interface in mod.chiselsandbits.api.change">IChangeTracker</a>
<a href="IChangeTracker.html#clear()">clear</a>, <a href="IChangeTracker.html#getChanges()">getChanges</a>, <a href="IChangeTracker.html#onBlocksUpdated(java.util.Map,java.util.Map)">onBlocksUpdated</a>, <a href="IChangeTracker.html#onBlockUpdated(net.minecraft.core.BlockPos,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot,mod.chiselsandbits.api.multistate.snapshot.IMultiStateSnapshot)">onBlockUpdated</a>, <a href="IChangeTracker.html#setChanges(java.util.Deque)">setChanges</a>
:::::
:::::::
  
  
  

  

  

  

  

  

  

