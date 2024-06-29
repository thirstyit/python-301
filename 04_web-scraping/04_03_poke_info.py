# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5
import requests



BASE_URL = "https://pokeapi.co/api/v2/"
POKEMON_SLUG = "pokemon/"

id = [1,2,3,4,5,6]

pokemon_list = []

class Pokemon:
    def __init__(self, id, name, weight, type) -> None:
       self.id = id
       self.name = name
       self.weight = weight
       self.type = type

    def __str__(self):
        return f"Pokemon {self.name} with id {self.id} and types {self.type} has weight {self.weight}"

for i in id:
    req = requests.get(BASE_URL + POKEMON_SLUG + str(i))
    poke_dict = req.json()
    
    idx = poke_dict['id']
    name = poke_dict['name']
    weight = poke_dict['weight']
    type_list = [type['type']['name'] for type in poke_dict['types']]

    p = Pokemon(idx, name, weight, type_list)
    pokemon_list.append(p)

for poke in pokemon_list:
    print(poke)
