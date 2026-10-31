--- 
title: DataGenerator
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util.constants](index)  
# Class DataGenerator  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.constants.DataGenerator  
  
**Enclosing Class:**  
[Constants](Constants)  

---
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">Constants.DataGenerator</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Paths and a shared Gson instance used by the data generator to emit resources into the resource pack and datapacks.  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
Field Summary  
:::tabs
== Fields
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#BLOCK_TAGS_DIR" class="member-name-link">BLOCK_TAGS_DIR</a></code></td><td><div class="block">Directory for the mod's block tag definitions (datapack tags/blocks).</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#BLOCKSTATE_DIR" class="member-name-link">BLOCKSTATE_DIR</a></code></td><td><div class="block">Directory for block-state JSON files within the mod resource pack.</div><br></td></tr>
  <tr><td><code>static final net.minecraft.resources.Identifier</code></td><td><code><a href="#CHISELED_BLOCK_MODEL" class="member-name-link">CHISELED_BLOCK_MODEL</a></code></td><td><div class="block">Resource location of the model used to render a chiseled block.</div><br></td></tr>
  <tr><td><code>static final net.minecraft.resources.Identifier</code></td><td><code><a href="#CHISELED_PRINTER_MODEL" class="member-name-link">CHISELED_PRINTER_MODEL</a></code></td><td><div class="block">Resource location of the model used to render a chiseled printer.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#CONFIG_LANG_DIR" class="member-name-link">CONFIG_LANG_DIR</a></code></td><td><div class="block">Directory for language files under the mod resource pack's lang/config path.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#EN_US_LANG" class="member-name-link">EN_US_LANG</a></code></td><td><div class="block">Path to the English (en_us) language file inside the mod resource pack.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#FORGE_ITEM_TAGS_DIR" class="member-name-link">FORGE_ITEM_TAGS_DIR</a></code></td><td><div class="block">Directory for Forge-specific item tag definitions (datapack tags/items).</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#FORGE_TAGS_DIR" class="member-name-link">FORGE_TAGS_DIR</a></code></td><td><div class="block">Directory for Forge-specific datapack tag definitions.</div><br></td></tr>
  <tr><td><code>static final com.google.gson.Gson</code></td><td><code><a href="#GSON" class="member-name-link">GSON</a></code></td><td><div class="block">Shared Gson configured for pretty-printed, non-HTML-escaped JSON output.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#ITEM_MODEL_DIR" class="member-name-link">ITEM_MODEL_DIR</a></code></td><td><div class="block">Directory for item model JSON files within the mod resource pack.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#ITEM_TAGS_DIR" class="member-name-link">ITEM_TAGS_DIR</a></code></td><td><div class="block">Directory for the mod's item tag definitions (datapack tags/items).</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#LOOT_TABLES_DIR" class="member-name-link">LOOT_TABLES_DIR</a></code></td><td><div class="block">Directory for block loot-table JSON files in the mod datapack.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#MINECRAFT_ITEM_TAGS_DIR" class="member-name-link">MINECRAFT_ITEM_TAGS_DIR</a></code></td><td><div class="block">Directory for item tag definitions in vanilla Minecraft's datapack namespace.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#MINECRAFT_TAGS_DIR" class="member-name-link">MINECRAFT_TAGS_DIR</a></code></td><td><div class="block">Directory containing vanilla Minecraft tag definitions.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#RECIPES_DIR" class="member-name-link">RECIPES_DIR</a></code></td><td><div class="block">Directory for recipe JSON files in the mod datapack.</div><br></td></tr>
  <tr><td><code>static final <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#TAGS_DIR" class="member-name-link">TAGS_DIR</a></code></td><td><div class="block">Root directory for this mod's datapack tag definitions.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
Constructor Summary  
:::tabs
== Constructors
<table class="stretched-table">
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E()" class="member-name-link">DataGenerator</a>()</code></td><td><div class="block">Creates access to the shared resource-generation constants.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="GSON">

:::tabs
== GSON
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">com.google.gson.Gson</span>&nbsp;<span class="element-name">GSON</span></div>
Shared Gson configured for pretty-printed, non-HTML-escaped JSON output.
</div>
:::


</section>

<section id="EN_US_LANG">

:::tabs
== EN_US_LANG
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">EN_US_LANG</span></div>
Path to the English (en_us) language file inside the mod resource pack.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.EN_US_LANG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="ITEM_MODEL_DIR">

:::tabs
== ITEM_MODEL_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">ITEM_MODEL_DIR</span></div>
Directory for item model JSON files within the mod resource pack.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.ITEM_MODEL_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="RECIPES_DIR">

:::tabs
== RECIPES_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">RECIPES_DIR</span></div>
Directory for recipe JSON files in the mod datapack.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.RECIPES_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="TAGS_DIR">

:::tabs
== TAGS_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">TAGS_DIR</span></div>
Root directory for this mod's datapack tag definitions.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.TAGS_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="MINECRAFT_TAGS_DIR">

:::tabs
== MINECRAFT_TAGS_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">MINECRAFT_TAGS_DIR</span></div>
Directory containing vanilla Minecraft tag definitions.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.MINECRAFT_TAGS_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="BLOCK_TAGS_DIR">

:::tabs
== BLOCK_TAGS_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">BLOCK_TAGS_DIR</span></div>
Directory for the mod's block tag definitions (datapack tags/blocks).
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.BLOCK_TAGS_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="ITEM_TAGS_DIR">

:::tabs
== ITEM_TAGS_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">ITEM_TAGS_DIR</span></div>
Directory for the mod's item tag definitions (datapack tags/items).
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.ITEM_TAGS_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="MINECRAFT_ITEM_TAGS_DIR">

:::tabs
== MINECRAFT_ITEM_TAGS_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">MINECRAFT_ITEM_TAGS_DIR</span></div>
Directory for item tag definitions in vanilla Minecraft's datapack namespace.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.MINECRAFT_ITEM_TAGS_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="FORGE_TAGS_DIR">

:::tabs
== FORGE_TAGS_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">FORGE_TAGS_DIR</span></div>
Directory for Forge-specific datapack tag definitions.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.FORGE_TAGS_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="FORGE_ITEM_TAGS_DIR">

:::tabs
== FORGE_ITEM_TAGS_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">FORGE_ITEM_TAGS_DIR</span></div>
Directory for Forge-specific item tag definitions (datapack tags/items).
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.FORGE_ITEM_TAGS_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="LOOT_TABLES_DIR">

:::tabs
== LOOT_TABLES_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">LOOT_TABLES_DIR</span></div>
Directory for block loot-table JSON files in the mod datapack.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.LOOT_TABLES_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="BLOCKSTATE_DIR">

:::tabs
== BLOCKSTATE_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">BLOCKSTATE_DIR</span></div>
Directory for block-state JSON files within the mod resource pack.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.BLOCKSTATE_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="CONFIG_LANG_DIR">

:::tabs
== CONFIG_LANG_DIR
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">CONFIG_LANG_DIR</span></div>
Directory for language files under the mod resource pack's lang/config path.
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#mod.chiselsandbits.api.util.constants.Constants.DataGenerator.CONFIG_LANG_DIR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</div>
:::


</section>

<section id="CHISELED_BLOCK_MODEL">

:::tabs
== CHISELED_BLOCK_MODEL
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.resources.Identifier</span>&nbsp;<span class="element-name">CHISELED_BLOCK_MODEL</span></div>
Resource location of the model used to render a chiseled block.
</div>
:::


</section>

<section id="CHISELED_PRINTER_MODEL">

:::tabs
== CHISELED_PRINTER_MODEL
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type">net.minecraft.resources.Identifier</span>&nbsp;<span class="element-name">CHISELED_PRINTER_MODEL</span></div>
Resource location of the model used to render a chiseled printer.
</div>
:::


</section>

:::::
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>()">

:::tabs
== DataGenerator
<div class="horizontal-scroll">
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">DataGenerator</span>()</div>
Creates access to the shared resource-generation constants.
</div>
:::


</section>

:::::
  

  

  

