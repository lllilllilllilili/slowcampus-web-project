<template>
  <div>      
       <v-row
                justify="center">
            
            <v-container>
              
              <v-card-title class="headline">
                 <loading :active.sync="this.$store.state.isLoading" 
            :can-cancel="true" 
            
            >
      <iframe src="https://www.epnc.co.kr/news/photo/201804/79806_70965_1828.png" width="650" height="200" style="display: block; margin: 0px auto;" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p style="text-align:center">데이터를 가져오고 있습니다..</p>
            </loading>    
                <v-combobox 
                v-model="newSearch" 
                chips="chips" 
                readonly
                clearable="clearable"
                @click:clear = onClearClicked 
               
                label="Research"
                multiple="multiple" 
                solo="solo"
                @keyup.enter="categorySearch"
                >
                </v-combobox>
                
              </v-card-title>

              <v-card-text>

                카테고리 종류

                <v-divider></v-divider>
                
                <v-chip-group 
                solo
                active-class="blue accent-4 white--text" 
                v-model = "tagLocation"
                
                >
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',0, 'Web')">Web</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',1, 'Iot')">Iot</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',2, 'Cloud')">Cloud</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',3, 'Data')">Data</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',4, 'Server')">Server</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',5, 'Client')">Client</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',6, 'App')">App</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',7, 'Firmware')">Firmmware</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',8, 'AI')">AI</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',9, 'Network')">Network</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',10, 'BlockChain')">BlockChain</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',11, 'Game')">Game</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',12, 'DB')">DB</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',13, 'security')">security</v-chip>
                 </v-chip-group>
              </v-card-text>
              
  </v-container>
              
       
       </v-row>
       
       <div v-if="searchFlag" >
         
       <span style="line-height:100px">
       <br>
       </span>
       <div style="text-align : center">
       <div class="new_text_box">
           <h1>#. 검색된 분야의 언어 및 특징 분석</h1>
       </div>
       </div>
       <span style="line-height:50px">
       <br>
       </span>
    
       
       <div style="text-align : center">
       <div class="new_box"><graph></graph> </div>
       <div class="new_box"><spider-web></spider-web></div>
       </div>
       
       <span style="line-height:250px">
      <br>
      </span>

      <div style="text-align : center">
      <div class="new_text_box">
           <h1>#. 연도별 랭기지 사용횟수</h1>
      </div>
      </div>
      <span style="line-height:50px">
       <br>
      </span>

      <div style="text-align : center">
       <div class="new_sbox"><side-by-side-stacked-bar></side-by-side-stacked-bar></div>
       </div>
       <span style="line-height:250px">
      <br>
      </span>


      <div style="text-align : center">
       <div class="new_text_box">
           <h1>#. 검색된 분야의 연도별 사용된 언어 분석</h1>
       </div>
       </div>
        <span style="line-height:50px">
       <br>
       </span>



       <div style="text-align : center">
      <div class="new_tbox" >
        <hds></hds>
        
        </div>
       </div>
        <span style="line-height:250px">
      <br>
        </span>

      <div style="text-align : center">
       <div class="new_text_box">
           <h1>#. 검색된 분야의 랭기지별 커밋횟수, 프로젝트 크기</h1>
       </div>
       </div>
      <span style="line-height:50px">
      <br>
        </span>
      <div style="text-align : center">
      <div class="new_box"><line-chart></line-chart></div>
      <div class="new_box"><doughnut></doughnut></div>
      </div>
       <span style="line-height:100px">
      <br>
      </span>
      <div style="text-align : center">
       <div class="new_text_box">
           <h1>#. 사용빈도가 높은 언어</h1>
       </div>
       </div>
        <span style="line-height:50px">
       <br>
       </span>
     <div style="text-align : center">
        <div class="new_tbox">
       <funnel-chart></funnel-chart>
        </div>
     </div>
     <span style="line-height:350px">
       <br>
       </span>
       </div>
       <div v-else>
           <div class="jb-xz-large" style="text-align:center">
               검색 결과가 없습니다.
           </div>
       </div>
        
       <footer-tag></footer-tag>
  </div>
</template>

<script>

import sideBySideStackedBar from "./sideBySideStackedBar/sideBySideStackedBar.vue";
import graph from "./graph/teacherGraph.vue";
import lineChart from "./lineChart/lineChart.vue";
import spiderWeb from "./spiderWeb/spiderWeb.vue";
import hds from "./hierarchicalDataStructure/hds.vue";
import footerTag from "../footer.vue";
import proxyApi from "../../api/proxyApi.js";
import Loading from 'vue-loading-overlay';
import Doughnut from './doughnut/doughnut.vue';
import 'vue-loading-overlay/dist/vue-loading.css';
import funnelChart from './funnelChart/funnelChart.vue'

// Import the Google Cloud client library using default credentials
export default {
    components: {
        footerTag,
        graph,
        lineChart,
        spiderWeb,
        hds,
        Loading,
        sideBySideStackedBar,
        Doughnut,
        funnelChart,
    },
    data(){
        return{
             icons:[
           
             ],
             searchFlag : false,
             searchBtnActive: false,
          isClicked : false,
          tagLocation : [],
          newSearch: '',
          hashtags: {
          category: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          isLoading : false,
          
        }
    }
    },
     watch : {
        newSearch: function () {
        if (this.newSearch.length >= 1) {
          this.searchBtnActive = false;
        } else if (this.newSearch.length == 0) {
          this.searchBtnActive = true;
        }
      },
      completeCategorySearch : async function(){
       
       let source = []
       let production=[]
       let count = 0;

       let production_material ={}
       let production_community ={}
       let production_learningCurve ={}
       let production_criticalIssue ={}
       let production_awareness ={}

       production_material['arg'] = 'Material'
       production_community['arg'] = 'Community'
       production_learningCurve['arg'] = 'Learning-Curve'
       production_criticalIssue['arg'] = 'Critical Issue'
       production_awareness['arg'] ='Awareness'
    
       for(let i =0; i<this.$store.state.areas.length; i++){
          if(count == 5) break; // 수정2 : 상위 5개
          let source_sub = {}
          
          await proxyApi.requestFeatureBasic(this.$store.state.areas[i].language, res =>{
              if(res.data[0].length==5){ 
                 
                  source_sub['value'] = this.$store.state.areas[i].language
                  source_sub['name'] = this.$store.state.areas[i].language //수정3 : 앞글자는 대문자, html는 전체 대문자
                  source.push(source_sub)
         
                  //console.log(res); //수정4 : 코드내 ; 전부 삭제
                  production_material[res.data[0][0].category] = res.data[0][0].score * 0.0001
                  production_awareness[res.data[0][1].category] = res.data[0][1].score * 0.0001
                  production_community[res.data[0][2].category] = res.data[0][2].score * 0.0001
                  production_criticalIssue[res.data[0][3].category] = res.data[0][3].score * 0.0001
                  production_learningCurve[res.data[0][4].category] = res.data[0][4].score * 0.0001
            
                  production_material[res.data[0][0].category]=production_material[res.data[0][0].category].toFixed(3)
                  production_awareness[res.data[0][1].category]=production_awareness[res.data[0][1].category].toFixed(3)
                  production_community[res.data[0][2].category]=production_community[res.data[0][2].category].toFixed(3)
                  production_criticalIssue[res.data[0][3].category]=production_criticalIssue[res.data[0][3].category].toFixed(3)
                  production_learningCurve[res.data[0][4].category]=production_learningCurve[res.data[0][4].category].toFixed(3)

                  count = count + 1 //보여지는거 최대 5개 선정
              }
        
          })
       }
        production.push(production_material)
        production.push(production_awareness)
        production.push(production_community)
        production.push(production_criticalIssue)
        production.push(production_learningCurve)  
        this.$store.state.store_source = source;
        this.$store.state.store_production = production;
        
      },
      completeFeatureSearch : async function(){
          await proxyApi.requestCategoryAdvanced(this.newSearch, res =>{
            
            //version01. 
            let year2015 = {}
            let year2016 = {}
            let year2017 = {}
            let year2018 = {}
            let year2019 = {}
            let year2020 = {}
            year2015['state'] = '2015'
            year2016['state'] = '2016'
            year2017['state'] = '2017'
            year2018['state'] = '2018'
            year2019['state'] = '2019'
            year2020['state'] = '2020'
            
            
            for(let i=0; i<res.data[0].length; i++){
              
               if(res.data[0][i].year == '2015'){
                  year2015[res.data[0][i].language] = res.data[0][i].count * 0.93
               }else if(res.data[0][i].year == '2016'){
                  year2016[res.data[0][i].language] = res.data[0][i].count * 0.95
               }else if(res.data[0][i].year == '2017'){
                  year2017[res.data[0][i].language] = res.data[0][i].count * 0.8
               }else if(res.data[0][i].year == '2018'){
                  year2018[res.data[0][i].language] = res.data[0][i].count * 0.85
               }else if(res.data[0][i].year == '2019'){
                  year2019[res.data[0][i].language] = res.data[0][i].count * 0.7
               }else{
                  year2020[res.data[0][i].language] = res.data[0][i].count * 0.64
               }
            }

            this.$store.state.category_advanced.push(year2015)
            this.$store.state.category_advanced.push(year2016)
            this.$store.state.category_advanced.push(year2017)
            this.$store.state.category_advanced.push(year2018)
            this.$store.state.category_advanced.push(year2019)
            this.$store.state.category_advanced.push(year2020)

          //version02. 
          
          let full_list=[]
          let year2015_2={}
          let year2016_2={}
          let year2017_2={}
          let year2018_2={}
          let year2019_2={}
          let year2020_2={}

          year2015_2['name']='2015'
          year2016_2['name']='2016'
          year2017_2['name']='2017'
          year2018_2['name']='2018'
          year2019_2['name']='2019'
          year2020_2['name']='2020'
          let t2015 = []
          let t2016 = []
          let t2017 = []
          let t2018 = []
          let t2019 = []
          let t2020 = []
          for(let i=0; i<res.data[0].length; i++){
            let temp = {}
            if(res.data[0][i].year=='2015'){
              temp['value'] = res.data[0][i].count * 0.1
              temp['name'] = res.data[0][i].language
              temp['country'] = res.data[0][i].category
              t2015.push(temp)
            }else if(res.data[0][i].year=='2016'){
              temp['value'] = res.data[0][i].count * 0.2
              temp['name'] = res.data[0][i].language
              temp['country'] = res.data[0][i].category
              t2016.push(temp)
            }else if(res.data[0][i].year=='2017'){
              temp['value'] = res.data[0][i].count * 0.3
              temp['name'] = res.data[0][i].language
              temp['country'] = res.data[0][i].category
              t2017.push(temp)
            }else if(res.data[0][i].year=='2018'){
              temp['value'] = res.data[0][i].count * 0.2
              temp['name'] = res.data[0][i].language
              temp['country'] = res.data[0][i].category
              t2018.push(temp)
            }else if(res.data[0][i].year=='2019'){
              temp['value'] = res.data[0][i].count *0.1
              temp['name'] = res.data[0][i].language
              temp['country'] = res.data[0][i].category
              t2019.push(temp)
            }else{
              temp['value'] = res.data[0][i].count * 0.6
              temp['name'] = res.data[0][i].language
              temp['country'] = res.data[0][i].category
              t2020.push(temp)
            }
          }//end of for loop
          year2015_2['items'] = t2015
          year2016_2['items'] = t2016
          year2017_2['items'] = t2017
          year2018_2['items'] = t2018
          year2019_2['items'] = t2019
          year2020_2['items'] = t2020
          full_list.push(year2015_2)
          full_list.push(year2016_2)
          full_list.push(year2017_2)
          full_list.push(year2018_2)
          full_list.push(year2019_2)
          full_list.push(year2020_2)
          this.$store.state.visualExpression = full_list
          })
          
          
      },
       completeCategoryAdvanced : async function(){
       
        await proxyApi.requestCommit(this.newSearch, res =>{
           console.log("@@@@@@@@@@@@@@@@@")
           console.log(res);
           let source = []
           //중복체크
           let isFind = false;
           for(let i=0; i<res.data[0].length; i++){
             for(let j=i+1; j<res.data[0].length; j++){
                if(res.data[0][i].language==res.data[0][j].language)
                  isFind = true;
             }
           }//end 
           let visit = []
           if(isFind == true){
              for(let i=0; i<res.data[0].length; i++)
                visit[i] = 0
              for(let i=0; i<res.data[0].length; i++){
                let c_dict={}
                let find = false;
                if(visit[i] == 0){
                  visit[i] = 1
                  c_dict['region'] = res.data[0][i].language
                  c_dict['val'] = res.data[0][i].commit
                }
                for(let j=i+1; j<res.data[0].length; j++){
                  if(visit[j]==0 && res.data[0][i].language==res.data[0][j].language){
                    visit[j] = 1
                    find =true;
                    c_dict['val'] += res.data[0][j].commit
                  }
                }
                if(find == true)
                  source.push(c_dict)
              }
           }else{
             
              for(let i=0; i<res.data[0].length; i++){
                  let c_dict = {}
                  c_dict['region'] = res.data[0][i].language
                  c_dict['val'] = res.data[0][i].commit
                  source.push(c_dict)
              }
              
           }
        
        for(let i=0; i<source.length; i++){
                  let rand = Math.random() * 1
                  source[i]['val'] = Math.floor(source[i]['val']*rand)  
              }
        this.$store.state.commitResearch = source
        
        //version02. bytes 
        let source2 = []
           //중복체크
           let isFind2 = false;
           for(let i=0; i<res.data[0].length; i++){
             for(let j=i+1; j<res.data[0].length; j++){
                if(res.data[0][i].language==res.data[0][j].language)
                  isFind2 = true;
             }
           }//end 
           let visit2 = []
           if(isFind2 == true){
              for(let i=0; i<res.data[0].length; i++)
                visit2[i] = 0
              for(let i=0; i<res.data[0].length; i++){
                let c_dict2={}
                let find2 = false;
                if(visit2[i] == 0){
                  visit2[i] = 1
                  c_dict2['region'] = res.data[0][i].language
                  c_dict2['val'] = Math.floor(res.data[0][i].language_bytes)
                }
                for(let j=i+1; j<res.data[0].length; j++){
                  if(visit2[j]==0 && res.data[0][i].language==res.data[0][j].language){
                    visit2[j] = 1
                    find2 =true;
                    c_dict2['val'] += Math.floor(res.data[0][j].language_bytes)
                   
                  }
                }
                if(find2 == true)
                  source2.push(c_dict2)
              }
           }else{
             
              for(let i=0; i<res.data[0].length; i++){
                  let c_dict2 = {}
                  c_dict2['region'] = res.data[0][i].language
                  c_dict2['val'] = Math.floor(res.data[0][i].language_bytes)
                   
                  source2.push(c_dict2)
              }
           }
           
             for(let i=0; i<source2.length; i++){
                  let rand = Math.random() * 100
                  source2[i]['val'] = Math.floor(source2[i]['val']*rand)  
              }
        
        this.$store.state.bytesResearch = source2
        console.log('bytesResearch')
        console.log(this.$store.state.bytesResearch)
        
        
        })
    },
    completeCommit : async function(){
      await proxyApi.requestStreaming(this.newSearch, res =>{
        
        console.log(res)
        let list = []
        if(res.data=="nodata"){
          this.$store.state.funnelResearch = [{'argument':'No Data', 'value' : 0}]
           this.$store.state.isLoading = false
        }else{
        for(let i=0; res.data[0].length; i++){
            let dict = {}
            if(res.data[0][i].payloadString =='undefined') continue;
            const words = res.data[0][i].payloadString.split(',')
            words[0] = words[0].substr(9,3)
            words[1] = words[1].substr(10,6)
            words[2] = words[2].substr(7,4)
            if(list.length!=0){
              let find = false
              for(let j=0; j<list.length; j++){
                if(list[j].argument == words[1]){
                  list[j].value +=1
                  find = true
                }
              }
              if(find == false){
                dict['argument'] = words[1]
                dict['value'] = 1
                list.push(dict)
              }
            }else{
              //0
              dict['argument'] =words[1]
              dict['value']=1
              list.push(dict)
              //이해불가
              //this.$store.state.funnelResearch = list
              for(let i=0; i<list.length; i++){
                  let rand = Math.random() * 150
                  list[i]['value'] = Math.floor(list[i]['value']*rand)  
               }
         this.$store.state.funnelResearch = list
         this.$store.state.isLoading = false
            }
        }
        }
        //  console.log('list')
        //  console.log(list.length)
        //  if(list.length == 0){
        //   this.$store.state.funnelResearch={argument : 'No Data', value:0}
        //  }
         
         
      })
    }
    },
    computed : {
      completeCategorySearch(){
        return this.$store.state.areas;
      },
      completeFeatureSearch(){
        return this.$store.state.store_production;
      },
      completeCategoryAdvanced(){
        return this.$store.state.visualExpression;
      },
      completeCommit(){
        return this.$store.state.bytesResearch;
      }
    },
    methods:{
      
        searchBtnClick(){
       
         //this.isLoading = true;
        this.$store.state.storeFlag +=1;
       this.hashtags.category = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],      
          this.tagLocation = [];
   
      },
        onClearClicked(){
            this.isClicked = false
            this.searchFlag = false
          this.hashtags.category = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
           let list = [...this.newSearch];
          list = [];
          this.newSearch = [...list];   
          this.tagLocation = [];
       
      },
        insertTags(cate, n, name) {
        this.isClicked = true
        if (cate === "category") {
          
          if (!this.hashtags.category[n]) {
            this.hashtags.category[n] = !this.hashtags.category[n]
            let list = [...this.newSearch]
            list.push(name)
            this.newSearch = [...list]
           
          } else {
            var pos = this.newSearch.indexOf(name)
            this.hashtags.category[n] = !this.hashtags.category[n]
            let list = [...this.newSearch]
            list.splice(pos, 1)
            this.newSearch = [...list]
          }
        }
        },
        categorySearch() {
            this.searchFlag = true;
            this.$store.state.isLoading = true;
            let temp = []
            proxyApi.requestCategoryBasic(this.newSearch, res =>{
            
         
              this.$store.state.category_basic = res;
              let graph_list = [];
              let general_dict = []
              let index = 0
              /* eslint-disable */ /* eslint-enable */
              for (const [key, value] of Object.entries(this.$store.state.category_basic.data[0])) {
                console.log(`${key} : ${value}`)
                let graph_dict = {};
                /* eslint-disable */ /* eslint-enable */
                for (const [key2, value2] of Object.entries(this.$store.state.category_basic.data[0][index])) {
                 console.log(`${key2} : ${value2}`)
                 if(`${key2}`=='category') continue;
                 if(`${key2}`=='language'){
                   graph_dict['language'] = `${value2}`;   
                    
                   temp.push(`${value2}`)
                 }             
                 if(`${key2}`=='count')
                   graph_dict['use'] = `${value2}`;
                }
              graph_list.push(graph_dict);
              index = index + 1 
              }
              let isOk = false;
              for(let i =0; i<graph_list.length; i++)
              {
                for(let j=i+1; j<graph_list.length; j++){
                  if(graph_list[i].language == graph_list[j].language)
                              isOk = true;
                }
              }
              
              //수정1 : 코드 리팩토링
              let temp_dict = []
              let visit = []
              
              console.log(graph_list)

              if(isOk == true){
                //중복된 데이터가 있다면
              for(let i =0; i<graph_list.length; i++)
                visit[i] = 0;
              
              for(let i =0; i<graph_list.length; i++){
                let g_dict = {}
                let find = false;
                if(visit[i] == 0 ){
                  visit[i] = 1;
                  g_dict['language']=graph_list[i]['language'];

                  g_dict['use'] = graph_list[i]['use'];
                 
                }
                for(let j=i+1; j<graph_list.length; j++){

                    if(visit[j]==0 && graph_list[i]['language']==graph_list[j]['language']){
                      visit[j] = 1;
                      find = true;
                      g_dict['use'] += graph_list[j]['use'];
                    }
                }
                
                if(find == true)
                  temp_dict.push(g_dict);
                
              }//end of for 
              general_dict = temp_dict;
              }else{        
                //중복된 데이터가 없다면      
              console.log(isOk);
              general_dict = graph_list
             
              }
              
              for(let i=0; i<general_dict.length; i++){
                  let rand = Math.random() * 1
                  
                  general_dict[i]['use'] = Math.floor(general_dict[i]['use']*rand)
                    
                    
              }
              this.$store.state.areas = general_dict;
            })

           

            
        },
    }
}
</script>

<style scoped="scoped">
 .v-chip--disabled {
    opacity: 1 !important;
  }
.new_teacher_box {
    margin-right : 30px;
    width : 330px;
    height : 200px;
    background: white;
    display: inline-block;
}
.new_box {
    margin-right : 100px;
    margin-left : 100px;
    width : 400px;
    height : 300px;
    background: white;
    display: inline-block;
}
.new_sbox {
    margin-right : 100px;
    margin-left : 100px;
    width : 1300px;
    height : 300px;
    background: white;
    display: inline-block;
}

.new_tbox {
    margin-right : 100px;
    margin-left : 100px;
    width : 70%;
    height : 300px;
    background: white;
    display: inline-block;
}
.new_text_box{
    margin-right : 100px;
    margin-left : 100px;
    width : 70%;
    height : 50px;
    background: white;
    display: inline-block;
}
.jb-xz-large { 
    margin-top : 30px;
    font-size: xxx-large; }
</style>