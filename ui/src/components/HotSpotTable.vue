<template>

    <el-table :data="tableData" style="width: 100%" :show-header="false" :border="true" stripe lazy>
        <el-table-column prop="title" label="标题">
            <template #default="scope">
                <el-row justify="space-between">
                    <el-col :span="23">
                        <el-link :href="scope.row.href" target="_blank" :underline="false"
                            @click="addHistory({ href: scope.row.href, title: scope.row.title })">
                            {{ (scope.$index + 1) + '. ' + scope.row.title }}
                        </el-link>
                    </el-col>
                    <el-col :span="1">
                        <el-button type="primary" size="small" @click="buttonClick(scope.row.title, scope.row.href)">收藏
                        </el-button>
                    </el-col>
                </el-row>
            </template>
        </el-table-column>
    </el-table>
</template>

<script lang="ts" setup>
import { getRank, updateFavor, updateHistory } from "../api"
const props = defineProps(["site"])
const tableData = ref(Array())
let tableName = ""
getRank(props.site).then((res) => {
    console.log('%cHotSpot.vue line:12 object', 'color: #007acc;', res.data);
    tableData.value = res.data.content
    tableName = res.data.hot_name
})
function addHistory(data: any) {
    updateHistory(data).then((res) => {
        console.log('%cHistoryPage.vue line:9 res.data', 'color: #007acc;', res.data);
    })
}
function buttonClick(title: string, href: string) {
    updateFavor({ site: props.site, title: title, href: href }).then((res) => {
        console.log('%cHotSpotTable.vue line:40 res.data', 'color: #007acc;', res.data);
        if (res.data.result == "添加成功") {
            ElMessage({
                message: "添加收藏成功",
                type: "success",
                offset: 40,
            });
        }
        else {
            ElMessage({
                message: "收藏内容已存在",
                type: "warning",
                offset: 40,
            });
        }
    })
}
</script>
