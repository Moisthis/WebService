<template>
  <!--头部区  -->
  <el-container class="home-container">
    <el-header>
      <div>
        <img src="../assets/child.jpg" alt=""/>
        <span>人员信息收集系统</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>
    <!-- 页面主体区 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="200px">
        <!-- 侧边栏菜单区域 -->
        <div>
          <img src="../assets/xiaomai.jpg" alt=""><br/>
          <span>Welcome!</span>
        </div>
        <el-menu
            background-color="#52ACFF"
            text-color="#000084"
            active-text-color="#ffd04b"
            unique-opened
            router>
          <el-submenu index="1">
            <template slot="title">
              <i class="iconfont icon-icon_xinyong_xianxing_jijin-"></i>
              <span>信息管理</span>
            </template>
            <el-menu-item index="1-1" @click="sub">
              <template>
                <i class="el-icon-menu"></i>
                <span>个人信息展示</span>
              </template>
            </el-menu-item>
          </el-submenu>
          <el-submenu index="3" v-show="this.userID == 1">
            <template slot="title">
              <i class="iconfont icon-haoyou"></i>
              <span>用户管理</span>
            </template>
            <el-menu-item index="3-1">
              <template>
                <i class="el-icon-menu"></i>
                <span>用户列表</span>
              </template>
            </el-menu-item>
          </el-submenu>
          <el-submenu index="4">
            <template slot="title">
              <i class="iconfont icon-zhaoxueyuan"></i>
              <span>学院管理</span>
            </template>
            <el-menu-item index="4-1">
              <template>
                <i class="el-icon-menu"></i>
                <span>学院列表</span>
              </template>
            </el-menu-item>
          </el-submenu>
          <el-submenu index="5">
            <template slot="title">
              <i class="iconfont icon-bumen"></i>
              <span>部门管理</span>
            </template>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 右侧内容主体 -->
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      userID: this.$route.query.permission
    }
  },
  methods: {
    logout() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
  }
}
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
  background-color: #eaedf1;
}

.el-header {
  background-color: #08AEEA;
  background-image: linear-gradient(0deg, #08AEEA 0%, #2AF598 100%);
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  color: #000084;
  font-size: 25px;
  font-weight: bold;
  font-family: "Lucida Console", monospace;
  align-items: center;

  > div {
    display: flex;
    align-items: center;

    span {
      margin-left: 15px;
    }
  }

  img {
    height: 60px;
    width: 75px;
    border-radius: 50%;

  }
}

.el-aside {
  margin-top: 20px;
  margin-bottom: 20px;
  //background-color:#8ed4c7;
  background-color: #52ACFF;
  border-radius: 15px;

  .el-menu {
    border-right: none;
  }

  > div {
    padding-left: 10px;
    padding-bottom: 20px;
    text-align: center;
    color: #000084;
  }

  img {
    padding-top: 10px;
    width: 80%;
    height: 130px;
    border-radius: 60%;
    cursor: pointer;
  }
}

.el-main {
  background-color: #eaedf1;
}

</style>
