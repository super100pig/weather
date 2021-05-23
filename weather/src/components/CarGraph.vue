<template>
  <div style="margin-left:20px;margin-top:20px;">
<!--    <el-row type="flex" :gutter="20">-->
<!--      <el-col :span="7">-->
<!--        <a style="font-size: small">测试项目名称：</a>-->
<!--        <el-input style="width: 300px" v-model="selectedNode" placeholder="请输入测试项目名称"></el-input>-->
<!--      </el-col>-->
<!--    </el-row>-->
    <el-row type="flex" :gutter="20">
      <el-col :span="5">
        <a style="font-size: small">测试项目名称：</a>
        <el-select style="width: 300px" v-model="testItem" placeholder="请选择测试项目名称">
          <el-option label="BMS.ReadMaxTemperature" value=1></el-option>
          <el-option label="BMS.ReadMinTemperature" value=2></el-option>
          <el-option label="BMS.TemperatureDelta" value=3></el-option>
        </el-select>
      </el-col>
      <el-col :span="3">
        <el-switch v-model="showOk" active-text="显示OK边" inactive-text="不显示OK边"></el-switch>
      </el-col>
      <el-col :span="4">
        <el-button type="primary" @click="load_and_show">可视化结果</el-button>
      </el-col>
    </el-row>
    <el-dialog title="训练参数" :visible.sync="setParametersVisible">
      <el-form :model="parameters">
        <el-form-item label="最小支持度" :label-width="formLabelWidth">
          <el-input v-model="parameters.support" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="最小置信度" :label-width="formLabelWidth">
          <el-input v-model="parameters.conf" autocomplete="off"></el-input>
        </el-form-item>
        <!-- <el-form-item label="最小关联元数" :label-width="formLabelWidth">
          <el-input v-model="parameters.min_item_num" autocomplete="off"></el-input>
        </el-form-item> -->
        <el-form-item label="滑窗步长" :label-width="formLabelWidth">
          <el-input v-model="parameters.step" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="窗口大小" :label-width="formLabelWidth">
          <el-input v-model="parameters.window" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="setParametersVisible = false">取 消</el-button>
        <el-button type="primary" @click="setParametersVisible = false">确 定</el-button>
      </div>
    </el-dialog>
    <div id="neo4jd3" style="height: 800px;"></div>
  </div>
</template>

<script>
// document.getElementById('neo4jd3').style.display = '';
function rel2DataRelationship(r) {
  return r;
}

function graphNode2DataNode(r) {
  return r;
}

let neo4jd3Instance;

let screen_height, screen_width;

function init() {
  const eleId = "neo4jd3";
  console.log(document.getElementById(eleId));
  document.getElementById(eleId).innerHTML = "";
  // @ts-ignore
  // eslint-disable-next-line no-undef
  let temp_neo4jd3Instance = new Neo4jd3("#neo4jd3", {
    highlight: [],
    red_rel: [],
    icons: {
      客户: "user",
      person: "user",
      Person: "user",
      Relation: "yelp",
      基金: "money",
      项目: "database",
      Company: "university",
      People: "handshake-o",
      stock: "credit-card",
      User: "user",
      Business: "yelp",
      Industry: "database",
      Shareholder: "money",
      Module: "database",
      Component: 'gear,cog',
      Car: 'automobile,car',
      Check: 'check-square',
      PreCheck: 'check-circle',
    },
    images: {
      Contributor: "https://eisman.github.io/neo4jd3/img/twemoji/1f38f.svg",
      Project: "https://eisman.github.io/neo4jd3/img/twemoji/1f5c3.svg"
    },
    minCollision: 60,
    neo4jData: {results: [], errors: []},
    nodeRadius: 30,
    onNodeDoubleClick: onNodeDoubleClicked,
    onRelationshipDoubleClick: onRelationshipDoubleClicked,
    zoomFit: false
  });
  screen_height = temp_neo4jd3Instance.get_screen_height();
  screen_width = temp_neo4jd3Instance.get_screen_width();
  console.log(screen_width, screen_height);
  return temp_neo4jd3Instance;
}

// eslint-disable-next-line no-unused-vars
function onNodeDoubleClicked(node) {
  // console.log("double click on node: ", node);
}

function onRelationshipDoubleClicked(relationship) {
  console.log("double click on relationship: ", relationship);
}

function show_data(graph_data) {
  let temp;
  neo4jd3Instance = init();
  // (document.getElementById("select_id3") as HTMLSelectElement).disabled = false;
  temp = graph_data;
  // console.log("出现了！res");
  // console.log(res);
  const d3Data = {
    nodes: [],
    relationships: []
  };
  for (let i in temp.nodes) {
    d3Data.nodes.push(graphNode2DataNode(temp.nodes[i]));
  }

  let important_rel = [];
  for (let i in temp.relationships) {
    d3Data.relationships.push(rel2DataRelationship(temp.relationships[i]));

    if (temp.relationships[i].type === "Recommend") {
      important_rel.push(temp.relationships[i].id);
    }
  }
  // console.log("important_rel", important_rel);
  console.info("d3Data");
  console.info(d3Data);
  neo4jd3Instance.replaceWithD3Data(d3Data, [graph_data['center_id']], important_rel);
}

let module_id_map = {
  AS: 1,
  CCS: 2,
  AAA: 3,
  MDU: 4,
  VOD: 5,
  GBSG: 6,
  SA: 7
};
let rel_id = 100;
let graph_data = {
  "nodes": [
    {
      "labels": [
        "Check"
      ],
      "id": 1,
      "properties": {
        "name": "BMS.ReadMaxTemperature",
        "table": 'W3_08',
        "color": "RGB(225, 0, 0)"
      },
      "showName": "BMS.ReadMaxTemperature"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 2,
      "properties": {
        "name": "Car 25",
      },
      "showName": "Car 25"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 3,
      "properties": {
        "name": "Car 115",
      },
      "showName": "Car 115"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 4,
      "properties": {
        "name": "Car 149",
      },
      "showName": "Car 149"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 5,
      "properties": {
        "name": "Car 193",
      },
      "showName": "Car 193"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 6,
      "properties": {
        "name": "Car 232",
      },
      "showName": "Car 232"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 7,
      "properties": {
        "name": "Car 237",
      },
      "showName": "Car 237"
    },
    {
      "labels": [
        "PreCheck"
      ],
      "id": 8,
      "properties": {
        "name": "BMS.ReadMinTemperature",
        'table': "W3_07",
        'score': 0.527,
        "color": "RGB(225, 128, 128)"
      },
      "showName": "BMS.ReadMinTemperature"
    },
    {
      "labels": [
        "PreCheck"
      ],
      "id": 9,
      "properties": {
        "name": "PEU",
        'table': "W3_05",
        'score': 0.480,
        "color": "RGB(225, 150, 150)"
      },
      "showName": "PEU"
    },
    // {
    //   "labels": [
    //     "PreCheck"
    //   ],
    //   "id": 10,
    //   "properties": {
    //     "name": "BCM.BATT12VSOCRead",
    //     'table': "W3_07"
    //   },
    //   "showName": "BCM.BATT12VSOCRead"
    // },
    {
      "labels": [
        "PreCheck"
      ],
      "id": 11,
      "properties": {
        "name": "BMS.ReadMaxTemperature",
        'table': "W3_07",
        'score': 0.458,
        'color': "RGB(255, 160, 160)"
      },
      "showName": "BMS.ReadMaxTemperature"
    },
    {
      "labels": [
        "PreCheck"
      ],
      "id": 12,
      "properties": {
        "name": "PTC",
        'table': "W3_05",
        'score': 0.456,
        'color': "RGB(255, 165, 165)"
      },
      "showName": "PTC"
    },
  ],
  "relationships": [
    {
      "startNode": 1,
      "endNode": 2,
      "source": 1,
      "target": 2,
      "id": 201,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 3,
      "source": 1,
      "target": 3,
      "id": 202,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 4,
      "source": 1,
      "target": 4,
      "id": 203,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 5,
      "source": 1,
      "target": 5,
      "id": 204,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 6,
      "source": 1,
      "target": 6,
      "id": 205,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 7,
      "source": 1,
      "target": 7,
      "id": 206,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 5,
      "endNode": 8,
      "source": 5,
      "target": 8,
      "id": 207,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 6,
      "endNode": 8,
      "source": 6,
      "target": 8,
      "id": 208,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 2,
      "endNode": 9,
      "source": 2,
      "target": 9,
      "id": 209,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 3,
      "endNode": 9,
      "source": 3,
      "target": 9,
      "id": 210,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 7,
      "endNode": 9,
      "source": 7,
      "target": 9,
      "id": 211,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 2,
      "endNode": 11,
      "source": 2,
      "target": 11,
      "id": 212,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 3,
      "endNode": 11,
      "source": 3,
      "target": 11,
      "id": 213,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 4,
      "endNode": 11,
      "source": 4,
      "target": 11,
      "id": 214,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 5,
      "endNode": 11,
      "source": 5,
      "target": 11,
      "id": 215,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 6,
      "endNode": 11,
      "source": 6,
      "target": 11,
      "id": 216,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 7,
      "endNode": 11,
      "source": 7,
      "target": 11,
      "id": 217,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 3,
      "endNode": 12,
      "source": 3,
      "target": 12,
      "id": 218,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 4,
      "endNode": 12,
      "source": 4,
      "target": 12,
      "id": 219,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 5,
      "endNode": 12,
      "source": 5,
      "target": 12,
      "id": 220,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
  ],
  'center_id': 1
};
let ok_edge = [
  {
    "startNode": 2,
    "endNode": 8,
    "source": 2,
    "target": 8,
    "id": 301,
    "type": "rel",
    "properties": {
      "status": "Ok"
    },
    "linknum": "1",
    "showName": "Ok"
  },
  {
    "startNode": 3,
    "endNode": 8,
    "source": 3,
    "target": 8,
    "id": 302,
    "type": "rel",
    "properties": {
      "status": "NG"
    },
    "linknum": "1",
    "showName": "NG"
  },
  {
    "startNode": 4,
    "endNode": 8,
    "source": 4,
    "target": 8,
    "id": 303,
    "type": "rel",
    "properties": {
      "status": "Ok"
    },
    "linknum": "1",
    "showName": "Ok"
  },
  {
    "startNode": 4,
    "endNode": 9,
    "source": 4,
    "target": 9,
    "id": 304,
    "type": "rel",
    "properties": {
      "status": "Ok"
    },
    "linknum": "1",
    "showName": "Ok"
  },
  {
    "startNode": 5,
    "endNode": 9,
    "source": 5,
    "target": 9,
    "id": 305,
    "type": "rel",
    "properties": {
      "status": "Ok"
    },
    "linknum": "1",
    "showName": "Ok"
  },
  {
    "startNode": 6,
    "endNode": 9,
    "source": 6,
    "target": 9,
    "id": 306,
    "type": "rel",
    "properties": {
      "status": "Ok"
    },
    "linknum": "1",
    "showName": "Ok"
  },
  {
    "startNode": 2,
    "endNode": 12,
    "source": 2,
    "target": 12,
    "id": 315,
    "type": "rel",
    "properties": {
      "status": "Ok"
    },
    "linknum": "1",
    "showName": "Ok"
  },
  {
    "startNode": 7,
    "endNode": 12,
    "source": 7,
    "target": 12,
    "id": 316,
    "type": "rel",
    "properties": {
      "status": "Ok"
    },
    "linknum": "1",
    "showName": "Ok"
  },
];
let new_graph_data = {
  "nodes": [
    {
      "labels": [
        "Check"
      ],
      "id": 1,
      "properties": {
        "name": "BMS.ReadMaxTemperature",
        "table": 'W3_08',
        "color": "RGB(225, 0, 0)"
      },
      "showName": "BMS.ReadMaxTemperature"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 2,
      "properties": {
        "name": "Car 25",
      },
      "showName": "Car 25"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 3,
      "properties": {
        "name": "Car 115",
      },
      "showName": "Car 115"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 4,
      "properties": {
        "name": "Car 149",
      },
      "showName": "Car 149"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 5,
      "properties": {
        "name": "Car 193",
      },
      "showName": "Car 193"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 6,
      "properties": {
        "name": "Car 232",
      },
      "showName": "Car 232"
    },
    {
      "labels": [
        "Car"
      ],
      "id": 7,
      "properties": {
        "name": "Car 237",
      },
      "showName": "Car 237"
    },
    {
      "labels": [
        "PreCheck"
      ],
      "id": 8,
      "properties": {
        "name": "BMS.ReadMinTemperature",
        'table': "W3_07",
        'score': 0.527,
        "color": "RGB(225, 128, 128)"
      },
      "showName": "BMS.ReadMinTemperature"
    },
    {
      "labels": [
        "PreCheck"
      ],
      "id": 9,
      "properties": {
        "name": "PEU",
        'table': "W3_05",
        'score': 0.480,
        "color": "RGB(225, 150, 150)"
      },
      "showName": "PEU"
    },
    // {
    //   "labels": [
    //     "PreCheck"
    //   ],
    //   "id": 10,
    //   "properties": {
    //     "name": "BCM.BATT12VSOCRead",
    //     'table': "W3_07"
    //   },
    //   "showName": "BCM.BATT12VSOCRead"
    // },
    {
      "labels": [
        "PreCheck"
      ],
      "id": 11,
      "properties": {
        "name": "BMS.ReadMaxTemperature",
        'table': "W3_07",
        'score': 0.458,
        'color': "RGB(255, 160, 160)"
      },
      "showName": "BMS.ReadMaxTemperature"
    },
    {
      "labels": [
        "PreCheck"
      ],
      "id": 12,
      "properties": {
        "name": "PTC",
        'table': "W3_05",
        'score': 0.456,
        'color': "RGB(255, 165, 165)"
      },
      "showName": "PTC"
    },
  ],
  "relationships": [
    {
      "startNode": 1,
      "endNode": 2,
      "source": 1,
      "target": 2,
      "id": 201,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 3,
      "source": 1,
      "target": 3,
      "id": 202,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 4,
      "source": 1,
      "target": 4,
      "id": 203,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 5,
      "source": 1,
      "target": 5,
      "id": 204,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 6,
      "source": 1,
      "target": 6,
      "id": 205,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 1,
      "endNode": 7,
      "source": 1,
      "target": 7,
      "id": 206,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 5,
      "endNode": 8,
      "source": 5,
      "target": 8,
      "id": 207,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 6,
      "endNode": 8,
      "source": 6,
      "target": 8,
      "id": 208,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 2,
      "endNode": 9,
      "source": 2,
      "target": 9,
      "id": 209,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 3,
      "endNode": 9,
      "source": 3,
      "target": 9,
      "id": 210,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 7,
      "endNode": 9,
      "source": 7,
      "target": 9,
      "id": 211,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 2,
      "endNode": 11,
      "source": 2,
      "target": 11,
      "id": 212,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 3,
      "endNode": 11,
      "source": 3,
      "target": 11,
      "id": 213,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 4,
      "endNode": 11,
      "source": 4,
      "target": 11,
      "id": 214,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 5,
      "endNode": 11,
      "source": 5,
      "target": 11,
      "id": 215,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 6,
      "endNode": 11,
      "source": 6,
      "target": 11,
      "id": 216,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 7,
      "endNode": 11,
      "source": 7,
      "target": 11,
      "id": 217,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 3,
      "endNode": 12,
      "source": 3,
      "target": 12,
      "id": 218,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 4,
      "endNode": 12,
      "source": 4,
      "target": 12,
      "id": 219,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
    {
      "startNode": 5,
      "endNode": 12,
      "source": 5,
      "target": 12,
      "id": 220,
      "type": "rel",
      "properties": {
        "status": "NG"
      },
      "linknum": "1",
      "showName": "NG"
    },
  ],
  'center_id': 1
};
for (let i in ok_edge) {
  new_graph_data.relationships.push(ok_edge[i]);
}
// new_graph_data['relationships'] = graph_data['relationships'].concat(ok_edge);
let select_mode = false;
let exist_relations = [];
export default {
  data() {
    return {
      showOk: false,
      selectedNode: 'BMS.ReadMaxTemperature',
      selectedNodeId: 2009911,
      testItem: "BMS.ReadMaxTemperature",
      time_range: [new Date(2018, 0, 1, 0, 0), new Date(2020, 11, 31, 23, 59)],
      select_mode_val: false,
      setParametersVisible: false,
      parameters: {
        support: 0.01,
        conf: 0.1,
        min_item_num: 2,
        step: 1,
        window: 2
      },
      formLabelWidth: "110px"
    };
  },
  mounted() {
    this.load_and_show();
  },
  methods: {
    load_and_show() {
      if (this.showOk) {
        // let new_graph_data = JSON.parse(JSON.stringify(graph_data));
        // new_graph_data['relationships'] = graph_data['relationships'].concat(ok_edge);
        // console.log("新图");
        // console.log(new_graph_data);
        show_data(new_graph_data);
      } else {
        show_data(graph_data);
      }
    },
    switch_change_select_mode() {
      console.log("change");
      select_mode = !select_mode;
      neo4jd3Instance.change_select_mode(select_mode);
    },
    btn_clear_relationship() {
      show_data(graph_data);
      exist_relations = [];
      this.select_mode_val = false;
      select_mode = false;
      neo4jd3Instance.change_select_mode(false);
    },
    btn_search_relationship() {
      let module2search = neo4jd3Instance.get_select_info();
      if (module2search.length === 0) {
        return;
      }
      console.log(module2search);
      console.log(this.time_range[0].getTime(), this.time_range[1].getTime());
      let new_relationships = [];
      let edge_count = 0;
      for (let i = 0; i < module2search.length; i++) {
        for (let j = i + 1; j < module2search.length; j++) {
          if (Math.random() > 0.5) {
            continue;
          }
          let id_i = module_id_map[module2search[i]];
          let id_j = module_id_map[module2search[j]];
          if (exist_relations.indexOf(id_i + "#" + id_j) > -1) {
            console.log(id_i + "#" + id_j, "跳过");
            continue;
          }
          edge_count += 1;
          exist_relations.push(id_i + "#" + id_j);
          console.log(exist_relations);
          new_relationships.push({
            startNode: id_i,
            endNode: id_j,
            source: id_i,
            target: id_j,
            id: rel_id,
            type: "rel",
            properties: {},
            linknum: "1",
            showName: Math.round(Math.random() * 1000) / 1000
          });
          rel_id++;
        }
      }
      if (edge_count === 0) {
        this.$message('无边新增！');
      }
      neo4jd3Instance.updateWithD3Data({
        nodes: [],
        relationships: new_relationships
      });
      this.select_mode_val = false;
      select_mode = false;
      console.log("change");
      neo4jd3Instance.change_select_mode(false);
    },
    btn_set_parameters() {
      this.setParametersVisible = true;
    }
  }
};
</script>
