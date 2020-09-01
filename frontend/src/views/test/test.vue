<template>
<v-app>
  <v-container>
              <v-card-title class="headline">
                <v-combobox 
                v-model="newSearch" 
                chips="chips" 
                readonly
                clearable="clearable"
                @click:clear = onClearClicked 
               
                label="Research"
                multiple="multiple" 
                solo="solo"
                @keyup.enter="searchBtnClick"
                ></v-combobox>
              </v-card-title>

              <v-card-text>

                카테고리 종류

                <v-divider></v-divider>
                <v-chip-group 
                solo
                active-class="orange accent-4 white--text" 
                v-model = "tagLocation"
                
                >
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',0, 'Web')">Web</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',1, 'Iot')">Iot</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',2, 'Cloud')">Cloud</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',3, 'Data')">Data</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',4, 'Server')">Server</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',5, 'Client')">Client</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',6, 'App')">App</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',7, 'Firmware')">Firmmware</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',8, 'AI')">AI</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',9, 'Network')">Network</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',10, 'BlockChain')">BlockChain</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',11, 'Game')">Game</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',12, 'DB')">DB</v-chip>
                <v-chip :disabled="isClicked" draggable="draggable" @click="insertTags('category',13, 'security')">security</v-chip>
                 </v-chip-group>
              </v-card-text>
  </v-container>
  </v-app>
</template>

<script>
export default {
    data(){
        return {
          searchBtnActive: false,
          isClicked : false,
          tagLocation : [],
          newSearch: [],
          hashtags: {
          category: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        }
    },
    watch : {
        newSearch: function () {
        if (this.newSearch.length >= 1) {
          this.searchBtnActive = false;
        } else if (this.newSearch.length == 0) {
          this.searchBtnActive = true;
        }
      },
    },
    methods:{
        searchBtnClick(){
       
         this.isLoading = true;
        this.$store.state.storeFlag +=1;
       this.hashtags.category = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],      
          this.tagLocation = [];
   
      },
    
        onClearClicked(){
            this.isClicked = false
          this.hashtags.category = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
           let list = [...this.newSearch];
          list = [];
          this.newSearch = [...list];   
          this.tagLocation = [];
       
      },
        insertTags(cate, n, name) {
            this.isClicked = true
        if (cate === "category") {
          
          if (!this.hashtags.category[n]) {
            this.hashtags.category[n] = !this.hashtags.category[n]
            let list = [...this.newSearch]
            list.push(name)
            this.newSearch = [...list]
           
          } else {
            var pos = this.newSearch.indexOf(name)
            this.hashtags.category[n] = !this.hashtags.category[n]
            let list = [...this.newSearch]
            list.splice(pos, 1)
            this.newSearch = [...list]
          }
        } 
    }
}
}
</script>

<style scoped="scoped">
  .v-chip--disabled {
    opacity: 1 !important;
  }
</style>