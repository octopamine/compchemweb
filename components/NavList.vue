<template>
	<nav class="nav">
		<h5>{{ title }}</h5>
		<div
			v-for="item in links"
			:key="item.title"
		>
			<a
				v-if="item.external"
				:href="item.src"
				target="_blank">
					{{ item.title }}
			</a>
			<nuxt-link
				v-else
				:to="item.src"
			>
			{{ item.title }}
			</nuxt-link>
		</div>
	</nav>
</template>

<script>
export default {
	props: {
		title: {
			type: String,
			default: ''
		},
		src: {
			type: String,
			default: ''
		},
		links: {
			type: Array,
			default: () => [],
			required: true
		}
	}
}
</script>

<style lang="scss">
.nav {
	display: flex;
	flex-direction: column;
}
</style>