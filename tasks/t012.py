"""
TAREA t012 - CATALOGO COMO BASE DE DATOS (dificultad: DIFICIL)

CONTEXTO:
Cierras la serie de la mini tienda online con el reto mas ambicioso: el
CATALOGO de productos. Hasta ahora cada diccionario era UNA cosa (un
cliente en t010, un recuento en t011). Ahora vas a construir un diccionario
de diccionarios donde la clave es el SKU (codigo unico del producto) y el
valor es el diccionario con los datos del producto.

Esto es exactamente como funciona una tabla de base de datos: cada fila es
un producto, el SKU es su id, y las columnas (name, price, stock,
category) son las claves del diccionario interno. Cuando en unos meses
toques SQL o MongoDB, esta estructura te va a resultar familiar.

NOTA DE IMPORTS:
En esta tarea cerramos el circulo de la reutilizacion. La funcion
`count_by_category` aplica EL MISMO patron que `contar_ventas` de la
tarea t011: por eso la importas en lugar de reescribirla. Tu funcion
nueva solo extrae la lista de categorys del catalogo y se la pasa a la
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

    catalog = {
        "SKU-001": {"name": "Camiseta roja", "price": 19.99,
                    "stock": 30, "category": "ropa"},
        "SKU-002": {"name": "Taza negra", "price": 9.99,
                    "stock": 50, "category": "hogar"}
    }

FUNCIONES A IMPLEMENTAR:

1) add_product(catalog:dict, sku:str, name:str, price:float,
                   stock:int, category:str) -> dict
   Anade un producto nuevo al catalog. Si el sku YA EXISTE, imprime un
   aviso y NO sobrescribe. Devuelve el catalog.

2) update_stock(catalog:dict, sku:str, cambio:int) -> dict
   Suma `cambio` al stock del producto (puede ser negativo si es una
   salida). Reglas:
     - Si el sku no existe: imprime aviso y no hace nada.
     - Si el resultado quedara por debajo de 0: imprime aviso y no aplica.
   Devuelve el catalog.

3) search_by_category(catalog:dict, category:str) -> list
   Devuelve una lista con los nameS de los productos de esa category
   (no los SKUs).

4) apply_discount(catalog:dict, porcentaje:int) -> dict
   Reduce el price de TODOS los productos en el porcentaje indicado.
   Ejemplo: porcentaje = 10 -> prices al 90%. Devuelve el catalog.

5) valor_total_inventario(catalog:dict) -> float
   Devuelve la suma de price * stock de todos los productos.

6) count_by_category(catalog:dict) -> dict
   Devuelve un diccionario {category: numero_de_productos}.
   DEBE reutilizar `contar_ventas` importada de t011: primero extrae la
   lista de categorys recorriendo el catalog y despues se la pasa a
   contar_ventas.

EJEMPLO:

    catalog = {}
    add_product(catalog, "SKU-001", "Camiseta roja", 19.99, 30, "ropa")
    add_product(catalog, "SKU-002", "Camiseta azul", 19.99, 10, "ropa")
    add_product(catalog, "SKU-003", "Taza negra", 9.99, 50, "hogar")
    add_product(catalog, "SKU-004", "Libro Python", 14.99, 5, "libros")
    add_product(catalog, "SKU-001", "Otra", 1.0, 1, "ropa")
    # ^ debe avisar que SKU-001 ya existe y no sobrescribir

    search_by_category(catalog, "ropa")
    # ["Camiseta roja", "Camiseta azul"]

    update_stock(catalog, "SKU-003", -10)   # Taza a 40
    update_stock(catalog, "SKU-004", -20)   # aviso, no aplica
    update_stock(catalog, "SKU-999", 5)     # aviso, no existe

    apply_discount(catalog, 10)              # todos los prices al 90%
    valor_total_inventario(catalog)             # float con el total

    count_by_category(catalog)
    # {"ropa": 2, "hogar": 1, "libros": 1}
"""

# from t011 import count_sales


# def add_product(catalog:dict, sku:str, name:str, price:float,
#                 stock:int, category:str) -> dict:
#     ...

# def update_stock(catalog:dict, sku:str, change:int) -> dict:
#     ...

# def search_by_category(catalog:dict, category:str) -> list:
#     ...

# def apply_discount(catalog:dict, percentage:int) -> dict:
#     ...

# def total_inventory_value(catalog:dict) -> float:
#     ...

# def count_by_category(catalog:dict) -> dict:
#     # 1. Iterate the catalog and build a list of categories
#     #    (duplicates included — that's the point).
#     # 2. Pass that list to count_sales (imported from t011).
#     # 3. Return the result.
#     ...


# --- Tests ---
# catalog = {}
# add_product(catalog, "SKU-001", "Red T-shirt",  19.99, 30, "clothing")
# add_product(catalog, "SKU-002", "Blue T-shirt", 19.99, 10, "clothing")
# add_product(catalog, "SKU-003", "Black Mug",     9.99, 50, "home")
# add_product(catalog, "SKU-004", "Python Book",  14.99,  5, "books")
# add_product(catalog, "SKU-001", "Duplicate",     1.0,   1, "clothing") # warning: already exists
#
# print(search_by_category(catalog, "clothing"))  # ["Red T-shirt", "Blue T-shirt"]
# update_stock(catalog, "SKU-003", -10)           # Mug stock -> 40
# update_stock(catalog, "SKU-004", -20)           # warning: insufficient stock
# update_stock(catalog, "SKU-999",   5)           # warning: SKU not found
#
# apply_discount(catalog, 10)                     # all prices at 90%
# print(total_inventory_value(catalog))           # float with total
# print(count_by_category(catalog))               # {"clothing": 2, "home": 1, "books": 1}
