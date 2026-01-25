<script setup lang="ts">
import {useData} from 'vitepress';
import DefaultTheme from 'vitepress/theme'
import RecipeDisplay from "./RecipeDisplay.vue";
import {Recipe} from "./DisplayRecipe";

interface Summary {
  icon?: string
  title: string
  summary: string
  recipe: Recipe
}

interface Frontmatter {
  summary : Summary
  title?: string
  javadoc?: boolean
}

interface Data {
  frontmatter: Frontmatter
}

const {Layout} = DefaultTheme
const data : Data = useData() as unknown as Data;
const frontmatter : Frontmatter = data.frontmatter
</script>

<template>
  <Layout>
    <template #layout-top>
      <div v-if="frontmatter.javadoc">MARKER</div>
    </template>
    <template #aside-outline-before>
      <div class="page-summary" v-if="frontmatter.summary">
        <div class="summary-icon">
          <img :src="frontmatter.summary.icon" alt="icon" v-if="frontmatter.summary.icon"/>
        </div>
        <div class="summary-description">
          <h1>{{ frontmatter.title ?? frontmatter.summary.title }}</h1>
          <p>{{ frontmatter.summary.summary }}</p>
        </div>
        <RecipeDisplay v-if="frontmatter.summary.recipe" :recipe="frontmatter.summary.recipe" :key="frontmatter.summary.title"/>
      </div>
    </template>
  </Layout>
</template>

<style scoped>
h1 {
  font-size: 20px;
  padding-bottom: 0.5rem;
  margin-bottom: 0.5rem;
  border-bottom: 1px solid var(--vp-c-divider);
}
p {
  font-size: 14px;
}
.page-summary {
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  padding: 1rem;
  z-index: 10;
  margin-bottom: 1rem;
}

.summary-icon img {
  width: 64px;
  height: 64px;
  display: block;
  margin: 0 auto 1rem auto;
}

.summary-description {
  text-align: center;
  padding-bottom: 0.25rem;
}
</style>

<style>
:root{
  --code-font-family: 'DejaVu Sans Mono', monospace;
}

.module-signature,
.package-signature,
.type-signature,
.member-signature {
  font-family:var(--code-font-family),monospace;
  font-size:1em;
  margin:14px 0;
  white-space: pre-wrap;
}
.module-signature,
.package-signature,
.type-signature {
  margin-top: 0;
}
.member-signature .type-parameters-long,
.member-signature .parameters,
.member-signature .exceptions {
  display: inline-block;
  vertical-align: top;
  white-space: pre;
}
.member-signature .type-parameters {
  white-space: normal;
}
</style>

<style>
a.anchor-link {
  text-decoration: none;
  --vp-custom-block-info-text: var(--vp-c-text-1);
  color: inherit !important;
}

a.anchor-link:hover {
  color: initial;
}

@media (min-width: 1440px) {
  .VPContent.has-sidebar {
    padding-right: initial !important;
    padding-left: initial !important;
  }
  .VPSidebar {
    padding-left: 32px !important;
    width: var(--vp-sidebar-width) !important;
  }

  .VPNavBar.has-sidebar > .wrapper > .container > .title {
    padding-left: 32px !important;
    width: initial !important;
  }

  .VPNavBar.has-sidebar > .wrapper > .container > .content {
    padding-left: var(--vp-sidebar-width);
    padding-right: calc((100% - var(--vp-layout-max-width)) / 2 + 32px);
  }

  .VPNavBar.has-sidebar .divider {
    padding-left: var(--vp-sidebar-width) !important;
  }
}

:root {
  --vp-sidebar-width: 333px !important;
}


.VPDoc:not(.has-sidebar) .container {
  max-width: initial !important;
}

.VPDoc.has-aside .content-container {
  max-width: initial !important;
  padding-left: var(--vp-sidebar-width);
}

.VPDoc:not(.has-sidebar) .content-container {
  max-width: initial !important;
  padding-left: 32px;
}

.VPDoc:not(.has-sidebar) .content {
  max-width: initial !important;
}

.pager-link {
  max-width: var(--vp-sidebar-width);
}
</style>