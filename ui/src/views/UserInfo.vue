<template>
    <div class="bg">
        <el-card class="card-left">
            <div>

                <el-row class="list-user-info">
                    <el-icon style="margin: 8px;">
                        <edit />
                    </el-icon>用户名：{{ username }}
                </el-row>
                <el-row class="list-user-info">
                    <el-icon style="margin: 8px;">
                        <user />
                    </el-icon>用户组：{{ "普通用户" }}
                </el-row>
                <el-row class="list-user-info">
                    <el-icon style="margin: 8px;">
                        <cloudy />
                    </el-icon>{{ "创建时间：" + dateJoined }}
                </el-row>
                <el-row>
                    <p>
                        <el-button @click="logout"> 登 出 </el-button>
                    </p>
                </el-row>
            </div>
        </el-card>
    </div>
</template>

<script setup lang="ts">
import { Iphone, User, Message, Cloudy, Edit } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus';
import { getUserInfo } from '../api';
import router from '../router/router';
const username = ref("测试名")
const dateJoined = ref("2022-02-04")
function logout() {
    localStorage.setItem('ACCESS_TOKEN', "");
    ElMessage({ message: '成功登出账号', type: "success", offset: 40 })
    router.go(0)
}
getUserInfo().then((res)=>{
    username.value = res.data.username
})
</script>

<style scoped>
.bg {
    height: 100%;
    position: fixed;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.card-left {
    position: fixed;
    top: 270px;
    border-radius: 20px;
    height: 200px;
    width: 20%;
    min-width: 400px;
    line-height: 32px;
    padding: 32px 16px 24px 16px;
    justify-content: center;
}

.list-user-info {
    font-size: middle;
    font-weight: lighter;
    align-items: baseline;
}
</style>