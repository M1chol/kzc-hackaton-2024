<template>
    <div id="content">
          <h1 id="firstHeading" class="firstHeading">{{ title || "no title" }}</h1>
          <div id="bodyContent">
            {{ content }}
          </div>
              <li v-for="post in posts" :key="post.ID">
              <span v-if="post.iconID == 1">
                <h2>Rozkład jazdy</h2>
                Najbliższy tramwaj za 20 minut
              </span>
            </li>
          <hr>
          <h2 id="PostsElem">Posty:</h2>
          <ul>
            <li v-for="post in posts" :key="post.ID">
              <div id="postText">{{ post.txt }}</div>
              <div id="PostAuth"> {{ post.authorID }} - {{ post.date }}</div>
            </li>
          </ul>
          <form @submit.prevent="sendMessege">
            <div id="addBar">
              <input id="addComment" v-model="textVal" required placeholder="Dodaj komentarz"><br>
            </div>
            <div id="addpost">
              <button @click="addPost">
                <span>+</span>
              </button>
            </div>
          </form>
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
    }).then(textVal.value = '');
}

</script>

<style scoped>

#postText {
  font-size: 18px;
}
#postAuth {
  font-style: oblique;
}
#PostsElem {
  margin-bottom: 10px;
}
li {
  margin-left: 0px;
}

#addComment {
  margin-top: 10px;
  margin-left: 10px;
  max-width: 250px;
  background-color: #f5f5f5;
  color: #627254;
  padding: .15rem .5rem;
  min-height: 40px;
  border-radius: 15px;
  outline: none;
  border: none;
  line-height: 1.15;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

#addComment:focus {
  border-bottom: 2px solid #627254;
  border-radius: 15px;
}

#addComment:hover {
  outline: 1px solid lightgrey;
}

  #submitComment{
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  #firstHeading {
    text-align: center;
  }
  hr {
    margin-top: 10px;
    margin-bottom: 10px;
  }

  #content {
    overflow-y: hidden;
  }

  #addpost {
    display: flex;
    justify-content: center;
  }

  button {

    background-color: #76885B;
    border: 1px solid rgb(209,213,219);
    border-radius: .5rem;
    color: #111827;
    font-family: ui-sans-serif,system-ui,-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
    font-size: .7rem;
    font-weight: 600;
    line-height: 1.75rem;
    padding: .75rem 3rem;
    padding-bottom: 0;
    text-align: center;
    -webkit-box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  box-shadow: 0px 10px 20px -18px;

    cursor: pointer;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-user-select: none;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    }

    button:hover {
    background-color: #627254;
    }

    button:focus {
    outline: 2px solid rgba(0,0,0,0.1);
    outline-offset: 2px;
    }

    button:focus-visible {
    -webkit-box-shadow: none;
    box-shadow: none;
    }

    button span {
      font-size: 40px;
      padding: 0;
      margin: 0;
      color: white;
    }
</style>