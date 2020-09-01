<template>
  <div>
      login
      <div class="grid">
          <div class="header"></div>
          <div class="header2"></div>
          <div class="content"></div>
          <div class="nav"></div>
          <div class="footer"></div>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.father {
    display : grid;
    grid-template-columns: 20px 55px 89px 100px;
}
.grid {
    display : grid;
    gap : 10px;
    grid-template-columns: 1fr, 1fr, 1fr, 1fr;
    grid-template-rows: 100px repeat(2,200px) 100px;
    grid-template-areas: 
    "header header header header"
    "content content content nav"
    "content content content nav"
    "footer footer footer footer";
}
.header {
    grid-area : header;
}

.header2 {
    grid-area : header2;
    grid-column-start: 2;
    grid-column-end: 5;
}

.content {
    grid-area : content;
}
.nav {
    
    grid-area : nav;
}
.footer{
  
    grid-area : footer;
}
</style>