"""
Reglas del reto:
- Hay un grupo de personas intentando cruzar un río utilizando una balsa.
- Cada turno, una persona se sube a la balsa y la mueve una distancia aleatoria entre 1 y 5 metros.
- La balsa puede transportar a una sola persona a la vez.
- El objetivo es cruzar una distancia total definida por el usuario para llegar al otro lado del río.
- Muestra el progreso de cada turno y declara quién logra llegar al otro lado primero.
"""

import random
import time

def cruce_del_rio(num_personas, distancia_total):
    # Crear una lista para las distancias recorridas por cada persona
    distancias = [0] * num_personas
    turno = 1

    print("¡Comienza el cruce del río!\n")
    time.sleep(1)

    while max(distancias) < distancia_total:
        print(f"--- Turno {turno} ---")
        # Elegir una persona al azar para mover la balsa
        persona_actual = random.randint(0, num_personas - 1)
        avance = random.randint(1, 5)
        distancias[persona_actual] += avance
        print(f"La persona {persona_actual + 1} mueve la balsa {avance} metros. Total: {distancias[persona_actual]} metros.")

        print("\n" + "=" * 40 + "\n")
        time.sleep(1)
        turno += 1

    # Determinar el ganador
    ganador = distancias.index(max(distancias)) + 1
    print(f"¡La persona {ganador} ha cruzado el río primero!")
    print("\nEstado final del cruce:")
    for i, distancia in enumerate(distancias):
        print(f"Persona {i + 1}: {distancia} metros.")

# Configurar el cruce
num_personas = int(input("¿Cuántas personas están cruzando el río? "))
distancia_total = int(input("¿Cuál es la distancia total para cruzar el río? "))

# Ejecutar el cruce
cruce_del_rio(num_personas, distancia_total)
