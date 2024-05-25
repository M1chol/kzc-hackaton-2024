<template>
    <div id="content">
          <h1 id="firstHeading" class="firstHeading">{{ title }}</h1>
          <div id="bodyContent">
            {{ content }}
          </div>
        </div>
</template>

<script setup>
const props = defineProps({
  title: String,
  content: String
})
</script>

<style scoped>

</style>