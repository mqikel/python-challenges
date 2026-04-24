"""
TAREA t011 - TOP DE VENTAS (dificultad: MEDIO)

CONTEXTO:
Sigues trabajando en el backend de la mini tienda online. A final de dia te
pasan la lista de ventas: un elemento por venta, con el nombre del producto
vendido. Quieres saber cuantas unidades se han vendido de cada producto,
cual es el mas vendido y cuales superan un minimo.

Este es uno de los patrones mas utiles del mundo real con diccionarios:
CONTAR FRECUENCIAS. Lo usaras en analitica, logs, estadisticas, metricas
de negocio... basicamente en cualquier trabajo de desarrollo backend.

NOTA DE IMPORTS (CONCEPTO NUEVO):
En esta tarea vas a usar por primera vez el concepto de IMPORTAR funciones
de otro archivo. Al principio del archivo tienes la linea:

    from t010 import crear_cliente, registrar_pedido

Eso permite usar funciones de t010 sin reescribirlas. Es exactamente como
en el trabajo real se comparten utilidades entre modulos. Para que el
import funcione, ejecuta el archivo DESDE la carpeta tasks/:

    cd tasks
    python t011.py

REQUISITOS GENERALES:
- Todo va dentro de una funcion. Nada de codigo suelto excepto las llamadas
  de prueba al final.
- Cada funcion lleva type hints (ej: `def nombre(param:list) -> dict:`).
- Antes de teclear: escribe en un comentario de 2-4 lineas que hace la
  funcion, que recibe y que devuelve.

FUNCIONES A IMPLEMENTAR:

1) contar_ventas(ventas:list) -> dict
   Recibe una lista con los nombres de productos vendidos y devuelve un
   diccionario {producto: cantidad}.
   Pista: recorrer la lista y, por cada producto, sumar 1 a su contador.
          Si el producto aun no esta en el diccionario, inicializalo en 1.

2) producto_mas_vendido(recuento:dict) -> str
   Devuelve el nombre del producto con mayor numero de ventas.

3) productos_con_minimo(recuento:dict, minimo:int) -> list
   Devuelve una lista con los nombres de productos cuya cantidad vendida
   es mayor o igual al minimo indicado.

4) total_unidades(recuento:dict) -> int
   Devuelve la suma total de unidades vendidas (suma de todos los valores).

5) registrar_compra(cliente:dict, producto:str, recuento:dict) -> None
   Registra una compra nueva. Dos efectos a la vez:
     a) Incrementa en 1 la cantidad de `producto` en `recuento`
        (mismo patron de contar_ventas, pero aplicado a una compra suelta).
     b) Incrementa en 1 el numero de pedidos del cliente
        REUTILIZANDO la funcion `registrar_pedido` importada de t010.
   No devuelve nada: modifica los diccionarios que recibe (ambos son
   mutables, se pasan por referencia).

EJEMPLOS:

    ventas = ["camiseta", "gorra", "camiseta", "pantalon",
              "camiseta", "gorra", "zapatillas"]

    recuento = contar_ventas(ventas)
    # {"camiseta": 3, "gorra": 2, "pantalon": 1, "zapatillas": 1}

    producto_mas_vendido(recuento)        # "camiseta"
    productos_con_minimo(recuento, 2)     # ["camiseta", "gorra"]
    total_unidades(recuento)              # 7

    # Integracion con t010 via imports:
    cliente = crear_cliente("Ana", "ana@mail.com", "Madrid")
    recuento_2 = {}
    registrar_compra(cliente, "camiseta", recuento_2)
    registrar_compra(cliente, "camiseta", recuento_2)
    registrar_compra(cliente, "gorra", recuento_2)
    # recuento_2 -> {"camiseta": 2, "gorra": 1}
    # cliente["pedidos"] -> 3
"""

# from t010 import create_client, register_order


# def count_sales(sales:list) -> dict:
#     ...

# def top_selling_product(tally:dict) -> str:
#     ...

# def products_above_minimum(tally:dict, minimum:int) -> list:
#     ...

# def total_units(tally:dict) -> int:
#     ...

# def register_purchase(client:dict, product:str, tally:dict) -> None:
#     ...


# --- Tests ---
# sales = ["t-shirt", "cap", "t-shirt", "trousers",
#          "t-shirt", "cap", "sneakers"]
# tally = count_sales(sales)
# print(tally)
# print(top_selling_product(tally))       # "t-shirt"
# print(products_above_minimum(tally, 2)) # ["t-shirt", "cap"]
# print(total_units(tally))               # 7
#
# # Integration test with t010
# client = create_client("Ana", "ana@mail.com", "Madrid")
# tally_2 = {}
# register_purchase(client, "t-shirt", tally_2)
# register_purchase(client, "t-shirt", tally_2)
# register_purchase(client, "cap",     tally_2)
# print(tally_2)   # {"t-shirt": 2, "cap": 1}
# print(client)    # client["orders"] -> 3
