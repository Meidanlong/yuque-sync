import {defineConfig} from 'vitepress'
// import markdownItAnchor from 'markdown-it-anchor'
// import markdownItFoo from 'markdown-it-foo'
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
  },
  // markdown: {
  //   // markdown-it-anchor 的选项
  //   // https://github.com/valeriangalliat/markdown-it-anchor#usage
  //   anchor: {
  //     permalink: markdownItAnchor.permalink.headerLink()
  //   },
  //   // @mdit-vue/plugin-toc 的选项
  //   // https://github.com/mdit-vue/mdit-vue/tree/main/packages/plugin-toc#options
  //   toc: { level: [1, 2] },
  //   config: (md) => {
  //     // 使用更多的 Markdown-it 插件！
  //     md.use(markdownItFoo)
  //   }
  // }
})
