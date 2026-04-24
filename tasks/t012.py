"""
TAREA t012 - CATALOGO COMO BASE DE DATOS (dificultad: DIFICIL)

CONTEXTO:
Cierras la serie de la mini tienda online con el reto mas ambicioso: el
CATALOGO de productos. Hasta ahora cada diccionario era UNA cosa (un
cliente en t010, un recuento en t011). Ahora vas a construir un diccionario
de diccionarios donde la clave es el SKU (codigo unico del producto) y el
valor es el diccionario con los datos del producto.

Esto es exactamente como funciona una tabla de base de datos: cada fila es
un producto, el SKU es su id, y las columnas (nombre, precio, stock,
categoria) son las claves del diccionario interno. Cuando en unos meses
toques SQL o MongoDB, esta estructura te va a resultar familiar.

NOTA DE IMPORTS:
En esta tarea cerramos el circulo de la reutilizacion. La funcion
`contar_por_categoria` aplica EL MISMO patron que `contar_ventas` de la
tarea t011: por eso la importas en lugar de reescribirla. Tu funcion
nueva solo extrae la lista de categorias del catalogo y se la pasa a la
funcion que ya tenias hecha.

    from t011 import contar_ventas

Ejecuta desde la carpeta tasks/:

    cd tasks
    python t012.py

REQUISITOS GENERALES:
- Todo va dentro de una funcion. Nada de codigo suelto excepto las llamadas
  de prueba al final.
- Cada funcion lleva type hints.
- Antes de teclear: escribe en un comentario de 2-4 lineas que hace la
  funcion, que recibe y que devuelve.

ESTRUCTURA DE DATOS:

    catalogo = {
        "SKU-001": {"nombre": "Camiseta roja", "precio": 19.99,
                    "stock": 30, "categoria": "ropa"},
        "SKU-002": {"nombre": "Taza negra", "precio": 9.99,
                    "stock": 50, "categoria": "hogar"}
    }

FUNCIONES A IMPLEMENTAR:

1) anadir_producto(catalogo:dict, sku:str, nombre:str, precio:float,
                   stock:int, categoria:str) -> dict
   Anade un producto nuevo al catalogo. Si el sku YA EXISTE, imprime un
   aviso y NO sobrescribe. Devuelve el catalogo.

2) actualizar_stock(catalogo:dict, sku:str, cambio:int) -> dict
   Suma `cambio` al stock del producto (puede ser negativo si es una
   salida). Reglas:
     - Si el sku no existe: imprime aviso y no hace nada.
     - Si el resultado quedara por debajo de 0: imprime aviso y no aplica.
   Devuelve el catalogo.

3) buscar_por_categoria(catalogo:dict, categoria:str) -> list
   Devuelve una lista con los NOMBRES de los productos de esa categoria
   (no los SKUs).

4) aplicar_descuento(catalogo:dict, porcentaje:int) -> dict
   Reduce el precio de TODOS los productos en el porcentaje indicado.
   Ejemplo: porcentaje = 10 -> precios al 90%. Devuelve el catalogo.

5) valor_total_inventario(catalogo:dict) -> float
   Devuelve la suma de precio * stock de todos los productos.

6) contar_por_categoria(catalogo:dict) -> dict
   Devuelve un diccionario {categoria: numero_de_productos}.
   DEBE reutilizar `contar_ventas` importada de t011: primero extrae la
   lista de categorias recorriendo el catalogo y despues se la pasa a
   contar_ventas.

EJEMPLO:

    catalogo = {}
    anadir_producto(catalogo, "SKU-001", "Camiseta roja", 19.99, 30, "ropa")
    anadir_producto(catalogo, "SKU-002", "Camiseta azul", 19.99, 10, "ropa")
    anadir_producto(catalogo, "SKU-003", "Taza negra", 9.99, 50, "hogar")
    anadir_producto(catalogo, "SKU-004", "Libro Python", 14.99, 5, "libros")
    anadir_producto(catalogo, "SKU-001", "Otra", 1.0, 1, "ropa")
    # ^ debe avisar que SKU-001 ya existe y no sobrescribir

    buscar_por_categoria(catalogo, "ropa")
    # ["Camiseta roja", "Camiseta azul"]

    actualizar_stock(catalogo, "SKU-003", -10)   # Taza a 40
    actualizar_stock(catalogo, "SKU-004", -20)   # aviso, no aplica
    actualizar_stock(catalogo, "SKU-999", 5)     # aviso, no existe

    aplicar_descuento(catalogo, 10)              # todos los precios al 90%
    valor_total_inventario(catalogo)             # float con el total

    contar_por_categoria(catalogo)
    # {"ropa": 2, "hogar": 1, "libros": 1}
"""

# from t011 import contar_ventas


# def anadir_producto(catalogo:dict, sku:str, nombre:str, precio:float,
#                     stock:int, categoria:str) -> dict:
#     ...

# def actualizar_stock(catalogo:dict, sku:str, cambio:int) -> dict:
#     ...

# def buscar_por_categoria(catalogo:dict, categoria:str) -> list:
#     ...

# def aplicar_descuento(catalogo:dict, porcentaje:int) -> dict:
#     ...

# def valor_total_inventario(catalogo:dict) -> float:
#     ...

# def contar_por_categoria(catalogo:dict) -> dict:
#     # 1. Recorrer el catalogo y construir una lista con las categorias
#     #    (habra repetidos, eso es lo que queremos).
#     # 2. Pasar esa lista a contar_ventas (importada de t011).
#     # 3. Devolver el resultado.
#     ...


# --- Pruebas ---
# catalogo = {}
# anadir_producto(catalogo, "SKU-001", "Camiseta roja", 19.99, 30, "ropa")
# anadir_producto(catalogo, "SKU-002", "Camiseta azul", 19.99, 10, "ropa")
# anadir_producto(catalogo, "SKU-003", "Taza negra", 9.99, 50, "hogar")
# anadir_producto(catalogo, "SKU-004", "Libro Python", 14.99, 5, "libros")
# anadir_producto(catalogo, "SKU-001", "Duplicada", 1.0, 1, "ropa")  # aviso
#
# print(buscar_por_categoria(catalogo, "ropa"))
# actualizar_stock(catalogo, "SKU-003", -10)
# actualizar_stock(catalogo, "SKU-004", -20)   # aviso
# actualizar_stock(catalogo, "SKU-999", 5)     # aviso
#
# aplicar_descuento(catalogo, 10)
# print(valor_total_inventario(catalogo))
# print(contar_por_categoria(catalogo))
