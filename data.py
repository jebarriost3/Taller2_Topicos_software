import random

pokeneas = [
    {
        "id": 1,
        "nombre": "PokeneaRoja",
        "altura": 1.2,
        "habilidad": "Fuego eterno",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea1.png",
        "frase_filosofica": "El fuego que ilumina también puede consumir."
    },
    {
        "id": 2,
        "nombre": "PokeneaVerde",
        "altura": 0.8,
        "habilidad": "Regeneración",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea2.png",
        "frase_filosofica": "Cada hoja caída es una lección."
    }
]


def obtener_pokenea_aleatoria():
    return random.choice(pokeneas)
