import DefaultTheme from 'vitepress/theme'
// @ts-ignore
import WithPageSummary from './WithPageSummary.vue'
import PrimeVue from 'primevue/config';
// @ts-ignore
import Aura from '@primeuix/themes/aura';
// @ts-ignore
import ItemIcon from './ItemIcon.vue';
// @ts-ignore
import RecipeElement from './RecipeElement.vue';
// @ts-ignore
import RecipeDisplay from './RecipeDisplay.vue';


export default {
    extends: DefaultTheme,
    // override the Layout with a wrapper component that
    // injects the slots
    Layout: WithPageSummary,
    enhanceApp({ app }) {
        console.log("Loaded custom theme")

        app.use(PrimeVue, {
            theme: {
                preset: Aura
            }
        })

        app.component('ItemIcon', ItemIcon)
        app.component('RecipeElement', RecipeElement)
        app.component('RecipeDisplay', RecipeDisplay)
    }
}