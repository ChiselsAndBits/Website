--- 
title: PlacementResult
aside: false 
---
_Package:_ [mod.chiselsandbits.api.placement](index.md)  
# Class PlacementResult  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.placement.PlacementResult  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">PlacementResult</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

<div class="block">Represents a result of a placement attempt.</div>
  

<dl class="notes"></dl>  

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
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(java.util.function.Function)" class="member-name-link">failure</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor)</code></td><td><div class="block">Creates a new failed placement result with specified client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(java.util.function.Function,net.minecraft.network.chat.Component)" class="member-name-link">failure</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Creates a new failed placement result with specified failure message and client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(org.joml.Vector4f)" class="member-name-link">failure</a><wbr>(org.joml.Vector4f&nbsp;color)</code></td><td><div class="block">Creates a new failed placement result with specified color.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(org.joml.Vector4f,net.minecraft.network.chat.Component)" class="member-name-link">failure</a><wbr>(org.joml.Vector4f&nbsp;color,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Creates a new failed placement result with specified color and failure message.</div><br></td></tr>
  <tr><td><code>org.joml.Vector4f</code></td><td><code><a href="#getColor()" class="member-name-link">getColor</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.chat.Component</code></td><td><code><a href="#getFailureMessage()" class="member-name-link">getFailureMessage</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isSuccess()" class="member-name-link">isSuccess</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success()" class="member-name-link">success</a>()</code></td><td><div class="block">Creates a new successful placement result with client config specified color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success(java.util.function.Function)" class="member-name-link">success</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor)</code></td><td><div class="block">Creates a new successful placement result with specified client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success(org.joml.Vector4f)" class="member-name-link">success</a><wbr>(org.joml.Vector4f&nbsp;color)</code></td><td><div class="block">Creates a new successful placement result with specified color.</div><br></td></tr>
  </tbody>
</table>
== Static Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(java.util.function.Function)" class="member-name-link">failure</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor)</code></td><td><div class="block">Creates a new failed placement result with specified client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(java.util.function.Function,net.minecraft.network.chat.Component)" class="member-name-link">failure</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Creates a new failed placement result with specified failure message and client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(org.joml.Vector4f)" class="member-name-link">failure</a><wbr>(org.joml.Vector4f&nbsp;color)</code></td><td><div class="block">Creates a new failed placement result with specified color.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(org.joml.Vector4f,net.minecraft.network.chat.Component)" class="member-name-link">failure</a><wbr>(org.joml.Vector4f&nbsp;color,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Creates a new failed placement result with specified color and failure message.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success()" class="member-name-link">success</a>()</code></td><td><div class="block">Creates a new successful placement result with client config specified color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success(java.util.function.Function)" class="member-name-link">success</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor)</code></td><td><div class="block">Creates a new successful placement result with specified client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success(org.joml.Vector4f)" class="member-name-link">success</a><wbr>(org.joml.Vector4f&nbsp;color)</code></td><td><div class="block">Creates a new successful placement result with specified color.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>org.joml.Vector4f</code></td><td><code><a href="#getColor()" class="member-name-link">getColor</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.chat.Component</code></td><td><code><a href="#getFailureMessage()" class="member-name-link">getFailureMessage</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isSuccess()" class="member-name-link">isSuccess</a>()</code></td><td>&nbsp;</td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(java.util.function.Function)" class="member-name-link">failure</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor)</code></td><td><div class="block">Creates a new failed placement result with specified client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(java.util.function.Function,net.minecraft.network.chat.Component)" class="member-name-link">failure</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Creates a new failed placement result with specified failure message and client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(org.joml.Vector4f)" class="member-name-link">failure</a><wbr>(org.joml.Vector4f&nbsp;color)</code></td><td><div class="block">Creates a new failed placement result with specified color.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#failure(org.joml.Vector4f,net.minecraft.network.chat.Component)" class="member-name-link">failure</a><wbr>(org.joml.Vector4f&nbsp;color,<br> net.minecraft.network.chat.Component&nbsp;message)</code></td><td><div class="block">Creates a new failed placement result with specified color and failure message.</div><br></td></tr>
  <tr><td><code>org.joml.Vector4f</code></td><td><code><a href="#getColor()" class="member-name-link">getColor</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>net.minecraft.network.chat.Component</code></td><td><code><a href="#getFailureMessage()" class="member-name-link">getFailureMessage</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#isSuccess()" class="member-name-link">isSuccess</a>()</code></td><td>&nbsp;</td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success()" class="member-name-link">success</a>()</code></td><td><div class="block">Creates a new successful placement result with client config specified color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success(java.util.function.Function)" class="member-name-link">success</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor)</code></td><td><div class="block">Creates a new successful placement result with specified client config color if clientside.</div><br></td></tr>
  <tr><td><code>static <a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></code></td><td><code><a href="#success(org.joml.Vector4f)" class="member-name-link">success</a><wbr>(org.joml.Vector4f&nbsp;color)</code></td><td><div class="block">Creates a new successful placement result with specified color.</div><br></td></tr>
  </tbody>
</table>
:::
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from class&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a>
<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang" class="external-link">clone</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang" class="external-link">equals</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang" class="external-link">finalize</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang" class="external-link">getClass</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang" class="external-link">hashCode</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang" class="external-link">notify</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang" class="external-link">notifyAll</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang" class="external-link">toString</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang" class="external-link">wait</a>, <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang" class="external-link">wait</a>
:::::
:::::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="success()">

:::tabs
== success
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">success</span>()</div>
<div class="block">Creates a new successful placement result with client config specified color if clientside.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>A new result indicating successful placement.</dd>
</dl>
:::


</section>

<section id="success(java.util.function.Function)">

:::tabs
== success
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">success</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor)</span></div>
<div class="block">Creates a new successful placement result with specified client config color if clientside.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clientColor</code> - The client config specified color of the ghost or wireframe to indicate the failure type.</dd>
<dt>Returns:</dt>
<dd>A new result indicating successful placement.</dd>
</dl>
:::


</section>

<section id="failure(java.util.function.Function)">

:::tabs
== failure
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">failure</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor)</span></div>
<div class="block">Creates a new failed placement result with specified client config color if clientside.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clientColor</code> - The client config specified color of the ghost or wireframe to indicate the failure type.</dd>
<dt>Returns:</dt>
<dd>A new result indicating failed placement.</dd>
</dl>
:::


</section>

<section id="failure(java.util.function.Function,net.minecraft.network.chat.Component)">

:::tabs
== failure
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">failure</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function" class="external-link">Function</a>&lt;<a href="../config/IClientConfiguration.html" title="interface in mod.chiselsandbits.api.config">IClientConfiguration</a>,<wbr><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function" class="external-link">Supplier</a>&lt;org.joml.Vector4f&gt;&gt;&nbsp;clientColor,
 net.minecraft.network.chat.Component&nbsp;message)</span></div>
<div class="block">Creates a new failed placement result with specified failure message and client config color if clientside.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clientColor</code> - The client config specified color of the ghost or wireframe to indicate the failure type.</dd>
<dd><code>message</code> - The message to show to the user.</dd>
<dt>Returns:</dt>
<dd>A new result indicating failed placement.</dd>
</dl>
:::


</section>

<section id="success(org.joml.Vector4f)">

:::tabs
== success
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">success</span><wbr><span class="parameters">(org.joml.Vector4f&nbsp;color)</span></div>
<div class="block">Creates a new successful placement result with specified color.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>color</code> - The color of the ghost or wireframe to indicate the success type.</dd>
<dt>Returns:</dt>
<dd>A new result indicating successful placement.</dd>
</dl>
:::


</section>

<section id="failure(org.joml.Vector4f)">

:::tabs
== failure
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">failure</span><wbr><span class="parameters">(org.joml.Vector4f&nbsp;color)</span></div>
<div class="block">Creates a new failed placement result with specified color.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>color</code> - The color of the ghost or wireframe to indicate the failure type.</dd>
<dt>Returns:</dt>
<dd>A new result indicating failed placement.</dd>
</dl>
:::


</section>

<section id="failure(org.joml.Vector4f,net.minecraft.network.chat.Component)">

:::tabs
== failure
<div class="member-signature"><span class="modifiers">public static</span>&nbsp;<span class="return-type"><a href="PlacementResult.html" title="class in mod.chiselsandbits.api.placement">PlacementResult</a></span>&nbsp;<span class="element-name">failure</span><wbr><span class="parameters">(org.joml.Vector4f&nbsp;color,
 net.minecraft.network.chat.Component&nbsp;message)</span></div>
<div class="block">Creates a new failed placement result with specified color and failure message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>color</code> - The color of the ghost or wireframe to indicate the failure type.</dd>
<dd><code>message</code> - The message to show to the user.</dd>
<dt>Returns:</dt>
<dd>A new result indicating failed placement.</dd>
</dl>
:::


</section>

<section id="isSuccess()">

:::tabs
== isSuccess
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">isSuccess</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getColor()">

:::tabs
== getColor
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">org.joml.Vector4f</span>&nbsp;<span class="element-name">getColor</span>()</div>
<dl class="notes"></dl>
:::


</section>

<section id="getFailureMessage()">

:::tabs
== getFailureMessage
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">net.minecraft.network.chat.Component</span>&nbsp;<span class="element-name">getFailureMessage</span>()</div>
<dl class="notes"></dl>
:::


</section>

:::::
  

