from flask import jsonify

productos = [
    {"id": 1, "nombre": "Jean", "precio": 20000},
    {"id": 2, "nombre": "Shorts", "precio": 15000},
    {"id": 3, "nombre": "Buzo", "precio": 18000}
]

def listar_productos():
    return jsonify(productos)

def obtener_producto_por_id(id):
    for producto in productos:
        if producto["id"] == id:
            return producto
    return None