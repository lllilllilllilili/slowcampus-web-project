<template>
  <div id="app">
  <v-app id="inspire">
      <div class="grid">
          <div class="mark">
            <a href = "/main">
              <img  src="../assets/symbol.jpeg"  style = "display: block; margin: 0px auto;" width="150" height="50"> 
            </a>
          </div>

         
          <div class="header">
               
          </div>
          <div class="login">
    <div class="text-center">
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="primary"
            dark
            v-bind="attrs"
            v-on="on"
          >
            로그인
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in items"
            :key="index"
          >
            <v-list-item-title @click="signUp(item.title)">{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>

          </div>
          <div class="menu">
                <v-tabs fixed-tabs>             
                    <v-tab @click="valid('main-intro')">
                        훈장</v-tab>
                    <v-tab @click="valid('main-teacher')">훈장2</v-tab>
                    <v-tab @click="valid('main-contents')">훈장3</v-tab>
                    <v-tab @click="valid('main-reviews')" >훈장4</v-tab>
                    <v-tab @click="valid('main-customer')">훈장5</v-tab>
                </v-tabs>
               
                <router-view></router-view>
              <div v-if="this.$store.state.mainFlag">
                <intro-page></intro-page>
              </div> 
              <div v-else>
                
              </div>
          </div>
          <div class="content"></div>
          <div class="nav"></div>
          <div class="footer"></div>
          
      </div>

  </v-app>
  </div>
</template>

<script>
import introPage from "./introPage.vue";
export default {
   data: () => ({
    items: [
      { title: '선생님 로그인' },
      { title: '학생 로그인' },
    ],
  }),
  components : {
    introPage,
  },
  methods: {
      valid(name){
          this.$store.state.mainFlag = false;
          this.$router.push({name : name});
      },
      signUp(title){
          this.$store.state.mainFlag = false;
        
          if(title == "선생님 로그인"){
              this.$router.push({name: "teacherLogin"})
          }else{
              this.$router.push({name: "studentLogin"})
          }
      },
  },
};
</script>

<style >
.grid {
    display : grid;
    gap : 10px;
    grid-template-columns: 1fr, 1fr, 1fr, 1fr;
    grid-template-rows: 40px 60px 100px 100px;
    grid-template-areas: 
    "mark header header login"
    "menu menu menu menu"
    "content content content nav"
    "content content content nav"
    "footer footer footer footer";
}
.mark{
    margin-right:1000px;
    grid-area : mark;
   
}
.textLine{
    margin-top : 1px;
    font-size: xx-large; 
    grid-area : text;
}
.header {
    grid-area : header;
}

.menu {
    grid-area : menu;
}

.login {
    grid-area : login;
}
.header2 {
    grid-area : header2;
    grid-column-start: 2;
    grid-column-end: 5;
}

.content {
    grid-area : content;
}
.nav {
    
    grid-area : nav;
}
.footer{
  
    grid-area : footer;
}
</style>
