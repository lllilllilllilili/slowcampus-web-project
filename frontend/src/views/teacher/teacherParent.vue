<template>
  <div id="app">
    <div class="frameworks">
    <framework v-for="(dataset,i) in datasets" :key="i" :data="dataset.data" :slug="dataset.slug" />
  </div>
  </div>

</template>

<script>
import axios from "axios"
import framework from "./framework.vue";
export default {
  
    components:{
        framework,
    },
data: ()=>({
    frameworks: ["vue", "react", "angular", "hapi", "express", "koa", "spring" ],
    data: null,
    
  }),
  computed: {
    datasets() {
      if (!this.data) return null;
      return this.frameworks.filter(f => this.data[f]).map(f => {
        return {
          slug: f,
          data: this.data[f].downloads.map(d => {
            return { value: d.downloads, day: d.day };
          })
        };
      });
    }
  },
  methods: {
      
    fetchData() {
      axios
        .get(
          `https://api.npmjs.org/downloads/range/last-week/${this.frameworks.join(
            ","
          )}`
        )
        .then(res => {
          this.data = res.data;
        })
        .catch(error => console.log(error));
    }
  },
  mounted() {
    this.fetchData();
  }
}
</script>

<style lang="scss" scoped>
* {
  box-sizing: border-box;
}

strong {
  font-weight: 600;
}

body {
  padding: 0;
  margin: 0;
  font-family: "Source Sans Pro", sans-serif;
  color: #2f4053;
}

#app {
  margin: 0 auto;
  padding: 20px;
  max-width: 700px;
}

</style>