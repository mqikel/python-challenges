# Ejercicio: convertir una variable en camelCase a snake_case.,
# Dado un string con nombre en camelCase, generar una nueva cadena con guiones bajos,
# antes de cada letra mayúscula y con todas las letras en minúsculas.,
# "laMamaDeHugoMePone" -> "la_mama_de_hugo_pone_cachondo",
# texto_camel = input("Dame tu texto en camelCase")


# texto_camel:str = input("Dame un texto en camelCase graciosillo\n")
# nuevo_texto = ""
# for letra in texto_camel:
#     if letra.isupper() and letra != texto_camel[0]:
#         nuevo_texto += "_" + letra
#     else:
#         nuevo_texto += letra
         
# print(nuevo_texto.lower())

def to_snake_case(texto:str) -> str:
    nuevo_texto = ""
    for letra in texto:
        if letra.isupper() and letra != texto[0]:
            nuevo_texto += "_" + letra
        else:
            nuevo_texto += letra
    return nuevo_texto.lower()

print(to_snake_case("LaMamaDelInnombrableEsUnaBellisimaPersona"))