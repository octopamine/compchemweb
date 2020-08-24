<template>
	<div class="rubric markdown-body" v-html="markdown" /> <!-- calls markdown() -->
</template>

<script>
import markdownData from '~/assets/data/markdown/rubric.md'

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
.rubric {

}
</style>