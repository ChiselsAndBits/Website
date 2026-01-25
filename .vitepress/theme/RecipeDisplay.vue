<script setup lang="ts">
import type {Recipe} from "./DisplayRecipe.ts";
import RecipeElement from "./RecipeElement.vue";

interface Properties {
  recipe: Recipe
}

const properties = defineProps<Properties>()
</script>

<template>
  <div class="summary-recipe" v-if="recipe">
    <h3>Recipe</h3>
    <div class="summary-recipe-table">
      <table>
        <tr v-for="recipeRow in recipe.contents">
          <td v-for="recipeCharacter in recipeRow">
            <RecipeElement v-if="recipe.ingredients[recipeCharacter] != null" :ingredient="recipe.ingredients[recipeCharacter]" />
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<style scoped>
h3 {
  font-size: 18px;
  text-align: center;
  padding-bottom: 0.25rem;
  margin-bottom: 0.25rem;
  margin-top: 0.5rem;
  padding-top: 0.25rem;
  border-top: 1px solid var(--vp-c-divider);
}

.summary-recipe {
  margin: 0 auto 1rem auto;
}
.summary-recipe-table {
  justify-content: center !important;
  display: flex;
  height: 136px;
  width: 192px;
}
.summary-recipe-table table {
  border-collapse: collapse;
  border: none;
}
.summary-recipe-table td,
.summary-recipe-table th {
  border: none;
  position: relative;
  margin: 2px;
  padding: 6px;
  width: 47px;
  height: 46px;
}
.summary-recipe-table td:not(:last-child),
.summary-recipe-table th:not(:last-child) {
  border-right: 2px solid var(--vp-c-divider)
}
.summary-recipe-table tr:not(:last-child) td,
.summary-recipe-table tr:not(:last-child) th {
  border-bottom: 2px solid var(--vp-c-divider)
}
</style>

