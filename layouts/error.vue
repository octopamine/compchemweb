<template>
  <div class="error">
		<h1 v-if="error.statusCode === 404">{{ error.statusCode }}</h1>
    <h1 v-if="error.statusCode === 404">{{ error.message }}</h1>
    <h1 v-else>An error occurred</h1>
  </div>
</template>

<script>
  export default {
    props: ['error'],
    layout: 'error' // you can set a custom layout for the error page
  }
</script>

<style lang="scss">
.error {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100vh;
}
</style>