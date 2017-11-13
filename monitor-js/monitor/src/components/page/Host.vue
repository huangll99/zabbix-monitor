<template>
    <div>
        <div class="table">
            <div class="crumbs">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item><i class="el-icon-menu"></i> 主机</el-breadcrumb-item>
                    <el-breadcrumb-item>主机列表</el-breadcrumb-item>
                </el-breadcrumb>
            </div>
            <el-table v-loading.body="loading" :data="tableData" border style="width:100%" ref="multipleTable"
                      @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="50"></el-table-column>
                <el-table-column prop="hostid" label="主机ID" sortable width="100">
                </el-table-column>
                <el-table-column prop="name" label="主机名称" sortable width="400">
                </el-table-column>
                <el-table-column label="所在组" width="400">
                    <template scope="scope">
                        <span style="border: 1px dotted #ff22f3;margin-left: 5px;padding: 2px"
                              v-for="group in scope.row.groups">{{group.name}}  </span>
                    </template>
                </el-table-column>
                <el-table-column prop="host" label="host" sortable width="200">
                </el-table-column>
                <el-table-column label="主机状态" width="200">
                    <template scope="scope">

                        <el-button v-if="scope.row.available == 1" size="small" type="success"><i
                            class="el-icon-check"></i>可用
                        </el-button>
                        <el-button v-if="scope.row.available == 0" size="small" type="danger"><i
                            class="el-icon-close"></i>未知
                        </el-button>
                        <el-button v-if="scope.row.available == 2" size="small" type="danger"><i
                            class="el-icon-close"></i> 失效
                        </el-button>
                    </template>
                </el-table-column>
                <el-table-column label="操作" width="200">
                    <template scope="scope">
                        <el-button size="small" type="info"
                                   @click="hostDetail(scope.$index, scope.row)">监控详情
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>

        </div>

    </div>


</template>

<script>
    export default {
        data() {
            return {
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

<style slot-scope>
    .handle-box {
        margin-bottom: 20px;
    }

    .handle-select {
        width: 120px;
    }

    .handle-input {
        width: 300px;
        display: inline-block;
    }
</style>
