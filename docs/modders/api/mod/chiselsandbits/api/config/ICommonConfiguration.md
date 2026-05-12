--- 
title: ICommonConfiguration
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.config](index.md)  
# Interface ICommonConfiguration  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ICommonConfiguration</span></div>  

  

  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBlockSaveThreadCount()" class="member-name-link">getBlockSaveThreadCount</a>()</code></td><td><div class="block">Indicates how many threads can be used to calculate and compress off-thread NBT data for saving.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getClassMetadataCacheSize()" class="member-name-link">getClassMetadataCacheSize</a>()</code></td><td><div class="block">Determines the size of caches which hold class metadata.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getCollisionBoxCacheSize()" class="member-name-link">getCollisionBoxCacheSize</a>()</code></td><td><div class="block">Determines the size of the collision box cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableHelp()" class="member-name-link">getEnableHelp</a>()</code></td><td><div class="block">Indicates if the help tooltips should be enabled or not.</div><br></td></tr>
  <tr><td><code>static <a href="ICommonConfiguration.html" title="interface in mod.chiselsandbits.api.config">ICommonConfiguration</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The common configuration.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="ICommonConfiguration.html" title="interface in mod.chiselsandbits.api.config">ICommonConfiguration</a></code></td><td><code><a href="#getInstance()" class="member-name-link">getInstance</a>()</code></td><td><div class="block">The common configuration.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBlockSaveThreadCount()" class="member-name-link">getBlockSaveThreadCount</a>()</code></td><td><div class="block">Indicates how many threads can be used to calculate and compress off-thread NBT data for saving.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getClassMetadataCacheSize()" class="member-name-link">getClassMetadataCacheSize</a>()</code></td><td><div class="block">Determines the size of caches which hold class metadata.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getCollisionBoxCacheSize()" class="member-name-link">getCollisionBoxCacheSize</a>()</code></td><td><div class="block">Determines the size of the collision box cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableHelp()" class="member-name-link">getEnableHelp</a>()</code></td><td><div class="block">Indicates if the help tooltips should be enabled or not.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBlockSaveThreadCount()" class="member-name-link">getBlockSaveThreadCount</a>()</code></td><td><div class="block">Indicates how many threads can be used to calculate and compress off-thread NBT data for saving.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getClassMetadataCacheSize()" class="member-name-link">getClassMetadataCacheSize</a>()</code></td><td><div class="block">Determines the size of caches which hold class metadata.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</code></td><td><code><a href="#getCollisionBoxCacheSize()" class="member-name-link">getCollisionBoxCacheSize</a>()</code></td><td><div class="block">Determines the size of the collision box cache size.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</code></td><td><code><a href="#getEnableHelp()" class="member-name-link">getEnableHelp</a>()</code></td><td><div class="block">Indicates if the help tooltips should be enabled or not.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="getInstance()">

:::tabs
== getInstance
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">static</span>&nbsp;<span class="return-type"><a href="ICommonConfiguration.html" title="interface in mod.chiselsandbits.api.config">ICommonConfiguration</a></span>&nbsp;<span class="element-name">getInstance</span>()</div>
<div class="block">The common configuration.
Elements in this configuration are relevant for both the server and the client side of C&amp;B.
This configuration does not need to be in-sync with the server values.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The common configuration.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getEnableHelp()">

:::tabs
== getEnableHelp
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang" class="external-link">Boolean</a>&gt;</span>&nbsp;<span class="element-name">getEnableHelp</span>()</div>
<div class="block">Indicates if the help tooltips should be enabled or not.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that can indicate of the help tooltips should be shown or not.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getCollisionBoxCacheSize()">

:::tabs
== getCollisionBoxCacheSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</span>&nbsp;<span class="element-name">getCollisionBoxCacheSize</span>()</div>
<div class="block">Determines the size of the collision box cache size.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines the size of the collision box cache size.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getClassMetadataCacheSize()">

:::tabs
== getClassMetadataCacheSize
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang" class="external-link">Long</a>&gt;</span>&nbsp;<span class="element-name">getClassMetadataCacheSize</span>()</div>
<div class="block">Determines the size of caches which hold class metadata.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The class metadata cache size.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="getBlockSaveThreadCount()">

:::tabs
== getBlockSaveThreadCount
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getBlockSaveThreadCount</span>()</div>
<div class="block">Indicates how many threads can be used to calculate and compress off-thread NBT data for saving.
Loading always happens on thread.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>A supplier that determines the number of threads to use for block saving.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

