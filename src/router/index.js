import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ShengView from '../views/ShengView.vue'
import ShiView from '../views/ShiView.vue'
import init_video from '../views/init_video.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    redirect:'/path/init_video'
  },
  {
    path: '/path',
    name: 'path',
    component: HomeView
  },
  { 
    path: '/path/ShengView',
    name: 'ShengView',
    component: ShengView
  },
  { 
    path: '/path/ShiView',
    name: 'ShiView',
    component: ShiView
  },
  { 
    path: '/path/init_video',
    name: 'init_video',
    component: init_video
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
