import gql from 'graphql-tag'

export const ACTUALIZAR_STOCK = gql`
  mutation actualizarStock($id: Int!, $cantidad: Int!) {
    actualizarStock(id: $id, cantidad: $cantidad) {
      producto {
        id
        stock
        disponible
      }
    }
  }
`
