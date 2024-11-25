'''
Crea un programa que permita al usuario escribir una historia corta, pero con un giro divertido:
Ciertas palabras serán marcadas con números en el texto, y el programa 
pedirá al usuario que proporcione esas palabras antes de mostrar la historia completa. 
Es como un Mad Libs programado.
'''

def historia_codificada():
    print("¡Bienvenido al creador de historias locas!")
    print("Primero, rellena los espacios en blanco con palabras divertidas.")
    
    # Palabras que el usuario necesita proporcionar
    palabras = {
        "1": input("Ingresa un sustantivo (plural): "),
        "2": input("Ingresa un verbo en infinitivo: "),
        "3": input("Ingresa un adjetivo: "),
        "4": input("Ingresa un nombre propio: "),
        "5": input("Ingresa un lugar: "),
        "6": input("Ingresa un animal: ")
    }
    
    # Historia con marcadores
    historia = """
    Un día, {4} decidió ir a {5}. Allí, se encontró con un grupo de {1} que estaban muy {3}.
    Sin pensarlo mucho, {4} decidió {2} junto a ellos. Pero de repente, apareció un(a) {6} gigante,
    que les gritó: "¡Dejen de {2}, esto es territorio de {6}s!".
    Fue el día más {3} que {4} había vivido.
    """
    
    # Completar la historia con las palabras del usuario
    historia_final = historia.format(**palabras)
    
    print("\n--- TU HISTORIA LOCAMENTE CODIFICADA ---")
    print(historia_final)

# Ejecutar el programa
historia_codificada()
