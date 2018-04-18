import Vue from 'vue';
import App from './App';
import router from './router';
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';    // 默认主题
// import '../static/css/theme-green/index.css';       // 浅绿色主题
import "babel-polyfill";
import iView from 'iview';
import 'iview/dist/styles/iview.css';

Vue.use(ElementUI);
Vue.prototype.$http = axios;
Vue.use(iView);

import VueParticles from 'vue-particles'
Vue.use(VueParticles);

import 'vue-awesome/icons'

import Icon from 'vue-awesome/components/Icon.vue'
Vue.component('icon',Icon);

import Echarts from 'vue-echarts/components/ECharts.vue'
Vue.component('chart',Echarts);

new Vue({
    router,
    render: h => h(App)
}).$mount('#app');
