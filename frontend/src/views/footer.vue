<template>
    <div class = "box">
        <div>
            SLOW | CAMPUS
            
                <div class="top-left">
                    <p>Copyright © 2020 SLOW | CAMPUS.co.,Ltd. All rights reserved.</p>
                    <address>Contact webmaster for more information. gscloud94@slowcampus</address>
                    <v-icon @click="Fshare" style="color:white" color="white" large>{{mdiFacebook }}  </v-icon>
                    <v-icon @click="Fshare" style="color:white" color="white" large>{{mdiYoutube }}</v-icon>
                    <v-icon @click="Fshare" style="color:white" color="white" large>{{mdiGithub }}</v-icon>
                </div>
        </div>
        <div>
            
        </div>
    </div>
</template>

<script>
 import {
    mdiFacebook,
    mdiYoutube,
    mdiGithub
  } from '@mdi/js';

export default {
    data:()=>({
        icons:[
           
        ],
        mdiFacebook,
        mdiYoutube,
        mdiGithub
    })
}
</script>
<style>
/* .box{
   position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
	padding: 15px 0;
    height : 200px;
	text-align: center;
	color: white;
	background: black;
} */
.box{
  position:fixed; 
  left:0px; 
  bottom:0px; 
  padding : 15px 0;
  height:150px; 
  width:100%; 
  background:black; 
  color: white; 
  text-align : center;
}

</style>