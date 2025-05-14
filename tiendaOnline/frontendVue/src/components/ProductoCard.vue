<template>
    <div class="card">
      <h3>{{ producto.nombre }}</h3>
      <p>💰 Precio: {{ producto.precio }}€</p>
      <p>📦 Stock: {{ producto.stock }}</p>
      <p :class="producto.disponible ? 'disponible' : 'no-disponible'">
        {{ producto.disponible ? '✅ Disponible' : '❌ No disponible' }}
      </p>
      <button @click="modificarStock(1)">➕ Aumentar</button>
      <button @click="modificarStock(-1)">➖ Disminuir</button>
    </div>
  </template>
  
  <script>
  import { ACTUALIZAR_STOCK } from '../graphql/mutations'
  import { useMutation } from '@vue/apollo-composable'
  
  export default {
    props: {
      producto: Object,
      refetch: Function
    },
    setup(props) {
      const { mutate } = useMutation(ACTUALIZAR_STOCK)
  
      const modificarStock = (cantidad) => {
        mutate({
          id: props.producto.id,
          cantidad
        }).then(() => props.refetch())
      }
  
      return {
        modificarStock
      }
    }
  }
  </script>
  
  <style scoped>
  .card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 12px;
    background-color: #f9f9f9;
  }
  .disponible {
    color: green;
  }
  .no-disponible {
    color: red;
  }
  button {
    margin-right: 8px;
  }
  </style>
  