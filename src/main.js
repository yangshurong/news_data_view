import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import axios from 'axios'
import * as echarts from 'echarts'
import 'lib-flexible'
import 'echarts-gl'
import "echarts-wordcloud";
import ElementUI from 'element-ui';
import '../node_modules/element-ui/lib/theme-chalk/index.css';
const VueVideoPlayer = require('vue-video-player/dist/ssr')
require('video.js/dist/video-js.css')
require('vue-video-player/src/custom-theme.css')
Vue.config.productionTip = false
Vue.use(ViewUI)
Vue.use(ElementUI)
Vue.prototype.$axios=axios
Vue.prototype.$echarts=echarts
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
