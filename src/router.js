/* eslint-disable no-dupe-keys */
import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      redirect: "/index",
      component: Home,
      children: [
        {
          path: "index",
          name: "crawler",
          component: "crawler",
          component: () => import("@/views/crawler/index.vue"),
          meta: {
            keepAlive: true
          }
        },
        {
          path: "download",
          name: "download",
          component: "download",
          component: () => import("@/views/download/index.vue"),
          meta: {
            keepAlive: true
          }
        },
        {
          path: "settings",
          name: "settings",
          component: "settings",
          component: () => import("@/views/settings/index.vue"),
          meta: {
            keepAlive: true
          }
        }
      ]
    },
    {
      path: "/search",
      name: "search",
      component: "search",
      component: () => import("@/views/search/index.vue"),
      meta: {
        keepAlive: true
      }
    }
  ]
});
