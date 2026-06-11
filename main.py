import random
import json

def hacer_pregunta(p):
    texto = f"[{p['categoria']}] {p['pregunta']}"
    respuesta = input(texto + " ").strip().lower()
    return respuesta == p["respuesta"]

nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}")

puntaje = 0

with open("questions.json", encoding="utf-8") as archivo:
    preguntas = json.load(archivo)

random.shuffle(preguntas)

for p in preguntas:
    if hacer_pregunta(p):
        print("¡Correcto!")
        puntaje += 1
    else:
        print(f"La respuesta era: {p['respuesta']}")

print(f"Tu puntaje final es: {puntaje} de {len(preguntas)}")
