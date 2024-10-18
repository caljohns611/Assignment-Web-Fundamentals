# task 2
import requests
import json

#response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
#json_data = response.text

#pikachu_data = json.loads(json_data)

#print(pikachu_data["name"])
#print(pikachu_data["abilities"])


# task 3

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    pokemon_data.append({
        'name': data['name'],
        'abilities': [ability['ability']['name'] for ability in data['abilities']],
        'weight': data['weight']
    })

average_weight = calculate_average_weight(pokemon_data)

for pokemon in pokemon_data:
    print(f"Name: {pokemon['name']}, Abilities: {', '.join(pokemon['abilities'])}")

print(f"Average weight: {average_weight}")