'''
Crea una función que simule una batalla entre dos jugadores lanzando dados. Ambos jugadores tienen un número inicial de puntos, y el juego funciona de la siguiente manera:

Cada jugador lanza dos dados (valores aleatorios entre 1 y 6).
El jugador con el resultado más alto en su turno le quita puntos al otro jugador, 
igual a la diferencia entre los totales de los dados.
Si hay empate, no se pierde ni se gana puntos en el turno.
El juego continúa hasta que uno de los jugadores tenga 0 puntos o menos.
Muestra el ganador y cada turno del juego.
'''

import random

def batalla_de_dados(puntos_jugador1, puntos_jugador2):
    turno = 1
    
    while puntos_jugador1 > 0 and puntos_jugador2 > 0:
        print(f"\n--- Turno {turno} ---")
        
        # Lanzar dados para ambos jugadores
        dados_j1 = random.randint(1, 6) + random.randint(1, 6)
        dados_j2 = random.randint(1, 6) + random.randint(1, 6)
        
        print(f"Jugador 1 lanza: {dados_j1}")
        print(f"Jugador 2 lanza: {dados_j2}")
        
        # Comparar resultados y ajustar puntos
        if dados_j1 > dados_j2:
            daño = dados_j1 - dados_j2
            puntos_jugador2 -= daño
            print(f"Jugador 1 gana el turno y causa {daño} de daño. Puntos jugador 2: {puntos_jugador2}")
        elif dados_j2 > dados_j1:
            daño = dados_j2 - dados_j1
            puntos_jugador1 -= daño
            print(f"Jugador 2 gana el turno y causa {daño} de daño. Puntos jugador 1: {puntos_jugador1}")
        else:
            print("Empate, nadie pierde puntos.")
        
        turno += 1
    
    # Determinar el ganador
    print("\n--- FIN DEL JUEGO ---")
    if puntos_jugador1 <= 0:
        print("¡Jugador 2 gana la batalla!")
    else:
        print("¡Jugador 1 gana la batalla!")

# Iniciar el juego con 50 puntos para cada jugador
batalla_de_dados(50, 50)
