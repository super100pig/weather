<template>
  <div>
    <el-row>
      <el-input v-model="data_name" placeholder="请输入数据名称" style="width: 300px"></el-input>
      <el-button @click="open1">选择文件</el-button>
      <el-button type="primary" @click="open2">开始上传并处理</el-button>
    </el-row>
    <el-table
        ref="multipleTable"
        :data="tableData"
        tooltip-effect="dark"
        style="width: 100%"
    >
      <el-table-column prop="id" label="ID" width="120" sortable></el-table-column>
      <el-table-column prop="data_name" label="数据名称" width="120" sortable></el-table-column>
      <el-table-column prop="status" label="上传状态" width="120" sortable></el-table-column>
      <el-table-column prop="start_time" label="开始时间" width="240" sortable></el-table-column>
      <el-table-column prop="end_time" label="完成时间" width="240" sortable></el-table-column>
    </el-table>
  </div>
</template>

<script>
function wait(ms) {
  return new Promise(resolve => setTimeout(() =>resolve(), ms));
}
export default {
  data() {
    return {
      algorithm_name: "算法1",
      data_name: "",
      tableData: [
        {
          "id": 1,
          "data_name": "数据1",
          "status": "正在处理",
          "start_time": "2021.3.30",
          "end_time": "2021.3.30",
        },
        {
          "id": 2,
          "data_name": "数据2",
          "status": "上传成功",
          "start_time": "2021.3.30",
          "end_time": "2021.3.30",
        },
        {
          "id": 3,
          "data_name": "数据3",
          "status": "上传成功",
          "start_time": "2021.3.30",
          "end_time": "2021.3.30",
        },
        {
          "id": 4,
          "data_name": "数据4",
          "status": "上传成功",
          "start_time": "2021.3.30",
          "end_time": "2021.3.30",
        },
        {
          "id": 5,
          "data_name": "数据5",
          "status": "上传成功",
          "start_time": "2021.3.30",
          "end_time": "2021.3.30",
        },
      ]
    }
  },
  mounted() {
    this.show_algorithm()
  },
  methods: {
    show_algorithm() {
      this.$axios
          .get("http://" + localStorage.getItem('backend_host') + "/get_algorithms/")
          .then(response => {
            this.tableData = response.data;
            console.log(this.tableData);
          });
    },
    open1() {
      this.$message('算法正在执行……');
      wait(3000).then(()=>{
        localStorage.setItem("flag", "true");
        this.$message({
          message: '算法执行成功！',
          type: 'success'
        });
      })
    },
    open2() {
      this.$message('算法进程创建成功！');
      localStorage.setItem("flag", "true");
      this.$axios
          .get("http://" + localStorage.getItem('backend_host') + "/run_algorithm/",
              {
                params: {
                  algorithm_name: this.algorithm_name,
                  data_name: this.data_name
                }
              })
          .then(() => {
            this.show_algorithm()
          })
    }
  }
}
</script>