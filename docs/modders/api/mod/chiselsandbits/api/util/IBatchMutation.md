--- 
title: IBatchMutation
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.util](index.md)  
# Interface IBatchMutation  
**All Extended Interfaces:**  
AutoCloseable  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IBatchMutation</span><span class="extends-implements"><br/>  
extends <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang" class="external-link">AutoCloseable</a></span></div>  

  

Marker interface which represents a batch mutation
 update handler, which can be used with a try-with-resources
 mechanic to control the update process of a batch mutation.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Summary  
:::tabs key:method-summary-table
== All Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#close()" class="member-name-link">close</a>()</code></td><td><div class="block">Closes this resource, relinquishing any underlying resources.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#close()" class="member-name-link">close</a>()</code></td><td><div class="block">Closes this resource, relinquishing any underlying resources.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>void</code></td><td><code><a href="#close()" class="member-name-link">close</a>()</code></td><td><div class="block">Closes this resource, relinquishing any underlying resources.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="close()">

:::tabs
== close
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">close</span>()</div>
Closes this resource, relinquishing any underlying resources. This method is invoked automatically on objects managed by the <code>try</code>-with-resources statement.

 <p>While this interface method is declared to throw <code>
 Exception</code>, implementers are </p><em>strongly</em> encouraged to declare concrete implementations of the <code>close</code> method to throw more specific exceptions, or to throw no
 exception at all if the close operation cannot fail.

 <p> Cases where the close operation may fail require careful
 attention by implementers. It is strongly advised to relinquish the underlying resources and to internally </p><em>mark</em> the resource as closed, prior to throwing the
 exception. The <code>close</code> method is unlikely to be invoked more than once and so this ensures that the resources are released in a timely manner. Furthermore it reduces
 problems that could arise when the resource wraps, or is wrapped, by another resource.

 <p></p><em>Implementers of this interface are also strongly advised
 to not have the <code>close</code> method throw <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang" class="external-link"><code>InterruptedException</code></a>.</em>
 <p>
 This exception interacts with a thread's interrupted status, and runtime misbehavior is likely to occur if an <code>InterruptedException</code> is <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)" title="class or interface in java.lang" class="external-link">suppressed</a>.
 </p><p>
 More generally, if it would cause problems for an exception to be suppressed, the <code>AutoCloseable.close</code> method should not throw it.

 </p><p>Note that unlike the <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html#close()" title="class or interface in java.io" class="external-link"><code>close</code></a>
 method of <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io" class="external-link"><code>Closeable</code></a>, this <code>close</code> method is </p><em>not</em> required to be idempotent.  In other words, calling this <code>close</code> method more than once may have
 some visible side effect, unlike <code>Closeable.close</code> which is required to have no effect if called more than once.
 <p>
 However, implementers of this interface are strongly encouraged to make their <code>close</code> methods idempotent.</p>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close()" title="class or interface in java.lang" class="external-link">close</a></code>&nbsp;in interface&nbsp;<code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang" class="external-link">AutoCloseable</a></code></dd>
</dl>
:::


</section>

:::::
  

