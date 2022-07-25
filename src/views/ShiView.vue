<template>
  <div class="ShiBackground">
    <div class="title"></div>
    <div class="content">
      <div class="policy_content">
        <div style="height: 103px; width: 100%"></div>
        <div v-for="(item, i) in policy_content_list" :key="i">
          <div class="policy_item">
            <div class="policy_picture"></div>
            <div class="policy_right_content">
              <div class="policy_title">{{item.title}}</div>
              <div class="policy_text">{{item.content}}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="news_content">
        <div class="map_chart">
          <div
            ref="region"
            style="width: 100%; height: 100%; margin-left: 0rem"
          ></div>
        </div>
        <div class="time">
          <div style="font-size: 0.3rem; color: #ffffff; margin-bottom: 0rem">
            2017
          </div>
          <el-slider
            v-model="time_select_value"
            :max="2021"
            :min="2017"
            @change="get_time_change"
            :step="1"
            class="time_select"
          >
          </el-slider>

          <div style="font-size: 0.3rem; color: #ffffff; margin-top: 0rem">
            2021
          </div>
        </div>
        <div class="mind">
          <div
            ref="mind"
            style="width: 100%; height: 100%; margin-left: 0rem"
          ></div>
        </div>
      </div>
      <div class="right">
        <div class="tag_num">
          <div
            ref="tag_num"
            style="
              width: 100%;
              height: 100%;
              margin-left: 0rem;
              margin-top: 0.5rem;
            "
          ></div>
        </div>
        <div class="wordCloud">
          <svg
            :width="nowSize(width)"
            :height="nowSize(height)"
            style="margin-top: 0.5rem"
          >
            <a
              class="fontA"
              :style="{ fill: tag.color, 'font-weight': 'bold' }"
              v-for="(tag, index) in tags"
              :key="`tag-${index}`"
            >
              <text
                :id="tag.id"
                :x="nowSize(tag.x)"
                :y="nowSize(tag.y)"
                :font-size="
                  nowSize(18) * (nowSize(600) / (nowSize(600) - nowSize(tag.z)))
                "
                :fill-opacity="(nowSize(400) + nowSize(tag.z)) / nowSize(400)"
                @mousemove="listenerMove($event)"
                @mouseout="listenerOut($event)"
                @click="clickToPage"
              >
                {{ tag.text }}
              </text>
            </a>
          </svg>
        </div>
        <div class="rank_speed">
          <div style="width: 100%; height: 0.8333rem"></div>
          <div class="speed_content">
            <div v-for="(item, i) in rank_speed_list" :key="i">
              <div class="list_item" :class="{ as_first: i == 0 }">
                <div class="item_rank">{{ item.rank }}</div>
                <div
                  class="item_title"
                  :class="{ item_title_content: i !== 0 }"
                >
                  {{ item.title }}
                </div>
                <div class="item_speed">{{ item.speed }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import test_mind_data from "../assets/Shi/test_mind_data.json";
import word_cloud_data from "../assets/Sheng/item_data/word_cloud_3ddata.json";
import speed_data from "../assets/Shi/speed_data.json";
export default {
  data() {
    return {
      cur_info: {
        year: "2017",
        title: "政治",
        region: "阳泉",
        region_data: "",
      },
      locate_data_url: {
        晋中: "jinzhong.json",
        吕梁: "lvliang.json",
        朔州: "shuozhou.json",
        太原: "taiyuan.json",
        阳泉: "yangquan.json",
      },
      news_value: 0,
      news_list: [
        {
          url: "http://www.gov.cn/xinwen/2022-05/01/5688367/images/874baddfbc4c43809aae929bf2a190a2.JPG",
        },
        {
          url: "http://www.gov.cn/xinwen/2022-05/01/5688367/images/441dbcc82f714ce58365ab925ac4c783.JPG",
        },
        {
          url: "http://www.gov.cn/xinwen/2022-05/01/5688367/images/89106ba8a3a6455e8d323ba63e307cf0.JPG",
        },
      ],
      time_select_value: 0,
      rank_speed_list: [
        {
          rank: "排名",
          title: "主题",
          speed: "响应时间",
        },
        {
          rank: 1,
          title: "政治",
          speed: 0.2,
        },
        {
          rank: "2",
          title: "民生",
          speed: 1.9,
        },
      ],
      policy_content_list: [
        {
          title:'金融支持文化旅游产业纾困发展',
          content:'5月13日，太原市金融支持文化旅游产业纾困发展政银企对接会召开，副市长高德胜出席并讲话。'
        },
        {
          title:'坚持正确舆论导向 发挥网媒宣传优势',
          content:'5月13日，全市网络正能量宣传暨互联网行业党建工作会召开，全面总结去年工作，部署今年重点任务。市委常委、宣传部部长杨继承出席并讲话。 '
        },
        {
          title:'市委召开今年第二次党外代表人士座谈会',
          content:'5月12日，市委召开2022年度第二次党外代表人士座谈会，通报太忻经济一体化发展太原区建设情况并征求意见建议。'
        },
        {
          title:'春植改秋植 市民可申请退款',
          content:'5月13日，记者从市园林局获悉，受疫情影响，原定于4月16日至17日开展的2022年群众纪念林植树活动，经两次延期后最终决定暂时取消，待金秋十月再择时开展。'
        },
        {
          title:'清仓见底促增收 固本强基谋发展',
          content:'5月11日，市委副书记、政法委书记张韬在娄烦县调研壮大村集体经济和农村集体资产“清化收”工作，并召开座谈会。副市长程永平参加。 '
        },
        {
          title:'唱响乡村振兴曲 走进古交市岔口乡关头村',
          content:'晋绥八分区是抗日战争时期晋西北的南大门，是通往延安、晋察冀、晋冀鲁豫、华东、华中等抗日根据地的交通要道。'
        },
      ],
      orgin_dataAxis: ["政治", "经济", "资源", "生产", "文化", "民生"],
      width: 576,
      height: 300,
      tagsNum: 0, //标签数量
      RADIUS: 110, //球的半径
      speedX: Math.PI / 360 / 0.5, //球一帧绕x轴旋转的角度
      speedY: Math.PI / 360 / 0.5, //球-帧绕y轴旋转的角度
      tags: [],
      data: word_cloud_data["value"],
      timer: null,
    };
  },
  created() {
    this.initData();
    this.cur_info.region = this.$route.query.region;
  },
  mounted() {
    this.set_region_map();
    this.set_policy_detail();
    this.set_num_tag();
    this.set_rank_list();
    window.addEventListener("resize", this.screenAdapter);
    this.screenAdapter();
  },
  methods: {
    get_time_change(new_time) {
      //时间变化后
      //console.log(new_time.toString());
      new_time = new_time.toString();
      if (new_time in speed_data[this.cur_info.region] == false) {
        alert("这里没有数据");
        return;
      }
      this.cur_info.year = new_time;
      this.set_num_tag();
      this.set_rank_list();
      this.screenAdapter();
      //this.cur_info.year = new_time.toString();
      //this.set_num_tag();
      //this.set_speed_tag();
    },
    async set_region_map() {
      // await this.$axios({
      //   url: "https://geo.datav.aliyun.com/areas_v3/bound/370200_full.json",
      //   method: "get",
      // }).then((res) => {
      // });
      // this.cur_info.region_data = res.data;
      this.cur_info.region_data = require("../assets/Shi/map/" +
        this.locate_data_url[this.cur_info.region]);
      this.$echarts.registerMap(
        this.cur_info.region,
        this.cur_info.region_data
      );
      let _data = this.cur_info.region_data.features,
        scar_data = [];
      for (let i in _data) {
        let x = _data[i].properties.center[0],
          y = _data[i].properties.center[1],
          z = _data[i].properties.name;
        scar_data.push([x, y, z]);
      }
      this.speed_region_Chart = this.$echarts.init(this.$refs.region);
      let layoutSize = "600",
        aspectScale = 687 / 415;
      let speed_region_option = {
        geo: {
          map: this.cur_info.region,
          z: 2,
          aspectScale: 1,
          layoutCenter: ["50%", "50%"], //地图位置
          //layoutSize: layoutSize,
          zoom: 1, //当前视角的缩放比例
          scaleLimit: {
            //滚轮缩放的极限控制
            min: 1,
            max: 2,
          },
          label: {
            normal: {
              show: false,
              textStyle: {
                color: "#FFFFFF",
                fontSize: 18,
              },
            },
            emphasis: {
              show: false,
              textStyle: {
                color: "#FFFFFF",
                fontSize: 18,
              },
            },
          },
          itemStyle: {
            normal: {
              shadowColor: "rgba(21,55,112,255)",
              shadowOffsetX: 10,
              shadowOffsetY: 10,
              areaColor: "rgba(24,48,82,255)",
              borderColor: "rgba(84,113,166)",
              borderWidth: 1.5,
            },
            emphasis: {
              areaColor: "rgba(7,69,162)",
            },
          },
        },

        series: [
          {
            type: "map",
            mapType: this.cur_info.region,
            aspectScale: 1,
            zoom: 1,
            //layoutSize: layoutSize,
            z: 1,
            layoutCenter: ["50%", "50%"], //地图位置
            label: {
              normal: {
                show: false,
              },
              emphasis: {
                show: false,
              },
            },
            itemStyle: {
              normal: {
                shadowColor: "rgba(22,57,89,255)",
                shadowOffsetX: 20,
                shadowOffsetY: 20,
                //areaColor: "rgba(22,57,89,255)",
                borderColor: "#4a75ff",
                borderWidth: 7,
              },
              emphasis: {
                areaColor: "rgba(22,57,89,0)",
              },
            },
          },
        ],
      };
      this.speed_region_Chart.setOption(speed_region_option);
    },
    async set_policy_detail() {
      let option = {
        tooltip: {
          trigger: "item",
          triggerOn: "mousemove",
        },
        series: [
          {
            type: "tree",
            data: [test_mind_data],
            top: "1%",
            left: "7%",
            bottom: "1%",
            right: "20%",
            symbolSize: 10,
            label: {
              position: "left",
              verticalAlign: "middle",
              align: "right",
              fontSize: 10,
              color: "#FFFFFF",
            },
            leaves: {
              label: {
                position: "right",
                verticalAlign: "middle",
                align: "left",
              },
            },
            emphasis: {
              focus: "ancestor",
            },
            expandAndCollapse: true,
            animationDuration: 550,
            animationDurationUpdate: 750,
          },
        ],
      };
      this.detail_chart = this.$echarts.init(this.$refs.mind);
      this.detail_chart.setOption(option);
    },
    async set_num_tag() {
      // prettier-ignore
      let dataAxis = [];
      let data = [];
      for (let i in this.orgin_dataAxis) {
        if (
          this.orgin_dataAxis[i] in
            speed_data[this.cur_info.region][this.cur_info.year] ==
          false
        )
          continue;
        dataAxis.push(this.orgin_dataAxis[i]);
        data.push(
          speed_data[this.cur_info.region][this.cur_info.year][
            this.orgin_dataAxis[i]
          ]["num"]
        );
      }
      // prettier-ignore
      let yMax = 500;
      let dataShadow = [];
      for (let i = 0; i < data.length; i++) {
        dataShadow.push(yMax);
      }
      let echarts = this.$echarts;
      let option = {
        xAxis: {
          name: "主题",
          data: dataAxis,
          axisLabel: {
            inside: true,
            color: "#FFFFFF",
          },
          axisTick: {
            show: false,
          },
          axisLine: {
            show: false,
          },
          nameTextStyle: {
            color: "rgba(255,255,255)",
            fontSize: 20,
          },

          z: 10,
        },
        yAxis: {
          name: "个数",
          axisLine: {
            show: false,
          },
          axisTick: {
            show: false,
          },
          nameTextStyle: {
            color: "rgba(255,255,255)",
            fontSize: 20,
          },

          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        dataZoom: [
          {
            type: "inside",
          },
        ],
        series: [
          {
            type: "bar",
            showBackground: true,
            itemStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: "#83bff6" },
                { offset: 0.5, color: "#188df0" },
                { offset: 1, color: "#188df0" },
              ]),
            },
            emphasis: {
              itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: "#2378f7" },
                  { offset: 0.7, color: "#2378f7" },
                  { offset: 1, color: "#83bff6" },
                ]),
              },
            },
            data: data,
          },
        ],
      };
      // Enable data zoom when user click bar.
      const zoomSize = 3;
      this.num_tag_chart = this.$echarts.init(this.$refs.tag_num);
      let that = this;
      this.num_tag_chart.on("click", function (params) {
        let h = parseInt(Math.max(params.dataIndex - zoomSize / 2, 0));
        let t = parseInt(
          Math.min(params.dataIndex + zoomSize / 2, data.length - 1)
        );
        console.log(h, t);
        that.num_tag_chart.dispatchAction({
          type: "dataZoom",
          startValue: dataAxis[h],
          endValue: dataAxis[t],
        });
      });
      this.num_tag_chart.setOption(option);
    },
    async set_rank_list() {
      let rank_speed_list = [];
      let tmp = this.rank_speed_list[0];
      this.rank_speed_list = [];
      this.rank_speed_list.push(tmp);
      let cur_data = speed_data[this.cur_info.region][this.cur_info.year];
      let rank_num = 1;
      for (let k in cur_data) {
        if(k=='avg')continue
        rank_speed_list.push({
          rank: 0,
          title: k,
          speed: Math.floor(cur_data[k]["avg"] * 100) / 100 ,
          
        });
      }
      rank_speed_list = rank_speed_list.sort((a, b) => {
        return a.speed - b.speed;
      });
      for (let i in rank_speed_list) {
        rank_speed_list[i].rank = rank_num;
        this.rank_speed_list.push(rank_speed_list[i]);
        rank_num++;
      }
    },
    screenAdapter() {
      let that = this;
      setTimeout(function () {
        if (that.detail_chart) {
          let option = {
            series: [
              {
                symbolSize: that.nowSize(10),
                label: {
                  fontSize: that.nowSize(10),
                },
              },
            ],
          };
          that.detail_chart.setOption(option);
          that.detail_chart.resize();
        }
      }, 300);
      setTimeout(function () {
        if (that.speed_region_Chart) {
          let option = {
            geo: {
              itemStyle: {
                normal: {
                  shadowOffsetX: that.nowSize(10),
                  shadowOffsetY: that.nowSize(10),
                  borderWidth: that.nowSize(1.5),
                },
              },
            },
            series: [
              {
                itemStyle: {
                  normal: {
                    shadowOffsetX: that.nowSize(20),
                    shadowOffsetY: that.nowSize(20),
                    borderWidth: that.nowSize(7),
                  },
                },
              },
            ],
          };
          that.speed_region_Chart.setOption(option);
          that.speed_region_Chart.resize();
        }
      }, 300);
      setTimeout(function () {
        if (that.num_tag_chart) {
          let option = {
            xAxis: {
              nameTextStyle: {
                fontSize: that.nowSize(20),
              },
            },
            yAxis: {
              nameTextStyle: {
                fontSize: that.nowSize(20),
              },
            },
          };
          that.num_tag_chart.setOption(option);
          that.num_tag_chart.resize();
        }
      }, 300);
    },

    initData() {
      //初始化标签位置
      let tags = [];
      this.tagsNum = this.data.length;
      for (let i = 0; i < this.data.length; i++) {
        let tag = {};
        let k = -1 + (2 * (i + 1) - 1) / this.tagsNum;
        let a = Math.acos(k);
        let b = a * Math.sqrt(this.tagsNum * Math.PI); //计算标签相对于球心的角度
        tag.text = this.data[i];
        tag.x = this.CX + this.RADIUS * Math.sin(a) * Math.cos(b); //根据标签角度求出标签的x,y,z坐标
        tag.y = this.CY + this.RADIUS * Math.sin(a) * Math.sin(b);
        tag.z = this.RADIUS * Math.cos(a);
        tag.id = i; // 给标签添加id
        tag.color =
          "rgb(" +
          [
            Math.round(Math.random() * 254),
            Math.round(Math.random() * 254),
            Math.round(Math.random() * 254),
          ].join(",") +
          ")";
        tags.push(tag);
        // console.log(tag);
      }
      this.tags = tags; //让vue替我们完成视图更新
    },
    // 纵向旋转
    rotateX(angleX) {
      var cos = Math.cos(angleX);
      var sin = Math.sin(angleX);
      for (let tag of this.tags) {
        var y1 = (tag.y - this.CY) * cos - tag.z * sin + this.CY;
        var z1 = tag.z * cos + (tag.y - this.CY) * sin;
        tag.y = y1;
        tag.z = z1;
      }
    },
    // 横向旋转
    rotateY(angleY) {
      var cos = Math.cos(angleY);
      var sin = Math.sin(angleY);
      for (let tag of this.tags) {
        var x1 = (tag.x - this.CX) * cos - tag.z * sin + this.CX;
        var z1 = tag.z * cos + (tag.x - this.CX) * sin;
        tag.x = x1;
        tag.z = z1;
      }
    },
    // 运动函数
    async runTags() {
      if (typeof this.timer === "number") {
        clearInterval(this.timer);
        this.timer = null;
      }
      let timer = setInterval(() => {
        this.rotateX(this.speedX);
        this.rotateY(this.speedY);
      }, 17);
      this.timer = timer;
    },
    // 监听移入事件
    listenerMove(e) {
      if (e.target.id) {
        clearInterval(this.timer);
      }
    },
    // 监听移出事件
    listenerOut(e) {
      if (e.target.id) {
        this.runTags();
      }
    },
    // 点击事件
    clickToPage() {},
    //up----------------------------------------------------------set word_cloud
  },
  beforeDestroy() {
    if (this.speed_region_Chart) {
      this.speed_region_Chart.dispose();
      this.speed_region_Chart = null;
    }
    if (this.detail_chart) {
      this.detail_chart.dispose();
      this.detail_chart = null;
    }
    if (this.word_cloud_Chart) {
      this.word_cloud_Chart.dispose();
      this.word_cloud_Chart = null;
    }
    if (this.num_tag_chart) {
      this.num_tag_chart.dispose();
      this.num_tag_chart = null;
    }
    window.removeEventListener("resize", this.screenAdapter);
  },
  computed: {
    CX() {
      //球心x坐标
      return this.width / 2;
    },
    CY() {
      //球心y坐标
      return this.height / 2;
    },
    nowSize() {
      return function nowSize(val, initWidth = 1920) {
        let nowClientWidth = document.documentElement.clientWidth;
        return val * (nowClientWidth / initWidth);
      };
    },
  },
};
</script>
<style lang="less">
.tag_num {
  width: 100%;
  height: 5.6667rem;
  background: url(../assets/Shi/tag_num.png) no-repeat;
  background-size: 100% 100%;
  background-position: center top;
}
.wordCloud {
  width: 100%;
  margin-top: 0.2rem;
  height: 5.0333rem;
  background: url(../assets/Shi/3dwordCloud.png) no-repeat;
  background-size: 100% 100%;
  background-position: center top;
}
.rank_speed {
  width: 100%;
  margin-top: 0.2rem;
  margin-left: 0.1rem;
  height: 5.45rem;
  background: url(../assets/Shi/rank_speed.png) no-repeat;
  background-size: 100% 100%;
  background-position: center top;
  display: flex;
  flex-flow: column;
  .speed_content {
    margin-left: 0.5333rem;
    margin-top: 0.3333rem;
    line-height: 0.3333rem;
    border-radius: 0.0833rem;
    width: 8.15rem;
    height: 3.5833rem;
    background-color: rgba(64, 183, 246, 0.2);
  }
  .list_item {
    display: flex;
    width: 8.15rem;
    margin-left: 1.4833rem;
    margin-top: 0.1667rem;
    .item_rank {
      color: rgba(255, 255, 255, 100);
      font-size: 0.3333rem;
      text-align: left;
      font-weight: bold;
      width: 1.8333rem;
      //font-family: SourceHanSansSC-regular;
    }
    .item_title {
      color: rgba(161, 158, 158, 100);
      font-size: 0.3333rem;
      width: 1.4333rem+0.5167rem;
      text-align: left;
    }
    .item_speed {
      color: rgba(161, 158, 158, 100);
      font-size: 0.3333rem;
    }
    .item_title_content {
      color: rgba(231, 0, 0);
      font-size: 0.3333rem;
      width: 1.4333rem+0.5167rem;
      text-align: left;
      font-weight: bold;
    }
  }
}
.news_content {
  .map_chart {
    width: 11.4333rem;
    height: 6.9167rem;
    margin: 1.4833rem 0 0 0.3667rem;
  }
  .time {
    width: 100%;
    height: 0.4667rem;
    margin-left: 1.3833rem;
    margin-top: 0rem;
    display: flex;
    .time_select {
      width: 8.2667rem;
      height: 0.4667rem;
      margin-top: 0.3333rem;
    }
  }
  .mind {
    width: 8.9667rem;
    height: 6.5rem;
    margin-left: 1.2833rem;
  }
  width: 12.25rem;
  height: 15.7833rem;
  margin-top: 1.9rem;
  margin-left: 0.75rem;
  background: url(../assets/Shi/news_content.png) no-repeat;
  background-size: 100% 100%;
  background-position: center top;
  display: flex;
  flex-flow: column;
}
.policy_content {
  width: 8.1167rem;
  height: 16.6167rem;
  margin-top: 0.7167rem;
  margin-left: 0.9rem;
  background: url(../assets/Shi/policy_content.png) no-repeat;
  background-size: 100% 100%;
  background-position: center top;
  .policy_item {
    width: 7.4rem;
    height: 2.1667rem;
    border-radius: .0833rem;
    background-color: rgba(64, 183, 246, 0.2);
    margin-left: .3333rem;
    margin-top: .2667rem;
    display: flex;
    .policy_picture {
      width: 1.6667rem;
      height: 1.3167rem;
      background: url(../assets/Shi/policy_icon.png) no-repeat;
      background-size: 100% 100%;
      margin-left: .3667rem;
      margin-top: .4333rem;
    }
    .policy_right_content {
      //margin-left: 2.45rem;
      display: flex;
      flex-flow: column;
      margin-left: .3667rem;
      margin-top: .35rem;
      .policy_title {
        width: 2.6333rem;
        height: .3667rem;
        color: rgba(0, 0, 0, 0.85);
        font-size: .2667rem;
        font-family: PingFangSC-regular;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .policy_text {
        width: 4.0833rem;
        height: 1.1rem;        
        overflow: hidden;
        text-overflow: ellipsis;
        color: rgba(0, 0, 0, 0.65);
        font-size: .2333rem;
        text-align: left;
        font-family: PingFangSC-regular;
      }
    }
  }
}
.right {
  margin-top: 1.15rem;
  margin-left: 0.6rem;
  width: 9.45rem;
  height: 12.9167rem+4.7833rem;
  display: flex;
  flex-flow: column;

  justify-content: flex-start;
}

.ShiBackground {
  width: 32.2667rem;
  height: 18.05rem;
  background: url(https://ysr-data-view.oss-cn-hangzhou.aliyuncs.com/C778FA422F5F4FDB8043352BFEBFDC6B-6-2.png) no-repeat fixed;
  background-size: 100% 100%;
  overflow: hidden;
  .title {
    width: 32.2667rem;
    height: 5.7167rem;
    background: url(../assets/main_page_title.png) no-repeat;
    background-size: 100% 100%;
    background-position: center top;
  }
  .content {
    margin-top: -5.7167rem;
    width: 32.2667rem;
    height: 12.3333rem;
    display: flex;
  }
}
</style>
