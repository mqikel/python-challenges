# Crea una funcion que reciba nombre y apellido,
# y devuelva el nombre de usuario en minusculas separado por punto.,
# Ejemplo: crear_usuario("Carlos", "Garcia") -> "carlos.garcia",
# -- escribe tu funcion aqui arriba --,
# print(crear_usuario("Carlos", "Garcia"))  # carlos.garcia,
# print(crear_usuario("Carlos", "Garcia"))  # carlos.garcia,

def crear_usuario(nombre:str, apellido:str) -> str:
    return ".".join([nombre, apellido]).lower()
print(crear_usuario("Miguel", "Blanco"))




# Ejercicio 6b,
# Crea una funcion que reciba el precio base y el porcentaje de IVA,
# y devuelva el precio final con el IVA incluido.,
# Ejemplo: calcular_precio_final(100, 21) -> 121.0,
# -- escribe tu funcion aqui arriba --,
# print(calcular_precio_final(100, 21))    # 121.0

def calcular_precio_final(precio:float, iba:int) -> float:
     precio_iba = precio * 0.21
     precio_total = precio_iba + precio
     return precio_total
     
print(calcular_precio_final(100, 21))