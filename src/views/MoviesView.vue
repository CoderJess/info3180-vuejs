<template>
    <div class="movies-view">
      <h1>Movies</h1>
      <div class="movies-list">
        <div class="movie-card" v-for="movie in movies" :key="movie.id">
          <img :src="`http://localhost:8080/api/v1/posters/${movie.poster}`" alt="Poster" />
          <h2>{{ movie.title }}</h2>
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </template>

<script setup> 
import { ref, onMounted } from "vue"; 

let movies = ref([]);

async function fetchMovies() {
  try {
    const response = await fetch("http://localhost:8080/api/v1/movies");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    movies.value = data;
  } catch (error) {
    console.error("Error fetching movies:", error);
  }
}

onMounted(fetchMovies);
</script>

<style scoped>
.movies-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.movie-card {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  max-width: 200px;
}
.movie-card img {
  max-width: 100%;
  border-radius: 5px;
}
</style>