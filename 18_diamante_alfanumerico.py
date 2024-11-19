'''
RETO DIAMANTE ALFANUMÉRICO
Crea una función que dibuje un diamante alfanumérico 
basado en un número n de líneas.

En la parte superior, cada línea contiene números y letras alternados, 
comenzando desde "1" y "A", creciendo hacia los lados.
En la parte inferior, el patrón se invierte.
Cada línea está centrada con espacios iniciales para formar un diamante 
perfecto.

'''


def diamante_alfanumerico(n):
    for i in range(1, n + 1):
        # Espacios iniciales para centrar
        espacios = " " * (n - i)
        # Construir la línea de números y letras
        numeros = "".join(str(x) for x in range(1, i))
        letras = "".join(chr(65 + j) for j in range(i - 1))
        # Línea completa
        linea = numeros + letras + numeros[::-1]
        print(espacios + "1" + linea)
    
    for i in range(n - 1, 0, -1):
        # Espacios iniciales para centrar
        espacios = " " * (n - i)
        # Construir la línea de números y letras
        numeros = "".join(str(x) for x in range(1, i))
        letras = "".join(chr(65 + j) for j in range(i - 1))
        # Línea completa
        linea = numeros + letras + numeros[::-1]
        print(espacios + "1" + linea)

# Llama a la función con un número final
diamante_alfanumerico(5)
