"""
Simulacro de bugfix - Registro de pedidos

Contexto:
Este script se usa para anotar pedidos de una tienda pequena al final del dia.
El objetivo es registrar los datos basicos de cada pedido y sacar un resumen
rapido para revisar la facturacion.

Importante:
El programa contiene errores metidos a proposito para practicar bugfix.
La idea es que el alumno trabaje como si recibiera codigo real de otra persona.

Capas de errores que deberia encontrar:
1. Un error de ejecucion que rompe el programa.
2. Errores de procesamiento que hacen que los datos salgan mal.
3. Errores de formato o salida.
4. Casos limite mal resueltos.

Sugerencia de pruebas:
- Probar con 2 o 3 pedidos normales.
- Probar con 0 pedidos.
- Probar con importes decimales.
- Probar con un pedido cancelado.
- Probar con nombres de cliente vacios.
"""

# Guardamos la informacion del dia en listas separadas porque es el formato
# con el que trabaja este script antiguo.
clientes = []
importes = []
estados = []

print("REGISTRO DE PEDIDOS DEL DIA")
print("---------------------------")

# El encargado indica cuantos pedidos quiere cargar.
cantidad_pedidos = int(input("Cuantos pedidos quieres registrar hoy? "))

pedido_actual = 1
total_facturado = 0
pedidos_activos = 0

# Se registran los pedidos uno a uno.
while pedido_actual <= cantidad_pedidos:
    print("\nCargando pedido " + str(pedido_actual))

    nombre_cliente = input("Nombre del cliente: ")
    if nombre_cliente == "":
        print("Porfavor introduzca un nombre") #tengo que meter un bucle while pero no se como hacerlo sin que sea infinito
    clientes.append(nombre_cliente)
     
    importe_pedido = float(input("Importe del pedido: "))
    importes.append(importe_pedido)

    # if importe_pedido == type(str):
    #     print("Porfavor introduzca un numero entero o decimal valido, en caso de decimal utilice el punto para la separacion")

    estado_pedido = input("Estado del pedido (pendiente, enviado, cancelado): ")
    estados.append(estado_pedido)

    # Solo se deberia facturar lo que no esta cancelado.
    if estado_pedido != "cancelado":
        total_facturado += importe_pedido
        pedidos_activos += 1

    pedido_actual += 1

print("\nRESUMEN DEL DIA")
print("---------------------------")
print("Pedidos registrados:", len(clientes))
print("Pedidos activos:", pedidos_activos)
print("Total facturado:", round(total_facturado, 2), "euros")

# El ticket medio se calcula solo con pedidos activos.
if total_facturado == 0:
    print("Ticket medio: 0 euros")
elif total_facturado > 0: 
    ticket_medio = total_facturado / pedidos_activos
    print("Ticket medio:", round(ticket_medio), "Euros")


print("\nLISTADO FINAL")
print("---------------------------")

indice = 0
while indice < len(clientes):  
    print(                                          
        str(indice + 1) + ". Cliente: " + str(clientes[indice])
        + " | Importe: " + str(importes[indice]) + " euros"
        + " | Estado: " + str(estados[indice])
    )
    indice += 1

# Se marca el cliente con pedido mas alto para revision comercial.
if importes == True:
    importe_maximo = max(importes)
    posicion_maxima = importes.index(importe_maximo)
    print("\nPedido mas alto:" + clientes[posicion_maxima] + " con " + str(importe_maximo) + " euros")





