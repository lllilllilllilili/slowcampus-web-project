<template>
  <DxTreeMap
    id="treemap"
    :data-source="this.$store.state.visualExpression"
    title="2015~2020, Annual Language Analysis"
  >
    <DxTooltip
      :enabled="true"
      :customize-tooltip="customizeTooltip"
      format="thousands"
    />
  </DxTreeMap>
</template>

<script>

import DxTreeMap, { DxTooltip } from 'devextreme-vue/tree-map';
//import { citiesPopulation } from './data.js';

export default {
  components: {
    DxTreeMap,
    DxTooltip
  },
  data() {
    return {
      //citiesPopulation
    };
  },
  methods: {
    customizeTooltip(arg) {
      const data = arg.node.data;

      return {
        text: arg.node.isLeaf() ?
          `<span class="city">values:${data.name}</span> (${data.country})<br/>commit: ${arg.valueText}` :
          null
      };
    }
  }
};
</script>

<style>
#treemap {
    height: 500px;
}
.city {
    font-weight: 500;
}
</style>
