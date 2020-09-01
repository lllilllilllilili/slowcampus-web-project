<template>
  <div id="app">
  <v-app id="inspire">
      <div   style=" -webkit-text-stroke: 1px black; /* width and color */
    font-family: sans; color: black; ">
      {{this.$store.state.name}} 님 안녕하세요?
      </div>      
<div class="grid">
    <div class="mark">
        <a href = "/main">
              <img  src="../assets/gs네오텍.png"  style = "display: block; margin: 0px auto;" width="150" height="50"> 
        </a>
          </div>
   
    <div class="header">

    </div>
    <div class="login">
        <v-col class="text-center" style="padding: 1px 1px 1px 1px;" cols="10">
         <div class="my-2" >
             <v-btn @click="logout" small color="primary" >로그아웃</v-btn>
         </div>
        </v-col>
    </div>
    <div class="menu">
<v-tabs fixed-tabs>
    <v-tab @click="valid('teacherLecture')">강의 목록</v-tab>
    <v-tab @click="valid('teacherResearch')">리서치 페이지</v-tab>
  </v-tabs>
  <router-view></router-view>
  <div v-if="this.$store.state.teacherFlag">
    <teacher-lecture></teacher-lecture>
    </div>
  <div else>

  </div>
</div>
</div>
 
  </v-app>
  </div>
</template>

<script>
import teacherLecture from "./teacher/teacherLecture.vue";
export default {
  components : {
      teacherLecture,
  },
  methods: {
      valid(name){
          this.$store.state.teacherFlag = false;
          this.$router.push({name : name});

      },
      signout(){

      },
      logout(){
          this.$store.state.teacherFlag = true;
          this.$store.state.mainFlag = true;

          this.$router.push({
                name: "main"
          });
      }
  },
}
</script>

<style scoped>
.jb-x-large { 
    margin-top : 30px;
    font-size: xx-large; }
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
.header {
    grid-area : header;
}
.mark{
    margin-right:1000px;
    grid-area : mark;
   
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