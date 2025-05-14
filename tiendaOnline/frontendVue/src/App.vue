<template>
    <div id="app">
      <h1>🛍️ Tienda Online</h1>
      <ListaProductos />
    </div>
  </template>
  
  <script>
  import ListaProductos from './components/ListaProductos.vue'
  
  export default {
    name: 'App',
    components: {
      ListaProductos
    }
  }
  </script>
  
  <style>
  #app {
    max-width: 800px;
    margin: auto;
    padding: 2rem;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
  }
  </style>
  