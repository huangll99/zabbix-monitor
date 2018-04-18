<template>
    <chart :width="1000" :options="polar"></chart>
</template>

<script>
    import moment from 'moment'

    export default {
        props: {
            itemid: String,
            name: String
        },
        data() {
            return {
                polar: {
                    title: {
                        // text: 'cpu利用率'
                    },
                    tooltip: {
                        trigger: 'axis'

                    },
                    legend: {
                        data: ['']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        data: []
                    },
                    yAxis: {},
                    series: [
                        {
                            name: '',
                            type: 'line',

                            data: [],

                            itemStyle: {
                                normal: {
                                    color: 'rgb(255,70,131)'
                                }
                            }
                        }
                    ]

                }
            }
        },
        created() {
            console.log(this.name)
            let self = this;
            this.$http.get('/api/history/', {
                params: {
                    itemid: this.itemid
                }
            }).then((res) => {
                let items = res.data;
                let ydata = [];
                let xdata = [];
                for (let j = 0; j < items.length; j++) {
                    xdata.push(items[j]['clock']);
                    ydata.push(items[j]['value_avg']);
                }
                xdata = xdata.map(function (time) {
                    return moment(time * 1000).format('HH:mm:ss') + '\n\n' + moment(time * 1000).format('YYYY/MM/DD')
                });
                self.polar.xAxis.data = xdata;
                self.polar.series[0].data = ydata;
                self.polar.legend.data[0] = self.name + " 服务监听"
                self.polar.series[0].name = self.name + " 服务监听"
            });
        }
    }
</script>
<style scoped="scoped">
    .echarts {
        width: 1500px;
    }
</style>
