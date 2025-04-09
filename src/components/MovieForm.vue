<template>
  <div class="movie-form">
    <!-- <h1>Add a New Movie</h1> -->
    <form @submit.prevent="saveMovie" id="movieForm">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" v-model="movie.title" name="title" class="form-control" required />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea v-model="movie.description" name="description" class="form-control" required></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input type="file" @change="handleFileUpload" name="poster" class="form-control" required />
      </div>

      <button type="submit" class="btn btn-primary">Submit Movie</button>
    </form>

    <div v-if="message" class="alert alert-success mt-3">{{ message }}</div>
    <div v-if="errors.length" class="alert alert-danger mt-3">
      <h3>Errors:</h3>
      <ul>
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

onMounted(() =>{
    getCsrfToken()
});

let csrf_token = ref("");

function getCsrfToken(){
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
            //csrf_token = data.csrf_token;
        })
}

const movie = ref({
  title: '',
  description: '',
  poster: null,
});

const message = ref('');
const errors = ref([]);

const handleFileUpload = (event) => {
  movie.value.poster = event.target.files[0];
};

const saveMovie = async () => {
  let movieForm = document.getElementById('movieForm'); 
  let form_data = new FormData(movieForm);
  
  form_data.append('title', movie.value.title);
  form_data.append('description', movie.value.description);
  form_data.append('poster', movie.value.poster);
  form_data.append('csrf_token', csrf_token.value);
  

  try {
  const response = await fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  });

  if (!response.ok) {
    const contentType = response.headers.get("content-type");
    if (contentType && contentType.includes("application/json")) {
      const data = await response.json();
      errors.value = data.errors ? data.errors.map(err => Object.values(err).join(' ')) : ['Server returned an error'];
    } else {
      const errorText = await response.text();
      errors.value = [`Server error (${response.status}): Not a valid JSON response`];
      console.error("Server returned non-JSON response:", errorText);
    }
    message.value = '';
    return;
  }

    const data = await response.json();
    message.value = data.message;
    errors.value = [];
  } catch (error) {
    console.error("Request failed:", error);
    errors.value = ['An error occurred while submitting the form.'];
    message.value = '';
  }
};
</script>

<style scoped>
.movie-form {
  max-width: 500px;
  margin: auto;
}

.errors {
  color: red;
}
</style>