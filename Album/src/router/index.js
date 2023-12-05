import { createRouter, createWebHistory } from "vue-router"

import Login from "@/views/Login/LoginIndex.vue"
import HomePage from "@/views/Home/HomePageIndex.vue"
import UserInfo from "@/views/UserInfo/UserInfoIndex.vue"
import Demo from "@/views/Demo/Demo1Index.vue"
import Main from "@/views/MainPage/MainIndex.vue"
import Welcome from "@/views/Home/HomeView.vue"
import info from "@/components/userinfo.vue"
import imagewaterfall from "@/components/ImageWaterFall.vue"
import Album from "@/views/Album/AlbumView.vue"


// 查询参数（如 ?uid=1）不需要在路由配置中定义。
const routes = [
    {    path: '/login', component: Login },
    {    path: '/index', component: HomePage },
    {    path: '/userinfo', component: UserInfo },
    {    path: '/', redirect: '/login' },
    {    path: '/demo', component: Demo },
    {
        path: '/main',
        component: Main,
        children:
        [
            {   path: '/main/welcome', component: Welcome},
            {   path: '/main/userinfo', component: info },
            {   path:'/main/imagewaterfall', component: imagewaterfall},
            {   path: '/main/album', component: Album }
        ]

    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router

