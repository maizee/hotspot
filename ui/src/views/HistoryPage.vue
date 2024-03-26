<template>
    <el-backtop :right="100" :bottom="100" />
    <el-row justify="center">
        <el-col :span="12">

            <el-empty v-if="historyList.length==0" description="暂无内容"  style='margin-top:200px'/>
            <el-card v-else style="border-radius: 20px;padding-top:30px">
                <el-timeline>
                    <el-timeline-item v-for="(activity, index) in historyList" :key="index"
                        :timestamp="activity.time.slice(0, 19).replace('T', ' ')">
                        <el-link :href="activity.href" style="font-size:large">{{ activity.title }}</el-link>
                    </el-timeline-item>
                </el-timeline>
            </el-card>
        </el-col>
    </el-row>
</template>
    
<script setup lang='ts'>
import { getHistory } from '../api';
const historyList = ref(Array())
getHistory().then((res) => {
    console.log('%cHistoryPage.vue line:9 res.data', 'color: #007acc;', res.data);
    historyList.value = res.data.result
})

</script>
    
<style scoped>
</style>