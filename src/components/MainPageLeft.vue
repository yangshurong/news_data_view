<template>
  <!-- 无缝滚动效果 -->

  <li class="main_li">
    <div class="verticalBar"></div>
    <div class="marquee-wrap">
      <ul class="marquee-list">
        <li
          @click="title_click(item,index)"
          class="swiper-slide"
          :class="{ 'title_click':item.clicked }"
          v-for="(item, index) in listData"
          :key="index"
        >
          {{ item.info }}
        </li>
      </ul>
    </div>
  </li>
</template>
 
<script>
export default {
  name: "marquee-up",
  data() {
    return {
      animateUp: false,
      listData: [
        {
          info:"经济",
          clicked:false
        },
        {
          info:"资源", 
          clicked:false
        },
        {
          info:"生产",
          clicked:false
        },
        {
          info:"文化",
          clicked:false
        },
        {
          info:"民生",
          clicked:false
        },
        {
          info:"政治",
          clicked:true         
        },                                                    
      ],
      timer: null,
    };
  },
  mounted() {
    //this.timer = setInterval(this.scrollAnimate, 1500);
  },
  methods: {
    // scrollAnimate() {
    //   this.animateUp = true;
    //   setTimeout(() => {
    //     thisNaNpxData.push(thisNaNpxData[0]);
    //     thisNaNpxData.shift();
    //     this.listData = [];
    //     for (let i = 0; i <= 5; i++) {
    //       this.listData.push(thisNaNpxData[i]);
    //     }
    //     this.animateUp = false;
    //   }, 500);
    // },
    title_click(item,id) {
      this.$emit('title_change',item.info);
      for(let i in this.listData){
        this.listData[i].clicked=false
      }
      this.listData[id].clicked=true

    },
  },
  destroyed() {
    
  },
};
</script>
 
<style lang="less">
.main_li {
  display: flex;
  .verticalBar {
    width: .0833rem;
    height: 15.1333rem;
    background: rgba(255, 255, 255, 100);
    display: inline-block;
    vertical-align: top;
    margin-left: .45rem;
    margin-top: .8833rem;
  }

  .marquee-wrap {
    margin-left: .4333rem;
    width: 80%;
    border-radius: .3333rem;
    background: rgba(0, 0, 0, 0);
    margin: 0 auto;
    overflow: hidden;
    flex-flow: column;
    .marquee-list {
      overflow: hidden;
      li {
        width: 100%;
        height: .7167rem;
        align-items: center;
        justify-content: center;
        text-overflow: hidden;
        overflow: hidden;
        white-space: nowrap;
        padding: 1.3833rem .4rem;
        list-style: none;
        line-height: .8333rem;
        text-align: center;
        color: #fff;
        font-size: .4667rem;
      }
      .title_click{
        width: 100%;
        height: .7167rem;
        align-items: center;
        justify-content: center;
        text-overflow: hidden;
        overflow: hidden;
        white-space: nowrap;
        padding: 1.3833rem .4rem;
        list-style: none;
        line-height: .8333rem;
        text-align: center;
        color: #fff;
        font-size: .6rem;
        font-weight: bold;
      }
    }
    .animate-up {
      transition: all 0.5s ease-in-out;
      transform: translateY(-2.7667rem);
    }
  }
}
</style>