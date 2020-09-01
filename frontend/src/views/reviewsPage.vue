<template>
  <div>
    <div style=" -webkit-text-stroke: 1px black; /* width and color */
    font-family: sans; color: black; " class="jb-x-large">질문 게시판</div>
    
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
    ></v-pagination>
  </div>
      <footer-tag></footer-tag>
  </div>
</template>

<script>
import footerTag from './footer.vue';
export default {
    data () {
      return {
        desserts: [
          {
            name: '998. GCP VPC 구성에 대해 질문이 있습니다..',
            calories: '낚시왕 강태공',
          },
          {
            name: '997. 재혁 선생님 덕분에 AWS pro 땄습니다. 감사해요~-~',
            calories: 'GS편의점왕',
          },
          {
            name: '996. 강의가 너무 지루해요...',
            calories: '고민하다가 공부안함',
          },
          {
            name: '995. AWS, GCP, NCP 어떤것을 공부하는게 좋을까요?',
            calories: 'AWS 주식사는사람',
          },
          {
            name: '994. react와 vue의 차이가 무엇인가요?',
            calories: 'front는 싫은데 서버가 좋아',
          },
          {
            name: '993. GCP Dataflow workflow 에 대해 궁금합니다.',
            calories: 'google에 취업 꼭',
          },
          {
            name: '992. Google VPC에서 방화벽 규칙 설정은 어떻게 되는것인지 궁금합니다.',
            calories: 'NCP왕',
          },
          {
            name: '991. bigData 로드맵이 있나요? 있다면 참고 사이트 부탁드립니다.',
            calories: 'bigData싫어용',
          },
          {
            name: '990. 클라우드가 무엇인지 궁금합니다.',
            calories: 'cloudcloud99',
          },
          {
            name: '989. 환불 부탁드립니다.',
            calories: "negative man",
          },
        ],
      }
    },
    components : {
        footerTag
    }
}
</script>

<style scoped>
.jb-x-large { 
    margin-top : 30px;
    font-size: xx-large; }
</style>