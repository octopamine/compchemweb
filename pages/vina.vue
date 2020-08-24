<template>
	<div class="vina markdown-body" v-html="markdown" /> <!-- calls markdown() -->
</template>

<script>
import markdownData from '~/assets/data/markdown/VINATemplate.md'

export default {
	computed: {
		// returns data
		markdown() {
			return markdownData
		}
	}
}
</script>

<style lang="scss">
.vina {

}
</style>