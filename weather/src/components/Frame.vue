<template>
  <div id="app">
    <el-container>
      <el-header style="background-color: midnightblue" height="80px">
        <el-row>
          <div style="font-size: xx-large; color: white; font-family: 幼圆,serif">天气图谱</div>
        </el-row>
        <el-row type="flex" justify="end">
          <el-col :span="6">
            <el-dropdown>
              <el-button icon="el-icon-user" round>
                欢迎登陆，王小明！<i class="el-icon-arrow-down el-icon--right"></i>
              </el-button>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item>设置</el-dropdown-item>
                <el-dropdown-item>切换账号</el-dropdown-item>
                <el-dropdown-item>注销</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </el-col>
        </el-row>

      </el-header>
    </el-container>
    <el-container>
      <el-aside style="background-color: #545c64">
        <el-menu default-active="/uploadPage" :default-openeds="['1', '2']" class="el-menu-vertical-demo" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" router>
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>异常天气</span>
            </template>
            <el-menu-item index="/wgGraph">
              <span slot="title">
                网格数据
              </span>
            </el-menu-item>
            <el-menu-item index="/rxGraph">
              <span slot="title">
                热线数据
              </span>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-main>
          <router-view></router-view>
        </el-main>
        <el-footer>©上海市数据科学重点实验室</el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>

export default {
  name: 'frame'
}
</script>

<style>
</style>
