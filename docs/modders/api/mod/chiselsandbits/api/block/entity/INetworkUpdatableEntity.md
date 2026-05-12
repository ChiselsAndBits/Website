--- 
title: INetworkUpdatableEntity
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.block.entity](index.md)  
# Interface INetworkUpdatableEntity\<TPayload\>  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">INetworkUpdatableEntity&lt;TPayload&gt;</span></div>  

  

Marks the entity as a network updatable entity.  

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
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#blockPos()" class="member-name-link">blockPos</a>()</code></td><td><div class="block">Returns The position of the block..</div><br></td></tr>
  <tr><td><code><a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a></code></td><td><code><a href="#payload()" class="member-name-link">payload</a>()</code></td><td><div class="block">Returns The payload to transfer..</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#receivePayload(TPayload)" class="member-name-link">receivePayload</a><wbr>(<a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a>&nbsp;payload)</code></td><td><div class="block">Called when the client receives a payload useful for updating the entity.</div><br></td></tr>
  <tr><td><code>net.minecraft.core.RegistryAccess</code></td><td><code><a href="#registryAccess()" class="member-name-link">registryAccess</a>()</code></td><td><div class="block">Returns The registry access for this entity..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec used to serialize the payload..</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#blockPos()" class="member-name-link">blockPos</a>()</code></td><td><div class="block">Returns The position of the block..</div><br></td></tr>
  <tr><td><code><a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a></code></td><td><code><a href="#payload()" class="member-name-link">payload</a>()</code></td><td><div class="block">Returns The payload to transfer..</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#receivePayload(TPayload)" class="member-name-link">receivePayload</a><wbr>(<a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a>&nbsp;payload)</code></td><td><div class="block">Called when the client receives a payload useful for updating the entity.</div><br></td></tr>
  <tr><td><code>net.minecraft.core.RegistryAccess</code></td><td><code><a href="#registryAccess()" class="member-name-link">registryAccess</a>()</code></td><td><div class="block">Returns The registry access for this entity..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec used to serialize the payload..</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code>net.minecraft.core.BlockPos</code></td><td><code><a href="#blockPos()" class="member-name-link">blockPos</a>()</code></td><td><div class="block">Returns The position of the block..</div><br></td></tr>
  <tr><td><code><a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a></code></td><td><code><a href="#payload()" class="member-name-link">payload</a>()</code></td><td><div class="block">Returns The payload to transfer..</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#receivePayload(TPayload)" class="member-name-link">receivePayload</a><wbr>(<a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a>&nbsp;payload)</code></td><td><div class="block">Called when the client receives a payload useful for updating the entity.</div><br></td></tr>
  <tr><td><code>net.minecraft.core.RegistryAccess</code></td><td><code><a href="#registryAccess()" class="member-name-link">registryAccess</a>()</code></td><td><div class="block">Returns The registry access for this entity..</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns The stream codec used to serialize the payload..</div><br></td></tr>
  </tbody>
</table>
:::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<ul class="member-list">
<li>
<section id="registryAccess()">

:::tabs
== registryAccess
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.core.RegistryAccess</span>&nbsp;<span class="element-name">registryAccess</span>()</div>
<div class="block">Returns The registry access for this entity..</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The registry access for this entity.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="blockPos()">

:::tabs
== blockPos
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.core.BlockPos</span>&nbsp;<span class="element-name">blockPos</span>()</div>
<div class="block">Returns The position of the block..</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The position of the block.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="payload()">

:::tabs
== payload
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type"><a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a></span>&nbsp;<span class="element-name">payload</span>()</div>
<div class="block">Returns The payload to transfer..</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The payload to transfer.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="streamCodec()">

:::tabs
== streamCodec
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">net.minecraft.network.codec.StreamCodec&lt;net.minecraft.network.RegistryFriendlyByteBuf, <a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
<div class="block">Returns The stream codec used to serialize the payload..</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The stream codec used to serialize the payload.</dd>
</dl>
</div>
:::


</section>

</li>
<li>
<section id="receivePayload(TPayload)">

:::tabs
== receivePayload
<div class="horizontal-scroll">
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">receivePayload</span><wbr><span class="parameters">(<a href="#type-param-TPayload" title="type parameter in INetworkUpdatableEntity">TPayload</a>&nbsp;payload)</span></div>
<div class="block">Called when the client receives a payload useful for updating the entity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>payload</code> - The payload to receive.</dd>
</dl>
</div>
:::


</section>

</li>
</ul>
:::::
  

