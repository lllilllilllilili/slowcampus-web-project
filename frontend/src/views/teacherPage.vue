<template>
 <div >
  
<v-row justify="start">
    <v-flex v-for="(item, i) in items" :key="i+10" mr="10" > 
    <v-card
      class="mx-auto"
      style="margin-top:20px; margin-left:100px;"
      color="#f8f9fa"

      dark
      max-width="374"
      height ="400"
    >
      <v-card-title>
        <v-icon
          large
          left
          style="color : black"
        >
          {{item.icon}}
        </v-icon>
        <span style ="color : black " class="title font-weight-light">{{item.domain}}</span>
      </v-card-title>
  
      <v-card-text style ="color : black" class="headline font-weight-bold">
       {{item.info}}
      </v-card-text>
      <div style="margin-bottom : 30px;"></div>
      <v-card-actions>
        <v-list-tile class="grow">
          <v-list-tile-avatar color="grey darken-3">
            <v-img
              style = "display: block; margin: 0px auto;"
              class="elevation-6" width="100" height="100"
              :src=item.profile
            ></v-img>
          </v-list-tile-avatar>
  
          <v-list-tile-content>
            <br>
            <v-list-tile-title style="color : black; text-align:center;">{{item.name}}</v-list-tile-title>
          </v-list-tile-content>
  
          <v-layout
            align-center
            justify-end
          >
           <div style="margin-top : 100px;"></div>
            <v-icon class="mr-1" style="color : black">mdi-heart</v-icon>
            <span class="subheading mr-2" style="color : black">{{item.likeCnt}}</span>
            <span class="mr-1">·</span>
            <v-icon class="mr-1" style="color : black">mdi-share-variant</v-icon>
            <span class="subheading" style="color : black">{{item.share}}</span>
          </v-layout>
        </v-list-tile>
      </v-card-actions>
    </v-card>
    </v-flex>
    <footer-tag></footer-tag>
</v-row>
<span style="line-height:100%"> <br>
      <div class="new_teacher_box"></div>
      </span>
</div>
</template>

<script>
import footerTag from './footer.vue';
 import {
    
    mdiAws,
    mdiGoogle,
    
  } from '@mdi/js';
export default {
    data(){
        return {
            items : [
                {
                    domain : 'Data Engineering',
                    info : 'Google Cloud Platform Architect - bigData lecture',
                    profile : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ43wOiQWMkOfGixnPHbSMeLQNS5uAavc-iQQ&usqp=CAU',
                    name : 'Hwang In Kyu',
                    likeCnt : 100002,
                    share : 1918,
                    icon : mdiGoogle,
                    
                },
                {
                    domain : 'DevOps Engineering',
                    info : 'Google Cloud Platform Architect - DevOps lecture',
                    profile : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ43wOiQWMkOfGixnPHbSMeLQNS5uAavc-iQQ&usqp=CAU',
                    name : 'Jang Sung Woo',
                    likeCnt : 2300002,
                    share : 19182,
                    icon : mdiGoogle,
                },
                {
                    domain : 'Data/AI,ML Engineering',
                    info : 'Google Cloud Platform Architect - bigData,AI lecture',
                    profile : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR0rIX2TiL28ysi11TFUNeyYSsDMYk-5DRCQQ&usqp=CAU',
                    name : 'Noh Tae Kyun',
                    likeCnt : 1000,
                    share : 1991,
                    icon : mdiGoogle,

                },
                {
                    domain : 'Media Engineering',
                    info : 'Naver Cloud Platform Architect - Media lecture',
                    profile : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQVu038w99zxoodomwBp1MvV7NtiU6arM2rMg&usqp=CAU',
                    name : 'Won Bum Hee',
                    likeCnt : 122121,
                    share : 11999,
                    icon : mdiAws,
                },
                {
                    domain : 'Cloud Engineering',
                    info : 'NCP, GCP, AWS Architect - Cloud ALL',
                    profile : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRmNtgeGvN58Ci1O__-5kxyYwQurTgqVtktrA&usqp=CAU',
                    name : 'Lee Jae Hyuk',
                    likeCnt : 199999999,
                    share : 222123332,
                    icon : mdiAws,
                },
                {
                    domain : 'Data/AI,ML Engineering',
                    info : 'Google Cloud Platform Architect - bigData,AI lecture',
                    profile : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR0rIX2TiL28ysi11TFUNeyYSsDMYk-5DRCQQ&usqp=CAU',
                    name : 'Noh Tae Kyun',
                    likeCnt : 1000,
                    share : 1991,
                    icon : mdiGoogle,

                },
                {
                    domain : 'Media Engineering',
                    info : 'Naver Cloud Platform Architect - Media lecture',
                    profile : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQVu038w99zxoodomwBp1MvV7NtiU6arM2rMg&usqp=CAU',
                    name : 'Won Bum Hee',
                    likeCnt : 122121,
                    share : 11999,
                    icon : mdiAws,
                },
                {
                    domain : 'Cloud Engineering',
                    info : 'NCP, GCP, AWS Architect - Cloud ALL',
                    profile : 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRmNtgeGvN58Ci1O__-5kxyYwQurTgqVtktrA&usqp=CAU',
                    name : 'Lee Jae Hyuk',
                    likeCnt : 199999999,
                    share : 222123332,
                    icon : mdiAws,
                }
            ]
        }
    },
    components :{
        footerTag
    }
}
</script>

<style>
.new_teacher_box {
    margin-right : 30px;
    width : 330px;
    height : 100px;
    background: white;
    display: inline-block;
}
</style>