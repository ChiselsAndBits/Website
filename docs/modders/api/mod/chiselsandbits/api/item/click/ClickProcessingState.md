--- 
title: ClickProcessingState
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.item.click](index.md)  
# Class ClickProcessingState  
java.lang.Object  
&ensp;↳mod.chiselsandbits.api.item.click.ClickProcessingState  
  
---
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ClickProcessingState</span><br/>  
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang" class="external-link">Object</a></span></div>  

  

Represents the continuous processing state of a click interaction.  

<dl class="notes"></dl>  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Nested Class Summary  
:::tabs
== Nested Classes
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Class</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>static enum&nbsp;</code></td><td><code><a href="ClickProcessingState.ProcessingResult.html" class="type-name-link" title="enum class in mod.chiselsandbits.api.item.click">ClickProcessingState.ProcessingResult</a></code></td><td><div class="block">The processing result of the click interaction.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
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
  <tr><td><code>static final <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#ALLOW" class="member-name-link">ALLOW</a></code></td><td><div class="block">The click was successfully processed, and not further processing is needed.</div><br></td></tr>
  <tr><td><code>static final <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#ALLOW_NO_CANCEL" class="member-name-link">ALLOW_NO_CANCEL</a></code></td><td><div class="block">The click was successfully processed, but the interactions processing should continue.</div><br></td></tr>
  <tr><td><code>static final <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#DEFAULT" class="member-name-link">DEFAULT</a></code></td><td><div class="block">No processing of the click was done, and the interactions processing should continue.</div><br></td></tr>
  <tr><td><code>static final <a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></code></td><td><code><a href="#DENIED" class="member-name-link">DENIED</a></code></td><td><div class="block">The click was not processed successfully, and the interactions processing should stop.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Summary  
:::tabs
== Constructors
<table>
  <thead>
    <tr><th>Constructor</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="#%3Cinit%3E(boolean,mod.chiselsandbits.api.item.click.ClickProcessingState.ProcessingResult)" class="member-name-link">ClickProcessingState</a><wbr>(boolean&nbsp;shouldCancel,<br> <a href="ClickProcessingState.ProcessingResult.html" title="enum class in mod.chiselsandbits.api.item.click">ClickProcessingState.ProcessingResult</a>&nbsp;nextState)</code></td><td><div class="block">Creates a new processing state.</div><br></td></tr>
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
  <tr><td><code><a href="ClickProcessingState.ProcessingResult.html" title="enum class in mod.chiselsandbits.api.item.click">ClickProcessingState.ProcessingResult</a></code></td><td><code><a href="#getNextState()" class="member-name-link">getNextState</a>()</code></td><td><div class="block">Gets the next state to process.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldCancel()" class="member-name-link">shouldCancel</a>()</code></td><td><div class="block">Indicates if this state should cancel the interaction.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="ClickProcessingState.ProcessingResult.html" title="enum class in mod.chiselsandbits.api.item.click">ClickProcessingState.ProcessingResult</a></code></td><td><code><a href="#getNextState()" class="member-name-link">getNextState</a>()</code></td><td><div class="block">Gets the next state to process.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldCancel()" class="member-name-link">shouldCancel</a>()</code></td><td><div class="block">Indicates if this state should cancel the interaction.</div><br></td></tr>
  </tbody>
</table>
== Concrete Methods
<table>
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="ClickProcessingState.ProcessingResult.html" title="enum class in mod.chiselsandbits.api.item.click">ClickProcessingState.ProcessingResult</a></code></td><td><code><a href="#getNextState()" class="member-name-link">getNextState</a>()</code></td><td><div class="block">Gets the next state to process.</div><br></td></tr>
  <tr><td><code>boolean</code></td><td><code><a href="#shouldCancel()" class="member-name-link">shouldCancel</a>()</code></td><td><div class="block">Indicates if this state should cancel the interaction.</div><br></td></tr>
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
<section id="ALLOW">

:::tabs
== ALLOW
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></span>&nbsp;<span class="element-name">ALLOW</span></div>
The click was successfully processed, and not further processing is needed.
<dl class="notes"></dl>
:::


</section>

<section id="ALLOW_NO_CANCEL">

:::tabs
== ALLOW_NO_CANCEL
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></span>&nbsp;<span class="element-name">ALLOW_NO_CANCEL</span></div>
The click was successfully processed, but the interactions processing should continue.
<dl class="notes"></dl>
:::


</section>

<section id="DENIED">

:::tabs
== DENIED
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></span>&nbsp;<span class="element-name">DENIED</span></div>
The click was not processed successfully, and the interactions processing should stop.
<dl class="notes"></dl>
:::


</section>

<section id="DEFAULT">

:::tabs
== DEFAULT
<div class="member-signature"><span class="modifiers">public static final</span>&nbsp;<span class="return-type"><a href="ClickProcessingState.html" title="class in mod.chiselsandbits.api.item.click">ClickProcessingState</a></span>&nbsp;<span class="element-name">DEFAULT</span></div>
No processing of the click was done, and the interactions processing should continue.
<dl class="notes"></dl>
:::


</section>

:::::
  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Constructor Details  
<section id="<init>(boolean,mod.chiselsandbits.api.item.click.ClickProcessingState.ProcessingResult)">

:::tabs
== ClickProcessingState
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="element-name">ClickProcessingState</span><wbr><span class="parameters">(boolean&nbsp;shouldCancel,
 <a href="ClickProcessingState.ProcessingResult.html" title="enum class in mod.chiselsandbits.api.item.click">ClickProcessingState.ProcessingResult</a>&nbsp;nextState)</span></div>
Creates a new processing state.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shouldCancel</code> - Indicates if the state should cancel the interaction.</dd>
<dd><code>nextState</code> - The next state to process.</dd>
</dl>
:::


</section>

:::::
  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="shouldCancel()">

:::tabs
== shouldCancel
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type">boolean</span>&nbsp;<span class="element-name">shouldCancel</span>()</div>
Indicates if this state should cancel the interaction.
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if the interaction should be cancelled, <code>false</code> otherwise.</dd>
</dl>
:::


</section>

<section id="getNextState()">

:::tabs
== getNextState
<div class="member-signature"><span class="modifiers">public</span>&nbsp;<span class="return-type"><a href="ClickProcessingState.ProcessingResult.html" title="enum class in mod.chiselsandbits.api.item.click">ClickProcessingState.ProcessingResult</a></span>&nbsp;<span class="element-name">getNextState</span>()</div>
Gets the next state to process.
<dl class="notes">
<dt>Returns:</dt>
<dd>The next processing state.</dd>
</dl>
:::


</section>

:::::
  

