'''
Ejercicio: Escape de la Mazmorra
Contexto: Un explorador (🧍) está atrapado en una mazmorra llena de trampas y tesoros. Su objetivo es llegar a la salida 🏁, evitando las trampas y recogiendo la mayor cantidad de tesoros 💎.
Requisitos:
La mazmorra es una cuadrícula de tamaño configurable (por ejemplo, 5x5).
El explorador comienza en la esquina superior izquierda (posición (0, 0)).
La salida está en la esquina inferior derecha (posición (N-1, N-1)).
Cada celda puede contener:
Un espacio vacío _.
Un tesoro 💎 (el explorador lo recoge al pasar).
Una trampa 💀 (si cae en una, pierde 1 vida).
El explorador tiene un total de 3 vidas. Si pierde todas las vidas, el juego termina.
El explorador puede moverse hacia la derecha o hacia abajo en cada turno.
Cada movimiento se realiza automáticamente, pero de forma aleatoria.
El objetivo es llegar a la salida con la mayor cantidad de tesoros posible y al menos 1 vida restante.
'''

import random
import os
import time

def dungeon_escape(grid_size: int):
    # Crear la mazmorra
    dungeon = create_dungeon(grid_size)

    # Posición inicial y variables del explorador
    explorer_pos = [0, 0]
    lives = 3
    treasures_collected = 0

    # Imprimir el estado inicial
    print_dungeon(dungeon, explorer_pos, treasures_collected, lives)

    while explorer_pos != [grid_size - 1, grid_size - 1] and lives > 0:
        time.sleep(1)

        # Decidir el próximo movimiento
        move = random.choice(["right", "down"])
        if move == "right" and explorer_pos[1] < grid_size - 1:
            explorer_pos[1] += 1
        elif move == "down" and explorer_pos[0] < grid_size - 1:
            explorer_pos[0] += 1

        # Interactuar con la celda
        cell_content = dungeon[explorer_pos[0]][explorer_pos[1]]
        if cell_content == "💎":
            treasures_collected += 1
            dungeon[explorer_pos[0]][explorer_pos[1]] = "_"
        elif cell_content == "💀":
            lives -= 1
            dungeon[explorer_pos[0]][explorer_pos[1]] = "_"

        # Imprimir el estado actual
        print_dungeon(dungeon, explorer_pos, treasures_collected, lives)

    # Resultado final
    if lives > 0:
        print(f"¡Has escapado de la mazmorra con {treasures_collected} tesoros! 🎉")
    else:
        print("Has perdido todas tus vidas y quedaste atrapado en la mazmorra. 😢")

def create_dungeon(grid_size: int) -> list:
    dungeon = []
    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            cell = random.choice(["_", "_", "_", "💎", "💀"])  # Mayor probabilidad de espacios vacíos
            row.append(cell)
        dungeon.append(row)
    
    # Garantizar que la entrada y salida sean seguras
    dungeon[0][0] = "_"
    dungeon[-1][-1] = "_"
    return dungeon

def print_dungeon(dungeon: list, explorer_pos: list, treasures: int, lives: int):
    os.system("clear")  # Usa "cls" si estás en Windows
    for i, row in enumerate(dungeon):
        for j, cell in enumerate(row):
            if [i, j] == explorer_pos:
                print("🧍", end=" ")
            else:
                print(cell, end=" ")
        print()
    print(f"Tesoros recogidos: {treasures}, Vidas restantes: {lives}")
    print()

# Ejecutar el juego con una mazmorra de 5x5
dungeon_escape(5)
