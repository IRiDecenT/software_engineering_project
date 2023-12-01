import { createRouter, createWebHistory } from "vue-router"

import Login from "@/views/Login/LoginIndex.vue"
import HomePage from "@/views/Home/HomePageIndex.vue"
import UserInfo from "@/views/UserInfo/UserInfoIndex.vue"

const routes = [
    {    path: '/login', component: Login },
    {    path: '/index/:id', component: HomePage },
    {    path: '/userinfo', component: UserInfo },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router

