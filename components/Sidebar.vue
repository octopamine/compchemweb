<template>
	<div class="sidebar">
		<Nav />
	</div>
</template>

<script>
import Nav from '../components/Nav'

export default {
	components: {
		Nav
	}

}
</script>

<style lang="scss">
.sidebar {
	width: 10vw;
	height: 100vh;
	background: #ccc;
}
</style>