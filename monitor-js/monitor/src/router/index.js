import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/login'
        },
        {
            path: '/dashboard',
            component: resolve => require(['../components/common/Home.vue'], resolve),
            children: [
                {
                    path: '/',
                    component: resolve => require(['../components/page/Dashboard.vue'], resolve)
                },
                {
                    path: '/groups',
                    component: resolve => require(['../components/page/HostGroupCircle.vue'], resolve)
                },
                {
                    path: '/circle',
                    component: resolve => require(['../components/page/HostGroupCircle.vue'], resolve)
                },
                {
                    path: '/hosts',
                    component: resolve => require(['../components/page/Host.vue'], resolve)
                },
                {
                    path: '/hostDetail',
                    component: resolve => require(['../components/page/HostDetail.vue'], resolve)
                },
                {
                    path: '/events',
                    component: resolve => require(['../components/page/Events.vue'], resolve)
                },
                {
                    path: '/waterfall',
                    component: resolve => require(['../components/page/WaterFall.vue'], resolve)
                },
                {
                    path: '/apache',
                    component: resolve => require(['../components/page/ApacheMonitor.vue'], resolve)
                },
                {
                    path: '/ftp',
                    component: resolve => require(['../components/page/FTPMonitor.vue'], resolve)
                },
                {
                    path: '/agent',
                    component: resolve => require(['../components/page/Agent.vue'], resolve)
                }
            ]
        },
        {
            path: '/login',
            component: resolve => require(['../components/page/Login.vue'], resolve)
        },
    ]
})
