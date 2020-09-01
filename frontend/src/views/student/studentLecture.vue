<template>
  <div class="app">
 <v-row justify="start">
    <v-flex v-for="(item, i) in items" :key="i+10" > 
    <v-card
    :loading="loading"
    class="mx-auto mr-auto"
    style="margin-top:20px; padding-left:10px"
    max-width="374"
    max-height="650" height="800"
  >
    <v-img
      height="250"
      :src= "item.image"
    ></v-img>

    <v-card-title
    style=" -webkit-text-stroke: 1px black; /* width and color */

    font-family: sans; color: black; "
    >{{item.title}}</v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
        
      >
        <v-rating
          :value="4.5"
          color="#FFDE03"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ml-4">{{item.rate}}</div>
      </v-row>

      <div
        style="color : red"
       class="my-4 subtitle-1">
        {{item.place}}
      </div>

      <div
      style="color : black"
      >{{item.explain}}</div>
      
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>{{item.time}}</v-card-title>

    <v-card-text>
      <v-chip-group
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
      >

      </v-chip-group>
    </v-card-text>

  </v-card>
  </v-flex>
  </v-row>
      <span style="line-height:100%"> <br>
      <div class="new_content_box"></div>
      </span>
      <footer-tag></footer-tag>
  </div>
</template>

<script>
import footerTag from '../footer.vue'
export default {
    data(){
        return {
           items: [
      { 
        title: '장성우 강사님 - Vue.js의 이해, webhook과 함께',
        image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSSTRxrIms9XBvg-uMfrEIpykzrvDvT-A0c-A&usqp=CAU',
        rate : 5,
        explain : '이 강의에서는 Vue.js 기초부터 심화까지 내용을 다룹니다. Q&A 가 개설되어 있습니다. 강의 내용은 index를 참고바...',
        place : '온라인강의',
        time : '~8월 30일까지',
      },
      { 
        title: '원범희 강사님 - 쉽게 이해하는 NCP(NCP에서 CDN을 이용한 Live Streaming',
        rate : 4,
        explain : 'NCP는 무엇인지 간략하게 소개하고, Media Service에 대한 내용들을 살펴봅니다. 실무진의 경험으로...',
        time : '~9월 02일까지',
        place : '온라인강의',
        image : 'https://t1.daumcdn.net/news/201801/26/dt/20180126161534429vhda.jpg',
      },
      { 
        title: '노태균 강사님 - bigData 뽀개기(Data Lake ~ market 정제하는 pipeline)' ,
        rate : 4.5,
        explain : 'NCP는 무엇인지 간략하게 소개하고, Media Service에 대한 내용들을 살펴봅니다. 실무진의 경험으로...',
        place : '현장강의',
        time : '~9월 02일까지',
        image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTZT84AoMH0rk2JvKxHwNZeLTHDiNMZGydWMA&usqp=CAU',
      },
      { 
        title: '노태균 강사님 - 발표 잘하는 방법, 연습에서 실전까지',
        rate : 5,
        explain : '발표 하는 방법에 대해 쉽게 설명합니다. 우리 모두가 PPT에 지쳤다면 이 강의를...',
        place : '온라인강의',
        time : '~8월 20일까지',
        image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQNyu5HpnpSu-L_wdImT3BHGm4zzaPZAStolg&usqp=CAU',
      },
      { 
        title: '이재혁 강사님 - 🔥(HOT!!) AWS 이론 + 실습 종합',
        rate : 5,
        explain : 'AWS가 처음이라면? AWS가 어렵다면? AWS를 정복하고 싶다면 당장 이 강의를 사세요!!!! 학생 만족도 1위!',
        place : '온라인강의',
        time : '~9월 01일까지',
        price : 2300000,
        image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQuceBM74y_ePVw2T93YnGHoXcvofEHbfBSMA&usqp=CAU',  
      },
      { 
          title: '원범희 강사님 - ML을 정형학적인 수치로 구현하기',
          rate : 5,
          explain : 'ML을 수치적으로 접근할 수 있습니다. 어려운 내용도 쉽게 이해할 수 있...',
          place : '온라인강의',
          time : '~8월 10일까지',
          price : 83000,
          image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTR8inIT-7FdYEud1Jg71XmhHLaCOJ-obugCw&usqp=CAU',
      },  
      { 
        title: '장성우 강사님 - Docker, Container에 대한 이해, 실습 까지',
        rate : 5,
        explain : 'Docker, Container에 대해 명확하게 이해할 수 있습니다.. !! GCP, AWS, NCP 어떤 플랫폼에도...',
        place : '온라인강의',
        time : '~8월 20일까지',
        price : 81000,
        image : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRbDkFgtySt8gRypcz1lFSP1M0xgG3nTQT4IA&usqp=CAU",
      },
      { 
        title: '장성우 강사님 - 누구나 쉽게 따라할 수 있는 React',
        rate : 5,
        explain : 'Facebook React 팀으로부터 전수받은 다양한 노하우로 강의를 ...',
        place : '온라인강의',
        time : '~8월 22일까지',
        price : 71000,
        image : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQgAcp9vXEbEjKr3XdpVhTOZbQsXcovu9twww&usqp=CAU",
      },
      { 
        title: '원범희 강사님 - Spring Framework에 대한 이해',
        rate : 5,
        explain : 'IOC, DI 개념부터 spring framework에 대한 기본 개념을 파악한다. MVC 패턴의 실습으로...',
        place : '온라인강의',
        time : '~9월 30일까지',
        price : 53000,
        image : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQhnLmpelZsWQ3rRfDlBnv6pLphS-hzGFeMcg&usqp=CAU",
      },
      { 
        title: '노태균 강사님 - OS, concurrent programming',
        rate : 5,
        explain : 'pthead 와 POSIX library 를 활용한 임베디드 프로그래밍의 정석을 보여..',
        place : '온라인강의',
        time : '~8월 01일까지',
        price : 45000,
        image : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTeHfplz_0D1oUdIo1doGMNPY00jDjNkJS5HA&usqp=CAU",
      }
    ]
        }
    },
    components : {
        footerTag
    }
}
</script>

<style scoped>
.new_content_box {
    margin-right : 30px;
    width : 330px;
    height : 200px;
    background: white;
    display: inline-block;
}
.flex, .child-flex > * {
    flex: 1 1 auto;
    max-width: 30%;
}
</style>