// src/main.js
import { createApp, h } from 'vue'
import App from './App.vue'
import { DefaultApolloClient } from '@vue/apollo-composable'
import { ApolloClient, InMemoryCache, HttpLink } from '@apollo/client/core'

const httpLink = new HttpLink({
  uri: 'http://localhost:5000/graphql' // Asegúrate de que coincide con tu backend Flask
})

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
})

createApp({
  setup() {
    return {
      [DefaultApolloClient]: apolloClient
    }
  },
  render: () => h(App)
}).mount('#app')
