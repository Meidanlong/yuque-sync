// index.js
import DefaultTheme from 'vitepress/theme'
import './style/custom.css'
import MyLayout from "./components/BlogLayout.vue";

export default {
    ...DefaultTheme,
    Layout: MyLayout,
}