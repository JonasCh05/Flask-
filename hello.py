from flask import Flask
from flask import Flask, request
from productos import listar_productos
from carrito import ver_carrito
from carrito import ver_carrito, agregar_producto

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