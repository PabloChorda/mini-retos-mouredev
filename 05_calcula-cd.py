def calcular_tmb(peso: float, altura: float, edad: int, sexo: str) -> float:
    """Calcula la Tasa Metabólica Basal (TMB) usando la fórmula de Mifflin-St Jeor"""
    if sexo.lower() == 'hombre':
        return 10 * peso + 6.25 * altura - 5 * edad + 5
    elif sexo.lower() == 'mujer':
        return 10 * peso + 6.25 * altura - 5 * edad - 161
    else:
        raise ValueError("Sexo no válido. Ingresa 'hombre' o 'mujer'.")

def obtener_factor_actividad() -> float:
    """Solicita el nivel de actividad física del usuario y devuelve el factor correspondiente"""
    niveles = {
        1: 1.2,  # Sedentario
        2: 1.375,  # Ligero (ejercicio ligero)
        3: 1.55,  # Moderado (ejercicio moderado)
        4: 1.725,  # Activo (ejercicio intenso)
        5: 1.9  # Muy activo (ejercicio muy intenso)
    }
    while True:
        try:
            print("Selecciona tu nivel de actividad física:")
            print("1. Sedentario (poco o nada de ejercicio)")
            print("2. Ligero (ejercicio ligero 1-3 días por semana)")
            print("3. Moderado (ejercicio moderado 3-5 días por semana)")
            print("4. Activo (ejercicio intenso 6-7 días por semana)")
            print("5. Muy activo (ejercicio muy intenso o trabajo físico")
            nivel = int(input("Nivel de actividad (1-5): "))
            return niveles[nivel]
        except KeyError:
            print("Por favor, selecciona un nivel válido.")

def obtener_datos_usuario() -> tuple:
    """Solicita y valida los datos básicos ingresados por el usuario"""
    while True:
        try:
            peso = float(input("Peso en Kg: "))
            altura = float(input("Altura en cm: "))
            edad = int(input("Edad en años: "))
            sexo = input("Sexo (hombre/mujer): ").lower()
            if peso <= 0 or altura <= 0 or edad <= 0:
                print("Por favor, ingresa valores mayores a 0.")
                continue
            return peso, altura, edad, sexo
        except ValueError:
            print("Entrada no válida. Por favor ingresa los datos correctamente.")

def main():
    """Función principal para calcular y mostrar las calorías diarias recomendadas"""
    peso, altura, edad, sexo = obtener_datos_usuario()
    tmb = calcular_tmb(peso, altura, edad, sexo)
    factor_actividad = obtener_factor_actividad()
    calorias_diarias = tmb * factor_actividad

    print(f"Tu TMB es: {tmb:.2f} calorías/día")
    print(f"Calorías diarias recomendadas según tu nivel de actividad: {calorias_diarias:.2f}")

if __name__ == "__main__":
    main()
