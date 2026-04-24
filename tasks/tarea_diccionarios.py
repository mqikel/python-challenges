"""
CONTEXTO:
Estas trabajando en el backend de una mini tienda online. Todavia no hay base
de datos real: todo se guarda en memoria con estructuras de Python.

En esta tarea das tus primeros pasos con DICCIONARIOS, la estructura que mas
vas a ver en el mundo real: un usuario, un producto, un pedido, la respuesta
de una API... casi todo "registro con propiedades" es un diccionario.

Tres ejercicios de dificultad creciente (facil, medio, dificil). Comparten
hilo (la misma tienda online) pero son independientes: hazlos en el orden
que quieras.

REQUISITOS GENERALES:
- Todo lo que hagas va dentro de una funcion. Nada de codigo suelto excepto
  las llamadas de prueba al final de cada bloque.
- Cada funcion lleva type hints (ej: `def nombre(param:str) -> dict:`).
- Una funcion hace UNA cosa y la hace bien.
- Si una funcion que ya implementaste te sirve mas abajo, REUTILIZALA
  (sobre todo en el ejercicio 3).
- Antes de teclear: escribe en un comentario de 2-4 lineas que hace la
  funcion, que recibe y que devuelve.


===============================================================================
EJERCICIO 1  (FACIL)  -  Ficha de cliente
===============================================================================

Vas a representar UN cliente de la tienda como un diccionario y a escribir
las operaciones basicas que cualquier app hace con sus usuarios: crear,
mostrar, actualizar.

Un cliente tiene: nombre, email, ciudad y numero de pedidos realizados
(que arranca en 0).

Funciones a implementar:

1) crear_cliente(nombre:str, email:str, ciudad:str) -> dict
   Devuelve un diccionario con las 4 claves. El contador de pedidos empieza en 0.

2) mostrar_cliente(cliente:dict) -> None
   Imprime la ficha del cliente en formato legible, una linea por campo:
       Nombre: Ana
       Email: ana@mail.com
       Ciudad: Madrid
       Pedidos: 0

3) actualizar_ciudad(cliente:dict, nueva_ciudad:str) -> dict
   Cambia la ciudad del cliente y devuelve el diccionario modificado.

4) registrar_pedido(cliente:dict) -> dict
   Suma 1 al numero de pedidos del cliente y devuelve el diccionario.

EJEMPLO:

    cliente = crear_cliente("Ana", "ana@mail.com", "Madrid")
    mostrar_cliente(cliente)
    cliente = actualizar_ciudad(cliente, "Valencia")
    cliente = registrar_pedido(cliente)
    cliente = registrar_pedido(cliente)
    mostrar_cliente(cliente)

Salida esperada del segundo mostrar_cliente:
    Nombre: Ana
    Email: ana@mail.com
    Ciudad: Valencia
    Pedidos: 2


===============================================================================
EJERCICIO 2  (MEDIO)  -  Top de ventas
===============================================================================

A final de mes te pasan la lista de ventas del dia: un elemento por venta,
con el nombre del producto vendido. Quieres saber cuantas unidades de cada
producto se han vendido, cual es el mas vendido y cuales superan un minimo.

Este es uno de los patrones mas utiles del mundo real con diccionarios:
CONTAR FRECUENCIAS. Lo usaras en analitica, logs, estadisticas, etc.

Funciones a implementar:

1) contar_ventas(ventas:list) -> dict
   Recibe una lista con los nombres de productos vendidos y devuelve un
   diccionario {producto: cantidad}.
   Pista: recorrer la lista y, por cada producto, sumar 1 a su contador.
          Si el producto aun no esta en el diccionario, inicializalo en 1.

2) producto_mas_vendido(recuento:dict) -> str
   Dado el diccionario devuelto por contar_ventas, devuelve el nombre del
   producto con mayor numero de ventas.

3) productos_con_minimo(recuento:dict, minimo:int) -> list
   Devuelve una lista con los nombres de productos cuya cantidad vendida
   es mayor o igual al minimo indicado.

4) total_unidades(recuento:dict) -> int
   Devuelve la suma total de unidades vendidas (suma de todos los valores).

EJEMPLO:

    ventas = ["camiseta", "gorra", "camiseta", "pantalon",
              "camiseta", "gorra", "zapatillas"]

    recuento = contar_ventas(ventas)
    # {"camiseta": 3, "gorra": 2, "pantalon": 1, "zapatillas": 1}

    producto_mas_vendido(recuento)        # "camiseta"
    productos_con_minimo(recuento, 2)     # ["camiseta", "gorra"]
    total_unidades(recuento)              # 7


===============================================================================
EJERCICIO 3  (DIFICIL)  -  Catalogo como base de datos
===============================================================================

Hasta ahora cada diccionario era UNA cosa (un cliente, un recuento). Ahora
vas a construir un CATALOGO: un diccionario de diccionarios donde la clave
es el SKU (codigo unico del producto) y el valor es el diccionario con los
datos del producto.

Esto es exactamente como funciona una tabla de base de datos: cada fila es
un producto, el SKU es su id, y las columnas (nombre, precio, stock,
categoria) son las claves del diccionario interno.

Estructura:

    catalogo = {
        "SKU-001": {"nombre": "Camiseta roja", "precio": 19.99,
                    "stock": 30, "categoria": "ropa"},
        "SKU-002": {"nombre": "Taza negra", "precio": 9.99,
                    "stock": 50, "categoria": "hogar"}
    }

Funciones a implementar:

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
   Devuelve una lista con los NOMBRES de los productos de esa categoria.

4) aplicar_descuento(catalogo:dict, porcentaje:int) -> dict
   Reduce el precio de TODOS los productos en el porcentaje indicado.
   Ejemplo: porcentaje = 10 -> precios al 90%. Devuelve el catalogo.

5) valor_total_inventario(catalogo:dict) -> float
   Devuelve la suma de precio * stock de todos los productos.

6) contar_por_categoria(catalogo:dict) -> dict
   Devuelve un diccionario {categoria: numero_de_productos}.
   IMPORTANTE: esta funcion debe REUTILIZAR `contar_ventas` del
   ejercicio 2. Extrae primero la lista de categorias del catalogo y
   pasasela a contar_ventas. Una funcion bien hecha sirve en otros
   contextos: ese es uno de los porques de las funciones.

EJEMPLO:

    catalogo = {}
    anadir_producto(catalogo, "SKU-001", "Camiseta roja", 19.99, 30, "ropa")
    anadir_producto(catalogo, "SKU-002", "Camiseta azul", 19.99, 10, "ropa")
    anadir_producto(catalogo, "SKU-003", "Taza negra", 9.99, 50, "hogar")
    anadir_producto(catalogo, "SKU-004", "Libro Python", 14.99, 5, "libros")
    anadir_producto(catalogo, "SKU-001", "Otra camiseta", 1.0, 1, "ropa")
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


# =============================================================================
# EJERCICIO 1  -  Ficha de cliente
# =============================================================================

# def crear_cliente(nombre:str, email:str, ciudad:str) -> dict:
#     ...

# def mostrar_cliente(cliente:dict) -> None:
#     ...

# def actualizar_ciudad(cliente:dict, nueva_ciudad:str) -> dict:
#     ...

# def registrar_pedido(cliente:dict) -> dict:
#     ...


# --- Pruebas ejercicio 1 ---
# cliente = crear_cliente("Ana", "ana@mail.com", "Madrid")
# mostrar_cliente(cliente)
# cliente = actualizar_ciudad(cliente, "Valencia")
# cliente = registrar_pedido(cliente)
# cliente = registrar_pedido(cliente)
# mostrar_cliente(cliente)


# =============================================================================
# EJERCICIO 2  -  Top de ventas
# =============================================================================

# def contar_ventas(ventas:list) -> dict:
#     ...

# def producto_mas_vendido(recuento:dict) -> str:
#     ...

# def productos_con_minimo(recuento:dict, minimo:int) -> list:
#     ...

# def total_unidades(recuento:dict) -> int:
#     ...


# --- Pruebas ejercicio 2 ---
# ventas = ["camiseta", "gorra", "camiseta", "pantalon",
#           "camiseta", "gorra", "zapatillas"]
# recuento = contar_ventas(ventas)
# print(recuento)
# print(producto_mas_vendido(recuento))
# print(productos_con_minimo(recuento, 2))
# print(total_unidades(recuento))


# =============================================================================
# EJERCICIO 3  -  Catalogo como base de datos
# =============================================================================

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
#     # REUTILIZA contar_ventas del ejercicio 2
#     ...


# --- Pruebas ejercicio 3 ---
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
