<template>
	<div class="outline markdown-body" v-html="markdown" /> <!-- calls markdown() -->
</template>

<script>
import markdownData from '~/assets/data/markdown/outline.md'

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
.outline {

}
</style>