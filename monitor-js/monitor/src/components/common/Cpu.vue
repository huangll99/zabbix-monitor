<template>
    <div id="cpu">

    </div>
</template>

<script>
    import echarts from 'echarts'
    import moment from 'moment'

    export default {
        props: {
            hostid: String
        },
        created() {
            self = this;
            self.$http.get('/api/cpu/', {
                params: {
                    hostid: self.hostid
                }
            }).then((res) => {
                const items = res.data;
                let ydata = [];
                let xdata = [];
                items.forEach(function (item) {
                    xdata.push(item['clock']);
                    ydata.push(item['value']);
                });
                xdata = xdata.map(function (time) {
                    return moment(time * 1000).format('HH:mm:ss') + '\n\n' + moment(time*1000).format('YYYY/MM/DD')
                });
                const cpuChart = echarts.init(document.getElementById('cpu'));
                const option = {
                    title: {
                       // text: 'cpu利用率'
                    },
                    tooltip: {
                        trigger: 'axis'

                    },
                    legend: {
                        data: ['cpu利用率']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        data: xdata
                    },
                    yAxis: {},
                    series: [
                        {
                            name: 'cpu利用率',
                            type: 'line',
                            smooth: true,
                            data: ydata,
                            sampling: 'average',
                            itemStyle: {
                                normal: {
                                    color: 'rgb(255,70,131)'
                                }
                            },
                            areaStyle: {
                                normal: {
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: 'rgb(255,158,68)'
                                    }, {
                                        offset: 1,
                                        color: 'rgb(255,70,131)'
                                    }])
                                }
                            }
                        }
                    ]
                };

                // 使用刚指定的配置项和数据显示图表。
                cpuChart.setOption(option);
            });
        }
    }
</script>
<style scoped="scoped">
    #cpu {
        width: 1500px;
        height: 500px;
    }
</style>
