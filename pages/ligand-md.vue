<template>
	<div class="ligand-md markdown-body" v-html="markdown" /> <!-- calls markdown() -->
</template>

<script>
import markdownData from '~/assets/data/markdown/LigandMDTemplate.md'

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
.ligand-md {

}
</style>