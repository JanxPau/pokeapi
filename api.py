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
        print(f'name: {pokemon_abilities}')


def get_pokemon_image():
    pokemon_image = pokemon_info['sprites']['other']['official-artwork']['front_default']
    print(pokemon_image)


def get_pokemon_types():
    for pokemon_type in pokemon_info['types']:
        pokemon_types = pokemon_type['type']['name']
        print(f'type: {pokemon_types}')


def get_pokemon_stats():
    for pokemon_stat in pokemon_info['stats']:
        pokemon_stats = pokemon_stat['stat']['name']
        print(f"{pokemon_stats}: {pokemon_stat['base_stat']}")


# pokemon = input("Name a pokemon: ")
pokemon = 'charizard'
pokemon_info = get_pokemon_info(pokemon)
print(pokemon_info['id'])
print(pokemon_info['name'])
get_pokemon_abilities()
get_pokemon_image()
get_pokemon_types()
# print(type(pokemon_info['stats']))
get_pokemon_stats()
