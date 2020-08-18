<template>
  <div class="container">
    <Sidebar />
    <div class="main">
      <Nuxt />
    </div>
  </div>
</template>

<style lang="scss">
@import '~assets/scss/vars';

// top level container
.container {
  display: flex;
  flex-direction: column;

  @media (min-width: $screen-md) {
    flex-direction: row;
  }
}

// main page content
.main {
  padding: 2rem 2.25rem;
}
</style>
