<template>

    <el-row justify="center">
        <el-backtop :right="100" :bottom="100" />
        <el-col :span="15" class="card">
            <el-tabs v-model="activeName" type="card" class="demo-tabs" @tab-click="handleClick">
                <el-tab-pane label="知乎" name="zhihu">
                    <hot-spot-table site="zhihu"/>
                </el-tab-pane>
                <el-tab-pane label="微博" name="weibo">
                    <hot-spot-table site="weibo"/>
                </el-tab-pane>
                <el-tab-pane label="贴吧" name="tieba">
                    <hot-spot-table site="tieba"/>
                </el-tab-pane>
                <el-tab-pane label="豆瓣" name="douban">
                    <hot-spot-table site="douban"/>
                </el-tab-pane>
                <el-tab-pane label="天涯" name="tianya">
                    <hot-spot-table site="tianya"/>
                </el-tab-pane>
                <el-tab-pane label="云音乐热门" name="wangyi">
                    <hot-spot-table site="wangyiyun"/>
                </el-tab-pane>
            </el-tabs>
        </el-col>
    </el-row>
</template>
<script lang="ts" setup>
import type { TabsPaneContext } from 'element-plus'

const activeName = ref('zhihu')
const handleClick = (tab: TabsPaneContext, event: Event) => {
    console.log(tab, event)
}
</script>
<style scoped>
.card {
    background-color: white;
    padding: 24px
}
</style>
