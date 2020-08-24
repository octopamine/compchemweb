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
				target="_blank"
				class="nav-link">
					{{ item.title }}
			</a>
			<!-- use nuxt-link for all internal links -->
			<nuxt-link
				v-else
				:to="item.src"
				class="nav-link"
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
.nav-list {
	margin: 2rem 0 0 0;
	padding: 0;

	.nav-title {
		padding: 0 2rem;
	}

	&-item {
		list-style-type: none;
		padding: 0 2rem;

		&:hover {
			color: var(--color-fg);
			background-color: var(--color-magenta);

			// make sure .nav-link gets style as well
			.nav-link {
				color: var(--color-fg);
			}
		}
		// make .nav-link take full width of .nav-list-item
		.nav-link {
			display: block;
			width: 100%;
		}
	}
}
</style>