from utils import crear_cliente, registrar_pedido, actualizar_ciudad, mostrar_cliente
from data import juan as juanillo

juan = crear_cliente("Juan","juan@email.com","Malaga", 2)
juan2 = crear_cliente("Juan","juan@email.com","Malaga", 2)
juan3 = crear_cliente("Juan","juan@email.com","Malaga", 2)
juan4 = crear_cliente("Juan","juan@email.com","Malaga", 2)
juan5 = crear_cliente("Juan","juan@email.com","Malaga", 2)
juan6 = crear_cliente("Juan","juan@email.com","Malaga", 2)


list_clientes = [juan, juan2, juan3, juan4, juan5, juan6]

for cliente in list_clientes:
    if cliente["nombre"] == "juan":
        cliente = registrar_pedido(cliente)
    
    if cliente["ciudad"] == "Sevilla":
        cliente = actualizar_ciudad(cliente, "Dos hermanas")

mostrar_cliente(juanillo)


