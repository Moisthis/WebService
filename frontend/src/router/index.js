import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login'
import Home from '../components/Home'
import Welcome from '@/components/Welcome'
import Users from '@/components/user/Users'
import UserLook from '@/components/user/UserLook'
import School from '@/components/school/School'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/login',
        component: Login
    },
    {
        path: '/home',
        component: Home,
        redirect: '/welcome',
        children: [
            {path: '/welcome', component: Welcome},
            {path: '/3-1', component: Users},
            {path: '/1-1', component: UserLook},
            {path: '/4-1', component: School}
        ]
    }
]

const router = new VueRouter({
    routes
})


//挂载路由导航守卫
router.beforeEach((to, from, next) => {
    //to 将要访问的路径
    //from 从哪个路径跳转而来
    //next 表示放行

    if (to.path === '/login') return next();
    //获取token
    const tokenStr = window.sessionStorage.getItem('token')
    if (!tokenStr) return next('/login')
    //加个字段
    next()
})
export default router