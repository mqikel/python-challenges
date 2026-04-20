###
# TAREA VICTOR PEDIDOS #
try:
    num_pedidos = int(input("Cuantos pedidos tiene el señor cliente\n"))
    total = 0
    if num_pedidos == 1:
        num_articulos = int(input(f"Digame cuantos productos tiene en el pedido numero {num_pedidos}\n"))
        total_articulo = 0
        while num_articulos > 0:
            precio_articulo = int(input(f"Cuanto cuesta el articulo {num_articulos}\n"))
            num_articulos -=1
            total_articulo += precio_articulo
        total += total_articulo
        num_pedidos -= 1

    while num_pedidos > 0:
        num_articulos = int(input(f"Digame cuantos productos tiene en el pedido numero {num_pedidos}\n"))
        total_articulo = 0
        while num_articulos > 0:
            precio_articulo = int(input(f"Cuanto cuesta el articulo {num_articulos}\n"))
            num_articulos -=1
            total_articulo += precio_articulo
        total += total_articulo
        print("El precio total de este pedido es:", total_articulo, "euros")
        num_pedidos -= 1
    print("El precio total sería:", total, "euros" )

except:
    print("Porfavor introduzca unicamente numeros enteros positivos gracias")
    
