import Vue from "vue";
import App from "./App.vue";
import router from "./routes";
import vuetify from "./plugins/vuetify";
import axios from 'axios'
import VueAxios from 'vue-axios'
import '@mdi/font/css/materialdesignicons.css';
import 'material-design-icons-iconfont/dist/material-design-icons.css';
import TrendChart from "vue-trend-chart";
import ApexCharts from 'apexcharts';
import store from './vuex/store.js';
import VueLoading from 'vuejs-loading-plugin'
Vue.config.productionTip = false;
Vue.use(TrendChart);
Vue.use(VueLoading);
new Vue({
  render: h => h(App),
  vuetify,
  router,
  axios,
  VueAxios,
  TrendChart,
  ApexCharts,
  store,
  icons:{
    iconfont: 'fa',
  },
}).$mount("#app");
