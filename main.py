import random

nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)

puntaje = 0

preguntas = [
    {"pregunta": "¿Cuántos días tiene un año?", "respuesta": "365"},
    {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "paris"},
    {"pregunta": "¿Cuánto es 7 x 8?", "respuesta": "56"},
    {"pregunta": "¿En qué planeta vivimos?", "respuesta": "tierra"},
    {"pregunta": "¿Cuántos continentes hay?", "respuesta": "7"},
]

random.shuffle(preguntas)

for p in preguntas:
    respuesta = input(p["pregunta"] + " ").strip().lower()
    if respuesta == p["respuesta"]:
        print("¡Correcto!")
        puntaje += 1
    else:
        print("Incorrecto. La respuesta era: " + p["respuesta"])

print("Tu puntaje final es: " + str(puntaje) + " de " + str(len(preguntas)))
