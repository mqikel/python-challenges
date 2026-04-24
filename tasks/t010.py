"""
TAREA t010 - FICHA DE CLIENTE (dificultad: FACIL)

CONTEXTO:
Estas trabajando en el backend de una mini tienda online. Todavia no hay
base de datos real: todo se guarda en memoria con estructuras de Python.
Tu primera mision es representar UN cliente y escribir las operaciones
basicas que cualquier app hace con sus usuarios: crear, mostrar, actualizar.

Un cliente tiene cuatro campos: nombre, email, ciudad y numero de pedidos
realizados (que arranca en 0).

ESTA ES LA BASE DE UNA SERIE:
Esta tarea es la primera de tres (t010, t011, t012). Las funciones que
hagas aqui las importaras desde las siguientes tareas para practicar el
concepto de REUTILIZACION via imports (igual que en un proyecto real).
Hazlas bien: otras tareas dependeran de ellas.

REQUISITOS GENERALES:
- Todo va dentro de una funcion. Nada de codigo suelto excepto las llamadas
  de prueba al final.
- Cada funcion lleva type hints (ej: `def nombre(param:str) -> dict:`).
- Antes de teclear: escribe en un comentario de 2-4 lineas que hace la
  funcion, que recibe y que devuelve.

FUNCIONES A IMPLEMENTAR:

1) crear_cliente(nombre:str, email:str, ciudad:str) -> dict
   Devuelve un diccionario con las 4 claves. El contador de pedidos
   empieza en 0.

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
"""


def crear_cliente(nombre:str, email:str, ciudad:str, pedidos:int) -> dict:
    """
    Esta función va a recoger la información de cada cliente
    y la va a convertir en un diccionario
    """
    cliente = {
        "nombre": nombre,
        "email": email,
        "ciudad": ciudad,
        "pedidos": pedidos
    }
    return cliente


def mostrar_cliente(cliente:dict) -> None:
    """
    Esta función va a mostrar los datos del cliente ya recogidos
    y transformados en diccionario
    """
    print(f"Nombre: {cliente["nombre"]}\n"
          f"Email: {cliente["email"]}\n"
          f"Ciudad: {cliente["ciudad"]}\n"
          f"Pedidos: {cliente["pedidos"]}\n")
    

def actualizar_ciudad(cliente:dict, nueva_ciudad:str) -> dict:
    """
    Esta función la utilizaremos para actualizar los datos de
    la nuevo ciudad en la que se encuentra el cliente
    """
    cliente["ciudad"] = nueva_ciudad
    return cliente


def registrar_pedido(cliente:dict) -> dict:
    """
    Con esta función vamos a sumar el numero de pedidos al apartado
    de pedidos del cliente
    """
    cliente_nuevo_pedido = {
        "nombre": cliente["nombre"],
        "email": cliente["email"],
        "ciudad": cliente["ciudad"],
        "pedidos": cliente["pedidos"]
    }
    cliente_nuevo_pedido["pedidos"] = cliente["pedidos"] + 1
    return cliente_nuevo_pedido
    
    
# --- Pruebas ---
cliente = crear_cliente("Ana", "ana@mail.com", "Madrid", 0)
cliente = actualizar_ciudad(cliente, "Valencia")
cliente = registrar_pedido(cliente)
cliente = registrar_pedido(cliente)
print(mostrar_cliente(cliente))




