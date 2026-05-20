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

def validar_usuario (usuario:str) -> bool:
    if len(usuario) >= 6 and len(usuario) <= 12:
        for letra in usuario:
            if letra == int:
                continue
            elif letra.isupper():
                continue
    elif usuario == ("admin", "root", "pedro_sanchez"):
        pass