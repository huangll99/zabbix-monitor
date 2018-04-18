<template>
    <div id="chinamap">

    </div>
</template>

<script>
    import 'echarts/map/js/china'
    import echarts from 'echarts'


    export default {
        mounted() {
            const mapChart = echarts.init(document.getElementById('chinamap'));
            let data = [
                {name: '合肥', value: 49},
                {name: '武汉', value: 40},
                {name: '北京', value: 82},
                {name: '巴西', value: 1}
            ];
            let geoCoordMap = {
                '北京': [116.46, 39.92],
                '合肥': [117.27, 31.86],
                '武汉': [114.31, 30.52],
                '巴西': [38.02, 23.44]
            };

            let convertData = function (data) {
                var res = [];
                for (var i = 0; i < data.length; i++) {
                    var geoCoord = geoCoordMap[data[i].name];
                    if (geoCoord) {
                        res.push({
                            name: data[i].name,
                            value: geoCoord.concat(data[i].value)
                        });
                    }
                }
                return res;
            };

            let option = {
                backgroundColor: '#404a59',
                title: {
                    text: '服务器城市分布',
                    x: 'center',
                    textStyle: {
                        color: '#fff'
                    }
                },
                tooltip: {
                    trigger: 'item',
                    formatter: function (params) {
                        return params.name + ' : ' + params.value[2];
                    }
                },
                legend: {
                    orient: 'vertical',
                    y: 'bottom',
                    x: 'right',
                    data: ['server'],
                    textStyle: {
                        color: '#fff'
                    }
                },
                visualMap: {
                    min: 0,
                    max: 200,
                    calculable: true,
                    inRange: {
                        color: ['#50a3ba', '#eac736', '#d94e5d']
                    },
                    textStyle: {
                        color: '#fff'
                    }
                },
                geo: {
                    map: 'china',
                    label: {
                        emphasis: {
                            show: true
                        }

                    },
                    itemStyle: {
                        normal: {
                            areaColor: '#004981',
                            borderColor: '#111'
                        },
                        emphasis: {
                            areaColor: '#2a333d'
                        }
                    }
                },
                series: [
                    {
                        name: 'server',
                        type: 'scatter',
                        coordinateSystem: 'geo',
                        data: convertData([
                            {name: '合肥', value: 49},
                            {name: '武汉', value: 40},
                            {name: '北京', value: 82},
                            {name: '巴西', value: 1}
                        ]),
                        symbolSize: 12,
                        label: {
                            normal: {
                                show: true,
                                formatter: '{b}',
                                position: 'right'
                            },
                            emphasis: {
                                show: false
                            }
                        },
                        itemStyle: {
                            emphasis: {
                                borderColor: '#fff',
                                borderWidth: 1
                            }
                        }
                    }
                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            mapChart.setOption(option);
        }
    }
</script>
<style scoped="scoped">
    #chinamap {
        width: 550px;
        height: 400px;
    }
</style>
