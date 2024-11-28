"""
Reglas del reto:
- Un grupo de astronautas está reparando partes de una nave espacial averiada.
- Cada turno, cada astronauta repara una cantidad aleatoria de daños entre 1 y 5 puntos.
- El objetivo es reparar completamente la nave (cantidad de puntos de daño definida por el usuario).
- La misión termina cuando los daños totales reparados alcanzan o superan la cantidad necesaria.
- Muestra el progreso de cada astronauta y el estado general de la reparación en cada turno.
"""

import random
import time

def reparacion_nave(num_astronautas, puntos_dano):
    # Crear una lista para los puntos de daño reparados por cada astronauta
    reparaciones = [0] * num_astronautas
    total_reparado = 0
    turno = 1

    print("¡Comienza la misión de reparación de la nave espacial!\n")
    time.sleep(1)

    while total_reparado < puntos_dano:
        print(f"--- Turno {turno} ---")
        for i in range(num_astronautas):
            reparacion = random.randint(1, 5)
            reparaciones[i] += reparacion
            total_reparado += reparacion
            if total_reparado >= puntos_dano:
                break
            print(f"Astronauta {i + 1} repara {reparacion} puntos. Total reparado: {reparaciones[i]} puntos.")
        
        print(f"\nEstado general: {total_reparado}/{puntos_dano} puntos reparados.\n")
        print("=" * 40)
        time.sleep(1)
        turno += 1

    # Determinar el astronauta que más contribuyó
    max_reparador = reparaciones.index(max(reparaciones)) + 1
    print("\n¡La nave ha sido reparada completamente!")
    print(f"Astronauta {max_reparador} fue quien más reparó, con {max(reparaciones)} puntos contribuidos.")
    print("\nEstado final de la misión:")
    for i, reparacion in enumerate(reparaciones):
        print(f"Astronauta {i + 1}: {reparacion} puntos reparados.")

# Configurar la misión
num_astronautas = int(input("¿Cuántos astronautas están participando en la misión? "))
puntos_dano = int(input("¿Cuántos puntos de daño tiene la nave? "))

# Ejecutar la misión
reparacion_nave(num_astronautas, puntos_dano)
