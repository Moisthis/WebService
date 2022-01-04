<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 头像区域 -->
      <div class="avatar_box">
        <img src="../assets/child.jpg" alt="">
      </div>
      <!-- 登录表单区域 -->
      <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="80px" class="login_form">
        <!-- 用户名 -->
        <el-form-item label="账号" prop="username">
          <el-input v-model="loginForm.username" prefix-icon="el-icon-user-solid"></el-input>
        </el-form-item>
        <!-- 密码 -->
        <el-form-item label="密码" prop="password">
          <el-input v-model="loginForm.password" prefix-icon="el-icon-s-goods" type="password"></el-input>
        </el-form-item>
        <!-- 验证码 -->
        <el-form-item label="验证码" prop="captcha" clearable>
          <el-input v-model="loginForm.captcha" placeholder="请输入验证码">
          </el-input>
        </el-form-item>
        <!-- 按钮区域 -->
        <el-form-item style="margin-bottom:10px">
          <div>
                    <span class="code">
                        <img :src="veriticationImg" alt="" style="width:125px; height:65px;cursor: pointer"
                             @click="acquireVerification">
                    </span>
            <span class="btns">
                        <el-button type="primary" @click="login">登录</el-button>
                        <el-button type="info" @click="resetLoginForm">重置</el-button>
                    </span>
          </div>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      //这是登录表单的数据绑定对象
      loginForm: {
        username: 'admin',
        password: 'admin',
        captcha: '',
        imgcode_id: ''
      },
      veriticationImg: '',
      //这是表单的验证规则对象
      loginFormRules: {
        //验证用户名是否合法
        username: [
          {required: true, message: '请输入登录名称', trigger: 'blur'},
          {min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur'}
        ],
        //验证密码是否合法
        password: [
          {required: true, message: '请输入登录密码', trigger: 'blur'},
          {min: 5, max: 15, message: '长度在 5 到 15 个字符', trigger: 'blur'}
        ],

      }
    }
  },
  mounted() {
    this.$nextTick(function () {
      this.acquireVerification()
    })
  },
  methods: {
    //点击重置按钮，重置登录表单
    resetLoginForm() {
      this.$refs.loginFormRef.resetFields();
    },
    login() {
      this.$refs.loginFormRef.validate(async valid => {
        if (!valid) return;
        const res = await this.$http.post('api/login/captcha/token/', this.loginForm)
        if (res.status !== 200) return this.$message.error('登录失败!');
        this.$message.success('登录成功！')
        //1.将登录成功之后的token，保存到客户端的sessionstore中
        //项目中除了登录之外的其他API接口，必须在登录之后才能访问
        //token只应在当前网站打开期间有效，所以将token保存在sessionStorage中
        window.sessionStorage.setItem("token", res.data.access)
        //2.通过编程式导航跳转到后台主页，路由地址是/home
        this.$router.push({
          path: "/home",
          query: {
            permission: res.data.permission
          }
        })
      })
    },
    acquireVerification() {
      this.$refs.loginFormRef.validate(async valid => {
        if (!valid) return;
        await this.$http.get('api/login/captcha/').then((response) => {
          this.loginForm.imgcode_id = response.data.id
          this.veriticationImg = response.data.image_base
        })
      })
    }
  },
}
</script>

<style lang="less" scoped>
.login_container {
  height: 100%;
  background: url("../assets/sky.jpg") no-repeat;
  background-size: cover;
}

.login_box {
  width: 450px;
  height: 300px;
  background-color: plum;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  opacity: 0.8;

  .avatar_box {
    height: 130px;
    width: 130px;
    border: 0px solid #eee;
    border-radius: 50%;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    padding-bottom: 50px;

    img {
      height: 100%;
      width: 100%;
      border-radius: 50%;
    }
  }
}

.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 60px;
  padding-left: 10px;
  box-sizing: border-box;
}

.code {
  width: 50%;
  //display: flex;
  //justify-content: flex-start;
  //padding-bottom: 0;
}

.btns {
  margin-right: 0%;
}
</style>
