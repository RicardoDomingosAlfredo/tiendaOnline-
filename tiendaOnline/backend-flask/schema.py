import graphene
from productos import productos, actualizar_disponibilidad

class ProductoType(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

class Query(graphene.ObjectType):
    productos = graphene.List(ProductoType)

    def resolve_productos(root, info):
        return productos

class ActualizarStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        cantidad = graphene.Int(required=True)

    producto = graphene.Field(lambda: ProductoType)

    def mutate(root, info, id, cantidad):
        for prod in productos:
            if prod['id'] == id:
                prod['stock'] += cantidad
                if prod['stock'] < 0:
                    prod['stock'] = 0
                actualizar_disponibilidad(prod)
                return ActualizarStock(producto=prod)
        raise Exception("Producto no encontrado")

class Mutation(graphene.ObjectType):
    actualizar_stock = ActualizarStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
