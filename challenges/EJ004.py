"""
Un videojuego online necesita validar nombres de usuario antes de registrarlos en el sistema.
Crea una función que valide los siguientes nombres de usuarios:
"""
usuarios = [
    "TitanGamer7",
    "IronLiftX9",
    "ShadowPlayer21",
    "PixelWarrior5",
    "MegaHunter88",
    "AtlasPower4",
    "CyberKnight12",
    "AlphaStriker3",
    "DragonSlayer77",
    "SpeedRunnerX2",
    "IronCore99",
    "NovaFighter6",
    "SteelChampion1",
    "RogueSniper44",
    "TitanForce8",
    "GamerElite55",
    "PowerBuilder9",
    "ThunderStrike22",
    "CodeMaster11",
    "DarkPhantom33",
    "LiftLegend10",
    "VelocityHero66",
    "MatrixPlayer7",
    "QuantumRider2",
    "SpartanMode5"
]

def existe_usuario(usuario:str) -> bool:
    return usuario in usuarios


def validar_usuario (usuario:str) -> bool:
    tiene_mayus = False
    tiene_num = False
    palabras_prohibidas = ["admin", "root", "pedro_sanchez"]
    if existe_usuario(usuario) == False:
        if " " in usuario:
            return False
        for palabra in palabras_prohibidas:
            if palabra in usuario:
                return False
        if len(usuario) >= 6 and len(usuario) <= 12:
            for character in usuario:
                if character.isdigit():
                    tiene_num = True
                if character.isupper():
                    tiene_mayus = True
            return tiene_mayus and tiene_num
    else:
        return False
    
                

print(validar_usuario("SpartanMode5"))
print(validar_usuario("juan perez"))
print(validar_usuario("admin_juan"))
print(validar_usuario("Trigger24"))
print(validar_usuario("Trigger"))
print(validar_usuario("trigger1"))


