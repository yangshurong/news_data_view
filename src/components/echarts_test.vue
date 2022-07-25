<template>
    <div>
         <div ref="main" style="width: 600px;height:400px;"></div>
    </div>
</template>
<script>
export default {
    data() {
        return {}
    },
    mounted() {
    // 基于准备好的dom，初始化echarts实例
        console.log(this.$refs.main)
        this.myChart = this.$echarts.init(this.$refs.main)
		// 指定图表的配置项和数据
        this.myChart.setOption({
            title: {
                text: '联系',
            },
            tooltip: {},
            xAxis: {
                data: ['一', '二', '三', '四', '五', '六']
            },
            yAxis: {},
            series: [{
                name: '人数',
                type: 'bar',
                data: [45, 46, 56, 34, 47, 48]
            }]
        })
    },
}

</script>