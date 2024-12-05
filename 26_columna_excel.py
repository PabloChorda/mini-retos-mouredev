'''
La Columna de Excel
Crea una función que calcule el número de la columna de una hoja de Excel
teniendo en cuenta su nombre.
- Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
- Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
'''

def calculate_column_number(column_name: str) -> int:
    """Calcula el número de la columna de Excel basado en su nombre."""
    column_number = 0
    
    for letter in column_name.upper():
        if not 'A' <= letter <= 'Z':
            raise ValueError("El nombre de la columna debe contener solo letras de A a Z.")
        column_number = column_number * 26 + (ord(letter) - ord('A') + 1)
    
    return column_number

# Ejemplos de prueba
print(calculate_column_number("A"))
print(calculate_column_number("Z"))
print(calculate_column_number("AA"))
print(calculate_column_number("CA"))
print(calculate_column_number("XFD"))
print(calculate_column_number("ZZZZ"))
