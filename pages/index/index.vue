<template>
	<view>
	<button type="primary"  @click="myclick">an</button>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				href: 'https://uniapp.dcloud.io/component/README?id=uniui'
			}
		},
		methods: {
			myclick(e){
			console.log('aaa',e)
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
