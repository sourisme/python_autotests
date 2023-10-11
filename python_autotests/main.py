import requests

token = 'YOUR TOKEN'
host = 'https://api.pokemonbattle.me:9104'

response_createPokemon = requests.post(f'{host}/pokemons', headers={"Content-Type": "application/json", "trainer_token": token},
                             json={"name": "generate", "photo": "generate"})
get_id_pokemon = response_createPokemon.json()["id"]
print(response_createPokemon.json())

response_changePokemon = requests.put(f'{host}/pokemons', headers={"Content-Type": "application/json", "trainer_token": token},
                             json={"pokemon_id": get_id_pokemon, "name": "generate", "photo": "generate"})
print(response_changePokemon.json())

response_catchPokemon = requests.post(f'{host}/trainers/add_pokeball', headers={"Content-Type": "application/json", "trainer_token": token},
                             json={"pokemon_id": get_id_pokemon})
print(response_catchPokemon.json())