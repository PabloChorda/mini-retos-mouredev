'''
RETO TABLERO EN ESPIRAL
Crea una función que genere un tablero numérico en forma de espiral, 
partiendo desde el número 1 en el centro y avanzando hacia afuera en 
sentido horario.

'''

def tablero_espiral(n):
    if n % 2 == 0:
        raise ValueError("El tamaño del tablero debe ser impar.")
    
    # Crear un tablero vacío
    tablero = [[0] * n for _ in range(n)]
    
    # Coordenadas iniciales en el centro
    x, y = n // 2, n // 2
    
    # Rellenar en espiral
    numero = 1
    tablero[x][y] = numero
    numero += 1
    
    # Direcciones: derecha, abajo, izquierda, arriba
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    paso = 1  # Cantidad de pasos antes de cambiar de dirección
    
    while numero <= n * n:
        for direccion in direcciones:
            for _ in range(paso):
                # Avanzar en la dirección actual
                x += direccion[0]
                y += direccion[1]
                
                if 0 <= x < n and 0 <= y < n:
                    tablero[x][y] = numero
                    numero += 1
                    if numero > n * n:
                        break
            
            if direccion in [(0, -1), (0, 1)]:  # Incrementar paso tras dos direcciones
                paso += 1
    
    # Imprimir el tablero
    for fila in tablero:
        print("  ".join(f"{num:2}" for num in fila))

# Llamar a la función con un tamaño de tablero impar
tablero_espiral(5)
