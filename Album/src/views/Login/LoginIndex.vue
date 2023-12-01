<script setup>
import { User, Lock } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus';
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { userRegister, userLogin } from '@/api/user'

//控制注册与登录表单的显示， 默认显示注册
const isRegister = ref(false)

const router = useRouter()//路由跳转

// 登陆表单
const formLogin = ref({
    username: '',
    password: '',
    agree: false
})

// 注册表单
const formRegister = ref({
    username: '',
    password: '',
    rePassword: ''
})

const clearFormRegister = () => {
    formRegister.value.username = ''
    formRegister.value.password = ''
    formRegister.value.rePassword = ''
}

const clearFormLogin = () => {
    formLogin.value.username = ''
    formLogin.value.password = ''
}

const doLogin = async () => {
    const { username, password } = formLogin.value
    if (!username || !password) {
        ElMessage({
            message: '用户名或密码不能为空',
            type: 'error'
        })
        return
    }
    // 发起请求
    let result = await userLogin({ username, password })
    if (result.code !== 200) {
        ElMessage({
            message: result.msg,
            type: 'error'
        })
        clearFormLogin()
        return
    }
    else {
        ElMessage({
            message: '登录成功',
            type: 'success'
        })
        router.replace(`/index/uid=${result.id}`)
    }

}

const doRegister = async () => {
    const { username, password, rePassword } = formRegister.value
    if (!username || !password || !rePassword) {
        ElMessage({
            message: '用户名或密码不能为空',
            type: 'error'
        })
        return
    }
    if (password !== rePassword) {
        ElMessage({
            message: '两次密码不一致',
            type: 'error'
        })
        return
    }
    // 发起请求
    let result = await userRegister({ username, password })
    if (result.code !== 200) {
        ElMessage({
            message: result.msg,
            type: 'error'
        })
    }
    else {
        ElMessage({
            message: '注册成功',
            type: 'success'
        })
        isRegister.value = false
    }
    clearFormRegister()
}
</script>



<template>
    <el-row class="login-page">
        <el-col :span="13" class="bg"></el-col>
        <el-col :span="6" :offset="3" class="form">
            <!-- 注册表单 -->
            <el-form ref="form" size="large" autocomplete="off" v-if="isRegister">
                <el-image src="src/assets/logo3.png" class="logo" alt="Logo" />
                <el-card class="box-card">
                    <el-form-item>
                        <h1 class="headtitle">注册</h1>
                    </el-form-item>
                    <el-form-item>
                        <el-input :prefix-icon="User" placeholder="请输入用户名" v-model="formRegister.username"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-input :prefix-icon="Lock" type="password" placeholder="请输入密码"
                            v-model="formRegister.password"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-input :prefix-icon="Lock" type="password" placeholder="请输入再次密码"
                            v-model="formRegister.rePassword"></el-input>
                    </el-form-item>
                    <!-- 注册按钮 -->
                    <el-form-item>
                        <el-button class="button" type="primary" auto-insert-space @click="doRegister">
                            注册
                        </el-button>
                    </el-form-item>
                    <el-form-item class="flex">
                        <el-link type="info" :underline="false" @click="isRegister = false">
                            ← 返回
                        </el-link>
                    </el-form-item>
                </el-card>
            </el-form>

            <!-- 登录表单 -->
            <el-form ref="form" size="large" autocomplete="off" v-else>
                <el-image src="src/assets/logo3.png" class="logo" alt="Logo" />
                <el-card class="box-card">
                    <el-form-item>
                        <h1 class="headtitle">登录</h1>
                    </el-form-item>
                    <el-form-item>
                        <el-input :prefix-icon="User" placeholder="请输入用户名" v-model="formLogin.username"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-input name="password" :prefix-icon="Lock" type="password" placeholder="请输入密码"
                            v-model="formLogin.password"></el-input>
                    </el-form-item>
                    <el-form-item class="flex">
                        <div class="flex">
                            <el-checkbox>记住我</el-checkbox>
                            <el-link type="primary" :underline="false">忘记密码？</el-link>
                        </div>
                    </el-form-item>
                    <!-- 登录按钮 -->
                    <el-form-item>
                        <el-button class="button" type="primary" auto-insert-space @click="doLogin">登录</el-button>
                    </el-form-item>
                    <el-form-item class="flex">
                        <el-link type="info" :underline="false" @click="isRegister = true">
                            注册 →
                        </el-link>
                    </el-form-item>
                </el-card>
            </el-form>
        </el-col>
    </el-row>
</template>

<style lang="scss" scoped>
.box-card {
    width: 480px;
    margin-left: auto;
    margin-right: auto;
}

.logo {
    height: auto;
    margin-bottom: 100px;
    margin-left: 50px;
    margin-right: auto;
    width: 350px;
    height: auto;
}

/* 样式 */
.login-page {
    height: 100vh;
    background-color: #ffffff;

    .bg {
        background:
            url('@/assets/bg1.jpg') no-repeat center / cover;
        border-radius: 0 20px 20px 0;
    }

    .form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        user-select: none;

        .title {
            margin: 0 auto;
        }

        .button {
            width: 100%;
        }

        .flex {
            width: 100%;
            display: flex;
            justify-content: space-between;
        }
    }

    .headtitle {
        font-size: 30px;
        font-weight: 700;
        color: #131212;

        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
    }
}</style>