<template>
  <div>
    <span style="line-height:100%"> <br>
      
          <div style=" -webkit-text-stroke: 1px black; /* width and color */
    font-family: sans; color: black; " class="jb-y-large">학생 로그인</div>
      </span>
    <div class="new_stu_box" style = "margin-top:200px; display: block; margin: 0px auto;">
 <form>
    <v-text-field
      v-model="user_id"
      :error-messages="nameErrors"
      :counter="10"
      label="아이디를 입력해주세요."
      required
      @input="$v.name.$touch()"
      @blur="$v.name.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="user_pw"
      :error-messages="emailErrors"
      type="password"
      label="비밀번호를 입력해주세요."
      required
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
    ></v-text-field>
   
    <v-btn class="mr-4" @click="submit">제출</v-btn>
    <v-btn @click="clear">회원가입</v-btn>
  </form>

    </div>
   
      <footer-tag></footer-tag>
  </div>
</template>

<script>
import footerTag from './footer.vue';
import userApi from '../api/userApi.js';
export default {
    components : {
        footerTag,
    },
    methods : {
      submit(){
        let {
          user_id, user_pw
        } = this;
        let data = {
          user_id,
          user_pw
        }
        userApi.requestLogin(data, res => {
          console.log(res);
          this.$store.state.name = res.user_name;

          if(res.status == true){
            this.$router.push({
              name :"studentDetail"
            });
          }else{
            alert("아이디, 비밀번호를 확인해주세요.");
        }
        })
      }
    }
}
</script>

<style>
.jb-y-large { 
    margin-top : 30px;
    font-size: xx-large; 
    height : 200px;
}
.new_stu_box {
    margin-right : 30px;
    width : 700px;
    height : 200px;
    background: white;
    display: inline-block;
}
</style>