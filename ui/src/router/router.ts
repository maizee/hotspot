import axios from "axios";
import { createRouter, createWebHistory } from "vue-router";
import { getUserInfo } from "../api";

// 路由信息
const routes = [
    {
        path: "/login",
        name: "登录",
        component: () => import('../views/LoginPage.vue'),
    },
    {
        path: "/",
        name: "首页",
        component: () => import('../views/MainPage.vue'),
    },
    {
        path: "/index",
        name: "首页",
        component: () => import('../views/MainPage.vue'),
    },
    {
        path: "/hotspot",
        name: "热点",
        component: () => import('../views/HotSpot.vue'),
    },
    {
        path: "/history",
        name: "历史",
        component: () => import('../views/HistoryPage.vue'),
    },
    {
        path: "/favor",
        name: "收藏",
        component: () => import('../views/FavorPage.vue'),
    },
    {
        path: "/userinfo",
        name: "个人中心",
        component: () => import('../views/UserInfo.vue'),
    },
    {
        path: "/about",
        name: "关于",
        component: () => import('../views/AboutUs.vue'),
    },
];

// 导出路由
const router = createRouter({
    history: createWebHistory(),
    routes
});
router.beforeEach((to, from, next) => {
    getUserInfo().then((res) => {
        console.log(to.path)
        next()
    }).catch((e) => {
        if (to.path=="/login"){
            next()
        }
        else{
            next('/login')
        }
    })

})
export default router;
