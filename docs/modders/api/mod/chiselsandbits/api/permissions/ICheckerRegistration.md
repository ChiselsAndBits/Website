--- 
title: ICheckerRegistration
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.permissions](index)  
# Interface ICheckerRegistration  
**All Extended Interfaces:**  
AutoCloseable  

---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ICheckerRegistration</span><span class="extends-implements"><br/>  
extends <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang" class="external-link">AutoCloseable</a></span></div>  

  

A marker interface which can be used to dynamically register and un-register
a <a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions"><code>IPermissionChecker</code></a> to the <a href="IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions"><code>IPermissionHandler</code></a>.

If the <a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/AutoCloseable.html#close()" title="class or interface in java.lang" class="external-link"><code>AutoCloseable.close()</code></a> is called then the <a href="IPermissionChecker.html" title="interface in mod.chiselsandbits.api.permissions"><code>IPermissionChecker</code></a> will be
unregistered from the <a href="IPermissionHandler.html" title="interface in mod.chiselsandbits.api.permissions"><code>IPermissionHandler</code></a>.  

<dl class="notes"></dl>  

<!-- ========== METHOD SUMMARY =========== -->
Method Summary  
<!-- JavaMarkContainer Depth: 1 -->
::::: tip Methods inherited from interface&nbsp;java.lang.<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang" class="external-link">AutoCloseable</a>
<a href="https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/AutoCloseable.html#close()" title="class or interface in java.lang" class="external-link">close</a>
:::::
  
  
  

  

  

  

  

  

  

