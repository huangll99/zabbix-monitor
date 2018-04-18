<template>
    <div class="detail">
        <el-card v-for="item in items" style="margin-bottom: 30px;">
            <div slot="header">
                <h2 style="color: #d15e10;">
                    <span>服务器名称: {{item.hosts[0].name}}</span> /
                    <span>主机host: {{item.hosts[0].host}}</span>
                </h2>
            </div>
            <div style="display: flex;justify-content: space-between;">
                <service-chart :itemid="item.itemid" :name="service"></service-chart>
            </div>
        </el-card>
    </div>
</template>

<script>
    import ElCard from "../../../node_modules/element-ui/packages/card/src/main.vue";
    import moment from "moment"
    import echarts from 'echarts'
    import ServiceChart from "../common/ServiceChart.vue"

    export default {
        components: {ElCard, ServiceChart},
        data() {
            return {
                service: 'FTP',
                items: ''
            }
        },
        created() {
            let self = this;
            this.$http.get('/api/serviceItems/', {
                params: {
                    service: this.service
                }
            }).then((res) => {
                self.items = res.data;
            });
        },
        methods: {
        }
    }
</script>

<style scoped>

</style>
