<template>
  <div>
    <router-link to="login"></router-link> 
    <div style=" -webkit-text-stroke: 1px black; /* width and color */

    font-family: sans; color: black; ">
      [Prototyping]
      </div>
    <router-link to="main"></router-link>
  
  <router-view></router-view>
  
  </div>
</template>

<script>

export default {
  components : {
    
  }
}
</script>

<style>

</style>