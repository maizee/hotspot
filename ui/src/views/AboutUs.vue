<template>
  <el-row justify="center" style="margin-top: 64px;">
  <el-col :span="12">
    <el-card>
      <md-editor v-model="text" previewOnly class="content" />
    </el-card>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import MdEditor from "md-editor-v3";
import 'md-editor-v3/lib/style.css';
const text = `
### 关于我们


>  Follow your heart.

![](https://pandao.github.io/editor.md/examples/images/8.jpg)

  **经过了四年的学习，大学生活接近尾声。在这四年多的时间里，我获得的不仅仅是知识，还有在实践中培养的思维方式。离校的日期将近，我的毕业设计的完成也接近尾声。经过几个月的时间，从选题到最后的定稿，期间获得了导师和同学的帮助和支持。没有这些良师益友，我的论文不会如此顺利的完成。在此，我致以最诚挚的谢意!**
`
</script>

<style scoped>
</style>