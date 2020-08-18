<template>
	<ul class="nav-list">
		<h5 class="nav-title">{{ title }}</h5>
		<li
			v-for="item in links"
			:key="item.title"
			class="nav-list-item"
		>
		<!-- if the link is external use normal anchor link-->
			<a
				v-if="item.external"
				:href="item.src"
				target="_blank">
					{{ item.title }}
			</a>
			<!-- use nuxt-link for all internal links -->
			<nuxt-link
				v-else
				:to="item.src"
			>
			{{ item.title }}
			</nuxt-link>
		</li>
	</ul>
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
ul {
	margin: 0;
	padding: 0;
}

li {
	list-style-type: none;
}
</style>