<template>
  <div>
        <div style=" -webkit-text-stroke: 1px black; /* width and color */
    font-family: sans; color: black; " class="jb-x-large">전화 상담</div>
    <p>전화 상담은 오전9:00~오후18:00 까지 가능합니다. (02-9876-5432)</p> 
    <v-simple-table style="margin-top:10px;">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">제목</th>
          <th class="text-left">글쓴이</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in desserts" :key="item.name">
          <td>{{ item.name }}</td>
          <td>{{ item.calories }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
   <div class="text-center">
    <v-pagination
      v-model="page"
      :length="10"
      style="margin-bottom : 30px"
    ></v-pagination>
  </div>
   <span style="line-height:100%"> <br>
      <div class="new_customer_box"></div>
      </span>
     
    <footer-tag></footer-tag>
  </div>
</template>

<script>
import footerTag from './footer.vue';
export default {
  components : {
    footerTag,
  },
  data () {
      return {
        desserts: [
          {
            name: '222. 강의 결제일은 언제부터 시작인가요?..',
            calories: '홍길동',
          },
          {
            name: '221. 강의 쿠폰은 언제 제공되는것인가요?',
            calories: 'GS편의점왕',
          },
          {
            name: '220. 취소 규정에 대해 궁금합니다.',
            calories: '마테차좋아용',
          },
          {
            name: '219. 자격증 바우처도 제공되나요? 관련 강의는 없는건가요?',
            calories: 'GCP 주식 사는 날',
          },
          {
            name: '218. 이회사도 야근이 있나요?',
            calories: '나도 언젠간...',
          },
          {
            name: '217. 다음달 강의는 언제나오나요?',
            calories: 'google에 취업 꼭',
          },
          {
            name: '216. 로그인 비밀번호 잊어버렸어요..',
            calories: 'NCP왕',
          },
          {
            name: '215. 고객센터 전화가 안되요..',
            calories: '데이터분석가김짱',
          },
          {
            name: '214. 강의 구매후 다른 강의로 전환이 가능한가요?',
            calories: 'cloudcloud',
          },
          {
            name: '213. 환불 부탁드립니다.',
            calories: "negative man",
          },
        ],
      }
    }
}
</script>

<style scoped>
.jb-x-large { 
    margin-top : 30px;
    font-size: xx-large; }

 .new_customer_box {
    margin-right : 30px;
    width : 330px;
    
    height : 50px;
    background: white;
    display: inline-block;
}   
</style>