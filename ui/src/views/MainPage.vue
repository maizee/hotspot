<template>
    <el-row justify="center">
        <el-col :span="18">
            <el-row :gutter="16">
                <el-col :span="8">
                    <p>
                        <hot-spot-card site="weibo"></hot-spot-card>
                    </p>
                </el-col>
                <el-col :span="8">
                    <p>
                        <hot-spot-card site="zhihu"></hot-spot-card>
                    </p>
                </el-col>
                <el-col :span="8">
                    <p>
                        <hot-spot-card site="douban"></hot-spot-card>
                    </p>
                </el-col>
            </el-row>
            <el-row :gutter="24">

                <el-col :span="8">
                    <p>
                        <hot-spot-card site="wangyiyun"></hot-spot-card>
                    </p>
                </el-col>
                <el-col :span="8">
                    <p>
                        <hot-spot-card site="tianya"></hot-spot-card>
                    </p>
                </el-col>
                <el-col :span="8">
                    <p>
                        <hot-spot-card site="tieba"></hot-spot-card>
                    </p>
                </el-col>
            </el-row>
        </el-col>
    </el-row>
</template>

<script setup lang="ts">

</script>

<style scoped>
</style>