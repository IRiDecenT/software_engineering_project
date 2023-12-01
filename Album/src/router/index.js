import { createRouter, createWebHistory } from "vue-router"

import Login from "@/views/Login/LoginIndex.vue"
import HomePage from "@/views/Home/HomePageIndex.vue"
import UserInfo from "@/views/UserInfo/UserInfoIndex.vue"
import Demo from "@/views/Demo/Demo1Index.vue"

const routes = [
    {    path: '/login', component: Login },
    {    path: '/index/uid=:id', component: HomePage },
    {    path: '/userinfo', component: UserInfo },
    {    path: '/', redirect: '/login' },
    {    path: '/demo/uid=:id', component: Demo },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router

