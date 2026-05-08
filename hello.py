from flask import Flask
from productos import listar_productos
from carrito import ver_carrito, agregar_producto, eliminar_producto, calcular_total

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bienvenido!'

@app.route('/productos')
def productos():
    return listar_productos()

@app.route('/carrito')
def ver():
    return ver_carrito()

@app.route('/carrito/agregar/<int:id>')
def agregar(id):
    return agregar_producto(id)

@app.route('/carrito/eliminar/<int:id>')
def eliminar(id):
    return eliminar_producto(id)

@app.route('/total')
def total():
    return calcular_total()