<template>
  <div>
     <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>用户管理</el-breadcrumb-item>
        <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图区 -->
    <el-card>
        <!-- 搜索与添加区域 -->
        <el-row :gutter="20">
            <el-col :span="8">
                <el-input placeholder="请输入内容" v-model="selectInfo.index" clearable @clear="getUseList">
                    <el-button slot="append" icon="el-icon-search" @click="query"></el-button>
                </el-input>
            </el-col>
            <el-col :span="6">
                <el-select v-model="value" placeholder="请选择查询的方式" @change="tt($event)">
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    >
                    </el-option>
                </el-select>
            </el-col>
            <el-col :span="4">
                <el-button type="primary" @click="addDialogVisible=true">添加用户</el-button>
            </el-col>
        </el-row>

        <!-- 用户列表区 -->
        <el-table :data="userlist" border stripe >
            <el-table-column type="index"></el-table-column>
            <el-table-column label="姓名" prop="name"></el-table-column>
            <el-table-column label="出生日期" prop="birthday"></el-table-column>
            <el-table-column label="性别" prop="gender"></el-table-column>
            <el-table-column label="电话" prop="phone"></el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-tooltip effect="dark" content="修改信息" placement="top" :enterable="false">
                        <el-button type="primary" icon="el-icon-edit" @click="showEditDialog(scope.row.id)"></el-button>
                    </el-tooltip>
                    <el-tooltip effect="dark" content="删除信息" placement="top" :enterable="false">
                        <el-button type="danger" icon="el-icon-delete" @click="Delete(scope.row.id)"></el-button>
                    </el-tooltip>
                </template>
            </el-table-column>
        </el-table>
    </el-card>
    <!-- 添加用户的对话框 -->
    <el-dialog
        title="添加用户"
        :visible.sync="addDialogVisible"
        width="50%"
        @close="addDialogClose"
        >
        <el-form ref="addFormRef" :model="addForm" label-width="70px" :rules="addFormRules">
            <el-form-item label="姓名" prop="username">
                <el-input v-model="addForm.username"></el-input>
            </el-form-item>
            <el-form-item label="账号" prop="account">
                <el-input v-model="addForm.account"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="addForm.password"></el-input>
            </el-form-item>
            <el-form-item label="出生日期" prop="birthday">
                <el-input v-model="addForm.birthday"></el-input>
            </el-form-item>
            <el-form-item label="性别" prop="gender">
                <el-input v-model="addForm.gender"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="phone">
                <el-input v-model="addForm.phone"></el-input>
            </el-form-item>
            <el-form-item label="年级" prop="grade">
                <el-input v-model="addForm.grade"></el-input>
            </el-form-item>
            <el-form-item label="学院" prop="school_name">
                <el-input v-model="addForm.school_name"></el-input>
            </el-form-item>
            <el-form-item label="专业" prop="major">
                <el-input v-model="addForm.major"></el-input>
            </el-form-item>
            <el-form-item label="班级" prop="stu_class">
                <el-input v-model="addForm.stu_class"></el-input>
            </el-form-item>
            <el-form-item label="职务" prop="post">
                <el-input v-model="addForm.post"></el-input>
            </el-form-item>
        </el-form>
        <!-- 底部区域 -->
        <span slot="footer" class="dialog-footer">
            <el-button @click="addDialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="addUser">确 定</el-button>
        </span>
    </el-dialog>

    <!-- 修改用户的对话框 -->
    <el-dialog
        title="修改用户"
        :visible.sync="editDialogVisible"
        width="50%"
        @close="editDialogClose"
        >
        <el-form ref="editFormRef" :model="editForm" :rules="editFormRules" label-width="70px">
            <el-form-item label="姓名" prop="username">
                <el-input v-model="editForm.username"></el-input>
            </el-form-item>
            <el-form-item label="出生日期" prop="birthday">
                <el-input v-model="editForm.birthday"></el-input>
            </el-form-item>
            <el-form-item label="性别" prop="gender">
                <el-input v-model="editForm.gender"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="phone">
                <el-input v-model="editForm.phone"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="editDialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="editUserInfo">确 定</el-button>
        </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
    data(){
        //验证出生日期的规则
        var checkBirthday = (rules,value,cb) => {
            const regBirthday = /^((19[2-9]\d{1})|(20((0[0-9])|(1[0-8]))))\-((0?[1-9])|(1[0-2]))\-((0?[1-9])|([1-2][0-9])|30|31)$/
            if(regBirthday.test(value)){
                return cb
            }
            cb(new Error('请输入合法的出生日期'))
        }
        //验证手机号的规则
        var checkPhone = (rules,value,cb)=> {
            //验证手机号的正则表达式
            const regPhone = /^1[3579][456789]\d{8}$/
            if(regPhone.test(value)){
                return cb
            }
            cb(new Error('请输入合法的手机号'))
            }
        return{
            userlist: [],
            result:{delete_id:''},
            selectInfo:{
                select_way:'',
                index:''
            },
            change:{
                select_way:1,
                index:''
            },
            options: [{
                    value: 1,
                    label: 'id查找'
                    }, {
                    value: 2,
                    label: '姓名查找'
                    }, {
                    value: 3,
                    label: '电话查找'
                    }, {
                    value: 4,
                    label: '性别查找'
                    }],
                    value: '',
            addDialogVisible:false,
            //添加用户的表单数据
            addForm:{
                username:'',
                birthday:'',
                gender:'',
                phone:'',
                account:'',
                password:'',
                grade:'',
                shool_name:'',
                major:'',
                stu_class:'',
                post:''
            },
            //添加表单的验证规则对象
            addFormRules:{
                username:[
                    {required: true, message:'请输入用户名', trigger: 'blur'},
                    {min:3,max:10,message:'用户名的长度在3~10个字符之间',trigger:'blur'}
                ],
                account:[
                        {required: true, message:'请输入账号', trigger: 'blur'},
                ],
                password:[
                        {required: true, message:'请输入密码', trigger: 'blur'},
                ],
                birthday:[
                    {required: true, message:'请输入出生日期', trigger: 'blur'},
                    {validator:checkBirthday,trigger:'blur'}
                ],
                gender:[
                        {required: true, message:'请输入性别', trigger: 'blur'},
                ],
                phone:[
                        {required: true, message:'请输入电话', trigger: 'blur'},
                        {validator:checkPhone,trigger:'blur'}
                ],
                grade:[
                    {required: true, message:'请输入性别', trigger: 'blur'},
                ],
                shool_name:[
                    {required: true, message:'请输入性别', trigger: 'blur'},
                ],
                major:[],
                stu_class:[
                    {required: true, message:'请输入性别', trigger: 'blur'},
                ],
                post:[
                    {required: true, message:'请输入性别', trigger: 'blur'},
                ]
            },
            //控制修改用户信息对话框的显示与隐藏
            editDialogVisible:false,
            //查询到的用户信息对象
            editForm:{
                edit_id:'',
                username:'',
                birthday:'',
                gender:'',
                phone:''
            },
            //修改表单的验证规则对象
            editFormRules:{
                username:[
                    {required: true, message:'请输入', trigger: 'blur'}
                ],
                birthday:[
                    {required: true, message:'请输入', trigger: 'blur'}
                ],
                gender:[
                    {required: true, message:'请输入', trigger: 'blur'}
                ],
                phone:[
                    {required: true, message:'请输入', trigger: 'blur'}
                ]
            }
            }
    },
    mounted() {
        this.$nextTick(function(){
            this.getUseList()
        })
    },
    methods: {
         tt(event){
             this.selectInfo.select_way = this.value
        },
        async getUseList(){
            const res = await this.$http.get('api/user/userinfo/allinfo')
            this.userlist = res.data
        },
        /* 查询 */
        async query(){
            const queryResult = await this.$http.post('api/user/userinfo/select',this.selectInfo)
            this.userlist = queryResult.data
        },
        async Delete(id){
            const confirmResult= await this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
                                    confirmButtonText: '确定',
                                    cancelButtonText: '取消',
                                    type: 'warning'
                        }).catch(err => {
                            return err
                        })
                        if(confirmResult !== 'confirm'){
                            return this.$message.info('已经取消删除')
                        }
                        this.result.delete_id = id
                        const res =  await this.$http.post('api/user/userinfo/delete',this.result)
                        if(res.status !== 200){
                            alert(result.delete_id)
                        }
                        this.$message.success('删除用户成功!')
                        this.getUseList()

        },
        //监听添加用户对话框的关闭事件
        addDialogClose(){
            this.$refs.addFormRef.resetFields()
        },
        //点击按钮添加新用户
        async addUser(){
                //可以发起添加用户的网络请求
                const res = await this.$http.post('api/user/userinfo/add',this.addForm)
                if(res.status !== 200){
                    this.$message.error('添加用户失败！')
                }
                this.$message.success('添加用户成功！')
                //隐藏添加用户的对话框
                this.addDialogVisible = false
                //重新获取用户的列表
                this.getUseList()
        },
        //展示编辑用户的对话框
        async showEditDialog(id){
            this.change.index = id
            const res = await this.$http.post('api/user/userinfo/select',this.change)
            if(res.status !== 200){
                return this.$message.error('查询用户信息失败')
            }
            this.editForm.edit_id = res.data[0]['id']
            this.editForm.username = res.data[0]['name']
            this.editForm.birthday = res.data[0]['birthday']
            this.editForm.gender = res.data[0]['gender']
            this.editForm.phone = res.data[0]['phone']
            this.editDialogVisible = true 
        },
        //监听修改用户对话框的关闭事件
        editDialogClose(){
            this.$refs.editFormRef.resetFields()
        },
        //修改用户信息并提交
        async editUserInfo(){
            const res =  await this.$http.post('api/user/userinfo/edit',this.editForm)
            if(res.status !== 200){
                return this.$message.error('更新用户信息失败')
            }
            //关闭对话框
            this.editDialogVisible = false
            //刷新数据列表
            this.getUseList()
            //提示修改成功
            this.$message.success('更新用户信息成功')
        }
    },
}
</script>

<style lang="less" scoped>

</style>