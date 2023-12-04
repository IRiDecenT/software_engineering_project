<script setup>
import ChangeAvatar from '@/components/ChangeAvatar.vue'
import { ref } from 'vue'
import { getUserInfo } from '@/api/user'
import { useRoute, useRouter } from 'vue-router';
import {
    Management,
    Promotion,
    UserFilled,
    User,
    Crop,
    EditPen,
    SwitchButton,
    CaretBottom,
} from '@element-plus/icons-vue'
const userInfo = ref({
    id: 0,
    username: 'YR',
    nickname: 'YR',
    email: '3360910573@qq.com',
})
const rules = {
    nickname: [
        { required: true, message: '请输入用户昵称', trigger: 'blur' },
        {
            pattern: /^\S{2,10}$/,
            message: '昵称必须是2-10位的非空字符串',
            trigger: 'blur'
        }
    ],
    email: [
        { required: true, message: '请输入用户邮箱', trigger: 'blur' },
        { type: 'email', message: '邮箱格式不正确', trigger: 'blur' }
    ]
}
const route = useRoute()
const router = useRouter()
// const uid = route.params.uid
const uid = route.query.uid
console.log(uid)
const toHome = () => {
  router.push(`/index?uid=${uid}`)
}

let avatar = ref(null)
async function getUserData(){
	let result = await getUserInfo(uid)
	console.log(result)
	avatar.value = result.avatar
}
getUserData()

</script>
<template>
    <el-container class="layout-container">
        <!-- 左侧菜单 -->
        <el-aside width="200px">
            <div class="el-aside__logo"></div>
            <el-menu active-text-color="#ffd04b" background-color="#c6e2ff" text-color="#000000" router>
                <el-menu-item @click="toHome">
                    <el-icon>
                        <Management />
                    </el-icon>
                    <span>首页</span>
                </el-menu-item>
                <el-menu-item @click="toDemo">
                    <el-icon>
                        <Promotion />
                    </el-icon>
                    <span>相册管理</span>
                </el-menu-item>
                <el-menu-item>
                    <el-icon>
                        <Promotion />
                    </el-icon>
                    <span>图片管理</span>
                </el-menu-item>
                <el-sub-menu>
                    <template #title>
                        <el-icon>
                            <UserFilled />
                        </el-icon>
                        <span>个人中心</span>
                    </template>
                    <el-menu-item>
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>基本资料</span>
                    </el-menu-item>
                    <el-menu-item>
                        <el-icon>
                            <Crop />
                        </el-icon>
                        <span>更换头像</span>
                    </el-menu-item>
                    <el-menu-item>
                        <el-icon>
                            <EditPen />
                        </el-icon>
                        <span>重置密码</span>
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <!-- 右侧主区域 -->
        <el-container>
            <!-- 头部区域 -->
            <el-header>
                <el-text style="margin-right: auto;" tag="b" size="large" type="success">电子相册系统</el-text>
                <el-input v-model="searchInfo" autosize placeholder="搜索" style="width: 700px"> </el-input>
                <el-button round style="margin-right: auto;">搜索</el-button>
                <el-dropdown placement="bottom-end">
                    <span class="el-dropdown__box">
                        <el-avatar @click="toInfo" :src="avatar" />
                        <el-icon>
                            <CaretBottom />
                        </el-icon>
                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item command="profile" :icon="User">基本资料</el-dropdown-item>
                            <el-dropdown-item command="avatar" :icon="Crop">更换头像</el-dropdown-item>
                            <el-dropdown-item command="password" :icon="EditPen">重置密码</el-dropdown-item>
                            <el-dropdown-item command="logout" :icon="SwitchButton">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </el-header>
            <!-- 中间区域 -->
            <el-main>
                <el-card class="page-container">
                    <div class="header">
                        <span>基本资料</span>
                    </div>
                    <el-row>
                        <el-col :span="12">
                            <el-form :model="userInfo" :rules="rules" label-width="100px" size="large">
                                <el-form-item label="用户头像">
                                    <el-avatar :src="avatar" />
                                </el-form-item>
                                <el-form-item label="登录名称">
                                    <el-input v-model="userInfo.username" disabled></el-input>
                                </el-form-item>
                                <el-form-item label="用户昵称" prop="nickname">
                                    <el-input v-model="userInfo.nickname"></el-input>
                                </el-form-item>
                                <el-form-item label="用户邮箱" prop="email">
                                    <el-input v-model="userInfo.email"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary">提交修改</el-button>
                                </el-form-item>
                            </el-form>
                        </el-col>
                    </el-row>
                </el-card>
                <ChangeAvatar />
            </el-main>
            <!-- 底部区域 -->
            <el-footer>电子相册系统 ©2023 Created by YR</el-footer>
        </el-container>
    </el-container>
</template>

<style lang="scss" scoped>
.elcard {
    width: 260px;
    height: auto;
}


.layout-container {
    height: 100vh;

    .el-aside {
        background-color: #ffffff;

        &__logo {
            height: 60px;
            background: url('@/assets/logo3.png') no-repeat center / 120px auto;
        }

        .el-menu {
            border-right: none;
        }
    }

    .el-main {
        background-color: aliceblue;
    }

    .el-header {
        background-color: dodgerblue;
        display: flex;
        align-items: center;
        justify-content: space-between;

        .el-dropdown__box {
            display: flex;
            align-items: center;

            .el-icon {
                color: #999;
                margin-left: 10px;
            }

            &:active,
            &:focus {
                outline: none;
            }
        }
    }

    .el-footer {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        color: #666;
    }
}

.time {
    font-size: 12px;
    color: #7e7c7c;
    margin-right: 0%;
}

.bottom {
    margin-top: 5px;
    line-height: 12px;
    //display: flex;
    justify-content: space-between;
    //align-items: center;
}

.button {
    padding: 0;
    min-height: auto;
}

.image {

    width: 100%;
    display: block;
}
</style>