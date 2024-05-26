<template>
    <div id="content">
          <h1 id="firstHeading" class="firstHeading">{{ title || "no title" }}</h1>
          <div id="bodyContent">
            {{ content }}
          </div>
          <h2 id="PostsElem">Posty:</h2>
          <ul>
            <li>
              <form @submit.prevent="sendMessege">
                <input v-model="textVal" required placeholder="Dodaj komentarz">
                <button>OK</button>
              </form>
            </li>
            <li v-for="post in posts" :key="post.ID">
            <div id="PostAuth"> {{ post.authorID }} - {{ post.date }}</div>
            <div>{{ post.txt }}</div>
            </li>
          </ul>
        </div>
</template>

<script setup>
import { ref } from 'vue'
const props = defineProps({
  title: String,
  content: String,
  posts: Array,
  pinId2: Number
})
let textVal = ref('')
let newMessege = {pinID: props.pinId2, txt: "", authorID: "Guest", iconID: 0}

function sendMessege() {
    newMessege.txt = textVal.value
  fetch(`http://127.0.0.1:8000/addnewpost`, {
    method: 'POST', // HTTP method
    headers: {
      'Content-Type': 'application/json' // Indicate the request body format
    },
    body: JSON.stringify(newMessege) // Convert the data object to a JSON string

  })
    .then(response => response.json()) // Parse the JSON from the response
    .then(data => {
      console.log('Success:', data); // Handle the success response
    })
    .catch((error) => {
      console.error('Error:', error); // Handle any errors
    }).then(textVal = '');
}

</script>

<style scoped>

</style>