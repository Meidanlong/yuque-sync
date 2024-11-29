import { defineConfig } from 'vitepress'
import sidebar from './theme/script/sidebar.mjs'
import nav from './theme/script/nav.mjs'
import socialLinks from './theme/script/socialLinks.mjs'
import footer from './theme/script/footer.mjs'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "MeiBlog",
  description: "A VitePress Site",
  srcDir:'docs',
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: nav,
    sidebar: sidebar,
    socialLinks: socialLinks,
    footer: footer
  }
})
