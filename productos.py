from flask import jsonify

productos = [
    {"id": 1, "nombre": "Jean", "precio": 20000},
    {"id": 2, "nombre": "Shorts", "precio": 15000},
    {"id": 3, "nombre": "Buzo", "precio": 18000}
]

def listar_productos():
    return jsonify(productos)