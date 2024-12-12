'''
Crea una función que encuentre todos los triples pitagóricos
(ternas) menores o iguales a un número dado.
Debes buscar información sobre qué es un triple pitagórico.
La función únicamente recibe el número máximo que puede
aparecer en el triple.
Ejemplo: Los triples menores o iguales a 10 están
formados por (3, 4, 5) y (6, 8, 10).
'''

def pythagorean_triples(max: int) -> list:
    triples = []

    for a in range(1, max + 1):
        for b in range(a, max + 1):
            ab_squared = a**2 + b**2
            c = ab_squared**0.5
            if c > max:
                break
            if c.is_integer(): # ab_squared == int(c)**2
                triples.append((a, b, int(c)))

    return triples

print(pythagorean_triples(9))
print(pythagorean_triples(10))
print(pythagorean_triples(20))