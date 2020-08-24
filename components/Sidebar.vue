<template>
	<div class="sidebar">
		<!-- Take me home yo!!! -->
		<div class="logo-container">
			<nuxt-link to="/" class="logo">SCGSSM Computational Chemistry</nuxt-link>
		</div>

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

		<NavList
			title="Lab Documents"
			:links="labDocuments"
			class="nav-list"
		/>
	</div>
</template>

<script>
import NavList from '../components/NavList'
import links from '../assets/data/json/links'

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
		modelingServices: links.modelingServices,
		labDocuments: links.labDocuments
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
	visibility: hidden;
	opacity: 0;
	padding: 2rem 0;

	@media (min-width: $screen-md) {
		position: relative;
		top: auto;
		left: auto;
		width: 20vw; // main is 80vw
		height: 100vh;
		border-right: 1px solid var(--color-black);
		visibility: visible;
		opacity: 1;
		overflow: hidden;
		overflow-y: scroll;
	}

	.logo-container {
		padding: 0 2rem;
	}

	.logo {
		font-size: 2.5rem;
		line-height: 1;
	}
}
</style>