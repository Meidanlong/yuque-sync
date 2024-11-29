---
layout: home

hero:
  name: MeiBlog        # `text` 上方的字符，带有品牌颜色
  text: 梅丹隆的个人博客   #hero 部分的主要文字，被定义为 `h1` 标签
  tagline: Break down. Build up.   # `text` 下方的标语
  image:
    src: /hero.png           # text 和 tagline 区域旁的图片
    alt: 头像不是在摸鱼           # 图片的alt文字
  actions:
    - theme: brand           # 按钮的颜色主题，默认为 `brand`
      text: Get Started      # 按钮的标签
      link: /guide/what-is-vitepress # 按钮的目标链接
      target: _blank        #可选的内容 链接的 target 属性，如果使用_blank,可以在浏览器重新打开一个标签
      rel:                  #可选的内容
    - theme: alt
      text: View on GitHub
      link: https://github.com/vuejs/vitepress

features:
  - icon: 🛠️                             # 在每个 feature 框中显示图标
    title: 系统教程                       # feature 的标题
    details: 程序员的系统教程              # feature 的详情
    link: /系统教程/VitePress/01.【邂逅初遇】VitePress介绍和安装   #  链接
    linkText: more
  - icon:
      src: /cool-feature-icon.svg
    title: Another cool feature
    details: Lorem ipsum...
  - icon:
      dark: /dark-feature-icon.svg        #黑色主题下的图标
      light: /light-feature-icon.svg      #白色主题下的图标
    title: Another cool feature
    details: Lorem ipsum...
---