<template>
	<view>
		<button type="primary"  @click="myclick">an</button>
		<button type="primary"  @click="tclick()">time</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				href: 'pages/index/time'
			}
		},
		onLoad(){
			uni.$on('jump1',function(data){
				
			})
		},
		methods: {
			myclick(e){
			console.log('aaa',e)
			},
			tclick(){
				uni.navigateTo({
					url:'/pages/index/time'
				})
			}
		}
	}
</script>

<style>
	.container {
		padding: 20px;
		font-size: 14px;
		line-height: 24px;
	}
	.box{
		width:100px;
		height:100px;
		background-color: aqua;
	}
	.a{
		background-color: blue;
	}
</style>
