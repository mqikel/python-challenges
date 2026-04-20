"""
Simulacro de bugfix y refactorizacion - Calculo de nominas

Contexto:
Este script se usa en una asesoria pequena para calcular un resumen rapido
de nominas y estimar la facturacion minima del mes.

Importante:
El codigo tiene errores metidos a proposito y tambien varias malas practicas
de programacion. La idea es que el alumno aprenda a:
- Leer codigo que no ha escrito.
- Encontrar excepciones y errores de logica.
- Detectar malas practicas simples.
- Refactorizar sin cambiar el objetivo del programa.

Tipos de problemas que hay dentro:
1. Error de ejecucion.
2. Errores de procesamiento.
3. Errores de formato o salida.
4. Casos limite mal resueltos.
5. Codigo repetido o poco claro.
6. Nombres de variables poco descriptivos.
7. Variables innecesarias.
8. Uso incorrecto de try/except demasiado amplio.

Sugerencia:
Primero haz que funcione. Despues mejora la legibilidad.
"""

lista_nombres: list[str] = [] 
lista_horas: list[int] = []  
lista_precio: list[float] = []  
lista_irpf: list[float] = []  
lista_bruto: list[float] = []
lista_retencion: list[float] = []
lista_neto: list[float] = []
lista_coste: list[float] = []                    

print("CALCULO MENSUAL DE NOMINAS")
print("--------------------------")

while True:
    try:
        numero_empleados = int(input("Cuantos empleados quieres registrar este mes? "))
        if numero_empleados <= 0:
            print("Solo numeros positivos que no sean 0")
            continue
        break  
    except:
        print("Porfavor introduzca un numero entero valido")

orden_empleados = 1
impuestos = 0.32

while orden_empleados <= numero_empleados:
    print("\nEmpleado " + str(orden_empleados))
    nombre_valido = False
    while nombre_valido != True:                                
        empleado : str = input("Nombre del empleado: ")
        if empleado.strip() == "":
            print("El nombre no puede estar vacio") 
        elif empleado.replace(" ","").isalpha():
            nombre_valido = True
        else:
            print("Porfavor introduce un nombre valido que solo tenga letras")
    lista_nombres.append(empleado)

    # while True:
    #     try:
    #         horas_mes = int(input("Horas trabajadas este mes: "))
    #         if horas_mes <= 0:
    #             print("No se admiten numero negativos")
    #             continue
    #         break
    #     except:
    #         print("Porfavor introduzca un numero valido")
    horas_mes = 0            
    while horas_mes <= 0:
        try:
            horas_mes = int(input("Horas trabajadas este mes: "))
            if horas_mes <= 0:
                print("Porfavor solo numeros positivos")                               
        except:
            print("Porfavor introduzca un numero valido")
    lista_horas.append(horas_mes)

    while True:
        try:
            precio = float(input("Precio por hora: "))
            if precio <= 0:
                print("Porfavor solo numeros positivos")
                continue
            break
        except:
            
            print("Solo numeros validos gracias")
    lista_precio.append(precio)

    while True:
        try:
            porcentaje = float(input("Porcentaje de retencion IRPF: "))
            if porcentaje < 0:
                print("Porfavor introduzca un numero valido para hacer el %")
                continue
            break
        except:
            print("Porfavor solo numeros")         
    lista_irpf.append(porcentaje)

    # Calculo de nomina.
    bruto = horas_mes * precio                          
    ret = bruto * porcentaje / 100
    neto = bruto - ret
    coste = bruto + bruto * impuestos    

    lista_bruto.append(bruto)
    lista_retencion.append(ret)
    lista_neto.append(neto)
    lista_coste.append(coste)         
    
    orden_empleados += 1                       

print("\nRESUMEN DE NOMINAS")
print("------------------")                                          
print("Empleados registrados:", len(lista_nombres))               
print("Total neto pagado:", sum(lista_neto, 2), "euros") 
print("Gasto total de empresa:", sum(lista_coste), "euros") 

media1 = sum(lista_coste) / len(lista_nombres)                                      
media2 = sum(lista_neto) / len(lista_nombres)                                 
print("Coste medio por empleado:", round(media1), "Euros")
print("Neto medio por empleado:", round(media2), "euros")

# La idea del script es estimar la facturacion minima si la empresa
# quiere conservar un 30 % de margen.

margen = 1.3  #1.3 seria el 30% + lo que ya tenemos de coste que seria el 100%                                                     
facturacion = sum(lista_coste) * margen                                                  
print("Facturacion minima recomendada:", round(facturacion, 2), "euros")         


print("\nDETALLE POR EMPLEADO")
print("--------------------")

variable_bucle = 0                                                          
while variable_bucle < len(lista_nombres):                                             
    print(
        str(variable_bucle + 1) + ". ", lista_nombres[variable_bucle]                       
        + " | Bruto: " + str(lista_bruto[variable_bucle]) + " euros"                  
        + " | Retencion: " + str(lista_retencion[variable_bucle]) + " euros"              
        + " | Neto: " + str(lista_neto[variable_bucle]) + " euros"
        + " | Coste empresa: " + str(lista_coste[variable_bucle]) + "euros"
    )
    variable_bucle += 1

# Se muestra el empleado mas caro para la empresa.
mayor = max(lista_coste)                           
pos = lista_coste.index(mayor)                    
print("\nEmpleado mas caro: " + lista_nombres[pos].upper() + " con un coste de " + str(mayor))         

                                       
