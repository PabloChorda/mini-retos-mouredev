"""
Crea un programa que permita al usuario jugar 
una partida de "Piedra, Papel o Tijeras" contra la computadora.
"""

import random

def obtener_eleccion_computadora() -> str:
    """La computadora elige aleatoriamente piedra, papel o tijeras"""
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def obtener_eleccion_usuario() -> str:
    """Solicita al usuario que elija entre piedra, papel o tijeras"""
    while True:
        eleccion = input("Elige piedra, papel o tijeras: ").lower()
        if eleccion in ["piedra", "papel", "tijeras"]:
            return eleccion
        else:
            print("Opción no válida, por favor elige piedra, papel o tijeras.")

def determinar_ganador(eleccion_usuario: str, eleccion_computadora: str) -> str:
    """Determina el ganador del juego"""
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def main():
    """Función principal para jugar una partida de piedra, papel o tijeras"""
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_computadora = obtener_eleccion_computadora()

    print(f"\nTú elegiste: {eleccion_usuario}")
    print(f"La computadora eligió: {eleccion_computadora}")

    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print(f"\nResultado: {resultado}")

if __name__ == "__main__":
    main()
