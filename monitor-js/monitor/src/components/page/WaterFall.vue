<template>
    <div>
        <div class="water">
            <div class="crumbs">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item><i class="el-icon-menu"></i> 主机</el-breadcrumb-item>
                    <el-breadcrumb-item>主机列表</el-breadcrumb-item>
                </el-breadcrumb>
            </div>
            <waterfall :lineGap="230" :watch="tableData">
                <waterfall-slot  :order="index" :key="host.host" :height="200" :width="200" v-for="(host,index) in tableData" >
                    <div style="padding: 10px;width: 200px;height: 200px;">
                       <div style="height: 200px;border-radius: 90px;text-align: center;line-height:200px;background-color: rgba(209,94,16,0.65);color: #000;">

                           <router-link :to="{path:'hostDetail',query:{hostid:host.hostid}}">{{host.name}}</router-link>
                       </div>
                    </div>
                </waterfall-slot>
            </waterfall>
        </div>
    </div>
</template>

<script>
    import Waterfall from 'vue-waterfall/lib/waterfall.vue'
    import WaterfallSlot from 'vue-waterfall/lib/waterfall-slot.vue'

    import vueFlashCard from 'vue-flashcard'

    export default {
        components:{
            Waterfall,
            WaterfallSlot,
            vueFlashCard
        },
        data() {
            return {
                url: './static/vuetable.json',
                tableData: [],
                cur_page: 1,
                multipleSelection: [],
                select_cate: '',
                select_word: '',
                del_list: [],
                is_search: false,
                loading: true
            }
        },
        created() {
            this.getData();
        },
        methods: {
            handleCurrentChange(val) {
                this.cur_page = val;
                this.getData();
            },
            getData() {
                let self = this;

                self.$http.get('/api/hosts/').then((res) => {
                    self.tableData = res.data;
                    self.loading = false
                })
            },
            search() {
                this.is_search = true;
            },
            formatter(row, column) {
                return row.address;
            },
            filterTag(value, row) {
                return row.tag === value;
            },
            hostDetail(index, row) {
                this.$router.push({
                    path: 'hostDetail',
                    query: {
                        hostid: row.hostid,
                        hostname: row.name
                    }
                })
            },
            handleDelete(index, row) {
                this.$message.error('删除第' + (index + 1) + '行');
            },
            delAll() {
                const self = this,
                    length = self.multipleSelection.length;
                let str = '';
                self.del_list = self.del_list.concat(self.multipleSelection);
                for (let i = 0; i < length; i++) {
                    str += self.multipleSelection[i].name + ' ';
                }
                self.$message.error('删除了' + str);
                self.multipleSelection = [];
            },
            handleSelectionChange(val) {
                this.multipleSelection = val;
            }
        }
    }
</script>

<style scope>
    .water a{
        color: #0e17ff;
        font-size:16px;
    }
</style>
