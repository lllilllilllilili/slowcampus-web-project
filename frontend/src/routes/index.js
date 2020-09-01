import Vue from "vue";
import VueRouter from "vue-router";
import mainPage from "../views/mainPage.vue";
import loginPage from "../views/loginPage.vue";
import introPage from "../views/introPage.vue";
import contentsPage from "../views/contentsPage.vue";
import reviewsPage from "../views/reviewsPage.vue";
import teacherPage from "../views/teacherPage.vue";
import customerPage from "../views/customerPage.vue";
import teacherLogin from "../views/teacherLogin.vue";
import studentLogin from "../views/studentLogin.vue";
import teacherDetail from "../views/teacherDetailPage.vue";
import studentDetail from "../views/studentDetailPage.vue";
import teacherLecture from "../views/teacher/teacherLecture.vue";
import teacherResearch from "../views/teacher/teacherResearch.vue";
import studentLecture from "../views/student/studentLecture.vue";
import studentResearch from "../views/student/studentResearch.vue";
import teacherParent from "../views/teacher/teacherParent.vue";
import teacherGraph from "../views/teacher/graph/teacherGraph.vue";
import lineChart from "../views/teacher/lineChart/lineChart.vue";
import test from "../views/test/test.vue";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      component: mainPage
    },
    {
      path: '/main',
      name : 'main',
      component: mainPage,
      children:[
        {
          path:'main-intro',
          name : 'main-intro',
          component:introPage
        },
        {
          path:'main-contents',
          name : 'main-contents',
          component:contentsPage
        },
        {
          path:'main-reviews',
          name : 'main-reviews',
          component:reviewsPage  
        },
        {
          path:'main-teacher',
          name: 'main-teacher',
          component:teacherPage
        },
        {
          path:'main-customer',
          name:'main-customer',
          component:customerPage
        },
        {
            path:'teacherLogin',
            name:'teacherLogin',
            component:teacherLogin
        },
        {
            path:'studentLogin',
            name:'studentLogin',
            component:studentLogin
        },
    ]},
    {
        path : '/teacherDetail',
        name : 'teacherDetail',
        component : teacherDetail,
        children:[
            {
                path : 'teacherLecture',
                name : 'teacherLecture',
                component : teacherLecture,
            },
            {
                path : 'teacherResearch',
                name : 'teacherResearch',
                component : teacherResearch,
            },
        ]
    },
    {
        path : '/studentDetail',
        name : 'studentDetail',
        component : studentDetail,
        children : [
            {
                path : 'studentLecture',
                name : 'studentLecture',
                component : studentLecture,
            },
            {
                path : 'studentResearch',
                name : 'studentResearch',
                component : studentResearch,
            }

        ]
    },
    {
      path: "/login",
      name : 'login',
      component: loginPage
    },
    {
        path : '/teacherParent',
        name : 'teacherParent',
        component : teacherParent
    },
    {
        path : '/teacherGraph',
        name : 'teacherGraph',
        component : teacherGraph
    },
    {
      path : '/lineChart',
      name : 'lineChart',
      component : lineChart
    },
    {
      path : '/test',
      name : 'test',
      component : test
    },
    
  ]
});
