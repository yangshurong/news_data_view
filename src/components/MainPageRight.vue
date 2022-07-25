<template>
  <div class="main_layout">
    <!-- <img src="../assets/view_test.PNG" alt="没有图片"> -->
    <div class="main_content">
      <MapPage :title_change="cur_title"/>
      <!-- <TestChart/> -->
      <div class="right-area">
        <h3>响应速度排名 <b></b></h3>
        <div class="area-inbox-1">
          <dl>
            <dt>山西省</dt>
            <dd class="font12"><span>第一名</span><b></b></dd>
            <dt class="ml-20">平均响应速度</dt>
            <dd class="font-red ml-20"><span>3.6天</span><b></b></dd>
            <dt></dt>
            <dd><span></span><b></b></dd>
          </dl>
          <div class="round-1"></div>
          <div class="round-2"></div>
          <div class="round-3">30%</div>
          <div class="round-4"></div>
        </div>
        <div class="area-inbox-2">
          <ul>
            <li><strong>2</strong>河北省<b></b><em></em></li>
            <li><strong>3</strong>河南省<b></b><em></em></li>
            <li><strong>4</strong>广西省<b></b><em></em></li>
          </ul>
          <div class="area-text">
            <b class="animation-line1"></b>
            <h4>速度说明：</h4>
            <p class="text_container"></p>
            <b class="animation-line2"></b>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="main_footer">
      <MainSupportRight />
    </div> -->
  </div>
</template>
<script>
import MainSupportRight from "./main_support_right.vue";
import MapPage from "./MainPageRightMap.vue";
import TestChart from "./echarts_test.vue";
import $ from "jquery";
import "jquery-ui";
export default {
  data(){
    return{
      cur_title:'政治'
    }
  },
  components: {
    MainSupportRight,
    MapPage,
    TestChart,
  },
  props:{
    title_change:{
      type:String,
      default:'政治'
    }
  },
  watch:{
    title_change(new_val,old_val){
      this.cur_title=new_val
    }
  },
  mounted() {
    var s =
      "速度根据，中央发布后地方做出响应的时间差来计算，响应天数大的速度慢";
    var con = $(".text_container");
    var index = 0;
    var length = s.length;
    var tId = null;
    function start() {
      con.text("");
      tId = setInterval(function () {
        con.append(s.charAt(index));
        if (index++ === length) {
          clearInterval(tId);
          index = 0;
          start();
        }
      }, 200);
    }
    start();
  },
};
</script>
<style lang="less" scoped>
.main_layout {
  //background-color: rgba(255, 255, 255, 0);
  display: flex;
  flex-flow: column;

  .main_content {
    @import "../assets/main_time/css/default.css";
    @import "../assets/main_time/css/mobile.css";
    @import "../assets/main_time/css/normalize.css";
    @import "../assets/main_time/css/style.css";
    margin-top: .2167rem;
    margin-left: 1.05rem;
    width: 25.7rem;
    height: 18rem;
    display: flex;
    //background: url(../assets/view_test.PNG) no-repeat;
    //background-size:100% 100%;
  }
  .main_footer {
    height: 0rem;
    margin-top: 0rem;
    padding-left: 0rem;
  }
}
</style>