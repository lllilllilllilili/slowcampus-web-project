<template>
  <div class="app">
 <v-row justify="start">
    <v-flex v-for="(item, i) in items" :key="i+10" > 
    <v-card
    :loading="loading"
    class="mx-auto mr-auto"
    style="margin-top:20px; padding-left:10px"
    max-width="374"
    max-height="750" height="800"
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
    <div class="my-2">
        <v-btn>강의 목차</v-btn>
      </div>
      <div class="my-2">
        <v-btn color="error">공지사항 작성하기</v-btn>
      </div>
       <div class="my-2">
        <v-btn color="primary">학생들 Q&A 바로가기</v-btn>
      </div>
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
        title: '황인규 강사님 - What is devOps?(GCP를 활용한 CI/CD~docker container',
        image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRCpDJWKSuIllY_OeHwzgVpANXaMR-YdV6Ctg&usqp=CAU',
        rate : 5,
        explain : '이 강의에서는 devOps의 기초부터 심화까지 내용을 다룹니다. Q&A 가 개설되어 있습니다. 강의 내용은 index를 참고...',
        place : '온라인강의',
      },
      { 
        title: '황인규 강사님 - 쉽게 이해하는 NCP(NCP에서 CDN을 이용한 Live Streaming',
        rate : 4,
        explain : 'NCP는 무엇인지 간략하게 소개하고, Media Service에 대한 내용들을 살펴봅니다. 실무진의 경험으로...',
        place : '온라인강의',
        image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQoLWqMyO8puCVrHGqNE4nAR_wmRmdu5vD62w&usqp=CAU',
      },
      { 
        title: '황인규 강사님 - bigData 뽀개기(Data Lake ~ market 정제하는 pipeline)' ,
        rate : 4.5,
        explain : 'NCP는 무엇인지 간략하게 소개하고, Media Service에 대한 내용들을 살펴봅니다. 실무진의 경험으로...',
        place : '현장강의',
        image : 'https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/g7Y/image/QoUPiRwBMJoYAppVWNhMq4v8l-o',
      },
      { 
        title: '황인규 강사님 - 발표 잘하는 방법, 발표 스킬부터 제작까지',
        rate : 5,
        explain : '발표 하는 방법에 대해 쉽게 설명합니다. 우리 모두가 PPT에 지쳤다면 이 강의를...',
        place : '온라인강의',
        image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTmFRSQ7RpiQ18wgaSJr4WAJRD8AYF5FGZwnQ&usqp=CAU',
      },
      { 
        title: '황인규 강사님 - 🔥(HOT!!) AWS 이론 + 실습 종합',
        rate : 5,
        explain : 'AWS가 처음이라면? AWS가 어렵다면? AWS를 정복하고 싶다면 당장 이 강의를 사세요!!!! 학생 만족도 1위!...',
        place : '온라인강의',
        image : 'https://perfectacle.github.io/images/aws-security-group-reference-another-security-group/thumb.png',  
      },
      { 
          title: '황인규 강사님 - ML을 정형학적인 수치로 구현하기',
          rate : 5,
          explain : 'ML을 수치적으로 접근할 수 있습니다. 어려운 내용도 쉽게 이해할 수 있...',
          place : '온라인강의',
          image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRuGgCkSYaJKmuG23Uh2jn6GCzUfw4xcmeK2Q&usqp=CAU',
      },  
      { 
        title: '황인규 강사님 - Docker, Container에 대한 이해, 실습 까지',
        rate : 5,
        explain : 'Docker, Container에 대해 명확하게 이해할 수 있습니다.. !! GCP, AWS, NCP 어떤 플랫폼에도...',
        place : '온라인강의',
        image : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTD5freTu0wFrq-kH4Gsg69EF53qsDsBHWchQ&usqp=CAU",
      },
      { 
        title: '황인규 강사님 - 누구나 쉽게 따라할 수 있는 React',
        rate : 5,
        explain : 'Facebook React 팀으로부터 전수받은 다양한 노하우로 강의를 ...',
        place : '온라인강의',
        image : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRGzHyBI-yMU1fhVaD6fdKdYukIESV0zHNOjw&usqp=CAU",
      },
      { 
        title: '황인규 강사님 - Spring Framework에 대한 이해',
        rate : 5,
        explain : 'IOC, DI 개념부터 spring framework에 대한 기본 개념을 파악한다. MVC 패턴의 실습으로...',
        place : '온라인강의',
        image : "https://res.cloudinary.com/practicaldev/image/fetch/s--jjr2KV1M--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--rJtOTAAi--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/qujqfb147yni0io75r1a.png",
      },
      { 
        title: '황인규 강사님 - OS, concurrent programming',
        rate : 5,
        explain : 'pthead 와 POSIX library 를 활용한 임베디드 프로그래밍의 정석을 보여..',
        place : '온라인강의',
        image : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTeHfplz_0D1oUdIo1doGMNPY00jDjNkJS5HA&usqp=CAU",
      },
      { 
        title: '황인규 강사님 - Spring Framework에 대한 이해(2)',
        rate : 5,
        explain : 'IOC, DI 개념부터 spring framework에 대한 기본 개념을 파악한다. MVC 패턴의 실습으로...',
        place : '온라인강의',
        image : "https://res.cloudinary.com/practicaldev/image/fetch/s--jjr2KV1M--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--rJtOTAAi--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/qujqfb147yni0io75r1a.png",
      },
      { 
        title: '황인규 강사님 - OS, concurrent programming(2)',
        rate : 5,
        explain : 'pthead 와 POSIX library 를 활용한 임베디드 프로그래밍의 정석을 보여..',
        place : '온라인강의',
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