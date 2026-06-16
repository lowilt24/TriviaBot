import random
import html
import requests

def obtener_preguntas():

    url = "https://opentdb.com/api.php?amount=5&type=multiple"
    try:
        datos = requests.get(url).json()
    except(requests.RequestException):
        print("Error: No se pudo conectar con el servidor.")
        return []

    preguntas = []

    for r in datos["results"]:
        opciones = [r["correct_answer"]] + r["incorrect_answers"]
        random.shuffle(opciones)

        preguntas.append({
            "pregunta": html.unescape(r["question"]),
            "categoria": html.unescape(r["category"]),
            "opciones": [html.unescape(o) for o in opciones],
            "respuesta": html.unescape(r["correct_answer"]),
        })
    
    return preguntas

def hacer_pregunta(p):
    print(f"\n[{p['categoria']}] {p['pregunta']}")

    for i, opcion in enumerate(p["opciones"], start=1):
            print(f"  {i}) {opcion}")

    eleccion = input("Tu respuesta (1-4): ").strip()

    try:
        return p["opciones"][int(eleccion) - 1] == p["respuesta"]
    except(ValueError, IndexError):
        print("Error: Seleccione un número válido")
        return False

nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}")

puntaje = 0

preguntas = obtener_preguntas()

random.shuffle(preguntas)

for p in preguntas:
    if hacer_pregunta(p):
        print("¡Correcto!")
        puntaje += 1
    else:
        print(f"La respuesta era: {p['respuesta']}")

print(f"Tu puntaje final es: {puntaje} de {len(preguntas)}")
