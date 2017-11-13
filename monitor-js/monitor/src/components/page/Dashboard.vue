<template>
    <div class="dashboard">
        <quick-menu :position="position" :menuCount="count" :iconClass="icons" :menuUrlList="list"></quick-menu>

        <el-row>
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
                    <p class="board-p">24</p>
                </el-card>
            </el-col>
            <el-col :span="2" :offset="2">
                <el-card>
                    <p class="board-p">
                        <img src="/static/img/mysql.png" alt="">
                    </p>
                    <p class="board-p">24</p>
                </el-card>
            </el-col>
            <el-col :span="2" :offset="2">
                <el-card>
                    <p class="board-p">
                        <img src="/static/img/oracle2.jpg" alt="">
                    </p>
                    <p class="board-p">24</p>
                </el-card>
            </el-col>
            <el-col :span="2" :offset="2">
                <el-card>
                    <p class="board-p">
                        <img src="/static/img/tomcat.png" alt="">
                    </p>
                    <p class="board-p">24</p>
                </el-card>
            </el-col>
        </el-row>
        <div style="margin-top: 40px;">
            <iframe src="http://172.17.38.107:3000/dashboard-solo/db/windows-pcji-qun-jian-kong?refresh=1m&orgId=1&panelId=8&from=1510220419309&to=1510231219309&var-host=All&var-int=All" width="650" height="300" frameborder="0"></iframe>

            <iframe src="http://172.17.38.107:3000/dashboard-solo/db/windows-pcji-qun-jian-kong?refresh=1m&orgId=1&panelId=14&from=1510220612644&to=1510231412644&var-host=All&var-int=All" width="650" height="300" frameborder="0"></iframe>
        </div>
        <div style="margin-top: 40px;">
            <iframe src="http://172.17.38.107:3000/dashboard-solo/db/windows-pcji-qun-jian-kong?refresh=1m&orgId=1&panelId=15&from=1510220811843&to=1510231611843&var-host=All&var-int=All" width="650" height="300" frameborder="0"></iframe>
            <iframe src="http://172.17.38.107:3000/dashboard-solo/db/windows-pcji-qun-jian-kong?refresh=1m&orgId=1&panelId=16&from=1510220852848&to=1510231652848&var-host=All&var-int=All" width="650" height="300" frameborder="0"></iframe>
        </div>
        <div style="margin-top: 40px;">
            <iframe src="http://172.17.38.107:3000/dashboard-solo/db/windows-pcji-qun-jian-kong?refresh=1m&orgId=1&panelId=17&from=1510220884462&to=1510231684462&var-host=All&var-int=All" width="650" height="300" frameborder="0"></iframe>
            <iframe src="http://172.17.38.107:3000/dashboard-solo/db/windows-pcji-qun-jian-kong?refresh=1m&orgId=1&panelId=18&from=1510220901934&to=1510231701934&var-host=All&var-int=All" width="650" height="300" frameborder="0"></iframe>
        </div>
    </div>
</template>

<script>
    import moment from "moment"
    import echarts from 'echarts'

    import quickMenu from 'vue-quick-menu'
    import QuickMenu from "../../../node_modules/vue-quick-menu/src/quickMenu.vue";

    export default {
        components: {QuickMenu},
        data() {
            return {
                service: 'httpd',
                items: '',
                count:4,
                icons:['tomcat'],
                list:['1','2','3','4'],
                position:'bottom-right'
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

</style>
