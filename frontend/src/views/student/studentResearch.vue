<template>
  <div>      
       <v-row
                justify="center">

                    <v-text-field 
                    hide-details 
                    prepend-inner-icon="search" 
                    @keyup.enter="storeListSearch" 
                    single-line
                    solo
                    v-model="ssearch" 
                    placeholder="키워드 입력해주세요."
                    style="max-width: 70%;
                    text-align: center !important;"
                    ></v-text-field>
       
       </v-row>
       <div v-if="searchFlag">
          <graph></graph>
          <spider-web></spider-web>
          <hds></hds>
          <line-chart></line-chart>
          <language-page></language-page>
       </div>
       <div v-else>
           <div class="jb-xz-large" style="text-align:center">
               검색 결과가 없습니다.
           </div>
       </div>
  </div>
</template>

<script>
import LanguagePage from "./studentParent.vue";
import graph from "./graph/studentGraph.vue";
import lineChart from "./lineChart/lineChart.vue";
import spiderWeb from "./spiderWeb/spiderWeb.vue";
import hds from "./hierarchicalDataStructure/hds.vue";
export default {
    components: {
      LanguagePage,
      graph,
      lineChart,
      spiderWeb,
      hds,
    },
    data(){
        return{
             icons:[
           
             ],
             searchFlag : false,
        }
    },
    methods:{
        storeListSearch() {
            this.searchFlag = true;

            
        },
    }
}
</script>

<style>
.new_teacher_box {
    margin-right : 30px;
    width : 330px;
    height : 200px;
    background: white;
    display: inline-block;
},
.jb-xz-large { 
    margin-top : 30px;
    font-size: xxx-large; }
</style>