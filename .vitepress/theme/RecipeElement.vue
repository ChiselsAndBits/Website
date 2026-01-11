<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import {Ingredient, ItemIngredient} from "./DisplayRecipe";
import ItemIcon from "./ItemIcon.vue";

interface Properties {
  ingredient: Ingredient
}

function buildDisplayName(ingredient: Ingredient) : string {
  if (ingredient.isTag) {
    return buildTagDisplayName(ingredient.location)
  } else {
    return (ingredient as ItemIngredient).title
  }
}

function buildTagDisplayName(location: string) : string {
  let result = location;
  if (result.includes("_")) {
    result = location.replace("_", " ")
  } else if (location.includes("/")) {
    let elements = result.split("/")
    result = elements.reverse().join(" ")
  }

  if (result.endsWith("s")) {
    result = result.substring(0, result.length - 1);
  }

  return `Any ${result}`
}

const properties = defineProps<Properties>()

const currentNamespace = ref(properties.ingredient.namespace)
const currentLocation = ref(properties.ingredient.location)
const tagEntries = ref([])
let intervalId = null

const currentDisplayName = computed(() => buildDisplayName(properties.ingredient))

async function fetchTagEntries() {
  const url = `https://raw.githubusercontent.com/ChiselsAndBits/Assets/refs/heads/main/Metadata/Tags/minecraft/item/${properties.ingredient.namespace}/${properties.ingredient.location}.json`
  try {
    const response = await fetch(url)
    if (!response.ok) return
    const data = await response.json()
    if (Array.isArray(data) && data.length > 0) {
      tagEntries.value = data
      rotateTagEntry(0)
      if (intervalId) clearInterval(intervalId)
      intervalId = setInterval(() => {
        const idx = (tagEntries.value.findIndex(e => e.split(':')[0] === currentNamespace.value && e.split(':')[1] === currentLocation.value) + 1) % tagEntries.value.length
        rotateTagEntry(idx)
      }, 2000)
    }
  } catch (e) {
    // fail silently
  }
}

function rotateTagEntry(newIndex: number) {
  const entry = tagEntries.value[newIndex]
  if (!entry) return
  const [ns, loc] = entry.split(':')
  currentNamespace.value = ns
  currentLocation.value = loc
}

const tooltipKey = ref(0)

watch([currentNamespace, currentLocation], () => {
  tooltipKey.value++
})

onMounted(() => {
  if (properties.ingredient.isTag) {
    fetchTagEntries()
  }
})

onUnmounted(() => {
  if (intervalId) clearInterval(intervalId)
})
</script>

<template>
  <div :key="tooltipKey" v-tooltip="currentDisplayName">
    <ItemIcon :namespace="currentNamespace" :location="currentLocation" :alternative="currentDisplayName" />
  </div>
</template>

<style scoped>

</style>