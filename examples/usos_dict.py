# alumnos = ["Miguel", "Robert", "Maria"]
# notas = [12, 11, 1]

# nombre_alumno = input("Dame el nombre del alumno del que quieres saber la nota\n")

# if nombre_alumno in alumnos:
#     print(notas[alumnos.index(nombre_alumno)])
# else:
#     print("el alumno no existe")

# Esto no es lo optimo
# info_clase = {
#     "alumnos": ["Miguel", "Robert", "Maria"],
#     "notas": [12, 11, 1]
# }

# MEJOR MANERA
alumnos = {
    "Miguel": 12,
    "Robert": 11,
    "Maria": 1
}

nombre_alumno = input("Dame el nombre del alumno del que quieres saber la nota\n")

nota_alumno = alumnos.get(nombre_alumno)
if nota_alumno:
    print(f"Tu nota es: {nota_alumno}")
else:
    print("El alumno no existe")