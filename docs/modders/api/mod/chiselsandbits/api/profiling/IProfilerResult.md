--- 
title: IProfilerResult
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.profiling](index)  
# Interface IProfilerResult  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IProfilerResult</span></div>  

  

The result of a profiling operation.  

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
  <tr><td><code>void</code></td><td><code><a href="#writeAsResponse(java.util.function.Consumer)" class="member-name-link">writeAsResponse</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;lineConsumer)</code></td><td><div class="block">Writes all profiling result data in a readable manor into the given consumer, allows for the outputting of the results to a player in chat, or the server console.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#writeToFile(java.nio.file.Path)" class="member-name-link">writeToFile</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file" class="external-link">Path</a>&nbsp;file)</code></td><td><div class="block">Writes all profiling result data to the given file.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#writeAsResponse(java.util.function.Consumer)" class="member-name-link">writeAsResponse</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;lineConsumer)</code></td><td><div class="block">Writes all profiling result data in a readable manor into the given consumer, allows for the outputting of the results to a player in chat, or the server console.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#writeToFile(java.nio.file.Path)" class="member-name-link">writeToFile</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file" class="external-link">Path</a>&nbsp;file)</code></td><td><div class="block">Writes all profiling result data to the given file.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#writeAsResponse(java.util.function.Consumer)" class="member-name-link">writeAsResponse</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;lineConsumer)</code></td><td><div class="block">Writes all profiling result data in a readable manor into the given consumer, allows for the outputting of the results to a player in chat, or the server console.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#writeToFile(java.nio.file.Path)" class="member-name-link">writeToFile</a><wbr>(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file" class="external-link">Path</a>&nbsp;file)</code></td><td><div class="block">Writes all profiling result data to the given file.</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="writeToFile(java.nio.file.Path)">

:::tabs
== writeToFile
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">writeToFile</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/Path.html" title="class or interface in java.nio.file" class="external-link">Path</a>&nbsp;file)</span></div>
Writes all profiling result data to the given file. Creating it if necessary.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - The file to write to.</dd>
</dl>
</div>
:::


</section>

<section id="writeAsResponse(java.util.function.Consumer)">

:::tabs
== writeAsResponse
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">writeAsResponse</span><wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function" class="external-link">Consumer</a>&lt;<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang" class="external-link">String</a>&gt;&nbsp;lineConsumer)</span></div>
Writes all profiling result data in a readable manor into the given consumer, allows for the outputting of the results to a player in chat, or the server console.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineConsumer</code> - The line consumer.</dd>
</dl>
</div>
:::


</section>

:::::
  

