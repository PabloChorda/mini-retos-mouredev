"""
Crea un programa que calcule el precio final
de un producto aplicando un descuento
"""

def calcular_precio_final(precio_original: float, porcentaje_descuento: float) -> float:
    """Calcula el precio final de un producto después de aplicar un descuento"""
    descuento = (porcentaje_descuento / 100) * precio_original
    precio_final = precio_original - descuento
    return precio_final

def obtener_datos_producto() -> tuple:
    """Solicita y valida el precio original y el descuento ingresados por el usuario"""
    while True:
        try:
            precio_original = float(input("Introduce el precio original del producto: "))
            porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))
            if precio_original < 0 or porcentaje_descuento < 0:
                print("Por favor, ingresa valores mayores o iguales a 0.")
                continue
            return precio_original, porcentaje_descuento
        except ValueError:
            print("Entrada no válida. Por favor ingresa números.")

def main():
    """Función principal para calcular el precio final de un producto"""
    precio_original, porcentaje_descuento = obtener_datos_producto()
    precio_final = calcular_precio_final(precio_original, porcentaje_descuento)

    print(f"Precio original: ${precio_original:.2f}")
    print(f"Descuento aplicado: {porcentaje_descuento}%")
    print(f"Precio final con descuento: ${precio_final:.2f}")

if __name__ == "__main__":
    main()
