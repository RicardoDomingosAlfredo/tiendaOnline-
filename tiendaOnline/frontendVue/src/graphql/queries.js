import gql from 'graphql-tag'

export const GET_PRODUCTOS = gql`
  query {
    productos {
      id
      nombre
      precio
      stock
      disponible
    }
  }
`
