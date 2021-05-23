<template>
  <div style="margin-left:20px;margin-top:20px;">
    <el-row type="flex" :gutter="20">
      <el-col :span="5">
        <a style="font-size: small">测试项目名称：</a>
        <el-select style="width: 300px" v-model="testItem" placeholder="请选择测试项目名称">
          <el-option label="BMS.ReadMaxTemperature" value=1></el-option>
          <el-option label="BMS.ReadMinTemperature" value=2></el-option>
          <el-option label="BMS.TemperatureDelta" value=3></el-option>
        </el-select>
      </el-col>

      <a style="font-size: small">该测试项目的相关故障车辆：26, 75, 121</a>
    </el-row>
    <el-row type="flex" :gutter="20">
    </el-row>

    <el-table
        ref="multipleTable"
        :data="tableData"
        tooltip-effect="dark"
        style="width: 100%"
        @selection-change="handleSelectionChange"
    >
      <el-table-column prop="device_id" label="相关异常节点" width="480" sortable></el-table-column>
      <el-table-column prop="score" label="分数" width="240" sortable></el-table-column>
      <el-table-column prop="related_car" label="相关车辆" width="240" sortable></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      testItem: "BMS.ReadMaxTemperature",
      dialogTableVisible: false,
      tableData: [
        {'device_id': 'BMS.ReadMinTemperature', 'score': 0.527, 'related_car': '121'},
        {'device_id': "PEU", 'score': 0.480, 'related_car': '26, 75, 121'},
        {'device_id': "BMS.ReadMaxTemperature", 'score': 0.458, 'related_car': '26, 121'},
        {'device_id': "PTC", 'score': 0.456, 'related_car': '75, 121'}
      ],
      time_range: [new Date(2018, 0, 28), new Date(2020, 2, 1)],
      filterModule: "数据1"
    };
  },
  mounted() {
    // this.show_data();
  },
  methods: {
    show_data() {
      this.$axios
          .get("http://" + localStorage.getItem('backend_host') + "/get_devices/")
          .then(response => {
            this.tableData = response.data;
          });
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    }
  }
};
</script>