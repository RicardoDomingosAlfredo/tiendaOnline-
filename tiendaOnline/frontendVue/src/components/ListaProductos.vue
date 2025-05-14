<template>
    <div>
      <h2>Inventario</h2>
      <ProductosCard
        v-for="producto in productos"
        :key="producto.id"
        :producto="producto"
        :refetch="refetch"
      />
    </div>
  </template>
  
  <script>
  import { useQuery } from '@vue/apollo-composable'
  import { GET_PRODUCTOS } from '../graphql/queries'
  import ProductosCard from './ProductosCard.vue'
  
  export default {
    components: { ProductosCard },
    setup() {
      const { result, refetch } = useQuery(GET_PRODUCTOS)
      return {
        productos: result,
        refetch
      }
    }
  }
  </script>
  