'''
Generador y Resolvedor de Laberintos
Descripción:
Crea un programa que genere un laberinto aleatorio en una cuadrícula, 
permita al usuario visualizarlo y resuelva automáticamente el laberinto utilizando un algoritmo de búsqueda (como búsqueda en profundidad o A*).

Requisitos del programa:

Generación del laberinto:

Crea un laberinto en una cuadrícula de tamaño definido (por ejemplo, 10x10).
La cuadrícula debe tener muros (#) y caminos ( ), con una entrada (E) y una salida (S) aleatorias.
Interacción del usuario:

Muestra el laberinto generado en la consola.
Pregunta al usuario si desea resolver el laberinto automáticamente.
Resolución automática:

Implementa un algoritmo (por ejemplo, búsqueda en profundidad) para encontrar el camino más corto desde la entrada hasta la salida.
Muestra el laberinto con el camino recorrido marcado, por ejemplo, con *.
Salida esperada:

Generación del laberinto aleatorio.
Opción para el usuario de ver el laberinto resuelto automáticamente.
Representación gráfica del laberinto en consola.

'''
import random

# Dimensiones del laberinto
TAMANO = 10

# Función para generar el laberinto
def generar_laberinto(tamano):
    laberinto = [["#" for _ in range(tamano)] for _ in range(tamano)]

    # Crear caminos aleatorios
    for i in range(1, tamano - 1):
        for j in range(1, tamano - 1):
            if random.random() < 0.7:  # 70% de probabilidad de ser camino
                laberinto[i][j] = " "

    # Añadir entrada y salida
    entrada = (0, random.randint(1, tamano - 2))
    salida = (tamano - 1, random.randint(1, tamano - 2))
    laberinto[entrada[0]][entrada[1]] = "E"
    laberinto[salida[0]][salida[1]] = "S"

    return laberinto, entrada, salida

# Función para imprimir el laberinto
def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print("".join(fila))

# Algoritmo para resolver el laberinto (búsqueda en profundidad)
def resolver_laberinto(laberinto, entrada, salida):
    filas, columnas = len(laberinto), len(laberinto[0])
    visitados = set()
    camino = []

    def dfs(x, y):
        if (x, y) == salida:
            return True

        # Marcar la posición como visitada
        visitados.add((x, y))

        # Movimientos posibles (arriba, abajo, izquierda, derecha)
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            # Verificar límites y si es un camino válido
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] != "#" and (nx, ny) not in visitados:
                camino.append((nx, ny))  # Añadir al camino
                if dfs(nx, ny):
                    return True
                camino.pop()  # Retroceder si no lleva a la solución

        return False

    dfs(*entrada)

    # Marcar el camino en el laberinto
    for x, y in camino:
        if laberinto[x][y] == " ":
            laberinto[x][y] = "*"

    return laberinto

# Función principal
def simulador_laberinto():
    # Generar laberinto
    laberinto, entrada, salida = generar_laberinto(TAMANO)

    print("\n--- Laberinto Generado ---")
    imprimir_laberinto(laberinto)

    opcion = input("\n¿Quieres resolver el laberinto automáticamente? (s/n): ").lower()
    if opcion == "s":
        print("\n--- Resolviendo Laberinto ---")
        laberinto_resuelto = resolver_laberinto(laberinto, entrada, salida)
        imprimir_laberinto(laberinto_resuelto)
        print("✔️ Laberinto resuelto con éxito.")
    else:
        print("👋 ¡Gracias por jugar!")

# Ejecutar el programa
simulador_laberinto()
