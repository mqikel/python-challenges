"""
CONTEXTO:
En una aplicacion para la gestion de facturas, el cliente necesita validar el IBAN de sus proveedores.
Para ello nos piden implementar una funcion que dado un posible IBAN valido, nos devuelva si este es o no valido.
Para que un IBAN se considere valido se deben atender a los siguientes requisitos:

REQUISITOS:
- Los numeros de cuenta (IBAN) solo pueden ser de uno de estos paises:
    - Bélgica
    - Francia
    - Suecia
    - Suiza
    - España
    - Hungría
- El IBAN debe tener una longitud especifica dependiendo del pais
- Los caracteres después del codigo de pais deben ser numericos
- Implementar funciones reutilizables:
    - validar_prefijo(prefijo)
    - es_valido(iban) -> usar dentro las funciones anteriores
- La funcion debe de devolver verdadero si es valido y falso cuando no lo sea

EJEMPLO:

Input:
ES7620770024003102575766

Output:
True


Input:
SE141234567890123456

Output:
False
"""
# PREFIJOS_VALIDOS = ["BE", "FR", "SE", "CH", "ES", "HU"]



# print(validar_prefijo("ES")) # --> los que devuelva
# print(validar_prefijo("FR")) # --> los que devuelva
# print(validar_prefijo("YH")) # --> los que devuelva


LONGITUD_VALIDA = [16, 27, 24, 21, 24, 28]
PREFIJOS_VALIDOS = ["BE", "FR", "SE", "CH", "ES", "HU"]


def indice_prefijo(prefijo:str) -> int:
    """
    Dado un valor (STR) determina el indice de un prefijo
    """
    try:
        indice = PREFIJOS_VALIDOS.index(prefijo)
    except:
        indice = -1
    return indice

def validar_iban(iban:str) -> bool:
    if indice_prefijo(iban[0:2]) >= 0:
        if len(iban) == LONGITUD_VALIDA[indice_prefijo(iban[0:2])]:
            return True
        else:
            return False
    else:
        return False


    
print(validar_iban("BE12345678901234"))
print(validar_iban("BE1234567890123490"))
print(validar_iban("JP12345678901234"))        
    

# PREFIJOS_VALIDOS.index(iban[0:2]) == len(LONGITUD_VALIDA.index(iban[0:2])):