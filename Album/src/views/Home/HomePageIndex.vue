<script setup>
import { ref } from 'vue'
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
import { useRoute, useRouter } from 'vue-router';
// const currentDate = ref(new Date())
const route = useRoute()
const router = useRouter()
const searchInfo = ref('')
const imageData = ref(
	[
		[
			{
				id: 1,
				title: '陶喆蓝专',
				time: '2023.11.20',
				img: '/src/assets/res8.PNG',
				avatar: '/src/assets/avator1.JPG',
				alaum: 'Music',
				poster: 'YR',
			},
			{
				id: 2,
				title: '维维道来',
				time: '2023.11.20',
				img: '/src/assets/res2.JPG',
				avatar: '/src/assets/avator2.JPG',
				alaum: '这就是中国',
				poster: 'YR',
			},
			{
				id: 3,
				title: '好想成为玛琪玛小姐的狗啊',
				time: '2023.11.20',
				img: '/src/assets/res3.JPG',
				avatar: '/src/assets/avator3.JPG',
				alaum: '二次元',
				poster: 'YR',
			},
			{
				id: 4,
				title: '艾尔登之王',
				time: '2023.11.20',
				img: '/src/assets/res4.PNG',
				avatar: '/src/assets/avator1.JPG',
				alaum: '艾尔登法环',
				poster: 'YR',
			}
		],
		[
			{
				id: 5,
				title: '菈妮小姐',
				time: '2023.11.20',
				img: '/src/assets/res5.JPG',
				avatar: '/src/assets/avator1.JPG',
				alaum: '艾尔登法环',
				poster: 'YR',
			},
			{
				id: 6,
				title: '武汉城门',
				time: '2023.11.20',
				img: '/src/assets/res6.JPG',
				avatar: '/src/assets/avator3.JPG',
				alaum: '武汉行',
				poster: 'YR',
			},
			{
				id: 7,
				title: '晴川阁',
				time: '2023.11.20',
				img: '/src/assets/res7.JPG',
				avatar: '/src/assets/avator3.JPG',
				alaum: '武汉行',
				poster: 'YR',
			},
			{
				id: 8,
				title: '快和丁真来学习',
				time: '2023.11.20',
				img: '/src/assets/res1.JPG',
				avatar: '/src/assets/avator3.JPG',
				alaum: '纯真男孩',
				poster: 'YR',
			}
		],
		[
			{
				id: 1,
				title: '陶喆蓝专',
				time: '2023.11.20',
				img: '/src/assets/res8.PNG',
				avatar: '/src/assets/avator1.JPG',
				alaum: 'Music',
				poster: 'YR',
			},
			{
				id: 2,
				title: '维维道来',
				time: '2023.11.20',
				img: '/src/assets/res2.JPG',
				avatar: '/src/assets/avator2.JPG',
				alaum: '这就是中国',
				poster: 'YR',
			},
			{
				id: 3,
				title: '好想成为玛琪玛小姐的狗啊',
				time: '2023.11.20',
				img: '/src/assets/res3.JPG',
				avatar: '/src/assets/avator3.JPG',
				alaum: '二次元',
				poster: 'YR',
			},
			{
				id: 4,
				title: '艾尔登之王',
				time: '2023.11.20',
				img: '/src/assets/res4.PNG',
				avatar: '/src/assets/avator1.JPG',
				alaum: '艾尔登法环',
				poster: 'YR',
			}
		],
	]
)

const uid = route.params.id
console.log(uid)

const toDemo = () => {
	router.push(`/demo/uid=${uid}`)
}

</script>

<template>
	<el-container class="layout-container">
		<!-- 左侧菜单 -->
		<el-aside width="200px">
			<div class="el-aside__logo"></div>
			<el-menu active-text-color="#ffd04b" background-color="#c6e2ff" text-color="#000000" router>
				<el-menu-item>
					<el-icon>
						<Management />
					</el-icon>
					<span>首页</span>
				</el-menu-item>
				<el-menu-item  @click="toDemo">
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
						<el-avatar src="/src/assets/avator1.JPG" />
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
				<div style="width: auto; height: auto;">
					<el-row v-for="(col, index) in imageData" :key="index" span="1" :gutter="20" style="margin-bottom: 10px;">
						<el-col v-for="(image, index) in col" :key="image.id" :span="4" :offset="index > 0 ? 2 : 1">
							<el-card :body-style="{ padding: '0px' }" class="elcard">
								<el-image :src="image.img" class="image" :fit="fit" :preview-src-list="[image.img]" />
								<div style="padding: 5px">
									<el-text tag="b" size="large">{{ image.title }}</el-text>
									<div>
										<el-text class="mx-1" type="info">相册：[{{ image.alaum }}]</el-text>
									</div>
									<div class="bottom">
										<el-row>
											<el-col span="4">
												<el-avatar :src=image.avatar />
											</el-col>
											<el-col span="20">
												<el-row style="margin-top: 5px;">
													<el-text tag="b" type="primary">{{ image.poster }}</el-text>
												</el-row>
												<el-row>
													<el-text class="time">{{ image.time }}</el-text>
													<el-button style="margin-left: 80px;">
														点赞
													</el-button>
												</el-row>
											</el-col>
										</el-row>
									</div>
								</div>
							</el-card>
						</el-col>
					</el-row>
				</div>
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