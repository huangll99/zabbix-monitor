<template>
    <div class="group">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 主机组</el-breadcrumb-item>
                <el-breadcrumb-item>组列表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div>
            <template v-for="(group,index) in tableData">
                <i-circle v-if="index%3==0" :size=160 class="circle" :percent="100" stroke-color="green">
                    <h2>主机组ID: {{group.groupid}}</h2>
                    <p style="padding-top: 15px;">{{group.name}}</p>
                </i-circle>
                <i-circle  v-if="index%3==1" :size=160 class="circle" :percent="100" stroke-color="red">
                    <h2>主机组ID: {{group.groupid}}</h2>
                    <p style="padding-top: 15px;">{{group.name}}</p>
                </i-circle>
                <i-circle  v-if="index%3==2" :size=160 class="circle" :percent="100" stroke-color="yellow">
                    <h2>主机组ID: {{group.groupid}}</h2>
                    <p style="padding-top: 15px;">{{group.name}}</p>
                </i-circle>
            </template>
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
                is_search: false
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
                self.$http.get('/api/groups/').then((res) => {
                    self.tableData = res.data;
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
                //this.$message('编辑第'+(index+1)+'行');
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

<style scoped>
    .circle {
        margin: 30px;
    }
</style>
