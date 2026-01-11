import {defineConfig} from 'vitepress'
// @ts-ignore
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite';
import {PrimeVueResolver} from '@primevue/auto-import-resolver';
import {generateSidebar} from "vitepress-sidebar";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Chisels & Bits - Documentation",
  description: "The documentation for the Minecraft mod Chisels & Bits",

  // Static head tags
  head: [
    ["link", {rel: "icon", sizes: "32x32", href: "/favicon.png"}],
    ["link", {rel: "license", href: "https://github.com/FabricMC/fabric-docs/blob/-/LICENSE"}],
    ["meta", {name: "theme-color", content: "#943D47"}],
    ["meta", {name: "twitter:card", content: "summary"}],
  ],

  metaChunk: true,

  themeConfig: {
    logo: '/icon.png',

    // https://vitepress.dev/reference/default-theme-config
    sidebar: generateSidebar([
      {
        documentRootPath: '/docs/players',
        basePath: '/docs/players/',
        resolvePath: '/docs/players/',
        useTitleFromFrontmatter: true,
        useFolderTitleFromIndexFile: true,
        frontmatterTitleFieldName: 'title',
        sortMenusByFrontmatterOrder: true,
        capitalizeFirst: true,
        hyphenToSpace: true,
        collapsed: false,
        debugPrint: true,
      },
      {
        documentRootPath: '/docs/modders',
        basePath: '/docs/modders/',
        resolvePath: '/docs/modders/',
        useTitleFromFrontmatter: true,
        useFolderTitleFromIndexFile: true,
        frontmatterTitleFieldName: 'title',
        sortMenusByFrontmatterOrder: true,
        capitalizeFirst: true,
        hyphenToSpace: true,
        collapsed: false,
        debugPrint: true,
      }]),

    search: {
      provider: 'local'
    },

    socialLinks: [
      {icon: 'curseforge', link: 'https://www.curseforge.com/members/chiselsandbits/projects'},
      {icon: 'github', link: 'https://github.com/ChiselsAndBits'}
    ]
  },
  vite: {
    plugins: [
      Components({
        resolvers: [
          PrimeVueResolver()
        ]
      })
    ]
  }
})
