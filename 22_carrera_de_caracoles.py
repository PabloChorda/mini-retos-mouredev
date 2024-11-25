"""
Reglas del reto:
Hay varios caracoles compitiendo (puedes definir cuántos).
Cada turno, cada caracol avanza una distancia aleatoria entre 1 y 5 unidades.
La carrera se detiene cuando un caracol llega o supera la meta (definida por el usuario).
Muestra el estado de la carrera en cada turno.
"""


import random
import time

def carrera_caracoles(num_caracoles, distancia_meta):
    # Crear una lista para la posición de cada caracol
    posiciones = [0] * num_caracoles
    turno = 1
    
    print("¡Comienza la carrera de caracoles!\n")
    time.sleep(1)
    
    while max(posiciones) < distancia_meta:
        print(f"--- Turno {turno} ---")
        for i in range(num_caracoles):
            avance = random.randint(1, 5)
            posiciones[i] += avance
            print(f"Caracol {i + 1} avanza {avance} pasos. Total: {posiciones[i]}")
        
        print("\n" + "="*40 + "\n")
        time.sleep(1)
        turno += 1
    
    # Determinar el ganador
    ganador = posiciones.index(max(posiciones)) + 1
    print(f"¡El caracol {ganador} ha ganado la carrera!")
    print("¡Felicidades al ganador!")
    print("\nEstado final:")
    for i, pos in enumerate(posiciones):
        print(f"Caracol {i + 1}: {pos} pasos.")

# Configurar la carrera
num_caracoles = int(input("¿Cuántos caracoles compiten? "))
distancia_meta = int(input("¿Cuántos pasos son necesarios para ganar? "))

# Ejecutar la carrera
carrera_caracoles(num_caracoles, distancia_meta)
