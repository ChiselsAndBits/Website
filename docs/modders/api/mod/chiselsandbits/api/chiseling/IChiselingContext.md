--- 
title: IChiselingContext
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.chiseling](index.md)  
# Interface IChiselingContext  
**All Extended Interfaces:**  
[IStateAccessor](../multistate/accessor/IStateAccessor.md)  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IChiselingContext</span><span class="extends-implements"><br/>  
extends <a href="../multistate/accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a></span></div>  

  

The current context for the running chiseling operation.  

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
  <tr><td><code>void</code></td><td><code><a href="#clearStateFilter()" class="member-name-link">clearStateFilter</a>()</code></td><td><div class="block">Clears the state filter which is applied to the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> for this context.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td><div class="block">Creates a deep copy of the context, so that the copy can be modified, without modifying this instance.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.network.chat.MutableComponent&gt;</code></td><td><code><a href="#getError()" class="member-name-link">getError</a>()</code></td><td><div class="block">Returns the error message that is displayed when the chiseling operation fails.</div><br></td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;T&gt;</code></td><td><code><a href="#getMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)" class="member-name-link">getMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;T&gt;&nbsp;key)</code></td><td><div class="block">Allows the storage of metadata on the context.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></code></td><td><code><a href="#getMode()" class="member-name-link">getMode</a>()</code></td><td><div class="block">Returns the current <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode"><code>IChiselMode</code></a> for which this context is valid.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></code></td><td><code><a href="#getModeOfOperandus()" class="member-name-link">getModeOfOperandus</a>()</code></td><td><div class="block">Indicates what kind of chiseling operation this context was created for.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a>&gt;</code></td><td><code><a href="#getMutator()" class="member-name-link">getMutator</a>()</code></td><td><div class="block">Returns the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> if there is one.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&gt;&gt;</code></td><td><code><a href="#getStateFilter()" class="member-name-link">getStateFilter</a>()</code></td><td><div class="block">Returns the filter that is currently applied on the context.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.level.LevelAccessor</code></td><td><code><a href="#getWorld()" class="member-name-link">getWorld</a>()</code></td><td><div class="block">The <code>LevelAccessor</code> in which the current chiseling context is valid.</div><br></td></tr>
  <tr><td><code>default @NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#include(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">include</a><wbr>(net.minecraft.core.BlockPos&nbsp;inWorldPosition,<br> net.minecraft.world.phys.Vec3&nbsp;relativeInBlockPosition)</code></td><td><div class="block">Includes the given exact position in the world of this context, retrievable via <a href="#getWorld()"><code>getWorld()</code></a>, in<br>the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#include(net.minecraft.world.phys.Vec3)" class="member-name-link">include</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;worldPosition)</code></td><td><div class="block">Includes the given exact position in the world of this context, retrievable via <a href="#getWorld()"><code>getWorld()</code></a>, in<br>the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isComplete()" class="member-name-link">isComplete</a>()</code></td><td><div class="block">Indicates if the context is completed or not.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isSimulation()" class="member-name-link">isSimulation</a>()</code></td><td><div class="block">Indicates if the current context that is being executed is supposed to be a simulation.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)" class="member-name-link">removeMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;?&gt;&nbsp;key)</code></td><td><div class="block">Removes the metadata from the context.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#resetMutator()" class="member-name-link">resetMutator</a>()</code></td><td><div class="block">Resets the mutator that is used to handle the current selected area.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setComplete()" class="member-name-link">setComplete</a>()</code></td><td><div class="block">Marks the current context as complete, so that it can not be reused for interactions which<br>will follow this one.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setError(net.minecraft.network.chat.MutableComponent)" class="member-name-link">setError</a><wbr>(net.minecraft.network.chat.MutableComponent&nbsp;errorText)</code></td><td><div class="block">Sets the error message that is displayed when the chiseling operation fails.</div><br></td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;void</code></td><td><code><a href="#setMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey,T)" class="member-name-link">setMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;T&gt;&nbsp;key,<br> T&nbsp;value)</code></td><td><div class="block">Allows for the setting of the metadata on the context.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setStateFilter(java.util.function.Function)" class="member-name-link">setStateFilter</a><wbr>(@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&gt;&nbsp;filterBuilder)</code></td><td><div class="block">Allows for the setting of a filterBuilder on the context, which limits which <a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IStateEntryInfo</code></a> are returned from<br>the relevant accessor methods of the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>, as well as which limits the setter methods on the same <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a><br>contained in the returned optional of the <a href="#getMutator()"><code>getMutator()</code></a>.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#tryDamageItem()" class="member-name-link">tryDamageItem</a>()</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operation.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#tryDamageItem(int)" class="member-name-link">tryDamageItem</a><wbr>(int&nbsp;damage)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operation.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDo(int,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(int&nbsp;damage,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#tryDamageItemAndDo(int,java.lang.Runnable,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(int&nbsp;damage,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onBroken)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDo(java.lang.Runnable,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onBroken)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDoOrSetBrokenError(java.lang.Runnable)" class="member-name-link">tryDamageItemAndDoOrSetBrokenError</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#validateBuildHeights()" class="member-name-link">validateBuildHeights</a>()</code></td><td><div class="block">Checks whether the mutator currently modifies blocks outside the levels build height.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clearStateFilter()" class="member-name-link">clearStateFilter</a>()</code></td><td><div class="block">Clears the state filter which is applied to the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> for this context.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td><div class="block">Creates a deep copy of the context, so that the copy can be modified, without modifying this instance.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.network.chat.MutableComponent&gt;</code></td><td><code><a href="#getError()" class="member-name-link">getError</a>()</code></td><td><div class="block">Returns the error message that is displayed when the chiseling operation fails.</div><br></td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;T&gt;</code></td><td><code><a href="#getMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)" class="member-name-link">getMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;T&gt;&nbsp;key)</code></td><td><div class="block">Allows the storage of metadata on the context.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></code></td><td><code><a href="#getMode()" class="member-name-link">getMode</a>()</code></td><td><div class="block">Returns the current <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode"><code>IChiselMode</code></a> for which this context is valid.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></code></td><td><code><a href="#getModeOfOperandus()" class="member-name-link">getModeOfOperandus</a>()</code></td><td><div class="block">Indicates what kind of chiseling operation this context was created for.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a>&gt;</code></td><td><code><a href="#getMutator()" class="member-name-link">getMutator</a>()</code></td><td><div class="block">Returns the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> if there is one.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&gt;&gt;</code></td><td><code><a href="#getStateFilter()" class="member-name-link">getStateFilter</a>()</code></td><td><div class="block">Returns the filter that is currently applied on the context.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.level.LevelAccessor</code></td><td><code><a href="#getWorld()" class="member-name-link">getWorld</a>()</code></td><td><div class="block">The <code>LevelAccessor</code> in which the current chiseling context is valid.</div><br></td></tr>
  <tr><td><code>default @NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#include(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">include</a><wbr>(net.minecraft.core.BlockPos&nbsp;inWorldPosition,<br> net.minecraft.world.phys.Vec3&nbsp;relativeInBlockPosition)</code></td><td><div class="block">Includes the given exact position in the world of this context, retrievable via <a href="#getWorld()"><code>getWorld()</code></a>, in<br>the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#include(net.minecraft.world.phys.Vec3)" class="member-name-link">include</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;worldPosition)</code></td><td><div class="block">Includes the given exact position in the world of this context, retrievable via <a href="#getWorld()"><code>getWorld()</code></a>, in<br>the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isComplete()" class="member-name-link">isComplete</a>()</code></td><td><div class="block">Indicates if the context is completed or not.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isSimulation()" class="member-name-link">isSimulation</a>()</code></td><td><div class="block">Indicates if the current context that is being executed is supposed to be a simulation.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)" class="member-name-link">removeMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;?&gt;&nbsp;key)</code></td><td><div class="block">Removes the metadata from the context.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#resetMutator()" class="member-name-link">resetMutator</a>()</code></td><td><div class="block">Resets the mutator that is used to handle the current selected area.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setComplete()" class="member-name-link">setComplete</a>()</code></td><td><div class="block">Marks the current context as complete, so that it can not be reused for interactions which<br>will follow this one.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setError(net.minecraft.network.chat.MutableComponent)" class="member-name-link">setError</a><wbr>(net.minecraft.network.chat.MutableComponent&nbsp;errorText)</code></td><td><div class="block">Sets the error message that is displayed when the chiseling operation fails.</div><br></td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;void</code></td><td><code><a href="#setMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey,T)" class="member-name-link">setMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;T&gt;&nbsp;key,<br> T&nbsp;value)</code></td><td><div class="block">Allows for the setting of the metadata on the context.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setStateFilter(java.util.function.Function)" class="member-name-link">setStateFilter</a><wbr>(@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&gt;&nbsp;filterBuilder)</code></td><td><div class="block">Allows for the setting of a filterBuilder on the context, which limits which <a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IStateEntryInfo</code></a> are returned from<br>the relevant accessor methods of the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>, as well as which limits the setter methods on the same <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a><br>contained in the returned optional of the <a href="#getMutator()"><code>getMutator()</code></a>.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#tryDamageItem()" class="member-name-link">tryDamageItem</a>()</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operation.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#tryDamageItem(int)" class="member-name-link">tryDamageItem</a><wbr>(int&nbsp;damage)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operation.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDo(int,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(int&nbsp;damage,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#tryDamageItemAndDo(int,java.lang.Runnable,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(int&nbsp;damage,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onBroken)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDo(java.lang.Runnable,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onBroken)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDoOrSetBrokenError(java.lang.Runnable)" class="member-name-link">tryDamageItemAndDoOrSetBrokenError</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#validateBuildHeights()" class="member-name-link">validateBuildHeights</a>()</code></td><td><div class="block">Checks whether the mutator currently modifies blocks outside the levels build height.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#clearStateFilter()" class="member-name-link">clearStateFilter</a>()</code></td><td><div class="block">Clears the state filter which is applied to the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> for this context.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#createSnapshot()" class="member-name-link">createSnapshot</a>()</code></td><td><div class="block">Creates a deep copy of the context, so that the copy can be modified, without modifying this instance.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.network.chat.MutableComponent&gt;</code></td><td><code><a href="#getError()" class="member-name-link">getError</a>()</code></td><td><div class="block">Returns the error message that is displayed when the chiseling operation fails.</div><br></td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;T&gt;</code></td><td><code><a href="#getMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)" class="member-name-link">getMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;T&gt;&nbsp;key)</code></td><td><div class="block">Allows the storage of metadata on the context.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></code></td><td><code><a href="#getMode()" class="member-name-link">getMode</a>()</code></td><td><div class="block">Returns the current <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode"><code>IChiselMode</code></a> for which this context is valid.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></code></td><td><code><a href="#getModeOfOperandus()" class="member-name-link">getModeOfOperandus</a>()</code></td><td><div class="block">Indicates what kind of chiseling operation this context was created for.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a>&gt;</code></td><td><code><a href="#getMutator()" class="member-name-link">getMutator</a>()</code></td><td><div class="block">Returns the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> if there is one.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&gt;&gt;</code></td><td><code><a href="#getStateFilter()" class="member-name-link">getStateFilter</a>()</code></td><td><div class="block">Returns the filter that is currently applied on the context.</div><br></td></tr>
  <tr><td><code>@NotNull net.minecraft.world.level.LevelAccessor</code></td><td><code><a href="#getWorld()" class="member-name-link">getWorld</a>()</code></td><td><div class="block">The <code>LevelAccessor</code> in which the current chiseling context is valid.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#include(net.minecraft.world.phys.Vec3)" class="member-name-link">include</a><wbr>(net.minecraft.world.phys.Vec3&nbsp;worldPosition)</code></td><td><div class="block">Includes the given exact position in the world of this context, retrievable via <a href="#getWorld()"><code>getWorld()</code></a>, in<br>the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isComplete()" class="member-name-link">isComplete</a>()</code></td><td><div class="block">Indicates if the context is completed or not.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isSimulation()" class="member-name-link">isSimulation</a>()</code></td><td><div class="block">Indicates if the current context that is being executed is supposed to be a simulation.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)" class="member-name-link">removeMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;?&gt;&nbsp;key)</code></td><td><div class="block">Removes the metadata from the context.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#resetMutator()" class="member-name-link">resetMutator</a>()</code></td><td><div class="block">Resets the mutator that is used to handle the current selected area.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setComplete()" class="member-name-link">setComplete</a>()</code></td><td><div class="block">Marks the current context as complete, so that it can not be reused for interactions which<br>will follow this one.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setError(net.minecraft.network.chat.MutableComponent)" class="member-name-link">setError</a><wbr>(net.minecraft.network.chat.MutableComponent&nbsp;errorText)</code></td><td><div class="block">Sets the error message that is displayed when the chiseling operation fails.</div><br></td></tr>
  <tr><td><code>&lt;T&gt;&nbsp;void</code></td><td><code><a href="#setMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey,T)" class="member-name-link">setMetadata</a><wbr>(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;T&gt;&nbsp;key,<br> T&nbsp;value)</code></td><td><div class="block">Allows for the setting of the metadata on the context.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setStateFilter(java.util.function.Function)" class="member-name-link">setStateFilter</a><wbr>(@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&gt;&nbsp;filterBuilder)</code></td><td><div class="block">Allows for the setting of a filterBuilder on the context, which limits which <a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IStateEntryInfo</code></a> are returned from<br>the relevant accessor methods of the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>, as well as which limits the setter methods on the same <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a><br>contained in the returned optional of the <a href="#getMutator()"><code>getMutator()</code></a>.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#tryDamageItemAndDo(int,java.lang.Runnable,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(int&nbsp;damage,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onBroken)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default @NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></code></td><td><code><a href="#include(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" class="member-name-link">include</a><wbr>(net.minecraft.core.BlockPos&nbsp;inWorldPosition,<br> net.minecraft.world.phys.Vec3&nbsp;relativeInBlockPosition)</code></td><td><div class="block">Includes the given exact position in the world of this context, retrievable via <a href="#getWorld()"><code>getWorld()</code></a>, in<br>the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#tryDamageItem()" class="member-name-link">tryDamageItem</a>()</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operation.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#tryDamageItem(int)" class="member-name-link">tryDamageItem</a><wbr>(int&nbsp;damage)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operation.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDo(int,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(int&nbsp;damage,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDo(java.lang.Runnable,java.lang.Runnable)" class="member-name-link">tryDamageItemAndDo</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged,<br> <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onBroken)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default int</code></td><td><code><a href="#tryDamageItemAndDoOrSetBrokenError(java.lang.Runnable)" class="member-name-link">tryDamageItemAndDoOrSetBrokenError</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged)</code></td><td><div class="block">Invoked to try to damage the item that caused the chiseling operations.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#validateBuildHeights()" class="member-name-link">validateBuildHeights</a>()</code></td><td><div class="block">Checks whether the mutator currently modifies blocks outside the levels build height.</div><br></td></tr>
  </tbody>
</table>
:::
Methods inherited from interface&nbsp;mod.chiselsandbits.api.multistate.accessor.<a href="../multistate/accessor/IStateAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateAccessor</a><a href="../multistate/accessor/IStateAccessor.html#getInAreaTarget(net.minecraft.world.phys.Vec3)" title="getInAreaTarget(Vec3)">getInAreaTarget</a>, <a href="../multistate/accessor/IStateAccessor.html#getInBlockTarget(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)" title="getInBlockTarget(BlockPos, Vec3)">getInBlockTarget</a>
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getMutator()">

:::tabs
== getMutator
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world">IWorldAreaMutator</a>&gt;</span>&nbsp;<span class="element-name">getMutator</span>()</div>
Returns the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> if there is one.
If a new chiseling operation is started no <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> is available,
as such an empty <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> will be returned in that case.

Only after the primary call to <a href="#include(net.minecraft.world.phys.Vec3)"><code>include(Vec3)</code></a> or <a href="#include(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)"><code>include(BlockPos, Vec3)</code></a>
the returned <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> can contain a <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.
<dl class="notes">
<dt>Returns:</dt>
<dd>The <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link"><code>Optional</code></a> containing the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</dd>
</dl>
</div>
:::


</section>

<section id="getWorld()">

:::tabs
== getWorld
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull net.minecraft.world.level.LevelAccessor</span>&nbsp;<span class="element-name">getWorld</span>()</div>
The <code>LevelAccessor</code> in which the current chiseling context is valid.
<dl class="notes">
<dt>Returns:</dt>
<dd>The <code>LevelAccessor</code>.</dd>
</dl>
</div>
:::


</section>

<section id="getMode()">

:::tabs
== getMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode">IChiselMode</a></span>&nbsp;<span class="element-name">getMode</span>()</div>
Returns the current <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode"><code>IChiselMode</code></a> for which this context is valid.
<dl class="notes">
<dt>Returns:</dt>
<dd>The <a href="mode/IChiselMode.html" title="interface in mod.chiselsandbits.api.chiseling.mode"><code>IChiselMode</code></a>.</dd>
</dl>
</div>
:::


</section>

<section id="include(net.minecraft.world.phys.Vec3)">

:::tabs
== include
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></span>&nbsp;<span class="element-name">include</span><wbr><span class="parameters">(net.minecraft.world.phys.Vec3&nbsp;worldPosition)</span></div>
Includes the given exact position in the world of this context, retrievable via <a href="#getWorld()"><code>getWorld()</code></a>, in
the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.

If the given position is already contained in the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>, this method makes
no changes to the current context.

It is up to the contexts implementation as well as the entire implementation of the chisels and bits api
to round the given value up and down into a precision which it can process, meaning that a given exact position
might already be included in the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> if it is within the precision of the
current runtime. Even if the given exact vector itself is not included in the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>worldPosition</code> - The position in the current world to include.</dd>
<dt>Returns:</dt>
<dd>The context, possibly with a mutated <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</dd>
</dl>
</div>
:::


</section>

<section id="include(net.minecraft.core.BlockPos,net.minecraft.world.phys.Vec3)">

:::tabs
== include
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="modifiers">default</span>&nbsp;<span class="return-type">@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></span>&nbsp;<span class="element-name">include</span><wbr><span class="parameters">(net.minecraft.core.BlockPos&nbsp;inWorldPosition,
 net.minecraft.world.phys.Vec3&nbsp;relativeInBlockPosition)</span></div>
Includes the given exact position in the world of this context, retrievable via <a href="#getWorld()"><code>getWorld()</code></a>, in
the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.

If the given position is already contained in the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>, this method makes
no changes to the current context.

It is up to the contexts implementation as well as the entire implementation of the chisels and bits api
to round the given value up and down into a precision which it can process, meaning that a given exact position
might already be included in the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> if it is within the precision of the
current runtime. Even if the given exact vector itself is not included in the current <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inWorldPosition</code> - The position of the block relative to which the <code>relativeInBlockPosition</code> is processed.</dd>
<dd><code>relativeInBlockPosition</code> - The relative position to include. Relative to the given <code>inWorldPosition</code></dd>
<dt>Returns:</dt>
<dd>The context, possibly with a mutated <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>.</dd>
</dl>
</div>
:::


</section>

<section id="setComplete()">

:::tabs
== setComplete
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setComplete</span>()</div>
Marks the current context as complete, so that it can not be reused for interactions which
will follow this one.

Indicates that an action has been performed using this context, making it invalid.</div>
:::


</section>

<section id="isComplete()">

:::tabs
== isComplete
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isComplete</span>()</div>
Indicates if the context is completed or not.
<dl class="notes">
<dt>Returns:</dt>
<dd>True when complete.</dd>
</dl>
</div>
:::


</section>

<section id="isSimulation()">

:::tabs
== isSimulation
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isSimulation</span>()</div>
Indicates if the current context that is being executed is supposed to be a simulation.
<dl class="notes">
<dt>Returns:</dt>
<dd>True when a simulation.</dd>
</dl>
</div>
:::


</section>

<section id="getModeOfOperandus()">

:::tabs
== getModeOfOperandus
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="ChiselingOperation.html" title="enum class in mod.chiselsandbits.api.chiseling">ChiselingOperation</a></span>&nbsp;<span class="element-name">getModeOfOperandus</span>()</div>
Indicates what kind of chiseling operation this context was created for.
This indicates if the mode is used for chiseling or placing.
<dl class="notes">
<dt>Returns:</dt>
<dd><a href="ChiselingOperation.html#CHISELING"><code>ChiselingOperation.CHISELING</code></a> when the context is used for breaking blocks, <a href="ChiselingOperation.html#PLACING"><code>ChiselingOperation.PLACING</code></a> for bit placement.</dd>
</dl>
</div>
:::


</section>

<section id="createSnapshot()">

:::tabs
== createSnapshot
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="IChiselingContext.html" title="interface in mod.chiselsandbits.api.chiseling">IChiselingContext</a></span>&nbsp;<span class="element-name">createSnapshot</span>()</div>
Creates a deep copy of the context, so that the copy can be modified, without modifying this instance.
A snapshot is automatically a simulation.
<dl class="notes">
<dt>Returns:</dt>
<dd>The snapshot context of this context.</dd>
</dl>
</div>
:::


</section>

<section id="tryDamageItem()">

:::tabs
== tryDamageItem
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">tryDamageItem</span>()</div>
Invoked to try to damage the item that caused the chiseling operation.
If no item was the cause of the operation this function always returns successfully.
If this item does not support damaging the item on a chiseling operation this method also
always returns successfully.

Does exactly 1 damage to the item.

The only case where this method does not return <code>True</code>, is when the item that caused the operation broke in the previous operation.
<dl class="notes">
<dt>Returns:</dt>
<dd><code>True</code> when successful, <code>false</code> when not.</dd>
</dl>
</div>
:::


</section>

<section id="tryDamageItem(int)">

:::tabs
== tryDamageItem
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">tryDamageItem</span><wbr><span class="parameters">(int&nbsp;damage)</span></div>
Invoked to try to damage the item that caused the chiseling operation.
If no item was the cause of the operation this function always returns successfully.
If this item does not support damaging the item on a chiseling operation this method also
always returns successfully.

The only case where this method does not return <code>True</code>, is when the item that caused the operation broke in the previous operation.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>damage</code> - The damage to apply to the item that caused the chiseling operation.</dd>
<dt>Returns:</dt>
<dd><code>True</code> when successful, <code>false</code> when not.</dd>
</dl>
</div>
:::


</section>

<section id="tryDamageItemAndDo(java.lang.Runnable,java.lang.Runnable)">

:::tabs
== tryDamageItemAndDo
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">tryDamageItemAndDo</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onBroken)</span></div>
Invoked to try to damage the item that caused the chiseling operations.

If no item was the cause of the operation, then the <code>onDamaged</code> callback is always invoked.
If the item that caused the operation, does not support damaging the item on a chiseling operation, then the <code>onDamaged</code> callback is always invoked.
If the item that caused the operation is already broken, then the <code>onBroken</code> callback is always invoked.

The total performed damaged is returned by this method, which is always <code>0</code> if the item that caused the operation is already broken.

Does exactly 1 damage to the item.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>onDamaged</code> - The callback to invoke when the item is damaged.</dd>
<dd><code>onBroken</code> - The callback to invoke when the item is broken.</dd>
<dt>Returns:</dt>
<dd>The total damage applied to the item.</dd>
</dl>
</div>
:::


</section>

<section id="tryDamageItemAndDoOrSetBrokenError(java.lang.Runnable)">

:::tabs
== tryDamageItemAndDoOrSetBrokenError
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">tryDamageItemAndDoOrSetBrokenError</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged)</span></div>
Invoked to try to damage the item that caused the chiseling operations.

If no item was the cause of the operation, then the <code>onDamaged</code> callback is always invoked.
If the item that caused the operation, does not support damaging the item on a chiseling operation, then the <code>onDamaged</code> callback is always invoked.
If the item that caused the operation is already broken, then the broken chisel item error message is set.

The total performed damaged is returned by this method, which is always <code>0</code> if the item that caused the operation is already broken.

Does exactly 1 damage to the item.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>onDamaged</code> - The callback to invoke when the item is damaged.</dd>
<dt>Returns:</dt>
<dd>The total damage applied to the item.</dd>
</dl>
</div>
:::


</section>

<section id="tryDamageItemAndDo(int,java.lang.Runnable)">

:::tabs
== tryDamageItemAndDo
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">int</span>&nbsp;<span class="element-name">tryDamageItemAndDo</span><wbr><span class="parameters">(int&nbsp;damage,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged)</span></div>
Invoked to try to damage the item that caused the chiseling operations.

If no item was the cause of the operation, then the <code>onDamaged</code> callback is always invoked.
If the item that caused the operation, does not support damaging the item on a chiseling operation, then the <code>onDamaged</code> callback is always invoked.
If the item that caused the operation is already broken, then the broken chisel item error message is set.

The total performed damaged is returned by this method, which is always <code>0</code> if the item that caused the operation is already broken.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>damage</code> - The damage to apply to the item that caused the chiseling operation.</dd>
<dd><code>onDamaged</code> - The callback to invoke when the item is damaged.</dd>
<dt>Returns:</dt>
<dd>The total damage applied to the item.</dd>
</dl>
</div>
:::


</section>

<section id="tryDamageItemAndDo(int,java.lang.Runnable,java.lang.Runnable)">

:::tabs
== tryDamageItemAndDo
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">int</span>&nbsp;<span class="element-name">tryDamageItemAndDo</span><wbr><span class="parameters">(int&nbsp;damage,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onDamaged,
 <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang" class="external-link">Runnable</a>&nbsp;onBroken)</span></div>
Invoked to try to damage the item that caused the chiseling operations.

If no item was the cause of the operation, then the <code>onDamaged</code> callback is always invoked.
If the item that caused the operation, does not support damaging the item on a chiseling operation, then the <code>onDamaged</code> callback is always invoked.
If the item that caused the operation is already broken, then the <code>onBroken</code> callback is always invoked.

The total performed damaged is returned by this method, which is always <code>0</code> if the item that caused the operation is already broken.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>damage</code> - The damage to apply to the item that caused the chiseling operation.</dd>
<dd><code>onDamaged</code> - The callback to invoke when the item is damaged.</dd>
<dd><code>onBroken</code> - The callback to invoke when the item is broken.</dd>
<dt>Returns:</dt>
<dd>The total damage applied to the item.</dd>
</dl>
</div>
:::


</section>

<section id="setStateFilter(java.util.function.Function)">

:::tabs
== setStateFilter
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setStateFilter</span><wbr><span class="parameters">(@NotNull
 @NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&gt;&nbsp;filterBuilder)</span></div>
Allows for the setting of a filterBuilder on the context, which limits which <a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor"><code>IStateEntryInfo</code></a> are returned from
the relevant accessor methods of the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>, as well as which limits the setter methods on the same <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a>
contained in the returned optional of the <a href="#getMutator()"><code>getMutator()</code></a>.

If this context has currently no mutator available, and gets a mutator available afterwards then this filterBuilder will be applied to the new mutator.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filterBuilder</code> - The new filterBuilder.</dd>
</dl>
</div>
:::


</section>

<section id="clearStateFilter()">

:::tabs
== clearStateFilter
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clearStateFilter</span>()</div>
Clears the state filter which is applied to the <a href="../multistate/mutator/world/IWorldAreaMutator.html" title="interface in mod.chiselsandbits.api.multistate.mutator.world"><code>IWorldAreaMutator</code></a> for this context.</div>
:::


</section>

<section id="getStateFilter()">

:::tabs
== getStateFilter
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../multistate/accessor/IAreaAccessor.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IAreaAccessor</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function" class="external-link">Predicate</a>&lt;<a href="../multistate/accessor/IStateEntryInfo.html" title="interface in mod.chiselsandbits.api.multistate.accessor">IStateEntryInfo</a>&gt;&gt;&gt;</span>&nbsp;<span class="element-name">getStateFilter</span>()</div>
Returns the filter that is currently applied on the context.
If one is applied.
<dl class="notes">
<dt>Returns:</dt>
<dd>An optional, potentially containing the filter.</dd>
</dl>
</div>
:::


</section>

<section id="getMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)">

:::tabs
== getMetadata
<div class="horizontal-scroll">
<div class="member-signature"><span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;T&gt;</span>&nbsp;<span class="element-name">getMetadata</span><wbr><span class="parameters">(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;T&gt;&nbsp;key)</span></div>
Allows the storage of metadata on the context.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="getMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)-type-param-T"><code>T</code> - The type of the metadata.</span></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - The key of the metadata.</dd>
<dt>Returns:</dt>
<dd>An optional possibly containing the stored metadata, or empty if no metadata is stored with the given key.</dd>
</dl>
</div>
:::


</section>

<section id="removeMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey)">

:::tabs
== removeMetadata
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">removeMetadata</span><wbr><span class="parameters">(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;?&gt;&nbsp;key)</span></div>
Removes the metadata from the context.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - The key for the metadata.</dd>
</dl>
</div>
:::


</section>

<section id="setMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey,T)">

:::tabs
== setMetadata
<div class="horizontal-scroll">
<div class="member-signature"><span class="type-parameters">&lt;T&gt;</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setMetadata</span><wbr><span class="parameters">(<a href="metadata/IMetadataKey.html" title="interface in mod.chiselsandbits.api.chiseling.metadata">IMetadataKey</a>&lt;T&gt;&nbsp;key,
 T&nbsp;value)</span></div>
Allows for the setting of the metadata on the context.
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><span id="setMetadata(mod.chiselsandbits.api.chiseling.metadata.IMetadataKey,T)-type-param-T"><code>T</code> - The type of the metadata.</span></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - The key of the metadata.</dd>
<dd><code>value</code> - The value of the metadata.</dd>
</dl>
</div>
:::


</section>

<section id="resetMutator()">

:::tabs
== resetMutator
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">resetMutator</span>()</div>
Resets the mutator that is used to handle the current selected area.</div>
:::


</section>

<section id="setError(net.minecraft.network.chat.MutableComponent)">

:::tabs
== setError
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setError</span><wbr><span class="parameters">(net.minecraft.network.chat.MutableComponent&nbsp;errorText)</span></div>
Sets the error message that is displayed when the chiseling operation fails.
If an error is already set on the context, then subsequent calls to this method will be ignored.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>errorText</code> - The new error message.</dd>
</dl>
</div>
:::


</section>

<section id="getError()">

:::tabs
== getError
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.network.chat.MutableComponent&gt;</span>&nbsp;<span class="element-name">getError</span>()</div>
Returns the error message that is displayed when the chiseling operation fails.
<dl class="notes">
<dt>Returns:</dt>
<dd>An optional with the potential error message included.</dd>
</dl>
</div>
:::


</section>

<section id="validateBuildHeights()">

:::tabs
== validateBuildHeights
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">validateBuildHeights</span>()</div>
Checks whether the mutator currently modifies blocks outside the levels build height.
<dl class="notes">
<dt>Returns:</dt>
<dd>True when the build height is respected, false when not.</dd>
</dl>
</div>
:::


</section>

:::::
  

