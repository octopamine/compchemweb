<template>
	<div class="sidebar">
		<!-- Take me home yo!!! -->
		<nuxt-link to="/">SCGSSM Computational Chemistry</nuxt-link>

		<NavList
			title="Course Basics"
			:links="courseBasics"
			class="nav-list"
		/>

		<NavList
			title="Linux Resources"
			:links="linuxResources"
			class="nav-list"
		/>

		<NavList
			title="Modeling Services"
			:links="modelingServices"
			class="nav-list"
		/>
	</div>
</template>

<script>
import NavList from '../components/NavList'
import links from '../assets/data/links'

export default {
	components: {
		NavList
	},
	props: {
		title: {
			type: String,
			default: ''
		}
	},
	// setting data here for NavList components
	data: () => ({
		courseBasics: links.courseBasics,
		linuxResources: links.linuxResources,
		modelingServices: links.modelingServices
	})
}
</script>

<style lang="scss">
@import '~assets/scss/vars';

.sidebar {
	position: absolute;
	top: 0;
	left: 0;
	width: 100vw;
	height: 100vh;
	background: #ccc;
	visibility: hidden;
	opacity: 0;
	padding: 2rem 1.25rem;

	@media (min-width: $screen-md) {
		position: relative;
		top: auto;
		left: auto;
		width: 18vw;
		height: 100vh;
		visibility: visible;
		opacity: 1;
	}

	.nav-list {
		margin-top: 2rem;
	}
}
</style>