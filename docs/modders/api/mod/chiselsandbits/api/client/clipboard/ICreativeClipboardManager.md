--- 
title: ICreativeClipboardManager
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.client.clipboard](index)  
# Interface ICreativeClipboardManager  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ICreativeClipboardManager</span></div>  

  

  

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
  <tr><td><code>void</code></td><td><code><a href="#addEntry(mod.chiselsandbits.api.item.multistate.IMultiStateItemStack,net.minecraft.core.HolderLookup.Provider)" class="member-name-link">addEntry</a><wbr>(<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack,<br> net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Adds an entry to the clipboard.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clear(net.minecraft.core.HolderLookup.Provider)" class="member-name-link">clear</a><wbr>(net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Clears the entire clip board.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&gt;</code></td><td><code><a href="#getClipboard()" class="member-name-link">getClipboard</a>()</code></td><td><div class="block">The clipboard contents.</div><br></td></tr>
  <tr><td><code>static <a href="ICreativeClipboardManager.html" title="interface in mod.chiselsandbits.api.client.clipboard">ICreativeClipboardManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeEntry(int,net.minecraft.core.HolderLookup.Provider)" class="member-name-link">removeEntry</a><wbr>(int&nbsp;index,<br> net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Removes an entry from the clipboard.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="ICreativeClipboardManager.html" title="interface in mod.chiselsandbits.api.client.clipboard">ICreativeClipboardManager</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#addEntry(mod.chiselsandbits.api.item.multistate.IMultiStateItemStack,net.minecraft.core.HolderLookup.Provider)" class="member-name-link">addEntry</a><wbr>(<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack,<br> net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Adds an entry to the clipboard.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clear(net.minecraft.core.HolderLookup.Provider)" class="member-name-link">clear</a><wbr>(net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Clears the entire clip board.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&gt;</code></td><td><code><a href="#getClipboard()" class="member-name-link">getClipboard</a>()</code></td><td><div class="block">The clipboard contents.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeEntry(int,net.minecraft.core.HolderLookup.Provider)" class="member-name-link">removeEntry</a><wbr>(int&nbsp;index,<br> net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Removes an entry from the clipboard.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#addEntry(mod.chiselsandbits.api.item.multistate.IMultiStateItemStack,net.minecraft.core.HolderLookup.Provider)" class="member-name-link">addEntry</a><wbr>(<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack,<br> net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Adds an entry to the clipboard.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#clear(net.minecraft.core.HolderLookup.Provider)" class="member-name-link">clear</a><wbr>(net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Clears the entire clip board.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a><wbr>&lt;<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&gt;</code></td><td><code><a href="#getClipboard()" class="member-name-link">getClipboard</a>()</code></td><td><div class="block">The clipboard contents.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#removeEntry(int,net.minecraft.core.HolderLookup.Provider)" class="member-name-link">removeEntry</a><wbr>(int&nbsp;index,<br> net.minecraft.core.HolderLookup.Provider&nbsp;provider)</code></td><td><div class="block">Removes an entry from the clipboard.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="ICreativeClipboardManager.html" title="interface in mod.chiselsandbits.api.client.clipboard">ICreativeClipboardManager</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
</div>
:::


</section>

<section id="getClipboard()">

:::tabs
== getClipboard
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/List.html" title="class or interface in java.util" class="external-link">List</a>&lt;<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&gt;</span>&nbsp;<span class="element-name">getClipboard</span>()</div>
The clipboard contents.
<dl class="notes">
<dt>Returns:</dt>
<dd>The clipboard contents.</dd>
</dl>
</div>
:::


</section>

<section id="addEntry(mod.chiselsandbits.api.item.multistate.IMultiStateItemStack,net.minecraft.core.HolderLookup.Provider)">

:::tabs
== addEntry
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">addEntry</span><wbr><span class="parameters">(<a href="../../item/multistate/IMultiStateItemStack.html" title="interface in mod.chiselsandbits.api.item.multistate">IMultiStateItemStack</a>&nbsp;multiStateItemStack,
 net.minecraft.core.HolderLookup.Provider&nbsp;provider)</span></div>
Adds an entry to the clipboard.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>multiStateItemStack</code> - The multi-state item stack to add.</dd>
<dd><code>provider</code> - The provider.</dd>
</dl>
</div>
:::


</section>

<section id="removeEntry(int,net.minecraft.core.HolderLookup.Provider)">

:::tabs
== removeEntry
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">removeEntry</span><wbr><span class="parameters">(int&nbsp;index,
 net.minecraft.core.HolderLookup.Provider&nbsp;provider)</span></div>
Removes an entry from the clipboard.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - The index of the entry to remove.</dd>
</dl>
</div>
:::


</section>

<section id="clear(net.minecraft.core.HolderLookup.Provider)">

:::tabs
== clear
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">clear</span><wbr><span class="parameters">(net.minecraft.core.HolderLookup.Provider&nbsp;provider)</span></div>
Clears the entire clip board.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The provider.</dd>
</dl>
</div>
:::


</section>

:::::
  

