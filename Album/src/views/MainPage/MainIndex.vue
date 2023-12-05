<script setup>
import { RouterLink, RouterView, useRouter, useRoute } from 'vue-router'
import {ref} from 'vue'
//需要获取user信息
const userId = ref(1)


// function showComponent(Component){
// 	console.log(Component);
// }

const router = useRouter()
const route = useRoute()
const curpath = route.path
if(curpath === '/main'){
    router.push(`/main/welcome?uid=${userId.value}`)
}


</script>

<template>
	<div>
		<header class="nav-bar">
			<div class="NavBar">
				<div class="container">
						<!--标签-->
					<a class="NavBarTitle" href="/main">
						<!-- <svg class="logo" viewbox="0 0 100 100" width="25" height="25"></svg> -->
						<span class="text">相册管理系统</span>
					</a>
					<div class="content">
						<div class="NavBarSearch">
							<div id="docsearch">
								<button type="button" class="DocSearch DocSearch-Button" aria-label="search">
									<span class="DocSearch-Button-Container">
										<svg width="20" height="20" class="DocSearch-Search-Icon" viewBox="0 0 20 20">
											<path d="M14.386 14.386l4.0877 4.0877-4.0877-4.0877c-2.9418 2.9419-7.7115 2.9419-10.6533 0-2.9419-2.9418-2.9419-7.7115 0-10.6533 2.9418-2.9419 7.7115-2.9419 10.6533 0 2.9419 2.9418 2.9419 7.7115 0 10.6533z"
											stroke="currentColor" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path>
										</svg>
										<span class="DocSearch-Button-Placeholder">Search</span>
									</span>
									<span class="DocSearch-Button-Keys">
										<kbd class="DocSearch-Button-key">
											<svg width="15" height="15" class="DocSearch-Control-Key-Icon">
												<path d="M4.505 4.496h2M5.505 5.496v5M8.216 4.496l.055 5.993M10 7.5c.333.333.5.667.5 1v2M12.326 4.5v5.996M8.384 4.496c1.674 0 2.116 0 2.116 1.5s-.442 1.5-2.116 1.5M3.205 9.303c-.09.448-.277 1.21-1.241 1.203C1 10.5.5 9.513.5 8V7c0-1.57.5-2.5 1.464-2.494.964.006 1.134.598 1.24 1.342M12.553 10.5h1.953"
												stroke-width="1.2" stroke="currentColor" fill="none" stroke-linecap="square"></path>
											</svg>
										</kbd>
										<kbd class="DocSearch-Button-key">K</kbd>
									</span>
								</button>
							</div>
						</div>
						<nav class="NavBarMenu">
							<RouterLink :to= "{path:`/main/welcome?uid=${userId}`}" class="NavBarMenuLink">首页</RouterLink>
							<!--<RouterLink to="/albumManagement" class="NavBarMenuLink">相册管理</RouterLink>-->
							<!--这个是否应该放在相册管理中-->
							<RouterLink to="/main/imagewaterfall" class="NavBarMenuLink">发现更多</RouterLink>
							<RouterLink to="/photoManagement" class="NavBarMenuLink">照片管理</RouterLink>
							<RouterLink to="/" class="NavBarMenuLink">退出登陆</RouterLink>
							<RouterLink :to="{path:`/main/userInfo/?uid=${userId}`}" class="NavBarMenuLink">
								<div class="avator">
									<img src="/src/assets/avator1.JPG">
								</div>
							</RouterLink>
						</nav>
					</div>
				</div>
			</div>
		</header>
		<div class="VPContent">
			<router-view v-slot="{ Component }" >
				<keep-alive>
					<component :is="Component"/>
				</keep-alive>
			</router-view>
		</div>
	</div>



</template>

<style scoped>

html, body, #app {
  width: 100%;
  margin: 0;
  padding: 0;
}

.MainIndex{
	display: flex;
    flex-direction: column;
    min-height: 100vh;
    background-color: #1a1a1a;
    transition: background-color .5s;
    padding-top: 0;
	width: 100%;
}
.nav-bar{
	position: fixed;
    top: 0px;
    width: 100%;
	height: 55px;
    left: 0;
    z-index: 999;
}
.NavBar{
	position: relative;
    border-bottom: 1px solid rgb(84 84 84);
    padding: 0 12px 0 24px;
    height: 55px;
    background-color: #1a1a1a;
    white-space: nowrap;
    transition: border-color .5s,background-color .5s;
}
.container{
	display: flex;
    justify-content: space-between;
    margin: 0 auto;
    max-width: 1376px;
	height: 55px;
}
.NavBarTitle{
	display: flex;
    align-items: center;
    padding-top: 1px;
    height: 54px;
    transition: opacity .25s;
	background-color: #1a1a1a;
}
.text{
    font-size: 16px;
    font-weight: 700;
	background-color: transparent;
    color:#42b883;
}
.content{
	display: flex;
    justify-content: flex-end;
    align-items: center;
    flex-grow: 1;
}
.NavBarSearch{
	display: flex;
    align-items: center;
    padding-left: 16px;
}
.NavBarMenu{
	display: flex;
	justify-content: flex-end;
	align-items: center;
}
.DocSearch-Button {
    justify-content: flex-start;
    width: 100%;
	display: flex;
	align-items: center;
    margin: 0;
	height: 55px;
    background: transparent;
	border: 0;
    border-radius: 40px;
    color: rgba(235, 235, 235, 0.5);
    cursor: pointer;
	font-weight: 500;
	padding: 0 8px;
	user-select: none;
}

.DocSearch-Button-Container {
    align-items: center;
    display: flex;
}
.DocSearch-Button .DocSearch-Search-Icon {
    color: rgba(235, 235, 235, 0.5);
    transition: color .5s;
    fill: currentColor;
	top: 1px;
    margin-right: 10px;
    width: 15px;
    height: 15px;
    position: relative;
	stroke-width: 1.6;
}
.DocSearch-Button:hover .DocSearch-Search-Icon{
	color: rgba(235, 235, 235, 0.9);
}
.DocSearch-Button .DocSearch-Button-Placeholder {
    transition: color .5s;
    font-size: 13px;
    font-weight: 700;
    color: rgba(235, 235, 235, 0.5);
    display: inline-block;
    padding: 0 10px 0 0;
}
.DocSearch-Button:hover .DocSearch-Button-Placeholder{
	color: rgba(235, 235, 235, 0.9);
}
.DocSearch-Button .DocSearch-Button-Keys {
    display: flex;
    gap: 2px;
    min-width: auto;
    box-sizing: border-box;
    border: 2px solid rgba(235, 235, 235, 0.5);
    border-radius: 4px;
    padding: 0 6px;
    font-family: inherit;
    font-size: 12px;
    height: 22px;
    line-height: 22px;
    font-weight: 1000;
    transition: color .5s,border-color .5s;
}
.DocSearch-Button:hover .DocSearch-Button-Keys{
	border-color:#42b883;
}
.DocSearch-Button .DocSearch-Button-key {
	align-items: center;
    background: transparent;
    border-radius: 3px;
    box-shadow: none;
	display: flex;
	justify-content: center;
	position: relative;
	border: 0;
	top: -1px;
    width: auto;
    min-width: auto;
    font-family: inherit;
    font-size: 12px;
    height: 22px;
    padding: 0;
    margin: 0;
    color: rgba(235, 235, 235, 0.5);
    transition: color .5s;
	font-weight: 600;
}
.DocSearch-Button:hover .DocSearch-Button-key{
	color: #42b883;
}
.NavBarMenuLink{

	display: block;
    padding: 0 12px;
    line-height: calc(54px);
    font-size: 13px;
    font-weight: 700;
    color: rgb(235 235 235);
    transition: color .25s;
    white-space: nowrap;
	text-decoration: inherit;
	background-color: transparent;
	user-select: none;
}
.NavBarMenuLink:hover{
	color: #42b883;
}

.avator{
	display: flex;
	align-items: center;
}
img{
	border-radius: 50%;
	width: 40px;

}
.VPContent{
	position: relative;
	height: auto;
    width: 100%;
    overflow: auto;
    background: #1a1a1a;
    padding-top: 0;
    flex-direction: column;
}
</style>
