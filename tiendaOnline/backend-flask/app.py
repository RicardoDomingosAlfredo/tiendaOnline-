from flask import Flask, request, jsonify
import graphene

# Definir un esquema básico de GraphQL
class Product(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Float()
    stock = graphene.Int()
    available = graphene.Boolean()

class Query(graphene.ObjectType):
    all_products = graphene.List(Product)

    def resolve_all_products(self, info):
        # Aquí deberías obtener los productos de una base de datos o estructura de datos
        return [
            Product(id=1, name="Producto A", price=100.0, stock=10, available=True),
            Product(id=2, name="Producto B", price=200.0, stock=0, available=False)
        ]

schema = graphene.Schema(query=Query)

app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    query = data.get("query")
    result = schema.execute(query)
    return jsonify(result.data)

if __name__ == "__main__":
    app.run(debug=True)
