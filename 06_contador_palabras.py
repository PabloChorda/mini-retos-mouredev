"""
Crea un programa que cuente cuántas veces 
aparece cada palabra en una frase que el usuario introduzca.

"""

def contar_palabras(frase: str) -> dict:
    """Cuenta cuántas veces aparece cada palabra en la frase"""
    palabras = frase.lower().split()
    contador_palabras = {}

    for palabra in palabras:
        palabra = palabra.strip('.,!?"')  # Elimina signos de puntuación
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1

    return contador_palabras

def obtener_frase_usuario() -> str:
    """Solicita una frase al usuario"""
    return input("Introduce una frase: ")

def mostrar_conteo_palabras(conteo: dict):
    """Muestra el conteo de palabras al usuario"""
    print("\nConteo de palabras:")
    for palabra, cantidad in conteo.items():
        print(f"{palabra}: {cantidad}")

def main():
    """Función principal para contar las palabras en una frase"""
    frase = obtener_frase_usuario()
    conteo_palabras = contar_palabras(frase)
    mostrar_conteo_palabras(conteo_palabras)

if __name__ == "__main__":
    main()
