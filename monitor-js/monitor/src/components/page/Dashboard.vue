<template>
    <div class="dashboard">
        <quick-menu :position="position" :menuCount="count" :iconClass="icons" :menuUrlList="list"></quick-menu>

        <el-row>
            <el-col :span="5" :offset="1">
                <china-map></china-map>
            </el-col>
            <el-col :span="14" :offset="4">
                <event-table></event-table>
            </el-col>
        </el-row>
        <el-row style="margin-top: 40px;">
            <el-col :span="2" :offset="2">
                <el-card>
                    <p class="board-p">
                        <img src="/static/img/redis.png" alt="">
                    </p>
                    <p class="board-p">24</p>
                </el-card>
            </el-col>
            <el-col :span="2" :offset="2">
                <el-card>
                    <p class="board-p">
                        <img src="/static/img/mongo.png" alt="">
                    </p>
                    <p class="board-p">15</p>
                </el-card>
            </el-col>
            <el-col :span="2" :offset="2">
                <el-card>
                    <p class="board-p">
                        <img src="/static/img/mysql.png" alt="">
                    </p>
                    <p class="board-p">3</p>
                </el-card>
            </el-col>
            <el-col :span="2" :offset="2">
                <el-card>
                    <p class="board-p">
                        <img src="/static/img/oracle2.jpg" alt="">
                    </p>
                    <p class="board-p">4</p>
                </el-card>
            </el-col>
            <el-col :span="2" :offset="2">
                <el-card>
                    <p class="board-p">
                        <img src="/static/img/tomcat.png" alt="">
                    </p>
                    <p class="board-p">31</p>
                </el-card>
            </el-col>
        </el-row>

        <el-row style="margin-top: 40px;">
            <el-col :span="10" :offset="1">
                <iframe src="http://172.17.38.107:3000/dashboard-solo/db/jian-kong-ping-tai-tu-biao?orgId=1&var-group=All&var-host=All&var-application=All&var-item=All&panelId=1&from=now-6h&to=now" width="650" height="300" frameborder="0"></iframe>
            </el-col>
            <el-col :span="10" :offset="1">
                <iframe src="http://172.17.38.107:3000/dashboard-solo/db/jian-kong-ping-tai-tu-biao?orgId=1&var-group=All&var-host=All&var-application=All&var-item=All&panelId=2&from=now-6h&to=now" width="650" height="300" frameborder="0"></iframe>
            </el-col>
        </el-row>
        <el-row style="margin-top: 40px;">
            <el-col :span="10" :offset="1">
                <iframe src="http://172.17.38.107:3000/dashboard-solo/db/jian-kong-ping-tai-tu-biao?orgId=1&var-group=All&var-host=All&var-application=All&var-item=All&panelId=3&from=now-6h&to=now" width="650" height="300" frameborder="0"></iframe>
            </el-col>
            <el-col :span="10" :offset="1">
                <iframe src="http://172.17.38.107:3000/dashboard-solo/db/jian-kong-ping-tai-tu-biao?orgId=1&var-group=All&var-host=All&var-application=All&var-item=All&panelId=4&from=now-6h&to=now" width="650" height="300" frameborder="0"></iframe>
            </el-col>
        </el-row>

    </div>
</template>

<script>
    import moment from "moment"
    import echarts from 'echarts'

    import quickMenu from 'vue-quick-menu'
    import QuickMenu from "../../../node_modules/vue-quick-menu/src/quickMenu.vue";
    import ElRow from "../../../node_modules/element-ui/packages/row/src/row.vue";

    import ChinaMap from "../common/ChinaMap.vue";
    import EventTable from "../common/EventTable.vue";

    export default {
        components: {
            ElRow,
            QuickMenu,
            ChinaMap,
            EventTable
        },
        data() {
            return {
                service: 'httpd',
                items: '',
                count:4,
                icons:['tomcat'],
                list:['1','2','3','4'],
                position:'bottom-right',
                star:4
            }
        },
        created() {

        },
        methods: {}
    }
</script>

<style>
    .board-p {
        text-align: center;
        font-size: 20px;
    }

    .board-p img {
        width: 80%;
        height: 40px;
    }

    .quick-menu{
        z-index: 1000;
    }
</style>
