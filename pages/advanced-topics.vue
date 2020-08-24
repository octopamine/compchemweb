<template>
	<div class="advanced-topics markdown-body" v-html="markdown" /> <!-- calls markdown() -->
</template>

<script>
import markdownData from '~/assets/data/markdown/advanced-topics.md'

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
.advanced-topics {

}
</style>