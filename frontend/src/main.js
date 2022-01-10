import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
//导入全局样式表
import './assets/css/global.css'
//导入字体图标
import './assets/fonts/iconfont.css'
import axios from 'axios'
//配置请求的根路径
axios.defaults.baseURL = 'http://127.0.0.1:8000'
    /* 设置axios请求头加入token */
axios.interceptors.request.use(config => {
    //判断是否存在token，如果存在将每个页面header添加token
    if (window.sessionStorage.getItem("token")) {
        config.headers.Authorization = `Bearer ` + window.sessionStorage.getItem("token")
    }
    return config
})
Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')