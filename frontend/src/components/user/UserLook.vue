<template>
  <div>
      <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>信息管理</el-breadcrumb-item>
        <el-breadcrumb-item>个人信息展示</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <div>
        <h1>
          个人信息
        </h1>
        <hr width="100%" size="2" noshade="noshade" color="#00E5EE"/>
        <div id="one">基本信息</div>
        <el-form :inline="true" class="demo-form-inline">
          <el-form-item label="姓名" style="margin-left:30px">
            <el-input disabled="ture" v-model="UserMeForm.name"></el-input>
          </el-form-item>
          <el-form-item label="性别" style="margin-left:260px">
            <el-input disabled="ture" v-model="UserMeForm.gender"></el-input>
          </el-form-item>
        </el-form>
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
          <el-form-item label="电话" style="margin-left:30px">
            <el-input disabled="ture" v-model="UserMeForm.phone"></el-input>
          </el-form-item>
          <el-form-item label="年级" style="margin-left:260px">
            <el-input disabled="ture" v-model="UserMeForm.grade"></el-input>
          </el-form-item>
        </el-form>
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
          <el-form-item label="学院" style="margin-left:30px"> 
            <el-input disabled="ture" v-model="UserMeForm.school_name"></el-input>
          </el-form-item>
          <el-form-item label="专业" style="margin-left:260px">
            <el-input disabled="ture" v-model="UserMeForm.major"></el-input>
          </el-form-item>
        </el-form>
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
          <el-form-item label="班级" style="margin-left:30px">
            <el-input disabled="ture" v-model="UserMeForm.stu_class"></el-input>
          </el-form-item>
          <el-form-item label="部门" style="margin-left:260px">
            <el-input disabled="ture" v-model="UserMeForm.department_name"></el-input>
          </el-form-item>
        </el-form>
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
          <el-form-item label="部门职务">
            <el-input disabled="ture" v-model="UserMeForm.position"></el-input>
          </el-form-item>
          <el-form-item label="出生日期" style="margin-left:235px">
            <el-input disabled="ture" v-model="UserMeForm.birthday"></el-input>
          </el-form-item>
           <el-form-item style="margin-left:60px">
            <el-button type="success" round @click="sub">获取数据</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  data(){
    return{
       UserMeForm:{
        id:'',
        name:'',
        birthday:'',
        gender:'',
        phone:'',
        school_name:'',
        stu_class:'',
        grade:'',
        major:'',
        department_name:'',
        position:''
        }
    }
  },
  mounted() {
    this.$nextTick(function(){
      this.sub()
    })
  },
  methods:{
     async sub(){
            const res = await this.$http.get('api/user/userinfo/')
            this.UserMeForm.name = res.data[0]['name']
            this.UserMeForm.birthday = res.data[0]['birthday']
            this.UserMeForm.gender = res.data[0]['gender']
            this.UserMeForm.phone = res.data[0]['phone']

            this.UserMeForm.school_name = res.data[1]['school_name']
            this.UserMeForm.stu_class = res.data[1]['stu_class']
            this.UserMeForm.grade = res.data[1]['grade']
            this.UserMeForm.major = res.data[1]['major']

            this.UserMeForm.department_name = res.data[2]['department_name']
            this.UserMeForm.position = res.data[2]['position']
          }
  }

}
</script>

<style lang="less" scoped>
</style>