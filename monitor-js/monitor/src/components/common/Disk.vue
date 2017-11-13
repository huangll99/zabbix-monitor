<template>
    <div id="disk">

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
            self.$http.get('/api/disk/', {
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
                ydata = ydata.map(function (memory) {
                    const i = Math.floor(Math.log(memory) / Math.log(1024));
                    return (memory / Math.pow(1024, i)).toPrecision(3);
                });
                const cpuChart = echarts.init(document.getElementById('disk'));
                const option = {
                    title: {
                        text: ''
                    },
                    tooltip: {
                        trigger: 'axis'

                    },
                    legend: {
                        data: ['剩余磁盘空间']
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
                    yAxis: {
                        name:'disk(G)'
                    },
                    series: [
                        {
                            name: '剩余磁盘空间',
                            type: 'line',
                            //smooth: true,
                            data: ydata,
                            //sampling: 'average',
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
    #disk {
        width: 1500px;
        height: 500px;
    }
</style>
