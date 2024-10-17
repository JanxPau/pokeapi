import requests

base_url = 'https://pokeapi.co/api/v2/'


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    data = response.json()
    return data


def get_pokemon_abilities():
    for ability in pokemon_info['abilities']:
        pokemon_abilities = ability['ability']['name']
        print(pokemon_abilities)


def get_pokemon_image():
    pokemon_image = pokemon_info['sprites']['other']['official-artwork']['front_default']
    print(pokemon_image)


# pokemon = input("Name a pokemon: ")
pokemon = 'charizard'
pokemon_info = get_pokemon_info(pokemon)
print(pokemon_info['id'])
print(pokemon_info['name'])
get_pokemon_abilities()
get_pokemon_image()
