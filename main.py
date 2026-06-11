import random

def hacer_pregunta(p):
    texto = f"[{p['categoria']}] {p['pregunta']}"
    respuesta = input(texto + " ").strip().lower()
    return respuesta == p["respuesta"]

nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}")

puntaje = 0

preguntas = [
    {"pregunta": "¿Cuántos días tiene un año?", "respuesta": "365", "categoria": "ciencia"},
    {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "paris", "categoria": "geografia"},
    {"pregunta": "¿Cuánto es 7 x 8?", "respuesta": "56", "categoria": "matematicas"},
    {"pregunta": "¿En qué planeta vivimos?", "respuesta": "tierra", "categoria": "ciencia"},
    {"pregunta": "¿Cuántos continentes hay?", "respuesta": "7", "categoria": "geografia"},
]

random.shuffle(preguntas)

for p in preguntas:
    if hacer_pregunta(p):
        print("¡Correcto!")
        puntaje += 1
    else:
        print(f"La respuesta era: {p['respuesta']}")

print(f"Tu puntaje final es: {puntaje} de {len(preguntas)}")
