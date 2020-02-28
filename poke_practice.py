# coding=utf-8

import json

from poke_classes.pokemon import Pokémon
from poke_classes.trainer import Trainer
from poke_classes.complex_encoder import ComplexEncoder

pikachu = {'name': 'Pikachu', 'level': 5}
bulbasaur = {'name': 'Bulbasaur', 'level': 10}
starymie = {'name': 'Starymie', 'level': 7}
psyduck = {'name': 'Psyduck', 'level': 9}

ash = Trainer({
    'name': 'Ash Ketchum',
    'poke_bag': [pikachu, bulbasaur]
})

misty = Trainer({
    'name': 'Misty',
    'poke_bag': [starymie, psyduck]
})

print(ash)
print(ash.to_dict())
print(ash.display_pokemon())

print(misty)
print(misty.to_dict())
print(misty.display_pokemon())

print(json.dumps([ash, misty], cls=ComplexEncoder, indent=4))