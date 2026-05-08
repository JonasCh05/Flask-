from flask import jsonify, request
from productos import obtener_producto_por_id
carrito = []

def ver_carrito():
    return jsonify(carrito)

def agregar_producto(id):

    producto = obtener_producto_por_id(id)

    if producto:
        carrito.append(producto)
        return jsonify({
            "mensaje": "Producto agregado",
            "carrito": carrito
        })

    return jsonify({
        "mensaje": "Producto no encontrado"
    })

def eliminar_producto(id):

    for producto in carrito:
        if producto["id"] == id:
            carrito.remove(producto)
            return jsonify({
                "mensaje": "Producto eliminado",
                "carrito": carrito
            })

    return jsonify({
        "mensaje": "Producto no encontrado"
    })

def calcular_total():

    total = 0

    for producto in carrito:
        total += producto["precio"]

    return jsonify({
        "total": total
    })