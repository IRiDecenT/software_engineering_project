import { createRouter, createWebHistory } from "vue-router"

import Login from "@/views/Login/LoginIndex.vue"
import HomePage from "@/views/Home/HomePageIndex.vue"
import UserInfo from "@/views/UserInfo/UserInfoIndex.vue"
import Demo from "@/views/Demo/Demo1Index.vue"


// 查询参数（如 ?uid=1）不需要在路由配置中定义。
const routes = [
    {    path: '/login', component: Login },
    {    path: '/index', component: HomePage },
    {    path: '/userinfo', component: UserInfo },
    {    path: '/', redirect: '/login' },
    {    path: '/demo', component: Demo },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router

