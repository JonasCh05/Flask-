from flask import jsonify

carrito = []

def ver_carrito():
    return jsonify(carrito)

def agregar_producto():
    
    producto = {
        "id": 1,
        "nombre": "Espresso",
        "precio": 1200
    }

    carrito.append(producto)

    return jsonify({
        "mensaje": "Producto agregado",
        "carrito": carrito
    })