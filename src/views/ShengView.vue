<template>
  <div class="ShengBackground">
    <section class="item_left">
      <LeftPage @title_change="title_change" />
    </section>
    <div class="item_right">
      <div class="title"></div>
      <div class="content">
        <div class="left">
          <div class="speed_region" style="display: flex">
            <div class="time_select">
              <div
                style="
                  font-size: 0.3rem;
                  color: #ffffff;
                  margin-bottom: 0.0833rem;
                "
              >
                2021
              </div>
              <el-slider
                v-model="time_select_value"
                :max="2021"
                :min="2017"
                vertical
                @change="get_time_change"
                height="4.2rem"
                :step="1"
              >
              </el-slider>
              <div
                style="font-size: 0.3rem; color: #ffffff; margin-top: 0.1667rem"
              >
                2017
              </div>
            </div>
            <div
              class="speed_region_chart"
              ref="speed_region"
              style="width: 12.9333rem; height: 8.8333rem; margin-top: 1rem"
            ></div>
          </div>
          <div class="down">
            <div class="news">
              <Carousel
                autoplay
                v-model="news_value"
                loop
                style="width: 100%; height: 100%"
              >
                <CarouselItem v-for="(item, i) in news_list" :key="i">
                  <!-- <img
                    :src="item.url"
                    alt="加载失败"
                    width="6.7833rem"
                    height="3.4833rem"
                    style="margin: 1.4333rem 0 0 1.1667rem"
                  /> -->
                  <div
                    :style="{
                      margin: '1.4333rem 0 0 1.1667rem',
                      height: '3.4833rem',
                      width: '6.8333rem',
                      background: 'url(' + item.url + ') no-repeat',
                      'background-size': '100% 100%',
                    }"
                  ></div>
                </CarouselItem>
              </Carousel>
            </div>
            <div class="speed_average">
              <div
                ref="speed_average"
                style="width: 100%; height: 100%; margin-top: 0.5rem"
              ></div>
            </div>
          </div>
        </div>
        <div class="right">
          <div class="num_tag">
            <div
              ref="num_tag"
              style="width: 95%; height: 95%; margin-top: 0.1667rem"
            ></div>
          </div>
          <div class="word_cloud">
            <svg
              :width="nowSize(width)"
              :height="nowSize(height)"
              style="margin-top: 0.8333rem"
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
                    nowSize(20) *
                    (nowSize(600) / (nowSize(600) - nowSize(tag.z)))
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
          <div class="speed_tag">
            <div
              ref="speed_tag"
              style="width: 100%; height: 100%; margin-top: 0.5rem"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import LeftPage from "../components/MainPageLeft.vue";
import word_cloud_data from "../assets/Sheng/item_data/word_cloud_3ddata.json";
import num_tag_data from "../assets/Sheng/item_data/locate_tag_num.json";
import speed_average_data from "../assets/Sheng/item_data/speed_average.json";
import shi_speed_data from "../assets/Shi/speed_data.json";
export default {
  data() {
    return {
      cur_info: {
        year: "2017",
        title: "政治",
        region: "山西",
        region_data: "",
      },
      locate_data_url: {
        河北: "hebei.json",
        山东: "shandong.json",
        山西: "shanxi.json",
        河南: "henan.json",
        辽宁: "liaoning.json",
        安徽: "anhui.json",
        广东: "guangdong.json",
        广西: "guangxi.json",
        内蒙古: "neimenggu.json",
        新疆: "xinjiang.json",
        西藏: "xizang.json",
        吉林: "jilin.json",
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
      width: 576,
      height: 300,
      time_select_value: 0,
      tagsNum: 0, //标签数量
      RADIUS: 120, //球的半径
      speedX: Math.PI / 360 / 0.5, //球一帧绕x轴旋转的角度
      speedY: Math.PI / 360 / 0.5, //球-帧绕y轴旋转的角度
      tags: [],
      data: word_cloud_data["value"],
      timer: null,
      color_list: [
        "#4587E7",
        "#35AB33",
        "#F5AD1D",
        "#ff7f50",
        "#da70d6",
        "#32cd32",
        "#6495ed",
        "#F3FA00",
      ],
    };
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
  created() {
    this.cur_info.region = this.$route.query.region;
    this.initData();
  },
  mounted() {
    //console.log(this.$route.params.region);

    //this.set_wordcloud();
    this.runTags();
    this.set_speed_average();
    this.set_speed_tag();
    this.set_speed_region();
    this.set_num_tag();
    this.set_speed_region();
    window.addEventListener("resize", this.screenAdapter);
    this.screenAdapter();
  },
  methods: {
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

    title_change(new_title) {
      //title变化后
      this.cur_info.title = new_title;
      if (
        num_tag_data[this.cur_info.region][this.cur_info.year][
          this.cur_info.title
        ] == null
      ) {
        alert("这里没有数据");
        return;
      }
      this.set_num_tag();
      this.set_speed_tag();
      this.screenAdapter();
    },
    get_time_change(new_time) {
      if (
        num_tag_data[this.cur_info.region][this.cur_info.year][
          this.cur_info.title
        ] == null
      ) {
        alert("这里没有数据");
        return;
      }
      //时间变化后
      this.cur_info.year = new_time.toString();
      this.set_num_tag();
      this.set_speed_tag();
      this.screenAdapter();
    },
    async set_num_tag() {
      // if (!this.num_tag_Chart)
      if (this.num_tag_Chart) this.num_tag_Chart.clear();
      else this.num_tag_Chart = this.$echarts.init(this.$refs.num_tag);

      this.num_tag_Chart.setOption({
        dataset: {
          source:
            num_tag_data[this.cur_info.region][this.cur_info.year][
              this.cur_info.title
            ],
        },
        grid: { containLabel: true },
        xAxis: {
          name: "数量",
          nameTextStyle: {
            color: "rgba(255,255,255)",
          },

          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        yAxis: {
          type: "category",
          nameTextStyle: {
            color: "rgba(255,255,255)",
          },

          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        visualMap: {
          orient: "horizontal",
          left: "center",
          min: 0,
          max: 10,
          text: ["慢速响应", "快速响应"],
          // Map the score column to color
          dimension: "avg",
          inRange: {
            color: ["#65B581", "#FFCE34", "#FD665F"],
          },
          textStyle: {
            color: "#FFFFFF",
          },
        },
        series: [
          {
            type: "bar",
            encode: {
              x: "num",
              y: "sub_title",
            },
          },
        ],
      });
    },
    async set_wordcloud() {
      //-------------------------set wordcloud
      if (!this.word_cloud_Chart)
        this.word_cloud_Chart = this.$echarts.init(this.$refs.word_cloud);
      var maskImage = new Image();
      maskImage.src = word_cloud_data.image;
      this.word_cloud_Chart.setOption({
        series: [
          {
            type: "wordCloud",
            shape: "circle",
            keepAspect: false,
            left: "center",
            top: "center",
            width: "70%",
            height: "70%",
            right: null,
            bottom: null,
            //maskImage:maskImage,
            sizeRange: [12, 30],
            rotationRange: [-45, 45],
            rotationStep: 90,
            // 词间距，数值越小，间距越小，这里间距太小的话，会出现大词把小词套住的情况，比如一个大的口字，中间会有比较大的空隙，这时候他会把一些很小的字放在口字里面，这样的话，鼠标就无法选中里面的那个小字
            gridSize: 2,
            // 允许词太大的时候，超出画布的范围
            drawOutOfBound: false,
            // 布局的时候是否有动画
            layoutAnimation: false,
            textStyle: {
              fontWeight: "bold",
              color: function () {
                return (
                  "rgb(" +
                  [
                    Math.round(Math.random() * 254),
                    Math.round(Math.random() * 254),
                    Math.round(Math.random() * 254),
                  ].join(",") +
                  ")"
                );
              },
            },
            emphasis: {
              focus: "self",
              textStyle: {
                textShadowBlur: 10,
                textShadowColor: "#333",
              },
            },

            // Data is an array. Each array item must have name and value property.
            data: word_cloud_data.value,
          },
        ],
      });
    },
    async set_speed_average() {
      //--------------------set speed_average
      //-------------------------------------------------------------set scar
      if (!this.speed_average_Chart)
        this.speed_average_Chart = this.$echarts.init(this.$refs.speed_average);
      let scar_data = speed_average_data["scar"][this.cur_info.region];
      let scar_series = [],
        scar_legend = [];
      let id = 0;
      for (let title_name in scar_data) {
        scar_series.push({
          name: title_name,
          type: "line",
          id: title_name,
          dataGroupId: title_name,
          lineStyle: {
            color: this.color_list[id],
          },
          universalTransition: {
            enabled: true,
            delay: function (idx, count) {
              return Math.random() * 400;
            },
          },
          data: scar_data[title_name],
        });
        scar_legend.push({
          name: title_name,
          icon: "circle",
          itemStyle: {
            color: this.color_list[id],
          },
        });
        id++;
      }
      console.log(scar_legend);
      let speed_region_average_scatterOption = {
        legend: {
          show: true,
          data: scar_legend,
          textStyle: {
            color: "#FFFFFF",
            fontSize: 14,
          },
          left: 80,
          top: 30,
        },
        xAxis: {
          scale: true,
          name: "年份",
          nameTextStyle: {
            color: "rgba(255,255,255)",
          },

          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        yAxis: {
          scale: true,
          name: "响应时间",
          nameTextStyle: {
            color: "rgba(255,255,255)",
          },

          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        series: scar_series,
      };
      //-------------------------------------------------------设置bar
      let bar_data = speed_average_data["bar"][this.cur_info.region];
      let bar_series = [],
        bar_x_data = [];
      for (let title_name in bar_data) {
        bar_x_data.push(title_name);
        bar_series.push({
          value: bar_data[title_name],
          groupId: title_name,
        });
      }
      let bar_key = bar_x_data;
      let speed_region_average_barOption = {
        xAxis: {
          type: "category",
          data: bar_x_data,
          name: "类别",
          nameTextStyle: {
            color: "rgba(255,255,255)",
          },
          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        yAxis: {
          name: "响应时间",
          nameTextStyle: {
            color: "rgba(255,255,255)",
          },

          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        series: [
          {
            type: "bar",
            id: "total",
            data: bar_series,
            universalTransition: {
              enabled: true,
              seriesKey: bar_key,
              delay: function (idx, count) {
                return Math.random() * 400;
              },
            },
          },
        ],
      };

      let currentOption = speed_region_average_scatterOption,
        that = this;
      that.speed_average_interval = setInterval(function () {
        currentOption =
          currentOption === speed_region_average_scatterOption
            ? speed_region_average_barOption
            : speed_region_average_scatterOption;
        that.speed_average_Chart.setOption(currentOption, true);
      }, 2000);
      that.speed_average_Chart.on("mouseover", function () {
        clearInterval(that.speed_average_interval);
      });
      that.speed_average_Chart.on("mouseout", function () {
        that.speed_average_interval = setInterval(function () {
          if (currentOption === speed_region_average_scatterOption) {
            currentOption = speed_region_average_barOption;
            that.speed_average_Chart.setOption(currentOption, true);
          } else {
            currentOption = speed_region_average_scatterOption;
            that.speed_average_Chart.setOption(currentOption, true);
            let option = {
              legend: {
                textStyle: {
                  fontSize: that.nowSize(14),
                },
                left: that.nowSize(80),
                top: that.nowSize(20),
              },
            };
            that.speed_average_Chart.setOption(option);
            that.speed_average_Chart.resize();
          }
        }, 2000);
      });
    },
    async set_speed_region() {
      //--------------------set speed_region
      //await this.$axios({
      //  url: 'https://geo.datav.aliyun.com/areas_v3/bound/370000_full.json',
      //  method: "get",
      //}).then((res) => {
      //  this.cur_info.region_data = res.data;
      //});
      this.cur_info.region_data = require("../assets/map/province/" +
        this.locate_data_url[this.cur_info.region]);
      this.$echarts.registerMap(
        this.cur_info.region,
        this.cur_info.region_data
      );
      let _data = this.cur_info.region_data.features,
        scar_data = [];
      for (let i in _data) {
        let x = _data[i].properties.cp[0],
          y = _data[i].properties.cp[1],
          z = _data[i].properties.name;
        scar_data.push([x, y, z]);
      }
      //-----------------------------------------------------------处理散点的位置
      this.cur_info.mx = 0;
      if (this.cur_info.region == "山西") {
        for (let re in shi_speed_data) {
          let y = this.cur_info.year;
          if (y in shi_speed_data[re] == true) {
            console.log(shi_speed_data[re][y]["avg"]);
            this.cur_info.mx = Math.max(
              this.cur_info.mx,
              shi_speed_data[re][y]["avg"]
            );
          }
        }
      }
      this.speed_region_Chart = this.$echarts.init(this.$refs.speed_region);
      let that = this;
      let speed_region_option = {
        geo: {
          map: this.cur_info.region,
          z: 2,
          aspectScale: 1,
          layoutCenter: ["50%", "50%"], //地图位置
          zoom: 1, //当前视角的缩放比例
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
            },
            emphasis: {
              show: true,
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
          {
            show: true,
            type: "effectScatter",
            symbolSize: function (params) {
              if (that.cur_info.region != "山西") return 0;
              let re = params[2].substring(0, 2);
              if (re in shi_speed_data == false) return 0;
              //console.log(re)
              let y = that.cur_info.year;
              if (y in shi_speed_data[re] == false) return 0;
              let cur_v = (shi_speed_data[re][y]["avg"] / that.cur_info.mx) * 1;
              console.log(cur_v);
              return 10 / cur_v;
            },
            rippleEffect: {
              // 涟漪特效相关配置。
              scale: 4, // 控制涟漪大小
            },
            coordinateSystem: "geo", // series坐标系类型
            data: scar_data,
            z: 10,
          },
        ],
      };
      this.speed_region_Chart.setOption(speed_region_option);
      this.speed_region_Chart.on("click", function (params) {
        if (that.cur_info.region != "山西") return;
        if (
          params.name.substring(0, 2) != "吕梁" &&
          params.name.substring(0, 2) != "晋中" &&
          params.name.substring(0, 2) != "阳泉" &&
          params.name.substring(0, 2) != "朔州" &&
          params.name.substring(0, 2) != "太原"
        )
          return;

        that.$router.push({
          name: "ShiView",
          query: {
            region: params.name.substring(0, 2),
          },
        });
      });
    },
    async set_speed_tag() {
      //--------------------------set speedTag
      if (this.speed_tag_Chart) this.speed_tag_Chart.clear();
      else this.speed_tag_Chart = this.$echarts.init(this.$refs.speed_tag);

      this.speed_tag_Chart.clear();
      let that = this;
      this.speed_tag_Chart.setOption({
        dataset: {
          source:
            num_tag_data[this.cur_info.region][this.cur_info.year][
              this.cur_info.title
            ],
        },
        polar: {
          radius: [30, "70%"],
        },
        radiusAxis: {
          type: "category",
          nameTextStyle: {
            color: "rgba(255,255,255)",
          },
          show: false,
          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        angleAxis: {
          startAngle: 75,
          name: "响应时间",
          nameTextStyle: {
            color: "rgba(255,255,255)",
          },

          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255)",
            },
          },
        },
        tooltip: {},
        series: {
          type: "bar",
          coordinateSystem: "polar",
          encode: {
            radius: 0,
            angle: 1,
          },
          label: {
            show: false,
            position: "middle",
          },
          itemStyle: {
            color: function (params) {
              return that.color_list[params.dataIndex];
            },
          },
        },
      });
    },
    screenAdapter() {
      let that = this;
      setTimeout(function () {
        if (that.num_tag_Chart) {
          let options = {
            xAxis: {
              nameTextStyle: {
                fontSize: that.nowSize(16),
              },
              axisLabel: {
                textStyle: {
                  fontSize: that.nowSize(16),
                },
              },
            },
            yAxis: {
              nameTextStyle: {
                fontSize: that.nowSize(16),
              },
              axisLabel: {
                textStyle: {
                  fontSize: that.nowSize(16),
                },
              },
            },
            visualMap: {
              textStyle: {
                fontSize: that.nowSize(16),
              },
            },
          };
          that.num_tag_Chart.setOption(options);
          that.num_tag_Chart.resize();
        }
      }, 300);
      setTimeout(function () {
        if (that.speed_average_Chart) {
          let option = {
            legend: {
              textStyle: {
                fontSize: that.nowSize(14),
              },
              left: that.nowSize(80),
              top: that.nowSize(20),
            },
          };
          that.speed_average_Chart.setOption(option);
          that.speed_average_Chart.resize();
        }
      }, 300);
      setTimeout(function () {
        if (that.speed_region_Chart) {
          let options = {
            geo: {
              label: {
                normal: {
                  textStyle: {
                    fontSize: that.nowSize(18),
                  },
                  offset: [0, that.nowSize(-20)],
                },
                emphasis: {
                  textStyle: {
                    fontSize: that.nowSize(18),
                  },
                  offset: [0, that.nowSize(-20)],
                },
              },
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
              {
                rippleEffect: {
                  // 涟漪特效相关配置。
                  scale: that.nowSize(4), // 控制涟漪大小
                },
              },
            ],
          };
          that.speed_region_Chart.setOption(options);
          that.speed_region_Chart.resize();
        }
      }, 300);
      setTimeout(function () {
        if (that.speed_tag_Chart) {
          let options = {
            polar: {
              radius: [that.nowSize(30), "70%"],
            },
          };
          that.speed_tag_Chart.setOption(options);
          that.speed_tag_Chart.resize();
        }
      }, 300);
    },
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
    if (this.num_tag_Chart) {
      this.num_tag_Chart.dispose();
      this.num_tag_Chart = null;
    }
    if (this.speed_average_Chart) {
      this.speed_average_Chart.dispose();
      this.speed_average_Chart = null;
    }
    clearInterval(this.speed_average_interval);
    window.removeEventListener("resize", this.screenAdapter);
  },
  components: {
    LeftPage,
  },
};
</script>
<style lang="less" scoped>
.fontA:hover {
  fill: #ffffff;
  font-weight: bold;
  cursor: pointer;
}
.time_select {
  width: 0.4667rem;
  height: 4.2rem;
  margin-left: 1.8rem;
  margin-top: 4.6167rem;
}
.speed_region {
  width: 17.5167rem;
  height: 9.9667rem;
  //width: 32rem;
  //height: 18rem;
  margin-top: 2.1rem;
  background: url(../assets/Sheng/speed_region.png) no-repeat;
  background-size: 100% 100%;
  justify-content: center;
}
.news {
  width: 9.1rem;
  height: 5.4167rem;
  margin-top: 0.2167rem;
  background: url(../assets/Sheng/news.png) no-repeat;
  background-size: 100% 100%;
}
.speed_average {
  width: 7.9833rem;
  height: 5.4167rem;
  margin-top: 0.2667rem;
  margin-left: 0.3667rem;
  background: url(../assets/Sheng/speed_average.png) no-repeat;
  background-size: 100% 100%;
}
.num_tag {
  width: 9.6rem;
  height: 5.6667rem;
  background: url(../assets/Sheng/num_tag.png) no-repeat;
  background-size: 100% 100%;
}
.word_cloud {
  width: 9.6rem;
  height: 5.6667rem;
  margin-top: 0.1667rem;

  background: url(../assets/Sheng/word_cloud.png) no-repeat;
  background-size: 100% 100%;
}
.speed_tag {
  width: 9.6rem;
  height: 5.0333rem;
  margin-top: 0.1667rem;

  background: url(../assets/Sheng/speed_tag.png) no-repeat;
  background-size: 100% 100%;
}
.ShengBackground {
  width: 32.2667rem;
  height: 18.05rem;
  background: url(https://ysr-data-view.oss-cn-hangzhou.aliyuncs.com/C778FA422F5F4FDB8043352BFEBFDC6B-6-2.png)
    no-repeat fixed;
  background-size: 100% 100%;
  margin: auto;
  display: flex;
  overflow: hidden;
  //background-position: center top;
  .item_left {
    margin-left: 0rem;
    margin-top: 0rem;
    width: 4.45rem;
    height: 100%;
    line-height: 0.3333rem;
    opacity: 0.89;
    background-color: rgba(29, 76, 170, 100);
    text-align: center;
  }
  .item_right {
    //display: flex;
    //flex-flow: column;
    .title {
      margin-left: 0rem;
      margin-top: 0rem;
      width: 27.8167rem;
      height: 5rem;
      background: url(../assets/main_page_title.png) no-repeat;
      background-size: 100% 100%;
      background-position: center top;
    }
    .content {
      margin-top: -5rem;
      display: flex;
      .left {
        margin-left: 0.7333rem;
        display: flex;
        flex-flow: column;
        height: 100%;
        width: 100%;
        .down {
          display: flex;
        }
      }
      .right {
        display: flex;
        flex-flow: column;
        margin-left: 0.1667rem;
        margin-top: 1rem;
        margin-right: 0.1667rem;
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>