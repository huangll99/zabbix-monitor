<template>
    <div class="detail">
        <el-card>
            <div slot="header">
                <h2 style="color: #d15e10;">主机简介</h2>
            </div>
            <div style="display: flex;justify-content: space-between;">
                <div class="box color-blue" style="width: 28%;">
                    <div class="title">当前时间</div>
                    <div class="contents"> {{systemTime}}</div>
                </div>
                <div class="box color-yellow" style="width: 40%;">
                    <div class="title">主机名称</div>
                    <div class="contents"> {{usage.hostname}}</div>
                </div>
                <div class="box color-blue" style="width: 28%;">
                    <div class="title">系统运行时间</div>
                    <div class="contents"> 1 WEEK</div>
                </div>
            </div>
        </el-card>

        <el-card style="margin-top: 50px;">
            <div slot="header">
                <h2 style="color: #d15e10;">资源利用率</h2>
            </div>
            <div style="margin-top: 50px;display: flex;justify-content:space-around">
                <i-circle :size=160 class="circle" :percent="usage.cpu" stroke-color="green" trail-color="#ccc">
                    <h2>CPU利用率</h2>
                    <h3 style="padding-top: 15px;">{{usage.cpu}}%</h3>
                </i-circle>
                <i-circle :size=160 class="circle" :percent="80" stroke-color="red" trail-color="#ccc">
                    <h2>内存利用率</h2>
                    <h3 style="padding-top: 15px;">{{usage.memory}} G</h3>
                </i-circle>
                <i-circle :size=160 class="circle" :percent="usage.disk" stroke-color="blue" trail-color="#ccc">
                    <h2>磁盘利用率</h2>
                    <h3 style="padding-top: 15px;">{{usage.disk}}%</h3>
                </i-circle>
            </div>
        </el-card>

        <el-card style="margin-top: 50px;">
            <div slot="header">
                <h2 style="color: #d15e10;">cpu监控</h2>
            </div>
            <div>
                <cpu :hostid="hostid"></cpu>
            </div>
        </el-card>

        <el-card style="margin-top: 50px;">
            <div slot="header">
                <h2 style="color: #d15e10;">memory监控</h2>
            </div>
            <div>
                <memory :hostid="hostid"></memory>
            </div>
        </el-card>

        <el-card style="margin-top: 50px;">
            <div slot="header">
                <h2 style="color: #d15e10;">disk监控</h2>
            </div>
            <div>
                <disk :hostid="hostid"></disk>
            </div>
        </el-card>
    </div>
</template>

<script>
    import ElCard from "../../../node_modules/element-ui/packages/card/src/main.vue";
    import cpu from "../common/Cpu.vue"
    import memory from "../common/Memory.vue"
    import disk from "../common/Disk.vue"
    import moment from "moment";

    export default {
        components: {ElCard, cpu, memory, disk},
        data() {
            return {
                hostid: this.$route.query.hostid,
                usage: {
                    disk: 0,
                    memory: 0,
                    cpu: 0,
                    hostname: ''
                },
                systemTime: ''
            }
        },
        created() {
            const self = this;
            self.$http.get('/api/usage/', {
                params: {
                    hostid: self.hostid
                }
            }).then((res) => {
                const items = res.data;
                let memory = items[0]['cpuUsage'][0]['value'];
                const i = Math.floor(Math.log(memory) / Math.log(1024));
                memory = (memory / Math.pow(1024, i)).toPrecision(3);
                self.usage = {
                    disk: parseInt(items[0]['diskUsage'][0]['value']),
                    hostname: items[0]['host']['name'],
                    memory: memory,
                    cpu: parseFloat(items[0]['cpuUsage'][0]['value']),
                }
            });
            setInterval(function () {
                self.systemTime = moment(new Date().getTime()).format('HH:mm:ss')
            }, 1000)
        },
        methods: {}
    }
</script>

<style scoped>
    .circle {
        display: inline-block;
        margin: 0 50px;
    }

    .box {
        height: 150px;
        padding: 0 50px;
        border: 1px solid #292929;
        text-align: center;
    }

    .box .title {
        font-weight: 600;
        font-size: 1rem;
        line-height: 2;
    }

    .box .contents {
        text-align: center;
        font-size: 3em;
        font-weight: 700;
        line-height: 3;
    }

    .color-yellow {
        background-color: rgba(250, 139, 47, 0.890196);
    }

    .color-blue {
        background-color: rgba(50, 172, 45, 0.972549);
    }

    .color-green {
        background-color: rgb(60, 87, 14);
    }
</style>
