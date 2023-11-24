import { createRouter, createWebHistory } from "vue-router"

import Login from "@/views/Login/LoginIndex.vue"
import HomePage from "@/views/Home/HomePageIndex.vue"

const routes = [
    {    path: '/login', component: Login },
    {    path: '/', component: HomePage },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router

