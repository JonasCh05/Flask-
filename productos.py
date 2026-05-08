from flask import jsonify

productos = [
    {"id": 1, "nombre": "Espresso", "precio": 1200},
    {"id": 2, "nombre": "Latte", "precio": 1500},
    {"id": 3, "nombre": "Capuccino", "precio": 1800}
]

def listar_productos():
    return jsonify(productos)