import requests

base_url = 'https://pokeapi.co/api/v2/'


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    data = response.json()
    return data


pokemon = input("Name a pokemon: ")
pokemon_info = get_pokemon_info(pokemon)
print(pokemon_info['id'])
print(pokemon_info['name'])
