<script setup lang="ts">

</script>

<template>
  <el-container>
    <el-header style="padding:0px;">
      <app-bar></app-bar>
    </el-header>
    <el-main>
      <router-view>
      </router-view>
    </el-main>
    <div id="building"></div>
  </el-container>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#building {
  background: url("./assets/bgp.svg");
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: 100% 100%;
  z-index: -100;
}
.icon {
  width: 1.5em;
  height: 1.5em;
  vertical-align: -0.35em;
  fill: currentColor;
  overflow: hidden;
}
</style>
