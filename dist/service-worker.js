if(!self.define){let n,i={};const e=(e,l)=>(e=new URL(e+".js",l).href,i[e]||new Promise((i=>{if("document"in self){const n=document.createElement("script");n.src=e,n.onload=i,document.head.appendChild(n)}else n=e,importScripts(e),i()})).then((()=>{let n=i[e];if(!n)throw new Error(`Module ${e} didn’t register its module`);return n})));self.define=(l,o)=>{const r=n||("document"in self?document.currentScript.src:"")||location.href;if(i[r])return;let s={};const u=n=>e(n,r),t={module:{uri:r},exports:s,require:u};i[r]=Promise.all(l.map((n=>t[n]||u(n)))).then((n=>(o(...n),s)))}}define(["./workbox-2d118ab0"],(function(n){"use strict";n.setCacheNameDetails({prefix:"myapp"}),self.addEventListener("message",(n=>{n.data&&"SKIP_WAITING"===n.data.type&&self.skipWaiting()})),n.precacheAndRoute([{url:"/css/app.1f2afd0d.css",revision:null},{url:"/css/chunk-vendors.8ffaaa7a.css",revision:null},{url:"/fonts/DS-DIGIT.56a27acf.TTF",revision:null},{url:"/fonts/element-icons.f1a45d74.ttf",revision:null},{url:"/fonts/element-icons.ff18efd1.woff",revision:null},{url:"/fonts/ionicons.31fd4446.ttf",revision:null},{url:"/fonts/ionicons.d03f2836.woff2",revision:null},{url:"/fonts/ionicons.dacd136b.woff",revision:null},{url:"/img/3dwordCloud.12aeb474.png",revision:null},{url:"/img/bg01warp.b36191c3.png",revision:null},{url:"/img/index_background2.6f34648a.jpg",revision:null},{url:"/img/ionicons.6e8059e8.svg",revision:null},{url:"/img/main_page_title.ba957627.png",revision:null},{url:"/img/main_tooltip.d0fffd89.png",revision:null},{url:"/img/news.9c3731d2.png",revision:null},{url:"/img/news_content.57e15aea.png",revision:null},{url:"/img/num_tag.2d0c9b5e.png",revision:null},{url:"/img/policy_content.9c6c45f1.png",revision:null},{url:"/img/policy_icon.5f132055.png",revision:null},{url:"/img/rank_speed.4ea780cf.png",revision:null},{url:"/img/speed_average.10ea6926.png",revision:null},{url:"/img/speed_region.7c04852c.png",revision:null},{url:"/img/speed_tag.4e61f790.png",revision:null},{url:"/img/tag_num.06e0ac24.png",revision:null},{url:"/img/word_cloud.12aeb474.png",revision:null},{url:"/index.html",revision:"48ec305081a693ba7b54b18d1a2e97a7"},{url:"/manifest.json",revision:"fb4b0f6c10067ebcb6fed2b06d92b3de"},{url:"/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"},{url:"/ydook.ico",revision:"ba8e2ba24144b7d142a0c02b65f89234"}],{})}));
//# sourceMappingURL=service-worker.js.map
