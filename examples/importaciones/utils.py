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