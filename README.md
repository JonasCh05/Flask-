API Carrito de Compras

Funciones: 
- Listar productos
- Ver carrito
- Agregar productos al carrito
- Eliminar productos del carrito
- Calcular total de la compra

 Productos disponibles
- ID 1: Jean - $20000
- ID 2: Shorts - $15000
- ID 3: Buzo - $18000

  Endpoints:

Inicio: http://127.0.0.1:5000/

Muestra el mensaje de bienvenida: "Bienvenido!"

  Listar productos

http://127.0.0.1:5000/productos

Nos da el: 
ID de producto
Nombre de producto
Precio del producto

  {"id": 1, "nombre": "Jean", "precio": 20000},
  {"id": 2, "nombre": "Shorts", "precio": 15000},
  {"id": 3, "nombre": "Buzo", "precio": 18000}

  Ver carrito

http://127.0.0.1:5000/carrito

Muestra los productos en el carrito de compras. Si no se agrego productos, no se muestran.

  Agregar producto al carrito

http://127.0.0.1:5000/carrito/agregar/<id>

Agrega productos al carrito de compras. Se debe elegir que producto agregar con su ID
Tambien nos da el mensaje de "Producto agregado". 
Si el producto no existe (su id no se reconoce) da el mensaje de "Producto no encontrado"

  Eliminar producto del carrito

http://127.0.0.1:5000/carrito/eliminar/<id>

Borra un producto del carrito de compras segun la id seleccionada.
Si no se encuentra el producto por la ID o si no existe producto con esa id en el carrito se muestra el mensaje "Producto no encontrado"
Si se encontro el producto del carrito con la ID elegida, se elimina ese producto del carrito de compras y da el mensaje "Producto eliminado"

   Calcular total

Para calcular el total del precio de todos l

