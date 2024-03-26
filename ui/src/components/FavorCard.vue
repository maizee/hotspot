<template>

    <el-card class="card" shadow="hover">
        <el-row>
            <el-col :span="2" style="display:flex; align-items: center;">
                <svg class="favor-icon" aria-hidden="true">
                    <use :xlink:href="'#icon-' + site"></use>
                </svg>
            </el-col>
            <el-col :span="2" style="display:flex; align-items: center;">
                <el-divider direction="vertical" style="height:120px"></el-divider>
            </el-col>
            <el-col :span="20">
                <el-tooltip :content="href.length>50?href.slice(0,30)+'...':href" placement="top">
                    <el-link class="text" :href="href" :underline="false" @click="addHistory({ href: href, title: title })">{{ title }}</el-link>
                </el-tooltip>
            </el-col>
        </el-row>
    </el-card>
</template>
    
<script setup lang='ts'>import { updateHistory } from '../api';

const props = defineProps(['site', "title", "href"])
function addHistory(data: any) {
    updateHistory(data).then((res) => {
        console.log('%cHistoryPage.vue line:9 res.data', 'color: #007acc;', res.data);
    })
}
</script>
    
<style scoped>
.card {
    width: 500px;
    height: 160px;
}

.favor-icon {
    width: 3em;
    height: 3em;
    vertical-align: -0.35em;
    fill: currentColor;
    overflow: hidden;

}

.text {
    font-size: x-large;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>