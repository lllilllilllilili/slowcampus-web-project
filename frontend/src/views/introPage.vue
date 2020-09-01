<template>
  <div >
 
        
      <img src="../assets/slow-campus.png" style = "display: block; margin: 0px auto;" width="500" height="500">
      <div style="text-align : center;">
       오프라인에서 온라인까지, B2C에서 B2B까지, IT교육에서 스킬까지,학습 방법과 분야를 끊임없이 확장하며 다양한 학습자의 필요를 만족시키는 모든 교육 콘텐츠를 제공하고자 노력하고 있습니다.
      </div>
      <span style="line-height:100px">
      <br>
      <div style="text-align : center">
        <!-- <div class="new_box">
             <img  src="../assets/pic1.png"  style = "display: block; margin: 0px auto;" width="200" height="200">
             IT  주제들을 연계하여 인사이트 제공

        </div> -->
        <div class="new_box">
            <img  src="../assets/pic2.png"  style = "display: block; margin: 0px auto;" width="200" height="200">
            IT 분야 별 실무 전문가로 구성된 강사진

        </div>
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