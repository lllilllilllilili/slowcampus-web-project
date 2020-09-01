import Vue from 'vue'
import Vuex from 'vuex';
Vue.use(Vuex);
export default new Vuex.Store({
    state : {
        mainFlag : true,
        teacherFlag : true,
        studentFlag : true,
        name : '',
        category_basic : {},
        areas : [],
        isLoading : false,
        feature_basic : {},
        store_source : [],
        store_production : [],
        category_advanced : [],
        visualExpression : [],
        commitResearch : [],
        bytesResearch : [],
        funnelResearch : [{'argument':'No Data', 'value' : 0}],
    }
});