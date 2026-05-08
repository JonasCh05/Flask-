from flask import Flask, request
from productos import listar_productos
from carrito import ver_carrito, agregar_producto, eliminar_producto, calcular_total

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/productos')
def productos():
    return listar_productos()

@app.route('/carrito', methods=['GET', 'POST'])
def carrito():

    if request.method == 'POST':
        return agregar_producto()

    return ver_carrito()

@app.route('/carrito/<int:id>', methods=['DELETE'])
def eliminar(id):
    return eliminar_producto(id)

@app.route('/total')
def total():
    return calcular_total()