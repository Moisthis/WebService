<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>学院管理</el-breadcrumb-item>
      <el-breadcrumb-item>学院列表</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card>
      <el-row :gutter="20">
        <el-col :span="8">
          <el-input placeholder="请输入内容">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="6">
          <el-button type="primary">添加用户</el-button>
        </el-col>
      </el-row>

      <el-table :data="shoollist" border stripe>
        <el-table-column prop="school_name" label="院名"></el-table-column>
        <el-table-column prop="grade" label="年级"></el-table-column>
        <el-table-column prop="major" label="专业"></el-table-column>
        <el-table-column prop="stu_class" label="班级"></el-table-column>
        <el-table-column prop="post" label="职位"></el-table-column>
        <el-table-column label="操作">
          <template>
            <el-tooltip effect="dark" content="修改信息" placement="top" :enterable="false">
              <el-button type="primary" icon="el-icon-edit"></el-button>
            </el-tooltip>
            <el-tooltip effect="dark" content="删除信息" placement="top" :enterable="false">
              <el-button type="danger" icon="el-icon-delete"></el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      schoollist: []
    }
  },
  /* mounted() {
      this.$nextTick(function(){
          this.getSchoolList()
      })
  }, */
}
</script>

<style>

</style>