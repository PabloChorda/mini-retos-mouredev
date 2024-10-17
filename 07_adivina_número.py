"""
Crea un programa en el que el usuario debe adivinar un número 
aleatorio generado por la computadora.
git push 

"""

import random

def generar_numero_aleatorio(inicio: int, fin: int) -> int:
    """Genera un número aleatorio dentro del rango especificado"""
    return random.randint(inicio, fin)

def obtener_intento_usuario() -> int:
    """Solicita al usuario que adivine el número"""
    while True:
        try:
            intento = int(input("Adivina el número: "))
            return intento
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

def main():
    """Función principal para el juego de adivinar el número"""
    print("¡Bienvenido al juego de adivinar el número!")
    print("He escogido un número entre 1 y 100. ¡Intenta adivinarlo!")
    
    numero_secreto = generar_numero_aleatorio(1, 100)
    intentos = 0
    
    while True:
        intento = obtener_intento_usuario()
        intentos += 1
        
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break

if __name__ == "__main__":
    main()
