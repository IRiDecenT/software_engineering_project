<script setup>

import {onMounted, ref} from 'vue'

const albumData = ref(
[
	{
		id: 1,
		title: "动漫画风",
		time: '2023.11.20',
		img: '../../public/01.jpg',
		avatar: '../../public/avator1.jpg',
		alaum: '壁纸',
		poster: 'YR',
	},
	{
		id: 2,
		title: '这就是中国',
		time: '2023.11.20',
		img: '/src/assets/res2.JPG',
		avatar: '../../public/02.jpg',
		alaum: '维维道来',
		poster: 'YR',
	},
	{
		id: 3,
		title: '好想成为玛琪玛小姐的狗啊',
		time: '2023.11.20',
		img: '/src/assets/res3.JPG',
		avatar: '../../public/03.jpg',
		alaum: '二次元',
		poster: 'YR',
	},
	{
		id: 4,
		title: '艾尔登之王',
		time: '2023.11.20',
		img: '../../public/04.jpg',
		avatar: '../../public/0.jpg',
		alaum: '艾尔登法环',
		poster: 'YR',
	},
	{
		id: 5,
		title: '菈妮小姐',
		time: '2023.11.20',
		img: '../../public/05.jpg',
		avatar: '/src/assets/avator1.JPG',
		alaum: '艾尔登法环',
		poster: 'YR',
	},
	{
		id: 6,
		title: '武汉城门',
		time: '2023.11.20',
		img: '../../public/06.jpg',
		avatar: '/src/assets/avator3.JPG',
		alaum: '武汉行',
		poster: 'YR',
	},
	{
		id: 7,
		title: '晴川阁',
		time: '2023.11.20',
		img: '../../public/07.jpg',
		avatar: '/src/assets/avator3.JPG',
		alaum: '武汉行',
		poster: 'YR',
	},
	{
		id: 8,
		title: '是不是拥有以后就会失去',
		time: '2023.11.20',
		img: '../../public/08.jpg',
		avatar: '/src/assets/avator3.JPG',
		alaum: '陶喆蓝专',
		poster: 'YR',
	},
	{
		id: 1,
		title: '快和丁真来学习',
		time: '2023.11.20',
		img: '../../public/09.jpg',
		avatar: '/src/assets/avator1.JPG',
		alaum: '纯真少年',
		poster: 'YR',
	}
]
)





// 这段JavaScript代码的作用是实现一个图片轮播效果。首先，通过document.querySelector('item')获取到所有具有item类名的元素，并将它们存储在items变量中。
// 然后，通过一个循环遍历每个item元素。在循环中，首先获取当前的item元素，然后通过querySelector方法获取到该item下的frame、front、left和right元素，并将它们分别存储在frame、frontBox、leftBox和rightBox变量中。
// 接下来，通过设置frontBox、leftBox和rightBox的style.backgroundImage属性，将背景图片设置为'url(./img/' + (i + 1).toString().padStart(2, '0') + '.jpg)'，其中(i + 1).toString().padStart(2, '0')表示将循环变量i加1后转换为字符串，并在前面补0，以保证图片的文件名格式正确。
// 接着，定义了一个立即执行函数，并在函数内部进行了一些操作。首先，通过document.querySelector('shell')[0]获取到具有shell类名的元素，并将其存储在shell变量中。然后，通过shell.querySelector方法获取到该shell元素下的shell_slider、item、prev和next元素，并将它们分别存储在slider、items、prevBtn和nextBtn变量中。
// 接下来，定义了一些变量，包括width、height、totalWidth、margin、currIndex、interval和intervalTime。width和height分别表示每个item的宽度和高度，totalWidth表示所有item的总宽度，margin表示item的外边距，currIndex表示当前显示的item的索引，interval表示定时器的ID，intervalTime表示定时器的时间间隔。
// 然后，定义了init函数，该函数用于初始化一些操作。在该函数中，首先调用resize函数调整大小，然后调用move函数将显示的item移动到中间位置，接着调用bindEvents函数绑定事件，最后调用timer函数启动定时器。
// 接着，定义了resize函数，该函数用于在窗口大小变化时调整大小。在该函数中，首先计算出新的width和height，然后根据计算结果设置slider的宽度，以及每个item的宽度和高度。
// 接下来，定义了bindEvents函数，该函数用于绑定事件。在该函数中，首先绑定了窗口大小变化时调用resize函数的事件，然后绑定了点击prev按钮和next按钮时调用prev函数和next函数的事件。
// 最后，在立即执行函数的末尾，调用了init函数来初始化页面，并定义了move、timer、prev和next函数。其中，move函数用于移动shell到指定的item，timer函数用于启动定时器，prev函数用于切换到上一个item，next函数用于切换到下一个item。
const doc = ref(null);
onMounted(()=>{
	const Items = doc.value.getElementsByClassName('item');
	for (let i = 0; i < Items.length; i++) {
        // 获取当前item
        let item = Items[i];
        let frame = item.getElementsByClassName('frame')[0];
        let frontBox = frame.getElementsByClassName('front')[0];
        let leftBox = frame.getElementsByClassName('left')[0];
        let rightBox = frame.getElementsByClassName('right')[0];
        // 设置背景图片
        frontBox.style.backgroundImage = 'url(../../../../public/'+(i+1).toString().padStart(2, '0')+'.JPG)';
        leftBox.style.backgroundImage = 'url(../../../../public/'+(i+1).toString().padStart(2, '0')+'.JPG)';
        rightBox.style.backgroundImage = 'url(../../../../public/'+(i+1).toString().padStart(2, '0')+'.JPG)';
    }
	let mainBOX = document.getElementsByClassName('background')[0];
	const slider = doc.value.getElementsByClassName('shell_slider')[0];
	const items = doc.value.getElementsByClassName('item');
	const prevBtn = doc.value.getElementsByClassName('prev')[0];
	const nextBtn = doc.value.getElementsByClassName('next')[0];
	let width, height, totalWidth, margin = 20,
		currIndex = 0,
		interval, intervalTime = 3000;

	function init(){
		resize();
		move(Math.floor(items.length / 2));
		bindEvents();
		timer();
	}

	function resize() {
		// 窗口大小变化时调整大小
		width = Math.max(window.innerWidth * .20, 275);
		height = window.innerHeight * .5;
		totalWidth = width * items.length;
		// 设置slider宽度
		slider.style.width = totalWidth + "px";
		// 设置每个item的宽度和高度
		for (var i = 0; i < items.length; i++) {
			let item = items[i];
			item.style.width = (width - (margin * 2)) + "px";
			item.style.height = height + "px";
		}
	}

	function bindEvents() {
		// 窗口大小变化时调整大小
		window.onresize = resize;
		// 点击prev按钮切换item
		prevBtn.addEventListener('click', () => { prev(); });
		nextBtn.addEventListener('click', () => { next(); });
	}

	function move(index) {
		// 移动shell到指定的item
		if (index < 1) index = items.length;
		if (index > items.length) index = 1;
		currIndex = index;
		// 遍历所有item
		for (var i = 0; i < items.length; i++) {
			let item = items[i],
				box = item.getElementsByClassName('frame')[0];
			if (i == (currIndex - 1)) {
				// 当前item添加active类并设置3D效果
				item.classList.add('item--active');
				box.style.transform = "perspective(1200px)";
			} else {
				// 其他item移除active类并设置3D效果
				item.classList.remove('item--active');
				box.style.transform = "perspective(1200px) rotateY(" + (i < (currIndex - 1) ? 40 : -40) + "deg)";
			}
		}
		// 移动slider
		slider.style.transform = "translate3d(" + ((currIndex * -width) + (width / 2) + window.innerWidth / 2) + "px, 0, 0)";
		// 设置body背景图片
		var frontBox = items[currIndex - 1].getElementsByClassName('front')[0];
		mainBOX.style.backgroundImage = frontBox.style.backgroundImage;

	}
	function timer() {
		// 定时器，自动切换shell
		clearInterval(interval);
		interval = setInterval(() => {
			move(++currIndex);
		}, intervalTime);
	}
	// 切换item
	function prev() {
		move(--currIndex);
		timer();
	}
	function next() {
		move(++currIndex);
		timer();
	}
	init();

})

// function clickItem(id){
// 	console.log(id);
// }


function showEllipsisTitle(value){
	if (!value) return "";
	if (value.length > 25) {
		return value.slice(0, 25) + "...";
	}
	return value;
}

function showEllipsisAlbum(value){
	if (!value) return "";
	if (value.length > 6) {
		return value.slice(0, 6) + "...";
	}
	return value;
}

</script>

<template>
	<div ref="doc" class="background">
		<div class="shell">
			<div class="shell-body">
				<div class="button">
					<!--  eslint-disable-next-line vue/no-parsing-error -->
					<div class="prev"><i class="iconfont icon-backward-filled"> &lt </i></div>
					<div class="next"><i class="iconfont icon-forward-filled"> > </i></div>
				</div>
				<div class="shell_slider">
					<RouterLink v-for="album in albumData" :key="album.id" class="item"  :to="{ path:`/main/album?aid=${album.id}`}">
						<div class="frame" >
							<div class="box front">
								<h1>{{showEllipsisAlbum(album.alaum)}}</h1>
								<span>{{showEllipsisTitle(album.title)}}</span>
							</div>
							<div class="box left"></div>
							<div class="box right"></div>
						</div>
					</RouterLink>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
.background {
	padding-top: 55px;
	display: flex;
	justify-self: center;
	align-items: center;
	height: 100%;
	background-size: cover;
	width: 100%;
	overflow: hidden;
	transition: background-image .7s ease-in-out;
}
.shell {
	position: relative;
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100vw;
	height: 100vh;
	box-sizing: border-box;
	background: rgba(99, 99, 99, 0.8);
}
.button {
	display: flex;
	justify-content: space-between;
	align-items: center;
	width: 380px;
	position: absolute;
	left: 50%;
	transform: translateX(-50%);
	bottom: -80px;
}
.prev, .next {
	transition: transform 0.25s ease;
	z-index: 99999;
	bottom: 5px;
	user-select: none;
}
.prev i,.next i {
	font-size: 90px;
	color: #fff;
	cursor: pointer;
	text-shadow: 0 0 10px #ffffff;
}
.shell-body {
	width: 100%;
	transform: scale(.8);
	padding: 20px 0 150px 0;
}
.shell_slider {
	position: relative;
	transition: transform 1s ease-in-out;
	background: transparent;
}
.item {
	position: relative;
	float: left;
	margin: 0 20px;
}
.frame {
	position: relative;
	width: 100%;
	height: 100%;
	transition: transform 1s ease-in-out;
		transform-style: preserve-3d;
}
.frame:after {
	content: "";
	position: absolute;
	bottom: -16%;
	width: 100%;
	height: 60px;
	background: #ffffff1c;
	box-shadow: 0px 0px 15px 5px #ffffff1c;
	transform: rotateX(90deg) translate3d(0px, -20px, 0px);
}

.box {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	position: absolute;
	width: 100%;
	height: 100%;
	border: 4px solid #fff;
	perspective: 1000px;
	transform-style: preserve-3d;
}
.box h1,.box span {
	color: #fff;
	transform: translateZ(10px);
}
.box h1 {
	text-shadow: 0 0 30px #1f05b4;
	font-size: 40px;
}
.box span {
	position: absolute;
	bottom: 20px;
	padding: 0 25px;
	text-shadow: 0 0 10px #1f05b4;
}
.front{
	box-shadow: 0 0 50px #ffffff;
	background-size: cover;
}

.left,.right {
	box-shadow: 0 0 50px #ffffff;
	background-size: cover;
}
.right,.left {
	top: 0;
	width: 60px;
	backface-visibility: hidden;
}
/* 设置.left元素的左侧偏移量为0，左边框宽度为5px，3D变换为向右平移1px，Z轴平移-60px，绕Y轴逆时针旋转90度，变换原点为左侧 */
.left {
	left: 0;
	border-left-width: 5px;
	transform: translate3d(1px, 0, -60px) rotateY(-90deg);
	transform-origin: 0%;
}

/* 设置.right元素的右侧偏移量为0，右边框宽度为5px，3D变换为向左平移1px，Z轴平移-60px，绕Y轴顺时针旋转90度，变换原点为右侧 */
.right {
	right: 0;
	border-right-width: 5px;
	transform: translate3d(-1px, 0, -60px) rotateY(90deg);
	transform-origin: 100%;
}
</style>