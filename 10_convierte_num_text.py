def convertir_numero_a_texto(numero: int) -> str:
    """Convierte un número entero (entre 0 y 99) a su representación en palabras"""
    unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = {10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince", 
                  16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve"}

    if numero < 10:
        return unidades[numero]
    elif 10 <= numero < 20:
        return especiales[numero]
    else:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return decenas[decena]
        elif decena == 2 and unidad != 0:
            return f"veinti{unidades[unidad]}"
        else:
            return f"{decenas[decena]} y {unidades[unidad]}"

def obtener_numero_usuario() -> int:
    """Solicita al usuario un número entero"""
    while True:
        try:
            numero = int(input("Introduce un número entre 0 y 99: "))
            if 0 <= numero <= 99:
                return numero
            else:
                print("Por favor, ingresa un número entre 0 y 99.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número entero.")

def main():
    """Función principal para convertir un número a su representación en palabras"""
    numero = obtener_numero_usuario()
    texto = convertir_numero_a_texto(numero)
    print(f"El número {numero} en palabras es: '{texto}'")

if __name__ == "__main__":
    main()
