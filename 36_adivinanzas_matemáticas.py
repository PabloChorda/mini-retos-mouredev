'''
Crea un juego interactivo por terminal en el que tendrás que adivinar 
el resultado de diferentes
operaciones matemáticas aleatorias (suma, resta, multiplicación 
o división de dos números enteros).
Tendrás 3 segundos para responder correctamente.
El juego finaliza si no se logra responder en ese tiempo.
Al finalizar el juego debes mostrar cuántos cálculos has acertado.
Cada 5 aciertos debes aumentar en uno el posible número de cifras 
de la operación (cada vez en un operando):
Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
Preguntas 11 a 15: XX operación YY
Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
'''

import random
import threading


def random_int(digits) -> int:
    return random.randint(0, 10**digits - 1)


def input_with_timeout():

    def on_timeout():
        print("\n¡El tiempo ha finalizado! Pulsa enter.")
        global game_on
        game_on = False

    timer = threading.Timer(3, on_timeout)
    timer.start()

    try:
        answer = input(f"¿Cuál es el resultado de {num1} {operation} {num2}? ")
    finally:
        timer.cancel()
    return answer


operations = ["+", "-", "*", "/"]
correct_answers = 0
num1_digits = 1
num2_digits = 1

game_on = True

while game_on:

    num1 = random_int(num1_digits)
    num2 = random_int(num2_digits)
    operation = random.choice(operations)

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        while num2 == 0:
            num2 = random_int(num2_digits)
        result = num1 / num2
        result = round(result, 1)

    answer = input_with_timeout()

    if not game_on:
        break
    elif answer == str(result):
        print("Respuesta correcta!")
        correct_answers += 1

        if correct_answers % 5 == 0:
            if correct_answers % 2 == 0:
                num2_digits += 1
            else:
                num1_digits += 1

    else:
        print("Respuesta incorrecta!")
        game_on = False

print(f"Juego finalizado. Has acertado {correct_answers} cálculos.")