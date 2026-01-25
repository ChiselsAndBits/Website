--- 
title: IStateVariantProvider
aside: false 
sidebar: false 
---
_Package:_ [mod.chiselsandbits.api.variant.state](index.md)  
# Interface IStateVariantProvider  
---
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">IStateVariantProvider</span></div>  

  

Represents the state variant provider, which allows external mods to provide their own state variants.  

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
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getAllDefaultVariants(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getAllDefaultVariants</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;state)</code></td><td><div class="block">Returns all the default variants for the given block state.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBeaconColorMultiplier(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.level.LevelReader,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">getBeaconColorMultiplier</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.level.LevelReader&nbsp;levelReader,<br> net.minecraft.core.BlockPos&nbsp;pos,<br> net.minecraft.core.BlockPos&nbsp;beaconPos)</code></td><td><div class="block">Returns the beacon color multiplier for the given block information.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;com.communi.suggestu.scena.core.fluid.FluidInformation&gt;</code></td><td><code><a href="#getFluidInformation(mod.chiselsandbits.api.variant.state.IStateVariant,long)" class="member-name-link">getFluidInformation</a><wbr>(<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;stateVariant,<br> long&nbsp;amount)</code></td><td><div class="block">Returns the fluid information for the given state variant.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.item.ItemStack&gt;</code></td><td><code><a href="#getItemStack(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getItemStack</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;stateVariant)</code></td><td><div class="block">Returns the item stack for the given state variant.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.network.chat.Component&gt;</code></td><td><code><a href="#getName(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getName</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;variant)</code></td><td><div class="block">Returns the name of the given state variant.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getRegistryName()" class="member-name-link">getRegistryName</a>()</code></td><td><div class="block">Returns the registry name of the provider.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(com.communi.suggestu.scena.core.fluid.FluidInformation)" class="member-name-link">getStateVariant</a><wbr>(com.communi.suggestu.scena.core.fluid.FluidInformation&nbsp;fluidInformation)</code></td><td><div class="block">Returns the state variant, if one exists, for the fluid information.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.block.state.BlockState,java.util.Optional)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.level.block.entity.BlockEntity&gt;&nbsp;blockEntity)</code></td><td><div class="block">Returns the state variant, if one exists, for the blockstate and block entity combination.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.block.state.BlockState,net.minecraft.world.item.ItemStack)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,<br> net.minecraft.world.item.ItemStack&nbsp;itemStack)</code></td><td><div class="block">Returns the state variant, if one exists, for the block state and item stack combination.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.material.FluidState)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.material.FluidState&nbsp;fluidStateIn)</code></td><td><div class="block">Returns the state variant, if one exists, for the fluid state.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns the map codec for the state variant.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setFullBlock(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setFullBlock</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;levelAccessor,<br> net.minecraft.core.BlockPos&nbsp;inWorldPos,<br> <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Sets the full block at the given position.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;? super net.minecraft.network.RegistryFriendlyByteBuf,<wbr>? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns the stream codec for the state variant.</div><br></td></tr>
  </tbody>
</table>
== Instance Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getAllDefaultVariants(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getAllDefaultVariants</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;state)</code></td><td><div class="block">Returns all the default variants for the given block state.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBeaconColorMultiplier(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.level.LevelReader,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">getBeaconColorMultiplier</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.level.LevelReader&nbsp;levelReader,<br> net.minecraft.core.BlockPos&nbsp;pos,<br> net.minecraft.core.BlockPos&nbsp;beaconPos)</code></td><td><div class="block">Returns the beacon color multiplier for the given block information.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;com.communi.suggestu.scena.core.fluid.FluidInformation&gt;</code></td><td><code><a href="#getFluidInformation(mod.chiselsandbits.api.variant.state.IStateVariant,long)" class="member-name-link">getFluidInformation</a><wbr>(<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;stateVariant,<br> long&nbsp;amount)</code></td><td><div class="block">Returns the fluid information for the given state variant.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.item.ItemStack&gt;</code></td><td><code><a href="#getItemStack(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getItemStack</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;stateVariant)</code></td><td><div class="block">Returns the item stack for the given state variant.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.network.chat.Component&gt;</code></td><td><code><a href="#getName(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getName</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;variant)</code></td><td><div class="block">Returns the name of the given state variant.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getRegistryName()" class="member-name-link">getRegistryName</a>()</code></td><td><div class="block">Returns the registry name of the provider.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(com.communi.suggestu.scena.core.fluid.FluidInformation)" class="member-name-link">getStateVariant</a><wbr>(com.communi.suggestu.scena.core.fluid.FluidInformation&nbsp;fluidInformation)</code></td><td><div class="block">Returns the state variant, if one exists, for the fluid information.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.block.state.BlockState,java.util.Optional)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.level.block.entity.BlockEntity&gt;&nbsp;blockEntity)</code></td><td><div class="block">Returns the state variant, if one exists, for the blockstate and block entity combination.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.block.state.BlockState,net.minecraft.world.item.ItemStack)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,<br> net.minecraft.world.item.ItemStack&nbsp;itemStack)</code></td><td><div class="block">Returns the state variant, if one exists, for the block state and item stack combination.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.material.FluidState)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.material.FluidState&nbsp;fluidStateIn)</code></td><td><div class="block">Returns the state variant, if one exists, for the fluid state.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns the map codec for the state variant.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setFullBlock(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setFullBlock</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;levelAccessor,<br> net.minecraft.core.BlockPos&nbsp;inWorldPos,<br> <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Sets the full block at the given position.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;? super net.minecraft.network.RegistryFriendlyByteBuf,<wbr>? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns the stream codec for the state variant.</div><br></td></tr>
  </tbody>
</table>
== Abstract Methods
<table class="stretched-table">
  <thead>
    <tr><th>Modifier and Type</th><th>Method</th><th>Description</th></tr>
  </thead>
  <tbody>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a><wbr>&lt;? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getAllDefaultVariants(net.minecraft.world.level.block.state.BlockState)" class="member-name-link">getAllDefaultVariants</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;state)</code></td><td><div class="block">Returns all the default variants for the given block state.</div><br></td></tr>
  <tr><td><code>@NotNull <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</code></td><td><code><a href="#getBeaconColorMultiplier(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.level.LevelReader,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)" class="member-name-link">getBeaconColorMultiplier</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,<br> net.minecraft.world.level.LevelReader&nbsp;levelReader,<br> net.minecraft.core.BlockPos&nbsp;pos,<br> net.minecraft.core.BlockPos&nbsp;beaconPos)</code></td><td><div class="block">Returns the beacon color multiplier for the given block information.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;com.communi.suggestu.scena.core.fluid.FluidInformation&gt;</code></td><td><code><a href="#getFluidInformation(mod.chiselsandbits.api.variant.state.IStateVariant,long)" class="member-name-link">getFluidInformation</a><wbr>(<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;stateVariant,<br> long&nbsp;amount)</code></td><td><div class="block">Returns the fluid information for the given state variant.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.world.item.ItemStack&gt;</code></td><td><code><a href="#getItemStack(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getItemStack</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;stateVariant)</code></td><td><div class="block">Returns the item stack for the given state variant.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;net.minecraft.network.chat.Component&gt;</code></td><td><code><a href="#getName(mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">getName</a><wbr>(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;variant)</code></td><td><div class="block">Returns the name of the given state variant.</div><br></td></tr>
  <tr><td><code>net.minecraft.resources.Identifier</code></td><td><code><a href="#getRegistryName()" class="member-name-link">getRegistryName</a>()</code></td><td><div class="block">Returns the registry name of the provider.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(com.communi.suggestu.scena.core.fluid.FluidInformation)" class="member-name-link">getStateVariant</a><wbr>(com.communi.suggestu.scena.core.fluid.FluidInformation&nbsp;fluidInformation)</code></td><td><div class="block">Returns the state variant, if one exists, for the fluid information.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.block.state.BlockState,java.util.Optional)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,<br> <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.level.block.entity.BlockEntity&gt;&nbsp;blockEntity)</code></td><td><div class="block">Returns the state variant, if one exists, for the blockstate and block entity combination.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.block.state.BlockState,net.minecraft.world.item.ItemStack)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,<br> net.minecraft.world.item.ItemStack&nbsp;itemStack)</code></td><td><div class="block">Returns the state variant, if one exists, for the block state and item stack combination.</div><br></td></tr>
  <tr><td><code><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a><wbr>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#getStateVariant(net.minecraft.world.level.material.FluidState)" class="member-name-link">getStateVariant</a><wbr>(net.minecraft.world.level.material.FluidState&nbsp;fluidStateIn)</code></td><td><div class="block">Returns the state variant, if one exists, for the fluid state.</div><br></td></tr>
  <tr><td><code>com.mojang.serialization.MapCodec<wbr>&lt;? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#mapCodec()" class="member-name-link">mapCodec</a>()</code></td><td><div class="block">Returns the map codec for the state variant.</div><br></td></tr>
  <tr><td><code>void</code></td><td><code><a href="#setFullBlock(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,mod.chiselsandbits.api.blockinformation.BlockInformation)" class="member-name-link">setFullBlock</a><wbr>(net.minecraft.world.level.LevelAccessor&nbsp;levelAccessor,<br> net.minecraft.core.BlockPos&nbsp;inWorldPos,<br> <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</code></td><td><div class="block">Sets the full block at the given position.</div><br></td></tr>
  <tr><td><code>net.minecraft.network.codec.StreamCodec<wbr>&lt;? super net.minecraft.network.RegistryFriendlyByteBuf,<wbr>? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</code></td><td><code><a href="#streamCodec()" class="member-name-link">streamCodec</a>()</code></td><td><div class="block">Returns the stream codec for the state variant.</div><br></td></tr>
  </tbody>
</table>
:::
:::::
  
  
  

  

  

  

  

  

<!-- JavaMarkContainer Depth: 1 -->
::::: info Method Details  
<section id="getRegistryName()">

:::tabs
== getRegistryName
<div class="member-signature"><span class="return-type">net.minecraft.resources.Identifier</span>&nbsp;<span class="element-name">getRegistryName</span>()</div>
Returns the registry name of the provider.
<dl class="notes">
<dt>Returns:</dt>
<dd>The registry name.</dd>
</dl>
:::


</section>

<section id="getStateVariant(net.minecraft.world.level.block.state.BlockState,java.util.Optional)">

:::tabs
== getStateVariant
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">getStateVariant</span><wbr><span class="parameters">(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,
 <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.level.block.entity.BlockEntity&gt;&nbsp;blockEntity)</span></div>
Returns the state variant, if one exists, for the blockstate and block entity combination.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockState</code> - The block state.</dd>
<dd><code>blockEntity</code> - The block entity.</dd>
<dt>Returns:</dt>
<dd>The state variant, if one exists.</dd>
</dl>
:::


</section>

<section id="getStateVariant(net.minecraft.world.level.material.FluidState)">

:::tabs
== getStateVariant
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">getStateVariant</span><wbr><span class="parameters">(net.minecraft.world.level.material.FluidState&nbsp;fluidStateIn)</span></div>
Returns the state variant, if one exists, for the fluid state.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fluidStateIn</code> - The fluid state.</dd>
<dt>Returns:</dt>
<dd>The state variant, if one exists.</dd>
</dl>
:::


</section>

<section id="getStateVariant(net.minecraft.world.level.block.state.BlockState,net.minecraft.world.item.ItemStack)">

:::tabs
== getStateVariant
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">getStateVariant</span><wbr><span class="parameters">(net.minecraft.world.level.block.state.BlockState&nbsp;blockState,
 net.minecraft.world.item.ItemStack&nbsp;itemStack)</span></div>
Returns the state variant, if one exists, for the block state and item stack combination.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockState</code> - The block state.</dd>
<dd><code>itemStack</code> - The item stack.</dd>
<dt>Returns:</dt>
<dd>The state variant, if one exists.</dd>
</dl>
:::


</section>

<section id="getStateVariant(com.communi.suggestu.scena.core.fluid.FluidInformation)">

:::tabs
== getStateVariant
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">getStateVariant</span><wbr><span class="parameters">(com.communi.suggestu.scena.core.fluid.FluidInformation&nbsp;fluidInformation)</span></div>
Returns the state variant, if one exists, for the fluid information.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fluidInformation</code> - The fluid information.</dd>
<dt>Returns:</dt>
<dd>The state variant, if one exists.</dd>
</dl>
:::


</section>

<section id="getAllDefaultVariants(net.minecraft.world.level.block.state.BlockState)">

:::tabs
== getAllDefaultVariants
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util" class="external-link">Collection</a>&lt;? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">getAllDefaultVariants</span><wbr><span class="parameters">(net.minecraft.world.level.block.state.BlockState&nbsp;state)</span></div>
Returns all the default variants for the given block state.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - The block state.</dd>
<dt>Returns:</dt>
<dd>The default variants.</dd>
</dl>
:::


</section>

<section id="getItemStack(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== getItemStack
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.world.item.ItemStack&gt;</span>&nbsp;<span class="element-name">getItemStack</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;stateVariant)</span></div>
Returns the item stack for the given state variant.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateVariant</code> - The state variant.</dd>
<dt>Returns:</dt>
<dd>The item stack.</dd>
</dl>
:::


</section>

<section id="getFluidInformation(mod.chiselsandbits.api.variant.state.IStateVariant,long)">

:::tabs
== getFluidInformation
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;com.communi.suggestu.scena.core.fluid.FluidInformation&gt;</span>&nbsp;<span class="element-name">getFluidInformation</span><wbr><span class="parameters">(<a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&nbsp;stateVariant,
 long&nbsp;amount)</span></div>
Returns the fluid information for the given state variant.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stateVariant</code> - The state variant.</dd>
<dd><code>amount</code> - The amount of fluid.</dd>
<dt>Returns:</dt>
<dd>The fluid information.</dd>
</dl>
:::


</section>

<section id="getName(mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== getName
<div class="member-signature"><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;net.minecraft.network.chat.Component&gt;</span>&nbsp;<span class="element-name">getName</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;variant)</span></div>
Returns the name of the given state variant.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variant</code> - The state variant to get the name for.</dd>
<dt>Returns:</dt>
<dd>The name of the variant if present.</dd>
</dl>
:::


</section>

<section id="mapCodec()">

:::tabs
== mapCodec
<div class="member-signature"><span class="return-type">com.mojang.serialization.MapCodec&lt;? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">mapCodec</span>()</div>
Returns the map codec for the state variant.
<dl class="notes">
<dt>Returns:</dt>
<dd>The map codec.</dd>
</dl>
:::


</section>

<section id="streamCodec()">

:::tabs
== streamCodec
<div class="member-signature"><span class="return-type">net.minecraft.network.codec.StreamCodec&lt;? super net.minecraft.network.RegistryFriendlyByteBuf,<wbr>? extends <a href="IStateVariant.html" title="interface in mod.chiselsandbits.api.variant.state">IStateVariant</a>&gt;</span>&nbsp;<span class="element-name">streamCodec</span>()</div>
Returns the stream codec for the state variant.
<dl class="notes">
<dt>Returns:</dt>
<dd>The stream codec.</dd>
</dl>
:::


</section>

<section id="setFullBlock(net.minecraft.world.level.LevelAccessor,net.minecraft.core.BlockPos,mod.chiselsandbits.api.blockinformation.BlockInformation)">

:::tabs
== setFullBlock
<div class="member-signature"><span class="return-type">void</span>&nbsp;<span class="element-name">setFullBlock</span><wbr><span class="parameters">(net.minecraft.world.level.LevelAccessor&nbsp;levelAccessor,
 net.minecraft.core.BlockPos&nbsp;inWorldPos,
 <a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation)</span></div>
Sets the full block at the given position.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>levelAccessor</code> - The level accessor.</dd>
<dd><code>inWorldPos</code> - The position in the world.</dd>
<dd><code>blockInformation</code> - The block information.</dd>
</dl>
:::


</section>

<section id="getBeaconColorMultiplier(mod.chiselsandbits.api.blockinformation.BlockInformation,net.minecraft.world.level.LevelReader,net.minecraft.core.BlockPos,net.minecraft.core.BlockPos)">

:::tabs
== getBeaconColorMultiplier
<div class="member-signature"><span class="annotations">@NotNull
</span><span class="return-type">@NotNull <a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html" title="class or interface in java.util" class="external-link">Optional</a>&lt;<a href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang" class="external-link">Integer</a>&gt;</span>&nbsp;<span class="element-name">getBeaconColorMultiplier</span><wbr><span class="parameters">(<a href="../../blockinformation/BlockInformation.html" title="class in mod.chiselsandbits.api.blockinformation">BlockInformation</a>&nbsp;blockInformation,
 net.minecraft.world.level.LevelReader&nbsp;levelReader,
 net.minecraft.core.BlockPos&nbsp;pos,
 net.minecraft.core.BlockPos&nbsp;beaconPos)</span></div>
Returns the beacon color multiplier for the given block information.
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockInformation</code> - The block information.</dd>
<dd><code>levelReader</code> - The level reader.</dd>
<dd><code>pos</code> - The position.</dd>
<dd><code>beaconPos</code> - The beacon position.</dd>
<dt>Returns:</dt>
<dd>The beacon color multiplier.</dd>
</dl>
:::


</section>

:::::
  

