productos = [
    {'id': 1, 'nombre': 'Teclado', 'precio': 25.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Ratón', 'precio': 15.99, 'stock': 0, 'disponible': False},
    {'id': 3, 'nombre': 'Monitor', 'precio': 199.99, 'stock': 5, 'disponible': True}
]

def actualizar_disponibilidad(producto):
    producto['disponible'] = producto['stock'] > 0
