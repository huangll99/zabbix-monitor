<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-date"></i> 表单</el-breadcrumb-item>
                <el-breadcrumb-item>Agent部署</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="form-box">
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="主机名">
                    <el-input v-model="form.hostname"></el-input>
                </el-form-item>
                <el-form-item label="主机密码">
                    <el-input v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item label="主机组">
                    <el-select v-model="form.group" placeholder="请选择">
                        <el-option v-for="item in group" :key="item.groupid" :label="item.name" :value="item.groupid"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="主机Host">
                    <el-input v-model="form.host"></el-input>
                </el-form-item>
                <el-form-item label="主机IP">
                    <el-input v-model="form.ip"></el-input>
                </el-form-item>
                <el-form-item label="模板">
                    <el-select v-model="form.template" placeholder="请选择" >
                        <el-option v-for="item in templates" :key="item.templateid" :label="item.name" :value="item.templateid"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                    <el-button>取消</el-button>
                </el-form-item>
            </el-form>
        </div>

    </div>
</template>

<script>

    export default {
        data: function () {
            return {
                form: {
                    hostname: '',
                    group: '',
                    host: '',
                    ip: '0.0.0.0',
                    template: '',
                    password:''
                },
                group:[],
                templates:[]
            }
        },
        methods: {
            onSubmit() {
                let self = this;
                this.$http.post('/api/deploy/',this.form)
                    .then(function (res) {
                        self.$message.success('提交成功！');
                    })
            }
        },
        created() {
            let self = this;
            self.$http.get('/api/groups/').then((res) => {
                self.group = res.data;
            });
            self.$http.get('/api/template/').then((res) => {
                self.templates = res.data;
            });
        }
    }
</script>
