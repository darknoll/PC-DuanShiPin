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
          component: () => import("@/views/crawler/Index.vue"),
          meta: {
            keepAlive: true
          }
        },
        {
          path: "download",
          name: "download",
          component: () => import("@/views/download/Index.vue"),
          meta: {
            keepAlive: true
          },
          children: [
            {
              path: "downloading",
              name: "downloading",
              component: () => import("@/views/download/Downloading.vue"),
              meta: {
                keepAlive: true
              }
            },
            {
              path: "downloaded",
              name: "downloaded",
              component: () => import("@/views/download/Downloaded.vue"),
              meta: {
                keepAlive: true
              }
            }
          ]
        },
        {
          path: "settings",
          name: "settings",
          component: () => import("@/views/settings/Index.vue"),
          meta: {
            keepAlive: true
          },
          children: [
            {
              path: "basic",
              name: "basic",
              component: () => import("@/views/settings/Basic.vue"),
              meta: {
                keepAlive: true
              }
            },
            {
              path: "transfer",
              name: "transfer",
              component: () => import("@/views/settings/Transfer.vue"),
              meta: {
                keepAlive: true
              }
            }
          ]
        }
      ]
    },
    {
      path: "/search",
      name: "search",
      component: () => import("@/views/search/Index.vue"),
      meta: {
        keepAlive: true
      }
    }
  ]
});
