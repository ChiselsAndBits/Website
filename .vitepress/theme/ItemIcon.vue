<script setup lang="ts">

interface Properties {
  namespace: string
  location: string
  alternative: string
}

defineProps<Properties>();
</script>

<template>
  <img :src="'https://raw.githubusercontent.com/ChiselsAndBits/Assets/refs/heads/main/Icons/InGame/' + namespace + '/' + location + '.png'" width="32" alt=""/>
</template>

<style scoped>
</style>