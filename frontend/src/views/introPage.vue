<template>
  <div >
      
      <br>
      <div class="new_box">   
      <img src="../assets/junjang-shinhanlife.jpeg" style = "display: block; margin: 0px auto;" width="250" height="250">
      <div style="text-align : center;">
       🏆. 2021년 4월 20일 - 신한라이프
      </div>

      
      </div>

       <div class="new_box">   
      <img src="../assets/cj.jpeg" style = "display: block; margin: 0px auto;" width="250" height="250">
      <div style="text-align : center;">
       🏆. 2021년 4월 22일 - CJ올리브네트웍스
      </div>
      </div>
      <span style="line-height:100px">
      <br>
      <div style="text-align : center">
        <!-- <div class="new_box">
             <img  src="../assets/pic1.png"  style = "display: block; margin: 0px auto;" width="200" height="200">
             IT  주제들을 연계하여 인사이트 제공

        </div> -->
        <!-- <div class="new_box">
            <img  src="../assets/cj.jpeg"  style = "display: block; margin: 0px auto;" width="250" height="250">
            IT 분야 별 실무 전문가로 구성된 강사진

        </div> -->
        <div class="new_box">
            <img  src="../assets/pic3.png"  style = "display: block; margin: 0px auto;" width="200" height="200">
                         언제 어디서나 들을 수 있는 온라인 IT 컨텐츠 제공

        </div>
        <div class="new_box">
            <img  src="../assets/insight.png"  style = "display: block; margin: 0px auto;" width="200" height="200">
                         IT  주제들을 연계하여 인사이트 제공
        </div>
        </div> 
     </span>
      <span style="line-height:100%"> <br>
      <div class="new_box"></div>
      </span>
      <footer-tag></footer-tag>
      
  </div>
</template>

<script>
import footerTag from './footer.vue'
export default {
    components : {
        footerTag
    }
}
</script>

<style>
.new_box {
    margin-right : 30px;
    height : 200px;
    background: white;
    display: inline-block;
}
</style>