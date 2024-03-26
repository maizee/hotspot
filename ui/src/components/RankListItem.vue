<template>
    <el-row style="white-space: nowrap;">
        <div :class="{ 'tag-primary': (tag <= 3), 'tag-secondary': (tag > 3) }">{{ tag }}</div>
        <a class="text" :href="href" @click="addHistory({ href: href, title: title })">
            <slot>{{ title }}</slot>
        </a>
    </el-row>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { updateHistory } from '../api';
const props = defineProps({ tag: { type: Number, default: 0 }, href: { type: String }, title: { type: String } })
function addHistory(data: any) {
    updateHistory(data).then((res) => {
        console.log('%cHistoryPage.vue line:9 res.data', 'color: #007acc;', res.data);
    })
}
</script>

<style scoped>
.tag-primary {
    color: ghostwhite;
    font-size: small;
    align-items: center;
    text-align: center;
    line-height: 24px;
    background-color: #53a8ff;
    border-radius: 6px;
    width: 24px;
    height: 24px;
    top: 0;
    left: 0;
}

.tag-secondary {
    color: ghostwhite;
    font-size: small;
    align-items: center;
    text-align: center;
    line-height: 24px;
    background-color: #909399;
    border-radius: 6px;
    width: 24px;
    height: 24px;
    top: 0;
    left: 0;
}

.text {
    text-align: center;
    max-width: 80%;
    font-size: small;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    word-break: break-all;
    margin-left: 8px;
    justify-content: left;
    color: #303133;
    text-decoration: none;
    transition: 0.2s;
    line-height: 24px;
    cursor: pointer;
}

.text:hover {
    color: #409eff;
}
</style>