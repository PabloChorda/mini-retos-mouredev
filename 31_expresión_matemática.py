'''
Crea una función que reciba una expresión matemática (String)
y compruebe si es correcta. Retornará true o false.
- Para que una expresión matemática sea correcta debe poseer
  un número, una operación y otro número separados por espacios.
  Tantos números y operaciones como queramos.
- Números positivos, negativos, enteros o decimales.
- Operaciones soportadas: + - * / % 
Ejemplos:
"5 + 6 / 7 - 4" -> true
"5 a 6" -> false
'''

def checkMathExp(expression: str) -> bool:

    components = expression.split(" ")

    if len(components) < 3 or len(components) % 2 == 0:
        return False
    
    check = True

    for index, component in enumerate(components):
        if index % 2 == 0:
            try:
                float(component)
            except:
                check = False
        else:
            check = component in ["+", "-", "*", "/", "%"]

        if not check:
            return False

    return check

print(checkMathExp("3 + 5"))
print(checkMathExp("3 a 5"))
print(checkMathExp("-3 + 5"))
print(checkMathExp("- 3 + 5"))
print(checkMathExp("-3 a 5"))
print(checkMathExp("-3+5"))
print(checkMathExp("3 + 5 - 1 / 4 % 8"))
