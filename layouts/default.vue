<template>
  <div class="container">
    <Sidebar />
    <div class="main">
      <Nuxt />
      <div class="footer">footer</div>
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

  @media (min-width: $screen-md) {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100vh;
    width: 80vw; // sidebar is 20vw
    overflow: hidden;
    overflow-y: scroll;
	}
}
</style>
