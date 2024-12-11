'''
Crea un programa que sea capaz de generar e imprimir todas las 
permutaciones disponibles formadas por las letras de una palabra.
- Las palabras generadas no tienen por qué existir.
- Deben usarse todas las letras en cada permutación.
- Ejemplo: sol, slo, ols, osl, los, lso 
'''

def permutations(word: str) -> list:

    if len(word) <= 1:
        return [word]
    
    result = []

    for index in range(len(word)):

        current_letter = word[index]
        rest_word = word[:index] + word[index+1:]

        for permutation in permutations(rest_word):
            result.append(current_letter + permutation)

    return result

for (index, permutation) in enumerate(permutations("solas")):
    print(f"{index + 1}. {permutation}")