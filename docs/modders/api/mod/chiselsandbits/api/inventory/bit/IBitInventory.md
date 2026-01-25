--- 
title: IBitInventory
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.inventory.bit](index.md)  
# Interface IBitInventory  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBitInventory</span></div>  

  

<div class="block">Represents an inventory in which bits are contained.</div>
  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canExtract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">canExtract</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Checks if it is possible to extract a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canExtractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canExtractOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if it is possible to extract exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canInsert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">canInsert</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Checks if it is possible to insert a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canInsertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canInsertOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if it is possible to insert exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#contains(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">contains</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Indicates whether the inventory contains a bit with this block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#extract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">extract</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Extracts a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#extractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">extractOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Extracts exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns the summed contained states of all bits in the inventory.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getMaxExtractAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getMaxExtractAmount</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Returns the maximal amount of bits with a given block information which can be extracted<br> of a given blockstate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getMaxInsertAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getMaxInsertAmount</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Returns the maximal amount of bits with a given block information which can be inserted<br> of a given blockstate.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#insert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">insert</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Inserts a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.item.ItemStack</code></td><td><code><a href="#insert(net.minecraft.world.item.ItemStack)" class="member-name-link">insert</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Tries to insert a given itemstack with a bit item into the inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#insertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">insertOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Inserts exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#insertOrDiscard(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">insertOrDiscard</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Inserts a given amount of bits with the given block information from<br> the current inventory, discards bits that don't fit.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Indicates if this inventory is empty or not.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canExtract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">canExtract</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Checks if it is possible to extract a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canExtractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canExtractOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if it is possible to extract exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canInsert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">canInsert</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Checks if it is possible to insert a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canInsertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canInsertOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if it is possible to insert exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#contains(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">contains</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Indicates whether the inventory contains a bit with this block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#extract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">extract</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Extracts a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#extractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">extractOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Extracts exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns the summed contained states of all bits in the inventory.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getMaxExtractAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getMaxExtractAmount</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Returns the maximal amount of bits with a given block information which can be extracted<br> of a given blockstate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getMaxInsertAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getMaxInsertAmount</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Returns the maximal amount of bits with a given block information which can be inserted<br> of a given blockstate.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#insert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">insert</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Inserts a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.item.ItemStack</code></td><td><code><a href="#insert(net.minecraft.world.item.ItemStack)" class="member-name-link">insert</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Tries to insert a given itemstack with a bit item into the inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#insertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">insertOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Inserts exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#insertOrDiscard(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">insertOrDiscard</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Inserts a given amount of bits with the given block information from<br> the current inventory, discards bits that don't fit.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Indicates if this inventory is empty or not.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>boolean</code></td><td><code><a href="#canExtract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">canExtract</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Checks if it is possible to extract a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#canInsert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">canInsert</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Checks if it is possible to insert a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#contains(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">contains</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Indicates whether the inventory contains a bit with this block.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#extract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">extract</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Extracts a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a><wbr>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getContainedStates()" class="member-name-link">getContainedStates</a>()</code></td><td><div class="block">Returns the summed contained states of all bits in the inventory.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getMaxExtractAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getMaxExtractAmount</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Returns the maximal amount of bits with a given block information which can be extracted<br> of a given blockstate.</div><br></td></tr>
  <tr><td><code>int</code></td><td><code><a href="#getMaxInsertAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getMaxInsertAmount</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Returns the maximal amount of bits with a given block information which can be inserted<br> of a given blockstate.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#insert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">insert</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Inserts a given amount of bits with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isEmpty()" class="member-name-link">isEmpty</a>()</code></td><td><div class="block">Indicates if this inventory is empty or not.</div><br></td></tr>
  </tbody>
</table>
== Default Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>default boolean</code></td><td><code><a href="#canExtractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canExtractOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if it is possible to extract exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default boolean</code></td><td><code><a href="#canInsertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">canInsertOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Checks if it is possible to insert exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#extractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">extractOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Extracts exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default net.minecraft.world.item.ItemStack</code></td><td><code><a href="#insert(net.minecraft.world.item.ItemStack)" class="member-name-link">insert</a><wbr>(net.minecraft.world.item.ItemStack&nbsp;stack)</code></td><td><div class="block">Tries to insert a given itemstack with a bit item into the inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#insertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">insertOne</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Inserts exactly one bit with the given block information from<br> the current inventory.</div><br></td></tr>
  <tr><td><code>default void</code></td><td><code><a href="#insertOrDiscard(mod.chiselsandbits.api.blockinformation.BlockInformation,int)" class="member-name-link">insertOrDiscard</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> int&nbsp;count)</code></td><td><div class="block">Inserts a given amount of bits with the given block information from<br> the current inventory, discards bits that don't fit.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="canExtractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== canExtractOne
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">canExtractOne</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Checks if it is possible to extract exactly one bit with the given block information from
 the current inventory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dt>Returns:</dt>
<dd><code>true</code> when extraction is possible.</dd>
</dl>
:::


</section>

<section id="canExtract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">

:::tabs
== canExtract
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">canExtract</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 int&nbsp;count)</span></div>
<div class="block">Checks if it is possible to extract a given amount of bits with the given block information from
 the current inventory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>count</code> - The amount of bits to extract.</dd>
<dt>Returns:</dt>
<dd><code>true</code> when extraction is possible.</dd>
</dl>
:::


</section>

<section id="getMaxExtractAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== getMaxExtractAmount
<div class="member-signature"><span class="return-type">int</span>&nbsp;<span class="element-name">getMaxExtractAmount</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Returns the maximal amount of bits with a given block information which can be extracted
 of a given blockstate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information in question.</dd>
<dt>Returns:</dt>
<dd>The amount of bits that can be extracted with a given blockstate.</dd>
</dl>
:::


</section>

<section id="extractOne(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== extractOne
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">extractOne</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span>
                 throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></span></div>
<div class="block">Extracts exactly one bit with the given block information from
 the current inventory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></code> - when extraction is not possible.</dd>
</dl>
:::


</section>

<section id="extract(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">

:::tabs
== extract
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">extract</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 int&nbsp;count)</span>
      throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></span></div>
<div class="block">Extracts a given amount of bits with the given block information from
 the current inventory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>count</code> - The amount of bits to extract.</dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></code> - when extraction is not possible.</dd>
</dl>
:::


</section>

<section id="canInsertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== canInsertOne
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">canInsertOne</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Checks if it is possible to insert exactly one bit with the given block information from
 the current inventory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dt>Returns:</dt>
<dd><code>true</code> when insertion is possible.</dd>
</dl>
:::


</section>

<section id="canInsert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">

:::tabs
== canInsert
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">canInsert</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 int&nbsp;count)</span></div>
<div class="block">Checks if it is possible to insert a given amount of bits with the given block information from
 the current inventory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>count</code> - The amount of bits to insert.</dd>
<dt>Returns:</dt>
<dd><code>true</code> when insertion is possible.</dd>
</dl>
:::


</section>

<section id="getMaxInsertAmount(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== getMaxInsertAmount
<div class="member-signature"><span class="return-type">int</span>&nbsp;<span class="element-name">getMaxInsertAmount</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Returns the maximal amount of bits with a given block information which can be inserted
 of a given blockstate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The blockstate in question.</dd>
<dt>Returns:</dt>
<dd>The amount of bits that can be inserted with a given blockstate.</dd>
</dl>
:::


</section>

<section id="insertOne(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== insertOne
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">insertOne</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span>
                throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></span></div>
<div class="block">Inserts exactly one bit with the given block information from
 the current inventory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></code> - when insertion is not possible.</dd>
</dl>
:::


</section>

<section id="insert(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">

:::tabs
== insert
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">insert</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 int&nbsp;count)</span>
     throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></span></div>
<div class="block">Inserts a given amount of bits with the given block information from
 the current inventory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>count</code> - The amount of bits to insert.</dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang" class="external-link">IllegalArgumentException</a></code> - when insertion is not possible.</dd>
</dl>
:::


</section>

<section id="insertOrDiscard(mod.chiselsandbits.api.blockinformation.BlockInformation,int)">

:::tabs
== insertOrDiscard
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">insertOrDiscard</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 int&nbsp;count)</span></div>
<div class="block">Inserts a given amount of bits with the given block information from
 the current inventory, discards bits that don't fit.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>count</code> - The amount of bits to insert.</dd>
</dl>
:::


</section>

<section id="isEmpty()">

:::tabs
== isEmpty
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">isEmpty</span>()</div>
<div class="block">Indicates if this inventory is empty or not.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> when empty.</dd>
</dl>
:::


</section>

<section id="insert(net.minecraft.world.item.ItemStack)">

:::tabs
== insert
<div class="member-signature"><span class="modifiers">default</span>&nbsp;<span class="return-type">net.minecraft.world.item.ItemStack</span>&nbsp;<span class="element-name">insert</span><wbr><span class="parameters">(net.minecraft.world.item.ItemStack&nbsp;stack)</span></div>
<div class="block">Tries to insert a given itemstack with a bit item into the inventory.
 Draining the itemstack completely if possible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stack</code> - The stack to insert.</dd>
<dt>Returns:</dt>
<dd>The remainder, or the original stack if it is not an bit item.</dd>
</dl>
:::


</section>

<section id="getContainedStates()">

:::tabs
== getContainedStates
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util" class="external-link">Map</a>&lt;<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getContainedStates</span>()</div>
<div class="block">Returns the summed contained states of all bits in the inventory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The contained state count of all bits in the inventory.</dd>
</dl>
:::


</section>

<section id="contains(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== contains
<div class="member-signature"><span class="return-type">boolean</span>&nbsp;<span class="element-name">contains</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
<div class="block">Indicates whether the inventory contains a bit with this block.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block to check for.</dd>
<dt>Returns:</dt>
<dd>True when contained.</dd>
</dl>
:::


</section>

:::::
  

