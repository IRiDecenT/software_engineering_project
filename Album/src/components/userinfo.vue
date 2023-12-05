<!-- eslint-disable vue/multi-word-component-names -->
<script setup>
import { reactive, ref } from 'vue'
const avatar = "../../public/avator1.JPG"
const nickname = "能不能出现在我想要的地方"
const design = "能不能别发警告了"
const form = reactive({
    name: '',
    region: '',
    date1: '',
    date2: '',
    delivery: false,
    type: [],
    resource: '',
    desc: '',
})

const modify = ref(false)
console.log(modify.value)
const onSubmit = () => {
    console.log('submit!')
}
function changeInformation() {
    console.log("changeUserInformation")
    modify.value = !modify.value
    console.log(modify.value)
}
function changeAvatar() {
    console.log("changeAvatar")
}
</script>


<template>
    <div class="info">
        <div class="container">
            <div class="topBox">
                <el-card class="topBox">
                    <el-upload class="topBoxImg" @click="changeAvatar()">
                        <img v-if="avatar" :src="avatar" v-image-preview>
                        <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
                    </el-upload>
                    <div class="topBoxText">
                        <div class="nicknameBox">{{ nickname }}</div>
                        <div class="designBox">{{ design }}</div>
                    </div>
                </el-card>
            </div>
            <el-divider />
            <div class="mainBox">
                <div v-if="modify">
                    <el-card>
                        <el-form :model="form" label-width="120px">
                            <el-form-item label="信息1">
                                <el-input v-model="form.name" />
                            </el-form-item>
                            <el-form-item label="信息2">
                                <el-select v-model="form.region" placeholder="please select your zone">
                                    <el-option label="Zone one" value="shanghai" />
                                    <el-option label="Zone two" value="beijing" />
                                </el-select>
                            </el-form-item>
                            <el-form-item label="Activity time">
                                <el-col :span="11">
                                    <el-date-picker v-model="form.date1" type="date" placeholder="Pick a date"
                                        style="width: 100%" />
                                </el-col>
                                <el-col :span="2" class="text-center">
                                    <span class="text-gray-500">-</span>
                                </el-col>
                                <el-col :span="11">
                                    <el-time-picker v-model="form.date2" placeholder="Pick a time" style="width: 100%" />
                                </el-col>
                            </el-form-item>
                            <el-form-item label="Instant delivery">
                                <el-switch v-model="form.delivery" />
                            </el-form-item>
                            <el-form-item label="Activity type">
                                <el-checkbox-group v-model="form.type">
                                    <el-checkbox label="Online activities" name="type" />
                                    <el-checkbox label="Promotion activities" name="type" />
                                    <el-checkbox label="Offline activities" name="type" />
                                    <el-checkbox label="Simple brand exposure" name="type" />
                                </el-checkbox-group>
                            </el-form-item>
                            <el-form-item label="Resources">
                                <el-radio-group v-model="form.resource">
                                    <el-radio label="Sponsor" />
                                    <el-radio label="Venue" />
                                </el-radio-group>
                            </el-form-item>
                            <el-form-item label="Activity form">
                                <el-input v-model="form.desc" type="textarea" />
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="onSubmit">确定</el-button>
                                <el-button @click="changeInformation">取消</el-button>
                            </el-form-item>
                        </el-form>
                    </el-card>
                </div>
                <div v-else>
                    <el-card>
                        <el-descriptions class="margin-top" title="用户信息" :column="3" :size="size" border>
                            <template #extra>
                                <el-button type="primary" @click="changeInformation">修改</el-button>
                            </template>
                            <el-descriptions-item>
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon :style="iconStyle">
                                            <user />
                                        </el-icon>
                                        用户名
                                    </div>
                                </template>
                                {{ nickname }}
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon :style="iconStyle">
                                            <iphone />
                                        </el-icon>
                                        电话
                                    </div>
                                </template>
                                18100000000
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon :style="iconStyle">
                                            <location />
                                        </el-icon>
                                        所在地
                                    </div>
                                </template>
                                Suzhou
                            </el-descriptions-item>

                            <el-descriptions-item>
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon :style="iconStyle">
                                            <tickets />
                                        </el-icon>
                                        Remarks
                                    </div>
                                </template>
                                School
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon :style="iconStyle">
                                            <office-building />
                                        </el-icon>
                                        Address
                                    </div>
                                </template>
                                No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province
                            </el-descriptions-item>
                        </el-descriptions>
                    </el-card>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
.info {
    margin-top: 65px;
    width: 100vw;
    display: flex;
    justify-content: center;
    overflow-y: auto;
}

.container {
    width: 80vw;
    height: 90vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    user-select: none;

}

.topBox {
    display: flex;
    width: 80%;
    height: 400px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.topBoxImg {
    width: 200px;
    cursor: pointer;
    overflow: hidden;
    border-radius: 50%;
    height: 200px;
    text-align: center;
    background-color: rgba(0, 0, 0, 0.5);
    opacity: 1;
    line-height: 200px;
}

.topBoxImg:hover {
    width: 200px;
    height: 200px;
    opacity: 0.8;
    color: #fff;
}

.topBoxImg img {
    width: 200px;
    overflow: hidden;
    border-radius: 50%;
}

.topBoxText {
    padding-top: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.topBoxText .nicknameBox {
    font-weight: bold;
    color: #fff;
    padding-bottom: 10px;
}

.topBoxText .designBox {
    color: rgba(193, 185, 185, 0.9);
}

.img {
    width: 80px;
    height: 80px;
}

:deep(.el-card) {
    width: 80vw;
    background-color: inherit;
}

:deep(.el-descriptions__title) {
    color: #fff;
}

:deep(.el-descriptions__body) {
    background-color: inherit;
}

:deep(.el-descriptions__label.el-descriptions__cell.is-bordered-label) {
    background: inherit;
}

:deep(.el-descriptions__content.el-descriptions__cell.is-bordered-content) {
    color: #ffffffc3;
}

:deep(.cell-item) {
    color: #fff;
}
</style>
