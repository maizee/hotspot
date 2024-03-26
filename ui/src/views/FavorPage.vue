<template>
<el-empty v-if="favorList.length==0" description="暂无内容" style='margin-top:200px'/>
<el-space v-else wrap style="justify-content:center">
    <favor-card  v-for="i in favorList" :title="i.title" :site="i.site" :href="i.href"></favor-card>
</el-space>
</template>
    
<script setup lang='ts'>
import { getFavor } from '../api';
const favorList=ref(Array())

getFavor().then((res)=>{
    console.log('%cFavorPage.vue line:12 res.data', 'color: #007acc;', res.data);
    favorList.value = res.data.result
})
</script>
    
<style scoped>
</style>