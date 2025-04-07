<template>
    <div class="add-movie-form-view">
      <h2>Add a New Movie</h2>
      <MovieForm />
    </div>
  </template>
  
  <script>
  import MovieForm from '../components/MovieForm.vue';
  
  export default {
    components: {
      MovieForm,
    },
  };
  </script>
  
  <style scoped>
  .add-movie-form-view {
    padding: 20px;
  }
  </style>