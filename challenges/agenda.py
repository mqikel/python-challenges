# Una agenda simple de numbers

numbers = [
    {"name": "Ana García", "number": "612345678", "email": "ana@email.com"},
    {"name": "Carlos López", "number": "698765432", "email": "carlos@email.com"},
    {"name": "Marta Ruiz", "number": "655443322", "email": "marta@email.com"},
    {"name": "Pedro Martínez", "number": "677112233", "email": "pedro@email.com"},
    {"name": "Lucía Fernández", "number": "634556677", "email": "lucia@email.com"},
    {"name": "Jorge Sánchez", "number": "691234567", "email": "jorge@email.com"},
    {"name": "Elena Torres", "number": "658990011", "email": "elena@email.com"},
    {"name": "Raúl Gómez", "number": "623344556", "email": "raul@email.com"},
    {"name": "Sofía Jiménez", "number": "645678901", "email": "sofia@email.com"},
    {"name": "David Moreno", "number": "617889900", "email": "david@email.com"},
    {"name": "Isabel Romero", "number": "668001122", "email": "isabel@email.com"},
    {"name": "Andrés Navarro", "number": "603223344", "email": "andres@email.com"},
    {"name": "Carmen Vega", "number": "679445566", "email": "carmen@email.com"}
]

"""
    Ejercicio 1: Escríbeme una función llamada "show_numbers" que reciba la lista
    y muestre por pantalla el nombre, teléfono y email de cada contacto.

    INPUT: lista de numbers
    OUTPUT: print con la siguiente estructura

    Ana García | 612345678 | ana@email.com
    Carlos López | 698765432 | carlos@email.com
    Marta Ruiz | 655443322 | marta@email.com
"""

def show_numbers():
    for data in numbers:
        print(data["name"], "|", data["number"], "|", data["email"])





"""
    Ejercicio 2: Ahora escríbeme una función llamada "find_number" que reciba
    la lista y un nombre, y devuelva el diccionario del contacto
    si existe, o None si no existe.

    EJEMPLO:
    resultado = find_number(numbers, "Ana García")
    # → {"nombre": "Ana García", "number": "612345678", "email": "ana@email.com"}

    resultado = find_number(numbers, "Pedro")
    # → None
"""

def find_number(list:list, contact_name:str) -> dict:
    for register in list:
        if register["name"] == contact_name:
            return register
    return None


# resultado = find_number(numbers, "Ana Bohueles")
# print("+34", resultado["number"])

"""
    Ejercicio 3: Escríbeme una función llamada "add_number" que reciba la lista,
    un nombre, un teléfono y un email, y añada el nuevo contacto.
"""
def add_number(list:list, name:str, number:str, email:str) -> dict:
    new_number = {
        "name":name,
        "number":number,
        "email":email
    }
    return list.append(new_number)





"""
    Ejercicio 4: Escribe una función llamada "edit_number" que reciba la lista de numbers, el nombre del contacto
    y el nuevo numero a cambiar.

    EJEMPLO:
    update_number(numbers, "Ana García", "657899902")

"""

def edit_number(list:list, name:str, new_number:str):
    for register in list:
        if register["name"] == name:
            register["number"] = new_number
            break #Esta instruccion hace que el bucle termine al encontrar el registro