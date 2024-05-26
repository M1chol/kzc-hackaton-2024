<template>
    <div id="content">
          <h1 id="firstHeading" class="firstHeading">{{ title || "no title" }}</h1>
          <div id="bodyContent">
            {{ content }}
          </div>
          <h2 id="PostsElem">Posty:</h2>
          <ul>
            <li v-for="post in posts" :key="post.ID">
            <div id="PostAuth"> {{ post.authorID }} - {{ post.date }}</div>
            <div>{{ post.txt }}</div>
            </li>
          </ul>
        </div>
</template>

<script setup>
const props = defineProps({
  title: String,
  content: String,
  posts: Array
})
</script>

<style scoped>

</style>