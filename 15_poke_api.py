"""
POKE_API:
Ahora vamos a obtener información detallada sobre un Pokémon específico 
basado en el nombre o número que ingreses:
"""

import requests

def obtener_datos_pokemon(nombre_o_numero):
    """ 
    Obtiene información detallada de un Pokémon específico.

    Parámetros:
    nombre_o_numero (str o int): Nombre o número del Pokémon a buscar.

    Retorna:
    dict: Información básica del Pokémon.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_numero}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        info_pokemon = {
            "Nombre": data['name'].capitalize(),
            "Número": data['id'],
            "Altura": data['height'],
            "Peso": data['weight'],
            "Tipos": [tipo['type']['name'] for tipo in data['types']]
        }
        return info_pokemon
    else:
        print("Pokémon no encontrado.")
        return None

def main():
    pokemon = input("Introduce el nombre o número del Pokémon que deseas buscar: ")
    info_pokemon = obtener_datos_pokemon(pokemon)
    
    if info_pokemon:
        print("\nInformación del Pokémon:")
        for key, value in info_pokemon.items():
            if key == "Tipos":
                print(f"{key}: {', '.join(value).capitalize()}")
            else:
                print(f"{key}: {value}")

if __name__ == "__main__":
    main()
