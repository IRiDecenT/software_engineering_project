<script setup>
import { ref, onMounted, onUnmounted, onActivated } from 'vue'
import axios from "axios"
let imgData = ref([])
let loading = false
let ScrollTop = ref(0)
Loading()

function Loading() {
	if (loading) return;
	loading = true;
	console.log('load');
	axios("/data.json").then((res) => {
		console.log(res.data);
		imgData.value = imgData.value.concat(res.data);
		loading = false;
	})
}
function scrollHandler() {

	const scrollHeight = document.getElementsByClassName('container')[1].scrollHeight;
	const scrollTop = document.getElementsByClassName('container')[1].scrollTop || document.documentElement.scrollTop;
	const clientHeight = document.documentElement.clientHeight;
	const distance = scrollHeight - scrollTop - clientHeight;
	ScrollTop.value = scrollTop;

	if (distance < 200) {
		Loading()
	}
}

function showImage(){
	console.log('弹出照片详情及评论页')
}

onActivated(() => {

})
onMounted(() => {

	console.log(ScrollTop.value);
	window.addEventListener("scroll", scrollHandler, true);
})
onUnmounted(() => {
	console.log('unMounted')
	window.removeEventListener("scroll", scrollHandler, true);
})
</script>

<template>
	<div class="container">
		<div class="background">
			<div class="shell">
				<!-- eslint-disable-next-line vue/valid-v-for -->
				<el-card :body-style="{ padding: '0px' }" v-for="image in imgData" class="image">
					<el-image :src="image.img" :preview-src-list="[image.img]" />
					<div style="padding: 14px">
						<span>{{image.title}}</span>
						<div class="bottom">
							<time class="time">{{ image.time }}</time>
							<el-button type="primary" class="button" @click="showImage">查看</el-button>

						</div>
					</div>
				</el-card>
			</div>
		</div>

	</div>
</template>

<style scoped>
.container {
	width: 100%;
	height: 100vh;
	overflow-y: auto;
	overflow-x: hidden;
	padding-top: 65px;
}

.background {
	color: #000;
	width: 100vw;
	display: flex;
	justify-content: center;
}

.shell {
	max-width: 80%;
	column-count: 5;
	column-gap: 15px;
}

.image {
	user-select: none;
	margin-bottom: 15px;
}

.image img {
	width: 100%;
}

:root(.el-card) {
	margin-top: 10px;
}

.time {
	font-size: 12px;
	color: #999;
}

.bottom {
	margin-top: 13px;
	line-height: 12px;
	display: flex;
	justify-content: space-between;
	align-items: center;
}
.button {
  padding: 0 5px 0;
  min-height: auto;
}


@media (max-width:1200px) {
	.shell {
		column-count: 4;
	}
}

@media (max-width:850px) {
	.shell {
		column-count: 3;
	}
}

@media (max-width:600px) {
	.shell {
		column-count: 2;
	}
}
</style>