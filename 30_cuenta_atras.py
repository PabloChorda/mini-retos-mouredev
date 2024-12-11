'''
Crea una función que reciba dos parámetros para crear una cuenta atrás.
- El primero, representa el número en el que comienza la cuenta.
- El segundo, los segundos que tienen que transcurrir entre cada cuenta.
- Sólo se aceptan números enteros positivos.
- El programa finaliza al llegar a cero.
- Debes imprimir cada número de la cuenta atrás.
'''
import time
import threading

def countdown(start: int, seconds: int):

    if type(start) == int and type(seconds) == int and start > 0 and seconds > 0:
        for number in range(start, -1, -1):
            print(number)
            time.sleep(seconds)
    else:
        raise Exception("Los parámetros tienen que ser enteros positivos")

# Asíncrono
threading.Thread(target=countdown, args=(10, 1)).start()

# Síncrono
# countdown(10, 1)

print("Boom!!! 💥")

