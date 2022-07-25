<template>
  <div id="app" class="main_background">
    <div class="title"></div>
    <div class="content">
      <section class="item_left">
        <LeftPage @title_change="title_change" />
      </section>
      <section class="item_right">
        <RightPage :title_change="cur_title" />
      </section>
    </div>
  </div>
</template>
<script>
import LeftPage from "../components/MainPageLeft.vue";
import RightPage from "../components/MainPageRight.vue";

export default {
  data() {
    return {
      cur_title: "政治",
    };
  },
  components: {
    LeftPage,
    RightPage,
  },
  mounted() {
    
  },
  methods: {
    title_change(new_title) {
      //title变化后
      this.cur_title = new_title;
    },
  },
};
</script>
<style lang="less" scope>
.main_background {
  // max-width: 1920px;
  // min-width: none;
  width: 32.2667rem;
  height: 18.05rem;
  //background: url(../assets/view_test.PNG) no repeat;
  background: url(../assets/index_background2.jpg) no-repeat;
  background-size: 100% 100%;
  margin: 0 auto;
  overflow: hidden;
  //display: flex;
  //flex-flow: column;
  .title {
    margin-left: 0rem;
    margin-top: 0rem;
    width: 100%;
    height: 5rem;
    background: url(../assets/main_page_title.png) no-repeat;
    background-size: 100% 100%;
    background-position: center top;
  }
  .content {
    display: flex;
    margin-top: -4.1667rem;
    .item_left {
      margin-left: .1333rem;
      margin-top: 0rem;
      width: 4.45rem;
      height: 17.2333rem;
      line-height: .3333rem;
      opacity: 0.89;
      background-color: rgba(29, 76, 170, 100);
      text-align: center;
    }
  }
}
</style>