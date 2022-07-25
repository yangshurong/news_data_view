<template>
  <div class="h-3">
    <div ref="myEchart" style="width: 20.5167rem; height: 13.4667rem"></div>
    <div class="time_content">
      <div class="Timeline">
        <div class="timeaxis">
          <div v-for="(item, i) in list" :key="i">
            <div class="timeaxis-box">
              <div
                class="timeaxis-topText"
                :class="{ 'bd-empty': i == list.length - 1 }"
              ></div>
              <div
                class="circular"
                @click="time_change(item, i)"
                :class="{ circular_click: item.clicked }"
              ></div>
              <div class="timeaxis-bootomText">
                <div class="text">{{ item.standard }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import china from "../assets/map/china.json";
import speed_average_data from "../assets/Sheng/item_data/speed_average.json";
import main_tooltip from "../assets/main_time/main_tooltip.json";
export default {
  props: {
    title_change: {
      type: String,
      default: "政治",
    },
  },
  watch: {
    title_change(new_val, old_val) {
      this.cur_info.title = new_val;
      this.set_china_map();
    },
    hookTooltip: {
      handler(new_val, old_val) {
        //console.log(new_val, old_val, "---------watch");
        let tooltipButton = document.querySelectorAll("#main_tooltip_click");
        // 通过addEventListener注册事件
        for (let i = 0; i < tooltipButton.length; i++) {
          tooltipButton[i].addEventListener("click", this.go_next_page);
        }
      },
    },
  },
  data() {
    return {
      cur_info: {
        year: "2017",
        title: "政治",
        max: 0,
        region: "",
      },
      list: [
        {
          clicked: true,
          standard: "2017",
        },
        {
          clicked: false,
          standard: "2018",
        },
        {
          clicked: false,
          standard: "2019",
        },
        {
          clicked: false,
          standard: "2020",
        },
        {
          clicked: false,
          standard: "2021",
        },
      ],
      hookTooltip: {},
    };
  },
  methods: {
    // 随机函数
    randomValue() {
      return Math.round(Math.random() * 1000);
    },
    time_change(x, id) {
      this.cur_info.year = x.standard;
      for (let i in this.list) {
        this.list[i].clicked = false;
      }
      this.list[id].clicked = true;
      this.set_china_map();
    },
    go_next_page() {
      console.log(this.cur_info.region);
      this.$router.push({
        name: "ShengView",
        query: {
          region: this.cur_info.region,
        },
      });
    },
    async set_china_map() {
      if (!this.myChart) {
        this.myChart = this.$echarts.init(this.$refs.myEchart);
      }
      this.layoutSize = "150%";
      let that = this;
      let _data = china.features,
        scar_data = [];
      for (let i in _data) {
        let x = _data[i].properties.cp[0],
          y = _data[i].properties.cp[1],
          z = _data[i].properties.name;
        scar_data.push([x, y, z]);
      }
      for (let name_l in speed_average_data["scar"]) {
        let cur = speed_average_data["scar"][name_l];
        if (this.cur_info.title in cur == false) continue;

        let t = parseInt(this.cur_info.year) - 2017;
        if (t in cur[this.cur_info.title] == false) continue;
        this.cur_info.max = Math.max(
          this.cur_info.max,
          cur[this.cur_info.title][t][1]
        );
      }
      if (this.cur_info.max == 0) this.cur_info.max = 1;
      let options = {
        tooltip: {
          triggerOn: "click",
          enterable: true,
          confine: true,
          backgroundColor: "rgba(255,255,255,0)",
          borderColor: "rgba(0,0,0,0)",
          formatter: function (params) {
            that.hookTooltip = params;
            const default_style = `
            <div
            style="
            width: 1.6667rem;
            height:.5rem;
            font-size:.4667rem;            
            color:rgba(255,255,255)">
            还没拿到该省此年份的数据呢</div>
            `;
            if (params.name in main_tooltip == false) return default_style;
            if (that.cur_info.year in main_tooltip[params.name] == false)
              return default_style;
            let regionName = "";

            if (that.region_info_interval)
              clearInterval(that.region_info_interval);
            that.region_info_interval = setInterval(function () {
              if (document.getElementById("main_page_map_tooltip")) {
                if (params.name !== regionName) {
                  regionName = params.name;
                  that.cur_info.region = regionName;
                  if (that.toolChart) {
                    that.toolChart.dispose();
                    that.toolChart = null;
                  }
                  that.toolChart = that.$echarts.init(
                    document.getElementById("main_page_map_tooltip")
                  );
                  let nowClientWidth = document.documentElement.clientWidth;
                  //换算方法;
                  let nowSize = function nowSize(val, initWidth = 1920) {
                    return val * (nowClientWidth / initWidth);
                  };
                  const treemapOption = {
                    series: [
                      {
                        type: "treemap",
                        id: "echarts-package-size",
                        animationDurationUpdate: 1000,
                        roam: false,
                        nodeClick: undefined,
                        data: main_tooltip[regionName][that.cur_info.year],
                        universalTransition: true,
                        label: {
                          show: true,
                          fontSize: nowSize(24),
                        },
                        breadcrumb: {
                          show: false,
                        },
                      },
                    ],
                  };
                  const sunburstOption = {
                    series: [
                      {
                        type: "sunburst",
                        id: "echarts-package-size",
                        radius: ["10%", "90%"],
                        animationDurationUpdate: 1000,
                        nodeClick: undefined,
                        data: main_tooltip[regionName][that.cur_info.year],
                        universalTransition: true,
                        itemStyle: {
                          borderWidth: nowSize(1),
                          borderColor: "rgba(255,255,255,.5)",
                        },
                        label: {
                          show: true,
                          fontSize: nowSize(14),
                          color: "rgba(255,255,255)",
                        },
                      },
                    ],
                  };
                  let currentOption = treemapOption;
                  that.toolChart.setOption(currentOption);
                  clearInterval(that.toolChart_interval);
                  that.toolChart_interval = setInterval(function () {
                    currentOption =
                      currentOption === treemapOption
                        ? sunburstOption
                        : treemapOption;
                    that.toolChart.setOption(currentOption);
                  }, 3000);
                  that.toolChart.on("mouseover", function () {
                    clearInterval(that.toolChart_interval);
                  });
                  that.toolChart.on("mouseout", function () {
                    that.toolChart_interval = setInterval(function () {
                      currentOption =
                        currentOption === treemapOption
                          ? sunburstOption
                          : treemapOption;
                      that.toolChart.setOption(currentOption);
                    }, 3000);
                  });
                }
              }
            }, 500);
            return `
            <div class="main_tooltip">
              <div class="up_span">

              </div>
              <div id="main_page_map_tooltip" class="chart">

              </div>
              
              <div class="bottom_route">
                <div class="text">
                查看该省详细信息
                </div>
                <div id="main_tooltip_click" class="icon">

                </div>
              </div>
            </div>
            `;
          }, //数据格式化
        },

        geo: {
          map: "china",
          aspectScale: 1,
          layoutCenter: ["50%", "50%"], //地图位置
          layoutSize: this.layoutSize,
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
              shadowColor: "#276fce",
              shadowOffsetX: 0,
              shadowOffsetY: 15,
              opacity: 0.5,
            },
            emphasis: {
              areaColor: "#276fce",
            },
          },
        },
        series: [
          // 常规地图
          {
            type: "map",
            mapType: "china",
            aspectScale: 1,
            layoutCenter: ["50%", "50%"], //地图位置
            layoutSize: this.layoutSize,
            zoom: 1, //当前视角的缩放比例
            // roam: true, //是否开启平游或缩放
            scaleLimit: {
              //滚轮缩放的极限控制
              min: 1,
              max: 2,
            },
            label: {
              normal: {
                show: true,
                textStyle: {
                  color: "#FFFFFF",
                  fontSize: 18,
                },
                offset: [0, -20],
              },
              emphasis: {
                show: true,
                textStyle: {
                  color: "#FFFFFF",
                  fontSize: 18,
                },
                offset: [0, -20],
              },
            },
            itemStyle: {
              normal: {
                areaColor: "#0c274b",
                borderColor: "#1cccff",
                borderWidth: 1.5,
              },

              emphasis: {
                areaColor: "#02102b",
              },
            },
          },
          {
            show: true,
            type: "effectScatter",
            symbolSize: function (params) {
              //
              let t = parseInt(that.cur_info.year) - 2017;
              if (params[2] in speed_average_data["scar"] == false) return 0;
              if (
                that.cur_info.title in speed_average_data["scar"][params[2]] ==
                false
              )
                return 0;
              if (
                t in
                  speed_average_data["scar"][params[2]][that.cur_info.title] ==
                false
              )
                return 0;
              let x =
                speed_average_data["scar"][params[2]][that.cur_info.title][t];
              let cur_v = (x[1] / that.cur_info.max) * 5 + 1;
              //设置每个点的大小
              return 30 / cur_v;
            },
            rippleEffect: {
              // 涟漪特效相关配置。
              scale: 4, // 控制涟漪大小
            },
            coordinateSystem: "geo", // series坐标系类型
            data: scar_data,
          },
        ],
      };
      that.myChart.setOption(options);
    },
    screenAdapter() {
      let that = this;
      //当前视口宽度
      setTimeout(function () {
        if (that.myChart) {
          let nowClientWidth = document.documentElement.clientWidth;
          let nowSize = function nowSize(val, initWidth = 1920) {
            return val * (nowClientWidth / initWidth);
          };

          let options = {
            geo: {
              itemStyle: {
                normal: {
                  shadowOffsetY: nowSize(15),
                },
              },
            },
            series: [
              // 常规地图
              {
                label: {
                  normal: {
                    textStyle: {
                      fontSize: nowSize(18),
                    },
                    offset: [0, nowSize(-20)],
                  },
                  emphasis: {
                    textStyle: {
                      fontSize: nowSize(18),
                    },
                    offset: [0, nowSize(-20)],
                  },
                },
                itemStyle: {
                  normal: {
                    borderWidth: nowSize(1.5),
                  },
                },
              },
              {
                show: true,
                type: "effectScatter",
                symbolSize: function (params) {
                  //
                  let t = parseInt(that.cur_info.year) - 2017;
                  if (params[2] in speed_average_data["scar"] == false)
                    return 0;
                  if (
                    that.cur_info.title in
                      speed_average_data["scar"][params[2]] ==
                    false
                  )
                    return 0;
                  if (
                    t in
                      speed_average_data["scar"][params[2]][
                        that.cur_info.title
                      ] ==
                    false
                  )
                    return 0;
                  let x =
                    speed_average_data["scar"][params[2]][that.cur_info.title][
                      t
                    ];
                  let cur_v = (x[1] / that.cur_info.max) * 5 + 1;
                  let nowClientWidth = document.documentElement.clientWidth;
                  let nowSize = function nowSize(val, initWidth = 1920) {
                    return val * (nowClientWidth / initWidth);
                  };
                  //设置每个点的大小
                  return nowSize(30) / cur_v;
                },
                rippleEffect: {
                  // 涟漪特效相关配置。
                  scale: nowSize(4), // 控制涟漪大小
                },
              },
            ],
          };
          that.myChart.setOption(options);
          that.myChart.resize();
        }
      }, 300);
    },
  },
  mounted() {
    this.$echarts.registerMap("china", china);
    this.set_china_map();
    window.addEventListener("resize", this.screenAdapter);
  },
  beforeDestroy() {
    if (this.myChart) {
      this.myChart.dispose();
      this.myChart = null;
    }
    if (this.toolChart) {
      this.toolChart.dispose();
      this.toolChart = null;
    }
    if (this.region_info_interval) clearInterval(this.region_info_interval);
    if (this.toolChart_interval) clearInterval(this.toolChart_interval);
    window.removeEventListener("resize", this.screenAdapter);
  },
};
// 基于准备好的dom，初始化echarts实例
</script>
<style lang="less">
/*懒加载图标动画*/
.main_tooltip {
  width: 16.8rem;
  height: 10.9333rem;
  background: url(../assets/main_time/main_tooltip.png) no-repeat;
  background-size: 100% 100%;
  // background-position: center top;
  // display: flex;
  // flex-flow: column;
  .up_span {
    padding-top: 1.1667rem;
    padding-right: 0.3333rem;
    font-size: 0.5rem;
  }
  .bottom_route {
    display: flex;
    margin-left: 10.8333rem;
    margin-top: -0.8333rem;
    float: right;
    .icon {
      background: url(../assets/main_time/ze-arrow.png) no-repeat;
      background-size: 100% 100%;
      width: 0.4rem;
      height: 0.4rem;
      z-index: 999999;
    }
    .text {
      //margin-top: -1.6667rem;
      padding-right: 0.3333rem;
      font-size: 0.5rem;
      color: white;
      text-align: right;
      vertical-align: middle;
    }
  }

  .chart {
    width: 100%;
    height: 9.7666rem;
    justify-content: center;
  }
}
.h-3 {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-flow: column;
  .time_content {
    width: 20.5167rem;
    height: 0rem;
    font-size: 0.3333rem;
    z-index: 999999;
    .Timeline {
      width: 100%;
      height: 100%;
      margin-top: 0.6667rem;
      .timeaxis {
        height: 0.8333rem;
        margin-top: 1.3333rem;
        margin-left: 4em;
        display: flex;
        .timeaxis-box {
          width: 5.5rem;
          .circular {
            width: 0.3333rem;
            height: 0.3333rem;
            border-radius: 50%;
            background: #165dff;
            //margin-bottom: -0.1667rem;
            position: relative;
            top: -0.1667rem;
            box-shadow: 0rem 0rem 0.0833rem 0.0833rem #fff;
          }
          .circular:hover {
            width: 0.5rem;
            height: 0.5rem;
            border-radius: 50%;
            background: #ff1616;
            //margin-bottom: -0.1667rem;
            position: relative;
            top: -0.25rem;
            left: -0.0833rem;
            box-shadow: 0rem 0rem 0.0833rem 0.0833rem #fff;
          }
          .circular_click {
            width: 0.5rem;
            height: 0.5rem;
            border-radius: 50%;
            background: #ff1616;
            //margin-bottom: -0.1667rem;
            position: relative;
            top: -0.25rem;
            left: -0.0833rem;
            box-shadow: 0rem 0rem 0.0833rem 0.0833rem #fff;
          }
          .timeaxis-topText {
            border-bottom: 0.0833rem solid #c9cdd4; //时间轴线的宽度和颜色
            position: relative;
          }
          .bd-empty {
            // border: 0;
            //margin-top: .0833rem;
            border-bottom: 0.0833rem solid #c9cdd4; //时间轴线的宽度和颜色
            opacity: 0;
            position: relative;
          }
          .timeaxis-bootomText {
            position: relative;
            .text {
              position: absolute;
              top: 0.1667rem;
              font-size: 0.4667rem;
              left: -0.3333rem;
              color: #fff;
            }
          }
        }
      }
    }
  }
}
</style>