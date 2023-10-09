<template>
    <view id="body" class="uni_flex_col_align_center" style="height: 640px;margin: 0 auto;">
		<view style="position: absolute;left: 0px; background-color: aliceblue;height: 50px;width: 100%; opacity:0.5;">
			<view style="position: absolute;left: 42%;top: 13px;font-size: 20px;">番茄钟</view>
		</view>
		<button class="back" @click="back"><</button>
		<view style="height: 100px;"></view>

        <!-- 圆环进度条 -->
        <luanqing-progressbar style="margin:  0px auto 20px auto;" 
            v-if="showMode === 'ring'"
            ref="ringProgressBar" 
            active-color="#E00300" 
            default-color="#ede3e7"     
            mode="ring" 
            :border="40" 
            :ringSize="400" 
            :deley="1800000">
            <view>
                <image class="image" src="../../static/未命名的设计.png" mode="widthFix" style="width: 150px;"></image>
            </view>
        </luanqing-progressbar>
		
		<view class="time" style="position: relative; left: 30%; margin: 30px auto 30px auto;display:flex;font-size: 37px;" >
				<view class="shijian" >{{countdownh}}</view>
				<text >:</text>
				<view class="shijian" >{{countdownm}}</view>
				<text >:</text>
				<view class="shijian" >{{countdowns}}</view>
		</view>
		
        <view v-if="showMode === 'ring'" class="uni_flex_row_between_center mt30" >
			<button @click="start" class="button red" :disabled="isLock1">▶</button>
            
            <!-- <view @click="stop" class="button red" style="margin:5px auto;">停止</view> -->
        </view>
		<view id="body" style="height: 30px;"></view>

        <!-- <view v-if="showMode === 'ring'" class="uni_flex_row_between_center mt5" style="margin-bottom: 128rpx;">
            <view @click="pause" class="button blue" style="margin: 5px auto;">暂停</view>
            <view @click="resume" class="button blue" style="margin: 5px auto;">恢复</view>
        </view> -->
		
		<view id="body">
			<view  style="position: relative; left: 10%;margin: 20px auto 20px auto;font-size: 15px;">
				如果你需要一点背景音乐……
			</view>
			<view class="page-body">
				<view class="page-section page-section-gap" style="text-align: center;">
					<audio style="text-align: left" :src="current.src" :poster="current.poster" :name="current.name" :author="current.author" :action="audioAction" controls></audio>
				</view>
			</view>
		</view>
    </view>
	
</template>

<script>
    export default {
        data() {
            return {
                // 显示哪个类型的进度条   ring圆环  line长条
                showMode: 'ring' , 
				countdownh:'00',
				countdownm:'30',
				countdowns:'00',
				timer: null, //重复执行
				current: {
					poster: '../../static/lili.JPG',
					name: '音乐',
					author: '',
					src: '../../static/柳轻颂 - 溯（钢琴版）.mp3',
				},
				audioAction: {
					method: 'pause'
				}
            }
        },
        onReady() {
            uni.setNavigationBarTitle({
                title:'倒计时',
            });
        },
        methods: {
            // 开始
            start(progress){
				this.isLock1 = true
                this.$refs.ringProgressBar.start();
				this.timestart(),
				setTimeout(this.show,1800000)
            },
			show(){
				uni.showToast({
					title: '完成了一个番茄钟！',
					duration: 4000
				});
				setTimeout(this.jump,4000)
			},
			jump(){
				uni.navigateTo({
					url: '/pages/index/index'
				})
				uni.$emit('jump1',{pat:1})
				// uni.redirectTo({
				// 	url: '/pages/index/index'
				// })
			},
			back(){
				uni.showModal({
					title: '!',
					content: '真的要离开吗？已有的进度将会重置(>_<)……',
					success: function (res) {
						if (res.confirm) {
							uni.redirectTo({
								url: '/pages/index/index'
							})
						} else if (res.cancel) {
							
						}
					}
				});
			},
            // // 停止
            // stop(){
            //     this.$refs.ringProgressBar.stop();
            // },
            // // 暂停
            // pause(){
            //     this.$refs.ringProgressBar.pause();
            // },
            // // 恢复
            // resume(){
            //     this.$refs.ringProgressBar.resume();
            // },
			timestart() {
				var d = new Date();
				var n = d.getTime(); 
				this.timer = setInterval(()=>{
					this.showtime(n+1800000)
				})
			},
			showtime (end) {
				var nowtime = new Date(),
				lefttime = end - nowtime.getTime(),
				lefth = Math.floor(lefttime/(1000*60*60)%24) < 10 ? "0" + Math.floor(lefttime/(1000*60*60)%24) : Math.floor(lefttime/(1000*60*60)%24),  //计算小时数
				leftm = Math.floor(lefttime/(1000*60)%60) < 10 ? "0" + Math.floor(lefttime/(1000*60)%60) : Math.floor(lefttime/(1000*60)%60),  //计算分钟数
				lefts = Math.floor(lefttime/1000%60) < 10 ? "0" + Math.floor(lefttime/1000%60) : Math.floor(lefttime/1000%60);  //计算秒数
				this.countdownh = lefth  //返回倒计时的字符串
				this.countdownm = leftm//返回倒计时的字符串
				this.countdowns = lefts  //返回倒计时的字符串
				// 倒计时结束时，显示00:00:00
				if(lefttime < 0) {
					this.countdownh = this.countdownm= this.countdowns = "00"
				}
			}
        }
    }
</script>

<style>
#body{
	background-image: url("../../static/bg.png");
	background-size: cover;
	background-repeat: no-repeat;
	background-attachment: fixed;
}
.button{
    margin: 10rpx;
    width: 150rpx;
    color: #ffffff;
    font-size: 40rpx;
    padding: 5rpx 5rpx;
    border-radius: 450rpx;
    display: flex;
    align-items: center;
    justify-content: center;
    letter-spacing: 4rpx;
	margin: 20px auto 20px auto;
}
.red{
    background-color: #E00300;
}
.blue{
    background-color: cornflowerblue;
}
.button:active{
    background-color: #CDCDCD;
}
.back{
	position: absolute;
	opacity:0.8;
	width: 75px;
	height: 50px;
	left: 0px;
	background-color: aliceblue;
	border-radius: 0rpx;
	border-style: none;
}
uni-button:after {
	border: none;
}
</style>
