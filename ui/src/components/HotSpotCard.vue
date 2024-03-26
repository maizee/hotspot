<template>
    <el-card shadow="hover">
        <template #header>
            <div class="card-header">
                <svg class="icon" aria-hidden="true">
                    <use :xlink:href="'#icon-' + site"></use>
                </svg>
                <span style="margin-left:12px">{{ title }}</span>
                <el-button class="button" text>
                    <el-icon>
                        <Link />
                    </el-icon>
                </el-button>
            </div>
        </template>
        <rank-list-item v-for="i, index in tableData" :tag="index + 1" :title="i.title" :href="i.href"
            style="margin-bottom:18px;margin-left:8px;margin-right:8px"></rank-list-item>
    </el-card>
</template>
    
<script setup lang='ts'>


import { getRank } from "../api"
const props = defineProps(["site"])
const tableData = ref(Array())
const title = ref("加载中。。。")
getRank(props.site).then((res) => {
    let li: object[] = res.data.content
    tableData.value = li.slice(0, 6)
    title.value = res.data.hot_name
    console.log('%cHotSpot.vue line:12 object', 'color: #007acc;', tableData.value);
})
</script>
    
<style scoped>
</style>