import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Posts from '@/components/Posts';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Ping',
      component: Ping
    },
    {
      path: '/posts',
      name: 'Posts',
      component: Posts
    }
  ],
  mode: 'history'
});
