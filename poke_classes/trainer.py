# coding=utf-8

from typing import Dict

from poke_classes.pokemon import Pokémon

class Trainer:

    def __init__(self, trainer_dict: Dict):
        self.name = trainer_dict['name']
        self.poke_bag = []
        for pokemon in trainer_dict['poke_bag']:
            self.poke_bag.append(Pokémon(pokemon))
    
    def __str__(self) -> str:
        return self.name
    
    def display_pokemon(self) -> str:
        display_pokemon = [f"{pokemon.__str__()} ({pokemon.level})" for pokemon in self.poke_bag]
        return  ", ".join(display_pokemon)
    
    def to_dict(self) -> Dict:
        return self.__dict__