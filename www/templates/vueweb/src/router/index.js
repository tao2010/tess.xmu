import Vue from 'vue'
import Router from 'vue-router'

import ana from '@/components/ana'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ana',
      component: ana
    },
  ]
})
