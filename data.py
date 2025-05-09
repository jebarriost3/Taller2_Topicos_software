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
    },
    {
        "id": 3,
        "nombre": "PokeneaAzul",
        "altura": 1.0,
        "habilidad": "Agua pura",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea3.png",    
        "frase_filosofica": "La calma del agua refleja la profundidad del alma."
    },
    {
        "id": 4,
        "nombre": "PokeneaAmarillo",
        "altura": 1.5,
        "habilidad": "Electricidad estática",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea4.png",
        "frase_filosofica": "La energía es la chispa de la vida."
    },
    {
        "id": 5,
        "nombre": "PokeneaNegro",
        "altura": 1.3,
        "habilidad": "Sombra eterna",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea5.png",
        "frase_filosofica": "En la oscuridad, la luz brilla más intensamente."
    },
    {
        "id": 6,
        "nombre": "PokeneaBlanco",
        "altura": 0.9,
        "habilidad": "Nieve eterna",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea6.png.png",
        "frase_filosofica": "La pureza de la nieve es un reflejo del alma."
    },
    {
        "id": 7,
        "nombre": "PokeneaRosa",
        "altura": 1.1,
        "habilidad": "Amor eterno",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea7.png",
        "frase_filosofica": "El amor es la fuerza más poderosa del universo."
    },
    {
        "id": 8,
        "nombre": "PokeneaMorado",
        "altura": 1.4,
        "habilidad": "Misterio eterno",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea8.png",
        "frase_filosofica": "El misterio es el alma de la curiosidad."
    },
    {
        "id": 9,
        "nombre": "PokeneaCyan",
        "altura": 1.6,
        "habilidad": "Agua helada",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea9.png",
        "frase_filosofica": "El agua fría es un refugio para el alma."
    },
    {
        "id": 10,
        "nombre": "PokeneaNaranja",
        "altura": 1.7,
        "habilidad": "Fuego ardiente",
        "imagen": "https://pokenea-imagenes-jebarriost.s3.us-east-1.amazonaws.com/pokenea10.png",
        "frase_filosofica": "El fuego ardiente es la pasión del alma."
    }
]

def obtener_pokenea_aleatoria():
    return random.choice(pokeneas)
