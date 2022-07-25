const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: config => {
    // config.module
    //   .rule("css")
    //   .test(/\.css$/)
    //   .oneOf("vue")
    //   .resourceQuery(/\?vue/)
    //   .use("px2rem")
    //   .loader("px2rem-loader")
    //   .options({
    //     remUnit: 192 // 设计稿大小比例 / 10
    //   });
  },
  pwa: {
    iconPaths: {
      favicon32: 'ydook.ico',
      favicon16: 'ydook.ico',
      appleTouchIcon: 'ydook.ico',
      maskIcon: 'ydook.ico',
      msTileImage: 'ydook.ico'
    }
  }
},
)
