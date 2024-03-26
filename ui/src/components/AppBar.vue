<template>
  <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect" :router="true">
    <el-menu-item index="/index">
      <el-icon :size="18" color="red">
        <home-filled></home-filled>
      </el-icon>
      主页快览
    </el-menu-item>
    <el-menu-item index="/hotspot">
      <el-icon :size="18" color="red">
        <promotion></promotion>
      </el-icon>
      热点内容
    </el-menu-item>
    <el-menu-item index="favor">
      <el-icon :size="18" color="red">
        <star-filled></star-filled>
      </el-icon>
      我的收藏
    </el-menu-item>
    <el-menu-item index="/history">
      <el-icon :size="18" color="red">
        <Paperclip></Paperclip>
      </el-icon>
      历史记录
    </el-menu-item>
    <el-menu-item index="/userinfo">
      <el-icon :size="18" color="red">
        <avatar></avatar>
      </el-icon>
      个人中心
    </el-menu-item>
    <el-menu-item index="/about">
      <el-icon :size="18" color="red">
        <message></message>
      </el-icon>
      关于我们
    </el-menu-item>
  </el-menu>
</template>

<script setup lang="ts">

const activeIndex2 = ref("/index")
const handleSelect = () => {

}
</script>

<style scoped>
.el-menu-demo {
  justify-content: center;
  margin-inline: 40px;
}
</style>