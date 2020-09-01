<template>
  <div id="frameworks" class="frameworks">

  <section class="framework" :class="slug" v-if="data">
    <header class="framework__header">
      <strong class="framework__name">{{name}}</strong>
    </header>
    <div class="framework__data">
      <div class="framework__data-info">
        <div class="framework__period">
          <svg viewBox="0 0 7.22 11.76" class="framework__period-icon">
            <path d="M4.59 4.94V0H2.62v4.94H0l3.28 4.59 3.94-4.59H4.59zM.11 10.76h7v1h-7z"></path>
          </svg>
          <span class="framework__period-text">{{info.label}}</span>
        </div>
        <strong class="framework__downloads">{{info.value}}</strong>
      </div>
      <trend-chart :datasets="[dataset]" :min="0" padding="5 5 0" :interactive="true" @mouse-move="onMouseMove"></trend-chart>
    </div>
  </section>

  </div>
</template>

<script>
import TrendChart from "vue-trend-chart";
export default {
  created :{
  },
 type:"text/x-template",
  id:"framework",
    template: "#framework",
  components :{
    TrendChart,
  },
 props: {
    data: {
      type: Array,
      required: true
    },
    slug: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      currentInfo: null
    };
  },
  computed: {
    name() {
      return `${this.slug[0].toUpperCase() + this.slug.slice(1)}`;
    },
    weeklyDownloads() {
      return this.numberWithSpaces(this.data.reduce((a, c) => a + c.value, 0));
    },
    dataset() {
      return {
        data: this.data,
        showPoints: true,
        fill: true,
        className : `curve-${this.slug}`,
      };
    },
    info() {
      return {
        label: this.currentInfo ? this.currentInfo.label : "weekly downloads",
        value: this.currentInfo ? this.currentInfo.value : this.weeklyDownloads
      };
    }
  },
  methods: {
    numberWithSpaces(n) {
      return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    },
    onMouseMove(params) {
      if (!params) {
        this.currentInfo = null;
        return;
      }
      this.currentInfo = {
        label: params.data[0].day,
        value: this.numberWithSpaces(params.data[0].value)
      };
    }
  }
}
</script>

<style lang="scss" scoped>
.frameworks {
  display: flex;
  flex-wrap: wrap;
  .vtc {
    width: 160px;
    height: 60px;
    margin-right: -5px;
  }
  .stroke {
    stroke-width: 2;
  }
  .fill {
    opacity: 0.2;
  }
  .active-line {
    stroke: rgba(0, 0, 0, 0.2);
  }
  .point {
    display: none;
  }
  .point.is-active {
    display: block;
  }
}


.framework {
  width: 100%;
  @media (max-width: 699px) {
    &:nth-child(n + 2) {
      margin-top: 30px;
    }
    &:nth-child(n + 4) {
      display: none;
    }
  }
  @media (min-width: 700px) {
    width: calc(50% - 25px);
    &:nth-child(2n) {
      margin-left: 50px;
    }
    &:nth-child(n + 3) {
      margin-top: 50px;
    }
  }

  &__header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  &__name {
    width: 150px;
  }
  &__period {
    display: flex;
    align-items: center;
    flex-shrink: 0;
    opacity: 0.5;
    &-icon {
      display: block;
      height: 10px;
      width: auto;
      margin-right: 5px;
    }
    &-text {
      font-size: 11px;
      line-height: 16px;
      white-space: nowrap;
    }
  }
  &__data {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
  }
  &__downloads {
    font-size: 24px;
  }
  &.vue {
    border-bottom: 2px solid rgba(#39af77, 0.2);
    
  }
  &.react {
    border-bottom: 2px solid rgba(#61dafb, 0.2);
  }
  &.angular {
    border-bottom: 2px solid rgba(#d8002b, 0.2);
  }
  &.hapi {
    border-bottom: 2px solid rgba(#febc6b, 0.2);
  }
  &.express {
    border-bottom: 2px solid rgba(#259dff, 0.2);
  }
  &.koa {
    border-bottom: 2px solid rgba(#33333d, 0.2);
  }
  &.spring{
    border-bottom: 2px solid rgba(#00f535, 0.2);  
  }
  .curve-vue {
  .stroke {
    stroke: #39af77;
  }
  .fill {
    fill: #39af77;
  }
  .point {
    fill: #39af77;
    stroke: #39af77;
  }
}
.curve-react {
  .stroke {
    stroke: #61dafb;
  }
  .fill {
    fill: #61dafb;
  }
  .point {
    fill: #61dafb;
    stroke: #61dafb;
  }
}
.curve-angular {
  .stroke {
    stroke: #d8002b;
  }
  .fill {
    fill: #d8002b;
  }
  .point {
    fill: #d8002b;
    stroke: #d8002b;
  }
}
.curve-hapi {
  .stroke {
    stroke: #febc6b;
  }
  .fill {
    fill: #febc6b;
  }
  .point {
    fill: #febc6b;
    stroke: #febc6b;
  }
}
.curve-express {
  .stroke {
    stroke: #259dff;
  }
  .fill {
    fill: #259dff;
  }
  .point {
    fill: #259dff;
    stroke: #259dff;
  }
}
.curve-koa {
  .stroke {
    stroke: #33333d;
  }
  .fill {
    fill: #33333d;
  }
  .point {
    fill: #33333d;
    stroke: #33333d;
  }
}

}

</style>