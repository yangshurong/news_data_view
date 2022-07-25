<template>
  <div class="video_main_background">
    <div class="video_show">
      <videoPlayer
      class="vjs-custom-skin videoPlayer"
      :options="playerOptions"
      ref="videoPlayer"
      :playsinline="true"
      @ended="onPlayerEnded($event)"
      style="z-index: 0;"
      ></videoPlayer>
    </div>
    
    <div class="go_main_page" @click="go_main_page">
      跳过动画，直接进入首页
    </div>
  </div>
</template>
<script>
// import 'video.js/dist/video-js.css'
import { videoPlayer } from "vue-video-player/src";
import "videojs-flash";
require("video.js/dist/video-js.css");
require("vue-video-player/src/custom-theme.css");
export default {
  data() {
    return {
      playerOptions: {
        height: 500,
        playbackRates: [0.7, 1.0, 1.5, 2.0, 4.0], // 播放速度
        autoplay: true, // 如果true,浏览器准备好时开始回放。
        muted: false, // 默认情况下将会消除任何音频。
        loop: false, // 导致视频一结束就重新开始。
        preload: "auto", // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
        language: "zh-CN",
        aspectRatio: "16:9", // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        sources: [
          {
            type: "video/mp4", // 这里的种类支持很多种：基本视频格式、直播、流媒体等，具体可以参看git网址项目【video/mp4】【application/x-mpegURL】【rtmp/flv】
            src: "https://ysr-data-view.oss-cn-hangzhou.aliyuncs.com/main_video.mp4" // url地址
          },
          //{
          //  type: "application/x-mpegURL",
          //  src: "https://cdn.letv-cdn.com/2018/12/05/JOCeEEUuoteFrjCg/playlist.m3u8",
          //},
        ],
        // poster: require("@/assets/poster.png"), // 你的封面地址
        //poster: "http://10.60.1.180:8081/file/yanhua.jpg", // 你的封面地址
        //width: document.documentElement.clientWidth, //播放器宽度
        notSupportedMessage: "此视频暂无法播放，请稍后再试", // 允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: false,
          durationDisplay: false,
          remainingTimeDisplay: false,
          fullscreenToggle: false, // 全屏按钮
        },
      },
    };
  },
  components: {
    videoPlayer,
  },
  mounted() {},
  methods: {
    go_main_page(){
      this.$router.push({
        name: "path",
      });
    },
    onPlayerEnded(params){
      this.go_main_page()
    }
  },
};
</script>
<style lang="less" scoped>
.video_main_background {
  height: 18rem;
  width: 32rem;
  margin: 0 auto;
  overflow: hidden;
  background-color: white;
  .video_show{
    height: 95%;
    width: 100%;
  }
  .go_main_page{
    z-index: 999999;
    font-size: 0.5rem;
    
    color: black;
  }
}
</style>