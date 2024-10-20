"""
EL FAMOSO "FIZZ BUZZ"
Crea programa que muestre por consola (con un print) los números 
de 1 al 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz"
Múltiplos de 5 por la palabra "buzz"
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""

for number in range(1, 101):
    output = ""
    if number % 3 == 0:
        output += "fizz"
    if number % 5 == 0:
        output += "buzz"
    
    print(output or number)