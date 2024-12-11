'''
Crea una función que encuentre todas las combinaciones de los números
de una lista que suman el valor objetivo.
- La función recibirá una lista de números enteros positivos
  y un valor objetivo.
- Para obtener las combinaciones sólo se puede usar
  una vez cada elemento de la lista (pero pueden existir
  elementos repetidos en ella).
- Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
  Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
  (Si no existen combinaciones, retornar una lista vacía)
'''

def find_sums(numbers: list, target: int) -> list:

    def find_sum(start: int, target: int, combination: list):

        # Solución encontrada
        if target == 0:
            result.append(combination[:])
            return
    
        # No posee solución
        if target < 0 or start == len(numbers):
            return
    
        # Búsqueda
        for index in range(start, len(numbers)):

            if index > start and numbers[index] == numbers[index - 1]:
                continue

            combination.append(numbers[index])
            find_sum(index + 1, target - numbers[index], combination)
            combination.pop()

    numbers.sort()
    result = []
    find_sum(0, target, [])
    return result

print(find_sums([1, 5, 3, 2], 6))
print(find_sums([1, 2, 1, 1, 1, 1, 2, 1], 6))