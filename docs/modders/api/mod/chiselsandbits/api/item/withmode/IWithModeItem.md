--- 
title: IWithModeItem
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.withmode](index)  
# Interface IWithModeItem\<M extends IToolMode\<?\>\>  
**Type Parameters:**  
M - The enum specifying the mode.  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IWithModeItem&lt;M extends <a href="IToolMode.html" title="interface in mod.chiselsandbits.api.item.withmode">IToolMode</a>&lt;?&gt;&gt;</span></div>  

  

Represents an item with several operational modes.  

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
  <tr><td><code><a href="#type-param-M" title="type parameter in IWithModeItem">M</a></code></td><td><code><a href="#getMode(net.minecraft.world.item.ItemStack)" class="member-name-link">getMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Returns the current mode of the itemstack.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="#type-param-M" title="type parameter in IWithModeItem">M</a>&gt;</code></td><td><code><a href="#getPossibleModes()" class="member-name-link">getPossibleModes</a>()</code></td><td><div class="block">Returns all possible modes this item can have.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#requiresUpdateOnClosure()" class="member-name-link">requiresUpdateOnClosure</a>()</code></td><td><div class="block">Indicates to the ux system that this item requires an additional<br>update when the player closes the interface.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#setMode(net.minecraft.world.item.ItemStack,int)" class="member-name-link">setMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> int&nbsp;modeIndex)</code></td><td><div class="block">Set the mode with the given index on the given itemstack.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setMode(net.minecraft.world.item.ItemStack,M)" class="member-name-link">setMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> <a href="#type-param-M" title="type parameter in IWithModeItem">M</a>&nbsp;mode)</code></td><td><div class="block">Set the given mode on the given itemstack.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#type-param-M" title="type parameter in IWithModeItem">M</a></code></td><td><code><a href="#getMode(net.minecraft.world.item.ItemStack)" class="member-name-link">getMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Returns the current mode of the itemstack.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="#type-param-M" title="type parameter in IWithModeItem">M</a>&gt;</code></td><td><code><a href="#getPossibleModes()" class="member-name-link">getPossibleModes</a>()</code></td><td><div class="block">Returns all possible modes this item can have.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#requiresUpdateOnClosure()" class="member-name-link">requiresUpdateOnClosure</a>()</code></td><td><div class="block">Indicates to the ux system that this item requires an additional<br>update when the player closes the interface.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#setMode(net.minecraft.world.item.ItemStack,int)" class="member-name-link">setMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> int&nbsp;modeIndex)</code></td><td><div class="block">Set the mode with the given index on the given itemstack.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setMode(net.minecraft.world.item.ItemStack,M)" class="member-name-link">setMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> <a href="#type-param-M" title="type parameter in IWithModeItem">M</a>&nbsp;mode)</code></td><td><div class="block">Set the given mode on the given itemstack.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#type-param-M" title="type parameter in IWithModeItem">M</a></code></td><td><code><a href="#getMode(net.minecraft.world.item.ItemStack)" class="member-name-link">getMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Returns the current mode of the itemstack.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;<a href="#type-param-M" title="type parameter in IWithModeItem">M</a>&gt;</code></td><td><code><a href="#getPossibleModes()" class="member-name-link">getPossibleModes</a>()</code></td><td><div class="block">Returns all possible modes this item can have.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setMode(net.minecraft.world.item.ItemStack,M)" class="member-name-link">setMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> <a href="#type-param-M" title="type parameter in IWithModeItem">M</a>&nbsp;mode)</code></td><td><div class="block">Set the given mode on the given itemstack.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#requiresUpdateOnClosure()" class="member-name-link">requiresUpdateOnClosure</a>()</code></td><td><div class="block">Indicates to the ux system that this item requires an additional<br>update when the player closes the interface.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#setMode(net.minecraft.world.item.ItemStack,int)" class="member-name-link">setMode</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack,<br> int&nbsp;modeIndex)</code></td><td><div class="block">Set the mode with the given index on the given itemstack.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="requiresUpdateOnClosure()">

:::tabs
== requiresUpdateOnClosure
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">requiresUpdateOnClosure</span>()</div>
Indicates to the ux system that this item requires an additional
update when the player closes the interface.
<dl class="notes">
<dt>Returns:</dt>
<dd>True when the update is required, false when not.</dd>
</dl>
</div>
:::


</section>

<section id="getMode(net.minecraft.world.item.ItemStack)">

:::tabs
== getMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type"><a href="#type-param-M" title="type parameter in IWithModeItem">M</a></span>&nbsp;<span class="element-name">getMode</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
Returns the current mode of the itemstack.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack in question.</dd>
<dt>Returns:</dt>
<dd>The mode the given stack has.</dd>
</dl>
</div>
:::


</section>

<section id="setMode(net.minecraft.world.item.ItemStack,M)">

:::tabs
== setMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setMode</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack,
 <a href="#type-param-M" title="type parameter in IWithModeItem">M</a>&nbsp;mode)</span></div>
Set the given mode on the given itemstack.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to set the mode on.</dd>
<dd><code>mode</code> - The mode to set on the stack.</dd>
</dl>
</div>
:::


</section>

<section id="setMode(net.minecraft.world.item.ItemStack,int)">

:::tabs
== setMode
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">setMode</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack,
 int&nbsp;modeIndex)</span></div>
Set the mode with the given index on the given itemstack.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to set the mode on.</dd>
<dd><code>modeIndex</code> - The modes index to set on the stack.</dd>
</dl>
</div>
:::


</section>

<section id="getPossibleModes()">

:::tabs
== getPossibleModes
<div class="horizontal-scroll">
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;<a href="#type-param-M" title="type parameter in IWithModeItem">M</a>&gt;</span>&nbsp;<span class="element-name">getPossibleModes</span>()</div>
Returns all possible modes this item can have.
<dl class="notes">
<dt>Returns:</dt>
<dd>The possible modes in an array.</dd>
</dl>
</div>
:::


</section>

:::::
  

