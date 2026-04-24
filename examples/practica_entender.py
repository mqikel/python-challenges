PREFIJOS_VALIDOS = ["BE", "FR", "ES"]
LONGITUDES_VALIDAS = [12, 24, 45]

def validar_prefijo(prefijo:str) -> bool: 
    return prefijo in PREFIJOS_VALIDOS

iban = "ES141234567890123456"
prefijo_iban = "BE"

if validar_prefijo(prefijo_iban):
    print("--LONGITUD VALIDA PARA PREFIJO BELGICA--")
    print(LONGITUDES_VALIDAS[PREFIJOS_VALIDOS.index(prefijo_iban)])
else:
    print("PREEFIJO INVALIDO, prueba con otro valor")