--- 
title: BlockStateSerializationUtils
aside: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Class BlockStateSerializationUtils  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.util.BlockStateSerializationUtils  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">BlockStateSerializationUtils</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

  

<dl class="notes"></dl>  

<!-- =========== FIELD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Summary  
:::tabs
== Fields
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Field</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static com.mojang.serialization.Codec<wbr>&lt;net.minecraft.world.level.block.state.BlockState&gt;</code></td><td><code><a href="#LEGACY_BLOCK_STATE_CODEC" class="member-name-link">LEGACY_BLOCK_STATE_CODEC</a></code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 2 -->
::::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static com.mojang.serialization.DataResult<wbr>&lt;net.minecraft.world.level.block.state.BlockState&gt;</code></td><td><code><a href="#deserialize(java.lang.String)" class="member-name-link">deserialize</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;string)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#deserialize(net.minecraft.network.FriendlyByteBuf)" class="member-name-link">deserialize</a><wbr>(net.minecraft.network.FriendlyByteBuf&nbsp;buffer)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#serialize(net.minecraft.network.FriendlyByteBuf,net.minecraft.world.level.block.state.BlockState)" class="member-name-link">serialize</a><wbr>(net.minecraft.network.FriendlyByteBuf&nbsp;buf,<br> net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#serialize(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">serialize</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static com.mojang.serialization.DataResult<wbr>&lt;net.minecraft.world.level.block.state.BlockState&gt;</code></td><td><code><a href="#deserialize(java.lang.String)" class="member-name-link">deserialize</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;string)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#deserialize(net.minecraft.network.FriendlyByteBuf)" class="member-name-link">deserialize</a><wbr>(net.minecraft.network.FriendlyByteBuf&nbsp;buffer)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#serialize(net.minecraft.network.FriendlyByteBuf,net.minecraft.world.level.block.state.BlockState)" class="member-name-link">serialize</a><wbr>(net.minecraft.network.FriendlyByteBuf&nbsp;buf,<br> net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#serialize(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">serialize</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static com.mojang.serialization.DataResult<wbr>&lt;net.minecraft.world.level.block.state.BlockState&gt;</code></td><td><code><a href="#deserialize(java.lang.String)" class="member-name-link">deserialize</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;string)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static net.minecraft.world.level.block.state.BlockState</code></td><td><code><a href="#deserialize(net.minecraft.network.FriendlyByteBuf)" class="member-name-link">deserialize</a><wbr>(net.minecraft.network.FriendlyByteBuf&nbsp;buffer)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static void</code></td><td><code><a href="#serialize(net.minecraft.network.FriendlyByteBuf,net.minecraft.world.level.block.state.BlockState)" class="member-name-link">serialize</a><wbr>(net.minecraft.network.FriendlyByteBuf&nbsp;buf,<br> net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></code></td><td><code><a href="#serialize(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">serialize</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Field Details  
<section id="LEGACY_BLOCK_STATE_CODEC">

:::tabs
== LEGACY_BLOCK_STATE_CODEC
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">com.mojang.serialization.Codec&lt;net.minecraft.world.level.block.state.BlockState&gt;</span>&nbsp;<span class="element-name">LEGACY_BLOCK_STATE_CODEC</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="deserialize(java.lang.String)">

:::tabs
== deserialize
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">com.mojang.serialization.DataResult&lt;net.minecraft.world.level.block.state.BlockState&gt;</span>&nbsp;<span class="element-name">deserialize</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&nbsp;string)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="serialize(net.minecraft.world.level.block.state.BlockState)">

:::tabs
== serialize
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a></span>&nbsp;<span class="element-name">serialize</span><wbr><span class="parameters">(net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="deserialize(net.minecraft.network.FriendlyByteBuf)">

:::tabs
== deserialize
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">net.minecraft.world.level.block.state.BlockState</span>&nbsp;<span class="element-name">deserialize</span><wbr><span class="parameters">(net.minecraft.network.FriendlyByteBuf&nbsp;buffer)</span></div>
<dl class="notes"></dl>
:::


</section>

<section id="serialize(net.minecraft.network.FriendlyByteBuf,net.minecraft.world.level.block.state.BlockState)">

:::tabs
== serialize
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type">void</span>&nbsp;<span class="element-name">serialize</span><wbr><span class="parameters">(net.minecraft.network.FriendlyByteBuf&nbsp;buf,
 net.minecraft.world.level.block.state.BlockState&nbsp;blockState)</span></div>
<dl class="notes"></dl>
:::


</section>

:::::
  

